"""C8: exact absent-target-eigenvalue obstruction for the fixed macro controller."""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
from check_raw_macro_readout import audit as macro_audit
from check_low_energy_net_v4 import ROOT, BASE, identity, multiply, tensor, determinant, characteristic

PROOF=BASE/'MACRO-CARRIER-OBSTRUCTION.md'
RESULT=BASE/'results/macro-carrier.v1.json'


def audit():
    macro=macro_audit();D=[[Q(x) for x in row] for row in macro['D']]
    I=identity(12)
    F=[[Q(0)]*12+D[i] for i in range(12)]+[I[i]+[Q(0)]*12 for i in range(12)]
    expected=[D[i]+[Q(0)]*12 for i in range(12)]+[[Q(0)]*12+D[i] for i in range(12)]
    assert multiply(F,F)==expected
    defect=[[D[i][j]-I[i][j] for j in range(12)] for i in range(12)]
    det=determinant(defect);assert det==9
    T=[[Q(-1,2),Q(1,2)],[Q(-3,2),Q(-1,2)]];G=[[Q(3),Q(0)],[Q(0),Q(1)]]
    U=tensor(T,T);H=tensor(G,G);v=[[Q(1)],[Q(0)],[Q(0)],[Q(3)]]
    assert multiply(U,v)==v
    norm=sum(v[i][0]*H[i][j]*v[j][0] for i in range(4) for j in range(4));assert norm==18
    # Independent characteristic evaluation at 1 cross-checks det(I-D)=det(D-I).
    coefficients=characteristic(D);assert sum(coefficients)==det
    sources=set(macro['source_sha256'])|{PROOF.relative_to(ROOT).as_posix(),Path(__file__).relative_to(ROOT).as_posix(),'research/scattering/low-energy/check_low_energy_net_v4.py'}
    return {'schema':'marici.scattering.macro-carrier.v1','status':'pass','C8_disposition':'refuted',
            'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(sources)},
            'macro_D':macro['D'],'primitive_clock_dimension':24,'phase_zero_return_verified':'F² phase-zero block = D',
            'det_D_minus_identity':str(det),'characteristic_coefficients_descending':list(map(str,coefficients)),
            'target_U':[[str(x) for x in row] for row in U],
            'target_invariant_vector':[str(x[0]) for x in v],'target_metric_norm_squared':str(norm),
            'deduction':'DJ=JU and Uv=v force Jv=0 because D-I is invertible, contradicting ||Jv||²=v*Hv=18.',
            'reducing_condition_needed_for_obstruction':False,'uses_C10_truth_as_premise':False,
            'all_possible_source_constructors_refuted':False,'physical_outcome':None}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    text=json.dumps(audit(),indent=2)+'\n'
    if args.check:assert RESULT.read_text(encoding='utf-8')==text,'stale C8 certificate'
    else:RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(text,encoding='utf-8')
    print('PASS: C8 refuted exactly: det(D-I)=9; target invariant vector has squared metric norm 18.')


if __name__=='__main__':main()
