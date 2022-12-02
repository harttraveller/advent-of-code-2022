from typing import Tuple, List
from rich.console import Console


trans = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

base = {"rock": 1, "paper": 2, "scissors": 3}


def load_text() -> List[List[str]]:
    return [i.split() for i in open("input.txt").read().split("\n") if i.strip() != ""]


def compute_outcome(op: str, me: str) -> Tuple[int]:
    op, me = trans[op], trans[me]
    if op == me:
        return (3, 3)
    elif op == "rock" and me == "paper":
        return (0, 6)
    elif op == "paper" and me == "scissors":
        return (0, 6)
    elif op == "scissors" and me == "rock":
        return (0, 6)
    elif op == "rock" and me == "scissors":
        return (6, 0)
    elif op == "paper" and me == "rock":
        return (6, 0)
    elif op == "scissors" and me == "paper":
        return (6, 0)
    else:
        raise Exception()


def compute_score(op: str, me: str) -> Tuple[int]:
    op_base, me_base = base[trans[op]], base[trans[me]]
    op_add, me_add = compute_outcome(op, me)
    op_total = op_base + op_add
    me_total = me_base + me_add
    return (op_total, me_total)


def compute_scores(data: List[List[str]]):
    scores = list()
    for i in data:
        scores.append(compute_score(i[0], i[1]))
    return scores


def compute_my_score(scores: List[Tuple[int]]) -> int:
    return sum([i[1] for i in scores])


def main():
    data = load_text()
    scores = compute_scores(data)
    return compute_my_score(scores)


if __name__ == "__main__":
    Console().print(main())
