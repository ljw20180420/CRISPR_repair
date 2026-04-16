from dataclasses import replace
from typing import Callable

from .state import RefState, State


class Skip:
    def __init__(self, skip_score: Callable[[int], int]) -> None:
        self.skip_score = skip_score

    def __call__(self, state: State, rpos: int) -> tuple[State, int]:
        delta_score = self.skip_score(rpos)
        new_state = State(
            ref_state=RefState(cis=True, forward=True, rpos=rpos, elong=False),
            qpos=0,
        )

        return new_state, delta_score


class Elong:
    def __init__(self, elong_score: Callable[[], int]) -> None:
        self.elong_score = elong_score

    def __call__(self, state: State) -> tuple[State, int]:
        delta_score = self.elong_score()
        new_state = replace(state, ref_state=replace(state.ref_state, elong=True))

        return new_state, delta_score


class Match:
    def __init__(self, match_score: Callable[[int, int], int]) -> None:
        self.match_score = match_score

    def __call__(self, state: State) -> tuple[State, int]:
        delta_score = self.match_score(state.ref_state.rpos, state.qpos)
        new_state = replace(
            state,
            ref_state=replace(state.ref_state, rpos=state.ref_state.rpos + 1),
            qpos=state.qpos + 1,
        )

        return new_state, delta_score


class Junc:
    def __init__(
        self,
        query_len: int,
        gap_score: Callable[[int], int],
        anneal_score: Callable[[int], int],
    ):
        self.query_len = query_len
        self.gap_score = gap_score
        self.anneal_score = anneal_score

    def __call__(self, state1: State, state2: State) -> tuple[State, State, int]:
        if state1.qpos + state2.qpos > self.query_len:
            delta_score = self.anneal_score(state1.qpos + state2.qpos - self.query_len)
        else:
            delta_score = self.gap_score(self.query_len - state1.qpos - state2.qpos)

        new_state = State(ref_state=None, qpos=-1)

        return new_state, delta_score


# TODO: infer mh from state
class Melt:
    def __init__(self, melt_score: Callable[[int], int]):
        self.melt_score = melt_score
