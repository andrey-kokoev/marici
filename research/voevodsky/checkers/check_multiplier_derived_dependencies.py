"""Recompute primitive-row proof dependencies from actual Farkas multipliers."""
from pathlib import Path
import json
row_names=('x-low','x-high','y-low','y-high')
leaf={'a':((1,2,0,0),(1,0),2),'b':((0,0,1,2),(0,1),2),
      'c':((0,1,0,0),(1,0),1),'d':((0,0,0,1),(0,1),1)}
base=(((-1,0),0),((1,0),1),((0,-1),0),((0,1),1))
def support(proof):return frozenset(row_names[i] for i,w in enumerate(proof[0]) if w>0)
def valid(proof,rows):
 m,v,T=proof
 return min(m)>=0 and tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in range(2))==v and sum(rows[i][1]*m[i] for i in range(4))==T
assert all(valid(p,base) for p in leaf.values())
computed={k:sorted(support(p)) for k,p in leaf.items()}
assert computed=={'a':['x-high','x-low'],'b':['y-high','y-low'],'c':['x-high'],'d':['y-high']}
def check_declaration(name,declared):
 if set(declared)!=support(leaf[name]):raise ValueError('DECLARED_DEPENDENCY_MISMATCH')
 return True
for k,v in computed.items():assert check_declaration(k,v)
for k,omitted in (('a',['x-low']),('c',[]),('b',['y-low']),('d',[])):
 try:check_declaration(k,omitted)
 except ValueError:pass
 else:raise AssertionError('omitted dependency admitted')
scenarios={}
for changed in ('x-high','y-high'):
 rows=list(base);i=row_names.index(changed);rows[i]=(rows[i][0],2)
 failed={k for k,p in leaf.items() if not valid(p,rows)}
 affected={k for k,p in leaf.items() if changed in support(p)}
 assert failed==affected
 scenarios[changed]={'affected':sorted(affected),'unchanged_row_proofs':sorted(set(leaf)-affected)}
assert scenarios['x-high']['affected']==['a','c'] and scenarios['y-high']['affected']==['b','d']
report={'passed':True,'derived_leaf_support':computed,'omitted_dependency_controls_refused':4,'independent_upper_row_edits':scenarios,'boundary':'Minimal positive-multiplier proof dependence is arithmetic; source-generation identity still changes for ALL old records and requires independent rebinding before authorized new-source use.'}
out=Path(__file__).resolve().parents[1]/'results/multiplier-derived-dependencies.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
