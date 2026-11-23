"""Inspect the original synthesis condition for eligible edge slots (disjoint addresses). Restrict it to address pairs internal to the four-label address Q. Keep eligibility separate from red links of particular wirings."""
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1];src=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());S=src['address_masks'];E=list(map(tuple,src['edge_order']));Q,=[q for q in S if q.bit_count()==4];bits=lambda u:[i for i in range(7) if (u>>i)&1];rows=[]
for i in bits(Q):
 a=(1<<6)|(1<<i);j=S.index(a);eligible=[s for s in S if s.bit_count()==2 and not s&~Q and tuple(sorted((j,S.index(s)))) in E];u=0
 for s in eligible:u|=s
 assert u==Q^(1<<i) and u not in S
 slots=[E.index(tuple(sorted((j,S.index(s))))) for s in eligible];redCounts=[sum((w>>k)&1 for k in slots) for w in src['wirings']];rows.append(dict(address=bits(a),eligible=list(map(bits,eligible)),support=bits(u),red_counts=redCounts))
print(rows);(D/'results/ramsey_partner_complement.json').write_text(json.dumps(rows,indent=2)+'\n')
