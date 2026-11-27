from ramsey_flank_singleton import *
from ramsey_relative_sign_joint_context import build
from collections import defaultdict

def run():
    rows=[s for s in combinations(range(8),3) if min(s[1]-s[0],s[2]-s[1])>=2];counts=defaultdict(Counter);example=None
    for ss in combinations(rows,5):
        S=grow(ss,1);es=[n for n,(i,j) in enumerate(ports) if not set(ss[i])&set(ss[j])];st=counts[len(es)];st['families']+=1
        if not es:continue
        full=sum(1<<i for i in es);M=[sum(1<<x for x in s) for s in S];U=[0]*32;E=[0]*32
        for p in range(1,32):
            b=p&-p;U[p]=U[p^b]|M[b.bit_length()-1];E[p]=sum(1<<i for i in es if all(p>>j&1 for j in ports[i]))
        def clauses(f,avoid,n):return {E[p] for p in range(32) if not U[p]&avoid and I[511&~(U[p]|f)]+p.bit_count()>=n}
        parent=clauses(0,0,7)
        for gap in range(1,9):
            f=3<<(gap-1);fe=clauses(f|f<<1|f>>1,f,5);sing=[b for b in fe if b.bit_count()==1];
            if not sing:continue
            allm=fe|clauses(f,0,6)
            for b in sing:
                st['raw']+=1
                if 0 in parent:kind='no_parent'
                elif b in parent:kind='forced_red'
                elif 0 in allm:kind='always_blocked'
                else:
                    rivals=sorted(m for m in allm if not m&b and not any(t&m==t for t in parent));kind='conditional' if rivals else 'reader'
                    if rivals and example is None:
                        m=rivals[0];c=full^m;assert c&b and all(verdict(graph(9,S,col)) for col in [full,c,full^b]);assert not verdict(build({gap:()},S,c)) and verdict(build({gap:()},S,full));example=dict(rows=ss,gap=gap,target=b,pass_color=full,fail_color=c)
                st[kind]+=1
    old=sum((counts[i] for i in (3,4)),Counter());assert (old['families'],old['raw'],old['always_blocked'],old['reader'],old['no_parent'])==(7024,1277,1017,58,202);tot=sum(counts.values(),Counter());assert tot['families']==15504;out=dict(protocol_sha=sha256((D.parent/'ramsey_flank_unfiltered_protocol.md').read_bytes()).hexdigest(),by_edges=counts,total=tot,example=example);print(out);save(D.parent/'ramsey_flank_unfiltered.json',out)
if __name__=='__main__':run()
