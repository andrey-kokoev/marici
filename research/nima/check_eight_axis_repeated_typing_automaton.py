#!/usr/bin/env python3
"""Bounded exhaustive audit of the repeated eight-axis typing automaton."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
A=('H','V','D','q','L','C','O','R')
# state=(input_arity,output_arity,polarity,chart,degree,realized,observed,cutoff,stable_shift)
s0=(1,1,0,0,0,0,0,0,0)
def step(s,a):
 h,v,d,q,l,c,o,r,sigma=s
 if a=='H':h+=1
 elif a=='V':v+=1
 elif a=='D':d^=1
 elif a=='q':
  q+=1
  if q==4:q=0;sigma+=1
 elif a=='L':l+=1
 elif a=='C':
  if c:return None
  c=1
 elif a=='O':
  if o:return None
  o=1
 elif a=='R':r+=1
 return (h,v,d,q,l,c,o,r,sigma)
def run(word,start=s0):
 s=start
 for a in word:
  s=step(s,a)
  if s is None:return None
 return s
MAX=6
words=[w for k in range(MAX+1) for w in itertools.product(A,repeat=k)]
typed=[w for w in words if run(w) is not None]
hom=True
for w in typed:
 for i in range(len(w)+1):
  mid=run(w[:i]);rhs=None if mid is None else run(w[i:],mid)
  if run(w)!=rhs:hom=False;break
 if not hom:break
checks={'bounded_words_enumerated':len(words)==sum(8**k for k in range(MAX+1)),'partial_action_composition_law':hom,'D_is_involution':run(('D','D'))==s0,'q_four_steps_are_one_stable_shift':run(('q','q','q','q'))[-1]==1 and run(('q','q','q','q'))[3]==0,'H_V_L_R_are_iterable':run(('H','V','L','R')*3) is not None,'C_and_O_are_directed_one_shot':run(('C','C')) is None and run(('O','O')) is None,'typed_words_nonempty':len(typed)>0}
out={'schema':'marici.nima.eight-axis-repeated-typing-automaton.v1','axes':A,'state_fields':['input_arity','output_arity','polarity','chart_mod_4','convolution_degree','realized','observed','cutoff','stable_shift'],'bounded_exhaustion_length':MAX,'words_tested':len(words),'typed_words':len(typed),'checks':checks,'passed':all(checks.values()),'interpretation':'partial monoid action on an infinite typed state set; history linearization turns each partial transition into a block operator','claim_boundary':'typing model only; C/O idempotent retention could alternatively be modeled by identity after first application, and analytic closability remains separate'}
p=ROOT/'research/nima/results/eight-axis-repeated-typing-automaton.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
