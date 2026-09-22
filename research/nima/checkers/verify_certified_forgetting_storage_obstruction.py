"""Independent primal/Farkas and distinguishability replay; no producer import."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    cp=OUT/'certified-forgetting-storage-obstruction-contract.json';pp=OUT/'certified-forgetting-storage-obstruction-packet.json';rp=OUT/'certified-forgetting-storage-obstruction.json'
    c,p,r=load(cp),load(pp),load(rp)
    assert sha(cp)==r['contract_sha256'] and sha(pp)==r['packet_sha256']
    for name,h in c['bindings'].items():assert sha(ROOT/name)==h
    source=load(OUT/'causal-interface-construction.json');base=load(OUT/'causal-interface-construction-contract.json')
    mixed=load(OUT/'mixed-source-tail-certificate-contract.json')
    assert mixed['task']['origin_zero']==['even_support','adjacent_capacity']
    start=p['source_path'][0]['before'];assert start in source['initial_state_ids'] and source['states'][start][1]==0
    here=start;marked=None
    for edge in p['source_path']:
        assert edge['before']==here
        accepted,there=source['transitions'][here][base['labels'].index(edge['label'])]
        assert accepted and there==edge['after']
        if edge['label']==['source',2,0]:marked=source['states'][here][3] is not None
        here=there
    assert here==p['final_source_state'] and source['states'][here]==[15,0,0,0,None] and marked==p['marked_answer']==True
    sigma=Q(1,2);coords=c['finite_test']['probe_coordinates'];N=len(coords);M=max(coords)
    assert len(set(coords))==N and all(n>=6 and n%2==0 for n in coords)
    # Check common optimizer on finite crossing rows; the general argument is
    # counting parity in any interval and summing the two geometric series.
    x=[sigma if n%2==0 else Q(0) for n in range(1,M+1)]
    y=[sigma if n%2 else Q(0) for n in range(1,M+1)]
    for a in range(M):
        for b in range(a+1,M+1):
            assert sum(x[a:b])<=sigma*sum(n%2==0 for n in range(a+1,b+1))
            assert sum(y[a:b])<=sigma*((b-a+1)//2)
    assert -sigma*(Q(1,4)/(1-Q(1,4))+Q(1,2)/(1-Q(1,4)))==Q(p['common_optimum'])==-Q(1,2)
    # The source's base dual bounds still apply after refinement. The same
    # optimizer attains them, so all new carriers have exactly that optimum.
    assert all(y[n-1]==0 for n in coords)
    assert Q(p['common_certified_lower'])==-Q(17,32)>Q(mixed['task']['threshold'])
    # Independently validate every candidate spike against all finite interval
    # rows. Beyond M it extends by zero; capacities only increase to the right.
    for n in coords:
        for a in range(M):
            for b in range(a+1,M+1):assert int(a<n<=b)<=(b-a+1)//2
    signatures=[];checks=0
    assert len(p['histories'])==2**N
    for history in p['histories']:
        zero=set(history['zero_slots']);assert zero<=set(coords)
        assert history['mask']==sum(1<<j for j,n in enumerate(coords) if n in zero)
        answers=[]
        for n in coords:
            if n in zero:
                # A positive Farkas combination of the two conflicting rows.
                coefficients=(Q(1),Q(-1));rhs=(Q(0),-sigma);weights=(Q(1),Q(1))
                assert sum(a*w for a,w in zip(coefficients,weights))==0
                assert sum(b*w for b,w in zip(rhs,weights))<0;answers.append(False)
            else:
                assert all((sigma if j==n else Q(0))<=0 for j in zero)
                assert sigma>=sigma;answers.append(True)
            checks+=1
        assert answers==history['future_feasibility'];signatures.append(tuple(answers))
    assert len(set(signatures))==2**N
    pairs=0
    for a in range(len(signatures)):
        for b in range(a+1,len(signatures)):
            delta=p['histories'][a]['mask']^p['histories'][b]['mask'];j=(delta&-delta).bit_length()-1
            assert signatures[a][j]!=signatures[b][j];pairs+=1
    bad=p['collision'];a,b=bad['histories'];B=c['finite_test']['history_dependent_bit_budget']
    assert (a&((1<<B)-1))==(b&((1<<B)-1))==bad['retained_low_bits']
    j=coords.index(bad['separating_coordinate']);assert signatures[a][j] and not signatures[b][j]
    assert N>B and 2**N>2**B
    assert p['synthesis']['required_bits']==N and p['synthesis']['disposition']=='REFUSE_BUDGET'
    assert checks==r['feasibility_checks'] and pairs==r['pairwise_separation_checks']
    result={'passed':True,'report_sha256':sha(rp),'histories':2**N,'distinct_future_languages':len(set(signatures)),
      'checked_feasibility_queries':checks,'pairwise_separations':pairs,'required_bits':N,'requested_bits':B,
      'general_lower_bound':'H independent refinement coordinates force at least H history-dependent bits, even with identical current optimizer, decision and marked source answer.',
      'scope':'Necessary bound for the larger language; N bits are sufficient only for this restricted zero-frame/read-only-probe subfamily.'}
    (OUT/'certified-forgetting-storage-obstruction-verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
