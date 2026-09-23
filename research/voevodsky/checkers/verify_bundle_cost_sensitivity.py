"""Independent rational threshold replay with typed-account refusal controls."""
from fractions import Fraction as Q
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];V=ROOT/'research/voevodsky'
load=lambda n:json.loads((V/'results'/n).read_text())
menu=load('fixed-menu-provider-bundles-verification.json');receipts=load('fixed-menu-provider-bundles.json');claimed=load('bundle-cost-sensitivity.json')
assert menu['passed'] and claimed['passed'] and receipts['passed']
price=receipts['provider_receipt_bytes'];A=Q(price['restricted_archive']);B=Q(price['full_archive']);C=Q(price['full_lift'])
assert A+C==Q(menu['minimum_receipt_bytes']) and A+B==Q(menu['after_full_lift_stale_minimum_bytes'])
threshold=B-C;assert threshold==180==Q(claimed['receipt_gap_bytes'])
# Common A cancels only when its scenario-specific extra charge is identical.
def compare(lift_extra,archive_extra,common_lift=0,common_archive=0,units='receipt_byte_equivalent'):
 if units!='receipt_byte_equivalent':raise TypeError('INCOMMENSURATE_ACCOUNTS')
 xs=tuple(map(Q,(lift_extra,archive_extra,common_lift,common_archive)))
 assert all(x>=0 for x in xs)
 l=A+C+xs[0]+xs[2];r=A+B+xs[1]+xs[3]
 return 'cheap' if l<r else 'tie' if l==r else 'archived'
assert compare(0,0)=='cheap' and compare(Q(359,2),0)=='cheap'
assert compare(180,0)=='tie' and compare(181,0)=='archived'
assert compare(181,2)=='cheap'
# A differential charge on the otherwise shared A invalidates naive cancel.
assert compare(0,0,181,0)=='archived'
try:compare(0,0,units='cpu_seconds')
except TypeError:incommensurate_refused=True
else:raise AssertionError('seconds were added to receipt bytes')
assert claimed['post_stale']=='cheap full-domain lift bundle inadmissible irrespective of omitted costs'
assert receipts['stale_full_lift_forces_archive_enabled_replacement']
report={'passed':True,'independent_threshold':str(threshold),'tie_checked':True,'reverse_checked':True,'unequal_common_cost_can_reverse':True,'incommensurate_units_refused':incommensurate_refused,'post_stale_ineligibility_requires_live_test':True,'scope':'Exact rational replay from menu receipts; symbolic supplemental charges require explicit common units and owner-scoped eligibility. No physical-cost observation.'}
(V/'results/bundle-cost-sensitivity-verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
