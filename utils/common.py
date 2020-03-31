def get_start_end_by_page_info(page, page_size):
    start = (page - 1) * page_size
    end = page * page_size
    return start, end


def get_total_page(total_num, page_size):
    if total_num % page_size == 0:
        return int(total_num / page_size)
    return int(total_num / page_size) + 1
