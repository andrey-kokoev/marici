"""Typed positroid-cell targets for the NNMHV history triangulation."""
from dataclasses import dataclass
from nnmhv_coherence_paths import compile_nnmhv_histories

@dataclass(frozen=True)
class PositroidCell:
    n:int
    k:int
    affine_permutation:tuple
    grassmann_necklace:tuple
    dimension:int
    history_index:int|None=None


def top_cell(k,n,history_index=None):
    """Top cell of G_+(k,n), in bounded-affine permutation convention."""
    perm=tuple(i+k for i in range(1,n+1))
    necklace=tuple(tuple((a+j-1)%n+1 for j in range(k)) for a in range(1,n+1))
    return PositroidCell(n,k,perm,necklace,k*(n-k),history_index)


def nnmhv_cell_requests(n):
    """BCFW history records requiring graph/permutation compilation."""
    return tuple({'history_index':j,'outer_pair':h.outer_pair,'inner_pair':h.inner_pair,
                  'branch':h.branch,'boundary_updates':tuple((u.side,u.replacement_path) for u in h.boundary_updates),
                  'target_k':2,'target_dimension':8,'status':'requires_on_shell_graph'}
                 for j,h in enumerate(compile_nnmhv_histories(n)))
