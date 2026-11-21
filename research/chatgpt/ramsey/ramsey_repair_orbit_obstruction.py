"""Locate exclusion mechanism for switch orbits: directed repair relations before testing joint validity."""
from pathlib import Path
from collections import Counter
from itertools import combinations
import json
from ramsey_hall_center_conjecture import decode
from ramsey_mutual_repair_conjecture import switches,repairs
from ramsey_repair_cyclic_phase import key,transport,root_auts

if __name__=='__main__':
 data=json.loads(Path(__file__).with_name('ramsey_hall_center_conjecture.json').read_text());report=[]
 for r in data['regular']:
  if r['record'] not in (190,191):continue
  A=decode(r['graph6'].encode());p=min(p for p in root_auts(A) if p!=tuple(range(22)));moves={key(s):s for s in switches(A)};todo=set(moves);orbits=[]
  while todo:
   q=min(todo);o=[]
   while q not in o:o.append(q);q=transport(q,p)
   todo-=set(o);orbits.append(o)
  index={s:i for i,o in enumerate(orbits) for s in o};rows=[]
  for i,o in enumerate(orbits):
   s=moves[o[0]];partners=[k for k,t in moves.items() if not s['support']&t['support'] and repairs(s,t)];reciprocal=[k for k in partners if repairs(moves[k],s)];rows.append({'orbit':i,'defects':len(s['bad']),'root_defects':sum(bool(m&1) for m in s['bad']),'repairers_by_orbit':dict(Counter(index[k] for k in partners)),'reciprocal_by_orbit':dict(Counter(index[k] for k in reciprocal)),'representative':s})
  drifts=[]
  for i,j in combinations(range(len(orbits)),2):
   if rows[i]['repairers_by_orbit'].get(j)!=1 or rows[j]['repairers_by_orbit'].get(i)!=1:continue
   a=orbits[i][0];s=moves[a];b,=[k for k in orbits[j] if not s['support']&moves[k]['support'] and repairs(s,moves[k])];t=moves[b];c,=[k for k in orbits[i] if not t['support']&moves[k]['support'] and repairs(t,moves[k])];drifts.append({'orbit_pair':[i,j],'return_phase':orbits[i].index(c)})
  report.append({'source':r['record'],'rows':rows,'unique_repair_return_phases':drifts});print('SOURCE',r['record'],'repair return phases',drifts)
  for row in rows:print({k:v for k,v in row.items() if k!='representative'})
 Path(__file__).with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
