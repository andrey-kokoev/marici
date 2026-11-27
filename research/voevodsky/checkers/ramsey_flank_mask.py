from ramsey_flank_singleton import *
from ramsey_relative_sign_joint_context import build

def run():
    counts=Counter();types=Counter();examples={}
    for idx,(ss,es) in enumerate(family(),1):
        S=grow(ss,1);U=[0]*32;E=[0]*32
        for p in range(1,32):
            U[p]=sum(1<<v for v in set().union(*(S[i] for i in range(5) if p>>i&1)));E[p]=sum(1<<j for j in es if all(p>>i&1 for i in ports[j]))
        def clauses(f,avoid,n):return {E[p] for p in range(32) if not U[p]&avoid and I[511&~(U[p]|f)]+p.bit_count()>=n}
        parent=clauses(0,0,7);full=sum(1<<j for j in es)
        for gap in range(1,9):
            f=3<<(gap-1);fe=clauses(f|f<<1|f>>1,f,5);sing={m for m in fe if m.bit_count()==1}
            if not sing:continue
            x=clauses(f,0,6)
            for b in sing:
                eligible=lambda c:verdict(graph(9,S,c));success=lambda c:verdict(build({gap:()},S,c));assert eligible(full)==(0 not in parent);assert eligible(full^b)==all(m&(full^b) for m in parent)
                if 0 in parent:counts['no_parent']+=1;continue
                if b in parent:counts['forced_red']+=1;continue
                assert not success(full^b);comp={m for m in fe|x if not m&b and not any(t&m==t for t in parent)};assert success(full)==(0 not in comp)
                if not comp:counts['reader']+=1;continue
                label='never_accepts' if 0 in comp else 'conditional';counts[label]+=1;mins=sorted(m for m in comp if not any(t!=m and t&m==t for t in comp));origins=''.join(t for t,Z in [('X',x),('E',fe)] if any(m in Z for m in mins));types[label,origins]+=1
                for m in mins:
                    c=full^m;assert eligible(c) and c&b and not success(c)
                if (label,origins) not in examples:
                    m=mins[0];a=graph(9,S,full^m);t='X' if m in x else 'E';fl={gap-1,gap};pool=[v for v in range(14) if v not in fl and (t=='X' or all(not(a[v]>>h&1) for h in fl))];q=next(q for q in combinations(pool,6 if t=='X' else 5) if all(not(a[i]>>j&1) for i,j in combinations(q,2)) and sum(1<<j for j in es if all(i+9 in q for i in ports[j]))==m);edge=lambda j:[i+1 for i in ports[j]];examples[label,origins]=dict(family=idx,rows=[[v+1 for v in s] for s in ss],gap=gap,target=edge(b.bit_length()-1),other_pairs=[edge(j) for j in es if m>>j&1],kind=t,sites=[v+1 for v in q if v<9],ports=[v-8 for v in q if v>=9])
    assert sum(counts.values())==1277;out=dict(protocol_sha=sha256((D.parent/'ramsey_flank_mask_protocol.md').read_bytes()).hexdigest(),counts=counts,origins={'/'.join(k):v for k,v in types.items()},examples={'/'.join(k):v for k,v in examples.items()});print(out);save(D.parent/'ramsey_flank_mask.json',out)
if __name__=='__main__':run()
