"""128-bit Arb factor residual for the exact stored binary matrix, not full H7."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse
import importlib.util
from importlib.metadata import version
import json
from pathlib import Path
import sys
import numpy as np
import scipy.linalg as la
from flint import acb,acb_mat,arb,ctx
from high_energy_scattering_net import ROOT,HOME,digest,validate as historical_validate
from receipt_replay import assert_receipt_matches

CALC=ROOT/'.ai/tmp/scattering-h6-response33/calculation'
NOTE=HOME/'BALL-FACTOR-RESIDUAL.md'
RESULT=HOME/'results/ball-factor-residual.v1.json'
PREVIOUS=HOME/'results/inverse-factor-reconstruction.v1.json'


def balls(A):
    return acb_mat([[acb(complex(x)) for x in row] for row in A])


def norm_squared(A):
    total=arb(0)
    for i in range(A.nrows()):
        for j in range(A.ncols()):
            z=A[i,j];total+=z.real*z.real+z.imag*z.imag
    return total


def audit():
    historical_validate();ctx.prec=128
    # Floating inputs must enter as exact binary dyadics, not decimal strings.
    assert arb(.1).is_exact() and arb(.1)!=arb(1)/10
    previous=json.loads(PREVIOUS.read_text(encoding='utf-8'))
    for path,value in previous['source_sha256'].items():assert digest(ROOT/path)==value
    calc=CALC
    if os.name=='nt':calc=Path(chr(92)*2+'?'+chr(92)+str(calc.resolve()))
    sys.path.insert(0,str(calc/'previous'))
    spec=importlib.util.spec_from_file_location('ball_source_tail',calc/'previous/tail_estimator.py')
    te=importlib.util.module_from_spec(spec);spec.loader.exec_module(te)
    engine=Path((calc/'engine_path.txt').read_text())
    M,dyn,it,down,base,efull,Vfull,solve,provenance=te.load_model(engine,'tail420')
    shift=float(10-te.CPOSE);b=250;n=49
    Dprev=None;Dballprev=None;residual2=arb(0);rows=[]
    for j in range(n):
        ix=slice(j*b,(j+1)*b);Hblock=it.H[ix,ix].toarray();A=Hblock-shift*np.eye(b)
        if j:
            C=it.H[ix,slice((j-1)*b,j*b)].toarray()
            L=la.solve(Dprev,C.conj().T,assume_a='her',check_finite=False).conj().T
            D=A-L@Dprev@L.conj().T;D=(D+D.conj().T)/2
            Lball=balls(L);LD=Lball*Dballprev
            off=balls(C)-LD
            off2=norm_squared(off)
            product=LD*balls(L.conj().T)
        else:
            D=(A+A.conj().T)/2;off2=arb(0);product=acb_mat(b,b)
        # Enclose Hblock - exact(binary shift) I, not rounded NumPy subtraction.
        Aball=balls(Hblock)
        for i in range(b):Aball[i,i]-=arb(shift)
        Dball=balls(D);diag=Aball-Dball-product
        diag2=norm_squared(diag);residual2+=diag2+2*off2
        rows.append({'block':j,'diagonal_squared_norm_ball':str(diag2),'off_diagonal_squared_norm_ball':str(off2)})
        Dprev=D;Dballprev=Dball
        if (j+1)%10==0:print('BALL_BLOCK',j+1,flush=True)
    assert residual2.lower()>=0
    norm=residual2.sqrt()
    # Presentation floats are outward-inflated. The ball string preserves the
    # actual Arb enclosure; comparisons use balls, not rounded JSON values.
    norm_upper=float(np.nextafter(float(norm.upper()),np.inf))
    separation=previous['factor_separation_lower_model']
    below_model=bool(norm.upper()<arb(separation))
    paths=[NOTE,Path(__file__),HOME/'receipt_replay.py',PREVIOUS,CALC/'previous/tail_estimator.py',HOME/'pentachoron_higher_closed_cutoff_bundle.zip',HOME/'pentachoron_full_response128_packet_bundle.zip']
    return {'schema':'marici.scattering.ball-factor-residual.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'python_flint_version':version('python-flint'),'precision_bits':128,
            'reference_matrix':'exact binary entries of regenerated raw H minus exact binary shifted threshold times I',
            'shift_threshold_binary_float':shift,'threshold_total_label':10.,
            'block_residual_balls':rows,'factor_residual_Frobenius_ball':str(norm),
            'factor_residual_Frobenius_upper':norm_upper,
            'factor_residual_enclosed_for_binary_reference':True,
            'residual_below_conditional_separation':below_model,
            'conditional_separation_from_inverse_screen':separation,
            'source_assembly_error_enclosed':False,'inertia_certified':False,'source_gap_certified':False,
            'missing_certification':['verified D-block inertia/separation and inverse-factor bound in place of gamma screens','original source assembly and exact energy-reference enclosure','retained spectral-frame transfer','full-band coupled inverse'],
            'bounded_H7_attempt_outcome':'inconclusive; eight-cycle budget exhausted',
            'H7_disposition':'open; factor residual enclosed for stored binary matrix only'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();result=audit()
    if args.check:assert_receipt_matches(json.loads(RESULT.read_text(encoding='utf-8')),result)
    else:RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','factor_residual_Frobenius_upper','residual_below_conditional_separation','bounded_H7_attempt_outcome','H7_disposition')}))


if __name__=='__main__':main()
