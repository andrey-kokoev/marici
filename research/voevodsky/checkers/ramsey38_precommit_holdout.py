"""Paired prospective retry: locally impossible disk transitions do not consume commitment."""
from ramsey38_large_pivot_holdout import P as last,previous,prior,old,select,apply_pin,compare,freeze,prev,json,sys
from ramsey38_tip_disk_domains import disks
P=prev.out/'ramsey38_precommit_predictions.json';B=prev.out/'ramsey38_precommit_control.json';R=prev.out/'ramsey38_precommit_comparison.json';C=prev.out/'ramsey38_precommit_control_comparison.json'
protocol='New canonical arrays after 1042. Stop at 24 arrays or three with replacement mesh proposals, whichever first, before checking fills. All ordered distinct edge targets. Both policies use same sorted collar candidates and largest-domain one pin. Control commits at first final-disk pass. Retry skips ONLY candidates with a vertex lacking a single compatible before/after disk pair (before neighbor propagation); it then tries the next ranked candidate. No retry on joint agreement or mesh selection failure. Compare exact plans against arbitrary-length append-only census.'
def blocker(L,rs,z):
    dec=lambda m:frozenset(v for i,v in enumerate(L) if m>>i&1);x,v=z['first'];y,t=z['second'];r1={**rs,x:rs[x]|1<<L.index(v)};r2={**r1,y:r1[y]|1<<L.index(t)};need=dec(rs[x])|{z['tip']};E=set(map(frozenset,z['collar']));B=set(map(dec,z['bd']));F=set(map(dec,z['end']))
    for i in L:
        ends=set(disks(L,i,F,set(map(dec,r2.values()))|E|{need}));extra={s for s in E if i in s}
        if not any(not s&E and s|extra in ends for s in disks(L,i,B,set(map(dec,r1.values()))|{need})):return i

def both(e,L,rs,candidates):
    ctl=None;skipped=[];result=dict(commit=None,pick=None,pin=None)
    for candidate in candidates:
        base=select(e,L,rs,[candidate]);q=base['commit']
        if not q:continue
        current=apply_pin(e,base,True)
        if ctl is None:ctl=current
        # Nonempty reduced domains imply that each raw domain was nonempty.
        b=None if all(base['sizes'].values()) else blocker(L,rs,q)
        if b is not None:skipped.append(dict(commit=q,vertex=b));continue
        result=current;break
    return dict(result,control=ctl or dict(commit=None,pick=None,pin=None),skipped=skipped)
def done(es):return len(es)>=24 or sum(any(d['skipped'] and d['pick'] for d in e['requests']) for e in es)>=3
if __name__=='__main__':
    if sys.argv[1]=='freeze':
        freeze(1042,(old,prior,previous,last),both,P,protocol,done);data=json.loads(P.read_text());data['paired_sha']=prev.sha(P.read_bytes());
        for e in data['cases']:e['requests']=[dict(j=d['j'],l=d['l'],**d['control']) for d in e['requests']]
        prev.save(B,data)
    elif sys.argv[1]=='compare':compare(P,R);compare(B,C)
