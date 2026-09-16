#!/usr/bin/env python3
"""Exact finite algebra audit for aligned positive regulator Grams.

This validates the acceptance algebra and a regulator-mismatch hostile. It does
not derive the semilocal positive Gram identity.
"""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]


def add(a,b): return [[x+y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def sub(a,b): return [[x-y for x,y in zip(ar,br)] for ar,br in zip(a,b)]
def diag(xs): return [[x if i==j else F(0) for j in range(len(xs))] for i,x in enumerate(xs)]
def encode(a): return [[str(x) for x in row] for row in a]

# An exact four-coordinate centered Hermitian form with both polarities.
D = diag([F(3,2), F(1,3), F(-2,5), F(-7,4)])
Dp = diag([F(3,2), F(1,3), F(0), F(0)])
Dm = diag([F(0), F(0), F(2,5), F(7,4)])
AbsD = add(Dp,Dm)

# Shared two-copy bulk/Widom edge after channelwise normalization.
C = diag([F(11), F(13), F(17), F(19)])
GT = add(C,Dp)
G0 = add(C,Dm)

# Hostile: one unmatched outer-regulator row leaves positive mass only in Tate.
H = diag([F(0), F(0), F(0), F(1,6)])
GT_bad = add(GT,H)

checks = {
    "aligned_gram_difference_is_centered": sub(GT,G0) == D,
    "common_edge_recovered_from_tate": sub(GT,Dp) == C,
    "common_edge_recovered_from_reference": sub(G0,Dm) == C,
    "residual_absolute_gram": add(sub(GT,C),sub(G0,C)) == AbsD,
    "signed_residual_gram": sub(sub(GT,C),sub(G0,C)) == D,
    "all_positive_diagonal_grams": all(x >= 0 for A in (C,GT,G0,Dp,Dm,AbsD) for i,row in enumerate(A) for j,x in enumerate(row) if i==j),
    "mismatched_regulator_detected": sub(GT_bad,G0) != D,
    "mismatch_residual_exact": sub(sub(GT_bad,G0),D) == H,
}

out = {
    "schema":"marici.voevodsky.positive-regulator-alignment-common-edge.v1",
    "status":"passed" if all(checks.values()) else "failed",
    "checks":checks,
    "centered_form":encode(D),
    "common_positive_edge":encode(C),
    "absolute_residual_gram":encode(AbsD),
    "hostile_unmatched_outer_row":encode(H),
    "interpretation":"With aligned regulators, common-edge removal returns the Jordan absolute Gram exactly. One unmatched positive regulator row is detected as an additive alignment residual.",
    "claim_boundary":"Exact finite matrix acceptance algebra only. The fixture does not construct semilocal physical features or prove that their Gram difference equals the centered regulator.",
}
path=ROOT/'research/voevodsky/results/positive_regulator_alignment_common_edge.json'
path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
raise SystemExit(out['status']!='passed')
