"""Separate mere exit membership from occurrence at the second partition. Reconstruct the inbound duad from two partitions, without an inverse lookup or stored predecessor."""
from collections import Counter
from itertools import combinations
from ramsey_partition_turn_lookup import P,T,m,r,D,json

def shared(j,k):
    d,=set(T[j-15])&set(T[k-15]);return P.index(d)

def run():
    assert all(len(set(a)&set(b))<=1 for a,b in combinations(T,2));counts=[Counter(),Counter()];total=0
    def visit(i,M,used):
        nonlocal total
        if i<15:
            for j,t in enumerate(T,15):
                if j not in used and P[i] in t and (i!=0 or j==16) and (i!=7 or j==29):visit(i+1,M+[(i,j)],used|{j})
            return
        total+=1;mate=[(r[d],r[j]) for d,j in M]
        for ix,(left,right,target) in enumerate(((M,mate,(19,7)),(mate,M,(27,4)))):
            f=dict(left);g={j:d for d,j in right};x=0;seen=set();turns=[]
            while x not in seen:
                seen.add(x);j=f[x];u=g[j];turns.append((x,j,u));x=u
            a,b=turns[:2];assert shared(a[1],b[1])==b[0];j,u=target
            if g[j]!=u:continue
            incoming={k:d for d,k in left}[j];pos=next((i+1 for i,z in enumerate(turns) if z[1:]==target),None);counts[ix][incoming,pos]+=1
    visit(0,[],set());assert total==36;return dict(total=total,rows=[[(d,pos,n) for (d,pos),n in c.items()] for c in counts],selected=[shared(16,19),shared(17,27)])
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_entry_anchored_turn.json').write_text(json.dumps(out)+'\n')
