"""H7 partial audit: native omitted residual of the corrected response128 state.

Requires the completed H6 source cache. Does not compute the complete kinetic/
boundary residual or a uniform inverse bound.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('OMP_NUM_THREADS','1')
import argparse
from receipt_replay import assert_receipt_matches
import copy
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np
from high_energy_scattering_net import ROOT,HOME,digest,validate as historical_validate

CALC=ROOT/'.ai/tmp/scattering-h6-response33/calculation'
if os.name=='nt':CALC=Path(chr(92)*2+'?'+chr(92)+str(CALC.resolve()))
CASE=CALC/'runs/h6_response33'
RESULT=HOME/'results/corrected-native-leakage.v1.json'
NOTE=HOME/'CORRECTED-RESIDUAL-NATIVE-TERM.md'


def audit():
    historical_validate()
    sys.path.insert(0,str(CALC/'previous'))
    spec=importlib.util.spec_from_file_location('h7_source_tail_estimator',CALC/'previous/tail_estimator.py')
    te=importlib.util.module_from_spec(spec);spec.loader.exec_module(te)
    engine=Path((CALC/'engine_path.txt').read_text())
    M,dyn,it,down,base,efull,Vfull,solve,provenance=te.load_model(engine,'tail420')
    with np.load(CASE/'central_state.npz',allow_pickle=False) as z:V=z['V'];e=z['e'];u=z['u']
    assert V.shape==(12250,548) and u.shape==(32*2*548,4)
    gram=V.conj().T@V;gram_error=float(np.linalg.norm(gram-np.eye(548)))
    assert gram_error<2e-8
    HV=it.H@V;ritz=V.conj().T@HV
    # Orthogonal projection onto the actual stored span, accounting for its tiny
    # finite-precision departure from orthonormal columns rather than assuming I.
    leakage=HV-V@np.linalg.solve(gram,ritz)
    orthogonality=float(np.linalg.norm(V.conj().T@leakage)/max(1,np.linalg.norm(leakage)))
    assert orthogonality<2e-9
    low=float(np.linalg.norm(leakage[:,:420]));tail=float(np.linalg.norm(leakage[:,420:]))
    assert low<1e-6 and tail>1e-4
    # Native Hamiltonian action on the actual corrected four-column state.
    coeff=u.reshape(32,2,548,4).transpose(2,0,1,3).reshape(548,-1)
    native_omitted=leakage@coeff
    per_column=np.sqrt(np.sum(abs(native_omitted.reshape(12250,32,2,4))**2,axis=(0,1,2)))
    native_action=HV@coeff
    relative=float(np.linalg.norm(native_omitted)/np.linalg.norm(native_action))
    assert float(np.linalg.norm(native_omitted))>1e-6
    # Reuse the supplied interaction/contact forcing in the corrected basis,
    # but label it as a component, not the complete outgoing residual.
    with np.load(CASE/'projection.npz',allow_pickle=False) as z:projected_V=z['Vblocks'];projected_S=z['S']
    with np.load(CASE/'central_state.npz',allow_pickle=False) as z:y=z['y']
    with np.load(CALC/'response_basis/raw_quadrature.npz',allow_pickle=False) as z:quad={k:z[k] for k in z.files}
    aug=copy.copy(it);aug.nm=548;aug.V=V;aug.e=e;aug.coeff=V.reshape(it.nlam,it.N,10,548)
    ent=copy.copy(base);ent.nb=548;ent.M=1096;ent.N=32*1096;ent.Vblocks=projected_V;ent.S=projected_S
    raw,interaction,proj=te.full_forcing(aug,down,ent,quad,u,y)
    # full_forcing subtracts V V*; remove the tiny Gram defect for direct comparison.
    raw_cols=raw.transpose(2,0,1,3).reshape(12250,-1)
    interaction_exact_span=raw_cols-V@np.linalg.solve(gram,V.conj().T@raw_cols)
    native_norm=float(np.linalg.norm(native_omitted));interaction_norm=float(np.linalg.norm(interaction_exact_span))
    inputs=[ROOT/'.ai/tmp/scattering-h6-response33/calculation/runs/h6_response33'/n for n in ('central_state.npz','projection.npz')]
    paths=inputs+[HOME/'receipt_replay.py',HOME/'pentachoron_full_response128_packet_bundle.zip',HOME/'pentachoron_higher_closed_cutoff_bundle.zip',Path(__file__),NOTE,ROOT/'.ai/tmp/scattering-h6-response33/calculation/previous/tail_estimator.py',ROOT/'.ai/tmp/scattering-h6-response33/calculation/response_feedback.py']
    return {'schema':'marici.scattering.corrected-native-leakage.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'K_radial':3.3,'operator_energy_unshifted':float(it.e[0]+3.3),'total_energy_with_pose_shift':float(it.e[0]+3.3+te.CPOSE),
            'raw_internal_dimension':12250,'retained_dimension':548,'gram_defect':gram_error,
            'retained_native_Ritz_diagonal_defect':float(np.linalg.norm(ritz-np.diag(e))),
            'native_omitted_column_block_norms':{'original_420':low,'added_128':tail},
            'native_omitted_state_norm':native_norm,'native_omitted_state_norm_per_prepared_column':per_column.tolist(),
            'native_omitted_relative_to_full_native_action':relative,'projection_orthogonality_residual':orthogonality,
            'interaction_only_omitted_state_norm':interaction_norm,
            'native_plus_interaction_omitted_state_norm':float(np.linalg.norm(native_omitted+interaction_exact_span)),
            'native_and_interaction_sum_is_full_residual':False,
            'missing_components':['full raw radial kinetic action on the non-invariant response span','outgoing entrance boundary action in the same raw space','positive solver-space norm and full-band inverse certificate'],
            'H7_disposition':'open: an additional nonzero native residual component is freshly exposed; no source singularity or uniform inverse proved',
            'continuum_or_observable_error_bound':False}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    result=audit()
    if args.check:
        old=json.loads(RESULT.read_text(encoding='utf-8'))
        assert_receipt_matches(old,result)
    else:RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','native_omitted_column_block_norms','native_omitted_state_norm','interaction_only_omitted_state_norm','H7_disposition')}))


if __name__=='__main__':main()
