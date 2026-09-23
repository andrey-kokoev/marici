"""A typed retained surplus grade repairs a restricted redundant-row retraction."""
from fractions import Fraction as Q
from pathlib import Path
import json
base_normal=(-1,1);base_bound=(0,1)
def fine(k):
 k=Q(k);assert k>=0
 return {'normal':(-1,1,1),'bound':(0,1,1+k),'surplus':k}
def decorated_drop(packet):
 assert packet['normal']==(-1,1,1) and packet['bound'][:2]==base_bound
 k=Q(packet['bound'][2])-Q(base_bound[1]);assert k>=0 and k==packet['surplus']
 return {'normal':base_normal,'bound':base_bound,'retained_surplus':k}
def restore(packet):
 assert packet['normal']==base_normal and packet['bound']==base_bound
 return fine(packet['retained_surplus'])
for k in (0,Q(1,2),1,2,5):
 x=fine(k);assert restore(decorated_drop(x))==x
 assert all(Q(v)>=0 for v in (0,0,x['surplus']))
# Plain drop cannot be inverted on the whole family: equal coarse projection
# but different fine proof presentations and strictly different surplus.
assert fine(0)!=fine(1) and decorated_drop(fine(0))['bound']==decorated_drop(fine(1))['bound']
assert decorated_drop(fine(0))['retained_surplus']!=decorated_drop(fine(1))['retained_surplus']
# Without a nonnegative surplus the same add matrix does not certify the row.
try:fine(-Q(1,2))
except AssertionError:negative_refused=True
else:raise AssertionError('negative Farkas surplus admitted')
# A new nonredundant fine row x<=1/2 has w-1<0; it cannot enter this
# restricted decorated-refinement family, even though its source set exists.
assert Q(1,2)-1<0
report={'passed':True,'checked_surplus_values':['0','1/2','1','2','5'],'decorated_retraction_exact_on_redundant_family':True,'undecorated_drop_nonfaithful':True,'negative_surplus_refused':negative_refused,'fine_refinement_x_le_half_outside_domain':True,'scope':'One restricted family of redundant rows x<=1+k with k>=0. Retained surplus is extra history data, not a quotient theorem or analytic cofiber.'}
out=Path(__file__).resolve().parents[1]/'results/retained-surplus-grade.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
