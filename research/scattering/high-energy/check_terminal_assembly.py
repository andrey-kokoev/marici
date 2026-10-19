"""AB1 cycle 1: exact terminal assembly from frozen binary native samples."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np
from flint import arb,acb,acb_mat,ctx
from high_energy_scattering_net import ROOT,HOME,digest,validate as historical_validate
from receipt_replay import assert_receipt_matches
from check_verified_inverse_factor import balls,squared_norm,outward_upper,outward_lower

CALC=ROOT/'.ai/tmp/scattering-h6-response33/calculation'
SOURCE=CALC/'cache/source_work/engine/source_packet/source/source/quantum_strain_route.py'
REFERENCE=HOME/'results/exact-pose-reference.v1.json'
SAMPLES=HOME/'results/native-samples.v1.npz'
NOTE=HOME/'H7-ASSEMBLY-BRIDGE.md'
RESULT=HOME/'results/terminal-assembly.v1.json'


def audit():
    historical_validate();ctx.prec=128
    reference=json.loads(REFERENCE.read_text(encoding='utf-8'))
    for path,value in reference['source_sha256'].items():assert digest(ROOT/path)==value
    code=SOURCE.read_text(encoding='utf-8')
    assert 'return A_LAM*(2-lam**2)/(4*(1+lam**2)**2)' in code
    calc=CALC
    if os.name=='nt':calc=Path(chr(92)*2+'?'+chr(92)+str(calc.resolve()))
    sys.path.insert(0,str(calc/'previous'))
    spec=importlib.util.spec_from_file_location('terminal_assembly_source',calc/'previous/tail_estimator.py')
    te=importlib.util.module_from_spec(spec);spec.loader.exec_module(te)
    engine=Path((calc/'engine_path.txt').read_text())
    M,dyn,it,down,base,efull,Vfull,solve,provenance=te.load_model(engine,'tail420')
    samples=np.array(it.L);assert samples.shape==(49,25,10,10)
    if SAMPLES.exists():
        with np.load(SAMPLES,allow_pickle=False) as z:assert np.array_equal(z['native_samples'],samples),'native sample drift'
    else:np.savez_compressed(SAMPLES,native_samples=samples)
    H=it.H;assert (H-H.conj().T).nnz==0
    a=arb(5)/16;dl=arb(6)/125;strain=a/(dl*dl);b=250;rows=[];error2=arb(0)
    ns=it.ns;phases=[[acb(0,-2*arb.pi()*q*l/25).exp()/25 for l in range(25)] for q in range(25)]
    identity=acb_mat(np.eye(b).tolist())
    for j in range(49):
        sample_balls=[balls(v) for v in samples[j]]
        coefficients=[]
        for q in range(25):
            coeff=acb_mat(10,10)
            for l in range(25):coeff+=sample_balls[l]*phases[q][l]
            coefficients.append(coeff)
        target=acb_mat(b,b)
        for n in range(25):
            for m in range(25):
                coeff=coefficients[int((ns[n]-ns[m])%25)]
                for p in range(10):
                    for r in range(10):target[10*n+p,10*m+r]=coeff[p,r]
        target=(target+target.conjugate().transpose())/2
        lam=arb(6*(j+1))/125
        scalar=8*(lam-1)**2+a*(2-lam*lam)/(4*(1+lam*lam)**2)
        for n in range(25):
            value=a*int(ns[n])**2/(1+lam*lam)+scalar+2*strain
            for p in range(10):target[10*n+p,10*n+p]+=value
        ix=slice(j*b,(j+1)*b)
        diagonal_error=squared_norm(balls(H[ix,ix].toarray())-target)
        if j:
            off_error=squared_norm(balls(H[ix,slice((j-1)*b,j*b)].toarray())+identity*strain)
        else:off_error=arb(0)
        error2+=diagonal_error+2*off_error
        rows.append({'block':j,'diagonal_squared_error_upper':outward_upper(diagonal_error),'off_diagonal_squared_error_upper':outward_upper(off_error)})
        if (j+1)%10==0:print('ASSEMBLY_BLOCK',j+1,flush=True)
    error=error2.upper().sqrt()
    separation=arb(reference['shifted_binary_H_separation_lower'])-error.upper()
    assert separation.lower()>0,'terminal assembly perturbation does not close'
    paths=[NOTE,Path(__file__),HOME/'receipt_replay.py',HOME/'check_verified_inverse_factor.py',REFERENCE,SOURCE,SAMPLES,
           CALC/'previous/tail_estimator.py',HOME/'pentachoron_higher_closed_cutoff_bundle.zip',HOME/'pentachoron_full_response128_packet_bundle.zip']
    return {'schema':'marici.scattering.terminal-assembly.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'precision_bits':128,'blocks_covered':49,'block_errors':rows,
            'terminal_assembly_difference_Frobenius_upper':outward_upper(error),
            'assembled_exact_pose_shift_separation_lower':outward_lower(separation),
            'assembled_reference_inertia_certified':True,'negative_inertia':130,'zero_inertia':0,
            'reference':'exact DFT and rational terminal assembly from frozen binary native samples, exact radical pose shift',
            'native_geometry_samples_enclosed':False,'original_source_assembly_certified':False,
            'true_ground_identity_certified':False,'retained_frame_certified':False,'full_band_coupled_inverse_certified':False,
            'AB1_execution_cycles_spent':1,'AB1_execution_cycles_remaining':1,
            'H7_disposition':'open; conditional terminal assembly and inertia certified, upstream samples/frame/coupled inverse remain'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=audit()
    if args.check:assert_receipt_matches(json.loads(RESULT.read_text(encoding='utf-8')),r)
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','terminal_assembly_difference_Frobenius_upper','assembled_exact_pose_shift_separation_lower','negative_inertia','H7_disposition')}))


if __name__=='__main__':main()
