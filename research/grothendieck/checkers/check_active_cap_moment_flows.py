"""Active-cap chains: exact potential/flow certificates and moment membership.
The network solves support; SymPy supplies comparison and membership proposals.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib
from joint_audit_tail_interface import lp,dot
from active_cap_network_support import support as network_support
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def build(m):
 s=[Q(1+j%3) for j in range(m)];r=[Q(1,128**j) for j in range(m)];edges=[]
 for j in range(m):edges.extend([(0,j+1,Q(100+2*j)/s[j]),(j+1,0,Q(0))])
 edges.append((0,1,Q(1)))
 for j in range(m-1):edges.extend([(j+1,j+2,Q(20)),(j+2,j+1,-Q(1,2))])
 A=[tuple(Q(int(j+1==v)-int(j+1==u)) for j in range(m)) for u,v,w in edges];b=[w for u,v,w in edges]
 T=[tuple(s[j]*int(j==0) for j in range(m)),tuple(s[j]*int(j==m-1) for j in range(m)),tuple(s),tuple(a*b for a,b in zip(s,r))]
 return s,r,edges,A,b,T

def exactify(A,weights,target,m):
 w=list(map(Q,weights));slack=[sum(w[i]*A[i][j] for i in range(len(A)))-target[j] for j in range(m)];assert all(v>=0 for v in slack)
 # Original odd-index rows are z_j>=0, with zero bound.
 for j,v in enumerate(slack):w[2*j+1]+=v
 assert all(sum(w[i]*A[i][j] for i in range(len(A)))==target[j] for j in range(m))
 return w

contract={'schema':'active-cap-moment-flow-contract.v1','m_values':[4,8,16],'chart':'s_j=1+(j mod 3)','initial_upper':'1','increment_bounds':['1/2','20'],'objectives':[['0','0','1','0'],['0','0','0','1'],['0','0','1','-200'],['1','-1','1','-200'],['-1','1','-1','100']],'observer':['first raw atom','last raw atom','U','V'],'scope':'exact residual-network support proposals compared with source LP; moment membership uses source LP; no polynomial augmentation or projected finite-cut guarantee'}
cp=R/'active-cap-moment-flow-contract.json';cp.write_text(json.dumps(contract,indent=2)+'\n');cases=[]
for m in contract['m_values']:
 s,r,edges,A,b,T=build(m);supports=[];members=[]
 for raw in contract['objectives']:
  a=tuple(map(Q,raw));q=tuple(sum(a[i]*T[i][j] for i in range(4)) for j in range(m));p=lp(A,b,q);assert p['status']=='OPTIMUM'
  flow=exactify(A,p['multipliers'],q,m);z=tuple(map(Q,p['point']));t=tuple(x*y for x,y in zip(s,z));value=Q(p['value'])
  assert dot(b,flow)==value
  reference={'objective':raw,'potential':['0']+list(map(str,z)),'source_lift':list(map(str,t)),'flow':list(map(str,flow)),'value':str(value)}
  network=network_support(edges,(-sum(q),*q));assert network['status']=='OPTIMUM' and Q(network['value'])==value
  potential=tuple(map(Q,network['potential']));network['source_lift']=list(map(str,[a*v for a,v in zip(s,potential[1:])]))
  supports.append({**network,'objective':raw,'reference':reference})
 # Feasible membership is solved with four observation equalities, not inferred
 # from graph closure or from a nominal inversion.
 for z in (tuple(Q(j,2) for j in range(m)),tuple(map(Q,supports[0]['potential'][1:]))):
  point=tuple(dot(row,z) for row in T);AA=list(A);bb=list(b)
  for row,value in zip(T,point):
   for sign in (-1,1):AA.append(tuple(sign*x for x in row));bb.append(sign*value)
  p=lp(AA,bb,(Q(0),)*m);assert p['status']=='OPTIMUM';answer=tuple(map(Q,p['point']))
  members.append({'point':list(map(str,point)),'potential':['0']+list(map(str,answer))})
 # Without source upper caps, the all-upper increment corner is admitted.
 relaxed=tuple(1+20*j for j in range(m));assert s[2]*relaxed[2]>104
 assert Q(supports[0]['value'])<sum(a*z for a,z in zip(s,relaxed))
 assert any(Q(supports[0]['flow'][2*j])>0 for j in range(1,m))
 cases.append({'m':m,'supports':supports,'membership':members,'uncapped_U':str(sum(a*z for a,z in zip(s,relaxed)))})
# Hidden active cap: both endpoint values obey their caps, all chain edges
# hold, but the moments force atom 2 above cap. No operational failure is
# needed to obtain this exact source-space Farkas separator.
m=4;s,r,edges,A,b,T=build(m);z=(Q(1),Q(21),Q(40),Q(60));point=tuple(dot(row,z) for row in T);gap=r[1]-r[2]
cut=((r[0]-r[1])/gap,(r[3]-r[1])/gap,r[1]/gap,-1/gap)
eta=tuple(-v for v in cut);flow=[Q(0)]*len(edges);flow[4]=s[2]
assert all(sum(flow[i]*A[i][j] for i in range(len(A)))+sum(eta[k]*T[k][j] for k in range(4))==0 for j in range(m))
assert dot(b,flow)+dot(eta,point)<0
separation={'m':4,'point':list(map(str,point)),'flow':list(map(str,flow)),'moment_multipliers':list(map(str,eta)),'cut_normal':list(map(str,cut)),'cut_upper':'104','excluded_raw_source':list(map(str,[a*v for a,v in zip(s,z)]))}
# An explicitly contradictory gain-edge refinement has a two-edge negative cycle.
negative_cycle={'m':4,'added_edges':[[1,2,'0'],[2,1,'-1']],'cycle_nodes':[1,2,1],'cycle_weights':['0','-1']}
negative_cycle['network_result']=network_support(edges+[(1,2,Q(0)),(2,1,Q(-1))],(Q(0),)*5)
assert negative_cycle['network_result']['status']=='INCONSISTENT'
out={'schema':'active-cap-moment-flow-result.v1','contract_sha256':sha(cp),'cases':cases,'separation':separation,'negative_cycle':negative_cycle,'bindings':{str(p):sha(p) for p in (Path(__file__),HERE/'active_cap_network_support.py',HERE/'joint_audit_tail_interface.py',cp)},'counts':{'support_flows':sum(len(c['supports']) for c in cases),'membership_lifts':sum(len(c['membership']) for c in cases),'separating_farkas':1,'negative_cycles':1}}
(R/'active-cap-moment-flows.json.gz').write_bytes(gzip.compress(json.dumps(out,separators=(',',':')).encode(),mtime=0));print(out['counts'])
