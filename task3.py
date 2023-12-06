from input.task3_input import old, new, diff


def find_json_diff(json_old, json_new, diff_list):
    """
    Find differences between two JSON objects based on a specified list of keys.

    Args:
        json_old (dict): The old JSON object for comparison.
        json_new (dict): The new JSON object for comparison.
        diff_list (list): A list of keys to consider for detecting differences.

    Returns:
        dict: A dictionary containing the differences between the old and new JSON objects,
              where keys are the differing keys and values are the corresponding new values.
    """
    result = {}

    def compare_objects(old_obj, new_obj, path):
        """
        Recursively compare two JSON objects and identify differences.

        Args:
            old_obj (dict): The old JSON object for comparison.
            new_obj (dict): The new JSON object for comparison.
            path (list): The current path in the JSON structure.

        Returns:
            None
        """
        for key in old_obj:
            new_key = path + [key]

            if isinstance(old_obj[key], dict) and key in new_obj and isinstance(new_obj[key], dict):
                compare_objects(old_obj[key], new_obj[key], new_key)
            elif key in new_obj and old_obj[key] != new_obj[key] and key in diff_list:
                result[tuple(new_key)] = new_obj[key]

    compare_objects(json_old, json_new, [])
    return {key[-1]: result[key] for key in result}


if __name__ == '__main__':
    res = find_json_diff(old, new, diff)
    print("Result:", res)
