"""Audit and freeze the connected successor without changing its completed parent."""
from pathlib import Path
import argparse, copy, hashlib, json
ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/strominger/contracts/native-query-physical-realization-net.v4.json'
def require(ok,msg):
    if not ok:raise ValueError(msg)
def path(s):
    p=(ROOT/s).resolve();require(p.is_relative_to(ROOT),'Path outside repository');return p
def load(s):return json.loads(path(s).read_text(encoding='utf-8'))
def digest(s):return hashlib.sha256(path(s).read_bytes()).hexdigest()
def validate(net):
    nodes={n['id']:n for n in net['nodes']}
    require(len(nodes)==len(net['nodes']),'Duplicate nodes')
    require(net['objective']=={'target':'source-authorized-physical-recording','status':'open','physical_validation':False},'Physical root must remain open')
    require(net['publication']=='owner_local_only','No graph publication authority')
    for key,value in net['semantics'].items():
        require(value==(key=='dependencies_are_research_links_not_proof_implications'),'Scope guard changed: '+key)
    parent=net['parent'];p=load(parent['contract'])
    require(parent['imports_proof'] is False and parent['mutates_parent'] is False,'Parent authority')
    require(parent['revision']==p['revision']==27 and p['objective']['status']=='completed','Completed parent changed')
    require(set(parent['nodes'])<={n['id'] for n in p['nodes']},'Unknown parent node')
    artifacts=net['artifacts']
    for a in artifacts.values():
        require(set(a['supports'])<=nodes.keys(),'Unknown support')
        for s in a['paths']+a['checks']+a['receipts']:require(path(s).is_file(),'Missing '+s)
        for s in a['receipts']:require(load(s)['status']=='pass','Failed evidence receipt '+s)
    expected_rejections={'task-declaration-selects-response','query-covariance-selects-pairing',
                         'transport-isometry-selects-general-pairing','reversible-recording-implies-isometry','passive-linear-oscillator-implementation'}
    for n in nodes.values():
        require(n['status'] in ('open','resolved'),'Invalid status')
        require(set(n['depends_on'])<=nodes.keys(),'Unknown dependency')
        require(set(n['evidence'])<=artifacts.keys(),'Unknown evidence')
        for key in ('statement','scope','falsifier'):require(bool(n[key]),'Missing '+key)
        if n['status']=='open':
            require(n['verdict']=='open' and n.get('next_action') and n.get('deliverable'),'Open gate missing action')
        else:
            require(n['verdict'] in ('constructed','rejected','declared'),'Invalid verdict')
            require(any(n['id'] in artifacts[e]['supports'] for e in n['evidence']),'Unsupported resolved node')
    require({n['id'] for n in nodes.values() if n['verdict']=='rejected'}==expected_rejections,'Rejections changed')
    for key in ('conditional-recording-orthogonality','conditional-joint-pairing-classification'):
        require(nodes[key].get('conditional') is True and len(nodes[key].get('premises',[]))>=4,'Conditional premises erased')
    require(nodes['native-controlled-recorder']['verdict']=='constructed','Native theorem disposition')
    visited=set();active=set()
    def visit(k):
        require(k not in active,'Cycle')
        if k in visited:return
        active.add(k)
        for d in nodes[k]['depends_on']:visit(d)
        active.remove(k);visited.add(k)
    visit(net['objective']['target']);require(visited==set(nodes),'Disconnected nodes')
    actionable=[k for k,n in nodes.items() if n['status']=='open' and all(nodes[d]['status']=='resolved' for d in n['depends_on'])]
    require(net['frontier']==actionable==['freeze-realization-equivalence','behavioural-minimality','freeze-physical-model'],'Wrong actionable frontier')
    require(net['revision']==4,'Wrong revision')
    typing=net['task_typing']
    specs=set(typing['specification_gates']); proofs=set(typing['proof_obligations']); assemblies=set(typing['assembly_objectives'])
    require(not(specs & proofs or specs & assemblies or proofs & assemblies),'Task kinds overlap')
    require({k for k,n in nodes.items() if n['status']=='open'} <= specs|proofs|assemblies,'Open task typing incomplete')
    require((specs|proofs|assemblies)-{k for k,n in nodes.items() if n['status']=='open'}=={'freeze-source-fragment','audit-named-physical-candidate'},'Unexpected completed task')
    for k in ('freeze-source-fragment','audit-named-physical-candidate'):
        require(nodes[k]['status']=='resolved' and nodes[k]['verdict']=='declared' and path(nodes[k]['completed_deliverable']).is_file(),'Specification completion unsupported')
    require(specs=={'freeze-source-fragment','freeze-realization-equivalence','audit-named-physical-candidate','freeze-physical-model','freeze-comparison-witness-types'},'Missing specification gate')
    for key in ('specification_gate_is_mathematical_theorem','audit_completion_authorizes_missing_operations','diagram_boundary_is_complete_witness_type'):
        require(typing[key] is False,'Specification promoted to theorem')
    require(set(actionable)<=specs|{'behavioural-minimality'},'Proof attempted before specification')
    require(nodes['behavioural-minimality']['depends_on']==['freeze-source-fragment'],'Predictive-state task must use frozen language')
    require('behavioural-minimality' in nodes['mathematical-realization-moduli']['depends_on'],'Dimension boundary omitted')
    require({'freeze-source-fragment','freeze-realization-equivalence'}<=set(nodes['mathematical-realization-moduli']['depends_on']),'Output A lacks definitions')
    require(nodes['freeze-physical-model']['depends_on']==['audit-named-physical-candidate','passive-linear-oscillator-implementation'],'Candidate obstruction bypassed')
    for k in proofs-{'mathematical-realization-moduli','tetrahedral-realization-coherence','behavioural-minimality'}:
        require('freeze-comparison-witness-types' in nodes[k]['depends_on'],'Untyped proof obligation')
    audit=net['candidate_audit']
    require(audit['accepted_physical_model'] is False and audit['permitted_added_primitives']==[] and audit['partial_contract_closes_model_gate'] is False,'Candidate authority inflated')
    require(len(audit['required_audit_fields'])==8 and all(path(s).is_file() for s in audit['paths']),'Unbounded candidate audit')
    certificate=load('research/strominger/results/native-fragment-and-oscillator-audit/verification.json')
    require(certificate['pulse_direction_rank']==6 and certificate['target_triangle_minus_identity_rank']==16 and certificate['physical_model_accepted'] is False,'Scoped obstruction evidence')
    require(net['prior_clues']['phase_backreaction_admitted'] is False and net['prior_clues']['multiparticle_encoding_constructed'] is False,'Prior lead promoted to implementation')
    require(net['artifacts']['representation-priors']['receipts']==[] and net['artifacts']['representation-priors']['supports']==[],'Search notes promoted to fresh evidence')
    previous=load(net['previous_contract'])
    for old in previous['nodes']:
        if old['status']=='resolved':require(nodes[old['id']]==old,'Historical verdict or scope changed')
    require(net['two_outputs']['A']['node']=='mathematical-realization-moduli' and net['two_outputs']['A']['physical_authority_claimed'] is False,'Output A typing')
    require(net['two_outputs']['B']['node']=='physical-protocol-compiler' and net['two_outputs']['B']['model_gate']=='freeze-physical-model','Output B typing')
    require(net['two_outputs']['B']['model_selected'] is False and net['two_outputs']['B']['permitted_model_enlargement_after_failure'] is False,'Model authority')
    t=net['tetrahedron']
    require(t['edges']=={'a':'S->N','b':'N->P','c':'P->R','d':'S->P','e':'N->R','f':'S->R'},'Tetrahedral edge typing')
    cells={'SNP':('face-source-native-protocol','alpha: b a => d'),'SNR':('face-source-native-realization','beta: e a => f'),'NPR':('face-native-protocol-realization','gamma: c b => e'),'SPR':('face-source-protocol-realization','delta: c d => f')}
    require(set(t['faces'])==set(cells),'Missing face')
    for face,(node,cell) in cells.items():
        require(t['faces'][face]=={'node':node,'cell':cell} and nodes[node]['status']=='open','Face promoted or mistyped')
    require(t['coherence']=='(c whisker alpha);delta = (gamma whisker a);beta, from c b a to f','Wrong pasting boundary')
    require(set(nodes[t['coherence_node']]['depends_on'])=={x[0] for x in cells.values()},'Higher coherence missing face')
    require(t['faces_already_constructed'] is False and t['tetrahedron_already_constructed'] is False,'No new coherence theorem')
    r=load(artifacts['native-recorder']['receipts'][0])
    require(r['positive_exit']==0 and r['negative_exit']==42 and r['ignore_interfaces'] and r['stable_inputs'],'Missing fresh native proof evidence')
    module=path('research/strominger/agda/NativeQueryControlledRecorder.agda')
    bound=[v for k,v in r['source_sha256'].items() if Path(k).resolve()==module]
    require(bound==[hashlib.sha256(module.read_bytes()).hexdigest()],'Native recorder source drift')
    pointer=load(net['pointer'])
    require(pointer['contract']==CONTRACT and pointer['id']==net['id'] and pointer['packet']==net['packet'] and pointer['publication']==net['publication'],'Pointer mismatch')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--freeze',action='store_true');args=parser.parse_args()
    net=load(CONTRACT);validate(net)
    controls=[]
    mutations=[('physical-closure',lambda n:n['objective'].update(status='completed')),
               ('native-isometry',lambda n:n['semantics'].update(reversibility_implies_isometry=True)),
               ('conditional-erasure',lambda n:next(x for x in n['nodes'] if x['id']=='conditional-recording-orthogonality').update(conditional=False)),
               ('parent-mutation',lambda n:n['parent'].update(mutates_parent=True)),
               ('false-frontier',lambda n:n.update(frontier=[])),
               ('erased-face',lambda n:n['tetrahedron']['faces'].pop('SPR')),
               ('wrong-pasting',lambda n:n['tetrahedron'].update(coherence='faces imply coherence')),
               ('unfrozen-model',lambda n:n['two_outputs']['B'].update(model_selected=True)),
               ('pairing-as-physics',lambda n:n['two_outputs']['A'].update(physical_authority_claimed=True)),
               ('specification-as-theorem',lambda n:n['task_typing'].update(specification_gate_is_mathematical_theorem=True)),
               ('invented-coupling',lambda n:n['candidate_audit'].update(permitted_added_primitives=['controlled-reflection'])),
               ('untyped-face',lambda n:next(x for x in n['nodes'] if x['id']=='face-native-protocol-realization')['depends_on'].remove('freeze-comparison-witness-types')),
               ('phase-model-import',lambda n:n['prior_clues'].update(phase_backreaction_admitted=True)),
               ('unproved-fock-encoding',lambda n:n['prior_clues'].update(multiparticle_encoding_constructed=True)),
               ('erased-linear-obstruction',lambda n:next(x for x in n['nodes'] if x['id']=='passive-linear-oscillator-implementation').update(verdict='constructed'))]
    for name,mutate in mutations:
        bad=copy.deepcopy(net);mutate(bad)
        try:validate(bad)
        except ValueError:controls.append(name)
        else:raise ValueError('Corruption accepted: '+name)
    previous=load(net['previous_contract'])
    names={CONTRACT,net['packet'],net['pointer'],net['validator'],net['parent']['contract'],net['previous_contract'],previous['pins'],previous['packet'],previous['pointer'],previous['validator'],previous['audit_receipt']} 
    for a in net['artifacts'].values():names.update(a['paths']+a['receipts']+a['checks'])
    pins={'schema':'marici.owner-local-net-pins.v1','net':net['id'],'sha256':{s:digest(s) for s in sorted(names)}}
    pinpath=path(net['pins'])
    if args.freeze and not pinpath.exists():
        with pinpath.open('x',encoding='utf-8') as stream:json.dump(pins,stream,indent=2);stream.write('\n')
    require(pinpath.exists() and load(net['pins'])==pins,'Pin drift: create a reviewed successor; never refresh silently')
    report={'status':'pass','revision':4,'nodes':len(net['nodes']),'rejected':5,'constructed':3,'declared_specifications':2,'conditional_constructions':2,
            'open':sum(n['status']=='open' for n in net['nodes']),'specification_gates':5,'open_specification_gates':3,'proof_obligations':8,'assembly_objectives':1,'coherence_faces':4,'higher_coherence_obligations':1,'frontier':net['frontier'],'pinned_files':len(names),'corruption_controls':controls,
            'parent_modified':False,'physical_validation':False,'proofs_rerun_by_this_audit':False,
            'publication':'owner_local_only'}
    out=path(net['audit_receipt']);out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8');print(json.dumps(report))
if __name__=='__main__':main()
