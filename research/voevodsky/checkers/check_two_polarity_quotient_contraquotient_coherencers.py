#!/usr/bin/env python3
"""Exact two-polarity quotient/contraquotient coherencer fixture.

Uses the exact rational Grams underlying the two-primitive V1->V4 packet.
"""
import json
from fractions import Fraction as Q
from pathlib import Path

def mv(A,x): return [sum(a*b for a,b in zip(r,x)) for r in A]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def det(A): return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def proportional(x,y): return x[0]*y[1]==x[1]*y[0] and any(x) and any(y)

Dp=[[Q(1,125),Q(3,125)],[Q(3,125),Q(9,125)]]
Dm=[[Q(81,125),Q(-27,125)],[Q(-27,125),Q(9,125)]]
rp=[Q(-3),Q(1)]; rm=[Q(1),Q(3)]
vp=[Q(1),Q(3)]; vm=[Q(3),Q(-1)]
F=[[Q(0),Q(-1)],[Q(1),Q(0)]]
F2=mm(F,F)
Frp=mv(F,rp); Frm=mv(F,rm); Fvp=mv(F,vp); Fvm=mv(F,vm)
checks={
 'positive_rank_one':det(Dp)==0 and Dp[0][0]>0,
 'negative_rank_one':det(Dm)==0 and Dm[0][0]>0,
 'plus_radical':mv(Dp,rp)==[0,0],
 'minus_radical':mv(Dm,rm)==[0,0],
 'radical_intersection_zero':not proportional(rp,rm),
 'joint_quotient_faithful':not proportional(rp,rm),
 'quarter_turn':F2==[[-1,0],[0,-1]],
 'quotient_coherencer_plus_to_minus':proportional(Frp,rm),
 'quotient_coherencer_minus_to_plus':proportional(Frm,rp),
 'contraquotient_coherencer_plus_to_minus':proportional(Fvp,vm),
 'contraquotient_coherencer_minus_to_plus':proportional(Fvm,vp),
}
out={
 'schema':'marici.voevodsky.two-polarity-quotient-contraquotient-coherencers.v1',
 'status':'passed' if all(checks.values()) else 'failed',
 'D_plus':[[str(x) for x in r] for r in Dp], 'D_minus':[[str(x) for x in r] for r in Dm],
 'radicals':{'R_plus':list(map(str,rp)),'R_minus':list(map(str,rm))},
 'contraquotient_ranges':{'V_plus':list(map(str,vp)),'V_minus':list(map(str,vm))},
 'C4_quarter_turn':[[str(x) for x in r] for r in F],
 'checks':checks,
 'interpretation':'Each polarity first has a quotient coherencer on X/R and a contraquotient coherencer on ran(D). The same quarter-turn exchanges both. Their joint quotient has kernel R_plus intersection R_minus=0, so quotienting the two coherencers loses no source direction in this fixture.',
 'claim_boundary':'Exact two-dimensional finite packet only; no identification with completed theta/Weil radicals or Evans trace.'
}
root=Path(__file__).resolve().parents[3]; p=root/'research/voevodsky/results/two_polarity_quotient_contraquotient_coherencers.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(out['status']!='passed')
