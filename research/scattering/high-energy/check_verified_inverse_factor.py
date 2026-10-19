"""VF1 verified residual-controlled inverse of a leading/full binary L factor."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse
import json
from pathlib import Path
import time
import numpy as np
from flint import arb,acb,acb_mat,ctx
from high_energy_scattering_net import ROOT,HOME,digest
from receipt_replay import assert_receipt_matches

WITNESS=HOME/'results/verified-factor-witness.v1.npz'
DRECEIPT=HOME/'results/verified-d-blocks.v1.json'
NOTE=HOME/'VERIFIED-INVERSE-FACTOR.md'
RESULT=HOME/'results/verified-inverse-factor.v1.json'
FRONTIER=HOME/'results/verified-inverse-frontier.v1.npz'


def balls(A):return acb_mat([[acb(complex(x)) for x in row] for row in A])


def squared_norm(A):
    # C-level dot product rather than a Python loop of ball multiplications.
    flat=[A[i,j] for i in range(A.nrows()) for j in range(A.ncols())]
    row=acb_mat([flat]);column=acb_mat([[v.conjugate()] for v in flat])
    return (row*column)[0,0].real


def outward_upper(x):return float(np.nextafter(float(x.upper()),np.inf))
def outward_lower(x):return float(np.nextafter(float(x.lower()),-np.inf))


def audit(row_limit=49,seconds=240):
    ctx.prec=128;start=time.monotonic()
    dreceipt=json.loads(DRECEIPT.read_text(encoding='utf-8'))
    for path,value in dreceipt['source_sha256'].items():assert digest(ROOT/path)==value
    with np.load(WITNESS,allow_pickle=False) as saved:L=saved['L_subdiagonal']
    assert L.shape==(49,250,250) and 1<=row_limit<=49
    b=250;previous=None;previous_balls=None;W2=arb(0);residual2=arb(0);rows=[]
    for j in range(row_limit):
        if j and time.monotonic()-start>seconds:break
        current=[];current_balls=[];row_W2=arb(0);row_R2=arb(0)
        if j:
            Lball=balls(L[j])
            for k in range(j):
                # Float W is only an approximate witness. Its true binary
                # product residual is independently enclosed by Arb.
                block=-(L[j]@previous[k]);block_ball=balls(block)
                residual=block_ball+Lball*previous_balls[k]
                row_R2+=squared_norm(residual)
                row_W2+=squared_norm(block_ball)
                current.append(block);current_balls.append(block_ball)
                previous[k]=None;previous_balls[k]=None
        current.append(np.eye(b,dtype=complex));current_balls.append(acb_mat(np.eye(b).tolist()))
        row_W2+=b;W2+=row_W2;residual2+=row_R2
        rows.append({'block_row':j,'inverse_squared_Frobenius_upper':outward_upper(row_W2),
                     'residual_squared_Frobenius_upper':outward_upper(row_R2)})
        previous=current;previous_balls=current_balls
        if (j+1)%5==0:print('VERIFIED_INVERSE_ROW',j+1,flush=True)
    coverage=len(rows)
    # Upper endpoints are exact points returned by Arb; norm bounds only need
    # the upper endpoint, avoiding a sqrt of a zero-containing interval.
    eta=residual2.upper().sqrt();wnorm=W2.upper().sqrt()
    assert eta.upper()<1,'inverse residual not certified below one'
    inverse_upper=wnorm.upper()/(1-eta.upper())
    separation=arb(dreceipt['minimum_D_separation_lower'])/(inverse_upper.upper()**2)
    complete=coverage==49
    frontier={'last_inverse_row':np.array(previous),'rows_covered':np.array(coverage),
              'W_squared_upper':np.array(outward_upper(W2)),
              'residual_squared_upper':np.array(outward_upper(residual2))}
    if FRONTIER.exists():
        with np.load(FRONTIER,allow_pickle=False) as old:
            for key,value in frontier.items():assert np.array_equal(old[key],value),'frontier drift: '+key
    else:np.savez_compressed(FRONTIER,**frontier)
    paths=[FRONTIER,NOTE,Path(__file__),HOME/'receipt_replay.py',DRECEIPT,WITNESS,HOME/'H7-VERIFIED-FACTOR-SUCCESSOR.md']
    return {'schema':'marici.scattering.verified-inverse-factor.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'precision_bits':128,'block_rows_covered':coverage,'total_block_rows':49,
            'row_results':rows,'W_Frobenius_upper':outward_upper(wnorm),
            'W_squared_upper_for_resume':outward_upper(W2),
            'residual_squared_upper_for_resume':outward_upper(residual2),
            'LW_minus_I_Frobenius_upper':outward_upper(eta),
            'L_inverse_operator_norm_upper':outward_upper(inverse_upper),
            'LDLstar_separation_lower':outward_lower(separation),
            'leading_factor_inverse_certified':True,'full_binary_factor_inverse_certified':complete,
            'reference':'exact binary leading L factor in durable witness; exact binary approximate W with ball residual',
            'original_source_gap_certified':False,'full_band_coupled_inverse_certified':False,
            'factor_residual_linked_to_this_witness':False,
            'VF1_execution_cycles_spent':2,'VF1_execution_cycles_remaining':1,
            'unmet_gates':([] if complete else ['remaining inverse-factor rows'])+['factor-residual witness linkage','original source assembly/energy reference','spectral-frame transfer','full-band coupled matching inverse'],
            'H7_disposition':'open; inverse bound certified only for explicitly covered binary factor, source and coupled inverse still missing'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');p.add_argument('--rows',type=int,default=49);args=p.parse_args()
    if args.check:
        saved=json.loads(RESULT.read_text(encoding='utf-8'))
        # Replay exactly the saved coverage, not timing-dependent coverage.
        result=audit(saved['block_rows_covered'],seconds=270)
        assert_receipt_matches(saved,result)
    else:
        result=audit(args.rows,seconds=270 if args.rows<49 else 240);RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','block_rows_covered','LW_minus_I_Frobenius_upper','L_inverse_operator_norm_upper','LDLstar_separation_lower','full_binary_factor_inverse_certified','H7_disposition')}))


if __name__=='__main__':main()
