"""Independent raw-field audit: does not import or call the scattering solver."""
from pathlib import Path
import hashlib,json
import numpy as np
ROOT=Path(__file__).resolve().parents[3]


def main():
    base=ROOT/'research/strominger/results';receipt=base/'neutron-autonomous-rim-scattering.json';data=json.loads(receipt.read_text())
    assert data['status']=='passed'
    for p,h in data['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    npz=base/'neutron-autonomous-rim-scattering.npz';assert hashlib.sha256(npz.read_bytes()).hexdigest()==data['npz_sha256']
    with np.load(npz) as f:
        K=f['core_operator'];W=f['contact'];Qdark=f['dark_basis'];maxima={'jump':0.,'core':0.,'S_reconstruction':0.,'flux':0.,'dark_amplitude':0.}
        for E,S,a,c in zip(f['energies'],f['S'],f['boundary'],f['core']):
            speed=2*np.sqrt(E-.5);incoming=np.eye(2)/np.sqrt(speed)
            jump=2j*np.sqrt(E-.5)*(a-incoming)-2*(a-W.conj().T@c)
            core=(K+2*W@W.conj().T-E*np.eye(24))@c-2*W@a
            t=np.sqrt(speed)*a;r=t-np.eye(2);rebuilt=np.block([[r,t],[t,r]])
            flux=np.sum(abs(r)**2+abs(t)**2,axis=0)
            maxima['jump']=max(maxima['jump'],float(np.linalg.norm(jump)))
            maxima['core']=max(maxima['core'],float(np.linalg.norm(core)))
            maxima['S_reconstruction']=max(maxima['S_reconstruction'],float(np.linalg.norm(S-rebuilt)))
            maxima['flux']=max(maxima['flux'],float(np.max(abs(flux-1))))
            maxima['dark_amplitude']=max(maxima['dark_amplitude'],float(np.linalg.norm(Qdark.conj().T@c)))
        assert max(maxima.values())<1e-8
        count=len(f['energies'])
    out={'status':'passed','raw_energy_cases':count,'maximum_residuals':maxima,
         'scope':'Independent recomputation from retained fields, not a second independent PDE solve or physical calibration.',
         'source_hashes':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in (receipt,npz,Path(__file__).resolve())}}
    (base/'neutron-autonomous-rim-scattering-audit.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
