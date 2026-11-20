"""Two 11-rings with dihedral symmetry. Standard-library witness check."""
from itertools import combinations

def red(i,j):
    a,x=divmod(i,11); b,y=divmod(j,11)
    offsets=({1,3,8,10} if a==0 else {1,4,7,10}) if a==b else {3,8}
    return (y-x)%11 in offsets

if __name__=='__main__':
    for n,color in [(3,True),(7,False)]:
        assert not any(all(red(i,j)==color for i,j in combinations(t,2)) for t in combinations(range(22),n))
    print('Verified: no red triangle and no blue seven-set.')
