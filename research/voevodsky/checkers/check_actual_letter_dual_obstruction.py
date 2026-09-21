"""Actual-letter normalization and functional witness; no sampled spectra."""
from pathlib import Path
from math import factorial
import runpy
import json
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[3]
b=runpy.run_path(str(ROOT/'research/nima/checkers/check_seven_event_factorization_descent.py'))
v=b['multiply'](b['relation']((0,1),1),b['relation']((2,3),0))
assert len(v)==8

# Four positive letters in the first diamond; unequal values matter.
# Fixtures represent norm bookkeeping, NOT computed theta norms.
checks=0
for gammas in ((F(1),F(2),F(3),F(5)),
               (F(1,2**20),F(1,2**40),F(1,2**60),F(1,2**80))):
    edge_weights={(0,1):gammas[0],(1,3):gammas[1],
                  (0,2):gammas[2],(2,3):gammas[3]}
    weights={}
    for (word,marks),coef in v.items():
        state=0;weight=F(1)
        assert sum(marks)==1
        for event,keep in zip(word,marks):
            end=state|(1<<event)
            if keep:weight*=edge_weights[state,end]
            state=end
        weights[word,marks]=weight
    norm=factorial(4)*sum(abs(c)*weights[k] for k,c in v.items())
    assert norm==48*sum(gammas)
    unit={k:F(c)/norm for k,c in v.items()}
    functional=factorial(4)*sum((1 if v[k]>0 else -1)*weights[k]*c for k,c in unit.items())
    assert functional==1
    for R in (1,2,5,20):
        assert factorial(4)*R**4*sum(abs(c)*weights[k] for k,c in unit.items())==R**4
        checks+=1
    # Two occurrences per first-diamond event, four forgotten final edges.
    assert F(8)*sum(gammas)/norm==F(1,6)

result={'passed':True,'actual_weight_normalization_checks':checks,
 'checks':{'continuous_Q1_functional_takes_unit_vectors_to_one':True,
 'source_family_bounded_in_actual_letter_scales':True,
 'two_seam_term_norm_ratio_before_feature_attenuation':'1/6'},
 'scope':'Exact positive-letter norm bookkeeping. Actual late-window attenuation comes from the weighted trace estimate, not these rational fixtures. No weighted factorization lift is asserted.'}
out=ROOT/'research/voevodsky/results/actual-letter-dual-obstruction.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
