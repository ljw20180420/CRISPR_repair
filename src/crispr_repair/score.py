from abc import ABC, abstractmethod

from Bio import Seq

from .state import State


class BaseScore(ABC):
    @abstractmethod
    def __call__(self, old_state: State, new_state: State) -> int:
        """Return score from state."""


class ConstScore(BaseScore):
    def __init__(self, const: int) -> None:
        self.const = const

    def __call__(self, old_state: State, new_state: State) -> int:
        return self.const


class SkipScore:
    def __init__(self, unit: int) -> None:
        self.unit = unit

    def __call__(self, old_state: State, new_state: State) -> int:
        return self.unit * new_state.rpos


class MatchScore:
    def __init__(
        self,
        query: str,
        ref_cis: str,
        ref_trans: str,
        match_score: int,
        mismatch_score: int,
    ) -> None:
        self.query_cis = query
        self.query_trans = str(Seq.Seq(query).reverse_complement)
        self.ref_cis = ref_cis
        self.ref_trans = ref_trans
        self.match_score = match_score
        self.mismatch_score = mismatch_score

    def __call__(self, old_state: State, new_state: State) -> int:
        qbase = self.query[old_state.qpos]
        if old_state.ref_state.cis and old_state.ref_state.forward:
            ref = self.ref_cis
        elif old_state.ref_state.cis and not old_state.ref_state.forward:
            ref = self.query_trans
        elif not old_state.ref_state.cis and old_state.ref_state.forward:
            ref = self.query_cis
        else:
            ref = self.ref_trans
        rbase = ref[old_state.ref_state.rpos]

        if qbase == rbase:
            return self.match_score
        return self.mismatch_score


class CrossCutPenaltyScore:
    def __init__(
        self, cut_cis: int, coff_cis: int, cut_trans: int, coff_trans: int
    ) -> None:
        self.cut_cis = cut_cis
        self.coff_cis = coff_cis
        self.cut_trans = cut_trans
        self.coff_trans = coff_trans

    def __call__(self, old_state: State, new_state: State) -> int:
        # cis reverse
        if old_state.ref_state.cis and not old_state.ref_state.forward:
            return 0

        # trans forward
        if not old_state.ref_state.cis and old_state.ref_state.forward:
            return 0

        if old_state.ref_state.cis and old_state.ref_state.forward:
            cut = self.cut_cis
            coff = self.coff_cis
        else:
            cut = self.cut_trans
            coff = self.coff_trans

        penalty = 0
        for rpos in range(old_state.ref_state.rpos + 1, new_state.ref_state.rpos + 1):
            if rpos <= cut:
                continue
            penalty += (rpos - cut) * coff

        return penalty
