"""Test a literal between-placement operation, not fitted Boolean functions of two bits."""
from ramsey_retention_slice import CAT,D,decode,check
from itertools import combinations,product
from collections import Counter
import json,sys
P=D.parent/'ramsey_excel_overlap_supply_protocol.json';R=D.parent/'ramsey_excel_overlap_supply.json'
rule=dict(source='Use each terminal-reaching two-swap square F of separated triples. Each other two-swap square H in the whole width supplies one column: the four membership bits in H of the rows of F. Count H once, independent of how it was enumerated. No multiplicity from display copies or arbitrary duplication.',target='For each legal oriented-square construction on the full catalogues of 17/22 cores, hold the four anchors supplied. Compare exterior nonzero membership masks only. Allow any terminal square and any square symmetry jointly for the whole panel. Surplus columns can be discarded. Report coverage with and without replacement; the latter is necessary even for an unlabeled injective assignment. No graph-to-table labeling is inferred from a fit.')
def source(w):
    rows={frozenset(c) for c in combinations(range(1,w+1),3) if min(c[1]-c[0],c[2]-c[1])>=2};faces={}
    for r in sorted(rows,key=sorted):
        moves=[frozenset((i,i+1)) for i in range(1,w) if r^{i,i+1} in rows]
        for u,v in combinations(moves,2):
            f=(r,r^u,r^u^v,r^v)
            if not u&v and f[2] in rows:faces.setdefault(frozenset(f),f)
    supplies=[];profiles=[]
    for F,f in faces.items():
        if not any(w in s for s in F):continue
        def masks(seq):return Counter(sum(1<<i for i,r in enumerate(seq) if r in h) for h in faces if h!=F)
        profiles.append(dict(rows=[sorted(r) for r in f],supply=dict(sorted(masks(f).items()))));
        for seq in (f,f[::-1]):
            for i in range(4):supplies.append(masks(seq[i:]+seq[:i]))
    return supplies,profiles,len(faces)
def panels(k,n):
    for idx,line in enumerate((CAT/f'r3{k}_{n}.g6').read_text().splitlines(),1):
        a=decode(line);A=[{j for j in range(n) if j!=i and not v>>j&1 and not v&a[j]} for i,v in enumerate(a)]
        for i in range(n):
            for j in sorted(A[i]):
                for h in sorted(A[j]-{i}):
                    for l in sorted((A[h]&A[i])-{j}):
                        c=(i,j,h,l)
                        if i!=min(c) or j>l:continue
                        for d in (2,3):
                            G=a.copy()+[0]*5;S=[]
                            for t in range(4):
                                x,y=c[t],c[(t+1)%4];s=(1<<x)|(1<<y)|(a[c[(t+d)%4]]&~(a[x]|a[y]));S.append(s);G[n+t]=s|1<<(n+4);G[-1]|=1<<(n+t)
                                for z in range(n):G[z]|=((s>>z)&1)<<(n+t)
                            if check(G,(1<<(n+5))-1,3,k+1):
                                need=Counter(sum(((s>>z)&1)<<t for t,s in enumerate(S)) for z in set(range(n))-set(c));need.pop(0,None);yield idx,c,need

def run():
    assert json.loads(P.read_text())==rule;out=[]
    for k,n in ((6,17),(7,22)):
        avail,profiles,total=source(k+1);t=Counter();deficit=Counter();first=None
        for idx,c,need in panels(k,n):
            gap=min(sum((need-a).values()) for a in avail);deficit[gap]+=1;t['panels']+=1;t['types_fit']+=any(need.keys()<=a.keys() for a in avail);t['counts_fit']+=gap==0
            if first is None:first=dict(core_record=idx,square=c,demand=dict(sorted(need.items())),min_unmatched=gap)
        print(k,total,len(profiles),dict(t),dict(deficit),first,'max singles',max(sum(a[1<<i] for i in range(4)) for a in avail));out.append(dict(k=k,all_squares=total,focal_profiles=profiles,counts=t,minimum_unmatched_histogram=deficit,example=first))
    text=json.dumps(out,indent=2)+'\n';assert not R.exists() or R.read_text()==text;R.write_text(text)
if __name__=='__main__':
    if sys.argv[1]=='freeze':
        text=json.dumps(rule,indent=2)+'\n';assert not P.exists() or P.read_text()==text;P.write_text(text)
    else:run()
