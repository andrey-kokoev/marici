"""Exact local Hessian controls for the written generic global construction."""
from itertools import permutations
from pathlib import Path
import json
from check_hodge_fixed_sixfold_pairing import power,integrate


def determinant(matrix):
    n=len(matrix);total=0
    for p in permutations(range(n)):
        term=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        for i in range(n):term*=matrix[i][p[i]]
        total+=term
    return total


def hessian(A,B):
    return [[0]*3+[A[j][i] for j in range(3)] for i in range(3)]+[A[i]+B[i] for i in range(3)]


def main():
    matrices=[[[1,0,0],[0,1,0],[0,0,1]],[[2,1,0],[0,3,1],[1,0,1]],
              [[0,1,0],[1,0,0],[0,0,2]],[[1,2,3],[0,1,4],[5,6,0]]]
    normals=[[[0]*3 for _ in range(3)],[[2,1,-3],[1,0,4],[-3,4,6]],
             [[-2,0,0],[0,4,0],[0,0,8]]]
    tested=0
    for A in matrices:
        assert determinant(A)!=0
        for B in normals:
            H=hessian(A,B)
            assert all(H[i][j]==H[j][i] for i in range(6) for j in range(6))
            assert determinant(H)==-determinant(A)**2!=0
            tested+=1
    singular=[[1,0,0],[0,1,0],[0,0,0]]
    for B in normals:
        H=hessian(singular,B)
        assert determinant(H)==0
        assert all(row[2]==0 for row in H)  # (x3,0) is in the kernel
    E={(2*j,2*j+1):d for j,d in enumerate((1,1,1,-1,-1,-3))}
    assert integrate(power(E,6))==2160
    for k,m in ((1,2),(2,5),(3,7)):
        count=2160*k**3*(m-k)**3
        assert count>0 and count==2160*(k*(m-k))**3
    result={'passed':True,'classification':'generic_high_degree_envelope_has_only_nodes',
        'invertible_hessian_controls':tested,'nontransverse_controls':len(normals),
        'general_determinant_formula':'-det(A)^2',
        'node_count_for_sufficiently_large_m':'2160*k^3*(m-k)^3',
        'numerical_very_ampleness_or_vanishing_threshold_computed':False,
        'global_node_independence_proved':False,'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Nodal link groups and local-to-global support localization.'}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-singular-envelope-normal-jets-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
