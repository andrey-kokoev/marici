"""Boundaries of a proposed mixed redistribution/normalization 3-cell."""
from fractions import Fraction as Q
from pathlib import Path
import json
def valid(p,T):
 a,u,v,c=map(Q,p);return min(a,u,v,c)>=0 and u+v-a==1 and u+v+c==Q(T)
def n(p,side,T):
 assert valid(p,T)
 a,u,v,c=map(Q,p);q=(a+c,u+c,v,Q(0)) if side=='A' else (a+c,u,v+c,Q(0))
 assert valid(q,T);return q
def r(p,amount,T):
 assert valid(p,T)
 a,u,v,c=map(Q,p);amount=Q(amount)
 if not -v<=amount<=u:raise ValueError('BAD_BOUNDARY')
 q=(a,u-amount,v+amount,c);assert valid(q,T);return q
p=(Q(0),Q(1),Q(0),Q(1));T=Q(2);theta=Q(1,2);c=p[-1]
left_mid=r(p,theta,T);left_tip=n(left_mid,'B',T)
right_mid=n(p,'A',T);right_tip=r(right_mid,c+theta,T)
assert left_mid==(0,Q(1,2),Q(1,2),1)
assert right_mid==(1,2,0,0)
assert left_tip==right_tip==(1,Q(1,2),Q(3,2),0)
left=(('R',theta),('N_B',c));right=(('N_A',c),('R',c+theta))
assert left!=right
# Source proof roots support each *edge*. They do not constitute a filler of
# the parallel composite paths in the free path category.
roots={'low:-x<=0','upper-A:x<=1','upper-B:x<=1'}
def local_support(request):
 if set(request.get('roots',()))!=roots:return 'missing_primitive_root'
 if request.get('boundary')!=(left,right):return 'wrong_parallel_boundary'
 if request.get('constructor') not in ('mixed_interchange_3cell',):return 'no_mixed_3cell_constructor'
 return 'new_generator_requires_coherence_and_independent_admission'
assert local_support({'roots':roots,'boundary':(left,right),'constructor':'same_endpoint'})=='no_mixed_3cell_constructor'
assert local_support({'roots':roots-{'upper-B:x<=1'},'boundary':(left,right),'constructor':'mixed_interchange_3cell'})=='missing_primitive_root'
assert local_support({'roots':roots,'boundary':(left,right),'constructor':'mixed_interchange_3cell'})=='new_generator_requires_coherence_and_independent_admission'
report={'passed':True,'starting_proof':['0','1','0','1'],'theta':'1/2','left_intermediate':['0','1/2','1/2','1'],'right_intermediate':['1','2','0','0'],'common_tip':['1','1/2','3/2','0'],'parallel_2cell_paths_distinct':True,'primitive_row_support_on_edges':True,'first_missing_cell':'mixed_interchange_3cell','scope':'Free path presentation of proposed proof 2-cells. A typed candidate 3-cell boundary is exhibited, not its independent constructor, higher coherence or actual-history authority.'}
out=Path(__file__).resolve().parents[1]/'results/mixed-cell-path-boundary.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
