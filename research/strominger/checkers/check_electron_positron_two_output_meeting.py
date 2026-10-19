#!/usr/bin/env python3
"""Account for both complete seed histories in an e-/e+ two-output meeting.
Only existing label matches; no annihilation vertex or filling rule inserted.
"""
from itertools import combinations
from pathlib import Path
import hashlib
import json
import sys
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(Path(__file__).resolve().parent))
from check_half_electron_positron_seeds import analyse

def route(start,end,sign):
    out=[start]
    while out[-1]!=end:out.append((out[-1]+sign)%5)
    return tuple(out)

def polynomial_is_c3(coeffs):
    # Exact integer remainder at omega, omega^2+omega+1=0.
    a=b=0
    for c in map(int,coeffs):a,b=c-b,a-b
    return (a,b)==(0,0)

def main():
    meetings=[]
    complete={(owner,i,(i+sign)%5) for owner,sign in [('electron',1),('positron',-1)] for i in range(5)}
    for a,b in combinations(range(5),2):
        eab=route(a,b,1);eba=route(b,a,1)
        pab=route(a,b,-1);pba=route(b,a,-1)
        # Two perfect matchings of the two electron and two positron pieces.
        pairings=[('parallel_comparisons',[(eab,pab,'parallel'),(eba,pba,'parallel')]),('backtracking_returns',[(eab,pba,'return'),(eba,pab,'return')])]
        for name,pairs in pairings:
            outputs=[];used=[]
            for e,p,kind in pairs:
                output=analyse((e[0],len(e)-1,e),(p[0],len(p)-1,p),kind)
                outputs.append(output)
                used.extend((owner,i,j) for owner,path in [('electron',e),('positron',p)] for i,j in zip(path,path[1:]))
            assert len(used)==10 and len(set(used))==10 and set(used)==complete
            meetings.append({'meeting_labels':['ABCDE'[a],'ABCDE'[b]],'pairing':name,'outputs':outputs,'all_ten_occurrences_retained_once':True,'output_occurrence_counts':[o['arrow_occurrences'] for o in outputs],'two_prior_C3_photon_modes':all(polynomial_is_c3(o['continuation_characteristic_coefficients']) for o in outputs)})
    # Restrict to the originally requested two/three-arrow cuts, while retaining
    # the one/four cuts as an exhaustive same-label control.
    adjacent=[m for m in meetings if (ord(m['meeting_labels'][1])-ord(m['meeting_labels'][0]))%5 in (1,4)]
    nonadjacent=[m for m in meetings if m not in adjacent]
    checks={
        'all_ten_endpoint_pairs_and_two_pairings':len(meetings)==20,
        'both_histories_fully_retained_once':all(m['all_ten_occurrences_retained_once'] for m in meetings),
        'ten_two_three_cut_meetings':len(nonadjacent)==10,
        'crosswise_outputs_each_have_five_occurrences':all(m['output_occurrence_counts']==[5,5] for m in meetings if m['pairing']=='parallel_comparisons'),
        'same_route_pairing_unequal_output_sizes':all(sorted(m['output_occurrence_counts'])==[4,6] for m in nonadjacent if m['pairing']=='backtracking_returns'),
        'no_output_pair_matches_prior_photon_modes':not any(m['two_prior_C3_photon_modes'] for m in meetings),
    }
    example=next(m for m in meetings if m['meeting_labels']==['A','C'] and m['pairing']=='parallel_comparisons')
    out={'schema':'marici.strominger.electron-positron-two-output-meeting.v1','status':'passed' if all(checks.values()) else 'failed','scientific_disposition':'lossless two-output arrow partition constructed; photon-producing meeting rule not yet obtained','checks':checks,'input_occurrences':{'electron':['AB','BC','CD','DE','EA'],'positron':['AE','ED','DC','CB','BA']},'two_output_example':example,'meetings':meetings,'interpretation':{'positive':'At A,C, crosswise pairing partitions the ten input occurrences into two equal five-occurrence parallel-route comparisons, one A->C and one C->A. No seed arrow disappears.','first_output':['electron A->B->C','positron A->E->D->C'],'second_output':['electron C->D->E->A','positron C->B->A'],'failure':'These are oppositely directed route comparisons with pentagonal supports, not two shared-edge two-triangle photon seeds. Their endpoint-continuation operators have no prior conjugate C3 photon pair.','needed_operation':'A common arrow-derived comparison/interaction operation turning each retained route pair into the same photon output object. Endpoint matching itself does not supply that operation.','processor_boundary':'Retaining the original affine generators still gives the electron four-simplex; discarding them and calling route comparison a filled photon would change the processor.'},'source_hashes':{str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),ROOT/'research/strominger/checkers/check_half_electron_positron_seeds.py',ROOT/'research/strominger/results/half_electron_positron_seeds.json',ROOT/'research/voevodsky/inputs/relative-electron.json',ROOT/'research/strominger/inputs/relative-positron-candidate.json']}}
    (ROOT/'research/strominger/results/electron_positron_two_output_meeting.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'status':out['status'],'checks':checks,'example_outputs':[{'electron':o['electron_path'],'positron':o['positron_path'],'occurrences':o['arrow_occurrences'],'continuation_polynomial':o['continuation_characteristic_coefficients']} for o in example['outputs']]},indent=2))
    if not all(checks.values()):raise SystemExit(1)
if __name__=='__main__':main()
