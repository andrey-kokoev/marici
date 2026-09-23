"""Moment-aware balanced-gain block geometry and certified query controls."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib
from moment_chain_interface import MomentChain,dot
from composed_moment_chain import maximize as composed_maximize
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def enc(a,b):return {'normal':list(map(str,a)),'upper':str(b)}
contract={'schema':'moment-chain-contract.v1','m_values':[4,5,8,16,32],'refined_m':[4,5,8],'composition_m':[8,16,32],'composed_query_m':8,'scale':'s_j=1+(j mod 3)','increment_interval':['1/8','1/4'],'global_initial_interval':['0','1'],'observer':['left atom','right atom','U','V'],'scope':'owning atom caps with admitted cap-redundant gain-chain evidence; no arbitrary gain cycles or active-cap theorem'}
cp=R/'moment-chain-contract.json';cp.write_text(json.dumps(contract,indent=2)+'\n');blocks=[]
for m in contract['m_values']:
 model=MomentChain(0,m-1);facets=[{'id':name,**enc(a,b)} for name,(a,b) in model.cuts()];assert len(facets)==model.dictionary_size()
 support=[]
 for j in range(4):
  for sign in (-1,1):
   a=tuple(Q(sign*int(i==j)) for i in range(4));value,t=model.support(a);support.append({'objective':list(map(str,a)),'value':str(value),'source_lift':list(map(str,t))})
 membership=[]
 for ratio in (Q(0),Q(1,2),Q(1)):
  t=model.source(tuple(ratio*b for b in model.caps));point=model.observe(t);answer=model.oracle(point);assert 'source_lift' in answer
  membership.append({'point':list(map(str,point)),'answer':answer})
 outside=(-Q(1),Q(0),Q(0),Q(0));answer=model.oracle(outside);assert 'cut' in answer;membership.append({'point':list(map(str,outside)),'answer':answer})
 queries=[]
 if m in contract['refined_m']:
  center=model.observe(model.source(tuple(b/2 for b in model.caps)));unit=(Q(1),Q(0),Q(0),Q(0));mixed=(Q(0),Q(0),Q(1),Q(1));objective=(Q(0),Q(0),Q(1),Q(0))
  history=[(unit,center[0])]
  for step in range(3):
   if step==1:history.append((mixed,dot(mixed,center)))
   if step==2:history.append((tuple(-v for v in unit),-Q(3,4)))
   result=model.maximize(tuple(history),objective);assert (result['status']=='INCONSISTENT')==(step==2)
   queries.append({'frames':[enc(a,b) for a,b in history],'objective':list(map(str,objective)),'answer':result})
 blocks.append({'m':m,'facets':facets,'support':support,'membership':membership,'queries':queries})
compositions=[]
for m in contract['composition_m']:
 split=(m-1)//2;whole=MomentChain(0,m-1);left=MomentChain(0,split);right=MomentChain(split,m-1);samples=[]
 for ratio in (Q(0),Q(1,2),Q(1)):
  t=whole.source(tuple(ratio*b for b in whole.caps));global_point=whole.observe(t);a=left.observe(t[:split+1]);b=right.observe(t[split:])
  l=tuple(map(Q,left.oracle(a)['source_lift']));r=tuple(map(Q,right.oracle(b)['source_lift']));assert l[-1]==r[0];glued=l+r[1:]
  assert whole.observe(glued)==global_point
  assert global_point[2]==a[2]+b[2]-a[1] and global_point[3]==a[3]+b[3]-Q(1,128**split)*a[1]
  samples.append({'global_point':list(map(str,global_point)),'left_point':list(map(str,a)),'right_point':list(map(str,b)),'left_lift':list(map(str,l)),'right_lift':list(map(str,r)),'glued':list(map(str,glued))})
 bounds=[]
 for j in (2,3):
  for sign in (-1,1):
   c=tuple(Q(sign*int(k==j)) for k in range(4));cu,cv=c[2:];cl=(Q(0),-cu-cv*Q(1,128**split),cu,cv);cr=(Q(0),Q(0),cu,cv)
   vl,_=left.support(cl);vr,_=right.support(cr);v,t=whole.support(c);assert vl+vr==v
   bounds.append({'objective':list(map(str,c)),'left_objective':list(map(str,cl)),'right_objective':list(map(str,cr)),'left_bound':str(vl),'right_bound':str(vr),'global_bound':str(v),'source_lift':list(map(str,t))})
 compositions.append({'m':m,'split':split,'samples':samples,'bounds':bounds})
composed_queries=[]
m=contract['composed_query_m'];split=(m-1)//2;left=MomentChain(0,split);right=MomentChain(split,m-1)
reference=next(block for block in blocks if block['m']==m)
for qi in (0,1):
 query=reference['queries'][qi];frames=[(tuple(map(Q,f['normal'])),Q(f['upper'])) for f in query['frames']];objective=tuple(map(Q,query['objective']))
 answer=composed_maximize(left,right,frames,objective);assert answer['status']=='OPTIMUM' and answer['value']==query['answer']['value']
 composed_queries.append({'m':m,'query_index':qi,'answer':answer})
out={'schema':'moment-chain-result.v1','contract_sha256':sha(cp),'blocks':blocks,'compositions':compositions,'composed_queries':composed_queries,'bindings':{str(p):sha(p) for p in (Path(__file__),HERE/'moment_chain_interface.py',HERE/'composed_moment_chain.py',HERE/'joint_audit_tail_interface.py',cp)},'counts':{'blocks':len(blocks),'facets':[len(b['facets']) for b in blocks],'refined_queries':sum(len(b['queries']) for b in blocks),'glued_witnesses':sum(len(c['samples']) for c in compositions),'max_cut_additions':max(len(q['answer']['trace']) for b in blocks for q in b['queries'])}}
(R/'moment-chain-interface.json.gz').write_bytes(gzip.compress(json.dumps(out,separators=(',',':')).encode(),mtime=0));print(out['counts'])
