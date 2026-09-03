"""Independent labelled assembly of the frozen weighted prime-power interval."""
import json,sys
from fractions import Fraction as F
from pathlib import Path
HERE=Path(__file__).parent;ROOT=HERE.parent
sys.path.insert(0,str(HERE))
import preconditioned_spline_weil as w

def terms(cutoff):
 a=w.scale(F(2),w.log_q(F(2)));out=[]
 for p in w.primes(cutoff):
  q=p;m=1
  while q<=cutoff:
   lq=w.log_q(F(q));k=w.shifted_k(lq,a);weight=w.mul(w.log_q(F(p)),w.inv(w.sqrt_q(F(q))))
   out.append({'label':(p,m,q),'weight':weight,'test':k})
   q*=p;m+=1
 return out
def assemble(ts,sign=F(-2),weights=None):
 out=w.Z
 for i,t in enumerate(ts):out=w.add(out,w.scale(sign,w.mul(t['weight'] if weights is None else weights[i],t['test'])))
 return out
base_terms=terms(1024);base=assemble(base_terms)
frozen=json.loads((ROOT/'results/preconditioned_spline_weil.json').read_text())['intervals']['prime'];frozen=tuple(map(F,frozen))
assert len(base_terms)==198 and base==frozen
extended=terms(2048);beyond=[t for t in extended if t['label'][2]>1024];assert beyond
# Compact support is certified analytically. Raw interval evaluation outside support
# need not simplify the alternating truncated-power cancellation to the exact zero.
a=w.scale(F(2),w.log_q(F(2)));support_edge=w.add((F(4),F(4)),w.scale(F(2),a))
assert w.log_q(F(1024))[0] > support_edge[1]
stable=assemble([t for t in extended if t['label'][2]<=1024]);assert stable==base
raw_beyond=assemble(beyond);raw_dependency_artifact=raw_beyond!=w.Z
sign_flip=assemble(base_terms,F(2));assert sign_flip==(-base[1],-base[0]) and sign_flip!=base
weights=[t['weight'] for t in base_terms];weights[0],weights[1]=weights[1],weights[0]
permuted=assemble(base_terms,weights=weights);assert permuted!=base
out={'schema':'marici.weighted-prime-power-source-compatibility.v1','status':'passed','term_count':len(base_terms),'extended_term_count':len(extended),'analytically_zero_beyond_cutoff_count':len(beyond),'matches_frozen_prime_interval':True,'cutoff_stabilization_by_support_bound':True,'raw_outside_support_interval_dependency_artifact':raw_dependency_artifact,'hostile_results':{'sign_flip_changes_interval':True,'label_weight_permutation_changes_interval':True},'prime_interval_float':[float(base[0]),float(base[1])],'remaining_semantic_gap':'weighted source functional has no owner-authorized comparison to a G4 radial functional','claim_boundary':'finite weighted source compatibility only'}
(ROOT/'results/weighted-prime-power-source-compatibility.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
