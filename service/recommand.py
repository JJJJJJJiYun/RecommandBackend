import sys

from utils.common import get_start_end_by_page_info, get_total_page
from utils.redis import redis
from utils.redis_key import *


def recommand(user_id, page, page_size):
    """推荐"""
    try:
        start, end = get_start_end_by_page_info(page, page_size)
        # 看缓存池里有没有
        if redis.exists(key_of_user_recommand_result(user_id)):
            result = redis.zrevrange(key_of_user_recommand_result(user_id), 0, -1)
            return result, len(result), get_total_page(len(result), page_size)
        user_cf_item_score_list = redis.zrevrange(key_of_user_cf_user_item_interest(user_id), 0, -1, withscores=True)
        item_cf_item_score_list = redis.zrevrange(key_of_item_cf_user_item_interest(user_id), 0, -1, withscores=True)
        # 如果 user_cf 没有结果，返回默认推荐
        if len(user_cf_item_score_list) == 0:
            result = redis.smembers(key_of_default_recommand_result())[start:end]
            return result, len(result), get_total_page(len(result), page_size)
        # 如果 item_cf 没有结果，返回 user_cf 的推荐
        if len(item_cf_item_score_list) == 0:
            return [item for item, _ in user_cf_item_score_list[start:end]], len(
                user_cf_item_score_list), get_total_page(
                len(user_cf_item_score_list), page_size)
        # 计算混合推荐结果
        item_cf_item_score_dict = {item: score for item, score in item_cf_item_score_list}
        item_score_dict = dict()
        for item, score in user_cf_item_score_list:
            item_score_dict[item] = (score + (
                item_cf_item_score_dict[item] if item in item_cf_item_score_dict else 0)) / 2
        redis.zadd(key_of_user_recommand_result(user_id), item_score_dict)
        redis.expire(key_of_user_recommand_result(user_id), 60 * 60)
        result = redis.zrevrange(key_of_user_recommand_result(user_id), 0, -1)
        return result, len(result), get_total_page(len(result), page_size)
    except:
        print("recommand err:", sys.exc_info()[0])
        raise


def set_default_recommand_items(items):
    """设置默认推荐"""
    try:
        redis.sadd(key_of_default_recommand_result(), items)
    except:
        print("set default recommand items err:", sys.exc_info()[0])
        raise
