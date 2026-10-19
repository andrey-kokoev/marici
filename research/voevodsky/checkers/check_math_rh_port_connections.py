"""Explicit port wiring audit of parent, math, compatibility and RH work nets.
This checks declared connection coverage, not completeness of all mathematics.
--record creates a new reviewed model; normal execution only validates it.
"""
from pathlib import Path
import argparse,copy,json
from hashlib import sha256
ROOT=Path(__file__).resolve().parents[3]
HOME='research/conjecture_net/contracts/'
PATHS={
 'parent':HOME+'common-foundations-conjecture-net.v1.json',
 'math':HOME+'mathematical-realization-conjecture-net.v1.json',
 'compatibility':HOME+'same-source-compatibility-conjecture-net.v1.json',
 'rh':HOME+'rh-realization-work-net.v1.json'}
MODEL=HOME+'math-rh-port-connections.v10.json'
OUT=ROOT/'research/voevodsky/results/math-rh-port-connections-v1.json'


def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8'))
def require(c,m):
    if not c:raise ValueError(m)
def build(nets):
    nodes=[];connections=[];external=[]
    for alias,c in nets.items():
        by={n['id']:n for n in c['conjectures']}
        for n in c['conjectures']:
            key=alias+':'+n['id'];ins=[]
            for dep in n['depends_on']:
                constructive=dep in n.get('required_verdicts',{})
                port='requires:'+dep;ins.append({'id':port,'type':'constructed_witness' if constructive else 'scoped_research_knowledge'})
                connections.append({'source':alias+':'+dep,'source_port':'witness' if constructive else 'knowledge',
                  'target':key,'target_port':port,
                  'relation':'required_constructed_input' if constructive else 'research_prerequisite',
                  'available':by[dep].get('verdict')=='constructed' if constructive else by[dep]['status']=='resolved',
                  'logical_implication_asserted':False})
            for req in n.get('requires',[]):
                port='external:'+req;ins.append({'id':port,'type':'reviewed_external_witness'})
                external.append({'target':key,'target_port':port,'obligation':req,'status':'open','available':False})
            nodes.append({'id':key,'status':n['status'],'verdict':n.get('verdict','open'),
              'inputs':ins,'outputs':[{'id':'knowledge','type':'scoped_research_knowledge'},
               {'id':'witness','type':'constructed_witness'},{'id':'counterexample','type':'scoped_rejection'}]})
    # Cross-net references were already present, but their receiving ports and
    # nonpromotion conditions were not explicit. These are contribution slots,
    # not extra prerequisite edges which would block bounded RH work.
    cross=[
      ('rh:rh-math-assembly','math:rh-mathematical-realization-example','bounded-rh-example','scoped_example_contribution'),
      ('rh:rh-cross-realization-assembly','compatibility:rh-same-source-compatibility-example','same-source-rh-example','scoped_example_contribution'),
      ('math:mathematical-realization-example-assembly','parent:mathematical-realization','bounded-math-examples','bounded_branch_contribution'),
      ('compatibility:same-source-compatibility-example-assembly','parent:same-source-cross-realization','bounded-comparisons','bounded_branch_contribution'),
      ('math:stagewise-mathematical-interface','rh:rh-stagewise-interface','general-interface-review','interface_instantiation_review'),
      ('compatibility:common-witness-comparison-interface','rh:same-source-continuation-comparison','general-common-witness-review','interface_instantiation_review')]
    indexed={n['id']:n for n in nodes}
    for src,dst,port,rel in cross:
        indexed[dst]['inputs'].append({'id':port,'type':'constructed_witness'})
        connections.append({'source':src,'source_port':'witness','target':dst,'target_port':port,
          'relation':rel,'available':indexed[src]['verdict']=='constructed',
          'logical_implication_asserted':False,'discharges_target':False,
          'does_not_block_local_research':rel=='interface_instantiation_review',
          'acceptance':'Target acceptance and overlap review still required; source success alone does not resolve target.'})
    # Explicitly audited substantive comparisons; no transitive success inferred.
    cells=[
      {'id':'energy-reader-to-Weil','from':['rh:retained-six-coordinate-energy'],'to':'rh:weil-form-comparison',
       'status':'not_established','reason':'Exact energy recovery supplies no arithmetic test map; direct extension rejected.',
       'control':'rh:direct-fourier-energy-is-weil'},
      {'id':'operations-to-positive-form','from':['rh:carrier-fourier-attachment','rh:six-step-fourier-transport'],'to':'rh:weil-form-comparison',
       'status':'candidate_rejected','reason':'Operation squares do not imply form equality; positive hidden energy is lost.',
       'control':'rh:current-source-weil-pullback'},
      {'id':'continuous-to-discrete','from':['rh:history-continuous-bridge'],'to':'rh:native-tick-is-fourier',
       'status':'candidate_rejected','reason':'Continuous generator agreement does not identify discrete ticks.',
       'control':'rh:native-tick-is-fourier'},
      {'id':'generic-to-Riemann-faithfulness','from':['rh:carrier-fourier-attachment'],'to':'rh:riemann-specialization',
       'status':'constructed_with_kernel','reason':'Specialization exists but rank drops from four to one; retained source is not the scalar analytic image.'},
      {'id':'channel-to-native-source','from':['rh:additive-lattice-fourier','rh:carrier-fourier-attachment'],'to':'rh:channel-carrier-source-map',
       'status':'open','reason':'A common source dictionary and composition witness remain required.'},
      {'id':'multichannel-to-one-dimensional','from':['rh:additive-lattice-fourier'],'to':'rh:one-dimensional-source-selection',
       'status':'constructed_for_pointed_axis_task','reason':'Explicit mark-covariant axis restriction with retained complement; no canonical unmarked or physical selection. Full heat through symmetric sum is rejected.',
       'control':'rh:symmetric-full-heat-selection'},
      {'id':'signed-to-positive','from':['rh:signed-weil-quotient'],'to':'rh:weil-form-comparison',
       'status':'not_established','reason':'Signed covariance and radical identification do not supply positive source-form equality.'},
      {'id':'math-to-same-source','from':['rh:rh-math-assembly'],'to':'rh:rh-cross-realization-assembly',
       'status':'open','reason':'Both continuation and form witnesses on the same source are additional required inputs.'}]
    return {'schema':'marici.math-rh-port-connections.v1','contracts':PATHS,
      'scope':'All declared local prerequisite and required-verdict inputs, listed cross-net contribution ports, and named RH comparison cells in these four contracts. Not all conceivable implications or internals of legacy/physics nets.',
      'nodes':nodes,'connections':connections,'external_obligations':external,'comparison_cells':cells,
      'all_logical_implications_established':False,
      'external_references':[
        {'contract':nets['rh']['baseline'],'role':'parallel legacy RH routes; no proof import; internal ports not audited here'},
        {'contract':'research/conjecture_net/contracts/programme-hierarchy.v17.json','role':'unchanged physics programme; internal ports not audited here'}]}


def validate(m,nets):
    expected=build(nets)
    require(m==expected,'model differs from declared wiring or reviewed comparison inventory')
    by={n['id']:n for n in m['nodes']};seen=set()
    for e in m['connections']:
        require(e['source'] in by and e['target'] in by,'unknown node')
        outs={p['id']:p['type'] for p in by[e['source']]['outputs']}
        ins={p['id']:p['type'] for p in by[e['target']]['inputs']}
        require(outs[e['source_port']]==ins[e['target_port']],'port type mismatch')
        key=e['target'],e['target_port'];require(key not in seen,'duplicate driver');seen.add(key)
        require(not e['logical_implication_asserted'],'unsupported logical implication')
        if e['source_port']=='witness' and e['available']:
            require(by[e['source']]['verdict']=='constructed','rejection/open node used as witness')
    for e in m['external_obligations']:seen.add((e['target'],e['target_port']))
    required={(n['id'],p['id']) for n in m['nodes'] for p in n['inputs']}
    require(seen==required,'unrecorded input port')
    r={n['id']:n for n in nets['rh']['conjectures']}
    require(r['retained-six-coordinate-energy']['verdict']=='constructed','energy result missing')
    require(r['direct-fourier-energy-is-weil']['verdict']=='rejected','rotor rejection lost')
    require({'retained-six-coordinate-energy','direct-fourier-energy-is-weil'}<=set(r['successor-form-candidate']['depends_on']),'successor ignores latest controls')
    require(r['current-source-weil-pullback']['verdict']=='rejected','earlier rejection overwritten')
    return len(required)


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--record',action='store_true');args=parser.parse_args()
    nets={k:load(p) for k,p in PATHS.items()};path=ROOT/MODEL
    if args.record:
        require(not path.exists(),'refusing to overwrite port model; use reviewed revision')
        path.write_text(json.dumps(build(nets),indent=2)+'\n',encoding='utf-8')
    m=load(MODEL);count=validate(m,nets)
    failures=[]
    for mode in ('missing-edge','wrong-port','rejection-as-proof','false-implication','duplicate-driver','missing-cross-link','lost-kernel-cell','false-completeness','lost-external-gate'):
        bad=copy.deepcopy(m)
        if mode=='missing-edge':bad['connections'].pop(0)
        elif mode=='wrong-port':bad['connections'][0]['source_port']='counterexample'
        elif mode=='rejection-as-proof':
            e=next(e for e in bad['connections'] if e['source']=='rh:direct-fourier-energy-is-weil');e['source_port']='witness';e['available']=True
        elif mode=='false-implication':bad['connections'][0]['logical_implication_asserted']=True
        elif mode=='duplicate-driver':bad['connections'].append(copy.deepcopy(bad['connections'][0]))
        elif mode=='missing-cross-link':bad['connections'].pop()
        elif mode=='lost-kernel-cell':bad['comparison_cells'].pop(3)
        elif mode=='false-completeness':bad['all_logical_implications_established']=True
        else:bad['external_obligations']=[]
        try:validate(bad,nets)
        except ValueError:failures.append(mode)
        else:raise AssertionError('corruption accepted: '+mode)
    # Freshly verify the two latest receipts, without rerunning their source suites.
    artifacts={a['id']:a for a in nets['rh']['artifacts']}
    for aid in ('energy-observer','rotor-weil-counterexample'):
        receipt=load(artifacts[aid]['receipt']);require(receipt['passed'],'receipt failed')
        for p,h in receipt['source_hashes'].items():require(sha256(Path(p).read_bytes()).hexdigest()==h,'receipt drift '+p)
    rh=nets['rh']['conjectures']
    result={'schema':'marici.math-rh-port-audit.v1','passed':True,
      'covered_nodes':len(m['nodes']),'covered_input_ports':count,'connections':len(m['connections']),
      'available_connections':sum(e['available'] for e in m['connections']),
      'cross_net_links':sum('discharges_target' in e for e in m['connections']),
      'external_open_obligations':len(m['external_obligations']),
      'reviewed_comparison_cells':len(m['comparison_cells']),
      'rh_counts':{v:sum(n['verdict']==v for n in rh) for v in ('constructed','rejected','open')},
      'corruptions_rejected':failures,'latest_receipt_hashes_verified':True,
      'scientific_suites_rerun':False,'all_mathematical_implications_proved':False,
      'coverage_scope':m['scope'],
      'source_sha256':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in [*PATHS.values(),MODEL,Path(__file__).relative_to(ROOT).as_posix()]}}
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))


if __name__=='__main__':main()
