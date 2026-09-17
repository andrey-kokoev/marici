#!/usr/bin/env python3
"""Faithful history representation of all one-use words in the eight axes."""
import hashlib,itertools,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
AXES=('H','V','D','q','L','C','O','R')
# A basis state is its complete typed history. In the local Boolean model an
# axis may be appended exactly once.
histories=[p for k in range(9) for p in itertools.permutations(AXES,k)]
history_set=set(histories)
def act(axis,history):
 if axis in history:return None
 return history+(axis,)
def rho(word,history=()):
 state=history
 for a in word:
  state=act(a,state)
  if state is None:return None
 return state
counts=[sum(len(p)==k for p in histories) for k in range(9)]
maximal=[p for p in histories if len(p)==8]
# Exhaustive homomorphism law on every typed word and every split:
# rho(uv)=rho(v,rho(u)) for the append-on-right convention.
hom=True
for w in histories:
 for i in range(len(w)+1):
  u,v=w[:i],w[i:]
  mid=rho(u)
  rhs=None if mid is None else rho(v,mid)
  if rho(w)!=rhs:hom=False;break
 if not hom:break
# Every generator operator respects legality on every history.
operator_closed=all((act(a,p) is None or act(a,p) in history_set) for p in histories for a in AXES)
# Two orders around the lax face remain distinct histories with common endpoint.
qr=rho(('q','R'));rq=rho(('R','q'))
endpoint=lambda p:frozenset(p) if p is not None else None
digest=hashlib.sha256('\n'.join(''.join(p) for p in maximal).encode()).hexdigest()
checks={'history_count_109601':len(histories)==109601,'rank_counts_exact':counts==[1,8,56,336,1680,6720,20160,40320,40320],'maximal_words_40320':len(maximal)==math.factorial(8),'all_maximal_histories_unique':len(set(maximal))==len(maximal),'generator_operators_closed_on_typed_basis':operator_closed,'exhaustive_homomorphism_law':hom,'repeated_axis_is_zero':all(rho((a,a)) is None for a in AXES),'endpoint_only_collapses_all_maximal_words':len({endpoint(p) for p in maximal})==1,'qR_and_Rq_histories_distinct':qr!=rq,'qR_and_Rq_endpoint_equal':endpoint(qr)==endpoint(rq)}
out={'schema':'marici.nima.eight-axis-typed-path-representation.v1','axes':AXES,'representation':'rho(a)e_p=e_(p a) when a is unused, otherwise 0','composition_convention':'rho(uv)=rho(v) after rho(u), equivalently rho(uv)e_p=rho(v)rho(u)e_p','history_rank_counts':counts,'history_count':len(histories),'maximal_history_count':len(maximal),'maximal_history_sha256':digest,'lax_face':{'routes':['qR','Rq'],'same_endpoint':True,'identified':False,'two_cell':'A_X=P_X F (I-P_X)'},'checks':checks,'passed':all(checks.values()),'claim_boundary':'faithful combinatorial regular representation of the local one-use typed path category; analytic realization of every generator and all higher 2-cell relations is separate'}
p=ROOT/'research/nima/results/eight-axis-typed-path-representation.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
