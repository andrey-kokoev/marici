"""Shared old-core obligations: blind search for a verified attachment or exhaustion from each maximal first. Pairwise six-set screen fixed; add ONE violated 5/4-row at a time. Compare cold vs persistent rows, identical candidate order."""
from ramsey_capacity_transfer_78 import D,json,inds,decode,bits
from ramsey_fork_audit_uniform import grow,verify
from collections import Counter

def audit(H):
    I=inds(H);M=sorted(s for s in I if all(s>>v&1 or s&h for v,h in enumerate(H)));T={k:sorted(s for s in I if s.bit_count()==k) for k in (4,5,6)};miss={k:[sum(1<<j for j,t in enumerate(T[k]) if not s&t) for s in M] for k in T};w,q,p=(miss[k] for k in (4,5,6));adj=[sum(1<<j for j,b in enumerate(p) if not b&a) for a in p];n=len(M);F=(1<<n)-1;outputs=[]
    for warm in (False,True):
        L=J=0;out=[]
        for a in range(n):
            if not warm:L=J=0
            trace=[];witness=None
            while True:
                triple=None
                for b in bits(adj[a]):
                    N=adj[a]&adj[b]&~((1<<b)-1);ab=q[a]&q[b];ab4=w[a]&w[b]
                    for c in bits(N):
                        if ab&q[c]&L:continue
                        danger=(ab|((q[a]|q[b])&q[c]));danger4=ab4&w[c]
                        for d in bits(N&adj[c]&~((1<<c)-1)):
                            if danger&q[d]&L or danger4&w[d]&J:continue
                            triple=(b,c,d);break
                        if triple:break
                    if triple:break
                if not triple:break
                fail5=(ab&q[c])|(danger&q[d]);fail4=danger4&w[d]
                if not fail5|fail4:
                    witness=[M[b],M[c],M[d]];verify(grow(H,[M[a],*witness]),8);break
                k=5 if fail5 else 4;v=next(bits(fail5 or fail4));bit=1<<v
                if k==5:assert not bit&L;L|=bit
                else:assert not bit&J;J|=bit
                trace.append(T[k][v])
            out.append(dict(first=M[a],witness=witness,learned=trace))
        outputs.append(out)
    assert all(a['witness']==b['witness'] for a,b in zip(*outputs));return outputs

def run():
    cases=json.loads((D/'ramsey_bare_core_rank.json').read_text());lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[]
    for r in cases:
        G=decode(lines[r['parent']-1]);V=[i for i in range(22) if i!=r['deleted']];H=[sum(1<<j for j,y in enumerate(V) if G[x]>>y&1) for x in V];cold,warm=audit(H);assert [s['first'] for s in warm if s['witness']]==r['good'];out.append(dict(parent=r['parent'],deleted=r['deleted'],cold_counts=[len(s['learned']) for s in cold],warm=warm))
    return out
if __name__=='__main__':
    z=run();(D/'ramsey_blind_row_builder.json').write_text(json.dumps(z)+'\n');print(sum(sum(r['cold_counts']) for r in z),sum(len(s['learned']) for r in z for s in r['warm']),Counter((bool(s['witness']),bool(s['learned'])) for r in z for s in r['warm']));print(Counter(t.bit_count() for r in z for s in r['warm'] for t in s['learned']))
