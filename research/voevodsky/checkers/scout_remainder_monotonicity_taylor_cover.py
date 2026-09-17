#!/usr/bin/env python3
"""Scout Taylor radii for compact-interval certification of -R'(t)."""
import json
from pathlib import Path
src=json.loads((Path(__file__).parents[1]/'results'/'remainder_monotonicity_source_scout.json').read_text())['rows']
pts=[x for x in src if x['t'] in (.05,.075,.1,.15,.2,.25)]
# Conservative empirical slopes use all secants touching a point, inflated x4.
rows=[]
for i,x in enumerate(pts):
 slopes=[]
 if i:slopes.append(abs((x['minus_R_prime']-pts[i-1]['minus_R_prime'])/(x['t']-pts[i-1]['t'])))
 if i+1<len(pts):slopes.append(abs((pts[i+1]['minus_R_prime']-x['minus_R_prime'])/(pts[i+1]['t']-x['t'])))
 M=4*max(slopes+[1e-12]);radius=.5*x['minus_R_prime']/M
 rows.append({'center':x['t'],'value':x['minus_R_prime'],'empirical_derivative_bound_candidate':M,'candidate_radius':radius,'interval':[x['t']-radius,x['t']+radius]})
# interval union coverage diagnostic
right=rows[0]['interval'][0];gaps=[]
for r in rows:
 if r['interval'][0]>right:gaps.append([right,r['interval'][0]])
 right=max(right,r['interval'][1])
out={'schema':'marici.voevodsky.remainder-monotonicity-taylor-cover-scout.v1','rows':rows,'uncovered_gaps':gaps,
 'scope':'Planning scout only. Secant-based derivative candidates are not rigorous bounds; intervals are not certificates.',
 'next':'Interval-certify c1=R double-prime on each proposed interval, then replace candidate radii by value_lower/(2*c1_absolute_upper).','passed':True,'rh_proved':False}
p=Path(__file__).parents[1]/'results'/'remainder_monotonicity_taylor_cover_scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
