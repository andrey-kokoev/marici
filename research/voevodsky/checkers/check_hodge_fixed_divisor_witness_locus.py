"""Full tangent rank and exact-period controls for the written locus theorem."""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import json
from check_hodge_explicit_sixfold_candidate import identity,base_J,inverse,multiply,lie_action
from check_hodge_product_witness_first_order import real_imag_pair
from check_hodge_deligne_lift_image import rank


def chart_matrix(entries,diagonal=True):
    A=identity(12) if diagonal else [[Q(0)]*12 for _ in range(12)]
    for (row,col),(a,b) in entries.items():
        block=[[a,-b],[b,a]];weight=(1,1,3)[row]
        for i in range(2):
            for j in range(2):
                A[6+2*row+i][2*col+j]=block[i][j]
                A[2*col+j][6+2*row+i]=weight*block[i][j]
    return A


def actual_J(entries):
    A=chart_matrix(entries)
    return multiply(multiply(A,base_J()),inverse(A))


def main():
    factors=[v for j in range(3) for v in real_imag_pair(j,j+3)]
    basis=list(combinations(range(12),2));columns=[];off=[]
    for row in range(3):
        for col in range(3):
            for imaginary in (False,True):
                B=chart_matrix({(row,col):(Q(not imaginary),Q(imaginary))},False)
                BJ=multiply(B,base_J());JB=multiply(base_J(),B)
                dot=[[a-b for a,b in zip(r,s)] for r,s in zip(BJ,JB)]
                outputs=[lie_action(dot,f) for f in factors]
                column=[f.get(key,0) for f in outputs for key in basis]
                columns.append(column)
                if row==col:assert not any(column)
                else:off.append(column)
    assert rank(columns)==rank(off)==12 and len(columns)-rank(columns)==6
    diagonal={(0,0):(Q(1,8),Q(1,8)),(1,1):(Q(1,8),Q(-1,16)),(2,2):(Q(1,32),Q(1,16))}
    assert all((1,1,3)[r]*(a*a+b*b)<1 for (r,c),(a,b) in diagonal.items())
    assert all(not lie_action(actual_J(diagonal),f) for f in factors)
    controls=0
    for row in range(3):
        for col in range(3):
            if row==col:continue
            entries=dict(diagonal);entries[row,col]=(Q(1,32),Q(-1,64))
            # Frobenius bound implies I-P*DP>0 even with these mixed entries.
            assert sum((1,1,3)[r]*(a*a+b*b) for (r,c),(a,b) in entries.items())<1
            assert any(lie_action(actual_J(entries),f) for f in factors)
            controls+=1
    result={'passed':True,'classification':'fixed_six_factor_Hodge_locus_is_exactly_diagonal',
        'tangent_domain_real_dimension':18,'tangent_rank':12,'tangent_kernel_real_dimension':6,
        'exact_locus_complex_dimension':3,'mixed_period_controls':controls,
        'exact_locus_proved_by':'decomposable-form stabilizer and positive-plane splitting',
        'all_cycle_realization_locus_computed':False,'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'First-order Hodge derivatives of the actual degree-six summands and their cancellation in R.'}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-fixed-divisor-witness-locus-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
