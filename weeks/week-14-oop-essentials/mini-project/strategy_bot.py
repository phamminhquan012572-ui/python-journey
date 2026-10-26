"""Week 14 mini-project: swap bot strategies using composition."""

from collections.abc import Callable

State = dict[str, int]
Strategy = Callable[[State], str]


class Bot:
    """A bot delegates its action choice to a replaceable strategy."""

    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def choose_action(self, state: State) -> str:
        return self.strategy(state)


def move_toward_goal(state: State) -> str:
    position = state["position"]
    goal = state["goal"]

    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def defensive(state: State) -> str:
    opponent = state.get("opponent_position")
    if opponent is not None and abs(opponent - state["position"]) <= 1:
        return "wait"
    return move_toward_goal(state)


def balanced(state: State) -> str:
    return move_toward_goal(state)


def aggressive(state: State) -> str:
    return move_toward_goal(state)


def main() -> None:
    states = [
        {"position": 1, "opponent_position": 4, "goal": 4},
        {"position": 3, "opponent_position": 4, "goal": 0},
    ]
    strategies: tuple[tuple[str, Strategy], ...] = (
        ("defensive", defensive),
        ("balanced", balanced),
        ("aggressive", aggressive),
    )

    for state in states:
        print(f"State: {state}")
        for name, strategy in strategies:
            bot = Bot(strategy)
            print(f"  {name}: {bot.choose_action(state)}")


if __name__ == "__main__":
    main()
