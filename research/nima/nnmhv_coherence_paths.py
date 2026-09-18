"""Compile the sourced all-n NNMHV nested sum into coherence histories."""
from dataclasses import dataclass


@dataclass(frozen=True)
class BoundaryUpdate:
    side: str                 # lower or upper
    replacement_path: tuple  # source superscript labels


@dataclass(frozen=True)
class TransportedSpinor:
    """A covector represented by its starting spinor and x-matrix path."""
    vertices: tuple

    @property
    def start(self): return self.vertices[0]

    @property
    def matrix_edges(self): return tuple(zip(self.vertices,self.vertices[1:]))

    @property
    def is_external(self): return len(self.vertices)==1


@dataclass(frozen=True)
class TerminalRState:
    xi: TransportedSpinor
    lower_spinor: TransportedSpinor
    upper_spinor: TransportedSpinor


@dataclass(frozen=True)
class NNMHVHistory:
    n: int
    outer_pair: tuple
    inner_pair: tuple
    branch: str              # left-nested or right-nested
    inner_prefix: tuple      # empty or (b1,a1)
    boundary_updates: tuple

    @property
    def phases(self):
        return (('R', self.outer_pair), ('R', self.inner_prefix, self.inner_pair))


def _ordered_pairs(lower, upper, minimum_gap=1):
    return tuple((a,b) for a in range(lower,upper+1)
                 for b in range(a+minimum_gap,upper+1))


def terminal_r_state(history):
    """Apply Lrep/Urep and return the terminal generalized-R spinor state."""
    a,b=history.inner_pair
    xi=TransportedSpinor((history.n,)+history.inner_prefix)
    lower=TransportedSpinor((a-1,))
    upper=TransportedSpinor((b,))
    for update in history.boundary_updates:
        replacement=TransportedSpinor((history.n,)+update.replacement_path)
        if update.side=='lower': lower=replacement
        elif update.side=='upper': upper=replacement
        else: raise ValueError(f'unknown boundary side {update.side}')
    return TerminalRState(xi,lower,upper)


def supports_component_23(history):
    """Exact generic support criterion for product_A eta_2^A eta_3^A."""
    return (history.branch=='left-nested' and history.outer_pair[0]==2
            and history.inner_pair[0]==3)


def compile_nnmhv_histories(n):
    """Compile equation PNNMHVnew, retaining its boundary terms.

    Every last pair obeys the source convention a<b-1. Boundary updates
    replace endpoint spinors but do not relax this separation condition.
    """
    if n < 6:
        return ()
    histories=[]
    for a1,b1 in _ordered_pairs(2,n-1,2):
        # First nested sum: a1+1 <= a2 < b2 <= b1, upper superscript a1,b1.
        for a2,b2 in _ordered_pairs(a1+1,b1,2):
            updates=(() if b2!=b1 else (BoundaryUpdate('upper',(a1,b1)),))
            histories.append(NNMHVHistory(n,(a1,b1),(a2,b2),'left-nested',(b1,a1),updates))
        # Second nested sum: b1 <= a2 < b2 <= n-1, lower superscript a1,b1.
        for a2,b2 in _ordered_pairs(b1,n-1,2):
            updates=(() if a2!=b1 else (BoundaryUpdate('lower',(a1,b1)),))
            histories.append(NNMHVHistory(n,(a1,b1),(a2,b2),'right-nested',(),updates))
    return tuple(histories)
