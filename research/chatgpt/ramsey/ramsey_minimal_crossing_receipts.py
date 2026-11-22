"""Minimum positive self-dual crossing receipts on the fixed marked decagon, with and without imposing the literal swap. Enumerate all subsets, not a greedy choice."""
from itertools import combinations
from ramsey_history_matching_provenance import enum,D,json
from ramsey_row_quotient_constructor import move,R

def run():
    q=json.loads((D/'ramsey_open_shortcut_constructor.json').read_text())['marked'];c=q['cycle'];arc=[frozenset(tuple(sorted((x,c[(i+1)%10]))) for i,x in enumerate(c) if i%2==b) for b in [0,1]];ms=set(enum());samples=[]
    for m in ms:
        if not arc[0]<=m:continue
        n=(m-arc[0])|arc[1];
        if n not in ms:continue
        seen=[]
        for j,d,k,x in q['paths']:
            assert (d,j) not in m|n and (x,k) not in m|n
            if (d,k) not in m|n:seen.append(j)
        samples.append((frozenset(seen),n==move(m,R)))
    out={}
    for key,rows in [('all',[s for s,l in samples]),('literal',[s for s,l in samples if l])]:
        labels=sorted(j for j,*_ in q['paths']);counts={t:sum(set(t)<=s for s in rows) for k in range(6) for t in combinations(labels,k)};minimal=[t for t in counts if counts[t]==1 and all(counts[t[:i]+t[i+1:]]>1 for i in range(len(t)))];out[key]=dict(n=len(rows),exit_alone=counts[(29,)],exit_plus_one={j:counts[tuple(sorted((j,29)))] for j in labels if j!=29},minimal=minimal,patterns=sorted([sorted(s) for s in rows]))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_minimal_crossing_receipts.json').write_text(json.dumps(out)+'\n')
