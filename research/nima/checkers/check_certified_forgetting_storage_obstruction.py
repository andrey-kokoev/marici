"""Attack a fixed forgetting budget on the existing mixed carrier.

All histories have the same source path, marked answer, actual optimizer and
numerical decision. Only future feasibility of a finite linear frame differs.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,subprocess,sys
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')

def main():
    source=OUT/'causal-interface-construction.json';base=OUT/'causal-interface-construction-contract.json'
    mixed=OUT/'mixed-source-tail-certificate-contract.json';report=OUT/'mixed-source-tail-certificate.json'
    budget=8;N=10;coordinates=[6+2*j for j in range(N)]
    contract={'schema':'certified-forgetting-storage-obstruction-v1',
      'bindings':{str(p.relative_to(ROOT)):sha(p) for p in (source,base,mixed,report)},
      'source_path':[['acquire'],['source',3,0],['deliver'],['source',2,0]],
      'initial_origin':0,'marked_query':'Was a receipt already present immediately before the accepted source(2,0) transition?',
      'numeric_object':'Channel 1 of the existing mixed task: adjacent-capacity carrier at scale 1/2, same variables for every retained frame.',
      'past_frames':'For any finite set J of even n>=6, retain y_n<=0 for n in J. Each frame is true at the common odd-only optimizer.',
      'future_query':'Is adding y_n>=1/2 jointly feasible? This is a compatibility query, not a declaration that the actual tail changed.',
      'candidate_rule':'Dependency closure over declared probe coordinates retains the membership mask J on those coordinates; refuse publication of a lossless interface if it exceeds the bit budget.',
      'negative_rule':'Keep only the lowest budget bits of that mask and discard all other refinement information.',
      'finite_test':{'history_dependent_bit_budget':budget,'probe_coordinates':coordinates,'number_of_histories':2**N},
      'budget_accounting':'All history-dependent retained information counts, including any digest, cached certificate, code specialization or external journal used for recovery. Fixed source/task data do not vary with J.',
      'unbounded_claim_to_attack':'One fixed finite budget suffices for arbitrary finite-support frames and all future coordinate-feasibility queries.',
      'scope':'Existing rational control coupling, not an actual-prime evidence adapter. Truthful original frames and known source initialization are assumed.'}
    cp=OUT/'certified-forgetting-storage-obstruction-contract.json';save(cp,contract)
    subprocess.run([sys.executable,str(ROOT/'nima/checkers/verify_mixed_source_tail_certificate.py')],check=True,capture_output=True,text=True)
    data=load(source);parent=load(base)
    state=next(i for i in data['initial_state_ids'] if data['states'][i][1]==0)
    path=[];marked=None
    for label in contract['source_path']:
        before=state;accepted,state=data['transitions'][state][parent['labels'].index(label)];assert accepted
        if label[:2]==['source',2]:marked=data['states'][before][3] is not None
        path.append({'label':label,'before':before,'after':state})
    assert data['states'][state]==[15,0,0,0,None] and marked is True
    assert load(report)['compatible_scaled_lower']=='-17/32'
    # The same infinite pair is optimal for all J:
    # x_even=1/2, y_odd=1/2, every other coordinate zero.
    # The inherited carrier dual lower is (-1/3-2/3)/2=-1/2;
    # this explicit pair attains it and satisfies every new zero-even frame.
    optimum=-Q(1,2)*(Q(1,4)/(1-Q(1,4))+Q(1,2)/(1-Q(1,4)))
    assert optimum==-Q(1,2)>-Q(31,32)
    horizon=max(coordinates);sigma=Q(1,2);histories=[];signatures=set();checks=0
    for mask in range(2**N):
        zero_slots=[n for j,n in enumerate(coordinates) if mask&(1<<j)];answers=[]
        for j,n in enumerate(coordinates):
            if n in zero_slots:
                # Farkas: y_n<=0 plus -y_n<=-1/2 gives 0<=-1/2.
                certificate={'kind':'FARKAS','coordinate':n,'multipliers':['1','1'],'combined_coefficient':'0','combined_rhs':'-1/2'}
                assert Q(1)+Q(-1)==0 and Q(0)-sigma<0;feasible=False
            else:
                # x is zero; y has just one mass 1/2 at n. Every adjacent
                # interval cap is >=1/2 when it contains that mass.
                y=[sigma if k==n else Q(0) for k in range(1,horizon+1)]
                assert all(y[k-1]==0 for k in zero_slots)
                for a in range(horizon):
                    for b in range(a+1,horizon+1):assert sum(y[a:b])<=sigma*((b-a+1)//2)
                certificate={'kind':'PRIMAL','coordinate':n,'mass':'1/2','all_other_coordinates_zero':True};feasible=True
            answers.append(feasible);checks+=1
        signature=tuple(answers);assert signature not in signatures;signatures.add(signature)
        histories.append({'mask':mask,'zero_slots':zero_slots,'future_feasibility':answers})
    assert len(signatures)==2**N
    collision_a=0;collision_b=1<<budget;probe=coordinates[budget]
    assert collision_a&((1<<budget)-1)==collision_b&((1<<budget)-1)
    assert histories[collision_a]['future_feasibility'][budget] and not histories[collision_b]['future_feasibility'][budget]
    # Exact, independently replayable pairwise separation: any differing bit
    # supplies a declared future query. No global behavioral quotient defines
    # the synthesized mask; global signatures are used only to challenge it.
    pair_checks=0
    for a in range(2**N):
        for b in range(a+1,2**N):
            difference=a^b;j=(difference&-difference).bit_length()-1
            assert histories[a]['future_feasibility'][j]!=histories[b]['future_feasibility'][j];pair_checks+=1
    packet={'source_path':path,'final_source_state':state,'marked_answer':marked,
      'histories':histories,'common_optimum':str(optimum),'common_certified_lower':'-17/32','common_decision':'CERTIFIED',
      'collision':{'histories':[collision_a,collision_b],'retained_low_bits':0,'separating_coordinate':probe,
        'feasible_witness':{'channel':1,'coordinate':probe,'mass':'1/2','other_tail_entries_zero':True},
        'infeasibility_witness':{'rows':[[1,'0'],[-1,'-1/2']],'multipliers':['1','1'],'sum':[0,'-1/2']}},
      'synthesis':{'required_bits':N,'budget_bits':budget,'disposition':'REFUSE_BUDGET','bounded_horizon_repair':'Retain all N membership bits; each has a separating query.'}}
    pp=OUT/'certified-forgetting-storage-obstruction-packet.json';save(pp,packet)
    result={'verdict':'UNIFORM_FIXED_BUDGET_REFUTED_FOR_DECLARED_QUERY_FAMILY','contract_sha256':sha(cp),'packet_sha256':sha(pp),
      'histories':len(histories),'distinct_continuation_signatures':len(signatures),'feasibility_checks':checks,
      'pairwise_separation_checks':pair_checks,'minimum_refinement_bits_for_frozen_horizon':N,'requested_bits':budget,
      'same_current_optimum':'-1/2','same_marked_answer':True,'same_current_certificate':'-17/32 > -31/32',
      'general_argument':'For any H independent even coordinates there are 2^H pairwise distinguishable retained refinements, hence at least H history-dependent bits. H has no bound in the declared language.',
      'qualification':'This does not refute synthesis with a horizon-dependent budget or a restricted query language. Finite positive decision witnesses do not imply uniformly bounded memory for all future feasibility queries.',
      'scope':contract['scope']}
    for name,h in contract['bindings'].items():assert sha(ROOT/name)==h
    save(OUT/'certified-forgetting-storage-obstruction.json',result);print(json.dumps(result,indent=2))
if __name__=='__main__':main()
