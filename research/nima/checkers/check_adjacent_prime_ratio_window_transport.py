import json
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/adjacent-prime-ratio-window-transport.json"


def mm(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def rank(a):
    m = [r[:] for r in a]
    r = 0
    for c in range(len(m[0])):
        p = next((i for i in range(r, len(m)) if m[i][c]), None)
        if p is None:
            continue
        m[r], m[p] = m[p], m[r]
        d = m[r][c]
        m[r] = [x/d for x in m[r]]
        for i in range(len(m)):
            if i != r and m[i][c]:
                f = m[i][c]
                m[i] = [m[i][j]-f*m[r][j] for j in range(len(m[0]))]
        r += 1
    return r


def enc(a):
    return [[str(x) for x in row] for row in a]

# Common-refinement coordinates x,y,z correspond to
# [0,Lp), [Lp,Lq), [Lq,Lp+Lq), with Lp<Lq.
P_pq = [[Q(1), Q(0), Q(0)], [Q(0), Q(1), Q(1)]]
P_qp = [[Q(1), Q(1), Q(0)], [Q(0), Q(0), Q(1)]]
Total = [[Q(1), Q(1), Q(1)]]
Sum2 = [[Q(1), Q(1)]]
# Middle ratio-window hostile lies in ker(P_pq) but not ker(P_qp).
hostile = [[Q(0)], [Q(1)], [Q(-1)]]
pq_hostile = mm(P_pq, hostile)
qp_hostile = mm(P_qp, hostile)
# A two-port transport M with P_qp=M P_pq can exist only if
# ker(P_pq) is contained in ker(P_qp); the hostile disproves this.
checks = {
    "both_orders_have_same_total_window": mm(Sum2, P_pq) == Total and mm(Sum2, P_qp) == Total,
    "common_refinement_has_three_independent_pieces": rank([[Q(1),Q(0),Q(0)],[Q(0),Q(1),Q(0)],[Q(0),Q(0),Q(1)]]) == 3,
    "hostile_in_first_two_port_kernel": pq_hostile == [[Q(0)], [Q(0)]],
    "hostile_detected_by_swapped_order": qp_hostile != [[Q(0)], [Q(0)]],
    "no_two_port_factorization": pq_hostile == [[Q(0)], [Q(0)]] and qp_hostile != [[Q(0)], [Q(0)]],
}
assert all(checks.values()), checks
result = {
    "schema": "marici.nima.adjacent-prime-ratio-window-transport.v1",
    "claim_strength": "finite-cutoff source-typed transport obstruction",
    "source_operation": "common refinement of two transported interval partitions",
    "matrices": {"order_pq": enc(P_pq), "order_qp": enc(P_qp), "total": enc(Total)},
    "checks": checks,
    "hostile": {
        "common_refinement_coordinates": ["0", "1", "-1"],
        "order_pq_readout": [str(x[0]) for x in pq_hostile],
        "order_qp_readout": [str(x[0]) for x in qp_hostile],
        "residual_type": "signed_ratio_window",
    },
    "unsupported": ["three-prime braid coherence", "determinant-line transport", "completion"],
    "passed": True,
}
OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
