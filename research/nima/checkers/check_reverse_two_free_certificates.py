"""Replay both proposal sources through algebraic reverse transport."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,copy
from reverse_two_free_certificates import reverse_pair
OUT=Path(__file__).resolve().parents[1]/'results'
def size(x):return len(json.dumps(x,sort_keys=True,separators=(',',':')).encode())
def main():
    cp=OUT/'two-free-tail-query-contract.json';bp=OUT/'two-free-schema-bridge-packet.json.gz'
    requests=json.loads(cp.read_text())['requests'];bridge=json.loads(gzip.decompress(bp.read_bytes()));cases=[]
    def add(name,variant,proofs):
        request=requests[name];output,ledger=reverse_pair(request['state'],request['query'],proofs)
        assert output['result']['status']==request['status']
        if 'interval' in request:assert output['result']['interval']==request['interval']
        cases.append({'name':name,'variant':variant,'input':proofs,'output':output,'ledger':ledger,
                      'input_pair_bytes':size(proofs),'output_packet_bytes':size(output)})
    for name,p in bridge.items():
        add(name,'transported',p['general'])
        add(name,'simplex-with-disclosed-fallback',[s['certificate'] if s['status']=='VERIFIED' else g for s,g in zip(p['simplex'],p['general'])])
    # Non-normalized proof forms: arbitrary zero pin-equality cycles.
    proofs=copy.deepcopy(bridge['m3-worst-at']['general'])
    for proof in proofs:
        weights={k:Q(v) for k,v in proof['weights']}
        for k in (6,7):weights[k]=weights.get(k,Q(0))+7
        proof['weights']=[[k,str(v)] for k,v in sorted(weights.items())]
    add('m3-worst-at','pin-equality-cycle',proofs)
    # Add a positive constant to a Farkas combination, leaving it negative.
    proofs=copy.deepcopy(bridge['inconsistent']['general'])
    for proof in proofs:
        # In this state atom 0 is pinned to 1. cap row 0 plus pin row 7
        # has zero normal and bound 99. Recover the old bound directly.
        state=proof['state'];m=state['m'];bound=Q(0)
        for k,v in proof['weights']:
            b=Q(100+2*(k//2)) if k<2*m and k%2==0 else Q(0) if k<2*m else Q(state['frames'][k-2*m]['b'])
            bound+=Q(v)*b
        assert bound<0;delta=-bound/198;weights={k:Q(v) for k,v in proof['weights']}
        for k in (0,7):weights[k]=weights.get(k,Q(0))+delta
        proof['weights']=[[k,str(v)] for k,v in sorted(weights.items())]
    add('inconsistent','positive-constant-slack',proofs)
    contract={'bindings':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (cp,bp,Path(__file__).with_name('reverse_two_free_certificates.py'))},
              'domain':'Exact translated full-schema states; +/- first free atom; checked explicit dual/Farkas row weights.',
              'solver_calls_in_translation':0,'size_convention':'Compact JSON bytes; two input objective packets versus one output audit packet, including statements.'}
    (OUT/'reverse-two-free-contract.json').write_text(json.dumps(contract,indent=2)+'\n')
    raw=gzip.compress(json.dumps(cases,separators=(',',':')).encode(),mtime=0)
    (OUT/'reverse-two-free-packet.json.gz').write_bytes(raw)
    report={'cases':len(cases),'objective_translations':2*len(cases),'packet_sha256':hashlib.sha256(raw).hexdigest(),
            'max_input_pair_bytes':max(x['input_pair_bytes'] for x in cases),'max_output_packet_bytes':max(x['output_packet_bytes'] for x in cases),
            'max_input_terms':max(l['input_terms'] for x in cases for l in x['ledger']),
            'max_output_terms':max(l['output_terms'] for x in cases for l in x['ledger']),
            'scope':'No optimizer calls; explicit statement validation and arithmetic replay remain charged.'}
    (OUT/'reverse-two-free.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
