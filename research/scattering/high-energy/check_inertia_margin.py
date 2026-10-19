"""H7 block-LDL robustness attempt; floats do not certify interval inequalities."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np
import scipy.linalg as la
from high_energy_scattering_net import ROOT,HOME,digest,validate as historical_validate
from receipt_replay import assert_receipt_matches

CALC=ROOT/'.ai/tmp/scattering-h6-response33/calculation'
RESULT=HOME/'results/inertia-margin.v1.json'
NOTE=HOME/'INERTIA-MARGIN-ATTEMPT.md'


def audit(threshold_total=16.):
    historical_validate();calc=CALC
    if os.name=='nt':calc=Path(chr(92)*2+'?'+chr(92)+str(calc.resolve()))
    sys.path.insert(0,str(calc/'previous'))
    spec=importlib.util.spec_from_file_location('margin_source_tail',calc/'previous/tail_estimator.py')
    te=importlib.util.module_from_spec(spec);spec.loader.exec_module(te)
    engine=Path((calc/'engine_path.txt').read_text())
    M,dyn,it,down,base,efull,Vfull,solve,provenance=te.load_model(engine,'tail420')
    H=it.H;threshold=threshold_total-te.CPOSE;b=it.N*10;n=it.nlam
    assert (n,b,H.shape)==(49,250,(12250,12250))
    Dprev=None;previous_covariance=None;inverse_norm_squared=0.;min_pivot=np.inf
    rows=[];error_squares=0.;negative=0;orthogonality_squares=0.;spectral_error_squares=0.
    for j in range(n):
        ix=slice(j*b,(j+1)*b)
        A=H[ix,ix].toarray()-threshold*np.eye(b)
        if j:
            C=H[ix,slice((j-1)*b,j*b)].toarray()
            # L_j = C D_(j-1)^-1. Use Hermitian solve, but reconstruct
            # the factor product independently from this defining equation.
            L=la.solve(Dprev,C.conj().T,assume_a='her',check_finite=False).conj().T
            D=A-L@Dprev@L.conj().T
            D=(D+D.conj().T)/2
            off_error=C-L@Dprev
            diagonal_error=A-D-L@Dprev@L.conj().T
            covariance=np.eye(b)+L@previous_covariance@L.conj().T
            multiplier_norm=float(la.norm(L,2))
            error_squares+=2*float(la.norm(off_error,'fro')**2)
        else:
            D=(A+A.conj().T)/2;diagonal_error=A-D;covariance=np.eye(b);multiplier_norm=0.
        error_squares+=float(la.norm(diagonal_error,'fro')**2)
        covariance=(covariance+covariance.conj().T)/2
        inverse_norm_squared+=float(np.trace(covariance).real)
        ev,U=la.eigh(D,check_finite=False)
        pivot=float(np.min(abs(ev)));min_pivot=min(min_pivot,pivot)
        negative+=int(np.count_nonzero(ev<0))
        gram=U.conj().T@U-np.eye(b)
        reconstruction=D-(U*ev)@U.conj().T
        orthogonality_squares+=float(la.norm(gram,'fro')**2)
        spectral_error_squares+=float(la.norm(reconstruction,'fro')**2)
        rows.append({'block':j,'negative_pivots':int(np.count_nonzero(ev<0)),
                     'min_abs_pivot':pivot,'multiplier_spectral_norm':multiplier_norm})
        Dprev=D;previous_covariance=covariance
    # Verify raw H has exactly the assumed block-tridiagonal sparsity.
    coo=H.tocoo();assert np.max(abs(coo.row//b-coo.col//b))<=1
    factor_residual=float(np.sqrt(error_squares))
    inverse_frobenius=float(np.sqrt(inverse_norm_squared))
    # All are FLOAT candidates. In a rigorous implementation the D eigenframe
    # defects must first be enclosed; rounded eigvals are not exact pivots.
    separation=float(min_pivot/inverse_norm_squared)
    margin=separation-factor_residual
    assert negative<=420
    if threshold_total==16.:assert negative==420
    paths=[NOTE,Path(__file__),HOME/'receipt_replay.py',CALC/'previous/tail_estimator.py',HOME/'pentachoron_higher_closed_cutoff_bundle.zip',HOME/'pentachoron_full_response128_packet_bundle.zip']
    return {'schema':'marici.scattering.inertia-margin.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'shift_threshold_unshifted':threshold,'shift_threshold_total':threshold_total,
            'band_gap_candidate_float':float(threshold_total-(it.e[0]+3.51+te.CPOSE)),
            'raw_dimension':H.shape[0],
            'negative_count_float':negative,'block_rows':rows,
            'min_abs_D_pivot_float':float(min_pivot),
            'L_inverse_Frobenius_norm_float':inverse_frobenius,
            'factor_residual_Frobenius_norm_float':factor_residual,
            'D_eigenframe_Gram_defect_Frobenius_float':float(np.sqrt(orthogonality_squares)),
            'D_spectral_reconstruction_error_Frobenius_float':float(np.sqrt(spectral_error_squares)),
            'factor_separation_candidate_float':separation,
            'robustness_margin_candidate_float':margin,
            'candidate_margin_positive':bool(margin>0),
            'inertia_certified':False,'source_omitted_gap_certified':False,
            'missing_certification':['outward-rounded factor residual and triangular inverse norm recurrence','certified D-block eigenvalue separation/inertia','certified retained spectral embedding to transfer count into Q420 gap'],
            'H7_disposition':'open; quantitative block-factor conditioning and residual margin measured, not interval certified'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();result=audit()
    if args.check:assert_receipt_matches(json.loads(RESULT.read_text(encoding='utf-8')),result)
    else:RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','negative_count_float','L_inverse_Frobenius_norm_float','factor_residual_Frobenius_norm_float','factor_separation_candidate_float','candidate_margin_positive','H7_disposition')}))


if __name__=='__main__':main()
