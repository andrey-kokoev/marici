"""Exact hostile test for scalar versus labelled multi-Rees zero-mode normalization."""
import json
from fractions import Fraction as Q
from pathlib import Path


def covariance(l1, l2, a1=Q(1), a2=Q(1)):
    # Canonical ordering (q1,p1,q2,p2).  Each source block is
    # diag(lambda_i^2/alpha_i, alpha_i).
    return [
        [a1/(2*l1), Q(0), Q(0), Q(0)],
        [Q(0), l1/(2*a1), Q(0), Q(0)],
        [Q(0), Q(0), a2/(2*l2), Q(0)],
        [Q(0), Q(0), Q(0), l2/(2*a2)],
    ]


def scale(v, s):
    return [[s*x for x in row] for row in v]


def diagonal(v):
    return [v[i][i] for i in range(len(v))]


paths = []
for name, l1, l2 in [
    ("balanced", Q(1,100), Q(1,100)),
    ("lambda2=lambda1^2", Q(1,100), Q(1,10000)),
    ("lambda1=lambda2^2", Q(1,10000), Q(1,100)),
]:
    v = covariance(l1,l2)
    total_normal = l1*l2  # sqrt(det h_total)
    paths.append({
        "name": name,
        "lambda1": str(l1),
        "lambda2": str(l2),
        "total_normal_times_V_diagonal": [str(x) for x in diagonal(scale(v,total_normal))],
        "labelled_grades": {
            "lambda1_V_mode1": [str(l1*v[0][0]),str(l1*v[1][1])],
            "lambda2_V_mode2": [str(l2*v[2][2]),str(l2*v[3][3])],
        },
    })

# The total scalar grade has q entries lambda2/2 and lambda1/2; it collapses
# both leading rank-one coefficients at the simultaneous corner.  Dividing by
# either total parameter to recover them is path-dependent.  The labelled
# grades retain 1/2 independently.
packet = {
    "schema":"marici.two-mode-gaussian-multi-rees-lens.v1",
    "ordering":"(q1,p1,q2,p2)",
    "total_source_normal":"sqrt(det h_total)=lambda1 lambda2",
    "paths":paths,
    "scalar_grade_at_corner":"zero matrix",
    "scalar_normal_is_faithful":False,
    "labelled_normal_cone":["lambda1","lambda2"],
    "labelled_leading_coefficients":{"mode1":"diag(1/2,0)","mode2":"diag(1/2,0)"},
    "classification":"existing intersection of two labelled zero-frequency supports; multi-Rees coefficient object required; no new Carrier incidence",
    "conclusion":"At a simultaneous two-mode zero, the determinant normal lambda1*lambda2 erases both first boundary coefficients. Occurrence-resolved normals recover them canonically, so the correct boundary object is genuinely multi-filtered.",
}

out=Path(__file__).parent/'results'/'two-mode-gaussian-multi-rees-lens.json'
out.write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps(packet,indent=2))
