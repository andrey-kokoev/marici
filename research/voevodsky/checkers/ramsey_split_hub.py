"""Structural description after the split search. Inputs are the two opposed red pins and the fixed address catalogue. Compare predicted spokes with all viable one-bit splits; do not treat the characterization as a new independent prediction."""
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1];s=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());S=s['address_masks'];E=list(map(tuple,s['edge_order']));tests=json.loads((D/'results/ramsey_opposed_choices.json').read_text());out=[]
for t in tests:
 b=t['slot4'];red=[4 if b else 5,71 if b else 74];ends=[j for k in red for j in E[k]];h,=[i for i,m in enumerate(S) if all(not m&S[j] for j in ends)];spokes={j:E.index(tuple(sorted((j,h)))) for j in ends};valid={s['split'] for s in t['one_split']};assert valid=={v for j,v in spokes.items() if S[j]!=(1<<0|1<<2)};pick,=[spokes[j] for j in E[red[1]] if not S[j]&(1<<6)];assert pick in valid;out.append(dict(slot4=b,hub=[i for i in range(7) if S[h]>>i&1],red=red,all_spokes=spokes,successful=sorted(valid),partner_rule=pick))
print(out);(D/'results/ramsey_split_hub.json').write_text(json.dumps(out,indent=2)+'\n')
