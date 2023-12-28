class InvalidWorldError(ValueError):
    "World is invalid"

    def __init__(self, world: str, group: list) -> None:
        super().__init__(f"{world} is invalid. Expected: {group}")


class TooManyRequestsError(Exception):
    "Too many requests: Try again with after significant amount of time"

    def __init__(self) -> None:
        super().__init__("No more request is avaliable at the day. Please try again after next 00:00+09:00 (Midnight KST/JST) comes.")
