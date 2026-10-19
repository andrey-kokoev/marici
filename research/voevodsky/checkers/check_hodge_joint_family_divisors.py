"""Exact Picard upper bound plus invariant-basis/product controls for a two-parameter family."""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from pathlib import Path
import json
from check_hodge_fixed_divisor_witness_locus import actual_J
from check_hodge_explicit_sixfold_candidate import BASIS2,lie_action,sparse_rank
from check_hodge_cycle_map_scope import nullspace,rref
from check_hodge_product_witness_first_order import real_imag_pair,add
from check_hodge_fixed_sixfold_pairing import wedge


def rows_for(forms):
    keys=sorted(set().union(*(set(f) for f in forms)))
    return [[Q(f.get(key,0)) for key in keys] for f in forms]


def main():
    samples=[(Q(0),Q(0)),(Q(1,8),Q(0)),(Q(0),Q(1,8)),(Q(1,8),Q(1,8))]
    constraints=[]
    for s,t in samples:
        assert s*s+t*t<1
        J=actual_J({(0,0):(s,0),(0,1):(t,0)})
        columns=[lie_action(J,{key:1}) for key in BASIS2]
        constraints.extend([[c.get(key,0) for c in columns] for key in BASIS2])
    pic_rank,certificate=sparse_rank(constraints,True)
    assert pic_rank==56
    selected=[constraints[i] for i in certificate]
    assert len(rref(selected)[1])==56
    kernel=nullspace(selected)
    assert len(kernel)==10
    Eactive={(0,1):1,(2,3):1,(6,7):-1}
    basis=[Eactive,{(4,5):1},{(8,9):1},{(10,11):1},
           *real_imag_pair(2,4),*real_imag_pair(2,5),
           {(8,10):1,(9,11):1},{(8,11):-1,(9,10):1}]
    kernel_forms=[{key:c for key,c in zip(BASIS2,v) if c} for v in kernel]
    assert sparse_rank(rows_for(basis))==10
    assert sparse_rank(rows_for(basis+kernel_forms))==10
    active={0,1,2,3,6,7}
    assert all(set(key).isdisjoint(active) for f in basis[1:] for key in f)
    for s,t in samples+[(Q(1,7),Q(1,9)),(Q(-1,8),Q(1,5))]:
        J=actual_J({(0,0):(s,0),(0,1):(t,0)})
        assert all(not lie_action(J,f) for f in basis)
    products=[wedge(wedge(basis[i],basis[j]),basis[k])
              for i,j,k in combinations_with_replacement(range(10),3)]
    product_rows=rows_for(products)
    product_rank,product_certificate=sparse_rank(product_rows,True)
    assert product_rank==20
    assert len(rref([product_rows[i] for i in product_certificate])[1])==20
    assert all(sum(i in active for i in key)%2==0 for f in products for key in f)
    r1,s1=real_imag_pair(0,3);r2,s2=real_imag_pair(1,4);r3,s3=real_imag_pair(2,5)
    tri=lambda a,b,c:wedge(wedge(a,b),c)
    K1=add((1,tri(s1,s2,r3)),(-1,tri(r1,r2,r3)))
    K2=add((1,tri(r1,s2,s3)),(1,tri(s1,r2,s3)))
    R=add((1,K1),(1,K2))
    assert all(sum(i in active for i in key)==3 for f in (K1,K2,R) for key in f)
    assert sparse_rank(rows_for([K1,K2]))==2
    assert sparse_rank(rows_for(products+[K1,K2]))==22
    assert sparse_rank(rows_for(products+[R]))==21
    for s,t in samples+[(Q(1,7),Q(1,9))]:
        J=actual_J({(0,0):(s,0),(0,1):(t,0)})
        assert all(not lie_action(J,f) for f in (K1,K2,R))
    result={'passed':True,'classification':'joint_family_divisor_products_miss_preserved_kernel_classes',
        'degree_two_constraint_rank':56,'Picard_rank_at_independent_pair':10,
        'Picard_rank_certificate_rows':certificate,'triple_product_rank':20,
        'product_rank_certificate_rows':product_certificate,'rank_with_K1_K2':22,
        'rank_with_R':21,'exclusion_reason':'even active degree in divisor products versus active degree3 in K1,K2',
        'all_algebraic_cycles_excluded':False,'original_fixed_sixfold_replaced':False,
        'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Identify the odd-degree active/inactive Hodge tensor and its proper correspondence source, rather than search more divisor pairings.'}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-joint-family-divisor-products-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
