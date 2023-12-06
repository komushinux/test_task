import re


class VerifyError(Exception):
    """
    Custom exception class for verification errors.

    Attributes:
        exp (list): List of error expressions found during verification.
    """

    def __init__(self, exp):
        self.exp = exp

    def __str__(self):
        error_messages = "\n".join([f"{err}" for err in self.exp])
        return f"Errors in text:\n {error_messages}"


def verify_data(test_text, list_keys):
    """
    Verify the data in the provided text using a list of keys.

    Args:
        test_text (str): The text to be verified.
        list_keys (list): List of keys to be used for verification.

    Returns:
        str: The verified text.

    Raises:
        VerifyError: If verification errors are found, raises an exception with details.
    """
    try:
        errors = []
        local_text = test_text
        matches = [key for key in list_keys if key.lower() in local_text.lower()]
        wrong_indexes = []
        for key in matches:
            index = local_text.lower().index(key)
            if local_text[index - 1] != '{' and local_text[index + len(key)] != '}':
                errors.append(f"{local_text[index:index + len(key)]}")
                index = local_text.lower().index(key)
                wrong_indexes.append(index)

            elif index == 0 or (index > 0 and local_text[index - 1] != '{'):
                errors.append(f"{local_text[index:index + len(key)]}{'}'}")
                if index == 0:
                    local_text = '{' + local_text
                else:
                    local_text = local_text[:index] + '{' + local_text[index:]
                index = local_text.lower().index(key)
                wrong_indexes.append(index)

            elif (index + len(key) == len(local_text) or
                  (index + len(key) < len(local_text) and local_text[index + len(key)] != '}')):
                errors.append(f"{'{'}{local_text[index:index + len(key)]}")
                if index + len(key) == len(local_text):
                    local_text = local_text + '}'
                else:
                    local_text = local_text[:index + len(key)] + '}' + local_text[index + len(key):]
                index = local_text.lower().index(key)
                wrong_indexes.append(index)

        pattern = re.compile(r'\{([^}]*)\}')
        matches = pattern.findall(local_text)
        for key in matches:
            if key not in list_keys and local_text.index(key) not in wrong_indexes:
                errors.append(f"{'{'}{key}{'}'}")
        if errors:
            raise VerifyError(errors)
        return test_text
    except VerifyError as err:
        return err


if __name__ == '__main__':
    with open("./input/text.txt", "r") as file:
        text = file.read()
    with open("./input/list_keys.txt", "r") as file:
        keys = list(file.read().split(" "))
    print(verify_data(text, keys))
