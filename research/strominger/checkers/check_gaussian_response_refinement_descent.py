"""Small exact hostile: a response-only refinement map need not exist.
This is a positive weighted-graph example, not an FCC subdivision claim.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
import hashlib
from check_fcc_gaussian_boundary import reduce_kernel

OUT=Path(__file__).resolve().parents[1]/'results/gaussian-response-refinement-descent'

def subdivide(k):
    # Preserve each old vertex mass; replace every spring by two springs of the
    # same strength with a fresh zero-mass midpoint. This is NOT a tuned
    # response-preserving subdivision (that would double each new spring).
    edges=[(i,j,-k[i][j]) for i in range(len(k)) for j in range(i) if k[i][j]]
    masses=[sum(row) for row in k]; assert min(masses)>0
    size=len(k)+len(edges); a=[[Q(0) for _ in range(size)] for _ in range(size)]
    for i,m in enumerate(masses):a[i][i]=m
    for midpoint,(i,j,spring) in enumerate(edges,len(k)):
        assert spring>0
        for v in (i,j):
            a[v][v]+=spring; a[midpoint][midpoint]+=spring
            a[v][midpoint]-=spring; a[midpoint][v]-=spring
    return a

def encode(s):return [[str(x) for x in row] for row in s]

def main():
    expected=[[Q(2),Q(-1)],[Q(-1),Q(2)]]
    packets=[]
    for c in ((-1,-1),(-2,-1)):
        k=[[expected[i][j]+Q(c[i]*c[j],4) for j in range(2)]+[Q(c[i])] for i in range(2)]
        k.append([Q(c[0]),Q(c[1]),Q(4)])
        s,d,e=reduce_kernel(k,[0,1]); assert s==expected and d==4 and e==1
        fine=subdivide(k); fs,fd,fe=reduce_kernel(fine,[0,1])
        packets.append({'bulkKernel':encode(k),'boundaryKernel':encode(s),
                        'normalization':{'twoPiPower':e,'determinant':str(d)},
                        'refinedBoundaryKernel':encode(fs),
                        'refinedNormalization':{'twoPiPower':fe,'determinant':str(fd)}})
    assert packets[0]['refinedBoundaryKernel']!=packets[1]['refinedBoundaryKernel']
    # Non-unit-denominator and two-pivot Bareiss regression.
    s,d,e=reduce_kernel([[Q(2),Q(1),Q(0)],[Q(1),Q(3),Q(1)],[Q(0),Q(1),Q(4)]],[2])
    assert s==[[Q(18,5)]] and d==5 and e==2
    OUT.mkdir(parents=True,exist_ok=True)
    receipt={'status':'pass','scope':'generic positive weighted Gaussian graph; not the FCC factor-2 cell rule',
             'rule':'subdivide each spring with two identical-strength springs, retain all old vertex masses, give fresh midpoints zero mass',
             'sourceHashes':{str(p.relative_to(Path(__file__).resolve().parents[3])):hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),Path(__file__).with_name('check_fcc_gaussian_boundary.py'))},
             'packets':packets,
             'disposition':'Equal complete coarse boundary amplitudes acquire different refined kernels. This declared microscopic rule does not descend to a function of boundary amplitude alone.'}
    (OUT/'verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__':main()
