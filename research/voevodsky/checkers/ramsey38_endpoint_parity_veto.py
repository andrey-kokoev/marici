"""Local endpoint veto: protected stars, required cells and exposed triangle parity."""
from ramsey38_boundary_index_holdout import P as old,key,p
from ramsey38_boundary_ball_index import shared_index,candidates
from itertools import permutations,combinations
from functools import lru_cache
from collections import Counter
import sys
P=p.prev.out/'ramsey38_endpoint_veto_cases.json'
def freeze():
    prior={e['record']:e['root'] for path in (old,p.P) for e in p.json.loads(path.read_text())['entries']};seen=set();entries=[]
    with p.gzip.open(p.prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i in prior:seen.add(key(*p.setup(p.graph(line.strip()),prior[i])))
            if i<=260372:continue
            g=p.graph(line.strip())
            for u in sorted(g):
                if len(g[u])!=7:continue
                L,r,m=p.setup(g,u)
                if max(map(int.bit_count,r.values()))>4 or sum(s.bit_count()==2 for s in r.values())<2 or not any(p.setup(p.add(g,a),u)[2] for a in m):continue
                k=key(L,r,m)
                if k in seen:continue
                seen.add(k);entries.append(dict(record=i,root=u));break
            if len(entries)==32:break
    assert len(entries)==32;p.prev.save(P,dict(entries=entries,protocol='Same graph-only eligibility as boundary index holdout, after 260372, exclude calibration and holdout keys. No stage tests.'))

def veto(B,buried,exposed,required,edge_witness=False):
    # Cell-selection variables. A boundary triangle must have odd incidence.
    # An interior edge has a cycle as link; a subcycle in the endpoint link
    # must use the full cycle. Likewise an interior triangle needs both cells.
    cells=list(B);forced={t for t in B if any(s<=t for s in buried)}|required
    if not required<=B:return 'missing cell'
    eq=[(1<<i,1) for i,t in enumerate(cells) if t in forced]
    for s in buried:
        fs={frozenset(f) for t in B if s<=t for f in combinations(t,3) if s<=set(f)}
        if not fs or any(sum(f<=t for t in B)!=2 for f in fs):return 'open star'
    for f in exposed:
        if len(f)==3:eq.append((sum(1<<i for i,t in enumerate(cells) if f<=t),1))
    basis={}
    for m,b in eq:
        while m:
            i=m.bit_length();row=basis.get(i)
            if row is None:basis[i]=(m,b);break
            m^=row[0];b^=row[1]
        if not m and b:return 'inconsistent triangle equations'
    if edge_witness:
        # Each exposed edge needs some incident boundary triangle. A witness
        # adds one affine equation; try compatible witnesses jointly, not
        # independently per edge. Do not test shellability or containment here.
        triangles={frozenset(f) for t in cells for f in combinations(t,3)}
        clauses=[{sum(1<<i for i,t in enumerate(cells) if f<=t) for f in triangles if s<=f} for s in exposed if len(s)==2]
        def compatible(i,rows):
            if i==len(clauses):return True
            for m in clauses[i]:
                b=1
                while m and m.bit_length() in rows:
                    h,k=rows[m.bit_length()];m^=h;b^=k
                if not m:
                    if not b and compatible(i+1,rows):return True
                elif compatible(i+1,{**rows,m.bit_length():(m,b)}):return True
            return False
        clauses.sort(key=len)
        if not compatible(0,basis):return 'no joint exposed-edge witnesses'
    return None

def check(edge_witness=False):
    es=p.json.loads(P.read_text())['entries'];ids={e['record'] for e in es};words={};cnt=Counter();idx=shared_index()
    with p.gzip.open(p.prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i in ids:words[i]=line.strip()
            if i>=max(ids):break
    for e in es:
        g=p.graph(words[e['record']]);u=e['root'];L,rows,_,dec,stage,_=p.prepare(g,u);_,rs,ms=p.setup(g,u)
        @lru_cache(None)
        def pool(req,bds):return {frozenset(ts) for bd in bds for ts in candidates(idx,L,req,set(map(dec,bd)))}
        for a in ms:
            r,S=stage((a,));x,v=a;rr={**rs,x:rs[x]|1<<L.index(v)}
            for b in p.setup(p.add(g,a),u)[2]:
                q,T=stage(tuple(sorted((a,b))))
                for j,k in permutations(rows,2):
                    A=pool(r,tuple(S.get(frozenset([j]),())))
                    if not A:continue
                    for B in pool(q,tuple(T.get(frozenset([j,k]),()))):
                        yes=any(M<B for M in A);reason=veto(B,{dec(rs[x]),dec(rr[j])},{dec(s) for h,s in rr.items() if h!=j and s.bit_count()<4},{dec(s) for s in rr.values() if s.bit_count()==4},edge_witness);assert not (reason and yes);cnt[reason or ('feasible' if yes else 'missed negative')]+=1
    print(cnt);p.prev.save(p.prev.out/('ramsey38_endpoint_edge_veto.json' if edge_witness else 'ramsey38_endpoint_parity_veto.json'),dict(source_sha=p.prev.sha(P.read_bytes()),counts=dict(cnt)))
if __name__=='__main__':{'freeze':freeze,'check':check,'edges':lambda:check(True)}[sys.argv[1]]()
