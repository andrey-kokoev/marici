"""Independent anchored flow, potential and moment-Farkas verification."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,copy
if not __debug__:raise RuntimeError('Verification requires assertions enabled')
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
cp=R/'active-cap-moment-flow-contract.json';contract=json.loads(cp.read_text());packet=json.loads(gzip.decompress((R/'active-cap-moment-flows.json.gz').read_bytes()))
assert sha(cp)==packet['contract_sha256']
for p,h in packet['bindings'].items():assert sha(Path(p))==h

def expected(m):
 scale=[Q(1+j%3) for j in range(m)];rates=[Q(1,128**j) for j in range(m)];edges=[]
 for j in range(m):edges.extend([(0,j+1,Q(100+2*j)/scale[j]),(j+1,0,Q(0))])
 edges.append((0,1,Q(1)))
 for j in range(m-1):edges.extend([(j+1,j+2,Q(20)),(j+2,j+1,-Q(1,2))])
 T=[tuple(scale[j]*int(j==0) for j in range(m)),tuple(scale[j]*int(j==m-1) for j in range(m)),tuple(scale),tuple(s*r for s,r in zip(scale,rates))]
 return scale,rates,edges,T

def primal(m,p):
 scale,rates,edges,T=expected(m);assert len(p)==m+1 and p[0]==0
 assert all(p[v]-p[u]<=w for u,v,w in edges)
 raw=tuple(scale[j]*p[j+1] for j in range(m));assert all(0<=x<=100+2*j for j,x in enumerate(raw))
 return raw,tuple(dot(row,p[1:]) for row in T)

def divergence(m,edges,f):
 assert len(f)==len(edges) and all(v>=0 for v in f);normal=[Q(0)]*(m+1)
 for value,(u,v,w) in zip(f,edges):normal[v]+=value;normal[u]-=value
 return tuple(normal),sum(value*w for value,(u,v,w) in zip(f,edges))

def support(m,objective,answer):
 s,r,edges,T=expected(m);assert tuple(map(Q,answer['objective']))==objective
 q=tuple(sum(objective[i]*T[i][j] for i in range(4)) for j in range(m));q=(-sum(q),*q)
 f=tuple(map(Q,answer['flow']));normal,value=divergence(m,edges,f);assert normal==q
 raw,point=primal(m,tuple(map(Q,answer['potential'])));assert raw==tuple(map(Q,answer['source_lift']))
 assert dot(objective,point)==value==Q(answer['value'])
 # Complementary slackness follows numerically from the two exact bounds.
 p=tuple(map(Q,answer['potential']));assert all(weight*(w-p[v]+p[u])==0 for weight,(u,v,w) in zip(f,edges))

assert [c['m'] for c in packet['cases']]==contract['m_values']
for case in packet['cases']:
 m=case['m'];assert len(case['supports'])==len(contract['objectives'])
 for request,answer in zip(contract['objectives'],case['supports']):
  assert answer['status']=='OPTIMUM';support(m,tuple(map(Q,request)),answer);support(m,tuple(map(Q,request)),answer['reference']);assert answer['value']==answer['reference']['value']
 assert len(case['membership'])==2
 for member in case['membership']:
  raw,point=primal(m,tuple(map(Q,member['potential'])));assert point==tuple(map(Q,member['point']))
 s,r,edges,T=expected(m);relaxed=tuple(1+20*j for j in range(m));uncapped=sum(a*z for a,z in zip(s,relaxed));assert uncapped==Q(case['uncapped_U'])>Q(case['supports'][0]['value'])
 assert s[2]*relaxed[2]>104 and all(Q(1,2)<=relaxed[j]-relaxed[j-1]<=20 for j in range(1,m))
 f=tuple(map(Q,case['supports'][0]['flow']));t=tuple(map(Q,case['supports'][0]['source_lift']));assert any(f[2*j]>0 and t[j]==100+2*j for j in range(1,m))

# Moment-constrained infeasibility, not merely graph infeasibility.
def separation(answer):
 assert answer['m']==4;s,r,edges,T=expected(4);candidate=(Q(1),Q(42),Q(120),Q(60));z=tuple(a/b for a,b in zip(candidate,s));point=tuple(dot(a,z) for a in T)
 assert tuple(map(Q,answer['excluded_raw_source']))==candidate and tuple(map(Q,answer['point']))==point
 assert all(z[v-1]-z[u-1]<=w for u,v,w in edges if u and v)
 assert all(0<=v<=100+2*j for j,v in enumerate(candidate) if j!=2) and candidate[2]>104
 flow=tuple(map(Q,answer['flow']));eta=tuple(map(Q,answer['moment_multipliers']));assert len(eta)==4
 normal,bound=divergence(4,edges,flow);moment_normal=tuple(sum(eta[i]*T[i][j] for i in range(4)) for j in range(4));moment_normal=(-sum(moment_normal),*moment_normal)
 assert all(a+b==0 for a,b in zip(normal,moment_normal)) and bound+dot(eta,point)<0
 cut=tuple(map(Q,answer['cut_normal']));assert cut==tuple(-v for v in eta) and bound==Q(answer['cut_upper'])==104 and dot(cut,point)==120
separation(packet['separation'])

def negative_cycle(answer):
 assert answer['m']==4 and answer['added_edges']==[[1,2,'0'],[2,1,'-1']] and answer['cycle_nodes']==[1,2,1]
 weights=list(map(Q,answer['cycle_weights']));assert weights==[Q(0),Q(-1)] and sum(weights)<0
 for i,(u,v,w) in enumerate(answer['added_edges']):assert (u,v)==tuple(answer['cycle_nodes'][i:i+2]) and weights[i]==Q(w)
 result=answer['network_result'];assert result['status']=='INCONSISTENT';edges=expected(4)[2]+[(1,2,Q(0)),(2,1,Q(-1))];cycle=result['cycle_edges'];assert cycle and all(0<=i<len(edges) for i in cycle)
 assert all(edges[cycle[i]][1]==edges[cycle[(i+1)%len(cycle)]][0] for i in range(len(cycle))) and sum(edges[i][2] for i in cycle)<0
negative_cycle(packet['negative_cycle'])

def reject(f,x):
 try:f(x)
 except (AssertionError,IndexError,KeyError):return
 raise AssertionError('invalid certificate accepted')
case=packet['cases'][0];a=tuple(map(Q,contract['objectives'][0]));verify=lambda x:support(4,a,x)
bad=copy.deepcopy(case['supports'][0]);bad['flow'][0]='-1';reject(verify,bad)
bad=copy.deepcopy(case['supports'][0]);bad['flow'].pop(4);reject(verify,bad)
bad=copy.deepcopy(case['supports'][0]);bad['objective'][2]='2';reject(verify,bad)
bad=copy.deepcopy(case['supports'][0]);bad['source_lift'][2]='105';reject(verify,bad)
bad=copy.deepcopy(packet['separation']);bad['moment_multipliers'][0]='0';reject(separation,bad)
bad=copy.deepcopy(packet['separation']);bad['cut_upper']='120';reject(separation,bad)
bad=copy.deepcopy(packet['negative_cycle']);bad['cycle_weights'][1]='1';reject(negative_cycle,bad)
print('PASS: 15 exact network support flows and matching independently checked LP references, six moment-membership lifts, hidden-cap separating Farkas proof, negative cycle and seven rejection controls')
