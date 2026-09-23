"""Independent exact block geometry/query/gluing replay; no solver import."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,copy
if not __debug__:raise RuntimeError('Verification requires assertions enabled')
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def dec(row):return tuple(map(Q,row['normal'])),Q(row['upper'])
cp=R/'moment-chain-contract.json';contract=json.loads(cp.read_text());packet=json.loads(gzip.decompress((R/'moment-chain-interface.json.gz').read_bytes()))
assert sha(cp)==packet['contract_sha256']
for p,h in packet['bindings'].items():assert sha(Path(p))==h

def model(left,right):
 ids=list(range(left,right+1));s=[Q(1+j%3) for j in ids];r=[Q(1,128**j) for j in ids];m=len(ids)
 def obs(t):return (t[0],t[-1],sum(t),dot(r,t))
 low=[s[i]*Q(j,8) for i,j in enumerate(ids)]
 vectors=[tuple(s[j] if j>=i else Q(0) for j in range(m)) for i in range(m)]
 columns=[obs(v) for v in vectors];caps=[1+Q(left,8)]+[Q(1,8)]*(m-1)
 def support(a):return dot(a,obs(low))+sum(b*max(Q(0),dot(a,v)) for b,v in zip(caps,columns))
 def check_lift(raw,point=None):
  t=tuple(map(Q,raw));assert len(t)==m and all(0<=v<=100+2*j for v,j in zip(t,ids));z=[v/scale for v,scale in zip(t,s)]
  assert Q(left,8)<=z[0]<=1+Q(left,4) and all(Q(1,8)<=z[i]-z[i-1]<=Q(1,4) for i in range(1,m))
  if point is not None:assert obs(t)==point
  return t
 assert all(0<=lo and lo+sum(b*v[j] for b,v in zip(caps,vectors))<=100+2*ids[j] for j,lo in enumerate(low))
 return {'ids':ids,'s':s,'r':r,'low':low,'vectors':vectors,'columns':columns,'caps':caps,'support':support,'observe':obs,'lift':check_lift}

def verify_block(block):
 m=block['m'];M=model(0,m-1);facets={row['id']:dec(row) for row in block['facets']};n=m-1
 expected_ids={f'base:{s}' for s in (-1,1)}|{f'pair:{i}:{j}:{s}' for i in range(n) for j in range(i+1,n) for s in (-1,1)}
 assert set(facets)==expected_ids and len(block['facets'])==n*(n-1)+2
 for name,(a,b) in facets.items():
  assert len(a)==4 and M['support'](a)==b
  parts=name.split(':');sign=int(parts[-1])
  if parts[0]=='base':assert a==(Q(sign)/M['s'][0],Q(0),Q(0),Q(0))
  else:
   i,j=int(parts[1])+1,int(parts[2])+1
   # Unique normalized annihilator of the base column and exactly two
   # increment columns. No cross-product constructor is imported/replayed.
   assert a[1]*M['s'][-1]==-sign
   zeros={k for k,v in enumerate(M['columns']) if dot(a,v)==0};assert zeros=={0,i,j}
   if sign==1:assert tuple(-v for v in a)==facets[f'pair:{i-1}:{j-1}:-1'][0]
 assert len(block['support'])==8
 for record in block['support']:
  c=tuple(map(Q,record['objective']));value=Q(record['value']);t=M['lift'](record['source_lift']);assert M['support'](c)==value==dot(c,M['observe'](t))
 assert len(block['membership'])==4
 for record in block['membership']:
  p=tuple(map(Q,record['point']));answer=record['answer']
  if 'source_lift' in answer:M['lift'](answer['source_lift'],p)
  else:a,b=facets[answer['cut']];assert dot(a,p)>b
 assert len(block['queries'])==(3 if m in contract['refined_m'] else 0)
 center=M['observe'](tuple(lo+sum(b*v[j]/2 for b,v in zip(M['caps'],M['vectors'])) for j,lo in enumerate(M['low'])))
 history=[((Q(1),Q(0),Q(0),Q(0)),center[0])];objective=(Q(0),Q(0),Q(1),Q(0))
 for step,query in enumerate(block['queries']):
  if step==1:history.append(((Q(0),Q(0),Q(1),Q(1)),center[2]+center[3]))
  if step==2:history.append(((Q(-1),Q(0),Q(0),Q(0)),-Q(3,4)))
  assert list(map(dec,query['frames']))==history and tuple(map(Q,query['objective']))==objective
  result=query['answer'];rows=[]
  for j in range(4):
   for sign in (-1,1):
    a=tuple(Q(sign*int(i==j)) for i in range(4));rows.append((a,M['support'](a),f'box:{j}:{sign}'))
  rows += [(a,b,f'frame:{i}') for i,(a,b) in enumerate(history)];used=set()
  for cut in result['trace']:
   p=tuple(map(Q,cut['point']));name=cut['cut'];assert name not in used and all(dot(a,p)<=b for a,b,label in rows);used.add(name)
   a,b=facets[name];assert dot(a,p)>b;rows.append((a,b,name))
  if result['rows'][-1]['label']=='support:objective':rows.append((objective,M['support'](objective),'support:objective'))
  assert [(a,b,row['label']) for row in result['rows'] for a,b in [dec(row)]]==rows and len(used)<=len(facets)
  weights=list(map(Q,result['multipliers']));assert len(weights)==len(rows) and all(w>=0 for w in weights)
  normal=tuple(sum(w*a[j] for w,(a,b,label) in zip(weights,rows)) for j in range(4));bound=sum(w*b for w,(a,b,label) in zip(weights,rows))
  assert (result['status']=='INCONSISTENT')==(step==2)
  if step==2:assert all(v>=0 for v in normal) and bound<0
  else:
   assert result['status']=='OPTIMUM';p=tuple(map(Q,result['point']));M['lift'](result['source_lift'],p)
   assert all(dot(a,p)<=b for a,b in history) and all(a>=b for a,b in zip(normal,objective)) and bound==dot(objective,p)==Q(result['value'])

def verify_composition(case):
 m=case['m'];split=(m-1)//2;assert case['split']==split;G=model(0,m-1);L=model(0,split);Rr=model(split,m-1);rate=Q(1,128**split)
 assert len(case['samples'])==3 and len(case['bounds'])==4
 for sample in case['samples']:
  p=tuple(map(Q,sample['global_point']));pl=tuple(map(Q,sample['left_point']));pr=tuple(map(Q,sample['right_point']))
  l=L['lift'](sample['left_lift'],pl);r=Rr['lift'](sample['right_lift'],pr);assert l[-1]==r[0]==pl[1]==pr[0]
  glued=l+r[1:];assert glued==tuple(map(Q,sample['glued']));G['lift'](glued,p)
  assert p==(pl[0],pr[1],pl[2]+pr[2]-pl[1],pl[3]+pr[3]-rate*pl[1])
 for record in case['bounds']:
  c=tuple(map(Q,record['objective']));cu,cv=c[2:];cl=(Q(0),-cu-cv*rate,cu,cv);cr=(Q(0),Q(0),cu,cv)
  assert tuple(map(Q,record['left_objective']))==cl and tuple(map(Q,record['right_objective']))==cr
  vl=L['support'](cl);vr=Rr['support'](cr);v=G['support'](c)
  assert vl==Q(record['left_bound']) and vr==Q(record['right_bound']) and vl+vr==v==Q(record['global_bound'])
  t=G['lift'](record['source_lift']);assert dot(c,G['observe'](t))==v and dot(cl,L['observe'](t[:split+1]))==vl and dot(cr,Rr['observe'](t[split:]))==vr

assert [b['m'] for b in packet['blocks']]==contract['m_values']
for block in packet['blocks']:verify_block(block)
assert [c['m'] for c in packet['compositions']]==contract['composition_m']
for case in packet['compositions']:verify_composition(case)
def verify_composed_query(case):
 m=contract['composed_query_m'];assert case['m']==m;split=(m-1)//2;models={'L':model(0,split),'R':model(split,m-1)};maps={'L':(0,1,3,4),'R':(1,2,5,6)};rate=Q(1,128**split)
 reference=next(b for b in packet['blocks'] if b['m']==m)['queries'][case['query_index']];frames=list(map(dec,reference['frames']));objective=tuple(map(Q,reference['objective']))
 def pull(a):return (a[0],-a[2]-rate*a[3],a[1],a[2],a[3],a[2],a[3])
 def embed(a,side):
  out=[Q(0)]*7
  for i,j in enumerate(maps[side]):out[j]=a[i]
  return tuple(out)
 expected=[]
 for side in ('L','R'):
  for i in range(4):
   for sign in (-1,1):
    a=tuple(Q(sign*int(j==i)) for j in range(4));expected.append((embed(a,side),models[side]['support'](a),f'{side}:box:{i}:{sign}'))
 expected += [(pull(a),b,f'frame:{i}') for i,(a,b) in enumerate(frames)]
 answer=case['answer'];allrows=[(*dec(row),row['label']) for row in answer['rows']];assert allrows[:len(expected)]==expected;seen=set()
 for step in answer['trace']:
  p=tuple(map(Q,step['allocation']));assert len(p)==7;label=step['cut'];assert label not in seen and all(dot(a,p)<=b for a,b,name in expected);seen.add(label)
  a,b,name=allrows[len(expected)];assert name==label and dot(a,p)>b;parts=label.split(':');side=parts[0];M=models[side];local=tuple(a[j] for j in maps[side]);assert embed(local,side)==a and M['support'](local)==b
  sign=int(parts[-1]);assert sign in (-1,1)
  if parts[1]=='base':assert local==(Q(sign)/M['s'][0],Q(0),Q(0),Q(0))
  else:
   assert parts[1]=='pair';i,j=int(parts[2])+1,int(parts[3])+1
   assert 1<=i<j<len(M['columns']) and local[1]*M['s'][-1]==-sign
   assert {k for k,v in enumerate(M['columns']) if dot(local,v)==0}=={0,i,j}
  expected.append((a,b,name))
 assert expected==allrows;assert answer['dictionary_size']==sum((len(M['ids'])-1)*(len(M['ids'])-2)+2 for M in models.values()) and len(seen)<=answer['dictionary_size']
 weights=list(map(Q,answer['multipliers']));assert len(weights)==len(expected) and all(w>=0 for w in weights)
 normal=tuple(sum(w*a[j] for w,(a,b,label) in zip(weights,expected)) for j in range(7));upper=sum(w*b for w,(a,b,label) in zip(weights,expected))
 assert answer['status']=='OPTIMUM';allocation=tuple(map(Q,answer['allocation']));public=tuple(map(Q,answer['point']))
 l=models['L']['lift'](answer['left_lift'],tuple(allocation[j] for j in maps['L']));r=models['R']['lift'](answer['right_lift'],tuple(allocation[j] for j in maps['R']))
 assert l[-1]==r[0];model(0,m-1)['lift'](l+r[1:],public)
 assert public==(allocation[0],allocation[2],allocation[3]+allocation[5]-allocation[1],allocation[4]+allocation[6]-rate*allocation[1])
 assert all(dot(a,public)<=b for a,b in frames) and all(a>=b for a,b in zip(normal,pull(objective)))
 assert upper==dot(objective,public)==Q(answer['value'])==Q(reference['answer']['value'])
assert [(c['m'],c['query_index']) for c in packet['composed_queries']]==[(contract['composed_query_m'],i) for i in (0,1)]
for case in packet['composed_queries']:verify_composed_query(case)

def reject(f,x):
 try:f(x)
 except (AssertionError,IndexError,KeyError):return
 raise AssertionError('corruption accepted')
bad=copy.deepcopy(packet['blocks'][0]);bad['facets'].pop();reject(verify_block,bad)
bad=copy.deepcopy(packet['blocks'][0]);bad['facets'][0]['upper']='999';reject(verify_block,bad)
bad=copy.deepcopy(packet['blocks'][0]);bad['queries'][0]['frames'].pop();reject(verify_block,bad)
bad=copy.deepcopy(packet['compositions'][0]);bad['samples'][1]['right_lift'][0]='0';reject(verify_composition,bad)
bad=copy.deepcopy(packet['compositions'][0]);bad['samples'][1]['global_point'][2]=str(Q(bad['samples'][1]['global_point'][2])+Q(bad['samples'][1]['left_point'][1]));reject(verify_composition,bad)
bad=copy.deepcopy(packet['compositions'][0]);bad['bounds'][0]['left_objective'][1]='0';reject(verify_composition,bad)
print('PASS: five exact moment-aware facet dictionaries, support/membership, nine refined queries, nine glued witnesses, twelve composed support bounds, two lifted allocation optimizations, six rejection controls')
