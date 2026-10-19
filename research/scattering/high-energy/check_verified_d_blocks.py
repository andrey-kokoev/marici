"""VF1: Arb inertia/separation of exact binary D blocks, not original source gap."""
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
from flint import acb,acb_mat,arb,ctx
from high_energy_scattering_net import ROOT,HOME,digest,validate as historical_validate
from receipt_replay import assert_receipt_matches

CALC=ROOT/'.ai/tmp/scattering-h6-response33/calculation'
NOTE=HOME/'VERIFIED-D-BLOCKS.md'
RESULT=HOME/'results/verified-d-blocks.v1.json'
WITNESS=HOME/'results/verified-factor-witness.v1.npz'


def balls(A):return acb_mat([[acb(complex(x)) for x in row] for row in A])


def squared_norm(A):
    total=arb(0)
    for i in range(A.nrows()):
        for j in range(A.ncols()):
            v=A[i,j];total+=v.real*v.real+v.imag*v.imag
    return total


def upper_float(x):return float(np.nextafter(float(x.upper()),np.inf))
def lower_float(x):return float(np.nextafter(float(x.lower()),-np.inf))


def audit():
    historical_validate();ctx.prec=128
    assert arb(.1).is_exact()
    calc=CALC
    if os.name=='nt':calc=Path(chr(92)*2+'?'+chr(92)+str(calc.resolve()))
    sys.path.insert(0,str(calc/'previous'))
    spec=importlib.util.spec_from_file_location('verified_D_source',calc/'previous/tail_estimator.py')
    te=importlib.util.module_from_spec(spec);spec.loader.exec_module(te)
    engine=Path((calc/'engine_path.txt').read_text())
    M,dyn,it,down,base,efull,Vfull,solve,provenance=te.load_model(engine,'tail420')
    shift=float(10-te.CPOSE);n,b=49,250
    factors=[];multipliers=[];frames=[];spectra=[];Dprev=None
    for j in range(n):
        ix=slice(j*b,(j+1)*b);A=it.H[ix,ix].toarray()-shift*np.eye(b)
        if j:
            C=it.H[ix,slice((j-1)*b,j*b)].toarray()
            L=la.solve(Dprev,C.conj().T,assume_a='her',check_finite=False).conj().T
            D=A-L@Dprev@L.conj().T;D=(D+D.conj().T)/2
        else:D=(A+A.conj().T)/2;L=np.zeros((b,b),complex)
        assert np.array_equal(D,D.conj().T),'binary D not exactly Hermitian'
        ev,U=la.eigh(D,check_finite=False)
        factors.append(D);multipliers.append(L);frames.append(U);spectra.append(ev);Dprev=D
    data={'D':np.array(factors),'L_subdiagonal':np.array(multipliers),
          'eigenframes':np.array(frames),'eigenvalues':np.array(spectra),
          'binary_shift':np.array(shift)}
    if WITNESS.exists():
        with np.load(WITNESS,allow_pickle=False) as saved:
            assert set(saved.files)==set(data)
            for key,value in data.items():assert np.array_equal(saved[key],value),'binary witness drift: '+key
    else:np.savez_compressed(WITNESS,**data)
    rows=[];negative=0;minimum=np.inf;maximum_gram=0.;maximum_reconstruction=0.
    identity=acb_mat(np.eye(b).tolist())
    for j,(D,U,ev) in enumerate(zip(factors,frames,spectra)):
        Ub=balls(U);Ustar=Ub.conjugate().transpose()
        gram=(squared_norm(Ustar*Ub-identity)).sqrt()
        weighted=acb_mat([[acb(complex(U[i,k]))*arb(float(ev[k])) for k in range(b)] for i in range(b)])
        reconstruction=(squared_norm(balls(D)-weighted*Ustar)).sqrt()
        smallest=min(arb(abs(float(v))) for v in ev)
        assert gram.upper()<1
        comparison_separation=(1-gram.upper())*smallest
        assert reconstruction.upper()<comparison_separation.lower(),'D inertia homotopy not certified'
        separation=comparison_separation-reconstruction.upper()
        assert separation.lower()>0
        count=int(np.count_nonzero(ev<0));negative+=count
        minimum=min(minimum,lower_float(separation))
        maximum_gram=max(maximum_gram,upper_float(gram));maximum_reconstruction=max(maximum_reconstruction,upper_float(reconstruction))
        rows.append({'block':j,'negative_inertia_certified':count,
                     'Gram_defect_Frobenius_upper':upper_float(gram),
                     'spectral_reconstruction_Frobenius_upper':upper_float(reconstruction),
                     'D_separation_lower':lower_float(separation),
                     'Gram_defect_ball':str(gram),'spectral_reconstruction_ball':str(reconstruction)})
        if (j+1)%10==0:print('VERIFIED_D_BLOCK',j+1,flush=True)
    assert negative==130 and len(rows)==49
    paths=[NOTE,Path(__file__),HOME/'receipt_replay.py',HOME/'H7-VERIFIED-FACTOR-SUCCESSOR.md',WITNESS,CALC/'previous/tail_estimator.py',HOME/'pentachoron_higher_closed_cutoff_bundle.zip',HOME/'pentachoron_full_response128_packet_bundle.zip']
    return {'schema':'marici.scattering.verified-d-blocks.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'precision_bits':128,'binary_shift':shift,'blocks_covered':49,'block_dimension':250,
            'binary_D_inertia_certified':True,'negative_inertia_sum':negative,
            'minimum_D_separation_lower':minimum,'maximum_Gram_defect_upper':maximum_gram,
            'maximum_spectral_reconstruction_error_upper':maximum_reconstruction,'block_results':rows,
            'reference':'exact binary Hermitian D blocks of durable witness; congruence comparison and strict Hermitian perturbation',
            'verified_inverse_factor_bound':False,'original_source_gap_certified':False,
            'full_band_coupled_inverse_certified':False,
            'unmet_gates':['verified inverse-factor bound','linkage of factor witness to certified H-LDL* residual','original source assembly/energy reference','spectral-frame transfer','full-band coupled matching inverse'],
            'VF1_execution_cycles_spent':1,'VF1_execution_cycles_remaining':2,
            'H7_disposition':'open; all binary D-block inertias and separations certified, no source gap or coupled inverse inferred'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();result=audit()
    if args.check:assert_receipt_matches(json.loads(RESULT.read_text(encoding='utf-8')),result)
    else:RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','blocks_covered','negative_inertia_sum','minimum_D_separation_lower','maximum_Gram_defect_upper','H7_disposition')}))


if __name__=='__main__':main()
