#!/usr/bin/env python3
"""Tabulate coercive-tail thresholds as support crosses prime-power events."""
import json,math
from pathlib import Path
# Each log(q)/2 is an autocorrelation-support event, q=p^k.
def prime_powers(limit):
 out=[]
 for p in range(2,limit+1):
  if any(p%d==0 for d in range(2,int(math.sqrt(p))+1)):continue
  q=p
  while q<=limit:out.append((q,p));q*=p
 return sorted(out)
cg=2.6947343670010686;cb=math.pi/math.sqrt(3)+math.log(2)-3/8
rows=[];cp=0.0
for q,p in prime_powers(32):
 L=.5*math.log(q);cp+=math.log(p)/math.sqrt(q) # Lambda(q)/sqrt(q)
 C=cg+cb+cp;M=math.floor((2*L/math.pi)*(math.exp(2*C)-1))+1
 rows.append({'q':q,'prime':p,'event_L':L,'cumulative_prime_budget':cp,'total_budget':C,'tail_mode_threshold_immediately_after_event':M})
out={'schema':'marici.voevodsky.full-image-prime-power-threshold-table.v1','formula':'M=floor((2L/pi)(exp(2(Cgamma+Cboundary+sum_{p^k<=exp(2L)} log(p)/sqrt(p^k)))-1))+1','events_through_q':32,'rows':rows,'interpretation':'bookkeeping upper bounds only; no compact-window positivity certificate','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'full_image_prime_power_threshold_table.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
