"""Exact central readout algebra and invisible operator kernel for D(S3)."""

import json
import sympy as sp


def main():
    labels=("A","B","C","D","E","F","G","H")
    dims=(1,1,2,3,3,2,2,2); total=sum(dims)
    assert total==16 and sum(d*d for d in dims)==36
    sqrt3=sp.sqrt(3)
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
    sector_values={
        "identity":sp.ones(1,8),
        "twist_Re":sp.Matrix([[1,1,1,1,-1,1,-sp.Rational(1,2),-sp.Rational(1,2)]]),
        "twist_Im":sp.Matrix([[0,0,0,0,0,0,sqrt3/2,-sqrt3/2]]),
    }
    for j,label in enumerate(labels): sector_values["mu_"+label]=mu[:,j].T

    offsets=[]; cursor=0
    for dim in dims:
        offsets.append(cursor); cursor+=dim

    def central_operator(values):
        diagonal=[]
        for value,dim in zip(list(values),dims): diagonal.extend([value]*dim)
        return sp.diag(*diagonal)

    operators={name:central_operator(values) for name,values in sector_values.items()}
    assert all(a*b==b*a for a in operators.values() for b in operators.values())

    tomography_names=("identity","mu_B","mu_C","mu_D","mu_E","mu_F","mu_G","mu_H")
    flattened=sp.Matrix.hstack(*(sp.Matrix(operators[name]).reshape(total*total,1) for name in tomography_names))
    center_rank=flattened.rank()
    assert center_rank==8

    # Explicit invisible Hermitian operators.
    inter_sector=sp.zeros(total)
    inter_sector[offsets[0],offsets[1]]=1
    inter_sector[offsets[1],offsets[0]]=1
    within_c=sp.zeros(total)
    within_c[offsets[2],offsets[2]]=1
    within_c[offsets[2]+1,offsets[2]+1]=-1
    assert all(sp.trace(op*inter_sector)==0 for op in operators.values())
    assert all(sp.trace(op*within_c)==0 for op in operators.values())

    full_hermitian_real_dimension=total*total
    central_visible_dimension=center_rank
    total_invisible_dimension=full_hermitian_real_dimension-central_visible_dimension
    off_block_coherence_dimension=total*total-sum(d*d for d in dims)
    within_block_traceless_dimension=sum(d*d-1 for d in dims)
    assert off_block_coherence_dimension==220
    assert within_block_traceless_dimension==28
    assert total_invisible_dimension==248==off_block_coherence_dimension+within_block_traceless_dimension

    # Sector dephasing preserves every central expectation.
    matrix_symbols=sp.symbols("x0:"+str(total*total))
    arbitrary=sp.Matrix(total,total,matrix_symbols)
    dephased=sp.zeros(total)
    for offset,dim in zip(offsets,dims):
        dephased[offset:offset+dim,offset:offset+dim]=arbitrary[offset:offset+dim,offset:offset+dim]
    assert all(sp.simplify(sp.trace(op*arbitrary)-sp.trace(op*dephased))==0 for op in operators.values())

    result={
        "schema":"marici.s3-central-readout-algebra.v1",
        "ambient_direct_sum_dimension":total,
        "simple_block_dimensions":dict(zip(labels,dims)),
        "full_block_diagonal_algebra_dimension":sum(d*d for d in dims),
        "central_readout_algebra_dimension":central_visible_dimension,
        "full_hermitian_real_dimension":full_hermitian_real_dimension,
        "invisible_real_operator_dimension":total_invisible_dimension,
        "invisible_dimension_split":{
            "inter_sector_coherences":off_block_coherence_dimension,
            "within_sector_traceless_operators":within_block_traceless_dimension,
        },
        "selected_center_basis":list(tomography_names),
        "explicit_invisible_witnesses":["A_B_Hermitian_coherence","traceless_diagonal_inside_C"],
        "sector_dephasing_preserves_all_central_probe_expectations":True,
        "aggregate_gates":{
            "twist_and_normalized_monodromy_probes_commute":True,
            "seven_probe_tomography_plus_normalization_spans_full_center":True,
            "central_readout_recovers_sector_weights_only":True,
            "inter_sector_coherences_are_invisible":True,
            "within_sector_traceless_states_are_invisible":True,
            "invisible_dimension_is_248":True,
            "superselection_admissibility_is_separate_from_ambient_kernel":True,
        },
    }
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=="__main__": main()
