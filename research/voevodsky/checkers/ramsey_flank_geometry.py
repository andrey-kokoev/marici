from ramsey_flank_singleton import *
proto2=D.parent/'ramsey_flank_geometry_protocol.md';O=D.parent/'ramsey_flank_geometry.json'
def run():
    counts=Counter();by=Counter()
    for idx,(ss,es) in enumerate(family(),1):
        S=grow(ss,1);M=[sum(1<<v for v in s) for s in S];un=[0]*32;E=[0]*32
        for p in range(1,32):
            b=p&-p;un[p]=un[p^b]|M[b.bit_length()-1];E[p]=sum(1<<e for e in es if all(p>>j&1 for j in ports[e]))
        geo=set()
        for e in es:
            i,j=ports[e];u=511^(M[i]|M[j]);assert u.bit_count()==3 and u&2;adj=u&(u>>1)
            if adj.bit_count()!=1:continue
            gap=adj.bit_length();others=[k for k in range(5) if k not in (i,j) and not M[k]&u];
            if any(E[(1<<i)|(1<<j)|(1<<h)|(1<<l)]==1<<e for h,l in combinations(others,2)):geo.add((gap,e))
        def clauses(f,avoid,n):return {E[p] for p in range(32) if not un[p]&avoid and I[511&~(un[p]|f)]+p.bit_count()>=n}
        parent=clauses(0,0,7);full=sum(1<<e for e in es);observed=set()
        for gap in range(1,9):
            f=3<<(gap-1);fe=clauses(f|f<<1|f>>1,f,5);x=clauses(f,0,6)
            for e in es:
                b=1<<e
                if b not in fe:continue
                observed.add((gap,e));kind='seam touches site 2' if f&2 else 'isolated site 2';by[kind,'raw']+=1
                if not all(m&(full^b) for m in parent):continue
                by[kind,'variable']+=1
                if any(not m&b and not any(t&m==t for t in parent) for m in fe|x):continue
                by[kind,'reader']+=1
        assert geo==observed;counts['families']+=1;counts['witnesses']+=len(geo)
    print(counts,by);out=dict(protocol_sha=sha256(proto2.read_bytes()).hexdigest(),counts=counts,classes={k:{l:by[k,l] for l in ('raw','variable','reader')} for k in ('seam touches site 2','isolated site 2')});save(O,out)
if __name__=='__main__':run()
