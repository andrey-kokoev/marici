"""Test for an empty triple of row-hit families over maximal independent fourth supports. Superset of all tight rows of any legal fixed triple. Prune only by union cardinality; if empty triple found, still requires pairwise checks and simultaneous tightness."""
from ramsey_fork_audit_uniform import inds,grow,D,json
from ramsey_deletion_rank_new_parents import graph,induce
from ramsey_hall_center_conjecture import decode

def audit(H,k):
    I=inds(H);M=[s for s in I if all(s>>i&1 or s&r for i,r in enumerate(H))];n=len(M);allm=(1<<n)-1;cols=[sum(1<<i for i,s in enumerate(M) if s>>v&1) for v in range(len(H))];rows=[]
    for t in I:
        if k-4<=t.bit_count()<=k-2:
            h=0;s=t
            while s:x=s&-s;s-=x;h|=cols[x.bit_length()-1]
            m=allm^h;rows.append((m.bit_count(),m,t))
    rows.sort(reverse=True);tested=0;bound=n;pairbound=n;example=None
    for i,(a,x,t) in enumerate(rows):
        if 3*a<n:break
        for j in range(i+1,len(rows)):
            b,y,u=rows[j];
            if a+2*b<n:break
            if (x|y).bit_count()+b<n:continue
            for l in range(j+1,len(rows)):
                c,z,v=rows[l];
                if a+b+c<n:break
                tested+=1;left=n-(x|y|z).bit_count();bound=min(bound,left);pairbound=min(pairbound,n-max((x|y).bit_count(),(x|z).bit_count(),(y|z).bit_count()))
                if not left and all((a1|b1)!=allm for a1,b1 in ((x,y),(x,z),(y,z))):example=[t,u,v];break
            if example:break
        if example:break
    return dict(maximal_supports=n,rows=len(rows),three_largest_miss_counts=[r[0] for r in rows[:3]],union_tests=tested,lower_bound_surviving_supports=min(max(1,n-sum(r[0] for r in rows[:3])),bound),empty_pairwise_viable_triple=example)
if __name__=='__main__':
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());A=grow(p['stem_graphs'][-1],p['alternate']['to34']);B=induce(graph((1,7,11,16)),list(range(1,35)));B[0]|=1<<33;B[33]|=1;B[11]^=1<<22;B[22]^=1<<11
    out={'discovery':audit(A,10),'different_34':audit(B,10)};print(out,flush=True);(D/'ramsey_three_row_conflict_test.json').write_text(json.dumps(out)+'\n')
