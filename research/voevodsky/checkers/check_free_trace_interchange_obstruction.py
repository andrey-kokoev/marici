"""Free trace-path category detects absent interchange despite equal arithmetic image."""
from fractions import Fraction as Q
from pathlib import Path
import json
H=Q(1,2);I=Q(1)
def fire(w,move):
 kind,i=move
 assert 0<=i<len(w)-1
 pair=w[i:i+2]
 assert (kind,pair) in (('merge',(H,H)),('swap',(H,I)))
 return w[:i]+((I,) if kind=='merge' else (I,H))+w[i+2:]
def replay(w,moves):
 states=[w]
 for move in moves:states.append(fire(states[-1],move))
 return states
start=(H,H,I)
a=(('merge',0),);b=(('swap',1),('swap',0),('merge',1))
ra=replay(start,a);rb=replay(start,b)
assert ra[-1]==rb[-1]==(I,I)
# In the FREE category on the two named rewrite generators, paths are words
# of generator-occurrences. No relation equating these parallel words exists.
assert a!=b and len(a)==1 and len(b)==3
assert tuple(map(len,ra))!=(tuple(map(len,rb)))
# Source-bound arithmetic forgets the path but does not reflect its identity.
assert sum(ra[-1],Q(0))==sum(rb[-1],Q(0))==Q(2)
# Any supplied new 4-cell must carry this exact parallel boundary; admitting
# one is a NEW declaration, not derivable in the free presentation.
def admissible(packet):
 if packet.get('from')!=a or packet.get('to')!=b:return 'boundary_mismatch'
 if packet.get('constructor') not in ('source_derived_interchange',):return 'no_declared_generator'
 return 'requires_independent_constructor_check'
assert admissible({'from':a,'to':b,'constructor':'endpoint_equality'})=='no_declared_generator'
assert admissible({'from':a,'to':a,'constructor':'source_derived_interchange'})=='boundary_mismatch'
# Replay-of-path is a permitted fine control; quotienting by endpoint is not
# faithful to this control, even though a public endpoint control agrees.
assert len(a)!=len(b)
report={'passed':True,'free_path_distinct':True,'public_endpoint_equal':True,'proof_replay_step_counts':[len(a),len(b)],'first_missing_obligation':'new typed source-derived 4-cell generator or explicit path-forgetting quotient','self_asserted_endpoint_cell_refused':True,'scope':'Free presentation on fixed primitive half-unit trace generators. Not an impossibility theorem for enriched 4-categories, nor a semantic/operational authority claim.'}
out=Path(__file__).resolve().parents[1]/'results/free-trace-interchange-obstruction.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
