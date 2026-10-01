"""Audit the Postnikov tower's branching kernels and their displacement images.

For each tower level:
  1. Extract the projection matrix A_n: F_n -> C_{n-1} (step_decoder)
  2. Compute a basis for ker(A_n) — the sibling-branching subspace
  3. Compute D(ker(A_n)) — the image of the branching directions under displacement
  4. Report:
       dim ker(A_n)         = total branching dimension
       rank D(ker(A_n))     = spatially visible branching dimensions
       dim ker(A_n)∩ker(D) = spatially invisible branching dimensions
       concrete basis vectors for both visible and invisible subspaces
"""
from fractions import Fraction as F
from collections import defaultdict
import json
from pathlib import Path

from retained_path_successor import RetainedSuccessorLedger, apply, identity, zero
from check_natural_tower_return import PACKETS, mm, transpose, add, scale
from photon_native_spatial_step import VERTICES


LABELS = tuple(p[0] for p in PACKETS)


# ── Row-reduction utilities ──────────────────────────────────────────

def nullspace_basis(matrix):
    """Return a list of basis vectors for the kernel of a matrix over Q.

    Each basis vector is a tuple of Fractions of length = n_cols.
    Returns [] if kernel is trivial.
    """
    n_rows = len(matrix)
    n_cols = len(matrix[0])
    # Augment: [A | 0], storing column indices
    aug = [list(row) + [F(0)] for row in matrix]
    pivot_col_of_row = [-1] * n_rows  # which column is the pivot of each row

    row = 0
    for col in range(n_cols):
        pivot = None
        for r in range(row, n_rows):
            if aug[r][col] != F(0):
                pivot = r
                break
        if pivot is None:
            continue
        aug[row], aug[pivot] = aug[pivot], aug[row]
        pv = aug[row][col]
        aug[row] = [x / pv for x in aug[row]]
        for r in range(n_rows):
            if r != row and aug[r][col] != F(0):
                factor = aug[r][col]
                aug[r] = [x - factor * y for x, y in zip(aug[r], aug[row])]
        pivot_col_of_row[row] = col
        row += 1
        if row >= n_rows:
            break

    rank = row
    pivot_cols = set(pivot_col_of_row[:rank])
    free_cols = [c for c in range(n_cols) if c not in pivot_cols]

    # Extract the RREF to find nullspace basis
    # For each free column, set it to 1, solve for pivot columns
    basis = []
    for free_col in free_cols:
        vec = [F(0)] * n_cols
        vec[free_col] = F(1)
        for r in range(rank):
            # The RREF row r has pivot at pivot_col_of_row[r]
            # The equation is: x_pivot + sum(free * coefficient) = 0
            # So x_pivot = -sum(free * coefficient)
            pivot_col = pivot_col_of_row[r]
            vec[pivot_col] = -aug[r][free_col]
        basis.append(tuple(vec))

    return basis


def apply_matrix_to_vectors(mat, vectors):
    """Apply matrix to each vector in a list; return list of image vectors."""
    result = []
    for vec in vectors:
        img = tuple(sum(mat[axis][j] * vec[j] for j in range(len(vec)))
                     for axis in range(len(mat)))
        result.append(img)
    return result


def displacement_matrix(stage):
    """Build 3 x N displacement matrix for paths in a stage."""
    paths = stage.paths
    D_matrix = []
    for axis in range(3):
        row = []
        for path in paths:
            src = path[0][0]  # source vertex label of first primitive
            tgt = path[-1][1]  # target vertex label of last primitive
            diff = VERTICES[tgt][axis] - VERTICES[src][axis]
            row.append(F(diff))
        D_matrix.append(tuple(row))
    return tuple(D_matrix)


def rank_of_span(vectors, dim):
    """Row-reduce vectors (as rows of a matrix) to find rank."""
    if not vectors:
        return 0, []
    # Each row is one vector; row-reduce
    aug = [list(v) + [F(0)] for v in vectors]
    n_rows = len(aug)
    n_cols = dim

    row = 0
    for col in range(n_cols):
        pivot = None
        for r in range(row, n_rows):
            if aug[r][col] != F(0):
                pivot = r
                break
        if pivot is None:
            continue
        aug[row], aug[pivot] = aug[pivot], aug[row]
        pv = aug[row][col]
        aug[row] = [x / pv for x in aug[row]]
        for r in range(n_rows):
            if r != row and aug[r][col] != F(0):
                factor = aug[r][col]
                aug[r] = [x - factor * y for x, y in zip(aug[r], aug[row])]
        row += 1
        if row >= n_rows:
            break
    return row, aug  # rank


def format_vector(vec):
    return [str(x) for x in vec]


# ── Main ─────────────────────────────────────────────────────────────

def main():
    # Build tower
    ledger = RetainedSuccessorLedger(PACKETS)
    root = ledger.root
    tower = [root]
    for _ in range(4):
        tower.append(ledger.successor(tower[-1]))

    results = {'tower_levels': {}}

    for depth in range(1, len(tower)):  # depth 1,2,3,4
        stage = tower[depth]
        parent_stage = tower[depth - 1]
        n_paths = len(stage.paths)
        n_parents = len(parent_stage.paths)
        decoder = stage.step_decoder

        # Compute kernel basis
        K_basis = nullspace_basis(decoder)
        k_dim = len(K_basis)

        # Displacement matrix
        D_mat = displacement_matrix(stage)
        D_images = apply_matrix_to_vectors(D_mat, K_basis)

        # Rank of D(K)
        if D_images:
            vis_rank, _ = rank_of_span(D_images, 3)
        else:
            vis_rank = 0

        inv_dim = k_dim - vis_rank

        # Find invisible basis vectors (those with D(v)=0)
        inv_basis = []
        vis_basis = []
        for v, dv in zip(K_basis, D_images):
            if all(x == F(0) for x in dv):
                inv_basis.append(v)
            else:
                vis_basis.append((v, dv))

        results['tower_levels'][f'depth_{depth}'] = {
            'n_paths': n_paths,
            'n_parents': n_parents,
            'kernel_dim': k_dim,
            'displacement_rank': vis_rank,
            'invisible_dim': inv_dim,
            'visible_dim': vis_rank,
        }

        # Store examples
        if inv_basis:
            results['tower_levels'][f'depth_{depth}']['invisible_examples'] = [
                {'vector': format_vector(v)} for v in inv_basis[:4]
            ]
        if vis_basis:
            results['tower_levels'][f'depth_{depth}']['visible_examples'] = [
                {'vector': format_vector(v), 'displacement': format_vector(dv)}
                for v, dv in vis_basis[:4]
            ]

        print(f'depth {depth}:')
        print(f'  paths={n_paths}, parents={n_parents}')
        print(f'  kernel dim = {k_dim}')
        print(f'  visible dim (rank D(K)) = {vis_rank}')
        print(f'  invisible dim = {inv_dim}')
        if inv_basis:
            print(f'  invisible examples:')
            for v in inv_basis[:3]:
                # Show which paths have nonzero coefficients
                nonzero = [(i, x) for i, x in enumerate(v) if x != F(0)]
                desc = ', '.join(f'{stage.paths[i][0][2]}'
                                 f'->{stage.paths[i][-1][1]}'  # simplify
                                 for i, x in nonzero[:6])
                print(f'    {len(nonzero)} nonzero entries: {desc}')
        if vis_basis:
            print(f'  visible examples:')
            for v, dv in vis_basis[:3]:
                nonzero = [(i, x) for i, x in enumerate(v) if x != F(0)]
                desc = ', '.join(f'{stage.paths[i][0][2]}->{stage.paths[i][-1][1]}'
                                for i, x in nonzero[:6])
                print(f'    disp={dv}: {desc}')
        print()

    # ── Save ─────────────────────────────────────────────────────────
    ROOT = Path(__file__).resolve().parents[3]
    DEST = ROOT / 'research/nima/results/tower-kernel-displacement-audit.json'
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(json.dumps(results, indent=2) + '\n', encoding='utf-8')
    print(f'Saved to {DEST}')


if __name__ == '__main__':
    main()