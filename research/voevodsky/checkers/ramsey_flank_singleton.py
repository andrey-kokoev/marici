"""Enumerate shape candidates by port mask and path independent number."""
from ramsey_paired_decoder_transfer import *
from collections import Counter
proto=D.parent/'ramsey_flank_singleton_protocol.md';R=D.parent/'ramsey_flank_singleton.json'
def independent(m):
    n=0
    while m:
        b=m&-m;m&=~(b|2*b);n+=1
    return n
I=list(map(independent,range(512)))
def run():
    counts=Counter();example=None;local=None
    for idx,(ss,es) in enumerate(family(),1):
        counts['families']+=1;S=grow(ss,1);forb=[sum(1<<x for x in s) for s in S];U=[0]*32;E=[0]*32
        for p in range(1,32):
            i=(p&-p).bit_length()-1;U[p]=U[p^(1<<i)]|forb[i];E[p]=sum(1<<e for e in es if all(p>>j&1 for j in ports[e]))
        def clauses(f,avoid,need):return {E[p] for p in range(32) if not U[p]&avoid and I[511&~(U[p]|f)]+p.bit_count()>=need}
        parent=clauses(0,0,7);full=sum(1<<e for e in es);cand=False
        for g in range(1,9):
            f=3<<(g-1);nb=(f|(f<<1)|(f>>1))&511;fe=clauses(nb,f,5);sing={m for m in fe if m.bit_count()==1};counts['E_singleton_seams']+=bool(sing)
            if not sing:continue
            X=clauses(f,0,6);allm=X|fe;counts['raw_E_singletons']+=len(sing)
            for b in sing-X:
                counts['pure_E']+=1
                if not all(m&(full^b) for m in parent):continue
                counts['variable_pure_E']+=1
                if local is None:local=dict(family=idx,rows=ss,gap=g,bit=b)
                rem={m for m in allm if not any(t&m==t for t in parent)}
                if not all(m&b for m in rem):continue
                counts['pure_reader']+=1;e=b.bit_length()-1;targets=[(k,p) for k in range(1,9) if k!=g for p in terms(S,k) if E[p]==b];
                if not targets:continue
                counts['remote_readers']+=1;cand=True
                if example is None:
                    vals=[]
                    for j in range(1<<len(es)):
                        c=sum(1<<v for i,v in enumerate(es) if j>>i&1)
                        if verdict(graph(9,S,c)):
                            ok=verdict(build({g:()},S,c));assert ok==bool(c&b);vals.append(ok)
                    assert set(vals)=={True,False};example=dict(family=idx,original_rows_1based=[[x+1 for x in s] for s in ss],read_gap=g,port_edge=[x+1 for x in ports[e]],targets=targets,eligible_bits=es,blue_parent=full^b,red_parent=full)
        counts['remote_families']+=cand
    out=dict(protocol_sha=sha256(proto.read_bytes()).hexdigest(),counts=counts,first_variable_local=local,example=example);print(out);save(R,out)
if __name__=='__main__':run()
