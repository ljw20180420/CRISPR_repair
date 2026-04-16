from dataclasses import dataclass


@dataclass(frozen=True)
class RefState:
    cis: bool
    forward: bool
    rpos: int
    elong: bool
    """The reference state of single side of DSB.

    Args:
        cis: whether the annealing is cis.
        forward: whether the annealing is forward.
        rpos: the annealing position in reference.
        elong: whether the elongation is ready.
    """


@dataclass(frozen=True)
class State:
    ref_state: RefState | None
    qpos: int | None
    """The state of single side of DSB.

    Args:
        ref_state: the reference state of single side of DSB.
        qpos: the annealing position in query.
    """
