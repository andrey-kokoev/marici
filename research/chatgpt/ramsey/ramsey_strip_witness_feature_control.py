"""Factor the seed filter into swap, number of changed incidences, and alternating cycle shape. Count single Hall choices, not unordered swap pairs. Also remove the swap-partner constraint as a control."""
from ramsey_strip_witness_orbits import orbits,r,Counter
from itertools import combinations

def profile(a,b):
    ia=dict(a);ib={y:x for x,y in b};todo=set(ia);lens=[]
    while todo:
        x=next(iter(todo));n=0
        while x in todo:todo.remove(x);n+=1;x=ib[ia[x]]
        lens.append(n)
    return tuple(sorted(lens))
H=Counter();free=Counter();target=(1,1,1,1,11)
for a,k in orbits.items():
    b=frozenset((r[i],r[15+j]-15) for i,j in a);assert orbits[b]==k;H[k,profile(a,b)]+=1
for a,b in combinations(orbits,2):
    if profile(a,b)==target:free[tuple(sorted((orbits[a],orbits[b])))]+=1
print('swap with four common incidences',[(k,p,n) for (k,p),n in sorted(H.items()) if p.count(1)==4]);print('no partner constraint',free);print('full profiles',H)
