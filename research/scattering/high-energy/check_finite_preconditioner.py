"""H6 center finite-response preconditioner defect screen; not inverse certification."""
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
CASE=CALC/'runs/h6_response33'
NOTE=HOME/'FINITE-PRECONDITIONER-SCREEN.md'
RESULT=HOME/'results/finite-preconditioner.v1.json'


def audit(power_steps=0):
    historical_validate();calc=CALC
    if os.name=='nt':calc=Path(chr(92)*2+'?'+chr(92)+str(calc.resolve()))
    sys.path.insert(0,str(calc/'previous'))
    spec=importlib.util.spec_from_file_location('finite_prec_source',calc/'previous/tail_estimator.py')
    te=importlib.util.module_from_spec(spec);spec.loader.exec_module(te)
    engine=Path((calc/'engine_path.txt').read_text())
    M,dyn,it,down,base,efull,Vfull,solve,provenance=te.load_model(engine,'tail420')
    with np.load(CASE/'central_state.npz',allow_pickle=False) as z:e=z['e'];u=z['u'];y=z['y']
    with np.load(CASE/'projection.npz',allow_pickle=False) as z:V=z['Vblocks'];S=z['S']
    n,m,nr=32,1096,98;N=n*m;E=float(e[0]+3.3)
    assert V.shape==(n,m,m) and S.shape==(N,nr)
    offsets=E-np.r_[e,e]
    rel=base.ax.base;g=base.g
    gg=np.array([rel.rel_green(float(t),n,base.h,base.rho,7,9) for t in offsets])
    diagonal=np.diagonal(V,axis1=1,axis2=2).T
    inverse=np.linalg.inv(np.eye(n)[None,:,:]-gg*diagonal[:,None,:])
    R=inverse@gg
    Sb=S.reshape(n,m,nr);Sh=S.conj().T
    U=np.einsum('aij,jap->iap',R,Sb,optimize=True).reshape(N,nr)
    # Source downstream response only; no new entrance stationary solve.
    ds=down.solve(E);Z=ds['Z']
    small=np.eye(nr)+g*g*Z@(Sh@U)
    C=la.solve(small,g*g*Z,check_finite=False)
    UC=U@C
    # T=Dpre^-1 G Voff; Edefect=M G Voff=T-U C S* T.
    # Build only S*T and T*U (port rank) and the exact structured Frobenius sum.
    ST=np.empty((nr,N),complex);TstarU=np.empty((N,nr),complex);Tnorm2=0.
    Ublocks=U.reshape(n,m,nr)
    for j in range(n):
        off=V[j].copy();np.fill_diagonal(off,0)
        Rcol=R[:,:,j].T
        row_squares=np.sum(abs(off)**2,axis=1)
        Tnorm2+=float(np.sum(np.sum(abs(Rcol)**2,axis=0)*row_squares))
        Sr=np.einsum('iap,ia->pa',Sb.conj(),Rcol,optimize=True)
        ST[:,j*m:(j+1)*m]=Sr@off
        Ru=np.einsum('ia,iap->ap',Rcol.conj(),Ublocks,optimize=True)
        TstarU[j*m:(j+1)*m]=off.conj().T@Ru
    cross=np.trace(C@(ST@TstarU))
    correction_norm2=np.trace((UC.conj().T@UC)@(ST@ST.conj().T)).real
    defect_norm2=Tnorm2-2*cross.real+correction_norm2
    assert defect_norm2>0
    def apply_T(x):
        xb=x.reshape(n,m,-1);off_action=V@xb-diagonal.T[:,:,None]*xb
        return np.einsum('aij,jap->iap',R,off_action,optimize=True).reshape(N,-1)
    def apply_defect(x):
        t=apply_T(x);return t-UC@(Sh@t)
    # Independent sampled-column consistency for the port contractions.
    check_columns=[0,m-1,7*m+123,N-1]
    STerror=0.;TUerror=0.
    for index in check_columns:
        basis=np.zeros((N,1),complex);basis[index]=1;t=apply_T(basis)
        STerror=max(STerror,float(la.norm(Sh@t-ST[:,index:index+1])/max(1,la.norm(Sh@t))))
        TUerror=max(TUerror,float(la.norm(t.conj().T@U-TstarU[index:index+1])/max(1,la.norm(t.conj().T@U))))
    assert max(STerror,TUerror)<1e-9
    # Action lower bound on the four actual corrected prepared columns.
    action=apply_defect(u);ratios=np.linalg.norm(action,axis=0)/np.linalg.norm(u,axis=0)
    power_rows=[]
    if power_steps:
        assert 1<=power_steps<=16
        state=u.copy();initial_norms=np.linalg.norm(u,axis=0)
        for power in range(1,power_steps+1):
            state=apply_defect(state)
            power_rows.append({'power':power,'prepared_action_norm_ratios':(np.linalg.norm(state,axis=0)/initial_norms).tolist()})
    defect_fro=float(np.sqrt(defect_norm2))
    paths=[NOTE,Path(__file__),HOME/'receipt_replay.py',CALC/'previous/tail_estimator.py',CASE/'central_state.npz',CASE/'projection.npz',HOME/'pentachoron_higher_closed_cutoff_bundle.zip',HOME/'pentachoron_full_response128_packet_bundle.zip']
    result={'schema':'marici.scattering.finite-preconditioner.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'K_radial':3.3,'finite_entrance_dimension':N,'port_rank':nr,
            'diagonal_preconditioned_interaction_Frobenius_norm':float(np.sqrt(Tnorm2)),
            'full_Woodbury_defect_Frobenius_norm':defect_fro,
            'defect_action_norm_ratios_on_prepared_columns':ratios.tolist(),
            'port_contraction_check_relative_errors':{'Sstar_T':STerror,'Tstar_U':TUerror},
            'small_Woodbury_singular_value_min_float':float(la.svdvals(small)[-1]),
            'Frobenius_Neumann_candidate_below_one':bool(defect_fro<1),
            'spectral_Neumann_candidate_ruled_out_by_prepared_action_float':bool(max(ratios)>1),
            'inverse_bound_certified':False,'stationary_solver_error_certified':False,
            'full_band_covered':False,
            'H6_disposition':'open; source finite-response preconditioner defect tested at center, no residual-to-observable bound certified'}
    if power_steps:result['polynomial_power_action_tests']=power_rows
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();result=audit()
    if args.check:assert_receipt_matches(json.loads(RESULT.read_text(encoding='utf-8')),result)
    else:RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','full_Woodbury_defect_Frobenius_norm','defect_action_norm_ratios_on_prepared_columns','Frobenius_Neumann_candidate_below_one','H6_disposition')}))


if __name__=='__main__':main()
