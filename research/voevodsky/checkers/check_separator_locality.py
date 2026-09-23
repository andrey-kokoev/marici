"""Exhaustive finite semantic controls for separator-local replacement."""
from itertools import product
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
universe=list(product((0,1),repeat=2))
relations=[{p for i,p in enumerate(universe) if mask>>i&1} for mask in range(16)]
def image(R):return {s for h,s in R}
def compose(R,E):return {(s,x) for h,s in R for t,x in E if t==s}
contexts=refinements=gluing=0
for R in relations:
 Q=image(R)
 for E in relations:
  assert compose(R,E)=={(s,x) for s,x in E if s in Q};contexts+=1
  for f in relations:
   assert compose(R,E&f)==compose(R,E)&f;refinements+=1
 # Every incorrect interface subset has an exact point context separating it.
 for mask in range(4):
  proposed={s for s in (0,1) if mask>>s&1}
  if proposed!=Q:
   s=next(iter(proposed^Q));E={(s,0)}
   assert bool(compose(R,E))!=bool({(t,x) for t,x in E if t in proposed})
 for T in relations:
  fine={(h,k,s) for h,s in R for k,t in T if s==t}
  assert {s for h,k,s in fine}==image(R)&image(T);gluing+=1
R0={(0,0)};R1={(1,0)}
assert image(R0)==image(R1)
assert {p for p in R0 if p[0]==0} and not {p for p in R1 if p[0]==0}
# A fine lift valid for one relation is not a lift for the other even though
# their complete public states agree.
assert (0,0) in R0 and (0,0) not in R1
report={'passed':True,'context_pairs':contexts,'local_refinements':refinements,'two_block_gluing_checks':gluing,
 'nonlocal_counterexample':{'same_interface_image':[0],'first_hidden_value':0,'second_hidden_value':1,'distinguishing_frame':'h=0'},
 'scope':'Finite exhaustive semantic test. General result is existential distributivity; no representation-size or effective-lift theorem for arbitrary relations.'}
(OUT/'separator-locality.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
