"""Exercise 01: class, object and methods."""


class Progress:
    """Store progress and calculate its completion percentage."""

    def __init__(self, completed: int, total: int):
        if total < 1:
            raise ValueError("total must be positive")
        if completed < 0:
            raise ValueError("completed cannot be negative")
        self.completed = completed
        self.total = total

    def percentage(self) -> float:
        return self.completed / self.total * 100

    def __str__(self) -> str:
        return f"Progress: {self.completed}/{self.total} ({self.percentage():.0f}%)"


def main() -> None:
    progress = Progress(3, 4)
    print(progress.percentage())
    print(progress)


if __name__ == "__main__":
    main()
