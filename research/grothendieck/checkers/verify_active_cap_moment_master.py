"""Solver-free replay of network-priced masters and composed source proofs."""
from fractions import Fraction as Q
from pathlib import Path
import json,gzip,hashlib,copy
if not __debug__:raise RuntimeError('Assertions required')
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dot(a,b):return sum(x*y for x,y in zip(a,b))

def block(interval,extra_edges=()):
 l,r=interval;assert 0<=l<=r;ids=list(range(l,r+1));s=[Q(1+j%3) for j in ids];edges=[]
 for i,j in enumerate(ids):edges.extend([(0,i+1,Q(100+2*j)/s[i]),(i+1,0,Q(0))])
 if l==0:edges.append((0,1,Q(1)))
 for i in range(len(ids)-1):edges.extend([(i+1,i+2,Q(20)),(i+2,i+1,-Q(1,2))])
 for edge in extra_edges:
  assert set(edge)=={'block','tail','head','upper'} and (6*Q(edge['upper'])).denominator==1
  endpoints=[]
  for name in ('tail','head'):
   j=edge[name];assert j is None or (type(j)==int and j in ids);endpoints.append(0 if j is None else ids.index(j)+1)
  edges.append((*endpoints,Q(edge['upper'])))
 return ids,s,edges

def admitted(data,z,grid=False):
 ids,s,edges=data;assert len(z)==len(ids);p=(Q(0),*z)
 assert all(p[v]-p[u]<=w for u,v,w in edges)
 if grid:assert all((6*v).denominator==1 for v in z)
 raw=tuple(a*b for a,b in zip(s,z));assert all(0<=v<=100+2*j for v,j in zip(raw,ids));return raw

def verify_pricing(data,q,certificate):
 ids,s,edges=data;assert certificate['status']=='OPTIMUM';p=tuple(map(Q,certificate['potential']));assert len(p)==len(ids)+1 and p[0]==0;admitted(data,p[1:],True)
 f=tuple(map(Q,certificate['flow']));assert len(f)==len(edges) and all(v>=0 for v in f);normal=[Q(0)]*len(p)
 for weight,(u,v,bound) in zip(f,edges):normal[v]+=weight;normal[u]-=weight
 assert tuple(normal)==(-sum(q),*q)
 upper=sum(weight*bound for weight,(u,v,bound) in zip(f,edges));assert upper==dot(q,p[1:])==Q(certificate['value'])
 return p,upper

def verify(spec,answer,expected_seed=None,pricing_checker=None):
 B=len(spec['intervals']);fine=spec.get('fine_edges',[]);assert all(type(e['block'])==int and 0<=e['block']<B for e in fine)
 blocks=[block(interval,[e for e in fine if e['block']==b]) for b,interval in enumerate(spec['intervals'])];assert all(blocks[b][0][-1]==blocks[b+1][0][0] for b in range(B-1))
 zeros=[(Q(0),)*len(data[0]) for data in blocks]
 # Native source-node coefficients, independently avoiding the producer's
 # four-coordinate bookkeeping map. Charge each overlap's moments to its
 # right block, once, and retain both raw endpoint observations.
 def public(a):
  out=[]
  for b,(ids,s,edges) in enumerate(blocks):
   coeff=[]
   for i,j in enumerate(ids):
    v=a[2]+a[3]*Q(1,128**j)
    if b<B-1 and i==len(ids)-1:v=Q(0)
    if b==0 and i==0:v+=a[0]
    if b==B-1 and i==len(ids)-1:v+=a[1]
    coeff.append(s[i]*v)
   out.append(tuple(coeff))
  return out
 rows=[]
 for b in range(B):
  for sign in (-1,1):rows.append((zeros,tuple(Q(sign*int(i==b)) for i in range(B)),Q(sign)))
 for b in range(B-1):
  for sign in (-1,1):
   a=[list(v) for v in zeros];a[b][-1]=sign*blocks[b][1][-1];a[b+1][0]=-sign*blocks[b+1][1][0];rows.append((a,(Q(0),)*B,Q(0)))
 for f in spec['frames']:rows.append((public(tuple(map(Q,f['normal']))),(Q(0),)*B,Q(f['upper'])))
 for f in spec.get('local_frames',[]):
  side=f['block'];local=tuple(map(Q,f['normal']));ids,s,edges=blocks[side];coeff=list(zeros)
  coeff[side]=tuple(s[j]*(local[0]*int(j==0)+local[1]*int(j==len(ids)-1)+local[2]+local[3]*Q(1,128**ids[j])) for j in range(len(ids)))
  rows.append((coeff,(Q(0),)*B,Q(f['upper'])))
 if 'point' in spec:
  for i,value in enumerate(map(Q,spec['point'])):
   for sign in (-1,1):rows.append((public(tuple(Q(sign*int(i==j)) for j in range(4))),(Q(0),)*B,sign*value))
 if 'without_V_witness' in spec:
  raw=tuple(map(Q,spec['without_V_witness']));ids,s,edges=blocks[0];admitted(blocks[0],tuple(v/scale for v,scale in zip(raw,s)))
  assert (raw[0],raw[-1],sum(raw))==tuple(map(Q,spec['point'][:3])) and sum(Q(1,128**j)*v for j,v in zip(ids,raw))!=Q(spec['point'][3])
 objective=tuple(map(Q,spec['objective']));cost=public(objective);bounds=[r[2] for r in rows]
 columns=[]
 for column in answer['columns']:
  b=column['block'];assert 0<=b<B;z=tuple(map(Q,column['potential']));admitted(blocks[b],z,True);columns.append((b,z))
 assert len(set(columns))==len(columns)
 if expected_seed is None:
  count=B;assert [b for b,z in columns[:B]]==list(range(B))
 else:
  seed=[(item['block'],tuple(map(Q,item['potential']))) for item in expected_seed];count=len(seed)
  assert count and columns[:count]==seed and {b for b,z in seed}==set(range(B))
 phase=1;seen=set(columns[:count]);assert answer['trace']
 for ti,entry in enumerate(answer['trace']):
  assert entry['phase']==phase and entry['columns']==count
  A=[[mass[b]+dot(coeff[b],z) for b,z in columns[:count]] for coeff,mass,bound in rows]
  artificial=list(range(2*B,len(rows))) if phase==1 else []
  for i,a in enumerate(A):a.extend(Q(-int(i==j)) for j in artificial)
  c=[Q(0) if phase==1 else dot(cost[b],z) for b,z in columns[:count]]+[-Q(1)]*len(artificial)
  master=entry['master'];assert master['status']=='OPTIMUM';x=tuple(map(Q,master['point']));w=tuple(map(Q,master['multipliers']));value=Q(master['value'])
  assert len(x)==len(c) and len(w)==len(rows) and all(v>=0 for v in x+w)
  assert all(dot(a,x)<=b for a,b in zip(A,bounds)) and all(sum(w[i]*A[i][j] for i in range(len(rows)))>=c[j] for j in range(len(c)))
  assert dot(c,x)==dot(w,bounds)==value
  assert len(entry['pricing'])==B;positive=[];flow_bounds=[]
  for b,record in enumerate(entry['pricing']):
   assert record['block']==b;ids,s,edges=blocks[b]
   q=tuple((Q(0) if phase==1 else cost[b][j])-sum(weight*coeff[b][j] for weight,(coeff,mass,bound) in zip(w,rows)) for j in range(len(ids)))
   alpha=sum(weight*mass[b] for weight,(coeff,mass,bound) in zip(w,rows));assert alpha==Q(record['threshold'])
   local=tuple(map(Q,record['objective']));assert len(local)==4
   advertised=tuple(s[j]*(local[0]*int(j==0)+local[1]*int(j==len(ids)-1)+local[2]+local[3]*Q(1,128**ids[j])) for j in range(len(ids)));assert advertised==q
   certificate=record['certificate'];p,upper=(pricing_checker or verify_pricing)(blocks[b],q,certificate);flow_bounds.append(upper)
   if upper>alpha:positive.append((b,p[1:]))
  if 'added' in entry:
   added=(entry['added']['block'],tuple(map(Q,entry['added']['potential'])))
   assert positive and added==positive[0] and added not in seen and columns[count]==added;seen.add(added);count+=1
  else:
   assert not positive
   # This is a direct source-space bound/Farkas combination: master mass
   # constants are replaced by valid local flow costs, not trusted cuts.
   combined=sum(flow_bounds)+sum(w[i]*bounds[i] for i in range(2*B,len(rows)))
   assert combined<=value
   if phase==1:
    assert value<=0
    if value<0:
     assert combined<0 and ti==len(answer['trace'])-1 and answer['status']=='INCONSISTENT'
     if 'point' in spec:
      start=len(rows)-8;eta=tuple(w[start+2*i+1]-w[start+2*i] for i in range(4));upper=sum(flow_bounds)+sum(w[i]*bounds[i] for i in range(2*B,start));cut=tuple(-v for v in eta)
      assert cut==tuple(map(Q,answer['separator']['normal'])) and upper==Q(answer['separator']['upper']) and dot(cut,tuple(map(Q,spec['point'])))>upper
    else:assert all(v==0 for v in x[count:]);phase=2
   else:
    assert ti==len(answer['trace'])-1 and answer['status']=='OPTIMUM' and value==Q(answer['value'])==combined
    lifts=[]
    for b,data in enumerate(blocks):
     z=tuple(sum(x[k]*col[j] for k,(side,col) in enumerate(columns[:count]) if side==b) for j in range(len(data[0])));lifts.append(admitted(data,z))
    assert lifts==[tuple(map(Q,t)) for t in answer['block_lifts']] and all(lifts[b][-1]==lifts[b+1][0] for b in range(B-1))
    glued=lifts[0]+tuple(v for t in lifts[1:] for v in t[1:]);assert glued==tuple(map(Q,answer['source_lift']))
    ids=list(range(blocks[0][0][0],blocks[-1][0][-1]+1));assert len(ids)==len(glued)
    # Also check the actual joined source, not merely the allocation equations.
    full=block([ids[0],ids[-1]]);admitted(full,tuple(v/s for v,s in zip(glued,full[1])))
    observed=(glued[0],glued[-1],sum(glued),sum(Q(1,128**j)*v for j,v in zip(ids,glued)))
    assert dot(objective,observed)==value
    if 'point' in spec:assert observed==tuple(map(Q,spec['point']))
    assert all(dot(tuple(map(Q,f['normal'])),observed)<=Q(f['upper']) for f in spec['frames'])
    for f in spec.get('local_frames',[]):
     b=f['block'];t=lifts[b];local=(t[0],t[-1],sum(t),sum(Q(1,128**j)*v for j,v in zip(blocks[b][0],t)))
     assert dot(tuple(map(Q,f['normal'])),local)<=Q(f['upper'])
 assert count==len(columns) and 'added' not in answer['trace'][-1]
 if 'expected' in spec:assert answer['status']==spec['expected']
 # Do not allow a transcript stopping after feasible Phase I without Phase II.
 assert answer['status'] in ('OPTIMUM','INCONSISTENT')
 if answer['status']=='OPTIMUM':assert answer['trace'][-1]['phase']==2
 else:assert answer['trace'][-1]['phase']==1 and Q(answer['trace'][-1]['master']['value'])<0

def main():
 cp=R/'active-cap-moment-master-contract.json';contract=json.loads(cp.read_text());packet=json.loads(gzip.decompress((R/'active-cap-moment-master.json.gz').read_bytes()))
 assert sha(cp)==packet['contract_sha256'] and contract['grid_denominator']==6
 for p,h in packet['bindings'].items():assert sha(Path(p))==h
 assert len(packet['fallback_controls'])==2
 for answer,failure in zip(packet['fallback_controls'],('RuntimeError','AssertionError')):
  assert answer['master_method']=='FINITE_BASIS_FALLBACK' and answer['proposal_failure']==failure and answer['status']=='OPTIMUM'
  x=tuple(map(Q,answer['point']));w=tuple(map(Q,answer['multipliers']));assert len(x)==2 and len(w)==3 and all(v>=0 for v in x+w)
  assert sum(x)<=3 and x[0]<=2 and x[1]<=2 and w[0]+w[1]>=2 and w[0]+w[2]>=1
  assert 2*x[0]+x[1]==3*w[0]+2*w[1]+2*w[2]==Q(answer['value'])==5
 specs=contract['requests'];assert len(packet['answers'])==len(specs)==7
 for spec,answer in zip(specs,packet['answers']):verify(spec,answer)
 assert packet['answers'][2]['value']=='1071/2' and packet['answers'][3]['value']==packet['answers'][4]['value']
 def reject(f,x):
  try:f(x)
  except (AssertionError,IndexError,KeyError):return
  raise AssertionError('corrupted proof accepted')
 spec=specs[3];answer=packet['answers'][3];check=lambda x:verify(spec,x)
 bad=copy.deepcopy(answer);bad['trace'][-1]['pricing'][0]['certificate']['flow'].pop();reject(check,bad)
 bad=copy.deepcopy(answer);bad['trace'][-1]['master']['multipliers'][0]='-1';reject(check,bad)
 bad=copy.deepcopy(answer);bad['columns'][0]['potential'][0]='1/7';reject(check,bad)
 bad=copy.deepcopy(answer);bad['block_lifts'][1][0]='0';reject(check,bad)
 bad=copy.deepcopy(answer);bad['value']=str(Q(bad['value'])+1);reject(check,bad)
 bad=copy.deepcopy(spec);bad['frames'].pop();reject(lambda s:verify(s,answer),bad)
 bad=copy.deepcopy(packet['answers'][0]);bad['trace'][-1]['master']['value']='0';reject(lambda x:verify(specs[0],x),bad)
 bad=copy.deepcopy(answer);bad['trace'][0]['added']['potential']=bad['columns'][0]['potential'];reject(check,bad)
 print('PASS: seven complete priced-master transcripts, two infeasible query slices, two-/three-block allocation agreement, source gluing, exact flow bounds, two finite-master fallback controls and eight rejection controls')

if __name__=='__main__':main()
