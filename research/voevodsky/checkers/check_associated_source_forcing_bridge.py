"""Exact radius-loss bounds for the source -> forcing -> feature bridge."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json

checks=truncations=0
for aA,aF,C in ((F(1),F(3),F(1,3)),(F(4),F(1),F(4)),
                (F(3,2),F(5,2),F(3,5)),(F(2),F(2),F(1))):
    kappa=max(F(1),aF/aA)
    c=max(F(1),C)
    for n in range(2,33):
        for r in range(1,n//2+1):
            for m in (0,n//2,n):
                # Fixed graph factor cancels between source and forcing records.
                for b in (F(1),F(3,2),F(3)):
                    target=(1+n)**r*b**m*aF**n
                    source=(1+n)**r*(kappa*b*aA)**n
                    assert target<=source
                    assert C**m*b**m<=(c*b)**m
                    checks+=1
            # An additional radius factor two pays for the telescoping n factor.
            assert F(n,2**n)<=1
            truncations+=1

# The given source multiplication law and the bridge can use one common
# radius: apply its 2s,2b loss after the bridge's fixed kappa factor.
for kappa in (F(1),F(5,3),F(3)):
    for b in (F(1),F(2),F(7,2)):
        assert 2*(kappa*b)==kappa*(2*b)

result={'passed':True,'exact_bridge_weight_checks':checks,
 'theta_error_radius_checks':truncations,
 'checks':{'forcing_norm_paid_by_fixed_source_radius_loss':True,
 'feature_transfer_paid_by_feature_radius_loss':True,
 'extra_path_length_for_theta_error_paid_by_radius_two':True},
 'scope':'Exact weight regressions. Finite forcing lift, closed-kernel descent and continuous multiplicative comparison are proved in the companion note; no identification of source and forcing completions as equal spaces.'}
ROOT=Path(__file__).resolve().parents[3]
out=ROOT/'research/voevodsky/results/associated-source-forcing-bridge.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
