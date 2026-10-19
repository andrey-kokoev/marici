"""Audit new high-energy inputs and test their positive contact form on our rims.

Independent rational algebra only: no claimed scattering solve or physical
normalization. The supplied archive solvers are not executed by this checker.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,io,json,zipfile
from check_neutron_canonical_occupied_closure import ROOT,eye,mm,transpose,inverse,difference,scale,rank,encoded
from check_neutron_charge_completed_rest_gap import psd_rank


def main():
    base=ROOT/'research/scattering/high-energy';checks={};archive_audits={}
    for name,manifest in [('pentachoron_autonomous_contact_bundle.zip','SHA256.json'),('pentachoron_exit_gate_bundle.zip','MANIFEST.sha256.json')]:
        path=base/name
        with zipfile.ZipFile(path) as z:
            hashes=json.loads(z.read(manifest))
            for member,digest in hashes.items():assert hashlib.sha256(z.read(member)).hexdigest()==digest,member
            archive_audits[name]={'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'manifest_members_checked':len(hashes)}
            if name.startswith('pentachoron_autonomous'):
                with zipfile.ZipFile(io.BytesIO(z.read('pentachoron_connected_phase_energy_bundle.zip'))) as old:
                    assert hashlib.sha256(old.read('pentachoron_connected_phase_energy.py')).hexdigest()=='575b9f9ba16fc028effa5c5f209b552da815d0b093a5e8e28544b3d6fd9807f3'
                    assert hashlib.sha256(old.read('pentachoron_connected_phase_energy_results.json')).hexdigest()=='256b0a03239fb3e86053d8b905a8d5ed551a212484343fb24aacf3ec7fcbc1d5'
    checks['both_contact_and_exit_archives_and_nested_source_pins_verified']=True
    srcpath=ROOT/'research/strominger/results/neutron-two-rim-contact-binding.json';src=json.loads(srcpath.read_text());assert src['status']=='passed'
    for p,h in src['source_hashes'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h,p
    oldH=[list(map(F,r)) for r in src['full_joint_H_without_mu']];metric=[list(map(F,r)) for r in src['source_metric']]
    g=F(src['parameters']['g']);K=[r[2:] for r in oldH[2:]]
    T=scale(1/g,[r[2:] for r in oldH[:2]]);W=scale(1/g,[r[:2] for r in oldH[2:]])
    coremetric=[r[2:] for r in metric[2:]];assert mm(T,W)==eye(2)
    assert mm(transpose(W),coremetric)==scale(3,T)
    checks['existing_full_neutron_rim_attachment_unchanged']=True
    comparisons=[]
    for eta in (F(1,2),F(2)):
        # Boundary amplitude chart is (sqrt(ell)*psi(0),chi), with ell=1
        # for this algebra test. Positive form: 3 eta ||psi(0)-T chi||².
        D=[eye(2)[i]+[-x for x in T[i]] for i in range(2)]
        form=scale(3*eta,mm(transpose(D),D))
        G=mm(inverse(metric),form)
        assert psd_rank(form)==rank(G)==2
        assert mm(transpose(G),metric)==mm(metric,G)
        assert [r[:2] for r in G[:2]]==scale(eta,eye(2))
        assert [r[2:] for r in G[:2]]==scale(-eta,T)
        assert [r[:2] for r in G[2:]]==scale(-eta,W)
        assert [r[2:] for r in G[2:]]==scale(eta,mm(W,T))
        for x in (F(1,10),F(1),F(3)):
            Kx=[[a+F(i==j)*x for j,a in enumerate(r)] for i,r in enumerate(K)]
            response=mm(mm(T,inverse(Kx)),W)
            updated=[[a+b for a,b in zip(r,s)] for r,s in zip(Kx,scale(eta,mm(W,T)))]
            direct=difference(scale(eta,eye(2)),scale(eta*eta,mm(mm(T,inverse(updated)),W)))
            factor=[[F(i==j)+eta*response[i][j] for j in range(2)] for i in range(2)]
            expected=scale(eta,inverse(factor))
            assert direct==expected and psd_rank(direct)==2
            comparisons.append({'eta':str(eta),'x':str(x),'effective_contact_matrix_at_E_minus_x':encoded(direct)})
    checks['positive_contact_diagonal_and_offdiagonal_blocks_derived']=True
    checks['full_core_elimination_equals_exact_two_rim_response_formula']=True
    result={'status':'passed','checks':checks,'archive_audits':archive_audits,
            'candidate_reuse':{'state':'L2(R) tensor C2 incoming/outgoing port field, direct-sum existing C24 neutron/bank core',
                'energy_form':'Integral [kinetic term + incoming internal energy] + <chi,K chi>_M + eta ||sqrt(ell) psi(0)-T chi||^2_(3 I2)',
                'effective_contact':'V_eff(E)=eta*ell*[I2+eta*R(E)]^-1, R(E)=T(K-E)^-1 W, away from elimination poles',
                'checks_scope':'Exact boundary-form and subthreshold Schur identities, not a full continuum scattering calculation.',
                'new_inputs_required':['continuum kinetic coefficient','contact length ell','gate strength eta','incoming threshold matrix and preparation'],
                'important_difference':'This is a positive contact completion with both diagonals; it is not our earlier bare off-diagonal finite internal-channel Hamiltonian.'},
            'rational_tests':comparisons,
            'verification_boundary':'Archive manifests/source pins and independent rational adapter identities freshly checked. Bundled NumPy/SciPy/SymPy solvers were not run; those packages are absent in the default Python environment.',
            'physical_normalization':'Not selected by the new branch; its epsilon, hbar, m, ell and rho choices remain explicit model inputs.'}
    inputs=[srcpath,Path(__file__).resolve(),base/'pentachoron_autonomous_contact_note.md',base/'pentachoron_exit_gate_note.md',base/'pentachoron_relativistic_kinetics_note.md',base/'quantum_strain_note.md']
    result['source_hashes']={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}
    dest=ROOT/'research/strominger/results/high-energy-contact-reuse.json';dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'passed','checks':len(checks),'archive_audits':archive_audits,'exact_schur_cases':len(comparisons),'full_scattering_rerun':False},indent=2))

if __name__=='__main__':main()
