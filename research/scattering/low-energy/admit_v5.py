"""Explicit v5/C12 admission; preserves v4 and v1 planning records.

--check verifies the deterministic successor and planning extension. No scientific
outcome is admitted. C12 forecasts are subjective bounded-attempt estimates.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[3]
HOME=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'research/conjecture_net'))
import plan_low_energy as adapter

OLD='research/scattering/low-energy/contracts/low-energy-scattering-conjectures.v4.json'
NEW='research/scattering/low-energy/contracts/low-energy-scattering-conjectures.v5.json'
DRAFT='research/scattering/low-energy/contracts/pentachoron-bright-threshold-draft.v1.json'
PLANNING='research/conjecture_net/contracts/low-energy-test-planning.v2.json'
CARDS='research/conjecture_net/contracts/low-energy-action-cards.v2.json'
ID='pentachoron-bright-threshold-regularity'
ACTION=('Replay the exact ground certificate. Construct the positive square root Q of H_O-theta I from exact spectral data; form the full threshold boundary block and separate its two automatic dark null directions. Test remaining kernel vectors for a nonzero bright ground lead component, distinguishing invisible/core kernels. If regular, prove a uniform small-k expansion and the stated norm/packet bounds; otherwise exhibit an exact scoped counterexample. Stop after two focused assistant effort units, or earlier at proof/counterexample. An unresolved algebraic sign, domain or error bound is inconclusive, never acceptance. No numerical scan alone decides C12.')


def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()


def contract():
    assert sha(OLD)=='6ec12aad58e77b9c6151e1f667f75349dda92bd7bcffb69e89f5d800751832eb','frozen v4 contract changed'
    old=load(OLD);d=load(DRAFT);new=copy.deepcopy(old)
    new.update(schema='marici.scattering.low-energy-conjectures.v5',supersedes=OLD,
               historical_proposition_contract=OLD,
               next_test='Use the shared live workbench recommendation; C12 is open and independent of the disposed v4 tests. Programme coverage remains incomplete.')
    new['models']['pentachoron_contact']={k:d[k] for k in ('source_model','fixture','ground_energy','first_excitation_gap','input_space','dark_space','bright_space','observable')}
    new['models']['pentachoron_contact'].update(exact_matrix_receipt_sha256=d['exact_matrix_receipt_sha256'],ground_certificate=d['ground_certificate'])
    node={'id':ID,'label':'C12','model':'pentachoron_contact','status':'open',
          'statement':d['statement'],'quantifiers':d['statement'],
          'falsifier':d['falsifier'],'next_action':ACTION,
          'scope':'Fixed 20+20 contact, below its own first excitation; dark sector remains transparent. Bright regularity is not implied by the exact ground certificate, C1/C4, or numerical scans.',
          'sources':['research/scattering/high-energy/pentachoron_autonomous_contact_bundle.zip',
                     'research/scattering/high-energy/pentachoron_autonomous_contact_note.md',
                     'research/scattering/low-energy/PENTACHORON-GROUND-SECTOR.md',DRAFT,d['ground_certificate']],
          'prerequisite_certificates':[d['ground_certificate']],
          'conditional_packet_consequence':d['conditional_packet_consequence'],
          'first_test':d['first_test']}
    new['conjectures'].append(node)
    new['admission']={'draft':DRAFT,'draft_sha256':sha(DRAFT),'frozen_v4_sha256':sha(OLD),
                      'new_open_propositions':['C12'],'existing_proposition_outcomes_changed':False,
                      'new_proof_or_physical_outcome_admitted':False,
                      'reason':'Coverage audit exposed a distinct contact branch; exact dark transparency corrects the target to bright regularity.'}
    return new


def planning(new):
    model=copy.deepcopy(load('research/conjecture_net/contracts/low-energy-test-planning.v1.json'))
    cards=copy.deepcopy(load('research/conjecture_net/contracts/low-energy-action-cards.v1.json'))
    source_hash=sha(NEW)
    paths={'low-energy':NEW}
    initial=adapter.planning.initial(adapter.adapt(new),paths)
    row=next(r for r in initial['conjectures'] if r['id']=='low-energy:'+ID)
    node=new['conjectures'][-1]
    row['test'].update(protocol_status='specified',next_action=ACTION)
    basis='Assistant elicitation at v5/C12 admission; subjective forecast for one bounded two-effort-unit attempt, not theorem probability or measured calibration.'
    row['probability'].update(status='estimated',values={'accepted':.4,'rejected':.2,'inconclusive':.4},
        conditioning='Exact ground certificate available; no bright regularity assumed.',
        uncertainty='Positive square-root algebra and invisible kernels can defeat the bounded attempt; dark transparency provides no positive forecast evidence.',basis=basis)
    row['test_cost'].update(status='estimated',assistant_effort_units=2,basis=basis)
    model['conjectures'].append(row);model['contracts']=paths;model['source_sha256']={NEW:source_hash}
    model['extension']={'supersedes':'research/conjecture_net/contracts/low-energy-test-planning.v1.json',
                        'scope':'C12 admission only; all eleven historical rows preserved verbatim; no test cycle executed by admission.'}
    cards['source_sha256']={NEW:source_hash}
    cards['cards'].append({'id':row['id'],'first_action':ACTION,'acceptance':row['test']['acceptance'],
        'falsifier':node['falsifier'],'reuse_sources':node['sources'],
        'deliverable':'Uniform analytic proof with exact source binding, exact counterexample, or explicit inconclusive report.',
        'reuse_policy':'Preserve the source fixture and all closed/core coordinates. Remove known dark null directions, not actual bright resonances.',
        'stop_rule':ACTION,'review_promotion':'Planning is not proof, task claim, physical admission or permission to consume the paused high-energy protocol.'})
    return model,cards


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args()
    new=contract();text=json.dumps(new,indent=2)+'\n'
    if a.check:assert (ROOT/NEW).read_text(encoding='utf-8')==text,'v5 differs from explicit admission'
    else:
        if (ROOT/NEW).exists():assert load(NEW)==new,'refusing to overwrite changed successor'
        (ROOT/NEW).write_text(text,encoding='utf-8')
    model,cards=planning(new)
    for path,value in ((PLANNING,model),(CARDS,cards)):
        if a.check:assert load(path)==value,'planning differs from explicit admission: '+path
        else:
            if (ROOT/path).exists():assert load(path)==value,'refusing to overwrite edited planning extension'
            (ROOT/path).write_text(json.dumps(value,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','propositions':12,'new_open':['C12'],'historical_outcomes_changed':False}))


if __name__=='__main__':main()
