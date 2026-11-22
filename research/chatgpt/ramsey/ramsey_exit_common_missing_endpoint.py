"""Decode the third duad from the two red graphs' missing edges, not by composing corner permutations. Use the affine witness's duad-edge rule; test all 15 partitions."""
from itertools import combinations
from ramsey_seed_affine_witness import m,mate,P,T
from ramsey_folded_entry_handoff import D,json

def edges(M):
    removed={frozenset(P.index(e) for e in T[j-15] if e!=P[i]) for i,j in M};return {frozenset((i,k)) for i,k in combinations(range(15),2) if set(P[i]).isdisjoint(P[k])}-removed

def run():
    g,h=edges(m),edges(mate);out=[]
    for j,t in enumerate(T,15):
        vs={P.index(e) for e in t};pairs={frozenset(e) for e in combinations(vs,2)};x,=pairs-g;y,=pairs-h;common=x&y
        if x!=y:
            c,=common;a,=vs-x;b,=vs-y;assert {frozenset((a,b))}==pairs&g&h and c not in (a,b)
        out.append(dict(partition=j,missing=[sorted(x),sorted(y)],common_missing_endpoints=sorted(common)))
    assert sum(len(s['common_missing_endpoints'])==1 for s in out)==5;return out
if __name__=='__main__':
    out=run();print(out[-1]);(D/'ramsey_exit_common_missing_endpoint.json').write_text(json.dumps(out)+'\n')
