"""H5: fresh all-energy downstream residual and coherent packet ledger, response128."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse
import hashlib
import io
import json
from pathlib import Path
from zipfile import ZipFile
import numpy as np
import scipy.sparse as sp
from scipy.optimize import root
from high_energy_scattering_net import ROOT, HOME, digest, validate as historical_validate

ARCHIVE=HOME/'pentachoron_full_response128_packet_bundle.zip'
PROOF=HOME/'PACKET-CONTINUITY-PROOF.md'
RESULT=HOME/'results/response128-continuity.v1.json'
TOL=1e-8


def audit():
    historical_validate();prefix='results/response128/'
    with ZipFile(ARCHIVE) as z:
        def load(name):
            with np.load(io.BytesIO(z.read(prefix+name)),allow_pickle=False) as a:return {k:a[k] for k in a.files}
        md=load('metadata.npz');fields=np.load(io.BytesIO(z.read(prefix+'fields.npy')),allow_pickle=False)
        source_script=z.read('source_scripts/response_feedback.py').decode()
        assert "b=ent.g*ent.S.conj().T@d['u'];field=down.diagnostic_field[:,:down.nport]@b" in source_script
        sources=np.array([load(f'state_{i:03d}.npz')['source_b'] for i in range(len(md['K']))])
    K=md['K'];assert len(K)==17
    ng=fields.shape[2];assert ng==4
    mass=md['mass'];ih=md['iH'];ig=md['iGraph'];io_=md['iOut'];mid=ih[:,ih.shape[1]//2,:];nl=len(md['lambda_grid'])
    base=sp.csc_matrix((md['base_data'],md['base_indices'],md['base_indptr']),shape=tuple(md['base_shape']))
    herm=base-base.conj().T;assert max(abs(herm.data),default=0)<TOL
    slices=[np.r_[ih[j].ravel(),ig[0,j].ravel(),ig[1,j].ravel()] for j in range(nl)]
    assert set(np.concatenate(slices))==set(np.flatnonzero(mass>0))
    assert np.all(mass[io_.ravel()]==0)
    def forcing(b):
        rhs=np.zeros_like(fields[0])
        for j in range(nl):rhs[mid[j]]=md['B'][j]@b[2*j:2*j+2]/np.sqrt(md['sstar'][j])
        return rhs
    stationary=[]
    for i,E in enumerate(float(md['e0'])+K):
        f=fields[i];rhs=forcing(sources[i]);r=base@f-E*mass[:,None]*f-rhs
        for side in range(2):
            idx=io_[side].ravel();V=md['vs'][side];k=np.sqrt(E-md['es'][side]+0j)
            r[idx]-=1j*V@(k[:,None]*(V.conj().T@f[idx]))
        err=float(np.linalg.norm(r)/max(1,np.linalg.norm(rhs)));assert err<TOL
        stationary.append({'energy_index':i,'relative_full_downstream_residual':err})
    w=np.empty(len(K));w[0]=(K[1]-K[0])/2;w[-1]=(K[-1]-K[-2])/2;w[1:-1]=(K[2:]-K[:-2])/2
    def moments(par,ret=False):
        a=np.exp(-.25*((K-par[0])/np.exp(par[1]))**2);a/=np.sqrt(w@abs(a)**2)
        ew=w*abs(a)**2;mean=ew@K;var=ew@(K-mean)**2
        return (a,mean,var) if ret else [(mean-3.3)/.035,(var-.035**2)/.035**2]
    fit=root(moments,[3.3,np.log(.035)],tol=1e-10)
    assert max(abs(np.array(moments(fit.x))))<1e-9
    amplitude,mean,var=moments(fit.x,True)
    records=[]
    for t in (-15.,0.,10.,25.,60.):
        c=w*amplitude*np.exp(-1j*(K-3.3)*t)/np.sqrt(2*np.pi)
        f=np.tensordot(c,fields,axes=(0,0));dot=np.tensordot(-1j*(K-3.3)*c,fields,axes=(0,0));b=np.tensordot(c,sources,axes=(0,0))
        r=1j*mass[:,None]*dot+(float(md['e0'])+3.3)*mass[:,None]*f-base@f+forcing(b)
        dp=np.zeros(nl);entry=np.zeros(nl);exit_=np.zeros(nl);flow=np.zeros(nl+1);delta=np.zeros(nl);bounds=np.zeros(nl)
        for j,ids in enumerate(slices):
            dp[j]=2*np.real(np.sum(mass[ids,None]*f[ids].conj()*dot[ids]))/ng
            y=md['B'][j].conj().T@f[mid[j]]/np.sqrt(md['sstar'][j])
            entry[j]=2*np.imag(np.vdot(b[2*j:2*j+2],y))/ng
            for side in range(2):exit_[j]+=2*float(md['gate_exit'])*np.imag(np.vdot(f[ig[side,j,7]],f[io_[side,j]]))/ng
            if j<nl-1:flow[j+1]=2*(5/16)/float(md['dlam'])**2*np.imag(np.sum(mass[ids,None]*f[ids].conj()*f[slices[j+1]]))/ng
            delta[j]=2*np.imag(np.vdot(f[ids],r[ids]))/ng
            bounds[j]=2*np.sum(np.linalg.norm(f[ids],axis=0)*np.linalg.norm(r[ids],axis=0))/ng
        defect=dp-entry+exit_+np.diff(flow)
        equation=float(np.linalg.norm(r[mass>0])/max(1,np.linalg.norm(f)))
        ledger=float(max(abs(defect-delta)));balance=float(max(abs(defect)))
        assert max(equation,ledger,balance)<TOL and np.all(abs(delta)<=bounds+TOL)
        records.append({'time':t,'relative_interior_equation_residual':equation,'max_continuity_defect':balance,
                        'max_residual_ledger_discrepancy':ledger,'max_residual_contribution_bound':float(max(bounds)),
                        'omitted_exit_term_defect':float(max(abs(defect-exit_)))})
    assert max(r['omitted_exit_term_defect'] for r in records)>100*TOL
    sources_to_pin=[ARCHIVE,PROOF,Path(__file__),HOME/'response128_packet_note.md']
    return {'schema':'marici.scattering.response128-continuity.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in sources_to_pin},
            'embedded_builder_sha256':hashlib.sha256(source_script.encode()).hexdigest(),
            'stationary_records':stationary,'packet_records':records,'packet_mean':float(mean),'packet_rms':float(np.sqrt(var)),
            'prepared_columns':ng,'numerical_test_tolerance':TOL,'certified_response_error_bound':False,
            'response_truncation_location':'Entrance response space; downstream fields reconstructed from the complete retained downstream solve for the supplied entrance forcing.',
            'proof_scope':'Exact downstream finite-equation continuity for arbitrary entrance forcing and all finite coherent energy superpositions. Floating tests support source binding, not equality of rounded arrays or full entrance accuracy.',
            'source_stationary_solver_replayed':False,'saved_pass_flags_used':False}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    result=audit()
    if args.check:
        old=json.loads(RESULT.read_text(encoding='utf-8'))
        assert old['source_sha256']==result['source_sha256'],'stale H5 response128 binding'
        assert old['status']==result['status'] and len(old['stationary_records'])==17
    else:RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('PASS: all 17 response128 downstream equations and five coherent packet residual ledgers.')


if __name__=='__main__':main()
