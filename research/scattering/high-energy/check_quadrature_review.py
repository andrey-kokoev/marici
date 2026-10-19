"""Independent H6 raw-field review and explicit observable-error budgets."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse
from receipt_replay import assert_receipt_matches
import json
from pathlib import Path
import numpy as np
import scipy.sparse as sp
from scipy.optimize import root,minimize_scalar
from high_energy_scattering_net import ROOT,HOME,digest,validate as historical_validate

CASE=ROOT/'.ai/tmp/scattering-h6-response33/calculation/runs/h6_response33'
COMPARISON=HOME/'results/quadrature17-vs33.v1.json'
RESULT=HOME/'results/quadrature-review.v1.json'
NOTE=HOME/'QUADRATURE-REFINEMENT-REVIEW.md'


def audit():
    historical_validate();comparison=json.loads(COMPARISON.read_text(encoding='utf-8'))
    for p,h in comparison['source_sha256'].items():assert digest(ROOT/p)==h
    assert digest(CASE/'packet_kernels.npz')==comparison['kernel_sha256']
    md=np.load(CASE/'metadata.npz',allow_pickle=False);fields=np.load(CASE/'fields.npy',mmap_mode='r',allow_pickle=False)
    col=json.loads((CASE/'collection.json').read_text(encoding='utf-8'))
    K=md['K'];assert len(K)==33 and col['completed']==33 and fields.shape[2]==4
    assert all(r['response_directions']==128 for r in col['rows'])
    mass=md['mass'];ih=md['iH'];ig=md['iGraph'];io=md['iOut'];nl=len(md['lambda_grid']);mid=ih[:,ih.shape[1]//2,:]
    ids=[np.r_[ih[j].ravel(),ig[0,j].ravel(),ig[1,j].ravel()] for j in range(nl)]
    a0=np.concatenate(ids[:-1]);a1=np.concatenate(ids[1:]);ng=4
    base=sp.csc_matrix((md['base_data'],md['base_indices'],md['base_indptr']),shape=tuple(md['base_shape']))
    stationary=[];flux=[]
    for k,E in enumerate(float(md['e0'])+K):
        with np.load(CASE/f'state_{k:03d}.npz',allow_pickle=False) as state:
            b=state['source_b'];S=state['S'];flux.append(float(np.linalg.norm(S.conj().T@S-np.eye(ng),2)))
        f=fields[k];rhs=np.zeros_like(f)
        for j in range(nl):rhs[mid[j]]=md['B'][j]@b[2*j:2*j+2]/np.sqrt(md['sstar'][j])
        residual=base@f-E*mass[:,None]*f-rhs
        for side in range(2):
            ix=io[side].ravel();V=md['vs'][side];velocity=np.sqrt(E-md['es'][side]+0j)
            residual[ix]-=1j*V@(velocity[:,None]*(V.conj().T@f[ix]))
        stationary.append(float(np.linalg.norm(residual)/max(1,np.linalg.norm(rhs))))
    assert max(stationary)<1e-8 and max(flux)<1e-8
    ff=fields.reshape(len(K),-1)
    G=(ff.conj()*np.repeat(mass,ng))@ff.T/ng
    cross=(fields[:,a0,:].reshape(len(K),-1).conj()*np.repeat(mass[a0],ng))@fields[:,a1,:].reshape(len(K),-1).T
    cross*=2*(5/16)/float(md['dlam'])/ng
    B=(cross-cross.conj().T)/(2j)
    with np.load(CASE/'packet_kernels.npz',allow_pickle=False) as saved:
        errors={'occupation_kernel':float(np.max(abs(G-saved['G']))),'current_kernel':float(np.max(abs(B-saved['Gb'])))}
    assert max(errors.values())<1e-10
    prepared=[]
    for stride in (2,1):
        ix=np.arange(0,len(K),stride);k=K[ix];g=G[np.ix_(ix,ix)];b=B[np.ix_(ix,ix)]
        w=np.empty(len(k));w[0]=(k[1]-k[0])/2;w[-1]=(k[-1]-k[-2])/2;w[1:-1]=(k[2:]-k[:-2])/2
        def moments(p,full=False):
            amp=np.exp(-.25*((k-p[0])/np.exp(p[1]))**2);amp/=np.sqrt(w@amp**2)
            ew=w*amp**2;mean=ew@k;var=ew@(k-mean)**2
            return (amp,ew,mean,var) if full else [(mean-3.3)/.035,(var-.035**2)/.035**2]
        fit=root(moments,[3.3,np.log(.035)],tol=1e-10)
        assert max(abs(np.array(moments(fit.x))))<1e-9
        amp,ew,mean,var=moments(fit.x,True);coeff=w*amp/np.sqrt(2*np.pi)
        def vector(t):return coeff*np.exp(-1j*(k-3.3)*t)
        def population(t):v=vector(t);return float(np.vdot(v,g@v).real)
        # Tenfold denser search than the source's half-unit seed grid.
        times=np.arange(-100.,100.00001,.05);values=np.array([population(t) for t in times]);j=int(values.argmax())
        assert 0<j<len(times)-1
        fit=minimize_scalar(lambda t:-population(t),bounds=(times[j-1],times[j+1]),method='bounded',options={'xatol':1e-12})
        t=float(fit.x);v=vector(t);pop=population(t);rate=float(np.vdot(v,b@v).real/pop)
        # Direct field sum independently checks the energy-space kernel evaluation.
        state=np.tensordot(v,fields[ix],axes=(0,0));direct_pop=float(np.sum(mass[:,None]*abs(state)**2)/ng)
        direct_current=float(2*(5/16)/float(md['dlam'])*np.imag(np.sum(mass[a0,None]*state[a0].conj()*state[a1]))/ng)
        assert abs(direct_pop-pop)<1e-11 and abs(direct_current/pop-rate)<1e-10
        probabilities=np.array([r['product_probability'] for r in col['rows']])[ix]
        prepared.append({'energy_nodes':len(k),'peak_time':t,'peak_transport':rate,
                         'whole_packet_transport':float(ew@np.diag(b).real/(ew@np.diag(g).real)),
                         'product_probability':float(ew@probabilities),
                         'moment_matched_weights':ew.tolist(),'mean':float(mean),'rms':float(np.sqrt(var)),
                         'direct_peak_occupation_error':abs(direct_pop-pop),'direct_peak_current_ratio_error':abs(direct_current/pop-rate)})
    old,new=prepared;budgets={}
    for key in ('peak_transport','whole_packet_transport','product_probability'):
        difference=abs(new[key]-old[key]);margin=.01*abs(old[key])-difference
        assert margin>0
        budgets[key]={'relative_change':difference/abs(old[key]),'absolute_acceptance_margin':margin,
                      'max_common_relative_error_budget':margin/(abs(new[key])+1.01*abs(old[key])),
                      'sufficient_error_condition':'epsilon33 + 1.01 epsilon17 <= absolute_acceptance_margin'}
    maximum_entrance_residual=max(max(r['linear_residuals']) for r in col['rows'])
    paths=[HOME/'receipt_replay.py',COMPARISON,NOTE,Path(__file__),CASE/'metadata.npz',CASE/'fields.npy',CASE/'packet_kernels.npz',CASE/'collection.json']
    return {'schema':'marici.scattering.quadrature-review.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'fresh_stationary_downstream_checks':33,'max_downstream_relative_residual':max(stationary),
            'max_prepared_column_flux_defect':max(flux),'source_reported_max_projected_entrance_residual':maximum_entrance_residual,
            'kernel_reconstruction_errors':errors,'independently_reconstructed_packets':prepared,'error_budgets':budgets,
            'all_three_numerical_inequalities_pass':True,'solver_to_observable_error_certified':False,
            'global_peak_interval_certified':False,
            'H6_disposition':'open: independently reproduced numerical support; solver-error and rigorous peak-location margins not certified',
            'full_untruncated_H7_required':False}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    result=audit()
    if args.check:
        old=json.loads(RESULT.read_text(encoding='utf-8'))
        assert_receipt_matches(old,result)
    else:RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','relative_changes':{k:v['relative_change'] for k,v in result['error_budgets'].items()},'H6':'open; certified error margins remain missing'}))


if __name__=='__main__':main()
