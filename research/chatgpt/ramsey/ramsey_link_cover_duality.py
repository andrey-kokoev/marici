"""Exact minimum cover of partner triangles by missed five-sets, and maximum packing of triangles with disjoint miss lists. Certificates on all distributed failures."""
from functools import lru_cache
from itertools import combinations
from ramsey_first_link_obstructions import run,D,json,bits,Counter

def audit():
    out=[]
    def visit(r,A,T,patterns,num):
        ls=[]
        for s in sorted(patterns,key=lambda x:(x.bit_count(),x)):
            if all(t&s!=t for t in ls):ls.append(s)
        @lru_cache(None)
        def cover(rem):
            if not rem:return ()
            return min(((v,)+cover(tuple(s for s in rem if not s>>v&1)) for v in bits(rem[0])),key=len)
        cert=cover(tuple(ls));
        @lru_cache(None)
        def pack(rem):
            if not rem:return ()
            a=rem[0];yes=(a,)+pack(tuple(s for s in rem[1:] if not s&a));return yes if len(yes)==len(cert) else max(yes,pack(rem[1:]),key=len)
        lower=pack(tuple(ls));assert len(lower)<=len(cert) and all(any(s>>v&1 for v in cert) for s in patterns) and all(not s&t for s,t in combinations(lower,2));out.append(dict(parent=r['parent'],deleted=r['deleted'],first=A,triangles=num,patterns=len(patterns),minimal=len(ls),cover=[T[v] for v in cert],packing=[dict(partners=patterns[s],missed=[T[v] for v in bits(s)]) for s in lower]))
    run(visit);return out
if __name__=='__main__':
    z=audit();print(Counter((len(r['cover']),len(r['packing'])) for r in z));print(max(z,key=lambda r:len(r['cover'])));(D/'ramsey_link_cover_duality.json').write_text(json.dumps(z)+'\n')
