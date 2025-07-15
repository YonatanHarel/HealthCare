import copy
import functools
import json
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()


def load_json_file(filepath: str):
    with open(filepath, "r", encoding='utf-8') as f:
        return json.load(f)


def mask_sensitive_data(data):
    if isinstance(data, dict):
        masked = {}
        for k, v in data.items():
            if k in ("patient_id", "scan_id") and isinstance(v, str):
                masked[k] = "*" * (len(v) - 4) + v[-4:]
            else:
                masked[k] = mask_sensitive_data(v)
        return masked
    elif isinstance(data, list):
        return [mask_sensitive_data(item) for item in data]
    else:
        return data


def mask_and_log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_copy = copy.deepcopy(args)
        masked_args = mask_sensitive_data(args_copy)

        print(f"Input args: {masked_args}")
        result = func(*args, **kwargs)
        masked_result = mask_sensitive_data(copy.deepcopy(result))
        print(f"Output: {masked_result}")
        return result
    return wrapper


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logger.info(f"function {func.__name__} called with arguments: {mask_sensitive_data(copy.deepcopy(result))}")
            return result
        except Exception as e:
            logger.exception(f"Exception raised in {func.__name__}. exception: {str(e)}")
            raise e

    return wrapper


# @mask_and_log
@log
def process_patient_data(data):
    # print("handling")
    return {
        "status": "OK",
        "patient_id": data["patient_id"],
        "scan_id": data["scan_id"]
    }


def handle_batch_data(batch_data):
    for data in batch_data:
        process_patient_data(data)


if __name__ == '__main__':
    filepath = "patient_scan_10.json"
    batch_data = load_json_file(filepath)

    handle_batch_data(batch_data)
