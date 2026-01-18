from copy import deepcopy
from api.utils.security import SENSITIVE_FIELDS

MASK = "***"


def sanitize_dict(data: dict | None) -> dict | None:
    if not isinstance(data, dict):
        return data

    clean = deepcopy(data)

    for key in clean:
        if key.lower() in SENSITIVE_FIELDS:
            clean[key] = MASK

    return clean