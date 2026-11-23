"""Discard list order, arrow directions, face orientation and particle labels. Retain the six selected face-edge sectors. Require a chain that uses each face once, turns between its two selected edges and changes face across the same edge."""
from itertools import permutations,product
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results';src=json.loads((D/'pne_sector_p_extension.json').read_text());faces={}
for s in src['sectors']:faces.setdefault(frozenset(s['face']),set()).add(frozenset(s['leg']))
assert len(faces)==3 and all(len(es)==2 for es in faces.values());rows=[]
for fs in permutations(faces):
 for pairs in product(*(permutations(faces[f]) for f in fs)):
  if any(a[1]!=b[0] for a,b in zip(pairs,pairs[1:])):continue
  ws=[]
  for a,b in pairs:
   x,=a-b;y,=a&b;z,=b-a;ws.append([x,y,z])
  joins=['retain' if a[-2:]==b[:2] else 'return' for a,b in zip(ws,ws[1:])];rows.append(dict(windows=ws,joins=joins))
assert len(rows)==2 and rows[0]['windows']==[w[::-1] for w in rows[1]['windows'][::-1]];assert {tuple(r['joins']) for r in rows}=={('retain','return'),('return','retain')};print([r['joins'] for r in rows]);(D/'pne_unordered_sector_chain.json').write_text(json.dumps(rows,indent=2)+'\n')
