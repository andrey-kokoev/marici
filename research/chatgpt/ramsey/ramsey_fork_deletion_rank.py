"""Frozen ranking: among ALL legal red-edge deletions on skip-0 core, maximize the number of ORIGINAL independent sevens hit by one newly available support containing both endpoints. Equal scores stay tied. Predict first tier succeeds; exact four-port search only after scoring all edges."""
from ramsey_fork_audit_uniform import inds,grow,D,json,verify

def rank(A):
    I=inds(A);rows=[s for s in I if s.bit_count()==7];n=len(A);hit=[sum(1<<i for i,s in enumerate(rows) if s>>v&1) for v in range(n)];out=[]
    for u in range(n):
        for v in range(u):
            if not A[u]>>v&1:continue
            ban=A[u]|A[v];extensions=[s for s in I if not s&ban];
            if max(map(int.bit_count,extensions))>=7:continue
            score=0;winner=None
            for s in extensions:
                h=hit[u]|hit[v];z=s
                while z:b=z&-z;h|=hit[b.bit_length()-1];z-=b
                if h.bit_count()>score:score=h.bit_count();winner=s|(1<<u)|(1<<v)
            out.append(dict(edge=[v,u],hit=score,total=len(rows),best_support=winner))
    return out

def evaluate(A):
    out=rank(A);best=max((r['hit'] for r in out),default=None)
    from ramsey_ports_saturated_core import four
    for r in out:
        u,v=r['edge'];B=A[:];B[u]^=1<<v;B[v]^=1<<u;r['prediction']=r['hit']==best;z=four(B)['supports'];r['valid']=bool(z);r['witness']=z
        if z:verify(grow(B,z),10)
    return out
if __name__=='__main__':
    from collections import Counter
    from ramsey_port_clique_transfer import induce
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());A=grow(p['stem_graphs'][-1],p['to35'][1:]);out=evaluate(A);print(Counter((r['hit'],r['valid']) for r in out));(D/'ramsey_fork_deletion_rank.json').write_text(json.dumps(out)+'\n');G=p['graph35'];controls={}
    for i in range(3):
        rows=evaluate(induce(G,[j for j in range(35) if j!=i]));controls[i]=rows;print(i,Counter((r['hit'],r['valid']) for r in rows),flush=True)
    (D/'ramsey_fork_deletion_rank_controls.json').write_text(json.dumps(controls)+'\n')
