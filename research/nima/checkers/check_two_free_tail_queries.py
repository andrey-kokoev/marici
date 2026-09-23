"""Freeze requests before solving; test margins, cap clipping and refinement."""
from pathlib import Path
from fractions import Fraction as Q
import json,gzip,hashlib
from two_free_tail_queries import TwoFreeTail
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'nima/results'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def main():
    source=ROOT/'grothendieck/results/two-moment-tail-complexity.json';binding=sha(source)+':precision-control'
    requests={};jobs={}
    def base(m,free):return TwoFreeTail(m,free,[(j,Q(1)) for j in range(m) if j not in free],binding)
    def center(state,x=Q(20),y=Q(30)):
        i,j=state.free
        return (sum((v for k,v in state.pins),Q(0))+x+y,
                sum((v/128**k for k,v in state.pins),Q(0))+x/128**i+y/128**j)
    def add(name,state,h,status,interval=None):
        query={'kind':'free-atom-threshold','atom':state.free[0],'relation':'<=','threshold':str(h)}
        request={'state':state.descriptor(),'query':query,'status':status}
        if interval is not None:request['interval']=list(map(str,interval))
        requests[name]=request;jobs[name]=(state,h)
    for m in (3,4,8,16,64,1024):
        d=Q(1,128**(m-2))-Q(1,128**(m-1))
        for placement,free in [('best',(0,m-1)),('worst',(m-2,m-1))]:
            root=base(m,free);gap=Q(1,128**free[0])-Q(1,128**free[1]);c=center(root)
            for name,error in [('exact',Q(0)),('below',d/2),('at',d),('above',2*d)]:
                rho=error/gap;lo,hi=20-rho,20+rho
                add(f'm{m}-{placement}-{name}',root.measure(c,(0,error)),Q(21),'FORCED_TRUE' if hi<=21 else 'UNRESOLVED',(lo,hi))
        root=base(m,(m-2,m-1));s=Q(1,128**(m-1));c=center(root)
        simultaneous=root.measure(c,(Q(1,4),d-s/4))
        add(f'm{m}-simultaneous',simultaneous,Q(21),'FORCED_TRUE',(19,21))
        at=root.measure(c,(0,d))
        add(f'm{m}-false',at,Q(18),'FORCED_FALSE',(19,21))
        add(f'm{m}-lower-equality',at,Q(19),'UNRESOLVED',(19,21))
    root=base(3,(1,2));d=Q(1,128)-Q(1,16384);c=center(root)
    wide=root.measure(c,(0,2*d));narrow=wide.measure(c,(0,d/2))
    add('wide',wide,Q(21),'UNRESOLVED',(18,22))
    add('narrow',narrow,Q(21),'FORCED_TRUE',(Q(39,2),Q(41,2)))
    add('narrow-then-wide',narrow.measure(c,(0,2*d)),Q(21),'FORCED_TRUE',(Q(39,2),Q(41,2)))
    add('linear-refined',wide.refine((1,0),20),Q(21),'FORCED_TRUE',(18,20))
    add('x-cap-clipped',root.measure(center(root,Q(0),Q(30)),(0,d)),Q(1),'FORCED_TRUE',(0,1))
    add('y-cap-clipped',root.measure(center(root,Q(20),Q(0)),(0,d)),Q(20),'FORCED_TRUE',(19,20))
    add('y-upper-clipped',root.measure(center(root,Q(20),Q(104)),(0,d)),Q(20),'UNRESOLVED',(20,21))
    offset=center(root,Q(0),Q(0))
    add('inconsistent',root.measure((offset[0]-1,offset[1]),(0,0)),Q(21),'INCONSISTENT')
    add('zero-row-inconsistent',wide.refine((0,0),-1),Q(21),'INCONSISTENT')
    add('point',root.measure(c,(0,0)),Q(20),'FORCED_TRUE',(20,20))
    # A line and a singleton still have ambient planar vertices and certificates.
    add('line',root.refine((1,1),50).refine((-1,-1),-50),Q(20),'UNRESOLVED',(0,50))
    add('singleton',root.refine((1,0),0).refine((0,1),0),Q(0),'FORCED_TRUE',(0,0))
    add('no-pins-m2',base(2,(0,1)).refine((1,0),20),Q(20),'FORCED_TRUE',(0,20))
    contract={'schema':'two-free-tail-query-tests-v1','source_sha256':sha(source),
      'backend_sha256':sha(Path(__file__).with_name('two_free_tail_queries.py')),
      'lp_engine_sha256':sha(Path(__file__).with_name('check_symbolic_tail_interface.py')),
      'requests':requests,'precision':'Coordinatewise full-moment error box in original normalization; exact pins.',
      'scope':'Two free atoms; exact planar source-space LP with all retained closed linear evidence. No noisy pins or acquisition authentication.'}
    cp=OUT/'two-free-tail-query-contract.json';save(cp,contract) # BEFORE executing queries
    packets={}
    for name,(state,h) in jobs.items():
        packet=state.audit(h);assert packet['state']==requests[name]['state'] and packet['query']==requests[name]['query']
        assert packet['result']['status']==requests[name]['status']
        if 'interval' in requests[name]:assert packet['result']['interval']==requests[name]['interval']
        packets[name]=packet
    assert len(wide.evidence)==1 and len(narrow.evidence)==2
    invalid=0
    for operation in (lambda:root.measure(c,(-1,0)),lambda:root.measure(c,(0.1,0)),
                      lambda:root.audit(True),lambda:root.refine((0,0,1),0),
                      lambda:TwoFreeTail(3,(1,2),[],binding),lambda:TwoFreeTail(3,(1,2),[(0,101)],binding),
                      lambda:TwoFreeTail(3,(1,2),[(0,1),(0,1)],binding)):
        try:operation()
        except ValueError:invalid+=1
        else:raise AssertionError('invalid input accepted')
    pp=OUT/'two-free-tail-query-packet.json.gz';pp.write_bytes(gzip.compress(json.dumps(packets,separators=(',',':')).encode(),mtime=0))
    report={'certificates':len(packets),'contract_sha256':sha(cp),'packet_sha256':sha(pp),'invalid_inputs_rejected':invalid,
            'scope':contract['scope'],'qualification':'Independent certificate replay is a separate command.'}
    save(OUT/'two-free-tail-query.json',report);print(json.dumps(report,indent=2))
if __name__=='__main__':main()
