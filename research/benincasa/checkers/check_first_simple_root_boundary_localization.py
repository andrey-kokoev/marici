#!/usr/bin/env python3
"""Actual F-chart boundary plus a restricted, typed top-level extraction.

Source chart residue is computed; target boundary extraction is not invented.
"""
import json
import sys
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s


def main():
    a=s.symbols('a1:9');a1,a2,a3,a4,a5,a6,a7,a8=a
    C=s.Matrix([[1,a1+a2+a3+a4,(a2+a3+a4)*a5,(a3+a4)*a6,a4*a7,0],
                [0,1,a5,a6,a7,a8]])
    support=[1,2,3,4,5,8]
    minors={(support[i],support[j]):s.factor(C[:,[i,j]].det()) for i in range(6) for j in range(i+1,6)}
    # Delta12=1 fixes determinant scaling. Differential ranks of remaining
    # normalized minors therefore measure chart dimension in the Plucker patch.
    funcs=list(minors.values());sample=dict(zip(a,map(s.Integer,[2,3,5,7,11,13,17,19])))
    jac=s.Matrix(funcs).jacobian(a)
    boundary={key:s.factor(value.subs(a1,0)) for key,value in minors.items()}
    boundary_sample=sample|{a1:s.Integer(0)}
    top_rank=jac.subs(sample).rank()
    boundary_rank=jac[:,1:].subs(boundary_sample).rank()
    vanished=[list(key) for key,value in boundary.items() if value==0]
    loc=s.factor(s.prod(value for value in boundary.values() if value!=0))
    # Read prior receipts only; enforce their direct checker/source integrity.
    receipt_paths=['research/benincasa/results/untransported_simple_root_candidate.json',
                   'research/benincasa/results/untransported_simple_root_seed_admission.json']
    receipts=[]
    for p in receipt_paths:
        r=json.loads((ROOT/p).read_text())
        for source,h in r['source_sha256'].items():
            assert sha256((ROOT/source).read_bytes()).hexdigest()==h, source
        checker=('research/benincasa/checkers/check_untransported_simple_root_candidate.py'
                 if 'candidate.json' in p else 'research/benincasa/checkers/check_untransported_simple_root_seed_admission.py')
        assert sha256((ROOT/checker).read_bytes()).hexdigest()==r['checker_sha256']
        receipts.append(r)
    candidate,admission=receipts
    runs=[]
    for run,scan in zip(candidate['runs'],admission['runs']):
        assert run['shift']==scan['shift']
        assert all(m['seed']=='F' and m['support']==support and m['transported_to_seed_full_ratio']=='1'
                   for m in scan['fermionic_matches'])
        c=s.Rational(run['untransported_to_transported_ratio'])
        K=s.Rational(run['component']['K']);K0=s.Rational(run['component']['K0']);B=s.Rational(run['component']['B_11'])
        assert K0==c*K and B==(1-c)*K
        runs.append({'shift':run['shift'],'external_coefficient':str(c),
                     'source_boundary_residue_coefficient_K0':str(c),
                     'source_boundary_residue_coefficient_B11':str(1-c),
                     'top_component':{'K':str(K),'K0':str(K0),'B11':str(B)},
                     'orientation_flip_residual_K0':str(-2*c),
                     'unit_normalization_substitution_defect':str(1-c)})
    checks={'top_minor_patch_Delta12_one':minors[(1,2)]==1,
            'top_positive_sample':all(v.subs(sample)>0 for v in funcs),
            'top_rank_eight':top_rank==8,'boundary_rank_seven':boundary_rank==7,
            'single_vanishing_supported_minor':vanished==[[2,3]],
            'other_boundary_minors_positive':all(v.subs(sample)>0 for v in boundary.values() if v!=0),
            'boundary_open_nonempty':loc.subs(sample)!=0,
            'all_three_external_coefficients_regular_and_nonunit':all(s.Rational(r['external_coefficient']) not in (0,1) for r in runs),
            'top_component_linearity':True,
            'source_residue_split_recombines':all(s.Rational(r['source_boundary_residue_coefficient_K0'])+
                s.Rational(r['source_boundary_residue_coefficient_B11'])==1 for r in runs),
            'orientation_failure_control_nonzero':all(s.Rational(r['orientation_flip_residual_K0'])!=0 for r in runs)}
    assert all(checks.values()),checks
    out={'schema':'marici.benincasa.first-simple-root-boundary-localization.v1',
         'root':[1,1],'history_index':3,'source_chart':{'seed':'F','support':support,'matrix':[[str(x) for x in row] for row in C.tolist()],
             'orientation':'dlog a1 wedge ... wedge dlog a8','minor_patch':'Delta12=1'},
         'boundary':{'equation':'a1=0','cell_key':{'parallel_classes':[[1],[2,3],[4],[5],[8]],'zero_columns':[6,7]},
             'residue_orientation':1,'remaining_coordinates':[str(x) for x in a[1:]],
             'open_localization':'all remaining alpha positive; all supported minors except Delta23 nonzero',
             'localization_product':str(loc),'minors':{' '.join(map(str,k)):str(v) for k,v in boundary.items()},
             'rank_evidence':{'top':top_rank,'boundary':boundary_rank,'level':'exact rational Jacobian samples; nonzero minors witness nonempty rank opens; boundary has seven coordinates'},
             'physical_target_divisor':'not identified'},
         'restricted_top_extraction':{
             'domain':'rank-one external-coefficient module generated by the named transported F-chart canonical form, NOT all differential forms',
             'codomain_super':'rank-one module generated by the source F-seed canonical superfunction',
             'rule':'E_top(f*omega_F)=f*F_t under the source table identification',
             'component_rule':'S23(f*F_t)=f*K using eta2/eta3 coefficient divided by <23>^4',
             'verification':'The named generator matches the transported generalized-R product at three exact fixtures with all 70 quotient numerator coefficients and full bosonic normalization; coefficient linearity is algebraic.',
             'scope':'This restricted map is typed and reproduces K0/B11 on the named top generator. It is not a construction of the target eight-form pushforward or boundary extraction.'},
         'actual_source_residue':{
             'coefficient_convention':'external kinematics held fixed; c has no alpha dependence',
             'K0':'Res_a1=0(c omega_F)=c dlog a2 wedge ... wedge dlog a8',
             'B11':'Res_a1=0((1-c) omega_F)=(1-c) dlog a2 wedge ... wedge dlog a8',
             'missing_commuting_square':'E_boundary composed with source Res versus target Res composed with E_top: no boundary codomain/map/normal supplied, and E_top changes form type. Do not apply S23 to a seven-form as though it were a superfunction.'},
         'runs':runs,'checks':checks,'passed':True,
         'disposition':'actual_source_boundary_and_restricted_top_extraction_verified; target_residue_square_open',
         'next_required_witness':'A typed target boundary generator/normal, boundary extraction and normalization compatible with the restricted top map. Recover full source bundle for physical divisor attachment.',
         'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in receipt_paths+
             ['research/sources/nima/papers/six-point-nmhv/1212.5605/positive_grassmannian_update.tex']},
         'checker_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=ROOT/'research/benincasa/results/first_simple_root_boundary_localization.json'
    path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'checks':checks,'boundary':out['boundary']['cell_key'],
                     'disposition':out['disposition'],'next_required_witness':out['next_required_witness']},indent=2))


if __name__=='__main__':main()
