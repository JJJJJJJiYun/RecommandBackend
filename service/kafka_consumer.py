import json
import traceback

from utils.kafka import consumer
from utils.redis import redis
from utils.redis_key import key_of_user_rating_data


def consume_user_action():
    for message in consumer:
        try:
            print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                                 message.offset, message.key,
                                                 message.value))
            action_info = json.loads(message.value)
            key = key_of_user_rating_data(action_info['user_id'])
            old_score = redis.zscore(key, action_info['item_id'])
            old_score = old_score if old_score else 0
            redis.zadd(key, {action_info['item_id']: old_score + action_info['score']})
        except:
            traceback.print_exc()
