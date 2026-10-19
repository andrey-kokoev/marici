"""RB1 final audit: binary eigenpair proximity, not ground-label/source certification."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse
from fractions import Fraction as F
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np
from flint import arb,ctx
from high_energy_scattering_net import ROOT,HOME,digest,validate as historical_validate
from receipt_replay import assert_receipt_matches
from check_verified_inverse_factor import balls,squared_norm,outward_upper,outward_lower

CALC=ROOT/'.ai/tmp/scattering-h6-response33/calculation'
SOURCE=CALC/'cache/source_work/engine/source_packet/source/source/quantum_strain_route.py'
NOTE=HOME/'GROUND-FRAME-BRIDGE-AUDIT.md'
RESULT=HOME/'results/ground-frame-bridge.v1.json'
REFERENCE=HOME/'results/exact-pose-reference.v1.json'


def audit():
    historical_validate();ctx.prec=128
    reference=json.loads(REFERENCE.read_text(encoding='utf-8'))
    for path,value in reference['source_sha256'].items():assert digest(ROOT/path)==value
    code=SOURCE.read_text(encoding='utf-8')
    for term in ('coeff=np.fft.fft(L,axis=0)/N','self.nat.matrix(lam)','e,V=eigsh(self.H','self.ground=np.flatnonzero'):
        assert term in code
    calc=CALC
    if os.name=='nt':calc=Path(chr(92)*2+'?'+chr(92)+str(calc.resolve()))
    sys.path.insert(0,str(calc/'previous'))
    spec=importlib.util.spec_from_file_location('ground_bridge_source',calc/'previous/tail_estimator.py')
    te=importlib.util.module_from_spec(spec);spec.loader.exec_module(te)
    engine=Path((calc/'engine_path.txt').read_text())
    M,dyn,it,down,base,efull,Vfull,solve,provenance=te.load_model(engine,'tail420')
    H=it.H;assert (H-H.conj().T).nnz==0
    ids=it.ground;assert len(ids)==2
    V=it.V[:,ids];e0=float(it.e[0]);b=250;n=49
    norm2=[arb(0),arb(0)];residual2=[arb(0),arb(0)]
    for j in range(n):
        ix=slice(j*b,(j+1)*b);vb=balls(V[ix]);r=balls(H[ix,ix].toarray())*vb-vb*arb(e0)
        if j:r+=balls(H[ix,slice((j-1)*b,j*b)].toarray())*balls(V[(j-1)*b:j*b])
        if j+1<n:r+=balls(H[ix,slice((j+1)*b,(j+2)*b)].toarray())*balls(V[(j+1)*b:(j+2)*b])
        for a in range(2):
            from flint import acb_mat
            norm2[a]+=squared_norm(acb_mat([[vb[i,a]] for i in range(b)]))
            residual2[a]+=squared_norm(acb_mat([[r[i,a]] for i in range(b)]))
    rows=[]
    for index,nn,rr in zip(ids,norm2,residual2):
        assert nn.lower()>0
        norm=nn.lower().sqrt();res=rr.upper().sqrt();distance=res.upper()/norm.lower()
        rows.append({'stored_column':int(index),'vector_norm_lower':outward_lower(norm),
                     'residual_norm_upper':outward_upper(res),'distance_to_some_binary_H_eigenvalue_upper':outward_upper(distance)})
    # Exact hostile example: a perfect eigenpair need not be the ground pair.
    matrix_eigenvalues=[F(-1),F(0),F(10)];selected_value=F(0)
    assert selected_value in matrix_eigenvalues and selected_value!=min(matrix_eigenvalues)
    paths=[NOTE,Path(__file__),HOME/'receipt_replay.py',HOME/'check_verified_inverse_factor.py',REFERENCE,SOURCE,
           CALC/'previous/tail_estimator.py',CALC/'cache/source_work/engine/eigen_nl49_N25.npz',
           HOME/'pentachoron_higher_closed_cutoff_bundle.zip',HOME/'pentachoron_full_response128_packet_bundle.zip']
    return {'schema':'marici.scattering.ground-frame-bridge.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'precision_bits':128,'binary_energy_origin':e0,'ground_labelled_columns':rows,
            'binary_eigenvalue_proximity_certified':True,'true_ground_identity_certified':False,
            'source_assembly_certified':False,'retained_420_spectral_projector_certified':False,
            'full_band_coupled_inverse_certified':False,
            'source_assembly_unmet_enclosures':['native sampled geometry/spin matrices','FFT and coefficient assembly from exact native samples','strain/metric coefficients and intended nodes'],
            'frame_unmet_certificates':['complete low-spectrum coverage and ground label','retained eigenframe Gram enclosure and spectral-subspace transfer'],
            'exact_hostile_control':'zero eigenpair residual for diag(-1,0,10) at eigenvalue 0 does not certify ground',
            'RB1_execution_cycles_spent':2,'RB1_execution_cycles_remaining':0,
            'RB1_outcome':'inconclusive for full H7; exact pose and binary eigenpair proximity certified only',
            'H7_disposition':'open; source assembly, ground identity/frame and coupled inverse remain unproved'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();r=audit()
    if args.check:assert_receipt_matches(json.loads(RESULT.read_text(encoding='utf-8')),r)
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','ground_labelled_columns','true_ground_identity_certified','RB1_outcome')}))


if __name__=='__main__':main()
