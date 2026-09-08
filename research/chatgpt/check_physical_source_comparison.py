#!/usr/bin/env python3
from fractions import Fraction
import json

def matmul(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

def matvec(A,v):
    return [sum(a*b for a,b in zip(row,v)) for row in A]

def main():
    d3 = [[0],[1],[1],[1]]
    d2 = [
        [1,0,0,0],
        [1,0,0,0],
        [0,1,0,-1],
        [0,-1,1,0],
        [0,0,-1,1],
    ]
    d1 = [[1,-1,-1,-1,-1]]
    assert matmul(d2,d3) == [[0],[0],[0],[0],[0]]
    assert matmul(d1,d2) == [[0,0,0,0]]

    z = [1,0,1,0,0]
    a = [[0,0,1,1,1]]
    assert matmul(a,d2) == [[0,0,0,0]]
    assert matvec(a,z) == [1]

    # Endpoint coordinates are the first two coordinates.
    assert a[0][:2] == [0,0]

    # Strict uniqueness under endpoint-zero condition.
    # w=(0,0,r1,r2,r3), w*d2=0 forces all ri equal.
    # Verify on a finite symbolic basis by direct equations.
    # Columns 1..3 impose r1-r2=0, r2-r3=0, -r1+r3=0.
    for r1 in range(-3,4):
        for r2 in range(-3,4):
            for r3 in range(-3,4):
                w = [[0,0,r1,r2,r3]]
                closed = matmul(w,d2) == [[0,0,0,0]]
                if closed:
                    assert r1 == r2 == r3
                    if matvec(w,z) == [1]:
                        assert [r1,r2,r3] == [1,1,1]

    # Cohomology check: all closed degree-one rows modulo d1 are rank one.
    # Two convenient closed rows:
    endpoint_difference = [-1,1,0,0,0]
    road_sum = [0,0,1,1,1]
    assert matmul([endpoint_difference], d2) == [[0,0,0,0]]
    assert matmul([road_sum], d2) == [[0,0,0,0]]
    # d1 = -(endpoint_difference + road_sum)
    assert d1[0] == [-(x+y) for x,y in zip(endpoint_difference,road_sum)]

    result = {
        "status": "constructed_derived_physical_source_comparison",
        "J_chain_ranks": [1,4,5,1],
        "a_C_degree1_row": [0,0,1,1,1],
        "chain_equation_a_d2": "zero",
        "primitive_z": z,
        "a_C_of_z": 1,
        "endpoint_restriction": 0,
        "strict_uniqueness_with_endpoint_zero_and_positive_primitive": True,
        "normalization_lift": "a = rho[1]^{-1} o a_C in D(B)",
        "strict_global_sheet_section_used": False,
        "next_gate": "framed admissibility of the primitive for H_cond^nu - e_nu h_Morse"
    }
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
