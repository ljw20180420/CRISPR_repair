from dataclasses import dataclass
from typing import Callable

from .state import State


@dataclass
class Record:
    max_score: int | None
    sources: list[State | tuple[State, State]]
    """Record the maximal score of a state (pair) and the sources of the maximal score.

    Args:
        max_score: the maximal score of a state (pair).
        sources: list of operate and source state (pair) that leads to the maximal score.
    """


@dataclass
class Records:
    _records: dict[State | tuple[State, State], Record]

    def set(self, state: State | tuple[State, State], score: int):
        self._records[state] = Record(max_score=score, sources=[])

    def update(
        self,
        operate: Callable[
            [State | tuple[State, State]], tuple[State | tuple[State, State], int]
        ],
        state: State | tuple[State, State],
    ) -> None:
        new_state, delta_score = operate(state)
        new_score = self._records[state].max_score + delta_score

        record = self._records.get(new_state, Record(max_score=None, sources=[]))
        if record.max_score is None or record.max_score < new_score:
            record.max_score = new_score
            record.sources = [state]
        elif record.max_score == new_score:
            record.sources.append(state)
        self._records[new_state] = record
