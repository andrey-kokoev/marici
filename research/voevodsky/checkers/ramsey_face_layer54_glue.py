"""Finish every two-side blue-six survivor in layer 54. Vertex labels 0..20=H, 21..24=Q,25..28=T,29,30=roots,31..34=shared face."""
from ramsey_face_pair_obstruction import bits,ind,CAT,D,decode
from ramsey_retention_slice import check
from itertools import combinations,product
from collections import Counter
from functools import reduce
from operator import and_,or_
import gzip,json

def audit():
    p=D.parent;wins=json.loads((p/'ramsey_face_blind_layer54.json').read_text())['both_pass'];ids={r['record'] for r in wins};A={i:decode(l.strip()) for i,l in enumerate(gzip.open(CAT.parent/'r37_21.g6.gz','rt')) if i in ids};b=decode((CAT/'r35_13.g6').read_text().strip());results=[]
    for r in wins:
        a=A[r['record']];ls=r['sites'];q,t=r['q'],r['t'];m=sum(1<<i for i in ls);vs=bits(q)+bits(t);P=dict(zip(bits(8191^(q|t)),ls));P.update(zip(vs,range(21,29)));I=ind(a);S=set(I);qs={k:[x for x in I if x.bit_count()==k] for k in (4,5,6)};three=[x for x in I if not x&m and x.bit_count()==3];st=Counter()
        def panels(group):
            req=[sum(1<<j for v,j in P.items() if j<21 and b[i]>>v&1) for i in bits(group)];ds=[[s|v for s in three if s|v in S] for v in req];miss={s:{k:sum(1<<j for j,x in enumerate(c) if not x&s) for k,c in qs.items()} for d in ds for s in d};out=[]
            def dfs(rows):
                if len(rows)==4:
                    st[f'{group}_six']+=1
                    if any(reduce(and_,(miss[v][5] for v in sub)) for sub in combinations(rows,3)):return
                    st[f'{group}_five']+=1
                    if not reduce(and_,(miss[v][4] for v in rows)):out.append(rows)
                    return
                for s in ds[len(rows)]:
                    if any(miss[v][6]&miss[s][6] for v in rows):continue
                    dfs(rows+[s])
            dfs([]);return out
        L,R=panels(q),panels(t);st.update(first=len(L),second=len(R),pairs=len(L)*len(R));examples=[]
        for l,h in product(L,R):
            g=a[:]+[0]*14
            def edge(i,j):g[i]|=1<<j;g[j]|=1<<i
            for v,s in enumerate(l+h,21):
                edge(v,29 if v<25 else 30)
                for j in bits(s):edge(v,j)
            for i,j in combinations(vs,2):
                if b[i]>>j&1:edge(P[i],P[j])
            if any(g[i]&g[j] for i in range(31) for j in bits(g[i])):continue
            st['triangle_free']+=1
            xs=bits(((1<<21)-1)^m);need={j:8-g[j].bit_count() for j in xs}
            if Counter(need.values())!={1:8,2:8}:continue
            st['degree_profile']+=1
            if not check(g,(1<<31)-1,3,9):continue
            st['old_legal']+=1;old=ind(g[:31]);X=sum(1<<j for j in xs);roots=3<<29;eights=[x for x in old if not x&roots and x.bit_count()==8];rows=[s for s in I if s&~X==0 and s.bit_count()==6 and all(s&x for x in eights)];singles=sum(1<<j for j in xs if need[j]==1)
            def grow(rr,start,once,twice):
                if len(rr)==4:
                    masks=Counter(sum(1<<i for i,s in enumerate(rr) if s>>j&1) for j in xs);pairs=[s for s in masks if s.bit_count()==2];
                    if not(all(masks[1<<i]==2 for i in range(4)) and len(pairs)==4 and all(masks[s]==2 for s in pairs) and all(sum(s>>i&1 for s in pairs)==2 for i in range(4))):return
                    gg=g[:]
                    for j,s in enumerate(rr,31):
                        gg[j]=s|roots
                        for i in bits(s|roots):gg[i]|=1<<j
                    assert all(v.bit_count()==8 for v in gg)
                    if check(gg,(1<<35)-1,3,9):examples.append(gg)
                    return
                for k in range(start,len(rows)):
                    s=rows[k];d=s&once
                    if not d&(twice|singles):grow(rr+[s],k,once|s,twice|d)
            grow([],0,0,0)
        results.append(dict(**r,counts=st,completions=examples));print(r['record'],st,len(examples))
    (p/'ramsey_face_layer54_glue.json').write_text(json.dumps(results,indent=2)+'\n')
if __name__=='__main__':audit()
