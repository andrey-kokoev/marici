"""Use the three named edge probes of seven_transport_algebra, without P/N/E bindings. Compare both square roots at every starting wiring. Words are in execution order."""
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1];src=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());roots=json.loads((D/'results/ramsey_chart_square_roots.json').read_text());maps={word:dict(zip(src['wirings'],r['images'])) for r in roots for word in r['words']};slots=(0,4,6);bits=lambda w:tuple(w>>s&1 for s in slots);rows=[]
for w in src['wirings']:
 b=bits(w);row={'start':b};par=sum(b)%2
 for word in ['AC','CA']:
  u=maps[word][w];delta=tuple(i for i,(a,c) in enumerate(zip(b,bits(u))) if a!=c);expect=(2 if par==0 else 0) if word=='AC' else (0 if par==0 else 2);assert delta==(expect,);row[word]={'changed_probe_slot':slots[expect],'changed_wiring_bits':(u^w).bit_count()}
 rows.append(row)
print(rows);(D/'results/ramsey_cycle_probe_direction.json').write_text(json.dumps(rows,indent=2)+'\n')
