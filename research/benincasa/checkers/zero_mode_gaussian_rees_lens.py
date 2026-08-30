"""Exact Rees normalization of the one-mode Gaussian zero-frequency lens."""
import json
from fractions import Fraction as Q
from pathlib import Path


def packet_for(lam, alpha):
    # h=diag(lam^2/alpha, alpha), det(h)=lam^2.  The positive-source
    # covariance is sqrt(det h) h^{-1}/2.
    h = [[lam * lam / alpha, Q(0)], [Q(0), alpha]]
    v = [[alpha / (2 * lam), Q(0)], [Q(0), lam / (2 * alpha)]]
    rees = [[lam * x for x in row] for row in v]
    assert h[0][0] * h[1][1] == lam * lam
    assert v[0][0] * v[1][1] == Q(1, 4)
    return {
        "lambda": str(lam),
        "alpha": str(alpha),
        "h": [[str(x) for x in row] for row in h],
        "V": [[str(x) for x in row] for row in v],
        "lambda_V": [[str(x) for x in row] for row in rees],
    }


rows = [
    packet_for(Q(1, 10), Q(1)),
    packet_for(Q(1, 100), Q(1)),
    packet_for(Q(1, 10), Q(3, 2)),
]

# For a fixed limiting nonzero stiffness alpha_0, the source-normalized limit is
# diag(alpha_0/2,0).  Rescaling an external regulator epsilon -> c epsilon does
# not change it because lambda=sqrt(det h), rather than epsilon, is used.
packet = {
    "schema": "marici.zero-mode-gaussian-rees-lens.v1",
    "source_normal": "lambda=sqrt(det(h))",
    "family": rows,
    "limit": "lambda V -> diag(alpha_0/2,0)",
    "coordinate_rescaling_invariant": True,
    "depends_on_surviving_source_stiffness": True,
    "classification": "canonical first Rees grade over existing zero-frequency support; no new Carrier incidence",
    "conclusion": "The apparent affine ambiguity of the divergent covariance disappears after normalization by the intrinsic source normal lambda. The boundary coefficient is canonical relative to the surviving source quadratic form.",
}

out = Path(__file__).parent / "results" / "zero-mode-gaussian-rees-lens.json"
out.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet, indent=2))
