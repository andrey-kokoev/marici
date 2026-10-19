"""Exact archived pentachoron matrix binding and contact-dark ground sector.

Does not execute the archived high-energy solver or spend its live protocol.
"""
import argparse
import copy
import hashlib
import io
import json
from pathlib import Path
import zipfile
import pentachoron_exact as ex

ROOT=Path(__file__).resolve().parents[3]
HOME=Path(__file__).resolve().parent
ARCHIVE=ROOT/'research/scattering/high-energy/pentachoron_autonomous_contact_bundle.zip'
NOTE=HOME/'PENTACHORON-GROUND-SECTOR.md'
RESULT=HOME/'results/pentachoron-ground-sector.v1.json'
DRAFT=HOME/'contracts/pentachoron-bright-threshold-draft.v1.json'
SOURCE_SCRIPT_SHA='575b9f9ba16fc028effa5c5f209b552da815d0b093a5e8e28544b3d6fd9807f3'
SOURCE_RECEIPT_SHA='256b0a03239fb3e86053d8b905a8d5ed551a212484343fb24aacf3ec7fcbc1d5'


def sha(data):return hashlib.sha256(data).hexdigest()


def check_dark(H,P,theta,D):
    assert len(D)==20 and len(D[0])==2
    assert len(ex.rref(D)[1])==2,'dependent dark basis'
    assert ex.zero(ex.add(ex.mm(H,D),[[-theta*v for v in row] for row in D])),'not a threshold eigenvector'
    assert ex.zero(ex.mm(P,D)),'not contact-dark'


def build():
    draft=json.loads(DRAFT.read_text(encoding='utf-8'))
    assert draft['schema']=='marici.scattering.low-energy-pentachoron-bright-threshold-draft.v1'
    assert draft['registration']=='unresolved_draft_not_in_live_proposition_net' and draft['label'] is None
    assert draft['exact_matrix_receipt_sha256']==SOURCE_RECEIPT_SHA
    for key in ('bright_threshold_regularity_proved','added_to_live_planner','new_proposition_outcome_admitted'):
        assert draft[key] is False,'draft outcome/planning promotion'
    with zipfile.ZipFile(ARCHIVE) as z:
        outer=json.loads(z.read('SHA256.json'))
        for path,h in outer.items():assert sha(z.read(path))==h
        nested_bytes=z.read('pentachoron_connected_phase_energy_bundle.zip')
    with zipfile.ZipFile(io.BytesIO(nested_bytes)) as z:
        manifest=json.loads(z.read('SHA256.json'))
        for path,h in manifest.items():assert sha(z.read(path))==h
        raw=z.read('pentachoron_connected_phase_energy_results.json')
        script=z.read('pentachoron_connected_phase_energy.py')
    assert sha(raw)==SOURCE_RECEIPT_SHA and sha(script)==SOURCE_SCRIPT_SHA
    source=json.loads(raw);assert source['script_sha256']==sha(script)
    matrices={name:[[ex.parse(s) for s in row] for row in source['matrices'][name]]
              for name in ('L_original','L_connected','cycle_X','matching_P')}
    assert all(len(A)==20 and all(len(row)==20 for row in A) for A in matrices.values())
    Lo,Lc,X,P=(matrices[name] for name in ('L_original','L_connected','cycle_X','matching_P'))
    Ho=ex.add(Lo,X);Hc=ex.add(Lc,X);theta=ex.parse('(11-2*sqrt(6)-sqrt(5))/2')
    assert all(A==ex.adjoint(A) for A in (Ho,Hc,P))
    assert ex.mm(P,P)==P and len(ex.rref(P)[1])==2
    shifted=ex.add(Ho,[[-theta*v for v in row] for row in ex.eye(20)])
    rank=ex.psd_rank(shifted);assert rank==16
    V=ex.kernel(shifted);assert len(V[0])==4 and ex.zero(ex.mm(shifted,V))
    coupling=ex.mm(P,V);assert len(ex.rref(coupling)[1])==2
    D=ex.mm(V,ex.kernel(coupling));check_dark(Ho,P,theta,D)
    # The ambient orthogonal projector is independent of the chosen kernel basis.
    gram=ex.mm(ex.adjoint(D),D)
    det=gram[0][0]*gram[1][1]-gram[0][1]*gram[1][0];assert det
    inv=[[gram[1][1]/det,-gram[0][1]/det],[-gram[1][0]/det,gram[0][0]/det]]
    dark=ex.mm(ex.mm(D,inv),ex.adjoint(D))
    assert dark==ex.adjoint(dark) and ex.mm(dark,dark)==dark
    assert ex.zero(ex.mm(P,dark)) and ex.zero(ex.mm(dark,P))
    assert ex.mm(Ho,dark)==ex.mm(dark,Ho)==[[theta*v for v in row] for row in dark]
    controls=[]
    bad=copy.deepcopy(D);bad[0][0]=bad[0][0]+1
    for label,candidate in (('perturbed-dark-basis',bad),('duplicated-dark-column',[[row[0],row[0]] for row in D])):
        try:check_dark(Ho,P,theta,candidate)
        except AssertionError:controls.append(label)
        else:raise AssertionError('invalid dark certificate accepted: '+label)
    for text in ('__import__("os")','sqrt(7)','1.5','I.real'):
        try:ex.parse(text)
        except (AssertionError,ValueError):controls.append('reject-expression:'+text)
        else:raise AssertionError('unsafe/out-of-field expression accepted')
    paths={ARCHIVE,NOTE,DRAFT,Path(__file__),Path(ex.__file__),HOME/'test_pentachoron_exact.py'}
    return {'schema':'marici.scattering.low-energy-pentachoron-ground-sector.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():sha(p.read_bytes()) for p in sorted(paths)},
            'nested_bundle_sha256':sha(nested_bytes),'symbolic_receipt_sha256':sha(raw),'source_script_sha256':sha(script),
            'arithmetic':'Q(sqrt(2),sqrt(3),sqrt(5),i); exact rational sign enclosures for PSD pivots',
            'matrix_entry_source':'Archived symbolic strings, never floating NPZ or fitted eigenvectors',
            'original_ground_exact':'(11-2*sqrt(6)-sqrt(5))/2','Ho_minus_ground_psd_rank':rank,
            'ground_dimension':4,'ground_contact_rank':2,'ground_contact_kernel_dimension':2,
            'ground_basis':ex.encoded(V),'dark_basis':ex.encoded(D),'dark_projector':ex.encoded(dark),
            'Ho_and_Hc_hermitian':True,'matching_P_orthogonal_rank_two':True,
            'dark_sector_reduces_full_contact_H':True,
            'dark_channel_consequence':'For every k>0, E=theta+k^2, dark incoming vectors have t=I2,r=0 and chi=0 in the fixed contact model.',
            'uniform_all_ground_transmission_O_k_excluded':True,
            'threshold_full_block_automatic_dark_kernel_dimension_at_least':2,
            'bright_threshold_regularity_proved':False,'full_threshold_block_invertibility_proved':False,
            'draft':DRAFT.relative_to(ROOT).as_posix(),
            'archived_scientific_solver_executed':False,'new_proposition_outcomes_admitted':False,
            'physical_species_identified':False,'hostile_controls_refused':controls}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale ground-sector receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','Ho_minus_ground_psd_rank','ground_dimension','ground_contact_rank','ground_contact_kernel_dimension','bright_threshold_regularity_proved','new_proposition_outcomes_admitted')}))


if __name__=='__main__':main()
