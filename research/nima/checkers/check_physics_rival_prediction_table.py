"""Exact source-sensitive rival controls, not empirical model exclusions."""
import argparse
import copy
import json
from fractions import Fraction as F
from pathlib import Path
import check_physics_geometric_candidate as G
import check_physics_observation_resource_interface as O
import check_physics_dynamics_selection_audit as D

ROOT=G.ROOT
CONTRACT='research/nima/contracts/physics-rival-prediction-table.v1.json'
CLASSES={
    'delete-dark-return':'separated_by_ordered_model_continuation',
    'closed-compressed-plant':'rejected_as_closed_unitary_not_as_open_plant',
    'unordered-rounds':'separated_by_labelled_operation_transport',
    'reset-ready-every-bin':'separated_by_complete_model_histories',
    'no-click-is-ready':'separated_by_predictive_state_continuation',
    'discard-no-click-records':'invalid_complete_record_comparison',
    'active-port-phase-completion':'weak_premise_countermodel_not_selected_physical_law',
    'merged-no-click-environments':'not_identified_on_charter_domain',
    'imported-law-reproduction':'observational_alias_explanatory_provenance_gate'}


def validate(c):
    rivals={r['id']:r for r in c['rivals']}
    G.require(len(rivals)==len(c['rivals']) and {k:r['classification'] for k,r in rivals.items()}==CLASSES,'rival coverage/classification')
    G.require(c['decision']=='accept_scoped_rival_specification' and c['empirical_exclusions']==[],'empirical promotion')
    G.require(c['source_dependence']['native_source_law_derivation'] is False and c['source_dependence']['missing'],'source derivation promotion')
    G.require(set(c['targets'])==set(G.load('research/nima/contracts/physics-target-charter.v1.json')['selected_physical_targets']),'target coverage')
    G.require(c['source_witness_id']=='passive-port-fock-memory.v1' and F(c['discrepancy_allowance'])==F(1,100),'source/budget drift')
    for r in rivals.values():
        G.require(all(r.get(k) for k in ('target','change','shared','control','reference','rival')),'incomplete rival')
        G.require(r['target'] in c['targets']+['both_selected_targets'],'unknown target')


def word_probability(inputs,word,ready=F(1),reset=False):
    state=(ready,1-ready)
    for n,y in zip(inputs,word):
        if reset:state=(sum(state),F(0))
        state=O.step(n,y,state)
    return sum(state)


def main():
    p=argparse.ArgumentParser();p.add_argument('--pin',action='store_true');args=p.parse_args()
    c=G.load(CONTRACT);validate(c)
    paths={CONTRACT}|set(c['source_evidence']);pin=ROOT/c['source_pins']
    if args.pin:
        G.require(not pin.exists(),'refusing implicit re-pin')
        pin.write_text(json.dumps({'source_sha256':{p:G.sha(p) for p in sorted(paths)}},indent=2)+'\n',encoding='utf-8')
    pins=G.load(c['source_pins']);G.require(set(pins['source_sha256'])==paths,'pin coverage')
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source drift: '+path)
    eps=F(c['discrepancy_allowance']);controls={}
    yr,yt,xn,ye=O.cavity(F(4,5),F(3,5),F(0),F(0))
    following=O.cavity(F(0),xn,F(0),F(0))[0]
    G.require(yr==0 and xn==F(12,25) and following==F(48,125),'dark-return witness')
    G.require(following**2==F(2304,15625)>2*eps,'dark continuation margin')
    controls['delete-dark-return']={'reference_amplitude':str(following),'reference_occupation':str(following**2),'rival_occupation':'0'}
    outputs=O.cavity(F(0),F(1),F(0),F(0));env=outputs[3]**2
    retained=sum(x*x for x in outputs[:3])
    G.require(retained+env==1 and env==F(2304,15625) and retained==F(13321,15625),'open/unitary boundary')
    controls['closed-compressed-plant']={'retained_norm':str(retained),'environment_norm':str(env)}
    e0={G.occupation([0]):F(1)}
    reference=G.lift_state(G.round_map(1),G.lift_state(G.round_map(0),e0))
    reverse=G.lift_state(G.round_map(0),G.lift_state(G.round_map(1),e0))
    residual=D.add(reference,D.scale(-1,reverse));norm=G.inner(residual,residual)
    G.require(norm>0,'round-order alias')
    controls['unordered-rounds']={'coefficient_residual_norm_squared':str(norm)}
    cc=word_probability((1,1),'CC');cc_reset=word_probability((1,1),'CC',reset=True)
    cnc=word_probability((1,0,1),'CNC');cnc_reset=word_probability((1,0,1),'CNC',reset=True)
    G.require(cc==0 and cc_reset==F(81,625) and cnc==F(729,15625) and cnc_reset==F(81,625),'reset controls')
    G.require(cc_reset-cc>2*eps and cnc_reset-cnc>2*eps,'reset margins')
    controls['reset-ready-every-bin']={k:str(v) for k,v in {'CC':cc,'reset_CC':cc_reset,'CNC':cnc,'reset_CNC':cnc_reset}.items()}
    ready,likelihood=O.filter_step(1,'N',F(1,2))
    following_click=F(9,25)*ready
    G.require(ready==F(25,41) and following_click==F(9,41) and F(9,25)-following_click>2*eps,'no-click readiness alias')
    controls['no-click-is-ready']={'reference_readiness':str(ready),'reference_next_click':str(following_click),'rival_next_click':'9/25'}
    retained=word_probability((1,),'C');omitted=word_probability((1,),'N')
    G.require(retained==F(9,25) and omitted==F(16,25) and retained+omitted==1 and retained/retained==1,'postselection denominator')
    controls['discard-no-click-records']={'retained_mass':str(retained),'omitted_mass':str(omitted),'selected_frequency':'1'}
    audit=G.load('research/nima/contracts/physics-dynamics-selection-audit.v1.json')
    optical=D.optical(audit);detector=D.detector()
    controls['active-port-phase-completion']={'reference_field_mean':optical['reference_field_mean'],
        'rival_field_mean':optical['local_rival_field_mean'],'failed_creation_squares':optical['local_rival_failed_creation_squares'],
        'unchanged_low_sector_records':optical['unchanged_routed_records']}
    controls['merged-no-click-environments']={'identical_classical_histories':detector['identical_classical_histories'],
        'reference_out_of_scope_X':detector['reference_coherent_memory_X'],'rival_out_of_scope_X':detector['rival_coherent_memory_X'],
        'charter_discriminator_supplied':False}
    controls['imported-law-reproduction']={'same_operations_imply_same_predictions':True,'independent_native_derivation':False,'output_discriminator_supplied':False}
    rejected=[]
    for name in ('missing-rival','duplicate-rival','promoted-CP-alias','empirical-exclusion','derived-imported-law'):
        bad=copy.deepcopy(c)
        if name=='missing-rival':bad['rivals'].pop()
        elif name=='duplicate-rival':bad['rivals'].append(bad['rivals'][0])
        elif name=='promoted-CP-alias':bad['rivals'][7]['classification']='excluded_by_classical_records'
        elif name=='empirical-exclusion':bad['empirical_exclusions']=['reset-ready-every-bin']
        else:bad['source_dependence']['native_source_law_derivation']=True
        try:validate(bad)
        except ValueError:rejected.append(name)
        else:raise AssertionError('accepted '+name)
    for path,h in pins['source_sha256'].items():G.require(G.sha(path)==h,'source changed during check')
    out={'schema':c['schema'],'status':'pass','rival_count':len(controls),'controls':controls,
         'rejected_corruptions':rejected,'empirical_exclusions':[],'native_source_law_derived':False,
         'source_sha256':pins['source_sha256'],'checker_sha256':G.sha(Path(__file__))}
    (ROOT/c['result']).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='source_sha256'},indent=2))

if __name__=='__main__':main()
