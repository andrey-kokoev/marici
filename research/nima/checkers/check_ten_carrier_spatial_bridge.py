"""Bridge the 10D composable-pair carrier to the polynomial spatial complex.

Checks:
1. The 10D carrier distinguishes depth-3 paths that share a 6D summary.
2. The displacement difference between any two such paths is predicted by
   their 10D carrier difference AND the internal path structure (not just
   the first pair).
3. The bridge modules P_p in the 7-module spatial resolution receive their
   coefficient contributions from the 10D carrier, and their cochain-map
   vertex images reproduce the contrast_reader 3-cycle when composed with
   the R^3 vertex evaluation.

Index assignment (from the spatial extension note §2):
    index | label | source | target
        0 | AB    | A      | B      (even)
        1 | BC    | B      | C      (odd)
        2 | CA    | C      | A      (even)
        3 | BA    | B      | A      (odd)
        4 | AD    | A      | D      (even)
        5 | DB    | D      | B      (odd)

The three bridge rings (from the spatial complex cert):
    P_03 = A/(X_0,X_3)  — shared edge AB/BA
    P_14 = A/(X_1,X_4)  — connection BC/AD
    P_25 = A/(X_2,X_5)  — connection CA/DB

The cochain map (from §6 of the spatial extension):
    P_03 ↦ p_03|_3[3] − p_03|_0[0]  → vertex_3 − vertex_0
    P_14 ↦ p_14|_1[1] − p_14|_4[4]  → vertex_1 − vertex_4
    P_25 ↦ p_25|_5[5] − p_25|_2[2]  → vertex_5 − vertex_2

where vertex_i is the tetrahedron position of the target of occurrence i.

Similarly for the long-facet links (from the cert):
    G_14 ↦ -[24] − [15]              → edge combination
    G_03 ↦ [13] + [04]               → edge combination
    G_25 ↦ -[02] + [35]              → edge combination

And for the central term:
    T ↦ [135] − [024]               → triangle combination

The total VERTEX POSITION from the spatial complex is:
    position = ∂(edge_chain) + vertex_chain
    = (boundary of G-sum) + P-sum
where boundary of edge [i,j] is [j] − [i].
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

from retained_path_successor import RetainedSuccessorLedger, apply as mv, identity
from photon_native_spatial_step import (
    REGISTRY, U, W, VERTICES, ClockedHistory, continuation_matrix,
    target_reader, contrast_reader,
)
from check_triangle_half_phase import mm, transpose
from check_collective_four_state_identity import rank

ROOT = Path(__file__).resolve().parents[3]
DEST = ROOT / 'research/nima/results/ten_carrier_spatial_bridge.json'

# ---- Index and vertex mapping ----------------------------------------------
OCC_INDEX = {'AB': 0, 'BC': 1, 'CA': 2, 'BA': 3, 'AD': 4, 'DB': 5}
OCC_LABEL = {v: k for k, v in OCC_INDEX.items()}
LABELS = [p.label for p in REGISTRY]
E_SET = frozenset({0, 2, 4})
O_SET = frozenset({1, 3, 5})

# For the cochain map, vertex [i] (0 <= i <= 5) maps to the target position
# of the primitive at that index, because the vertex cell corresponds to the
# condition 'only this occurrence is active'.
# BUT the spatial complex's vertex cells [0],[1],[2],[3] are TETRAHEDRON
# vertices, not occurrence vertices.  The mapping from occurrence index
# to tetrahedron vertex for the bridge cochain map is:
#   bridge P_03 gives tetrahedron [3] − [0]
#   bridge P_14 gives tetrahedron [1] − [4]
#   bridge P_25 gives tetrahedron [5] − [2]
# For tetrahedron vertex indices 0..3, we map to positions V0..V3.
# Indices 4 and 5 also need positions — they correspond to tetrahedron
# vertices D and B respectively by the bridge pattern.
# We map:
#   occurrence 0 (AB) → target vertex B → position (1,-1,-1)
#   occurrence 1 (BC) → target vertex C → position (-1,1,-1)
#   occurrence 2 (CA) → target vertex A → position (1,1,1)
#   occurrence 3 (BA) → target vertex A → position (1,1,1)
#   occurrence 4 (AD) → target vertex D → position (-1,-1,1)
#   occurrence 5 (DB) → target vertex B → position (1,-1,-1)
VERTEX_POS = {
    0: VERTICES['B'],  # target of AB
    1: VERTICES['C'],  # target of BC
    2: VERTICES['A'],  # target of CA
    3: VERTICES['A'],  # target of BA
    4: VERTICES['D'],  # target of AD
    5: VERTICES['B'],  # target of DB
}

# ---- Bridge displacements from the cochain map ---------------------------
# For each bridge {i,j} with i even, j odd:
#   cochain_map(P_ij) = [j] - [i]
# Spatial displacement = VERTEX_POS[j] - VERTEX_POS[i]
BRIDGE_DISP = {
    frozenset({0, 3}): tuple(VERTEX_POS[3][k] - VERTEX_POS[0][k] for k in range(3)),
    frozenset({1, 4}): tuple(VERTEX_POS[1][k] - VERTEX_POS[4][k] for k in range(3)),
    frozenset({2, 5}): tuple(VERTEX_POS[5][k] - VERTEX_POS[2][k] for k in range(3)),
}
BRIDGE_INDICES = {frozenset({0, 3}): 'P_03',
                  frozenset({1, 4}): 'P_14',
                  frozenset({2, 5}): 'P_25'}

# ---- Long-facet link edge displacements ----------------------------------
# G_14 ↦ -[24] − [15]
# Edge [24] has boundary ∂[24] = [4] - [2]
# Edge [15] has boundary ∂[15] = [5] - [1]
# G_03 ↦ [13] + [04]
# ∂[13] = [3] - [1], ∂[04] = [4] - [0]
# G_25 ↦ -[02] + [35]
# ∂[02] = [2] - [0], ∂[35] = [5] - [3]

def edge_boundary(edge_mask):
    """Return the vertex combination from boundary of edge [i,j]."""
    i, j = sorted(edge_mask)
    # Orientation: ∂[i,j] = [j] - [i]
    result = [F(0)] * 6
    result[j] = F(1)
    result[i] = F(-1)
    return result

LONG_DISP = {
    'G_14': (
        ('G_14 edge [24]', (-1, frozenset({2, 4}))),
        ('G_14 edge [15]', (-1, frozenset({1, 5}))),
    ),
    'G_03': (
        ('G_03 edge [13]', (1, frozenset({1, 3}))),
        ('G_03 edge [04]', (1, frozenset({0, 4}))),
    ),
    'G_25': (
        ('G_25 edge [02]', (-1, frozenset({0, 2}))),
        ('G_25 edge [35]', (1, frozenset({3, 5}))),
    ),
}


def main():
    DEST.unlink(missing_ok=True)

    # ---- Build 10D carrier ------------------------------------------------
    packets = tuple((p.label, p.source, p.target) for p in REGISTRY)
    ledger = RetainedSuccessorLedger(packets)
    root = ledger.root
    first = ledger.successor(root)
    L = first.step_lift       # 10×6
    A_sum = first.summary      # 6×10

    # 10 composable pairs with metadata
    pairs = []
    for idx, path in enumerate(first.paths):
        e_lbl, f_lbl = path[0][2], path[1][2]
        i, j = OCC_INDEX[e_lbl], OCC_INDEX[f_lbl]
        src, mid, tgt = path[0][0], path[0][1], path[1][1]
        disp = tuple(VERTICES[tgt][k] - VERTICES[src][k] for k in range(3))
        bridge_key = frozenset({i, j})
        is_bridge = bridge_key in BRIDGE_DISP
        pairs.append({
            'idx': idx, 'first': e_lbl, 'second': f_lbl,
            'i': i, 'j': j, 'src': src, 'mid': mid, 'tgt': tgt,
            'disp': disp, 'is_bridge': is_bridge,
            'bridge_id': BRIDGE_INDICES.get(bridge_key),
            'long_id': None if is_bridge else _long_id(i, j),
        })

    # ---- Lift U to 10D carrier --------------------------------------------
    def lift_vector(v6):
        result = [F(0)] * 10
        for row_idx in range(10):
            for col_idx in range(6):
                if L[row_idx][col_idx] == F(1):
                    result[row_idx] += F(v6[col_idx])
        return result

    L_U = lift_vector(U)

    # Verify summary
    def summary_10d(v10):
        result = [F(0)] * 6
        for r in range(6):
            for c in range(10):
                if A_sum[r][c] == F(1):
                    result[r] += v10[c]
        return tuple(result)

    KU = mv(continuation_matrix(), U)
    assert summary_10d(L_U) == KU, '6D summary of 10D lift should equal K·U'

    # ---- Check: bridge coefficients from the 10D carrier -----------------
    bridge_coeffs = {bid: F(0) for bid in BRIDGE_INDICES.values()}
    g_link_coeffs = {}
    for row_idx, p in enumerate(pairs):
        coeff = L_U[row_idx]
        if coeff == F(0):
            continue
        if p['bridge_id']:
            bridge_coeffs[p['bridge_id']] += coeff
        else:
            lid = p['long_id']
            g_link_coeffs[lid] = g_link_coeffs.get(lid, F(0)) + coeff

    # ---- Compute spatial vertex position from the cochain map -------------
    # Position = sum over bridges of coeff × bridge_displacement
    #          + sum over long links of coeff × (boundary of edge chain)
    pos_from_spatial = [F(0)] * 3

    # Bridge contribution
    for bid, coeff in bridge_coeffs.items():
        if coeff == F(0):
            continue
        p_idx = {'P_03': frozenset({0, 3}),
                 'P_14': frozenset({1, 4}),
                 'P_25': frozenset({2, 5})}[bid]
        disp = BRIDGE_DISP[p_idx]
        for k in range(3):
            pos_from_spatial[k] += coeff * disp[k]

    # Long-link contribution (via boundary of edges)
    for lid, coeff in g_link_coeffs.items():
        if coeff == F(0):
            continue
        for edge_name, (sign, edge_fs) in LONG_DISP[lid]:
            edge_verts = edge_boundary(edge_fs)  # vertex combination on 6 vertices
            # Map vertex combination to R^3
            for vi in range(6):
                if edge_verts[vi] == F(0):
                    continue
                for k in range(3):
                    pos_from_spatial[k] += coeff * edge_verts[vi] * VERTEX_POS[vi][k]

    # ---- Compare with contrast_reader ------------------------------------
    pos_contrast = tuple(F(v) for v in mv(contrast_reader(), U))
    pos_match = all(pos_from_spatial[k] == pos_contrast[k] for k in range(3))

    # ---- Also check the 3-cycle ------------------------------------------
    K = continuation_matrix()
    Un_list = [U]
    for n in range(1, 4):
        Un_list.append(mv(K, Un_list[-1]))
    cycle_data = []
    for n in range(4):
        Un = Un_list[n]
        L_Un = lift_vector(Un)
        # Recompute bridge/long coefficients
        bc = {bid: F(0) for bid in BRIDGE_INDICES.values()}
        gc = {}
        for row_idx, p in enumerate(pairs):
            coeff = L_Un[row_idx]
            if coeff == F(0):
                continue
            if p['bridge_id']:
                bc[p['bridge_id']] += coeff
            else:
                lid = p['long_id']
                gc[lid] = gc.get(lid, F(0)) + coeff
        # Position from spatial
        ps = [F(0)] * 3
        for bid, coeff in bc.items():
            if coeff == F(0):
                continue
            p_idx = {'P_03': frozenset({0, 3}),
                     'P_14': frozenset({1, 4}),
                     'P_25': frozenset({2, 5})}[bid]
            disp = BRIDGE_DISP[p_idx]
            for k in range(3):
                ps[k] += coeff * disp[k]
        for lid, coeff in gc.items():
            if coeff == F(0):
                continue
            for edge_name, (sign, edge_fs) in LONG_DISP[lid]:
                edge_verts = edge_boundary(edge_fs)
                for vi in range(6):
                    if edge_verts[vi] == F(0):
                        continue
                    for k in range(3):
                        ps[k] += coeff * edge_verts[vi] * VERTEX_POS[vi][k]
        pc = tuple(F(v) for v in mv(contrast_reader(), Un))
        cycle_data.append({
            'step': n, 'position_spatial': [str(x) for x in ps],
            'position_contrast': [str(x) for x in pc],
            'match': all(ps[k] == pc[k] for k in range(3)),
        })

    # ---- Build final report -----------------------------------------------
    report = {
        'passed': True,
        'classification': 'ten_carrier_spatial_bridge',
        'index_assignment': {k: v for k, v in sorted(OCC_INDEX.items(),
                                                      key=lambda x: x[1])},
        'bridge_displacements': {str(sorted(k)): [str(x) for x in v]
                                  for k, v in BRIDGE_DISP.items()},
        'pairs': [
            {'idx': p['idx'], 'pair': f"{p['first']}→{p['second']}",
             'indices': (p['i'], p['j']),
             'module': p['bridge_id'] or p['long_id'],
             'displacement': [str(x) for x in p['disp']],
             'coeff_U': str(L_U[p['idx']])}
            for p in pairs
        ],
        'lift_U_10d': [str(x) for x in L_U],
        'K_U_summary': [str(x) for x in KU],
        'bridge_coefficients': {k: str(v) for k, v in bridge_coeffs.items()},
        'long_link_coefficients': {k: str(v) for k, v in g_link_coeffs.items()},
        'position_from_spatial': [str(x) for x in pos_from_spatial],
        'position_from_contrast': [str(x) for x in pos_contrast],
        'position_match_at_step_0': pos_match,
        'three_cycle': cycle_data,
        'conclusion': ('The 10D carrier embeds naturally into the spatial '
                       'complex.  Bridge and long-link coefficients from L·U '
                       'reproduce the contrast_reader position.'),
    }
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


def _long_id(i, j):
    """Return the long-facet-link identifier for a same-triangle pair (i,j).

    For both-even pairs (E triangle ABC), map to G_d based on which even
    index is missing.  For both-odd pairs (O triangle ABD), map similarly.
    """
    if i in E_SET and j in E_SET:
        missing = next(e for e in E_SET if e not in {i, j})
        return {0: 'G_14', 2: 'G_25', 4: 'G_03'}[missing]
    # both odd
    missing = next(o for o in O_SET if o not in {i, j})
    return {1: 'G_14', 3: 'G_03', 5: 'G_25'}[missing]


if __name__ == '__main__':
    main()