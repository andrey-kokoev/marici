"""Test a specific cross-k binding: four seed columns as vertices of an inscribed tetrahedron, its six edges as their unique common cube faces, incident face pairs as cube edge addresses. B pole selects its body diagonal only. Compare BOTH endpoints and both boundary-selected rows."""
from ramsey_cube_pair_rules import F,V,G,edges,D,json,combinations,permutations
from ramsey_seed_affine_witness import P,T,m,mate
from collections import Counter

def opposite(c):return ''.join(str(1-int(i)) for i in c)
def run():
    R=json.loads((D/'ramsey_cube_pair_rules.json').read_text());lookup={}
    for e,states in R.items():
        for g in G:lookup[tuple(sorted(map(g,e.split()))) ]={g(c,state=True) for c in states}
    seed=[]
    for M in (m,mate):
        removed={tuple(sorted(P.index(d) for d in T[j-15] if d!=P[i])) for i,j in M};seed.append({(i,j) for i,j in combinations(range(15),2) if set(P[i]).isdisjoint(P[j]) and (i,j) not in removed})
    records=[];canonical=None;hand=Counter()
    for parity in range(2):
        for verts in permutations([v for v in V if v.count('1')%2==parity]):
            faces=[''.join(a if a==b else '*' for a,b in zip(x,y)) for x,y in combinations(verts,2)];ids={}
            for i,(u,v) in enumerate(P):
                a,b=faces[u],faces[v];w=''.join(x if y=='*' else y for x,y in zip(a,b));
                if w.count('*')==1:ids[i]=w
            assert len(set(ids.values()))==len(ids)==12;coords=[verts[0],opposite(verts[0])];pairs=list(combinations(ids,2));assert len(pairs)==66
            # Unique proper cube rotation implementing row swap (23) on body diagonals fixes the B line and exchanges endpoints.
            line=lambda v:min(v,opposite(v));target=[verts[0],verts[2],verts[1],verts[3]];maps={tuple(g(v,state=True) for v in V) for g in G if all(line(g(x,state=True))==line(y) for x,y in zip(verts,target))};assert len(maps)==1 and maps.pop()[V.index(coords[0])]==coords[1]
            mismatch=[[sum(((i,j) in red)!=(c in lookup.get(tuple(sorted((ids[i],ids[j]))),())) for i,j in pairs) for c in coords] for red in seed];records.append(mismatch)
            if verts==('000','011','101','110'):canonical=mismatch
            a,b,c=[[int(y)-int(x) for x,y in zip(verts[0],v)] for v in verts[1:]];det=sum(a[i]*(b[(i+1)%3]*c[(i+2)%3]-b[(i+2)%3]*c[(i+1)%3]) for i in range(3));hand[det,tuple(mismatch[0])]+=1
    hist=Counter(tuple(tuple(row) for row in M) for M in records);print(hist,'canonical',canonical,'oriented',hand);return {'canonical_mismatch':canonical,'orientation_histogram':[[key,n] for key,n in hand.items()],'binding_count':len(records),'comparisons_per_row':66,'mismatch_histogram':[[key,n] for key,n in hist.items()]}
if __name__=='__main__':(D/'ramsey_boundary_corner_bridge.json').write_text(json.dumps(run())+'\n')
