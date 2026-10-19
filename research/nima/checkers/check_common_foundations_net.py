"""Structural validation of the new parent net, not verification of its conjecture."""
import argparse
import copy
import json
from hashlib import sha256
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[3]
HOME=ROOT/'research/nima'
CONTRACT=ROOT/'research/conjecture_net/contracts/common-foundations-conjecture-net.v1.json'
sys.path.insert(0,str(ROOT/'research/conjecture_net'))
from graph_metrics import MetricAction,MetricGraph


def require(ok,message):
    if not ok:raise ValueError(message)


def sha(p):return sha256(p.read_bytes()).hexdigest()


def sources(c):
    paths=({x['contract'] for x in c['branch_attachments']} | {x['path'] for x in c['candidate_evidence']}
            | {x['contract'] for x in c['branch_nets']} | {c['rh_work_net']['contract']})
    for b in c['branch_nets']:
        sub=json.loads((ROOT/b['contract']).read_text())
        if sub.get('comparison_interface'):paths.add(sub['comparison_interface'])
        for a in sub.get('artifacts',[]):paths.update(a[k] for k in ('note','checker','receipt'))
    return paths


def validate_subnode(n,sub):
    require(n['outcome'] is None and n['acceptance'] and n['falsifier'],'subnet scope/outcome')
    if n['status']=='open':
        require(n.get('verdict','open')=='open','unreviewed open verdict')
        return
    # Permit only the reviewed definition, not arbitrary branch/example promotion.
    require(sub['id']=='marici.same-source-compatibility.v1' and
            n['id']=='common-witness-comparison-interface' and n['status']=='resolved' and
            n['verdict']=='constructed' and n['resolution_kind']=='bounded_interface_definition' and
            n['evidence']==['common-witness-interface'] and
            n.get('physical_realization_admitted',False) is False,'unreviewed subnet resolution')
    require(sub['comparison_interface']=='research/conjecture_net/contracts/common-witness-comparison-interface.v1.json','definition binding')
    a=next(a for a in sub['artifacts'] if a['id']=='common-witness-interface')
    require(a['checker']=='research/voevodsky/checkers/check_common_witness_comparison_interface.py' and
            a['receipt']=='research/voevodsky/results/common-witness-comparison-interface-v1.json','definition evidence')
    r=json.loads((ROOT/a['receipt']).read_text());s=json.loads((ROOT/sub['comparison_interface']).read_text())
    require(n['scope']==s['scope'] and r['passed'] and r['resolution_kind']=='bounded_interface_definition' and
            r['definition']==sub['comparison_interface'] and not any(s['boundaries'].values()) and
            r['physical_realization_admitted'] is False and r['universal_compatibility_proved'] is False and
            r['WG_and_RH_sources_identified'] is False,'definition promoted')
    for p,digest in r['source_sha256'].items():
        require((ROOT/p).resolve().is_relative_to(ROOT) and sha(ROOT/p)==digest,'definition evidence drift: '+p)


def validate(c,pins):
    require(c['id']=='marici.common-foundations.v1','wrong parent id')
    require(c['root']['id']==c['objective']['target']=='common-foundations','wrong root')
    require(c['root']['outcome'] is None and c['objective']['outcome'] is None,'root promotion')
    require(c['root']['status']=='conjectured_requires_formulation','formulation promoted')
    require(all(v is False for v in c['boundary'].values()) and c['imports']==[],'evidence promotion')
    nodes=c['conjectures'];ids={n['id'] for n in nodes}
    require(len(ids)==len(nodes)==9,'node set changed')
    for n in nodes:
        require(n['status']=='open' and n['outcome'] is None,'child promotion')
        require(n['acceptance'] and n['rivals'] and n['falsifier'],'missing risky test/scope')
    graph=MetricGraph(tuple(MetricAction(n['id'],frozenset(n['depends_on']),frozenset(n['requires']),terminal=n['id']=='common-foundations') for n in nodes),frozenset(c['interfaces']))
    graph.validate()
    by={n['id']:n for n in nodes}
    require(set(by['same-source-cross-realization']['depends_on'])=={'mathematical-realization','physical-realization','uf-and-foundational-recovery'},'same-source bridge bypass')
    require(by['common-foundations']['requires']==['reviewed-root-assembly'],'automatic root assembly')
    require(c['interfaces']==[],'unreviewed assembly interface')
    require(c['frontier']['next_node']=='formulation-and-quantifiers','wrong initial frontier')
    require(set(pins['source_sha256'])==sources(c),'pin set mismatch')
    for name,expected in pins['source_sha256'].items():
        p=(ROOT/name).resolve()
        require(p.is_relative_to(ROOT) and sha(p)==expected,'source drift: '+name)
    attachments={a['id']:a for a in c['branch_attachments']}
    require(set(attachments)=={'existing-physics-programme','rh-domain-test'},'branch set changed')
    physics=attachments['existing-physics-programme'];rh=attachments['rh-domain-test']
    require(physics['parent_nodes']==['physical-realization'] and set(rh['parent_nodes'])=={'mathematical-realization','same-source-cross-realization'},'branch misattachment')
    for a in attachments.values():
        require(a['proof_bearing'] is False and a['discharges_parent'] is False and a['source_outcome'] is None,'branch evidence promotion')
    old=json.loads((ROOT/physics['contract']).read_text())
    require(old['root']['id']==physics['source_root']=='relational-carrier-physical-explanation' and old['root']['outcome'] is None,'physics root altered')
    rh_source=json.loads((ROOT/rh['contract']).read_text())
    require(rh_source['claim_boundary']['rh_implication'] is False,'RH status promoted')
    branches={b['node']:b for b in c['branch_nets']}
    require(set(branches)=={'mathematical-realization','same-source-cross-realization'},'branch net set')
    shared_rh=[]
    for node,b in branches.items():
        require(b['proof_bearing'] is False,'branch net promoted')
        sub=json.loads((ROOT/b['contract']).read_text())
        require(sub['parent']['node']==node and sub['parent']['contract']==CONTRACT.relative_to(ROOT).as_posix(),'subnet parent mismatch')
        require(sub['objective']['outcome'] is None and sub['imports']==[] and all(v is False for v in sub['boundary'].values()),'subnet promotion')
        MetricGraph(tuple(MetricAction(n['id'],frozenset(n['depends_on'])) for n in sub['conjectures'])).validate()
        subids={n['id'] for n in sub['conjectures']}
        require(sub['objective']['target'] in subids,'subnet target missing')
        for n in sub['conjectures']:
            validate_subnode(n,sub)
        for a in sub['example_attachments']:
            require(a['node'] in subids and a['proof_bearing'] is False and a['discharges_parent'] is False and a['outcome'] is None,'example promotion')
        r=next(a for a in sub['example_attachments'] if a['id']=='shared-rh-example')
        require(r['role']==('mathematical_realization' if node=='mathematical-realization' else 'same_source_compatibility'),'RH role conflation')
        shared_rh.append(r['contract'])
    require(shared_rh==[rh['contract'],rh['contract']],'RH examples refer to different revisions')
    for e in c['candidate_evidence']:
        require(set(e['nodes'])<=ids and e['scope'],'untyped evidence attachment')
    frontier=[n['id'] for n in nodes if not n['depends_on'] and not n['requires']]
    require(frontier==['formulation-and-quantifiers'],'frontier changed')
    return frontier


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--pin',action='store_true');args=parser.parse_args()
    c=json.loads(CONTRACT.read_text());pinpath=ROOT/c['source_pins']
    if args.pin:
        require(not pinpath.exists(),'refusing implicit source re-pin')
        pinpath.write_text(json.dumps({'schema':'marici.common-foundations.source-pins.v1','source_sha256':{n:sha(ROOT/n) for n in sorted(sources(c))}},indent=2,sort_keys=True)+'\n',encoding='utf-8')
    pins=json.loads(pinpath.read_text());frontier=validate(c,pins)
    hostiles=[]
    for name in ('root-promotion','child-promotion','cycle','unknown-dependency','proof-import','physics-attachment','same-source-bypass','automatic-assembly','rh-single-role','stale-pin'):
        b=copy.deepcopy(c);p=copy.deepcopy(pins)
        if name=='root-promotion':b['root']['outcome']='++'
        elif name=='child-promotion':b['conjectures'][0]['outcome']='++'
        elif name=='cycle':b['conjectures'][0]['depends_on']=['common-foundations']
        elif name=='unknown-dependency':b['conjectures'][0]['depends_on']=['invented']
        elif name=='proof-import':b['branch_attachments'][0]['proof_bearing']=True
        elif name=='physics-attachment':b['branch_attachments'][0]['parent_nodes']=['mathematical-realization']
        elif name=='same-source-bypass':b['conjectures'][6]['depends_on']=['physical-realization']
        elif name=='automatic-assembly':b['conjectures'][-1]['requires']=[]
        elif name=='rh-single-role':b['branch_attachments'][1]['parent_nodes']=['mathematical-realization']
        else:p['source_sha256'][next(iter(p['source_sha256']))]='0'*64
        try:validate(b,p)
        except ValueError:hostiles.append(name)
        else:raise AssertionError('hostile accepted: '+name)
    sub=json.loads((ROOT/'research/conjecture_net/contracts/same-source-compatibility-conjecture-net.v1.json').read_text())
    definition=next(n for n in sub['conjectures'] if n['id']=='common-witness-comparison-interface')
    if definition['status']=='resolved':
        for mode in ('definition-outcome-promotion','example-as-definition','definition-as-physical-proof'):
            bad=copy.deepcopy(definition)
            if mode=='definition-outcome-promotion':bad['outcome']='++'
            elif mode=='example-as-definition':bad['id']='physical-pilot-comparison-example'
            else:bad['physical_realization_admitted']=True
            try:validate_subnode(bad,sub)
            except ValueError:hostiles.append(mode)
            else:raise AssertionError('hostile accepted: '+mode)
    registry=json.loads((ROOT/'research/conjecture_net/registry.json').read_text())
    entries=[n for n in registry['nets'] if n['id']==c['id']]
    require(len(entries)==1 and entries[0]['contract']==CONTRACT.relative_to(ROOT).as_posix(),'registry attachment missing/duplicated')
    for b in c['branch_nets']:
        require(sum(n['contract']==b['contract'] for n in registry['nets'])==1,'branch registry attachment missing/duplicated')
    result={'schema':'marici.common-foundations.net-validation.v1','status':'pass','validation_only':True,
            'node_count':len(c['conjectures']),'source_pin_count':len(sources(c)),
            'frontier':frontier,'rejected_hostiles':hostiles,'root_outcome':None,
            'physics_child_preserved':True,'rh_domain_test_not_proof_import':True,'rh_attached_in_both_branch_nets':True,
            'contract_sha256':sha(CONTRACT),'pins_sha256':sha(pinpath),'checker_sha256':sha(Path(__file__)),
            'source_suites_rerun':False,'universal_conjecture_verified':False}
    out=HOME/'results/common-foundations-net-validation.json'
    out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
