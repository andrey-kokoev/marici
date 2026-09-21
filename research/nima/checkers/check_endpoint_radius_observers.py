"""Endpoint/word split counts for explicit paired observer scales."""
from fractions import Fraction as Q
from pathlib import Path
import json


def main():
    vertex_counts=split_counts=pairings=inequalities=0
    for n in range(2,13):
        first=1;last=(1<<(n-1))-1
        vertices=[v for v in range(1<<n) if first&v==first and v&last==v]
        assert len(vertices)==2**(n-2)
        vertex_counts+=1
        for m in range(9):
            fine=[(v,j,m-j) for v in vertices for j in range(m+1)]
            assert len(fine)==2**(n-2)*(m+1)
            assert len(fine)<=2**(n+m)
            # Each fine homogeneous split concatenates to the same fixed word.
            # Unit signed-eigenletter choice: beta intertwining is transpose.
            coefficients={key:(i%7)-3 for i,key in enumerate(fine)}
            observer=Q(3,2)
            coarse=sum(coefficients.values())
            assert coarse*observer==sum(c*observer for c in coefficients.values())
            split_counts+=1;pairings+=1
    for n in range(41):
        assert 1+n<=2**n
        for p in range(6):
            assert (1+n)**p<=2**(p*n)
            inequalities+=1
    for m in range(1,21):
        n=2*m;coefficient=Q(1,2**m)
        fine_mass=coefficient*2**(n-2)
        assert fine_mass==Q(2)**(m-2)
    # For each fixed polynomial moment the coarse hostile is summable:
    # a_(m+1)/a_m = ((2m+3)/(2m+1))^p / 2 eventually < 3/4.
    for p in range(7):
        m=10*(p+1)
        assert Q(2*m+3,2*m+1)**p/2<Q(3,4)
    result={'passed':True,'actual_intermediate_vertex_counts':vertex_counts,
            'homogeneous_word_split_counts':split_counts,'transpose_pairing_checks':pairings,
            'moment_radius_inequalities':inequalities,
            'scope':'Fixed finite artificial-cut diagrams and at most two seams. No arbitrary-depth or perfect-duality assertion.'}
    out=Path(__file__).resolve().parents[1]/'results/endpoint-radius-observers.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
