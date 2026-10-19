"""Versioned local source crosswalk; no atlas rewrite or physical admission."""
from pathlib import Path
import argparse
import hashlib
import json
from copy import deepcopy

ROOT=Path(__file__).resolve().parents[3]
BASE=Path(__file__).resolve().parent
DEST=BASE/'results/atlas-seed-correspondence.v1.json'
ATLAS='research/matter/element-isotope-catalog.json'
COLLECTION='research/strominger/results/arrow_particle_collection.json'

# Positional claim keys are local to the freshly hashed catalogue, not permanent
# owner IDs. Classes express scope, never promote owner claim status.
PLAN={
    'proton-candidate':('proton',['geometry_partial','protocol_not_compared','construction_partial','physical_gate_open']),
    'neutron-candidate':('neutron',['geometry_partial','protocol_not_compared','energy_not_compared','protocol_not_compared','physical_gate_open']),
    'electron-candidate':('electron',['geometry_partial','five_cell_gate_open','spinor_not_compared','spinor_not_compared','spinor_not_compared','spinor_not_compared','energy_not_compared','spinor_not_compared','physical_gate_open','spinor_not_compared','physical_gate_open']),
    'positron-candidate':('positron candidate',['different_operations_not_contradiction','physical_gate_open'])
}
EXPLANATIONS={
    'geometry_partial':'Seed/assembled geometry link only; complete atlas adapter, mode and interface claims are not replayed by this correspondence.',
    'protocol_not_compared':'Arrow seed/geometry entry is not the atlas native coefficient, transfer or memory protocol.',
    'construction_partial':'Shared candidate naming and geometry do not independently replay the retained coefficient construction.',
    'physical_gate_open':'Collection explicitly does not derive physical identification; atlas conjectural/unconstructed identification remains unchanged.',
    'energy_not_compared':'Seed generator and support counts do not establish the atlas charging, energy or mass law.',
    'five_cell_gate_open':'Five-cell geometric motion does not construct compatible five-cell tetrahedral-spinor/energy transport.',
    'spinor_not_compared':'Atlas tetrahedral spinor/field/interface claims concern another carrier/protocol; no seed-to-spinor intertwiner is imported.',
    'different_operations_not_contradiction':'Atlas viewer phase conjugation and newer inverse affine seed generator are distinct operations. Neither is a derived physical charge-conjugation operator.'
}


def load(path):return json.loads((ROOT/path).read_text(encoding='utf-8'))
def digest(path):return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
def validate_row(row,claim,model):
    if row['atlas_status']!=claim['status'] or row['atlas_statement']!=claim['statement'] or row['atlas_source_ids']!=claim['source_ids']:
        raise ValueError('Owner claim changed by local crosswalk')
    if row['collection_physical_identification_derived']!=model['physical_identification_derived']:
        raise ValueError('Collection physical boundary changed')
    if row['claim_proved_by_correspondence'] or row['physical_equivalence_admitted']:
        raise ValueError('Source correspondence is not proof or physical equivalence')
    if row['relation'] not in EXPLANATIONS:raise ValueError('Unknown scoped relation')


def audit():
    atlas=load(ATLAS);collection=load(COLLECTION)
    assert atlas['schema_version']=='1.1.0' and collection['schema']=='marici.strominger.arrow-particle-collection.v3'
    assert collection['status']=='passed'
    constituents={c['id']:c for c in atlas['constituents']};sources={s['id']:s for s in atlas['sources']}
    models={m['label']:m for m in collection['models']}
    assert len(models)==len(collection['models'])==9 and set(constituents)==set(PLAN)
    dependencies={ATLAS,COLLECTION,'research/matter/README.md',
        'research/strominger/positron-reversed-electron-seed.md','research/strominger/photon-shared-edge-seed.md',
        'research/strominger/reversed-matter-seeds.md','research/scattering/seed-composition/check_atlas_seed_correspondence.py',
        'research/scattering/seed-composition/contracts/seed-composition-work-net.v1.json',
        'research/scattering/seed-composition/contracts/source-pins.v1.json'}
    input_checks=[]
    for model in models.values():
        path=model['source_path'];actual=digest(path)
        assert actual==model['source_sha256']
        assert model['physical_identification_derived'] is False
        dependencies.add(path)
        input_checks.append({'label':model['label'],'source_path':path,'input_hash_matches':True,
                             'physical_identification_derived':False,'arrow_reversal_of':model.get('arrow_reversal_of')})
    rows=[]
    for cid,(label,relations) in PLAN.items():
        constituent=constituents[cid];model=models[label]
        assert len(relations)==len(constituent['claims'])
        for i,(claim,relation) in enumerate(zip(constituent['claims'],relations)):
            links=[]
            for sid in claim['source_ids']:
                s=sources[sid];path=s['location']
                assert s['kind']=='repository' and (ROOT/path).is_file()
                dependencies.add(path);links.append({'atlas_source_id':sid,'path':path})
            row={'local_claim_key':f'{cid}/claims/{i}','atlas_constituent_status':constituent['status'],
                 'atlas_status':claim['status'],'atlas_statement':claim['statement'],'atlas_source_ids':claim['source_ids'],
                 'atlas_resolved_sources':links,'collection_label':label,'collection_source_path':model['source_path'],
                 'collection_physical_identification_derived':False,'relation':relation,
                 'scope':EXPLANATIONS[relation],'claim_proved_by_correspondence':False,'physical_equivalence_admitted':False}
            validate_row(row,claim,model);rows.append(row)
    assert len(rows)==22
    unmatched=[label for label in models if label not in {label for label,relations in PLAN.values()}]
    assert unmatched==['neutrino candidate #1','photon candidate','antiproton candidate','antineutron candidate','antineutrino candidate']
    electron=models['electron'];positron=models['positron candidate'];photon=models['photon candidate']
    assert positron['arrow_reversal_of']=='electron'
    assert electron['effective_source']['metric']==positron['effective_source']['metric']
    assert photon['assembly_stage']=='retained two-face seed, before tetrahedral completion'
    assert photon['geometry']['f_vector']==[4,5,2]
    assert photon['geometry']['full_completion_counts']['supporting_facets']==4
    pin_records=[]
    for p,sha in load('research/scattering/seed-composition/contracts/source-pins.v1.json')['source_sha256'].items():
        pin_records.append({'path':p,'matches_existing_pin':digest(p)==sha})
    # Mechanical hostile tests: status laundering and geometric -> physical
    # promotion must be refused even when all links resolve.
    claim=constituents['electron-candidate']['claims'][0];original=next(r for r in rows if r['local_claim_key']=='electron-candidate/claims/0')
    hostiles=0
    for field,value in [('atlas_status','physically_identified'),('claim_proved_by_correspondence',True),('physical_equivalence_admitted',True),('collection_physical_identification_derived',True)]:
        hostile=deepcopy(original);hostile[field]=value
        try:validate_row(hostile,claim,electron)
        except ValueError:hostiles+=1
        else:raise AssertionError('Crosswalk promotion accepted')
    return {
        'schema':'marici.scattering.atlas-seed-correspondence.v1',
        'status':'twenty_two_claims_linked_by_scope_five_collection_entries_absent_from_atlas_no_physical_promotion',
        'source_sha256':{p:digest(p) for p in sorted(dependencies)},
        'identity_checks':{'collection_inputs':input_checks,'existing_pin_comparison':pin_records,
                           'owner_scientific_suites_replayed':False,'positional_claim_keys_bound_to_atlas_hash':True},
        'correspondence':rows,
        'missing_atlas_entries':[{'collection_label':label,'classification':'missing_catalogue_entry_not_contradiction_or_impossibility'} for label in unmatched],
        'specific_differences':{'positron':'Conjugate viewer phases versus inverse affine seed: no full-protocol/physical charge conjugation derived.',
                               'photon':'Two-face retained stage is separately recorded; unchanged full completion still has four facets. No atlas photon constituent entry.',
                               'electron':'Five-cycle geometry and rank-two tetrahedral spinor remain separate; compatible five-cell transport gate is unconstructed.',
                               'documentation_versions':'Older photon/positron notes describe six/five entries; live v3 collection and reversed-matter note contain nine. Historical narrative count, not a scientific inconsistency.'},
        'remaining_operation_requirements':[
            {'requirement':'source controller/dictionary policy','scope':'Supplied masks/conditional segmented automaton, not derived by catalogue naming'},
            {'requirement':'odd correlation preparation','scope':'Graph reflection exists; selecting odd input remains an added preparation'},
            {'requirement':'event-label recombination','scope':'Joint covariance does not authorize coherent label erasure or odd system postselection'},
            {'requirement':'algebraic state-dependent metric/filter','scope':'Conditional Perron/whitening constructions are not identified with atlas spinor or native physical energy'}],
        'hostile_promotions_refused':hostiles,
        'boundary':{'atlas_or_collection_rewritten':False,'formal_work_net_outcome_changed':False,
                    'source_correspondence_is_proof':False,'physical_species_equivalence_admitted':False},
        'next_gate':'Inspect the owning electron spinor and five-cycle source adapters to formulate a dimension- and operation-explicit comparison map, or a precise missing-map obligation. Do not infer it from shared pentachoron labels.'
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true')
    args=parser.parse_args();text=json.dumps(audit(),indent=2)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8')!=text:raise SystemExit('FAIL: stale atlas/seed crosswalk')
    else:
        DEST.parent.mkdir(parents=True,exist_ok=True);DEST.write_text(text,encoding='utf-8')
    print('PASS: 22 atlas claims retain exact statuses and source IDs; nine collection input hashes verified.')
    print('PASS: five absent catalogue entries are missing links, not contradictions; four promotion hostiles refused.')
    print('Boundary: source-identity correspondence only; no owner scientific replay, atlas rewrite or physical admission.')


if __name__=='__main__':main()
