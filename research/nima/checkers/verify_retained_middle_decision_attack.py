"""Exact replay of the source separator and middle-task feasibility reduction.
Does not reinterpret a worker timeout as an impossibility theorem.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,importlib.util
ROOT=Path(__file__).resolve().parents[2];N=ROOT/'nima/results';G=ROOT/'grothendieck/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def bounds(d):return Q(d['lower']),Q(d['upper'])
def main():
    report=load(N/'retained-middle-decision-conjecture-attack.json')
    contract=load(N/'retained-middle-decision-attack-contract.json')
    assert sha(N/'retained-middle-decision-attack-contract.json')==report['contract_sha256']
    for name,digest in contract['input_sha256'].items():assert sha(ROOT/name)==digest
    assert contract['unresolved_is_success'] is False
    assert contract['projection_dimension']==17*contract['projection_subdivisions']==408
    source={}
    for term in report['observation_factorization']['hidden_source']:
        word=tuple(term['word']);marks=tuple(term['marks']);value=Q(term['coefficient'])
        assert sorted(word)==list(range(6)) and marks==(0,)*6
        assert all(set(word[i:i+2])=={i,i+1} for i in (0,2,4))
        assert value==(-1)**sum(word[i]>word[i+1] for i in (0,2,4))
        assert (word,marks) not in source;source[word,marks]=value
    assert len(source)==8 and sum(source.values())==0
    assert source[tuple(range(6)),(0,)*6]==1
    base=load(N/'actual-private-core-with-original-cubic.json');union=load(N/'actual-retained-cubic-observer-union.json')
    protocol=load(G/'three-channel-cubic-protocol.json')
    assert union['source']['background']==protocol['parameters']['A']==2
    assert union['source']['events']==protocol['parameters']['prime_labels']
    rows=base['rows']+[r for f in union['frames'] for r in f['rows']]
    for row in rows:
        if row['corner_masks']==[0,63]:
            assert all(source.get((tuple(t['word']),tuple(t['marks'])),0)==0 for t in row['terms'])
    vac=protocol['channels']['vacuum']
    assert vac['source_signature']==[[[0,1],[2,3],[4,5]],[0,0,0]]
    assert vac['forward_gain_lower']==vac['forward_gain_upper']==['1','1']
    spec=importlib.util.spec_from_file_location('task',ROOT/'grothendieck/checkers/three_channel_source_task.py')
    t=importlib.util.module_from_spec(spec);spec.loader.exec_module(t)
    frozen=load(G/'calibration-refinement-frozen-inputs.json')
    case=frozen['cases']['private']['middle_threshold'];raw={n:t.interval(case['raw'][n]) for n in t.NAMES}
    B=Q(case['budget']);cap=(B/2**16-8*raw['vacuum'][0])/32
    assert raw['vacuum']==(Q(1,100),Q(1,100)) and raw['crossed']==(0,0)
    assert raw['positive'][0]>0 and cap==Q(499,400)
    threshold=raw['positive'][0]/cap
    assert threshold==Q(report['exact_feasibility_reduction']['threshold'])
    old=load(G/'projection-resolution-conjecture-attack.json');theta=load(G/'theta-mass-refinement.json')
    C=bounds(old['C_after']);H=bounds(old['h']);L=bounds(old['L'])
    xa=bounds(theta['windows']['A1']['X']);xb=bounds(theta['windows']['B1']['X'])
    ma=bounds(theta['windows']['A1']['mu']);mb=bounds(theta['windows']['B1']['mu'])
    assert min(C+H+xa+xb)>0 and ma[0]>L[1] and mb[0]>L[1]
    def gain(c,k):return 2*xa[k]*xb[k]*(c+H[k]*(ma[k]-L[1-k]))*(c+H[k]*(mb[k]-L[1-k]))
    low= gain(C[0],1);high=gain(C[1],0)
    assert low<threshold<high
    # Exact algebraic witnesses for the RELAXED gain branches, not claims that
    # either gain is the actual fixed detector's analytical value.
    for E,feasible in ((low,False),(threshold,True),(high,True)):
        a=raw['positive'][0]/E
        assert a*E==raw['positive'][0]
        assert (2**16*(32*a+8*Q(1,100))<=B)==feasible
    assert 8*2**16<=B
    assert report['endpoint_attack']['realizable_opposing_actual_histories'] is False
    initial=t.SourceTask(G/'three-channel-source-task-calibration-theta-taylor.json')
    assert all(initial.certify(frozen['cases'][mode]['middle_threshold'])['status']=='UNRESOLVED' for mode in ('private','reuse'))
    attempt=report['bounded_pairing_attempt']
    if attempt['status']=='completed':
        path=ROOT/attempt['calibration_file'];assert sha(path)==attempt['calibration_sha256']
        final=t.SourceTask(path)
        assert all(final.certify(frozen['cases'][mode]['middle_threshold'])==report['middle_results'][mode] for mode in ('private','reuse'))
    else:
        assert all(report['middle_results'][mode]['status']=='UNRESOLVED' for mode in ('private','reuse'))
    result={'passed':True,'source_rows_checked':len(rows),'forgotten_source_terms':len(source),
      'observation_factorization':'refuted','exact_cap':str(cap),'feasibility_threshold_identity':True,
      'endpoint_realizability_claim_rejected':True,
      'timing_scope':'Recorded worker outcome is not independently certified here and implies no universal deadline obstruction.',
      'attack_report_sha256':sha(N/'retained-middle-decision-conjecture-attack.json')}
    (N/'retained-middle-decision-attack-verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
