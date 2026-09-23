"""Owning m=4 fibers: pairwise compatibility does not imply a common lift."""
from fractions import Fraction as Q
from itertools import product,combinations
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
R=[Q(1,128**j) for j in range(4)];CENTER=[Q(50),Q(51),Q(52),Q(53)];DELTA=Q(1,128**4)
def lift(p,h,k):
 # Public U=Ucenter+delta*p, V=Vcenter. Fine parameters fix first two atoms.
 t0=CENTER[0]+DELTA*h;t1=CENTER[1]+DELTA*k
 u=sum(CENTER)+DELTA*p-t0-t1
 v=sum(a*b for a,b in zip(CENTER,R))-t0-R[1]*t1
 t2=(v-R[3]*u)/(R[2]-R[3]);return (t0,t1,t2,u-t2)
def holds(name,h,k):
 return 0<=h<=1 and 0<=k<=1 and {'A':h<=Q(1,4),'B':k<=Q(1,4),'C':h+k>=1}[name]
def main():
 corners=[]
 for p,h,k in product((Q(0),Q(1)),repeat=3):
  t=lift(p,h,k)
  assert all(0<x<100+2*j for j,x in enumerate(t))
  assert sum(t)==sum(CENTER)+DELTA*p and sum(a*b for a,b in zip(t,R))==sum(a*b for a,b in zip(CENTER,R))
  corners.append({'p':str(p),'h':str(h),'k':str(k),'source_lift':list(map(str,t))})
 # Affine source lift + corner source admission proves the whole 3D box.
 pair_points={'AB':(Q(0),Q(0)),'AC':(Q(0),Q(1)),'BC':(Q(1),Q(0))}
 pair_controls=[]
 for pair,(h,k) in pair_points.items():
  assert all(holds(n,h,k) for n in pair)
  for p in (Q(0),Q(1,2),Q(1)):
   t=lift(p,h,k);assert all(0<=x<=100+2*j for j,x in enumerate(t))
   pair_controls.append({'pair':pair,'p':str(p),'h':str(h),'k':str(k),'source_lift':list(map(str,t))})
 # Exact triple Farkas certificate, independent of the public parameter.
 rows=[((Q(1),Q(0)),Q(1,4)),((Q(0),Q(1)),Q(1,4)),((Q(-1),Q(-1)),Q(-1))]
 assert tuple(sum(a[j] for a,b in rows) for j in range(2))==(0,0)
 bound=sum(b for a,b in rows);assert bound==Q(-1,2)
 report={'passed':True,'source_m':4,'public_domain':'0<=p<=1; U=206+128^-4*p; V=V(center)',
 'fiber_parameters':'t0=50+128^-4*h, t1=51+128^-4*k; 0<=h,k<=1',
 'histories':{'A':'h<=1/4','B':'k<=1/4','C':'h+k>=1'},
 'source_box_corners':corners,'pair_sections':pair_controls,
 'triple_obstruction':{'rows':[{'normal':list(map(str,a)),'upper':str(b)} for a,b in rows],
 'weights':['1','1','1'],'combined_normal':['0','0'],'combined_upper':str(bound)},
 'minimal_lifting_states':2,'pairwise_incompatibility_graph_edges':0,
 'minimal_incompatible_hyperedges':[['A','B','C']],
 'scope':'All-domain affine source sections for every pair; uniform triple contradiction. No general continuous-selection or hypergraph-coloring algorithm claim.'}
 (OUT/'common-lift-hypergraph.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:report[k] for k in ('passed','minimal_lifting_states','pairwise_incompatibility_graph_edges','minimal_incompatible_hyperedges')},indent=2))
if __name__=='__main__':main()
