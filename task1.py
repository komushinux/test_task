import re


class VerifyError(Exception):
    def __init__(self, exp):
        self.exp = exp

    def __str__(self):
        error_messages = "\n".join([f"{err}" for err in self.exp])
        return f"Errors in text:\n {error_messages}"


def verify_data(test_text, list_keys):
    try:
        errors = []
        local_test = test_text
        matches = [key for key in list_keys if key.lower() in local_test.lower()]
        wrong_indexes = []
        for key in matches:
            index = local_test.lower().index(key)
            if local_test[index - 1] != '{' and local_test[index + len(key)] != '}':
                errors.append(f"{local_test[index:index + len(key)]}")
                index = local_test.lower().index(key)
                wrong_indexes.append(index)

            elif index == 0 or (index > 0 and local_test[index - 1] != '{'):
                errors.append(f"{local_test[index:index + len(key)]}{'}'}")
                if index == 0:
                    local_test = '{' + local_test
                else:
                    local_test = local_test[:index] + '{' + local_test[index:]
                index = local_test.lower().index(key)
                wrong_indexes.append(index)

            elif (index + len(key) == len(local_test) or
                  (index + len(key) < len(local_test) and local_test[index + len(key)] != '}')):
                errors.append(f"{'{'}{local_test[index:index + len(key)]}")
                if index + len(key) == len(local_test):
                    local_test = local_test + '}'
                else:
                    local_test = local_test[:index + len(key)] + '}' + local_test[index + len(key):]
                index = local_test.lower().index(key)
                wrong_indexes.append(index)

        pattern = re.compile(r'\{([^}]*)\}')
        matches = pattern.findall(local_test)
        for key in matches:
            if key not in list_keys and local_test.index(key) not in wrong_indexes:
                errors.append(f"{'{'}{key}{'}'}")
        if errors:
            raise VerifyError(errors)
        return test_text
    except VerifyError as err:
        return err


if __name__ == '__main__':
    with open("./input/text.txt", "r") as file:
        Test_text = file.read()
    with open("./input/list_keys.txt", "r") as file:
        List_keys = list(file.read().split(" "))

    print(verify_data(Test_text, List_keys))
