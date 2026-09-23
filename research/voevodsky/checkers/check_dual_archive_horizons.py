"""Finite service horizons separate mathematical availability from event audit."""
from itertools import product
from pathlib import Path
import json
MATH_DEADLINE=3;EVENT_A_DEADLINE=2
# availability inclusive by tick; provider A alone carries event A; either
# provider with matching rows supports the public mathematical replay.
def obligations(a_until,b_until):
 math=any(x>=MATH_DEADLINE for x in (a_until,b_until))
 event=a_until>=EVENT_A_DEADLINE
 return {'math_replay_at_3':math,'event_A_audit_at_2':event,'all_satisfied':math and event}
checks=0
for a,b in product(range(5),repeat=2):
 result=obligations(a,b)
 assert result['all_satisfied']==(a>=2 and max(a,b)>=3)
 checks+=1
assert checks==25
assert obligations(1,3)=={'math_replay_at_3':True,'event_A_audit_at_2':False,'all_satisfied':False}
assert obligations(2,3)['all_satisfied']
assert obligations(3,0)['all_satisfied']
assert not obligations(0,3)['all_satisfied']
# Event A may have been successfully inspected earlier, but that receipt
# does not provide a fresh event-A audit after A expires.
historical={'event_A_checked_at_0':True}
assert historical['event_A_checked_at_0'] and not obligations(1,3)['event_A_audit_at_2']
report={'passed':True,'schedules_checked':checks,'required_horizons':{'math_replay_tick':3,'event_A_audit_tick':2},'necessary_sufficient_for_menu':'A available through 2 AND at least one of A,B through 3','A_ends_1_B_ends_3':'math succeeds, event-A audit fails','A_ends_2_B_ends_3':'both succeed','historical_event_receipt_does_not_replace_fresh_audit':True,'scope':'Frozen two-provider inclusive-tick availability model; no authenticated issuers, live revocation race testing, total resource cost or universal retention theorem.'}
out=Path(__file__).resolve().parents[1]/'results/dual-archive-horizons.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
