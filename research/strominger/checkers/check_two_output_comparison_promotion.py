#!/usr/bin/env python3
"""Retained path-composition attempt for two e-/e+ output comparisons.
New compound occurrences are explicit; no path equality or primitive deletion.
"""
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/voevodsky/checkers'))
from assemble_relative_geometry import assemble
from check_neutrino_arrow_seed_science import rank
from check_half_electron_positron_seeds import characteristic
from build_neutrino_seed_candidates import simplex_source

def add(x,y):return (x[0]+y[0],x[1]+y[1])
def mul(x,y):return (x[0]*y[0]-3*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def conj(x):return (x[0],-x[1])
def act(K,v):
    out=[]
    for row in K:
        x=(Q(0),Q(0))
        for coefficient,z in zip(row,v):x=add(x,(coefficient*z[0],coefficient*z[1]))
        out.append(x)
    return out

def compile_output(output,rule):
    e,p=output['electron_path'],output['positron_path']
    assert len(e) in (3,4) and len(p) in (3,4) and len(e)!=len(p)
    short,long=(e,p) if len(e)==3 else (p,e)
    short_owner,long_owner=('electron','positron') if len(e)==3 else ('positron','electron')
    A,B,C=short
    if rule=='compose_first_two':D=long[2];prefix=long[:3];tail=long[2:]
    else:D=long[1];prefix=long[:2];tail=long[1:]
    # Internal cycles are ABC and ACD. They share AC in opposite directions.
    # Put the shared seam first, matching the prior registry's AB/BA slots.
    paths=[list(reversed(short)),short[:2],short[1:],short,list(reversed(tail)),list(reversed(prefix))]
    owners=[short_owner,short_owner,short_owner,short_owner,long_owner,long_owner]
    kinds=['inverse_composite','subpath','subpath','composite','inverse_subpath','inverse_subpath']
    occurrences=[{'id':i,'source':path[0],'target':path[-1],'retained_path':path,'source_owner':owner,'operation':kind,'primitive_steps':len(path)-1} for i,(path,owner,kind) in enumerate(zip(paths,owners,kinds))]
    # Index order matches native photon: X,Y,Z,X',W,V with cycles 0,1,2 and 3,4,5.
    K=[[Q(x['target']==y['source']) for x in occurrences] for y in occurrences]
    omega=(-Q(1,2),Q(1,2));w2=mul(omega,omega)
    plus=[(Q(1),Q(0)),(-Q(1),Q(0)),(-w2[0],-w2[1]),(-Q(1),Q(0)),(Q(1),Q(0)),w2]
    minus=[conj(z) for z in plus]
    mode_ok=act(K,plus)==[mul(omega,z) for z in plus] and act(K,minus)==[mul(conj(omega),z) for z in minus]
    labels=[A,B,C,D]
    source,_=simplex_source(4,[[0,1,2],[0,2,3]])
    geometry=assemble(source)
    covered=set()
    for item in occurrences:
        path=item['retained_path']
        if item['operation'].startswith('inverse'):path=list(reversed(path))
        covered|={(item['source_owner'],a,b) for a,b in zip(path,path[1:])}
    inputs={(owner,a,b) for owner,path in [('electron',e),('positron',p)] for a,b in zip(path,path[1:])}
    assert covered==inputs
    original_names=set(e+p)
    suppressed=sorted(original_names-set(labels))
    inherited_C5={tuple((i+j)%5 for i in range(5)) for j in range(5)}
    proposed_actions=[]
    for cycle in ([A,B,C],[A,C,D]):
        permutation=list(range(5))
        for x,y in zip(cycle,cycle[1:]+cycle[:1]):permutation['ABCDE'.index(x)]='ABCDE'.index(y)
        proposed_actions.append(tuple(permutation))
    inherited_actions=all(p in inherited_C5 for p in proposed_actions)
    return {'short_owner':short_owner,'long_owner':long_owner,'contraction_rule':rule,'corner_labels':labels,'suppressed_as_corner_but_retained_in_history':suppressed,'face_cycles':[[A,B,C,A],[A,C,D,A]],'compound_occurrences':occurrences,'continuation_matrix':[[int(x) for x in row] for row in K],'continuation_rank':rank(K),'characteristic_coefficients':[str(c) for c in characteristic(K)],'native_photon_mode_pair_recovered':mode_ok,'all_five_input_occurrences_covered':covered==inputs,'path_records_identified_by_equal_endpoints':False,'relative_source':source,'complete_processor_geometry':geometry,'visible_corner_count':4,'comparison_filling_witness_supplied':False,'proposed_output_generator_permutations':[list(p) for p in proposed_actions],'three_cycle_action_from_original_C5_library':inherited_actions}

def main():
    meeting_path=ROOT/'research/strominger/results/electron_positron_two_output_meeting.json'
    prior=json.loads(meeting_path.read_text())
    meetings=[m for m in prior['meetings'] if m['pairing']=='parallel_comparisons' and all(o['electron_length'] in (2,3) and o['positron_length'] in (2,3) for o in m['outputs'])]
    attempts=[]
    for meeting in meetings:
        for rule in ('compose_first_two','compose_last_two'):
            outputs=[compile_output(o,rule) for o in meeting['outputs']]
            retained_roots=set()
            for o in meeting['outputs']:
                for owner,path in [('electron',o['electron_path']),('positron',o['positron_path'])]:retained_roots|={(owner,a,b) for a,b in zip(path,path[1:])}
            attempts.append({'meeting_labels':meeting['meeting_labels'],'rule':rule,'outputs':outputs,'retained_input_root_occurrences':len(retained_roots),'emitted_compound_occurrences':sum(len(o['compound_occurrences']) for o in outputs)})
    checks={
        'five_cut_pairs_two_uniform_contractions':len(attempts)==10,
        'all_ten_original_occurrences_retained':all(a['retained_input_root_occurrences']==10 for a in attempts),
        'all_outputs_have_six_compound_occurrences':all(len(o['compound_occurrences'])==6 for a in attempts for o in a['outputs']),
        'all_outputs_recover_prior_C3_pair':all(o['native_photon_mode_pair_recovered'] for a in attempts for o in a['outputs']),
        'all_intermediate_history_retained':all(o['all_five_input_occurrences_covered'] and len(o['suppressed_as_corner_but_retained_in_history'])==1 for a in attempts for o in a['outputs']),
        'same_processor_still_completes_tetrahedron':all(o['complete_processor_geometry']['counts']['carrier_facets']==4 for a in attempts for o in a['outputs']),
        'no_existing_source_C3_action_claimed':all(not o['three_cycle_action_from_original_C5_library'] for a in attempts for o in a['outputs']),
    }
    example=next(a for a in attempts if a['meeting_labels']==['A','C'] and a['rule']=='compose_first_two')
    out={'schema':'marici.strominger.two-output-comparison-promotion.v1','status':'passed' if all(checks.values()) else 'failed','scientific_disposition':'retained compound-arrow compiler recovers two photon-like mode pairs; promotion/interaction and two-face stopping are not source-derived','construction':'Compose one consecutive pair on each long route; retain its intermediate vertex/history. Form two boundary comparison cycles using a short-path composite and its inverse. Do not equate short and long path records.','checks':checks,'attempts':attempts,'example':example,'accounting':{'input_primitive_root_occurrences':10,'output_compound_occurrences':12,'why_not_arrow_creation_from_nothing':'Output records are composites, inverse records and references to retained input paths. Twelve output records do not mean twelve independently supplied primitives.','resource_boundary':'No physical implementation cost or output probability is inferred from reference reuse.'},'missing_source_obligations':['Admit path composition/inversion as executed interaction operations, not just retained mathematical records','Supply comparison/filling witnesses for the paired routes','Derive the output three-cycle actions: original C5 action has no order-three element','Select the retained photon output rather than full tetrahedral completion using one common rule'],'source_hashes':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),meeting_path,ROOT/'research/strominger/checkers/build_neutrino_seed_candidates.py',ROOT/'research/strominger/checkers/check_half_electron_positron_seeds.py',ROOT/'research/strominger/checkers/check_neutrino_arrow_seed_science.py',ROOT/'research/voevodsky/checkers/assemble_relative_geometry.py']}}
    (ROOT/'research/strominger/results/two_output_comparison_promotion.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'checks':checks,'example':{'rule':example['rule'],'output_cycles':[o['face_cycles'] for o in example['outputs']],'polynomials':[o['characteristic_coefficients'] for o in example['outputs']],'root_inputs':10,'compound_outputs':12},'missing_source_obligations':out['missing_source_obligations']},indent=2))
    if not all(checks.values()):raise SystemExit(1)
if __name__=='__main__':main()
