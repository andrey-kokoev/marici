"""VF1 final cycle: resume inverse frontier and verify linked binary H inertia."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np
from flint import arb,acb_mat,ctx
from high_energy_scattering_net import ROOT,HOME,digest,validate as historical_validate
from receipt_replay import assert_receipt_matches
from check_verified_inverse_factor import balls,squared_norm,outward_upper,outward_lower

CALC=ROOT/'.ai/tmp/scattering-h6-response33/calculation'
WITNESS=HOME/'results/verified-factor-witness.v1.npz'
FRONTIER=HOME/'results/verified-inverse-frontier.v1.npz'
PREFIX=HOME/'results/verified-inverse-factor.v1.json'
DRECEIPT=HOME/'results/verified-d-blocks.v1.json'
NOTE=HOME/'VERIFIED-BINARY-INERTIA.md'
RESULT=HOME/'results/verified-binary-inertia.v1.json'


def audit():
    historical_validate();ctx.prec=128;start=time.monotonic()
    prefix=json.loads(PREFIX.read_text(encoding='utf-8'));dcert=json.loads(DRECEIPT.read_text(encoding='utf-8'))
    for receipt in (prefix,dcert):
        for path,value in receipt['source_sha256'].items():assert digest(ROOT/path)==value
    with np.load(WITNESS,allow_pickle=False) as z:L=z['L_subdiagonal'];D=z['D'];shift=float(z['binary_shift'])
    with np.load(FRONTIER,allow_pickle=False) as z:
        previous=list(z['last_inverse_row']);covered=int(z['rows_covered'])
        W2=arb(float(z['W_squared_upper']));R2=arb(float(z['residual_squared_upper']))
    assert covered==prefix['block_rows_covered']==41
    assert float(W2)==prefix['W_squared_upper_for_resume'] and float(R2)==prefix['residual_squared_upper_for_resume']
    previous_balls=[balls(v) for v in previous];b=250;rows=[]
    for j in range(covered,49):
        assert time.monotonic()-start<265,'bounded continuation ran out of time'
        current=[];current_balls=[];rw=arb(0);rr=arb(0);Lb=balls(L[j])
        for k in range(j):
            block=-(L[j]@previous[k]);wb=balls(block)
            rr+=squared_norm(wb+Lb*previous_balls[k]);rw+=squared_norm(wb)
            current.append(block);current_balls.append(wb);previous[k]=None;previous_balls[k]=None
        current.append(np.eye(b,dtype=complex));current_balls.append(acb_mat(np.eye(b).tolist()))
        rw+=b;W2+=rw;R2+=rr;previous=current;previous_balls=current_balls
        rows.append({'block_row':j,'inverse_squared_Frobenius_upper':outward_upper(rw),'residual_squared_Frobenius_upper':outward_upper(rr)})
        print('RESUMED_INVERSE_ROW',j+1,flush=True)
    previous=None;previous_balls=None;current=None;current_balls=None
    eta=R2.upper().sqrt();wnorm=W2.upper().sqrt();assert eta.upper()<1
    inverse_bound=wnorm.upper()/(1-eta.upper())
    separation=arb(dcert['minimum_D_separation_lower'])/(inverse_bound.upper()**2)
    calc=CALC
    if os.name=='nt':calc=Path(chr(92)*2+'?'+chr(92)+str(calc.resolve()))
    sys.path.insert(0,str(calc/'previous'))
    spec=importlib.util.spec_from_file_location('linked_inertia_source',calc/'previous/tail_estimator.py')
    te=importlib.util.module_from_spec(spec);spec.loader.exec_module(te)
    engine=Path((calc/'engine_path.txt').read_text())
    M,dyn,it,down,base,efull,Vfull,solve,provenance=te.load_model(engine,'tail420')
    H=it.H;assert (H-H.conj().T).nnz==0,'reference not exactly binary Hermitian'
    coo=H.tocoo();assert np.max(abs(coo.row//b-coo.col//b))<=1
    residual2=arb(0);factor_rows=[];Dprevious=None
    for j in range(49):
        assert time.monotonic()-start<280,'factor linkage exceeded bounded pilot'
        ix=slice(j*b,(j+1)*b);Ab=balls(H[ix,ix].toarray())
        for i in range(b):Ab[i,i]-=arb(shift)
        Db=balls(D[j])
        if j:
            Lb=balls(L[j]);LD=Lb*Dprevious
            off=balls(H[ix,slice((j-1)*b,j*b)].toarray())-LD
            off2=squared_norm(off);diagonal=Ab-Db-LD*Lb.conjugate().transpose()
        else:off2=arb(0);diagonal=Ab-Db
        diag2=squared_norm(diagonal);residual2+=diag2+2*off2;Dprevious=Db
        factor_rows.append({'block':j,'diagonal_squared_norm_upper':outward_upper(diag2),'off_diagonal_squared_norm_upper':outward_upper(off2)})
    factor_residual=residual2.upper().sqrt()
    margin=separation-factor_residual.upper()
    assert margin.lower()>0,'linked inertia perturbation margin not positive'
    negative=dcert['negative_inertia_sum'];assert negative==130
    paths=[NOTE,Path(__file__),HOME/'receipt_replay.py',HOME/'check_verified_inverse_factor.py',PREFIX,DRECEIPT,WITNESS,FRONTIER,CALC/'previous/tail_estimator.py',HOME/'pentachoron_higher_closed_cutoff_bundle.zip',HOME/'pentachoron_full_response128_packet_bundle.zip']
    return {'schema':'marici.scattering.verified-binary-inertia.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'precision_bits':128,'prefix_rows_reused':41,'new_rows_verified':8,'total_rows_verified':49,
            'continuation_rows':rows,'factor_linkage_rows':factor_rows,
            'LW_minus_I_Frobenius_upper':outward_upper(eta),
            'L_inverse_operator_norm_upper':outward_upper(inverse_bound),
            'LDLstar_separation_lower':outward_lower(separation),
            'linked_factor_residual_Frobenius_upper':outward_upper(factor_residual),
            'verified_inertia_perturbation_margin_lower':outward_lower(margin),
            'binary_shifted_H_inertia_certified':True,'negative_inertia':negative,
            'positive_inertia':12250-negative,'zero_inertia':0,
            'binary_shift':shift,'reference':'exact regenerated binary Hermitian H minus exact binary shift I; linked durable L/D witness',
            'original_source_assembly_enclosed':False,'exact_energy_reference_enclosed':False,
            'retained_spectral_frame_certified':False,'full_band_coupled_inverse_certified':False,
            'VF1_execution_cycles_spent':3,'VF1_execution_cycles_remaining':0,
            'VF1_outcome':'inconclusive for full H7; verified binary native inertia subgate completed',
            'H7_disposition':'open; full binary shifted native inertia certified, original source/frame and coupled inverse still missing'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();result=audit()
    if args.check:assert_receipt_matches(json.loads(RESULT.read_text(encoding='utf-8')),result)
    else:RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','negative_inertia','L_inverse_operator_norm_upper','linked_factor_residual_Frobenius_upper','verified_inertia_perturbation_margin_lower','VF1_outcome','H7_disposition')}))


if __name__=='__main__':main()
