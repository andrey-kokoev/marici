"""The proposed cycle-incidence normal form, using zero-based C7 labels."""
from itertools import combinations
PAIRS=tuple((i,j)for i,j in combinations(range(7),2)if j-i not in(1,6))
PROFILE=(0,1,1,2,1,2,1,0,1,1,2,0,2,0)

def profile_orbit(profile=PROFILE):
    orbit=set()
    for sign in(-1,1):
        for shift in range(7):
            counts={tuple(sorted(((sign*i+shift)%7,(sign*j+shift)%7))):c for(i,j),c in zip(PAIRS,profile)}
            orbit.add(tuple(counts[p]for p in PAIRS))
    return sorted(orbit)

def ordered_types(profile=PROFILE):
    return [0]+[k for k,count in enumerate(profile,1)for _ in range(count)]
