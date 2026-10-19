"""Administrative research-direction validation; not evidence against Hodge."""
from pathlib import Path
from hashlib import sha256
import json

ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/conjecture_net/contracts/hodge-conjecture-net.v1.json'
POLICY='research/conjecture_net/contracts/hodge-refutation-direction.v1.json'
NOTE='research/voevodsky/hodge-refutation-direction-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-refutation-direction-v1.json'
SUPPORT=['scope-and-cycle-map','literature-boundary-audit','candidate-variety-and-class','packet-coherence-dictionary',
 'obstruction-construction','cohomology-descent','rational-survival','candidate-hodge-membership','candidate-obstruction-nonzero','generic-middle-hodge-kernel']
CONTROLS=['positive-and-rational-controls','bare-chain-closure-obstruction','uniform-weil-projector-annihilation','tautological-power-witness-search']
ACTIVE=['all-algebraic-cycles-annihilation','counterexample-assembly','fixed-candidate-nonalgebraicity','higher-coherence-counterexample-existence']
NEW=ACTIVE[2:]


def require(test,message):
    if not test:raise ValueError(message)


def load(name):return json.loads((ROOT/name).read_text(encoding='utf-8'))


def validate_direction(c,p=None,history=None):
    require(c.get('research_direction_contract')==POLICY,'missing mandatory refutation direction')
    p=load(POLICY) if p is None else p
    require(p['schema']=='marici.hodge-refutation-direction.v1' and p['confirmation_research_allowed'] is False,'confirmation research reactivated')
    require(p['positive_controls_required'] is True,'known algebraic falsifiers removed')
    require(p['active_refutation_nodes']==ACTIVE and p['retained_support_nodes']==SUPPORT and p['falsification_control_nodes']==CONTROLS,'refutation role inventory changed')
    prior_path='research/voevodsky/hodge-history/iteration-51/work-net.json'
    require(p['historical_snapshot']==prior_path,'direction history rebound')
    history=load(prior_path) if history is None else history
    pins=load('research/voevodsky/inputs/hodge-net-source-pins.v54.json')
    require(sha256((ROOT/prior_path).read_bytes()).hexdigest()==pins['source_sha256'][CONTRACT],'direction history digest changed')
    old={n['id']:n for n in history['conjectures']};by={n['id']:n for n in c['conjectures']}
    require(len(by)==len(c['conjectures']) and set(by)==set(old)|set(NEW),'direction node coverage')
    dismissed=p['dismissed_construction_nodes']
    expected=set(old)-set(SUPPORT)-set(CONTROLS)-set(ACTIVE)
    require(len(dismissed)==len(set(dismissed))==52 and set(dismissed)==expected,'dismissal inventory incomplete')
    require(set(SUPPORT)|set(CONTROLS)|set(ACTIVE)|set(dismissed)==set(by),'unclassified conjecture')
    for identifier,n in old.items():
        for key in ('status','verdict','outcome','evidence','resolution_kind'):
            require(by[identifier].get(key)==n.get(key),'dismissal is not mathematical rejection: '+identifier)
    for identifier in ACTIVE[:2]:
        for key in ('statement','acceptance','falsifier','depends_on','required_verdicts'):
            require(by[identifier][key]==old[identifier][key],'universal refutation gate weakened: '+identifier)
    require(c['scope']==history['scope'] and c['research_hypothesis']==history['research_hypothesis'],'operator conjecture or fixed target substituted')
    for identifier in dismissed:
        require(by[identifier].get('active_research',False) is False,'dismissed construction reactivated: '+identifier)
    w=by['algebraic-witness-search']
    require(w.get('research_disposition')=='dismissed_by_operator' and w.get('active_research') is False,'witness-search not dismissed')
    for identifier in NEW:
        require(by[identifier]==p['additional_hypotheses'][identifier],'refutation hypothesis changed or promoted')
        require(by[identifier]['aim']=='refute_rational_Hodge' and by[identifier]['status']=='open' and by[identifier]['evidence']==[],'hypothesis registration promoted to proof')
    require(c['classical_conjecture'].get('research_role')=='refutation_target_not_confirmation_task','classical conjecture made confirmation task')
    require(p['first_unresolved_proof_obligation']=='all-algebraic-cycles-annihilation','universal-over-cycles gap displaced')
    require(c['frontier']['entry_nodes']==['all-algebraic-cycles-annihilation']+NEW and c['frontier']['recommended_start']=='all-algebraic-cycles-annihilation','dismissed or misdirected frontier')
    require(c['objective']['target']=='counterexample-assembly' and c['objective']['outcome'] is None,'counterexample objective replaced')
    return {'active_refutation_nodes':ACTIVE,'dismissed_construction_nodes':dismissed,'active_refutation_count':4,
        'dismissed_construction_count':52,'positive_controls_retained':True,
        'first_unresolved_proof_obligation':'all-algebraic-cycles-annihilation',
        'administrative_change_is_mathematical_evidence':False,'inventory_exhausts_possible_conjectures':False}


def source_paths():
    return {POLICY,NOTE,Path(__file__).relative_to(ROOT).as_posix(),
        'research/voevodsky/checkers/test_hodge_refutation_direction.py'}


def report():
    c=load(CONTRACT);result=validate_direction(c)
    return {'schema':'marici.hodge-refutation-direction-result.v1','passed':True,'verification_level':'Direction, inventory, preserved historical verdicts and honest open conjectures only; no mathematical proof.',
        **result,'Hodge_proved':False,'Hodge_refuted':False,
        'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(source_paths()|{CONTRACT})}}


if __name__=='__main__':
    r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in r.items() if k not in ('source_sha256','dismissed_construction_nodes')},indent=2))
