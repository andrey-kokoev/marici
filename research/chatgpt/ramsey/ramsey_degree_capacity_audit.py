"""Screen all 22 deletion cases without seven/six-set tests. For completeness of rejection for a REAL extension, enlarge supports to independent maximal sets (preserves triangle/alpha and hence degree cap). Passing this maximal-support screen is not a feasibility certificate."""
from ramsey_deletion_rank_new_parents import graph,induce,D,json
from ramsey_fork_audit_uniform import inds,verify,grow
from ramsey_final_miss_levels import bits
from collections import Counter

def screen(B):
    I=inds(B);top=[s for s in I if s.bit_count()==8];M=[s for s in I if all(s>>v&1 or s&r for v,r in enumerate(B))];masks=[sum(1<<i for i,t in enumerate(top) if t>>v&1) for v in range(len(B))];miss=[]
    for s in M:
        h=0
        for v in bits(s):h|=masks[v]
        miss.append(((1<<len(top))-1)^h)
    hot=lambda k:sum(1<<v for v,r in enumerate(B) if r.bit_count()>=k);d8,d7,d6=map(hot,(8,7,6));assert max(map(int.bit_count,B))<=8
    adj=[sum(1<<j for j in range(i,len(M)) if not x&miss[j]) for i,x in enumerate(miss)];first=None
    for i,row in enumerate(adj):
        a=M[i]
        for j in bits(row):
            b=M[j];common=row&adj[j];ab=a&b;pair=a|b
            for k in bits(common):
                tail=common&adj[k]
                if not tail:continue
                if first is None:first=[i,j,k,(tail&-tail).bit_length()-1]
                c=M[k];twice=ab|(pair&c);triple=ab&c
                if twice&d8 or triple&d7:continue
                ban=((pair|c)&d8)|(twice&d7)|(triple&d6)
                for l in bits(tail):
                    if not M[l]&ban:return True,[a,b,c,M[l]]
    return first is not None,None

def run():
    H=induce(graph((1,7,11,16)),list(range(1,35)));src=json.loads((D/'ramsey_deletion_rank_new_parents.json').read_text());out=[]
    for q in src:
        A=H[:]
        for a,b in q['added']:A[a]|=1<<b;A[b]|=1<<a
        for r in q['rows']:
            u,v=r['edge'];B=A[:];B[u]^=1<<v;B[v]^=1<<u;pair,S=screen(B);out.append(dict(parent=len(q['added']),edge=[u,v],pairwise=pair,capacity=bool(S),example=S,actual=r['valid']));assert S or not r['valid']
            if S:out[-1]['verified_graph']=verify(grow(B,S),10)
    return out
if __name__=='__main__':
    out=run();print(Counter((q['pairwise'],q['capacity'],q['actual']) for q in out));(D/'ramsey_degree_capacity_audit.json').write_text(json.dumps(out)+'\n')
