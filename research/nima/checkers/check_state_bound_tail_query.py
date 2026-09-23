"""Freeze and exercise the owning state/query/certificate API boundary."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib,copy
from check_symbolic_tail_interface import RetainedInterface,canonical_digest
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def main():
    engine=Path(__file__).with_name('check_symbolic_tail_interface.py');source=ROOT/'grothendieck/results/two-moment-tail-complexity.json'
    binding=sha(source)+':known-control-run';points=[['0','0'],['25','25'],['50','25'],['50','50'],['75','75'],['-1','0'],['0','-1'],['0','1']]
    requests={}
    def request(name,m,stage,kind,values):
        requests[name]={'expected_m':m,'expected_stage':stage,'expected_query':{'kind':kind,'point' if kind=='point-membership' else 'objective':values}}
    for name,m,stage,point in [('stale_history',2,1,points[4]),('wrong_source_size',3,0,points[0]),('foreign_source_binding',2,0,points[0]),
        ('wrong_query',2,1,points[4]),('resealed_query_lift_reuse',2,0,points[4]),('omitted_frame_resealed',2,3,points[2]),
        ('forged_frame_exclusion',2,2,points[0]),('corrupt_source_separator',2,0,points[7]),('corrupt_source_lift',2,0,points[1])]:
        request(name,m,stage,'point-membership',point)
    request('omitted_maximum_frame',2,3,'linear-maximum',['0','1'])
    contract={'schema':'state-bound-tail-query-test-v1','engine_sha256':sha(engine),'source_sha256':sha(source),
      'source_binding':binding,'m_values':[2,3,16,1024],'points':points,'objectives':[['0','1'],['1','-1']],
      'history':[[['1','0'],'50'],[['-1','0'],'-25'],[['-1/2','1'],'0'],[['0','-1'],'-30']],
      'states':'all five prefixes of the fixed history','attack_requests':requests,
      'trust':'Verifier receives the expected immutable state descriptor and exact request from an independent caller. Never derive the expected history from the certificate.',
      'binding':'Canonical exact rational state and query serialization, with source binding, m and every ordered frame. Hashes bind statements, not truth or origin of frames.',
      'scope':'Certified membership and linear optimization for the existing source-relative filling-family interface. No authentication or actual-source selection.'}
    cp=OUT/'state-bound-tail-query-contract.json';save(cp,contract)
    cases=[];lookup={};snapshots={}
    for m in contract['m_values']:
        state=RetainedInterface(m,source_binding=binding)
        for stage in range(5):
            snapshots[m,stage]=state
            for kind,queries in [('point-membership',points),('linear-maximum',contract['objectives'])]:
                for qi,values in enumerate(queries):
                    packet=state.member(values) if kind=='point-membership' else state.certify_maximum(values)
                    record={'m':m,'stage':stage,'kind':kind,'query_index':qi,'certificate':packet};cases.append(record);lookup[m,stage,kind,qi]=packet
            if stage<4:
                before=state;state=state.refine(*contract['history'][stage]);assert len(before.frames)==stage
    def cert(m,stage,qi,kind='point-membership'):return copy.deepcopy(lookup[m,stage,kind,qi])
    def reseal(packet):
        packet['state_digest']=canonical_digest(packet['state'])
        packet['query_digest']=canonical_digest({'state_digest':packet['state_digest'],'query':packet['query']})
    attacks=[]
    def attack(name,packet):attacks.append({'name':name,**requests[name],'certificate':packet})
    attack('stale_history',cert(2,0,4));attack('wrong_source_size',cert(2,0,0));attack('foreign_source_binding',cert(2,0,0))
    attack('wrong_query',cert(2,1,1))
    bad=cert(2,0,1);bad['query']=requests['resealed_query_lift_reuse']['expected_query'];reseal(bad);attack('resealed_query_lift_reuse',bad)
    bad=cert(2,3,2);del bad['state']['frames'][0];reseal(bad);attack('omitted_frame_resealed',bad)
    bad=cert(2,2,0);bad['result'].update(frame_index=0,lhs='0',upper='50');attack('forged_frame_exclusion',bad)
    bad=cert(2,0,7);bad['result']['separator']['upper']=str(Q(bad['result']['separator']['upper'])+1);attack('corrupt_source_separator',bad)
    bad=cert(2,0,1);bad['result']['lift']['theta']='2';attack('corrupt_source_lift',bad)
    bad=cert(2,3,0,'linear-maximum');rows=bad['result']['rows'];del rows[next(i for i,row in enumerate(rows) if row['kind']=='frame')];attack('omitted_maximum_frame',bad)
    # Nested caller input cannot mutate a constructed snapshot.
    external=[[[1,0],50]];isolated=RetainedInterface(2,external,binding);old=isolated.descriptor()
    external[0][0][0]=0;external[0][1]=-1;assert isolated.descriptor()==old
    assert not isolated.member([75,75])['result']['admitted']
    invalid_inputs=0
    for operation in (lambda:isolated.member([0,0,0]),lambda:isolated.refine([0,0,1],0),
                      lambda:isolated.member([0.1,0]),lambda:isolated.member([True,0]),
                      lambda:isolated.certify_maximum([0,0,1]),lambda:RetainedInterface(2,source_binding='')):
        try:operation()
        except ValueError:invalid_inputs+=1
        else:raise AssertionError('invalid query/state input admitted')
    packet={'cases':cases,'attacks':attacks,'snapshot_input_copy_checked':True,'invalid_input_controls':invalid_inputs}
    pp=OUT/'state-bound-tail-query-packet.json.gz';pp.write_bytes(gzip.compress(json.dumps(packet,separators=(',',':')).encode(),mtime=0))
    result={'verdict':'STATE_BOUND_QUERY_PACKETS_CONSTRUCTED','contract_sha256':sha(cp),'packet_sha256':sha(pp),
      'query_certificates':len(cases),'adversarial_packets':len(attacks),'invalid_input_controls':invalid_inputs,
      'snapshot_input_copy_checked':True,'scope':contract['scope'],
      'qualification':'Independent verification is a separate command; packet-provided history is never the expected-history authority.'}
    save(OUT/'state-bound-tail-query.json',result);print(json.dumps(result,indent=2))
if __name__=='__main__':main()
