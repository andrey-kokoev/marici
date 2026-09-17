#!/usr/bin/env python3
"""Verify contiguous coverage of completed rank-two Taylor cells accumulated so far."""
import json
from pathlib import Path
cells=[
(.05,.0525,48.47542925706735),(.0525,.055,29.326595915632428),(.055,.0575,17.674325103155876),
(.0575,.06,10.595292803110466),(.06,.0625,6.301341340162171),(.0625,.065,3.701756209147515),
(.065,.0675,2.131552703884854),(.0675,.07,1.1840485261982068),(.07,.0725,.6138664105521239),
(.0725,.075,.27199170103257),(.075,.0775,.06795774755026746),(.0775,.08,.15820321057816258),
(.08,.0825,.08631146522238131),(.0825,.085,.04464419992934059),(.085,.0875,.020897930878198443),
(.0875,.09,.00768440882318238),(.09,.0925,.0006058197002282266),(.0925,.09375,.014142690314738826),
(.09375,.095,.010945816855008637),(.095,.09625,.008461526013327569),(.09625,.0975,.006531811164736091),
(.0975,.09875,.0050335559939638395),(.09875,.1,.0038709443743475645),(.1,.10125,.0029693903448998627)]
contiguous=all(abs(cells[i][1]-cells[i+1][0])<1e-14 for i in range(len(cells)-1));positive=all(x[2]>0 for x in cells)
out={'schema':'marici.voevodsky.rank-two-compact-coverage-ledger.v1','interval':[cells[0][0],cells[-1][1]],'cell_count':len(cells),
 'cells':[{'interval':[a,b],'complete_lower_bound':v} for a,b,v in cells],
 'checks':{'contiguous_without_gaps':contiguous,'every_complete_lower_bound_positive':positive,'endpoints_match':cells[0][0]==.05 and cells[-1][1]==.10125},
 'weakest_lower_bound':min(x[2] for x in cells),'passed':contiguous and positive,'rh_proved':False,
 'scope':'Rank-two remainder Hankel determinant on [0.05,0.1] only; this does not imply higher-rank or Hardy co-defect positivity.'}
assert out['passed'];p=Path(__file__).parents[1]/'results'/'rank_two_compact_coverage_ledger.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='cells'},indent=2))
