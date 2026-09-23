"""Bounded proof endpoint contract refuses proof-history controls by design."""
from fractions import Fraction as Q
from pathlib import Path
import json
ROWS=((-Q(1),),(Q(1),),(Q(1),));BOUNDS=(Q(0),Q(1),Q(1))
def cert(m,c,T):
 return len(m)==3 and min((*m,c))>=0 and sum((ROWS[i][0]*m[i] for i in range(3)),Q(0))==1 and sum((BOUNDS[i]*m[i] for i in range(3)),Q(0))+c==T
def endpoint(m,c,T,choice,root_ids,requested_control='public_certificate'):
 if tuple(root_ids)!=('lower','upper-A','upper-B'):raise PermissionError('ROOT_PROVENANCE_MISSING')
 if requested_control not in ('public_certificate','public_target_bound'):raise PermissionError('PROOF_REPLAY_NOT_IN_ENDPOINT_CONTRACT')
 if not cert(m,c,T):raise ValueError('INVALID_SOURCE_CERTIFICATE')
 d={'A':(Q(1),Q(1),Q(0)),'B':(Q(1),Q(0),Q(1))}.get(choice)
 if d is None:raise ValueError('NO_SOURCE_DERIVED_WITNESS')
 assert sum((ROWS[i][0]*d[i] for i in range(3)),Q(0))==0
 B=sum((BOUNDS[i]*d[i] for i in range(3)),Q(0));assert B>0
 out=tuple(m[i]+c*d[i]/B for i in range(3));assert cert(out,Q(0),T)
 return {'target_normal':'1','target_bound':str(T),'multiplier':tuple(map(str,out)),'surplus':'0','source_rows':root_ids,'chosen_witness':choice}
roots=('lower','upper-A','upper-B');p=(Q(0),Q(1),Q(0));a=endpoint(p,Q(1),Q(2),'A',roots);b=endpoint(p,Q(1),Q(2),'B',roots)
assert a['target_normal']==b['target_normal'] and a['target_bound']==b['target_bound']
assert a['multiplier']!=b['multiplier'] and a['chosen_witness']!=b['chosen_witness']
for control in ('proof_replay','actual_history','analytic_role_map','source_widening'):
 try:endpoint(p,Q(1),Q(2),'A',roots,control)
 except PermissionError:pass
 else:raise AssertionError('fine control admitted: '+control)
try:endpoint(p,Q(1),Q(2),'A',('lower','upper-A'))
except PermissionError:pass
else:raise AssertionError('missing primitive bound admitted')
try:endpoint(p,Q(1),Q(2),'unrooted',roots)
except ValueError:pass
else:raise AssertionError('unrooted witness admitted')
report={'passed':True,'same_public_answer_distinct_certificates':True,'certificate_retains_multiplier_and_witness':True,'permitted_controls':['public_certificate','public_target_bound'],'refused_controls':['proof_replay','actual_history','analytic_role_map','source_widening'],'primitive_root_and_witness_required':True,'scope':'Prototype endpoint-only contract for fixed separately rooted three-row source. No proof-path equality, live provider authentication, 3/4-cell constructor or general analytic functor.'}
out=Path(__file__).resolve().parents[1]/'results/endpoint-contract-boundary.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
