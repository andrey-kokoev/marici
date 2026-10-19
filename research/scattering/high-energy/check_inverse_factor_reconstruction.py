"""H7 residual-controlled triangular inverse screen; no interval certificate."""
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
from check_inertia_roundoff_screen import gamma,norm_upper_model,product_error_model

CALC=ROOT/'.ai/tmp/scattering-h6-response33/calculation'
NOTE=HOME/'INVERSE-FACTOR-RECONSTRUCTION.md'
RESULT=HOME/'results/inverse-factor-reconstruction.v1.json'
PREVIOUS=HOME/'results/inertia-roundoff-screen.v1.json'


def audit():
    historical_validate();previous=json.loads(PREVIOUS.read_text(encoding='utf-8'))
    for path,value in previous['source_sha256'].items():assert digest(ROOT/path)==value
    calc=CALC
    if os.name=='nt':calc=Path(chr(92)*2+'?'+chr(92)+str(calc.resolve()))
    sys.path.insert(0,str(calc/'previous'))
    spec=importlib.util.spec_from_file_location('inverse_source_tail',calc/'previous/tail_estimator.py')
    te=importlib.util.module_from_spec(spec);spec.loader.exec_module(te)
    engine=Path((calc/'engine_path.txt').read_text())
    M,dyn,it,down,base,efull,Vfull,solve,provenance=te.load_model(engine,'tail420')
    shift=10-te.CPOSE;b=250;n=49;Dprev=None;previous_row=None
    Wnorm2=0.;residual2=0.;rows=[]
    for j in range(n):
        ix=slice(j*b,(j+1)*b);A=it.H[ix,ix].toarray()-shift*np.eye(b)
        if j:
            C=it.H[ix,slice((j-1)*b,j*b)].toarray()
            L=la.solve(Dprev,C.conj().T,assume_a='her',check_finite=False).conj().T
            D=A-L@Dprev@L.conj().T;D=(D+D.conj().T)/2
            row=[];row_error2=0.
            for old in previous_row:
                product=L@old;block=-product
                # Independently reconstruct this block of L W-I. The rounded
                # residual may cancel exactly, so include the product error.
                recomputed=L@old
                residual=block+recomputed
                err=norm_upper_model(residual)+product_error_model(L,old)+gamma(4)*(norm_upper_model(block)+norm_upper_model(recomputed))
                row_error2+=err**2;row.append(block)
            residual2+=row_error2
        else:D=(A+A.conj().T)/2;row=[];row_error2=0.
        row.append(np.eye(b,dtype=complex))
        row_norm2=sum(norm_upper_model(block)**2 for block in row)
        Wnorm2+=row_norm2
        rows.append({'block_row':j,'row_inverse_squared_norm_model':row_norm2,'row_residual_squared_norm_model':row_error2})
        previous_row=row;Dprev=D
    # Scalar accumulation is inflated as a model; this is still not a directed
    # interval implementation. Avoid recursive propagation of covariance error.
    inflation=1+gamma(8*n*n)
    eta=float(np.sqrt(residual2*inflation));wnorm=float(np.sqrt(Wnorm2*inflation))
    assert eta<1
    inverse_upper=wnorm/(1-eta)
    separation=previous['D_pivot_lower_model']/inverse_upper**2
    factor_error=previous['factor_residual_upper_model']
    paths=[NOTE,Path(__file__),HOME/'receipt_replay.py',HOME/'check_inertia_roundoff_screen.py',PREVIOUS,CALC/'previous/tail_estimator.py',HOME/'pentachoron_higher_closed_cutoff_bundle.zip',HOME/'pentachoron_full_response128_packet_bundle.zip']
    return {'schema':'marici.scattering.inverse-factor-reconstruction.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'threshold_total':10.,'inverse_block_rows':rows,
            'W_Frobenius_upper_model':wnorm,'LW_minus_I_Frobenius_upper_model':eta,
            'L_inverse_Frobenius_upper_model':inverse_upper,
            'factor_separation_lower_model':separation,'factor_residual_upper_model':factor_error,
            'factor_robustness_margin_model':separation-factor_error,
            'factor_robustness_margin_model_positive':bool(separation>factor_error),
            'inverse_reconstruction_residual_below_one_model':True,
            'interval_certificate':False,'source_gap_certified':False,
            'missing_certification':['directed/exact arithmetic enclosure of residual and norms','tighter or higher-precision factor reconstruction residual','source reference and retained spectral-frame enclosure'],
            'H7_disposition':'open; inverse-factor reconstruction replaces exploding covariance propagation but full factor margin remains conditional'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();result=audit()
    if args.check:assert_receipt_matches(json.loads(RESULT.read_text(encoding='utf-8')),result)
    else:RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','W_Frobenius_upper_model','LW_minus_I_Frobenius_upper_model','L_inverse_Frobenius_upper_model','factor_separation_lower_model','factor_robustness_margin_model_positive','H7_disposition')}))


if __name__=='__main__':main()
