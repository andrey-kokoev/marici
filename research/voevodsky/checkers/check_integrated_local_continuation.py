"""One owner migration: public operation, whole-section lift, archive and live authority."""
import importlib.util,json
from pathlib import Path
from fractions import Fraction as Q
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research/voevodsky'
p=V/'checkers/check_same_base_live_archive_services.py'
spec=importlib.util.spec_from_file_location('same_base_services',p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
s,r,proof=m.nodes[0];fresh=s._receipt();other,other_receipt,other_proof=m.nodes[1]
assert fresh['state']['migration_binding']==other_receipt['state']['migration_binding']==m.root
# The verified full-segment attachment is affine over every cell, not just probes.
for packet in (proof,other_proof):
 assert packet['migration_binding']==m.root
 assert tuple(map(Q,packet['vertices'][0]))==(0,0) and tuple(map(Q,packet['vertices'][-1]))==(1,1)
 assert all(tuple(map(Q,t))==(Q(v[0]),Q(0),Q(0)) and Q(v[0])==Q(v[1]) for v,t in zip(packet['vertices'],packet['source_lifts']))
# Source operation: add public evidence u<=3/4 to only one independently
# bootstrapped provider. The old full-domain provider stays unchanged.
assert fresh['state']['public_frames'][-1]=={'normal':['1','0'],'upper':'3/4'}
assert other_receipt['state']['public_frames']==[]
assert s.covered_lift(fresh['handle'],r['section_id'],['1/2','1/2'])==other.covered_lift(other_receipt['handle'],other_receipt['section_id'],['1/2','1/2'])==['1/2','0','0']
refused=[]
def reject(name,fn):
 try:fn()
 except (ValueError,PermissionError,AssertionError):refused.append(name)
 else:raise AssertionError(name+' unexpectedly accepted')
reject('excluded-public-point',lambda:s.covered_lift(fresh['handle'],r['section_id'],['1','1']))
reject('nonpublic-frame',lambda:s.advance(fresh['handle'],fresh['state'],{'kind':'append-public','normal':['1','0','0'],'upper':'0'},[1,0],{}))
reject('stale-provider',lambda:s.covered_lift(r['handle'],r['section_id'],['1/2','1/2']))
reject('stale-archive',lambda:s.reexpose(r['handle']))
restored=s.reexpose(fresh['handle'])
assert restored['frames'][-1]['upper']=='3/4' and restored['frames'][:-1]==m.plan['frames']
# A second provider substitutes only for lifting: its independent archive
# remains unrestricted and does not become the first provider's new archive.
assert other.reexpose(other_receipt['handle'])==m.archive_before
report={'passed':True,'root':m.root,'source_operation':'owner-verified public u<=3/4','whole_section_formula':'(u,u)->(u,0,0)','overlap_formula_equal':True,'replacement_lift_live':True,'fresh_archive_restricted':True,'refusals':refused,'resource_receipts':[fresh['bytes'],other_receipt['bytes']],'scope':'One bounded rank-one owning migration; no analytic SARCG identification, total-resource optimum, source authentication or authority transport.'}
(V/'results/integrated-local-continuation.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ('root','resource_receipts')},indent=2))
