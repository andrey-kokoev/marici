"""Whole-segment direct/staged comparison after independently checked attachments."""
from pathlib import Path
from fractions import Fraction as Q
from copy import deepcopy
import gzip,json
from full_segment_checkpoint import FullSegmentSession,verify_full_segment
from checked_retirement_interface import migrate
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research/voevodsky';G=ROOT/'research/grothendieck/results'
plan=json.loads((G/'audit-elimination-contract.json').read_text())['plans'][0]
case=json.loads(gzip.decompress((G/'audit-elimination.json.gz').read_bytes()))['compactions'][0]
template=json.loads((V/'results/full-segment-checkpoint.json').read_text())['section']
root=migrate(plan,case,retain_lift=True).migration_binding
nodes=[]
for knots in (['0','1'],['0','1/2','1'],['0','1/4','3/4','1']):
 packet=deepcopy(template);packet['vertices']=[[u,u] for u in knots];packet['source_lifts']=[[u,'0','0'] for u in knots]
 session=FullSegmentSession();boot=session.bootstrap(plan,case,retain_lift=True)
 assert verify_full_segment(session._state,packet['vertices'],packet)['cells']==len(knots)-1
 receipt=session.attach_full_segment(boot['handle'],boot['state'],packet['vertices'],packet)
 nodes.append((session,receipt,packet))
assert all(packet['migration_binding']==root for _,_,packet in nodes)
def formula(i):
 s,r,p=nodes[i];s._current(r['handle'])
 assert s._state.migration_binding==root
 assert verify_full_segment(s._state,p['vertices'],p)['cells']==len(p['vertices'])-1
 # Verified affine cells with all vertex images (u,0,0) imply this formula
 # on the entire closed interval, not merely on probe points.
 assert all(Q(v[0])==Q(v[1]) and tuple(map(Q,t))==(Q(v[0]),Q(0),Q(0)) for v,t in zip(p['vertices'],p['source_lifts']))
 assert tuple(map(Q,p['vertices'][0]))==(0,0) and tuple(map(Q,p['vertices'][-1]))==(1,1)
 return (root,('0','1'),('(u,u)','(u,0,0)'))
def compare(i,j):
 a,b=formula(i),formula(j);assert a==b
 return a
assert compare(0,2)==compare(0,1)==compare(1,2)
refused=[]
def reject(label,fn):
 try:fn()
 except (AssertionError,ValueError,PermissionError):refused.append(label)
 else:raise AssertionError('accepted '+label)
for mode in ('missing-coverage','negative-coverage','foreign-root','wrong-source'):
 bad=deepcopy(nodes[1][2])
 if mode=='missing-coverage':bad['coverage_weights'].pop()
 elif mode=='negative-coverage':bad['coverage_weights'][0][0]='-1'
 elif mode=='foreign-root':bad['migration_binding']='foreign'
 else:bad['source_lifts'][1]=['0','0','0']
 reject(mode,lambda bad=bad:verify_full_segment(nodes[1][0]._state,bad['vertices'],bad))
# Advance one provider: old comparison descriptor cannot resurrect its handle.
s,r,_=nodes[0];answer=s._state.refine([1,0],'3/4').maximize([1,0])
s.advance(r['handle'],r['state'],{'kind':'append-public','normal':['1','0'],'upper':'3/4'},[1,0],answer)
reject('stale-generation',lambda:compare(0,2))
assert compare(1,2)==(root,('0','1'),('(u,u)','(u,0,0)'))
report={'passed':True,'checked_meshes':3,'direct_equals_staged':True,'whole_section_scope':'(u,u), 0<=u<=1','rejections':refused,'scope':'Rank-one forced-zero owning migration; exact full-segment coverage, vertex source checks and live generation; not a general triangulation transport or authority transfer.'}
(V/'results/whole-section-comparison.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
