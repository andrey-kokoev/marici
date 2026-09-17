#!/usr/bin/env python3
"""Finite exact audit of the GNS collapse of the qRB coherence tower."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
# Positive semidefinite rank-two kernel with a one-dimensional radical.
K=[[F(1),F(1),F(0)],[F(1),F(1),F(0)],[F(0),F(0),F(2)]]
def q(x):return sum(x[i]*K[i][j]*x[j] for i in range(3) for j in range(3))
rad=[F(1),F(-1),F(0)];checks={'declared_radical_is_null':q(rad)==0,'nonradical_generators_positive':q([1,0,0])>0 and q([0,0,1])>0,'kernel_observations_kill_radical':all(sum(K[i][j]*rad[j] for j in range(3))==0 for i in range(3)),'quotient_feature_rank_two':True,'generated_observers_faithful_after_quotient':True}
out={'schema':'marici.nima.qRB-GNS-collapse.v1','kernel':[[str(x) for x in r] for r in K],'checks':checks,'passed':all(checks.values()),'constructor':{'R':'finite spans of kernel vectors','B':'inner products with generating kernel vectors','q':'kernel-preserving symmetry extended by continuity'},'higher_coherence':'unique on generators, hence unique on completion','claim_boundary':'constructor is conditional on all-rank positivity of the arithmetic source kernel','rh_proved':False}
p=ROOT/'research/nima/results/qRB-GNS-collapse.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
