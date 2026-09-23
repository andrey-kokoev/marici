"""Precision states proposed through the joint finite-dictionary backend."""
from pathlib import Path
from fractions import Fraction as Q
import sys,json,gzip,hashlib,copy
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
sys.path.insert(0,str(ROOT/'grothendieck/checkers'))
from joint_audit_tail_interface import JointAuditModel
from check_two_free_schema_bridge import translate as full_translation,transport
from verify_two_free_tail_queries import verify as verify_precision
from verify_schema_relative_tail_lp import check as verify_source

def recover_inconsistency(request,specialized,sign):
    """Certificate-only fallback; never infer emptiness from a solver error."""
    origin=request['state']
    if verify_precision(origin,request['query'],specialized)!='INCONSISTENT':
        raise ValueError('NO_VERIFIED_EMPTINESS_PROOF')
    target=full_translation(origin);objective=['0']*(origin['m']+2)
    objective[origin['free'][0]+2]=str(sign)
    query={'kind':'maximize','objective':objective}
    certificate=transport(origin,target,query,specialized,'minimum')
    verify_source(target,query,certificate)
    assert certificate['status']=='EMPTY'
    return certificate

def translate(origin):
    m=origin['m'];i,j=origin['free'];audits=[k for k,h in origin['pins']]
    slopes=[Q(1,128**k) for k in range(m)];gap=slopes[i]-slopes[j]
    def encode(source):
        v=(source[i]-source[j])/gap;u=source[i]-slopes[i]*v
        return tuple([u,v]+[source[k]-u-slopes[k]*v for k in audits])
    frames=[]
    for f in full_translation(origin)['frames']:
        a=list(map(Q,f['a']));source=[a[0]+a[1]*slopes[k]+a[k+2] for k in range(m)]
        frames.append((encode(source),Q(f['b'])))
    objective=encode([Q(int(k==i)) for k in range(m)])
    return audits,frames,objective

def main():
    cp=OUT/'two-free-tail-query-contract.json';sp=OUT/'two-free-tail-query-packet.json.gz'
    c=json.loads(cp.read_text());specialized=json.loads(gzip.decompress(sp.read_bytes()))
    names=[n for n,r in c['requests'].items() if r['state']['m']<=8]
    bindings={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (cp,sp,Path(__file__),ROOT/'grothendieck/checkers/joint_audit_tail_interface.py')}
    contract={'schema':'precision-joint-bridge-v1','cases':names,'bindings':bindings,
      'schema_rule':'Expose exactly the supplied pinned indices; encode free atoms by the exact residual inverse.',
      'scope':'Precision interface to joint lazy optimization; operational failures are not mathematical answers.'}
    (OUT/'precision-joint-bridge-contract.json').write_text(json.dumps(contract,indent=2)+'\n')
    packets={}
    for name in names:
        req=c['requests'][name];origin=req['state'];A,frames,obj=translate(origin);model=JointAuditModel(origin['m'],A);answers=[]
        for sign in (-1,1):
            try:
                answer=model.maximize(frames,tuple(sign*v for v in obj))
                answers.append({'status':'PROPOSED','answer':answer})
            except Exception as error:
                failure={'error_type':type(error).__name__,'message':str(error)}
                if specialized[name]['result']['status']=='INCONSISTENT':
                    certificate=recover_inconsistency(req,specialized[name],sign)
                    answers.append({'status':'SOURCE_FARKAS_FALLBACK','primary_failure':failure,'certificate':certificate})
                else:
                    answers.append({'status':'PROPOSAL_FAILED',**failure})
                print(name,sign,type(error).__name__,answers[-1]['status'],flush=True)
        packets[name]={'origin':origin,'query':req['query'],'audits':A,
                       'frames':[{'normal':list(map(str,a)),'upper':str(b)} for a,b in frames],
                       'objective':list(map(str,obj)),'specialized':specialized[name],'joint':answers}
    # A solver failure or a claimed EMPTY tag cannot replace an actual ray.
    for name,proof in [('wide',specialized['wide']),('inconsistent',copy.deepcopy(specialized['inconsistent']))]:
        if name=='inconsistent':proof['result']['farkas']=[]
        try:recover_inconsistency(c['requests'][name],proof,-1)
        except (AssertionError,ValueError):pass
        else:raise AssertionError('unjustified fallback accepted')
    pp=OUT/'precision-joint-bridge-packet.json.gz';pp.write_bytes(gzip.compress(json.dumps(packets,separators=(',',':')).encode(),mtime=0))
    report={'fallback_admission_rejections':2,'cases':len(packets),'proposed':sum(a['status']=='PROPOSED' for p in packets.values() for a in p['joint']),
            'source_farkas_fallbacks':sum(a['status']=='SOURCE_FARKAS_FALLBACK' for p in packets.values() for a in p['joint']),
            'primary_proposal_failures':sum(a['status']!='PROPOSED' for p in packets.values() for a in p['joint']),
            'proposal_failures':sum(a['status']=='PROPOSAL_FAILED' for p in packets.values() for a in p['joint']),
            'packet_sha256':hashlib.sha256(pp.read_bytes()).hexdigest()}
    (OUT/'precision-joint-bridge.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
if __name__=='__main__':main()
