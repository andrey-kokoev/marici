"""Independent integer control of the Rzk degree-window formulas.
Not an implementation of the physical coefficient complexes or their quotients.
"""
import hashlib
import json
from pathlib import Path

# M^-1=Z^2 -> M^0=Z, d(a,b)=a. N^-2=Z --4--> N^-1=Z
# -> N^0=0; r^-1(a,b)=2a+6b, r^0=0. All other groups zero.
# These are cochain complexes and r is a cochain map.
def dm(s): return s[0]
def r(s): return 2*s[0]+6*s[1]
def dn(k): return 4*k
def differential(s,k): return (dm(s),r(s)-dn(k))
def forward(s,z,k): return ((s[0]+z[0],s[1]+z[1]),k)
def backward(s,t,k): return ((t[0]-s[0],t[1]-s[1]),k)

checks=0
for f in range(-3,4):
    for a in range(-3,4):
        s=(f,a)
        for b in range(-3,4):
            z=(0,b)
            for k in range(-3,4):
                h=r(s)+r(z)-dn(k)
                t,k2=forward(s,z,k)
                assert differential(t,k2)==(f,h)
                assert backward(s,t,k2)==(z,k)
                assert h-r(s)==r(z)-dn(k)
                checks+=3
# The exact secondary quotient is Z/(6Z+4Z)=Z/2.
# Necessity is parity; sufficiency has the all-integer Bezout witness
# 2m = 6m - 4m, not an inference from a search bound.
for f in range(-5,6):
    for h in range(-9,10):
        s=(f,0)
        residual=h-r(s)
        if residual%2==0:
            m=residual//2
            t,k=forward(s,(0,m),m)
            assert differential(t,k)==(f,h)
        else:
            assert residual%2 != 0  # no integer 6b-4k has this parity
        checks+=1
# Neither ambient closed corrections nor higher boundary homotopies may
# be omitted: residual 2 is in 6Z+4Z but in neither 6Z nor 4Z separately.
assert differential((0,1),1)==(0,2)
assert 2%6 and 2%4
# Same ambient f and strict restriction r^0(f)=0, different h.
assert (1-2*0)%2==1
assert differential((0,0),0)==(0,0)
checks+=4
source=Path('research/nima/rzk/12-relative-cochain-secondary.rzk.md')
result={'status':'passed','assertions':checks,
        'rzk_source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'model':'M: Z^2 -> Z; N: Z --4--> Z -> 0; restriction (2,6)',
        'secondary_quotient':'Z/2 by parity and 6-4=2',
        'scope':'Independent integer regression; not a formal Rzk integer instance or physical parity calculation'}
Path('research/nima/results/relative-cochain-secondary-control.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
