"""Actual marked-source checks for the saturated observer transitions.

Use existing symbolic sector weights only for support/rank/nonvanishing.
The theorem substitutes the actual positive d_r for these symbolic scores.
"""
from pathlib import Path
from itertools import permutations, product
import runpy,json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
g=runpy.run_path(str(ROOT/'research/nima/checkers/check_all_depth_observer_tower.py'))
f=g['f'];ordered=g['ordered'];score=g['score']
vac=f['relation']((0,1),0);mixed=f['relation']((0,1),1)
# The initial two-event ideal corner has exactly these two independent vectors.
paths=[(word,marks) for word in permutations((0,1)) for marks in product((0,1),repeat=2)]
records=[f['record'](0,*key) for key in paths]
assert len(paths)==8 and f['rank'](records)==6
assert f['rank']([vac,mixed])==2
for col in (vac,mixed):
    image={}
    for key,c in col.items():
        for out,b in f['record'](0,*key).items():image[out]=image.get(out,0)+c*b
    assert not f['clean'](image)
assert score(ordered(0,vac,1),1)==1
assert score(ordered(0,mixed,1),1)==0
# Every possible right path context reaching the new four-event outer corner.
# No nonidentity left context can precede the fixed initial corner.
checked=0
for word in permutations((2,3)):
    for marks in product((0,1),repeat=2):
        contextual=f['multiply'](vac,{(word,marks):1})
        assert score(ordered(0,contextual,2),2)==0
        checked+=1
forgot_tail=f['relation']((2,3),0)
assert score(ordered(0,f['multiply'](mixed,forgot_tail),2),2)==2
# Hence old vacuum plus contextual mixed tests exhaust the 2D initial corner.
initial_observation=s.diag(1,2)
assert initial_observation.rank()==2
# For m>=2 the initial corner has no new kernel, so its mixed lift is forced.
# A right I^m context kills O_m but gives a nonzero new witness in O_(m+1).
obstructions=[]
for m in (2,3):
    factors=g['factors'](m+1)
    assert factors[0]==mixed
    tail=f['chain_product'](factors[1:])
    witness=f['multiply'](mixed,tail)
    for k in range(1,m+1):assert not ordered(0,witness,k)
    new=score(ordered(0,witness,m+1),m+1)
    assert new==2**m
    obstructions.append({'transition':f'O_{m+1}->O_{m}',
      'old_derivatives_vanish_through':m,'new_symbolic_witness_score':new})
result={'passed':True,'initial_corner':{'marked_paths':8,'recorder_rank':6,'ideal_dimension':2},
 'all_vacuum_lift_right_contexts_checked':checked,
 'first_transition_splitting_support_verified':True,
 'later_forced_lift_obstructions':obstructions,
 'scope':'Actual finite source support, corner rank, and obstruction checks. First splitting and all-depth nonsplitting use the companion source-module proofs. Scores are symbolic nonzero sector fixtures, not numerically calibrated residual values.'}
out=ROOT/'research/voevodsky/results/saturated-observer-transitions.json'
out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
