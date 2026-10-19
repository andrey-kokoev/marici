"""Fresh pilot-field H5 audit; does not close the later response128 binding."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse
import io
import json
from pathlib import Path
from zipfile import ZipFile
import numpy as np
import scipy
import scipy.sparse as sp
from high_energy_scattering_net import ROOT, HOME, digest, validate as historical_validate

ARCHIVE=HOME/'pentachoron_time_resolved_strain_bundle.zip'
RESULT=HOME/'results/packet-continuity-pilot.v1.json'
PROOF=HOME/'PACKET-CONTINUITY-PROOF.md'
TIMES=(-20.,0.,10.,20.,80.)
TOL=2e-11  # Pilot source-scale absolute arithmetic/consistency test, not certified error.


def audit():
    historical_validate();records=[]
    with ZipFile(ARCHIVE) as z:
        def load(name):
            with np.load(io.BytesIO(z.read(name)),allow_pickle=False) as a:return {k:a[k] for k in a.files}
        for fixture in ('primary','refined'):
            meta=load(fixture+'/metadata.npz');amp=load(fixture+'/amplitudes.npz');factor=load(fixture+'/spectral_field_factors.npz')
            options=json.loads(z.read(fixture+'/collection.json'))['options']
            K=meta['K'];center=options['center'];sigma=options['sigma'];ng=int(meta['ground_degeneracy'])
            assert ng==4 and center==2.3
            w=np.empty(len(K));w[0]=(K[1]-K[0])/2;w[-1]=(K[-1]-K[-2])/2;w[1:-1]=(K[2:]-K[:-2])/2
            a=np.exp(-.25*((K-center)/sigma)**2);a/=np.sqrt(w@abs(a)**2)
            mass=meta['mass'];ih=meta['iH'];ig=meta['iGraph'];io_=meta['iOut'];nl=len(meta['lambda_grid']);mid=ih[:,ih.shape[1]//2,:]
            base=sp.csc_matrix((meta['base_data'],meta['base_indices'],meta['base_indptr']),shape=tuple(meta['base_shape']))
            herm=base-base.conj().T;hermerr=float(max(abs(herm.data),default=0));assert hermerr<TOL
            slices=[np.r_[ih[j].ravel(),ig[0,j].ravel(),ig[1,j].ravel()] for j in range(nl)]
            assert np.all(mass[io_.ravel()]==0)
            assert set(np.concatenate(slices))==set(np.flatnonzero(mass>0))
            for t in TIMES:
                coeff=w*a*np.exp(-1j*(K-center)*t)/np.sqrt(2*np.pi)
                # Evaluate compressed raw spectra directly, never saved density/current series.
                shape=tuple(factor['shape'])[1:]
                psi=((coeff@factor['left'])@factor['right']).reshape(shape)
                dot=(((coeff*(-1j*(K-center)))@factor['left'])@factor['right']).reshape(shape)
                b=np.tensordot(coeff,amp['source_b'],axes=(0,0)).reshape(nl,2,ng)
                rhs=np.zeros_like(psi)
                for j in range(nl):rhs[mid[j]]=meta['B'][j]@b[j]/np.sqrt(meta['sstar'][j])
                residual=1j*mass[:,None]*dot-(base@psi-(float(meta['e0'])+center)*mass[:,None]*psi-rhs)
                dp=np.array([2*np.real(np.sum(psi[ix].conj()*dot[ix]*mass[ix,None]))/ng for ix in slices])
                y=np.einsum('jar,jai->jri',meta['B'].conj(),psi[mid])/np.sqrt(meta['sstar'])[:,None,None]
                entry=2*np.imag(np.sum(b.conj()*y,axis=(1,2)))/ng
                exit_=np.zeros(nl)
                h=psi[ih]
                flow=2*(5/16)/float(meta['dlam'])**2*np.imag(np.einsum('jqai,jqai,q->j',h[:-1].conj(),h[1:],meta['w']))/ng
                for side in range(2):
                    g=psi[ig[side]];trace=psi[io_[side]]
                    flow+=2*(5/16)/float(meta['dlam'])**2*np.imag(np.sum(g[:-1].conj()*g[1:],axis=(1,2,3)))/ng
                    exit_+=2*float(meta['gate_exit'])*np.imag(np.sum(g[:,7].conj()*trace,axis=(1,2)))/ng
                defect=dp-entry+exit_+np.diff(np.r_[0.,flow,0.])
                delta=np.array([2*np.imag(np.sum(psi[ix].conj()*residual[ix]))/ng for ix in slices])
                bound=np.array([2*np.sum(np.linalg.norm(psi[ix],axis=0)*np.linalg.norm(residual[ix],axis=0))/ng for ix in slices])
                balance=float(max(abs(defect)));equation=float(np.linalg.norm(residual[mass>0]));ledger=float(max(abs(defect-delta)))
                assert equation<TOL and balance<TOL and ledger<TOL
                assert np.all(abs(delta)<=bound+TOL)
                records.append({'fixture':fixture,'time':t,'energy_nodes':len(K),'center':center,
                                'hermiticity_residual':hermerr,'interior_equation_residual':equation,
                                'max_slice_continuity_defect':balance,'max_residual_ledger_discrepancy':ledger,
                                'max_residual_contribution_bound':float(max(bound)),
                                'omitted_exit_term_defect':float(max(abs(defect-exit_)))})
            print('PASS: fresh pilot continuity and residual ledger',fixture,flush=True)
    assert max(r['omitted_exit_term_defect'] for r in records)>100*TOL
    sources=[ARCHIVE,PROOF,Path(__file__)]
    return {'schema':'marici.scattering.packet-continuity-pilot.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in sources},
            'numpy_version':np.__version__,'scipy_version':scipy.__version__,
            'absolute_test_tolerance':TOL,'tolerance_is_certified_error_bound':False,'records':records,
            'H5_disposition':'partial audit only: this checker does not audit response128; see the separate response128 checker for that binding',
            'source_stationary_solver_replayed':False,'saved_time_series_pass_flags_used':False}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    result=audit()
    if args.check:
        old=json.loads(RESULT.read_text(encoding='utf-8'))
        assert old['source_sha256']==result['source_sha256'],'stale pilot receipt sources'
        assert old['status']==result['status'] and len(old['records'])==len(result['records'])
        # Fresh tolerance checks above are authoritative; floating reductions need not be bitwise equal.
    else:RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('Pilot audit only; response128 binding is handled by the separate response128 checker.')


if __name__=='__main__':main()
