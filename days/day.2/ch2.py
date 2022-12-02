#%%
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
"""
X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
"""

choice = {
    "rock": {"X": "scissors", "Y": "rock", "Z": "paper"},
    "paper": {"X": "rock", "Y": "paper", "Z": "scissors"},
    "scissors": {"X": "paper", "Y": "scissors", "Z": "rock"},
}
base = {"rock": 1, "paper": 2, "scissors": 3}


def load_text() -> List[List[str]]:
    return [i.split() for i in open("input.txt").read().split("\n") if i.strip() != ""]


def choices(op: str, me: str) -> Tuple[str, str]:
    opc = trans[op]
    mec = choice[opc][me]
    return opc, mec


def compute_outcome(op: str, me: str) -> Tuple[int]:
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
    opc, mec = choices(op, me)
    ops, mes = compute_outcome(opc, mec)
    ops = base[opc] + ops
    mes = base[mec] + mes
    return (ops, mes)


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


#%%
if __name__ == "__main__":
    Console().print(main())
