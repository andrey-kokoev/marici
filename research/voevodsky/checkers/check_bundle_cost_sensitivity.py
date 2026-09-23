"""Exact finite-menu sensitivity to omitted nonnegative provider-specific accounts."""
from fractions import Fraction as Q
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research/voevodsky'
packet=json.loads((V/'results/fixed-menu-provider-bundles-verification.json').read_text())
assert packet['passed'] and packet['minimum_receipt_bytes']==3658 and packet['after_full_lift_stale_minimum_bytes']==3838
cheap=Q(3658);archived=Q(3838);gap=archived-cheap;assert gap==180
# A is common. Separate unknown, nonnegative costs for B and C; no double
# counting A or claiming these symbolic terms were physically measured.
def decide(u_full_lift,u_full_archive,*,live_lift=True):
 x=Q(u_full_lift);y=Q(u_full_archive);assert x>=0 and y>=0
 if not live_lift:return 'archived_only'
 lhs=cheap+x;rhs=archived+y
 return 'cheap' if lhs<rhs else 'tie' if lhs==rhs else 'archived'
fixtures=[('equal-unknown',0,0,'cheap'),('cheap-extra-below',Q(359,2),0,'cheap'),('tie',180,0,'tie'),('reverse',181,0,'archived'),('archived-extra',181,2,'cheap'),('post-stale',0,0,'archived_only')]
for name,x,y,want in fixtures:
 assert decide(x,y,live_lift=name!='post-stale')==want
# For ALL nonnegative provider-specific omitted accounts no robust winner:
assert decide(0,0)=='cheap' and decide(181,0)=='archived'
# If the omitted differential is known <=t with t<180 the cheap bundle
# wins; <=180 only gives weak preference (possible tie).
for t in (Q(0),Q(1),Q(359,2)):
 assert t<gap and decide(t,0)=='cheap'
assert decide(gap,0)=='tie'
report={'passed':True,'receipt_gap_bytes':str(gap),'decision_rule':'cheap iff omitted_full_lift - omitted_full_archive < 180; tie at 180; archive bundle wins above 180','fixtures':[{'name':n,'lift_extra':str(x),'archive_extra':str(y),'result':w} for n,x,y,w in fixtures],'nonnegative_unknowns_do_not_select_winner':True,'post_stale':'cheap full-domain lift bundle inadmissible irrespective of omitted costs','scope':'Symbolic exact rational account units calibrated to receipt-byte objective; not measured heap/time, universal optimum or probabilistic prior.'}
(V/'results/bundle-cost-sensitivity.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
