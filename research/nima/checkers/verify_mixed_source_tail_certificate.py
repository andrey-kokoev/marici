"""Independent exact mixed replay; imports neither constructor nor LP solver."""
from pathlib import Path
from fractions import Fraction as F
from collections import deque
import json,gzip,hashlib
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def read(p):return json.loads(p.read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def digest(x):return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def check_numeric(p):
    m=p['m'];assert m in (4,8)
    x=list(map(F,p['primal']));y=list(map(F,p['dual']))
    assert len(x)==m and len(y)==m+m*(m+1)//2 and all(v>=0 for v in x+y)
    even=p['mode']=='even_support';assert even or p['mode']=='adjacent_capacity'
    coefficients=[];caps=[]
    for n in range(1,m+1):
        coefficients.append([int(i==n) for i in range(1,m+1)]);caps.append(int(not even or n%2==0))
    for a in range(m):
        for b in range(a+1,m+1):
            coefficients.append([int(a<n<=b) for n in range(1,m+1)])
            caps.append(sum(n%2==0 for n in range(a+1,b+1)) if even else (b-a+1)//2)
    assert all(sum(c*v for c,v in zip(row,x))<=cap for row,cap in zip(coefficients,caps))
    assert all(sum(y[j]*coefficients[j][i] for j in range(len(y)))>=F(1,2**(i+1)) for i in range(m))
    upper=-sum(v/2**(i+1) for i,v in enumerate(x));dual=-sum(z*c for z,c in zip(y,caps))
    assert upper==dual==F(p['finite_optimum'])==F(p['full_upper'])
    assert F(p['uniform_tail_error'])==F(1,2**m)
    assert F(p['full_lower'])==dual-F(1,2**m)
    return dual-F(1,2**m),upper

def main():
    cp=OUT/'mixed-source-tail-certificate-contract.json';pp=OUT/'mixed-source-tail-certificate-packet.json';rp=OUT/'mixed-source-tail-certificate.json'
    c=read(cp);p=read(pp);r=read(rp)
    assert sha(cp)==r['contract_sha256'] and sha(pp)==r['packet_sha256']
    for name,h in c['input_sha256'].items():assert sha(ROOT/name)==h
    assert digest(c['task'])==c['task_sha256']
    source=read(OUT/'causal-interface-construction.json');base=read(OUT/'causal-interface-construction-contract.json')
    states=source['states'];transitions=source['transitions'];labels=base['labels']
    def amplitude(s):return F(1,2) if s[0]&4 else F(1)
    def verdict(s,partials):
        lower=F(0)
        for part in partials:
            assert part['context']=={'base':base['context'],'mixed_task_sha256':c['task_sha256']}
            assert part['cut']==s[0] and F(part['scale'])==amplitude(s)
            assert part['accepted_calibration_audit']==['audit-origin',part['origin']]
            expected='even_support' if part['channel']==part['origin'] else 'adjacent_capacity'
            assert part['lp']['mode']==expected and part['lp']['m']==4
            lo,hi=check_numeric(part['lp']);lower+=amplitude(s)*lo
            # Each partial has an admitted source realization at this cut.
            assert any(t[0]==s[0] and t[1]==part['origin'] for t in states)
        assert sorted(q['channel'] for q in partials)==[0,1]
        compatible=all(q['origin']==s[1] for q in partials)
        status=('INCOMPATIBLE_SOURCE' if not compatible else 'NOT_AUTHORIZED' if not s[0]&8 or s[3]!=s[1]
                else 'NO_STRICT_CERTIFICATE' if lower<=F(c['task']['threshold']) else 'CERTIFIED')
        return {'status':status,'lower':str(lower),'live_origins':[s[1]] if compatible else []}
    for case in p['cases']:
        s=states[case['source_state']];assert verdict(s,case['packets'])==case['result']
        # Verify that a genuine accepted base path reaches each publishing cut.
        todo=deque(source['initial_state_ids']);seen=set(todo)
        while todo:
            i=todo.popleft()
            for accepted,j in transitions[i]:
                if accepted and j not in seen:seen.add(j);todo.append(j)
        assert case['source_state'] in seen
    for example in p['counterexamples']:
        assert example['scale']=='1'
        values=[]
        for ch,packet in enumerate(example['channels']):
            assert packet['mode']==('even_support' if ch==example['origin'] else 'adjacent_capacity')
            values.append(check_numeric(packet)[1])
            # All constraints crossing the cutoff hold after zero extension:
            # these capacities are nondecreasing in the right endpoint. Test
            # an additional finite range as a control, not as the infinite proof.
            x=list(map(F,packet['primal']))+[F(0)]*8
            for a in range(16):
                for b in range(a+1,17):
                    cap=sum(n%2==0 for n in range(a+1,b+1)) if packet['mode']=='even_support' else (b-a+1)//2
                    assert sum(x[a:b])<=cap
        assert sum(values)==F(example['total'])==-F(255,256)<F(c['task']['threshold'])
    assert -F(3,4)>-F(31,32) and -F(15,16)>-F(31,32)
    assert -F(17,16)<-F(31,32)<-F(17,32)
    checks=0
    for i,s in enumerate(states):
        for label,(accepted,j) in zip(labels,transitions[i]):
            t=states[j];factor=F(1,2) if accepted and label[:2]==['source',2] else F(1)
            assert s[1]==t[1] and amplitude(t)==amplitude(s)*factor;checks+=1
    reverse=p['reverse_control'];i=reverse['predecessor_state'];j=reverse['successor_state'];label=labels.index(reverse['label'])
    assert transitions[i][label]==[True,j] and transitions[j][label]==[False,j]
    with gzip.open(ROOT/'voevodsky/results/decomposition-coherence-carriers.json.gz','rt') as f:carriers=json.load(f)
    for n,carrier in enumerate(carriers['carriers']):
        for i,s in enumerate(carrier['canonical_states']):
            result=p['regrouping_verdicts'][n][i]
            assert result['lower']==str(amplitude(s)*(-F(17,16))) and result['live_origins']==[s[1]]
            expected='NOT_AUTHORIZED' if not s[0]&8 or s[3]!=s[1] else 'CERTIFIED' if s[0]&4 else 'NO_STRICT_CERTIFICATE'
            assert result['status']==expected
    transport=0
    for f in carriers['comparisons']:
        for i,j in enumerate(f['map']):
            assert carriers['carriers'][f['from']]['canonical_states'][i]==carriers['carriers'][f['to']]['canonical_states'][j]
            assert p['regrouping_verdicts'][f['from']][i]==p['regrouping_verdicts'][f['to']][j];transport+=1
    assert transport==r['mixed_verdict_transport_checks']==189280
    # Independently make a corrupted dual and suffix, not just read statuses.
    sample=p['cases'][2]['packets'][0]['lp']
    for field in ('dual','uniform_tail_error'):
        bad=json.loads(json.dumps(sample))
        if field=='dual':bad[field][1]=str(F(bad[field][1])+1)
        else:bad[field]='0'
        try:check_numeric(bad)
        except AssertionError:pass
        else:raise AssertionError('bad arithmetic certificate accepted')
    result={'passed':True,'report_sha256':sha(rp),'mixed_cases_replayed':len(p['cases']),
      'source_tail_update_checks':checks,'regrouping_checks':transport,
      'counterexample':'A coherent admitted finite tail pair has value -255/256 below threshold -31/32.',
      'scope':c['scope'],'qualification':'Sound conditional mixed constructor, not provenance authentication or a correspondence for the actual prime task.'}
    (OUT/'mixed-source-tail-certificate-verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
