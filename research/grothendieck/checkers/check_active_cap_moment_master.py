"""Frozen network-priced membership and compositional allocation workload."""
from pathlib import Path
from fractions import Fraction as Q
import gzip,json,hashlib
from active_cap_moment_master import Block,query
from finite_master_lp import maximize
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def frame(a,b):return {'normal':list(map(str,a)),'upper':str(b)}
zero=(Q(0),)*4;U=(Q(0),Q(0),Q(1),Q(0));left=(Q(1),Q(0),Q(0),Q(0));mixed=(Q(0),Q(0),Q(1),Q(1))
small=Block(0,3);hidden=small.observe((Q(1),Q(16),Q(36),Q(45)));low=small.observe((Q(1),Q(18),Q(104,3),Q(45)))
whole=Block(0,7);maximum=whole.price(U)[0];centre=whole.observe(tuple((maximum[j]+Q(j,2))/2 for j in range(8)));coupled=[frame(left,Q(1,2)),frame(mixed,centre[2]+centre[3])]
specs=[
 {'name':'hidden-active-cap','intervals':[[0,3]],'point':list(map(str,hidden)),'without_V_witness':['1','36','104','45'],'objective':list(map(str,zero)),'frames':[],'expected':'INCONSISTENT'},
 {'name':'feasible-membership','intervals':[[0,3]],'point':list(map(str,low)),'objective':list(map(str,zero)),'frames':[],'expected':'OPTIMUM'},
 {'name':'two-block-support','intervals':[[0,3],[3,7]],'objective':list(map(str,U)),'frames':[],'expected':'OPTIMUM'},
 {'name':'two-block-coupled','intervals':[[0,3],[3,7]],'objective':list(map(str,U)),'frames':coupled,'expected':'OPTIMUM'},
 {'name':'three-block-coupled','intervals':[[0,2],[2,4],[4,7]],'objective':list(map(str,U)),'frames':coupled,'expected':'OPTIMUM'},
 {'name':'local-frame-allocation','intervals':[[0,3],[3,7]],'objective':list(map(str,U)),'frames':[],'local_frames':[{'block':0,**frame(U,Q(70))}],'expected':'OPTIMUM'},
 {'name':'contradictory-history','intervals':[[0,3],[3,7]],'objective':list(map(str,U)),'frames':[frame(left,Q(1,2)),frame(tuple(-v for v in left),-Q(3,4))],'expected':'INCONSISTENT'}]
contract={'schema':'active-cap-moment-master-contract.v1','grid_denominator':6,'source':'owning caps; global chart 1+j%3; initial z_0<=1; neighbor increments [1/2,20]','requests':specs,'scope':'finite source-grid pricing progress; exact restricted-master LP required; no polynomial column-count claim'}
cp=R/'active-cap-moment-master-contract.json';cp.write_text(json.dumps(contract,indent=2)+'\n');answers=[]
for spec in specs:
 blocks=[Block(*interval) for interval in spec['intervals']];frames=[(tuple(map(Q,f['normal'])),Q(f['upper'])) for f in spec['frames']]
 result=query(blocks,frames,tuple(map(Q,spec['objective'])),None if 'point' not in spec else tuple(map(Q,spec['point'])),local_frames=[(f['block'],tuple(map(Q,f['normal'])),Q(f['upper'])) for f in spec.get('local_frames',[])]);assert result['status']==spec['expected']
 answers.append(result);print(spec['name'],result['status'],len(result['columns']),len(result['trace']),flush=True)
assert answers[2]['value']==whole.price(U)[1]['value'] and answers[3]['value']==answers[4]['value']
fallback_controls=[]
for kind in ('raised','false-inconsistency'):
 def bad_proposer(A,b,c):
  if kind=='raised':raise RuntimeError('forced control')
  return {'status':'INCONSISTENT'}
 answer=maximize([[1,1],[1,0],[0,1]],[3,2,2],[2,1],bad_proposer);assert answer['value']=='5' and answer['master_method']=='FINITE_BASIS_FALLBACK';fallback_controls.append(answer)
packet={'schema':'active-cap-moment-master-result.v1','contract_sha256':sha(cp),'answers':answers,'fallback_controls':fallback_controls,'bindings':{str(p):sha(p) for p in (Path(__file__),HERE/'active_cap_moment_master.py',HERE/'active_cap_network_support.py',HERE/'finite_master_lp.py',HERE/'exact_master_simplex.py',cp)}}
(R/'active-cap-moment-master.json.gz').write_bytes(gzip.compress(json.dumps(packet,separators=(',',':')).encode(),mtime=0))
