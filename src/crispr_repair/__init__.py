from .operate import Elong, Skip
from .record import Records
from .score import PropScore, ZeroScore
from .state import State


def local(query: str, ref: str):
    records = Records(_records={})
    skip = Skip(skip_score=PropScore(unit=0))
    elong = Elong(elong_score=ZeroScore())

    # initial state
    records.set(state=State(ref_state=None, qpos=0), score=0)

    # elongation start states
    for rpos in range(len(ref) + 1):
        records.update(
            operate=lambda state, rpos=rpos: skip(state, rpos),
            state=State(ref_state=None, qpos=0),
        )

    # elongation states
    for rpos in range(len(ref) + 1):
        pass
