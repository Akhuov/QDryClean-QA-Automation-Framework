
def is_subset(actual: dict, expected: dict) -> bool:
    for key, expected_value in expected.items():
        if key not in actual:
            return False
        if actual[key] != expected_value:
            return False
    return True