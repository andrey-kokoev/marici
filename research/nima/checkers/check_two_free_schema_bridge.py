"""Translate the precision backend to the general exact simplex reference."""
from pathlib import Path
import sys,json,gzip,hashlib
from fractions import Fraction as Q
from verify_two_free_tail_queries import reconstruct
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
sys.path.insert(0,str(ROOT/'voevodsky/checkers'))
from check_simplex_schema_tail import certify
from check_schema_relative_tail_lp import rows
from verify_schema_relative_tail_lp import check

def transport(origin,target,query,specialized,side):
    """Lift a planar dual/Farkas proof by adding exact-pin equality terms."""
    m=origin['m'];free=origin['free'];pins=origin['pins'];rs=rows(target)
    result=specialized['result'];empty=result['status']=='INCONSISTENT'
    proof=result if empty else result[side]
    terms=proof['farkas'] if empty else proof['dual'];weights={}
    cap_map=[2*free[0]+1,2*free[0],2*free[1]+1,2*free[1]]
    for index,value in terms:
        k=cap_map[index] if index<4 else 2*m+2*len(pins)+index-4
        weights[k]=weights.get(k,Q(0))+Q(value)
    normal=[sum(w*rs[k][0][j] for k,w in weights.items()) for j in range(m)]
    for ordinal,(j,h) in enumerate(pins):
        coefficient=normal[j]
        if coefficient:
            k=2*m+2*ordinal+(1 if coefficient>0 else 0)
            weights[k]=abs(coefficient)
    packet={'state':target,'query':query,'weights':[[k,str(v)] for k,v in sorted(weights.items()) if v]}
    if empty:packet['status']='EMPTY'
    else:
        x={j:h for j,h in pins};x.update(zip(free,proof['point']))
        packet.update(status='FEASIBLE_OPTIMUM',x=[str(x[j]) for j in range(m)],value=proof['value'])
    return packet

def translate(state):
    reconstruct(state)  # Validate the supported source-state language.
    m=state['m'];frames=[]
    def append(a,b):frames.append({'a':list(map(str,a)),'b':str(b)})
    for j,value in state['pins']:
        a=[Q(0)]*(m+2);a[j+2]=Q(1);h=Q(value)
        append(a,h);append([-v for v in a],-h)
    for event in state['evidence']:
        if event['kind']=='measurement_box':
            for k in range(2):
                a=[Q(0)]*(m+2);a[k]=Q(1);c=Q(event['center'][k]);e=Q(event['error'][k])
                append(a,c+e);append([-v for v in a],-c+e)
        else:
            a=[Q(0)]*(m+2)
            for j,value in zip(state['free'],event['normal']):a[j+2]=Q(value)
            append(a,Q(event['upper']))
    return {'m':m,'audits':list(range(m)),'frames':frames,'source':'tail-box-100+2j-128^-j-v1'}

def main():
    cp=OUT/'two-free-tail-query-contract.json';pp=OUT/'two-free-tail-query-packet.json.gz'
    c=json.loads(cp.read_text());source_packets=json.loads(gzip.decompress(pp.read_bytes()))
    names=[name for name,r in c['requests'].items() if r['state']['m']<=8]
    contract={'schema':'two-free-schema-bridge-v1','input_contract_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),
              'input_packet_sha256':hashlib.sha256(pp.read_bytes()).hexdigest(),'cases':names,
              'scope':'Exact pins and retained linear evidence translated to a full atom-audit schema; materialized reference rows.'}
    (OUT/'two-free-schema-bridge-contract.json').write_text(json.dumps(contract,indent=2)+'\n')
    packets={}
    for name in names:
        request=c['requests'][name];state=request['state'];target=translate(state);proofs=[];simplex=[]
        for sign,side in ((-1,'minimum'),(1,'maximum')):
            objective=['0']*(state['m']+2);objective[2+state['free'][0]]=str(sign)
            query={'kind':'maximize','objective':objective}
            proof=transport(state,target,query,source_packets[name],side);check(target,query,proof);proofs.append(proof)
            try:
                candidate=certify(target,query);check(target,query,candidate)
                simplex.append({'status':'VERIFIED','certificate':candidate})
            except Exception as error:
                simplex.append({'status':'PROPOSAL_FAILED','error_type':type(error).__name__,'message':str(error)})
                print(name,side,type(error).__name__,flush=True)
        packets[name]={'origin':state,'query':request['query'],'specialized':source_packets[name],'general':proofs,'simplex':simplex}
    path=OUT/'two-free-schema-bridge-packet.json.gz'
    path.write_bytes(gzip.compress(json.dumps(packets,separators=(',',':')).encode(),mtime=0))
    result={'cases':len(packets),'general_certificates':2*len(packets),
            'simplex_verified':sum(s['status']=='VERIFIED' for p in packets.values() for s in p['simplex']),
            'simplex_proposal_failures':sum(s['status']=='PROPOSAL_FAILED' for p in packets.values() for s in p['simplex']),
            'packet_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
            'scope':contract['scope']}
    (OUT/'two-free-schema-bridge.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
