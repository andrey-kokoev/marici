"""Test a sector-as-state interpretation, not sectors as windows. Label an exit side before moving using only its supplied triangle order (centroid, tail, head). Do not assign particle names to side types."""
import json
from itertools import permutations
from pathlib import Path
D=Path(__file__).resolve().parents[1]
source=json.loads((D.parent/'nima/results/twelve-triangle-positive-geometry.json').read_text())
tri=[tuple(s['triangle']) for s in source['triangles_and_transports']]
sides=['centroid-tail','outer','head-centroid']; moves={}
for i,t in enumerate(tri):
 for k,side in enumerate(sides):
  edge={t[k],t[(k+1)%3]};j,=[j for j,u in enumerate(tri) if i!=j and edge<=set(u)]
  moves[i,side]=j
rows=[]
for word in permutations(sides):
 paths=[]
 for i in range(len(tri)):
  p=[i]
  for s in word:p.append(moves[p[-1],s])
  paths.append(p)
 rows.append(dict(word=word,four_distinct=sum(len(set(p))==4 for p in paths),example=[tri[k] for k in paths[0]]))
print([(r['word'],r['four_distinct']) for r in rows]);(D/'results/pne_sector_move_words.json').write_text(json.dumps(rows,indent=2)+'\n')
