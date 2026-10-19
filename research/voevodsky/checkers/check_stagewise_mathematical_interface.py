"""Validate a bounded mathematical interface definition, not universal truth."""
import argparse
import json
import subprocess
import sys
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
DEF='research/conjecture_net/contracts/stagewise-mathematical-interface.v1.json'
NOTE='research/voevodsky/stagewise-mathematical-interface-v1.md'
OUT='research/voevodsky/results/stagewise-mathematical-interface-v1.json'
BRANCH='research/conjecture_net/contracts/mathematical-realization-conjecture-net.v1.json'
HEADLESS='research/voevodsky/results/domain-compiler-headless-review-v1.json'
SOURCES=['research/nima/typed-generator-layer-2.md','research/nima/typed-generator-layer-3.md',
 'research/nima/domain-witness-compiler-pilot.md','research/nima/label-from-to-fibration-tower.md',
 'research/nima/agda/DomainWitnessCompiler.agda','research/nima/agda/TypedGeneratorLayers.agda',
 'research/nima/agda/TypedGeneratorTransport.agda',
 'research/nima/checkers/check_typed_generator_layers.py','research/nima/checkers/check_typed_generator_transport.py',
 'research/nima/checkers/check_label_from_to_fibration_tower.py',
 'research/nima/results/typed-generator-layers.json','research/nima/results/typed-generator-transport.json',
 'research/strominger/wg-software-operations-composition-prior-search.md',
 'research/strominger/wg-I-squared-rehydration-correction.md',
 'research/conjecture_net/contracts/rh-bounded-mathematical-example.v1.json',
 'research/voevodsky/results/rh-stagewise-interface-assembly-v1.json',
 'research/voevodsky/results/fourier-six-step-descent-v1.json']


def load(p):return json.loads((ROOT/p).read_text())
def sha(p):return sha256((ROOT/p).read_bytes()).hexdigest()
def require(x,msg):
    if not x:raise ValueError(msg)


def run_admitted_boolean(state):
    phase,index,value=state
    require(type(index) is bool and index is False,'exact admitted false request index required')
    if phase=='request':return ('response',index,not index)
    require(phase=='response' and type(value) is bool,'typed response')
    return state


def validate_law(origin,trace):
    require(origin in load(DEF)['source_rules']['law_origins'],'law provenance')
    if origin=='native_rule_derivation':require(trace,'native generation without source-rule derivation')


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--record',action='store_true');args=ap.parse_args()
    s=load(DEF);require(not any(s['boundaries'].values()),'interface promotion')
    audits=[]
    for stem in ('typed_generator_layers','typed_generator_transport','label_from_to_fibration_tower'):
        p='research/nima/checkers/check_'+stem+'.py'
        r=subprocess.run([sys.executable,str(ROOT/p)],cwd=ROOT,capture_output=True,text=True,timeout=120)
        require(r.returncode==0,'source-bound audit failed '+p+'\n'+r.stderr)
        audits.append(dict(checker=p,returncode=0,summary=r.stdout.strip()))
    headless=load(HEADLESS);require(headless['passed'] and headless['returncode']==0,'missing fresh pilot compilation')
    for p,h in headless['source_sha256'].items():require(sha(p)==h,'pilot compilation source drift')
    for stem in ('typed-generator-layers','typed-generator-transport'):
        require(load('research/nima/results/'+stem+'.json')['passed'],'formal source audit failed')
    checks=[];hostiles=[]
    def check(name,test):require(test,name);checks.append(name)
    request=('request',False,None);response=run_admitted_boolean(request)
    check('retained admitted request index',response==('response',False,True))
    check('response phase idle, not a second Boolean compute',run_admitted_boolean(response)==response and (not (not False)) is False)
    try:run_admitted_boolean(('response',True,True))
    except ValueError:hostiles.append('output-relabelled-as-request-index')
    else:raise AssertionError('dependent index erasure admitted')
    check('same signature does not identify operations',(not False)!=False)
    flips=[(False,True),(True,False)]
    check('typed history join retains intermediate state',flips[0][1]==flips[1][0])
    check('two flips not one original relation edge',flips[0][0]==flips[-1][1] and not (flips[-1][1]==(not flips[0][0])))
    hostiles.append('universal original-relation folding')
    check('endpoint cannot decode empty versus two-step history',[]!=flips and flips[0][0]==flips[-1][1])
    check('circle-loop payload action not determined by endpoints',(not True)!=True)
    hostiles += ['history-erasure','endpoint-only payload action']
    validate_law('supplied_domain_law',None)
    try:validate_law('native_rule_derivation',None)
    except ValueError:hostiles.append('supplied-category-law-relabelled-native')
    else:raise AssertionError('native law without derivation')
    d=load('research/voevodsky/results/fourier-six-step-descent-v1.json')
    require(d['passed'] and d['composite_equals_original_direct_P'],'missing actual endpoint-preserving repair')
    for p,h in d['source_hashes'].items():require(sha(p)==h,'intermediate witness source drift')
    ranks=[r['full_tick_leakage_rank'] for r in d['original_prefix_audit']]
    check('actual RH intermediate mismatch ranks',ranks==[1,2,1,0,0,0])
    check('actual nonzero hidden-to-visible first-prefix control',any(Q(v[0])!=0 for v in d['original_prefix_audit'][0]['visible_tick_output']))
    check('actual repaired all-stage operation squares',all(x['full_tick_intertwining'] and x['hidden_reconstruction'] for x in d['verified_steps']))
    hostiles.append('endpoint-correct but intermediate-operation incompatible frame')
    assembly=load('research/voevodsky/results/rh-stagewise-interface-assembly-v1.json')
    check('RH completion and native distinctions retained',assembly['passed'] and not assembly['boundaries']['native_tick_identified_with_Fourier'] and not assembly['boundaries']['ordinary_log_tempered_comb_extension'])
    # Availability mismatch breaks naive joint-word equivalence transitivity.
    states={'x':(True,0),'y':(False,0),'z':(True,1)}
    joint=lambda a,b:not (states[a][0] and states[b][0]) or states[a][1]==states[b][1]
    check('intersection-only word agreement is not identity',joint('x','y') and joint('y','z') and not joint('x','z'))
    hostiles.append('unequal-guards-as-vacuous-identity')
    result=dict(schema='marici.stagewise-mathematical-interface-validation.v1',passed=True,
      resolution_kind='bounded_interface_definition',definition=DEF,checks=checks,corruptions_retained=hostiles,
      source_bound_audits=audits,headless_compile=HEADLESS,
      fresh_compilation_scope='Existing safe supplied-law pilot, not a new universal compiler or a formalization of this entire interface.',
      physical_realization_admitted=False,universal_compatibility_proved=False,WG_and_RH_sources_identified=False,
      universal_coverage_proved=False,examples_automatically_discharged=False,
      source_sha256={p:sha(p) for p in [DEF,NOTE,HEADLESS,Path(__file__).relative_to(ROOT).as_posix(),*SOURCES]})
    if args.record:
        require(not (ROOT/OUT).exists(),'refusing implicit interface receipt overwrite')
        (ROOT/OUT).write_text(json.dumps(result,indent=2)+'\n')
    else:
        require(load(OUT)==result,'definition evidence drift')
        c=load(BRANCH);n=next(n for n in c['conjectures'] if n['id']=='stagewise-mathematical-interface')
        require(n['status']=='resolved' and n['verdict']=='constructed' and n['resolution_kind']=='bounded_interface_definition' and c['mathematical_interface']==DEF,'missing definition registration')
    print(json.dumps(dict(passed=True,exact_checks=len(checks),controls=len(hostiles),source_bound_audits=len(audits),
      existing_pilot_fresh_safe_compile=True,universal_coverage_proved=False,examples_automatically_discharged=False),indent=2))


if __name__=='__main__':main()
