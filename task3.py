from input.task3_input import Json_old, Json_new, diff_lst


def find_json_diff(json_old, json_new, diff_list):
    result = {}

    def compare_objects(old_obj, new_obj, path):
        for key in old_obj:
            new_key = path + [key]

            if isinstance(old_obj[key], dict) and key in new_obj and isinstance(new_obj[key], dict):
                compare_objects(old_obj[key], new_obj[key], new_key)
            elif key in new_obj and old_obj[key] != new_obj[key] and key in diff_list:
                result[tuple(new_key)] = new_obj[key]

    compare_objects(json_old, json_new, [])
    return {key[-1]: result[key] for key in result}


if __name__ == '__main__':
    res = find_json_diff(Json_old, Json_new, diff_lst)
    print("Result:", res)
