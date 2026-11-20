"""Frozen path translation. No query result in a field. Labels 0,1 are untyped IDs; 2 is the customer-product pair vertex; 3 is fresh. At the fixed cut the two incidence edges have been read. Yes/no on each side encodes red/blue on its own incidence edge. Unknown not admitted on read edges; all four suffix edges are unassigned. Endpoint erasure retains both IDs unordered and both verdicts in their original fields."""
from itertools import combinations, product
from pathlib import Path
import json

E=list(combinations(range(4),2)); cut=[(0,2),(1,2)]; tail=[e for e in E if e not in cut]
def legal(edges):return all(len({edges[e] for e in combinations(t,2)})==2 for t in combinations(range(4),3))
def index(c,x,y):return (c,1-c,x,y)
def read(key):
    c,p,x,y=key
    return {(c,2):x,(p,2):y}
def views(k):
    c,p,x,y=k
    return dict(full=k,forget_endpoint=(tuple(sorted((c,p))),x,y),forget_customer=(c,p,y),forget_product=(c,p,x),static_sql=())
def main():
    rows=[]
    for c,a,b in product(range(2),repeat=3):
        raw=dict(zip(cut,(a,b)));k=index(c,raw[(c,2)],raw[(1-c,2)])
        assert read(k)==raw
        futures={s for s in product(range(2),repeat=4) if legal(raw|dict(zip(tail,s)))};rows.append((k,futures))
    results={}
    for name in views(rows[0][0]):
        examples=[]
        for (a,A),(b,B) in combinations(rows,2):
            if views(a)[name]!=views(b)[name] or A==B:continue
            s=min(A^B);examples.append(dict(keys=[a,b],red_suffix=[e for e,col in zip(tail,s) if col],legal=[s in A,s in B]))
        results[name]=dict(conflicting_pairs=len(examples),witness=examples[0] if examples else None)
    assert results['full']['conflicting_pairs']==0 and all(results[n]['conflicting_pairs'] for n in results if n!='full');return results
if __name__=='__main__':
    r=main();print(json.dumps(r));(Path(__file__).resolve().parents[1]/'results/ramsey_six_roles_path.json').write_text(json.dumps(r,indent=2)+'\n')
