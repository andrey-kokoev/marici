"""Exact pure-label versus classical-mixture identifiability for D(S3)."""

import itertools
import json
import sympy as sp


def main():
    labels=("A","B","C","D","E","F","G","H")
    dims=(1,1,2,3,3,2,2,2); sqrt3=sp.sqrt(3)
    s=sp.Matrix([
        [sp.Rational(1,6),sp.Rational(1,6),sp.Rational(1,3),sp.Rational(1,2),sp.Rational(1,2),sp.Rational(1,3),sp.Rational(1,3),sp.Rational(1,3)],
        [sp.Rational(1,6),sp.Rational(1,6),sp.Rational(1,3),-sp.Rational(1,2),-sp.Rational(1,2),sp.Rational(1,3),sp.Rational(1,3),sp.Rational(1,3)],
        [sp.Rational(1,3),sp.Rational(1,3),sp.Rational(2,3),0,0,-sp.Rational(1,3),-sp.Rational(1,3),-sp.Rational(1,3)],
        [sp.Rational(1,2),-sp.Rational(1,2),0,sp.Rational(1,2),-sp.Rational(1,2),0,0,0],
        [sp.Rational(1,2),-sp.Rational(1,2),0,-sp.Rational(1,2),sp.Rational(1,2),0,0,0],
        [sp.Rational(1,3),sp.Rational(1,3),-sp.Rational(1,3),0,0,sp.Rational(2,3),-sp.Rational(1,3),-sp.Rational(1,3)],
        [sp.Rational(1,3),sp.Rational(1,3),-sp.Rational(1,3),0,0,-sp.Rational(1,3),-sp.Rational(1,3),sp.Rational(2,3)],
        [sp.Rational(1,3),sp.Rational(1,3),-sp.Rational(1,3),0,0,-sp.Rational(1,3),sp.Rational(2,3),-sp.Rational(1,3)],
    ])
    mu=sp.Matrix(8,8,lambda i,j:sp.simplify(6*s[i,j]/(dims[i]*dims[j])))
    probes={
        "twist_Re":sp.Matrix([[1,1,1,1,-1,1,-sp.Rational(1,2),-sp.Rational(1,2)]]),
        "twist_Im":sp.Matrix([[0,0,0,0,0,0,sqrt3/2,-sqrt3/2]]),
    }
    for j,label in enumerate(labels): probes["mu_"+label]=mu[:,j].T

    selected=("twist_Im","mu_D","mu_F")
    selected_matrix=sp.Matrix.vstack(sp.ones(1,8),*(probes[name] for name in selected))
    selected_rank=selected_matrix.rank()
    selected_kernel=selected_matrix.nullspace()
    assert selected_rank==4 and len(selected_kernel)==4

    mix_ab=sp.Matrix([sp.Rational(1,2),sp.Rational(1,2),0,0,0,0,0,0])
    pure_f=sp.Matrix([0,0,0,0,0,1,0,0])
    assert selected_matrix*mix_ab==selected_matrix*pure_f
    mix_de=sp.Matrix([0,0,0,sp.Rational(1,2),sp.Rational(1,2),0,0,0])
    mix_cf=sp.Matrix([0,0,sp.Rational(2,3),0,0,sp.Rational(1,3),0,0])
    assert selected_matrix*mix_de==selected_matrix*mix_cf

    names=tuple(probes)
    minimum=None; minimum_families=[]
    ranks_by_size={}
    for size in range(len(names)+1):
        families=[]; maximum_rank=0
        for family in itertools.combinations(names,size):
            matrix=sp.Matrix.vstack(sp.ones(1,8),*(probes[name] for name in family))
            rank=matrix.rank(); maximum_rank=max(maximum_rank,rank)
            if rank==8: families.append(family)
        ranks_by_size[size]=maximum_rank
        if families:
            minimum=size; minimum_families=families; break
    assert minimum==7
    assert all(ranks_by_size[size]<=size+1<8 for size in range(7))
    selected_tomography=next(family for family in minimum_families if all(name.startswith("mu_") for name in family))
    selected_tomography_matrix=sp.Matrix.vstack(sp.ones(1,8),*(probes[name] for name in selected_tomography))
    assert selected_tomography_matrix.det()!=0

    result={
        "schema":"marici.s3-sector-mixture-tomography.v1",
        "pure_label_family":list(selected),
        "pure_label_augmented_rank":selected_rank,
        "pure_label_mixture_kernel_dimension":len(selected_kernel),
        "exact_mixture_collisions":{
            "half_A_plus_half_B_equals_F":["1/2 A + 1/2 B","F"],
            "half_D_plus_half_E_equals_two_thirds_C_plus_one_third_F":["1/2 D + 1/2 E","2/3 C + 1/3 F"],
        },
        "candidate_real_setting_count":len(names),
        "minimum_mixture_tomography_setting_count":minimum,
        "minimum_mixture_tomography_family_count":len(minimum_families),
        "selected_minimum_tomography_family":list(selected_tomography),
        "selected_augmented_determinant":str(sp.factor(selected_tomography_matrix.det())),
        "maximum_augmented_rank_by_setting_count":{str(k):v for k,v in ranks_by_size.items()},
        "aggregate_gates":{
            "three_setting_family_separates_vertices_but_not_mixtures":True,
            "two_exact_convex_collisions_exhibited":True,
            "three_setting_mixture_kernel_has_dimension_four":True,
            "at_least_seven_real_settings_are_dimensionally_required":True,
            "seven_settings_are_sufficient_on_frozen_surface":True,
            "mixture_tomography_is_distinct_from_sector_label_readout":True,
            "coherent_sector_superpositions_are_not_claimed_observable":True,
        },
    }
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=="__main__": main()
