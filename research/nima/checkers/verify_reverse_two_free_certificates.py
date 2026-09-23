"""Checks reverse transport independently, without translator or solver imports."""
from fractions import Fraction as Q
from pathlib import Path
import json,gzip,hashlib,copy
from verify_two_free_schema_bridge import expected_translation,check
from verify_two_free_tail_queries import verify,reconstruct
if not __debug__:raise RuntimeError('Assertions required')
OUT=Path(__file__).resolve().parents[1]/'results'
def size(x):return len(json.dumps(x,sort_keys=True,separators=(',',':')).encode())
def replay(request,case):
    origin=request['state'];m=origin['m'];free=origin['free'];pins={k:Q(h) for k,h in origin['pins']}
    target=expected_translation(origin);residual=reconstruct(origin)
    assert len(case['input'])==len(case['ledger'])==2
    verified=verify(origin,request['query'],case['output']);assert verified==request['status']
    for slot,(sign,proof) in enumerate(zip((-1,1),case['input'])):
        obj=['0']*(m+2);obj[2+free[0]]=str(sign)
        check(target,{'kind':'maximize','objective':obj},proof)
        # Construct the row map in residual order, independently of the
        # translator's per-input branching.
        correspondence={2*free[0]+1:0,2*free[0]:1,2*free[1]+1:2,2*free[1]:3}
        for n in range(len(residual)-4):correspondence[2*m+2*len(pins)+n]=4+n
        combined={};slack=Q(0);removed=0
        for index,raw in proof['weights']:
            w=Q(raw)
            if index in correspondence:
                k=correspondence[index];combined[k]=combined.get(k,Q(0))+w
            else:
                removed+=1
                if index<2*m:
                    atom=index//2;assert atom in pins
                    slack+=w*(Q(100+2*atom)-pins[atom] if index%2==0 else pins[atom])
                else:assert 2*m<=index<2*m+2*len(pins)
        terms=[[k,str(v)] for k,v in sorted(combined.items()) if v]
        ledger=case['ledger'][slot]
        assert ledger=={'constant_removed':str(slack),'input_terms':len(proof['weights']),'removed_terms':removed,'output_terms':len(terms)}
        n=tuple(sum(Q(v)*residual[k][0][j] for k,v in terms) for j in (0,1))
        b=sum((Q(v)*residual[k][1] for k,v in terms),Q(0))
        if proof['status']=='EMPTY':
            assert verified=='INCONSISTENT' and n==(0,0) and b<0
            if slot==0:assert case['output']['result']['farkas']==terms
        else:
            assert slack==0 and n==(sign,0) and b==Q(proof['value'])
            output=case['output']['result']['minimum' if sign==-1 else 'maximum']
            assert output['dual']==terms and output['value']==proof['value']
            assert output['point']==[proof['x'][k] for k in free]
    assert case['input_pair_bytes']==size(case['input']) and case['output_packet_bytes']==size(case['output'])

def main():
    contract=json.loads((OUT/'reverse-two-free-contract.json').read_text())
    for p,h in contract['bindings'].items():assert hashlib.sha256(Path(p).read_bytes()).hexdigest()==h
    requests=json.loads((OUT/'two-free-tail-query-contract.json').read_text())['requests']
    raw=(OUT/'reverse-two-free-packet.json.gz').read_bytes();report=json.loads((OUT/'reverse-two-free.json').read_text())
    assert hashlib.sha256(raw).hexdigest()==report['packet_sha256'];cases=json.loads(gzip.decompress(raw))
    names={n for n,r in requests.items() if r['state']['m']<=8}
    expected={(n,v) for n in names for v in ('transported','simplex-with-disclosed-fallback')}
    expected|={('m3-worst-at','pin-equality-cycle'),('inconsistent','positive-constant-slack')}
    assert len(cases)==len(expected)==94 and {(c['name'],c['variant']) for c in cases}==expected
    for case in cases:replay(requests[case['name']],case)
    positive=next(c for c in cases if c['variant']=='positive-constant-slack')
    assert all(Q(l['constant_removed'])>0 for l in positive['ledger'])
    control=next(c for c in cases if c['name']=='m3-worst-at' and c['variant']=='transported');rejected=[]
    for defect in ('state','objective','weight','output','ledger','extra-row'):
        bad=copy.deepcopy(control)
        if defect=='state':bad['input'][0]['state']['frames'].pop()
        if defect=='objective':bad['input'][0]['query']['objective'][0]='1'
        if defect=='weight':bad['input'][0]['weights'][0][1]='-1'
        if defect=='output':bad['output']['result']['maximum']['value']='999'
        if defect=='ledger':bad['ledger'][0]['constant_removed']='1'
        if defect=='extra-row':bad['input'][0]['state']['frames'].append({'a':['0']*5,'b':'0'})
        try:replay(requests[control['name']],bad)
        except (AssertionError,ValueError,KeyError,IndexError):rejected.append(defect)
        else:raise AssertionError('invalid reverse transport accepted')
    result={'passed':True,'pairs':len(cases),'objective_translations':2*len(cases),
            'positive_constant_farkas_controls':2,'attacks_rejected':rejected,
            'scope':'Exact translated pinned states only; no inverse claim for arbitrary general packets or witness syntax.'}
    (OUT/'reverse-two-free-verification.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
