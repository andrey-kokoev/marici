"""Compare a 3 x 35 x 2 coordinate description to direct incidence on the cyclic witness. Count actual simple four-cycles, not just walks of length four."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json
D=Path(__file__).resolve().parents[1]/'results'
def main():
    U=set(range(35));N=[set() for _ in U]
    for a,b in json.loads((D/'ramsey_39_glue_vs_circle.json').read_text())['plus_edges']:N[a].add(b);N[b].add(a)
    actual={frozenset(q) for q in combinations(range(35),4) if all(b not in N[a] for a,b in combinations(q,2)) and len(U.difference(q,*[N[a] for a in q]))==13}
    ds=[4*11**j%35 for j in range(3)];templates={'P':(0,1,2,3),'C':(-2,0,1,3)};table={(d,t,s):frozenset(d*(t+i)%35 for i in v) for d in ds for t in range(35) for s,v in templates.items()};assert len(table)==len(actual)==210 and set(table.values())==actual
    adj={a:set() for a in table}
    for a,b in combinations(table,2):
        if len(table[a]&table[b])==3:adj[a].add(b);adj[b].add(a)
    for (d,t,s),nb in adj.items():
        options=[(-1,'P'),(1,'P'),(0,'C'),(2,'C')] if s=='P' else [(0,'P'),(-2,'P')];assert nb=={(d,(t+h)%35,r) for h,r in options}
    squares={frozenset((a,b,x,y)) for a,b in combinations(adj,2) for x,y in combinations(adj[a]&adj[b],2)};expected={frozenset(((d,t,'P'),(d,(t+1)%35,'P'),(d,(t+2)%35,'P'),(d,(t+2)%35,'C'))) for d in ds for t in range(35)};assert squares==expected
    example=[(4,0,'P'),(4,1,'P'),(4,2,'P'),(4,2,'C')];cycle=[dict(roots=sorted(table[k]),core=sorted(U.difference(table[k],*[N[a] for a in table[k]]))) for k in example];out=dict(step_sizes=ds,templates=templates,coordinates=len(table),exchanges=sum(map(len,adj.values()))//2,simple_squares=len(squares),example=cycle);print(out);(D/'ramsey_39_exchange_normal_form.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
