"""Prepare one labeled residual for exact t=3 test, with all its independent sets of size 5..7."""
from ramsey310_matching_joint import *
p=Path(__file__).resolve().parents[1]/'results/ramsey38_26_e73_hog.g6';n=int(sys.argv[1]);idx=int(sys.argv[2]);A=next(g for j,g in enumerate(instances(decode(p.read_bytes().splitlines()[n-1]))) if j==idx)
with open(sys.argv[3],'w') as f:
    for V in (A,*[list(sets(A,F,k)) for k in (5,6,7)]):print(len(V),*V,file=f)
