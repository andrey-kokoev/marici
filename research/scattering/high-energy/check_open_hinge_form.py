"""Source-binding/support audit for the analytic H4 proof; not a proof assistant."""
import argparse
import hashlib
import io
import json
from pathlib import Path
from zipfile import ZipFile
import numpy as np
from high_energy_scattering_net import ROOT, HOME, digest, validate as historical_validate

ARCHIVE=HOME/'pentachoron_joint_incoming_bundle.zip'
PROOF=HOME/'OPEN-HINGE-FORM-PROOF.md'
RESULT=HOME/'results/open-hinge-form.v1.json'
PREFIX='source/inputs/geometric_source/inputs/open_products/'


def audit():
    historical_validate();data=ARCHIVE.read_bytes();nested={}
    for name in ('inputs/pentachoron_strained_phase_bundle.zip','inputs/pentachoron_axial_deformation_bundle.zip'):
        with ZipFile(io.BytesIO(data)) as z:data=z.read(name)
        nested[name]=hashlib.sha256(data).hexdigest()
    with ZipFile(io.BytesIO(data)) as z:
        pins=json.loads(z.read(PREFIX+'input_hashes.json'))['input_files'];payload={}
        for name,expected in pins.items():
            payload[name]=z.read(PREFIX+'inputs/'+name)
            assert hashlib.sha256(payload[name]).hexdigest()==expected
        source=z.read(PREFIX+'open_product_solver.py').decode()
    # Bind the proof's contact inventory to the actual source, not a fitted alternative.
    required=['defect(self.iH[j],self.iH[j+1],ID,.5/self.ds)',
              'sg*entry_strength*Q','sg*switch_strength*Q',
              'defect(endidx,graph[0],ID,end_strength)',
              "defect(out,np.r_[graph[7],mem],en['U'],end_strength)",
              "V=F@src['HC']@F.conj().T",
              'add(ix,ix,g*np.eye(len(ix)))','add(iy,iy,g*(U.conj().T@U))',
              'add(ix,iy,-g*U)','add(iy,ix,-g*U.conj().T)']
    for term in required:assert term in source,'missing declared form term: '+term
    with np.load(io.BytesIO(payload['native_matrices.npz']),allow_pickle=False) as z:
        HO=z['H_original'];HC=z['H_connected'];P=z['matching_projector']
    with np.load(io.BytesIO(payload['hinge_matrices.npz']),allow_pickle=False) as z:A=z['A']
    reports=[]
    for name,H in [('H_O',HO),('H_C',HC)]:
        assert H.shape==(20,20)
        herm=float(np.linalg.norm(H-H.conj().T));minimum=float(np.linalg.eigvalsh(H).min())
        assert herm<1e-11 and minimum>=-1e-11
        reports.append({'operator':name,'hermiticity_residual':herm,'numerical_min_eigenvalue':minimum})
    defects={'P_hermitian':float(np.linalg.norm(P-P.conj().T)),
             'P_projector':float(np.linalg.norm(P@P-P)),
             'P_rank_two_trace':float(abs(np.trace(P)-2)),
             'A_hermitian':float(np.linalg.norm(A-A.conj().T)),
             'A_square':float(np.linalg.norm(A@A-np.eye(20)/16))}
    assert all(v<1e-11 for v in defects.values())
    # Countercontrol: dropping the diagonal of a comparison gives an indefinite term.
    bad=np.array([[0.,-1.],[-1.,0.]])
    assert np.linalg.eigvalsh(bad).min()<0
    assert np.array([1.,1.])@bad@np.array([1.,1.])==-2
    sources=[ARCHIVE,PROOF,Path(__file__),HOME/'pentachoron_open_product_flux_note.md']
    return {'schema':'marici.scattering.open-hinge-form.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():digest(p) for p in sources},
            'nested_archive_sha256':nested,'compact_input_sha256':pins,
            'source_solver_sha256':hashlib.sha256(source.encode()).hexdigest(),
            'source_form_terms_checked':required,'native_sanity_checks':reports,'projector_generator_sanity_checks':defects,
            'numerical_tolerance':1e-11,'numerical_checks_are_positivity_proof':False,
            'finite_record_dimensions':[168,168],'field_component_dimensions':[20,20,28,28],
            'form_domain':'H1 on the line, compact hinge and both half-lines, plus unrestricted finite records',
            'analytic_proof':'Positive Gram terms and bounded native potential; trace bounds make the form norm equivalent to the complete H1/finite-record norm; representation theorem supplies the unique nonnegative self-adjoint operator.',
            'machine_checked_analytic_proof':False,'discard_contact_diagonals_control':'rejected: quadratic value -2',
            'source_solvers_replayed':False,'physical_explanation_outcome':None}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    result=audit()
    if args.check:
        old=json.loads(RESULT.read_text(encoding='utf-8'))
        assert old['source_sha256']==result['source_sha256'],'stale H4 proof/source receipt'
        assert old['source_form_terms_checked']==result['source_form_terms_checked']
        assert old['status']==result['status']
    else:RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('PASS: H4 source-binding audit. Closure/self-adjointness rests on the explicit analytic proof, not numerical checks.')


if __name__=='__main__':main()
