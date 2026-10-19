"""Fresh central matching residual audit; conditional tail estimate, not H7 closure."""
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
import scipy.sparse as sp
from high_energy_scattering_net import ROOT,HOME,digest,validate as historical_validate

CALC=ROOT/'.ai/tmp/scattering-h6-response33/calculation'
CASE=CALC/'runs/h6_response33'
NOTE=HOME/'CORRECTED-MATCHING-RESIDUAL.md'
RESULT=HOME/'results/corrected-matching-residual.v1.json'


def audit():
    historical_validate()
    calc=CALC
    if os.name=='nt':calc=Path(chr(92)*2+'?'+chr(92)+str(calc.resolve()))
    sys.path.insert(0,str(calc/'previous'))
    spec=importlib.util.spec_from_file_location('matching_source_tail',calc/'previous/tail_estimator.py')
    te=importlib.util.module_from_spec(spec);spec.loader.exec_module(te)
    engine=Path((calc/'engine_path.txt').read_text())
    M,dyn,it,down,base,efull,Vfull,solve,provenance=te.load_model(engine,'tail420')
    with np.load(CASE/'central_state.npz',allow_pickle=False) as z:V=z['V'];e=z['e'];u=z['u'];y=z['y']
    assert V.shape==(12250,548) and u.shape==(32*1096,4)
    with np.load(CASE/'projection.npz',allow_pickle=False) as z:projected_V=z['Vblocks'];projected_S=z['S']
    with np.load(CALC/'response_basis/raw_quadrature.npz',allow_pickle=False) as z:quad={k:z[k] for k in z.files}
    aug=copy.copy(it);aug.nm=548;aug.V=V;aug.e=e;aug.coeff=V.reshape(it.nlam,it.N,10,548)
    ent=copy.copy(base);ent.nb=548;ent.M=1096;ent.N=32*1096;ent.Vblocks=projected_V;ent.S=projected_S
    raw,unused,proj=te.full_forcing(aug,down,ent,quad,u,y)
    raw_cols=raw.transpose(2,0,1,3).reshape(12250,-1)
    coeff=u.reshape(32,2,548,4).transpose(2,0,1,3).reshape(548,-1)
    raw_u=V@coeff
    V0=V[:,:420];gram=V0.conj().T@V0
    gram_defect=float(np.linalg.norm(gram-np.eye(420)))
    eigen_defect=float(np.linalg.norm(it.H@V0-V0*e[:420]))
    assert gram_defect<2e-8 and eigen_defect<1e-6
    low_u=V0.conj().T@raw_u;low_q=V0.conj().T@raw_cols
    # Actual stored-span orthogonal complements, not merely subtraction of V V*.
    tail_u=raw_u-V0@np.linalg.solve(gram,low_u)
    tail_q=raw_cols-V0@np.linalg.solve(gram,low_q)
    K=3.3;E=float(e[0]+K);rel=base.ax.base
    offsets=E-e[:420]
    gg=np.array([rel.rel_green(float(t),32,base.h,base.rho,7,9) for t in offsets])
    low_u=low_u.reshape(420,32,2,4).transpose(1,2,0,3)
    low_q=low_q.reshape(420,32,2,4).transpose(1,2,0,3)
    # The source's original four prepared incoming columns, in the same order.
    all_offsets=E-np.r_[e[:420],e[:420]]
    oi=np.flatnonzero(all_offsets>1e-9);ground=np.flatnonzero(abs(np.r_[e[:420],e[:420]]-e[0])<1e-6)
    assert len(ground)==4
    k,v=rel.open_wave(all_offsets[oi],base.rho)
    ff=2*np.sqrt(base.h)*np.sinc(k*base.h/(2*np.pi))[None,:]*np.cos(base.x[:,None]*k)/np.sqrt(v)
    Fin=np.zeros((32,840,4),complex)
    for column,a in enumerate(ground):Fin[:,a,column]=ff[:,int(np.flatnonzero(oi==a)[0])]
    low_residual=low_u-np.einsum('aij,jtag->itag',gg,low_q,optimize=True)-Fin.reshape(32,2,420,4)
    low_norm=float(np.linalg.norm(low_residual))
    assert low_norm/max(1,np.linalg.norm(Fin))<1e-8
    # Independently evaluate the complete downstream row of the matching system.
    with np.load(CASE/'metadata.npz',allow_pickle=False) as md:
        md={key:md[key] for key in md.files}
    index=int(np.argmin(abs(md['K']-K)));assert abs(md['K'][index]-K)<1e-12
    fields=np.load(CASE/'fields.npy',mmap_mode='r',allow_pickle=False);field=fields[index]
    b=base.g*projected_S.conj().T@u
    rhs=np.zeros_like(field);ih=md['iH'];mid=ih[:,ih.shape[1]//2,:]
    trace=np.vstack([md['B'][j].conj().T@field[mid[j]]/np.sqrt(md['sstar'][j]) for j in range(len(mid))])
    trace_error=float(np.linalg.norm(trace-y));assert trace_error<1e-8
    for j in range(len(mid)):rhs[mid[j]]=md['B'][j]@b[2*j:2*j+2]/np.sqrt(md['sstar'][j])
    matrix=sp.csc_matrix((md['base_data'],md['base_indices'],md['base_indptr']),shape=tuple(md['base_shape']))
    rdown=matrix@field-E*md['mass'][:,None]*field-rhs
    for side in range(2):
        ix=md['iOut'][side].ravel();outV=md['vs'][side];velocity=np.sqrt(E-md['es'][side]+0j)
        rdown[ix]-=1j*outV@(velocity[:,None]*(outV.conj().T@field[ix]))
    down_norm=float(np.linalg.norm(rdown));assert down_norm/max(1,np.linalg.norm(rhs))<1e-8
    gap=16-(float(e[0])+3.51+float(md['cpose']));assert gap>2*base.rho
    tu=float(np.linalg.norm(tail_u));tq=float(np.linalg.norm(tail_q))
    envelope=tu+tq/gap
    paths=[HOME/'receipt_replay.py',NOTE,Path(__file__),HOME/'RADIAL-RESOLVENT-ENVELOPE.md',HOME/'results/radial-envelope.v1.json',CALC/'previous/tail_estimator.py',CALC/'response_basis/raw_quadrature.npz',CASE/'central_state.npz',CASE/'projection.npz',CASE/'fields.npy',CASE/'metadata.npz',HOME/'pentachoron_higher_closed_cutoff_bundle.zip',HOME/'pentachoron_full_response128_packet_bundle.zip']
    return {'schema':'marici.scattering.corrected-matching-residual.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in paths},
            'K_radial':K,'operator_energy_unshifted':E,'prepared_columns':4,
            'original_420_frame_Gram_defect':gram_defect,'original_420_native_eigen_defect':eigen_defect,
            'original_420_matching_residual_Frobenius_norm':low_norm,
            'downstream_matching_residual_Frobenius_norm':down_norm,'downstream_trace_reconstruction_error':trace_error,
            'Q420_corrected_state_Frobenius_norm':tu,'Q420_corrected_interaction_forcing_Frobenius_norm':tq,
            'uncertified_band_gap_candidate':gap,
            'conditional_central_Q420_residual_envelope':envelope,
            'conditional_central_total_residual_envelope':float(np.sqrt(low_norm**2+down_norm**2+envelope**2)),
            'envelope_is_certified':False,
            'unmet_envelope_premises':['certified invariant spectral projector/gap in place of floating source eigenframes','outward-rounded residual and norm evaluation'],
            'full_inverse_certified':False,'full_band_residual_evaluated':False,
            'H7_disposition':'open; central low-sector and downstream matching rows evaluated, conditional omitted-sector envelope computed'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args();result=audit()
    if args.check:
        old=json.loads(RESULT.read_text(encoding='utf-8'))
        assert_receipt_matches(old,result)
    else:RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','original_420_matching_residual_Frobenius_norm','downstream_matching_residual_Frobenius_norm','conditional_central_Q420_residual_envelope','H7_disposition')}))


if __name__=='__main__':main()
