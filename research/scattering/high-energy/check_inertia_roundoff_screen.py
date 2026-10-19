"""Conditional binary64 error-budget screen; not a runtime interval certificate."""
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
NOTE=HOME/'INERTIA-ROUNDOFF-SCREEN.md'
RESULT=HOME/'results/inertia-roundoff-screen.v1.json'
UNIT=2.**-53


def gamma(k):
    assert k*UNIT<1
    return k*UNIT/(1-k*UNIT)


def norm_upper_model(A):
    # Conditional standard arithmetic model. Inflate a computed norm rather
    # than pretending numpy/BLAS supplies an interval API.
    return float(np.nextafter(la.norm(A,'fro')*(1+gamma(8*A.size+16)),np.inf))


def product_error_model(A,B):
    return gamma(8*A.shape[1]+16)*norm_upper_model(A)*norm_upper_model(B)


def audit():
    historical_validate();calc=CALC
    if os.name=='nt':calc=Path(chr(92)*2+'?'+chr(92)+str(calc.resolve()))
    sys.path.insert(0,str(calc/'previous'))
    spec=importlib.util.spec_from_file_location('roundoff_source_tail',calc/'previous/tail_estimator.py')
    te=importlib.util.module_from_spec(spec);spec.loader.exec_module(te)
    engine=Path((calc/'engine_path.txt').read_text())
    M,dyn,it,down,base,efull,Vfull,solve,provenance=te.load_model(engine,'tail420')
    threshold=10-te.CPOSE;b=250;n=49
    Dprev=None;Rprev=None;recurrence_error=0.;inverse_square_upper=0.
    residual_square_upper=0.;pivot_lower=np.inf;negative=0;rows=[]
    for j in range(n):
        ix=slice(j*b,(j+1)*b)
        Hblock=it.H[ix,ix].toarray();A=Hblock-threshold*np.eye(b)
        subtraction_error=gamma(4)*(norm_upper_model(Hblock)+abs(threshold)*np.sqrt(b))
        if j:
            C=it.H[ix,slice((j-1)*b,j*b)].toarray()
            L=la.solve(Dprev,C.conj().T,assume_a='her',check_finite=False).conj().T
            LD=L@Dprev;LDL=LD@L.conj().T
            D=(A-LDL);D=(D+D.conj().T)/2
            off=C-LD
            off_bound=norm_upper_model(off)+product_error_model(L,Dprev)+gamma(4)*(norm_upper_model(C)+norm_upper_model(LD))
            diag=A-D-LDL
            diag_bound=norm_upper_model(diag)+subtraction_error+product_error_model(LD,L.conj().T)+product_error_model(L,Dprev)*norm_upper_model(L)+gamma(8)*(norm_upper_model(A)+norm_upper_model(D)+norm_upper_model(LDL))
            residual_square_upper+=2*off_bound**2
            LR=L@Rprev;LRL=LR@L.conj().T;R=np.eye(b)+LRL;R=(R+R.conj().T)/2
            # In the error propagation term Frobenius dominates spectral norm.
            ln=norm_upper_model(L)
            local_error=product_error_model(LR,L.conj().T)+product_error_model(L,Rprev)*ln+gamma(8)*(np.sqrt(b)+norm_upper_model(LRL))
            recurrence_error=ln**2*recurrence_error+local_error
        else:
            D=(A+A.conj().T)/2;R=np.eye(b)
            diag_bound=norm_upper_model(A-D)+subtraction_error;recurrence_error=0.
        residual_square_upper+=diag_bound**2
        # trace error <= sqrt(b) times matrix Frobenius error.
        trace_float=float(np.trace(R).real)
        trace_upper=trace_float+np.sqrt(b)*recurrence_error+gamma(4*b)*norm_upper_model(R)*np.sqrt(b)
        inverse_square_upper+=trace_upper
        ev,U=la.eigh(D,check_finite=False);negative+=int(np.count_nonzero(ev<0))
        gram=U.conj().T@U-np.eye(b)
        gram_bound=norm_upper_model(gram)+product_error_model(U.conj().T,U)+gamma(4)*(norm_upper_model(U.conj().T@U)+np.sqrt(b))
        UD=U*ev;reconstruction=D-UD@U.conj().T
        spectral_error=norm_upper_model(reconstruction)+product_error_model(UD,U.conj().T)+gamma(8)*(norm_upper_model(D)+norm_upper_model(UD)*norm_upper_model(U))
        # Singular value of U diag(ev) U* >= (1-||U*U-I||) min|ev|.
        candidate=(1-gram_bound)*float(np.min(abs(ev)))-spectral_error
        pivot_lower=min(pivot_lower,candidate)
        rows.append({'block':j,'D_pivot_lower_model':candidate,'inverse_recurrence_error_model':recurrence_error,'trace_upper_model':trace_upper,'diagonal_residual_upper_model':diag_bound})
        Dprev=D;Rprev=R
    residual_upper=float(np.sqrt(residual_square_upper))
    separation=float(pivot_lower/inverse_square_upper)
    assert negative==130 and pivot_lower>0
    paths=[NOTE,Path(__file__),HOME/'receipt_replay.py',CALC/'previous/tail_estimator.py',HOME/'pentachoron_higher_closed_cutoff_bundle.zip',HOME/'pentachoron_full_response128_packet_bundle.zip']
    return {'schema':'marici.scattering.inertia-roundoff-screen.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'threshold_total':10.,'unit_roundoff':UNIT,'negative_count_float':negative,
            'roundoff_model':'conditional gamma(8k+16) complex matrix products; Frobenius norm propagation',
            'rows':rows,'D_pivot_lower_model':float(pivot_lower),
            'inverse_Frobenius_squared_upper_model':inverse_square_upper,
            'factor_residual_upper_model':residual_upper,'factor_separation_lower_model':separation,
            'roundoff_margin_model':separation-residual_upper,
            'roundoff_margin_model_positive':bool(separation>residual_upper),
            'runtime_arithmetic_contract_verified':False,'interval_certificate':False,'source_gap_certified':False,
            'unmet_premises':['verified directed or exact enclosure arithmetic including scalar accumulation','source assembly and spectral-reference enclosure','certified retained spectral embedding'],
            'H7_disposition':'open; conservative standard-roundoff propagation screened, not interval certified'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();result=audit()
    if args.check:assert_receipt_matches(json.loads(RESULT.read_text(encoding='utf-8')),result)
    else:RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','D_pivot_lower_model','inverse_Frobenius_squared_upper_model','factor_residual_upper_model','factor_separation_lower_model','roundoff_margin_model_positive','H7_disposition')}))


if __name__=='__main__':main()
