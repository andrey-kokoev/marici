"""C12 final scoped mathematical review with fresh finite closure checks.

Finite hypotheses and scalar margins are checked here; the analytic argument is
reviewed in Markdown, not represented as a machine-formalized theorem.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import check_pentachoron_threshold_kernel as kernel

HOME=Path(__file__).resolve().parent
ROOT=HOME.parents[2]
NOTE=HOME/'PENTACHORON-THRESHOLD-REVIEW.md'
RESULT=HOME/'results/pentachoron-threshold-review.v1.json'
SOURCE=ROOT/'research/scattering/high-energy/pentachoron_autonomous_contact_note.md'
PARENT=HOME/'contracts/low-energy-scattering-conjectures.v5.json'


def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()


def build():
    fresh=kernel.build() # Includes fresh exact ground replay and inverse checks.
    assert json.loads(kernel.RESULT.read_text(encoding='utf-8'))==fresh,'stale kernel receipt'
    assert fresh['full_threshold_nullity']==2 and fresh['dark_reduced_threshold_block_invertible'] is True
    prior=json.loads((HOME/'contracts/pentachoron-threshold-attempt1.v1.json').read_text(encoding='utf-8'))
    assert prior['initial_total_effort_units']==2 and prior['effort_units_used']==prior['remaining_effort_units']==1
    assert prior['automatic_renewal_allowed'] is False and prior['high_energy_protocol_units_used']==0
    for path,h in prior['source_sha256'].items():assert sha(ROOT/path)==h,'stale attempt-1 evidence: '+path
    parent=json.loads(PARENT.read_text(encoding='utf-8'));c12=parent['conjectures'][-1]
    assert c12['label']=='C12' and c12['status']=='open'
    # Rational Neumann margin: eta<1/4 implies 1/(1-eta)<=4/3<2.
    assert 1/(1-Q(1,4))==Q(4,3) and Q(4,3)<2
    paths={NOTE,SOURCE,PARENT,Path(__file__),Path(kernel.__file__),kernel.RESULT,
           HOME/'contracts/pentachoron-threshold-attempt1.v1.json'}
    paths.update(ROOT/p for p in fresh['source_sha256'])
    return {'schema':'marici.scattering.low-energy-pentachoron-threshold-review.v1','status':'pass',
            'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in sorted(paths)},
            'reviewed_proposition':c12['id'],'statement':c12['statement'],
            'quantifiers':c12['quantifiers'],'falsifier':c12['falsifier'],
            'scope_verdict':'established','finite_support_freshly_replayed':True,
            'analytic_review':{'source_junction_signs':'checked against full boundary system',
                'kernel':'exactly the two known dark directions',
                'reducing_complement':'fixed N, dimension 38',
                'uniform_inverse':'Neumann bound with a*defect<1/4',
                'flux':'common ground v=2k cancels the preparation/readout factors',
                'packet':'energy measure, reducing orthogonal sectors, squared O(k) bound',
                'machine_formalized':False,'external_peer_review_claimed':False},
            'constants':{'a':'||N0^(-1)||','delta':'smallest positive eigenvalue of H_O-theta I',
                'L':'3+2/sqrt(delta)','k0':'min(1/2,sqrt(delta)/2,1/(4*a*L))','C':'4*a'},
            'protocol':{'initial_effort_units':2,'used_effort_units':2,'remaining_effort_units':0,'renewed':False},
            'physical_outcomes_admitted':False,'programme_coverage_complete':False,
            'high_energy_protocol_units_used':0}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');a=p.parse_args();r=build()
    if a.check:assert json.loads(RESULT.read_text(encoding='utf-8'))==r,'stale C12 review receipt'
    else:RESULT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:r[k] for k in ('status','scope_verdict','finite_support_freshly_replayed','protocol','physical_outcomes_admitted')}))


if __name__=='__main__':main()
