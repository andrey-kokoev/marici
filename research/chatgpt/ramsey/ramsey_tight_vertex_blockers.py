"""Test one-step vertex blocking, and its sound iterative closure: restrict each tight row to surviving vertices; delete x if all remaining options in one row are neighbours of x. Never treat x as a neighbour of itself."""
from collections import Counter
from ramsey_fork_audit_uniform import grow,inds,D,json

def audit(H,T,q):
    a,b,c=q;rows=[s for size,ss in T.items() for s in ss if int(not a&s)+int(not b&s)+int(not c&s)==9-size];live=(1<<len(H))-1;rounds=[]
    while True:
        options={s&live for s in rows};small=sorted(options,key=int.bit_count);blocked={x:next((t for t in small if t&~h==0),None) for x,h in enumerate(H) if live>>x&1};blocked={x:t for x,t in blocked.items() if t is not None};rounds.append(list(blocked));live &= ~sum(1<<x for x in blocked);fail=next((t for t in rows if not t&live),None)
        if fail or not blocked:break
    return dict(rounds=rounds,empty=fail,tight=len(rows),min_surviving=min((s&live).bit_count() for s in rows),survivors=live)

def run():
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=grow(p['stem_graphs'][-1],p['alternate']['to34']);T={k:[] for k in [6,7,8]}
    for t in inds(H):
        if t.bit_count() in T:T[t.bit_count()].append(t)
    rows=json.loads((D/'ramsey_compulsory_kernel_test.json').read_text())['triples'];out=[];hist=Counter()
    for r in rows:
        q=r['triple'];v=audit(H,T,q);ok=bool(r['maximal_count']);assert not(ok and v['empty']);hist[ok,len(v['rounds']) if v['empty'] else 0]+=1;out.append(dict(fixed=q,repairable=ok,**v))
    return dict(hist={str(k):v for k,v in hist.items()},rows=out)
if __name__=='__main__':
    out=run();print(out['hist']);(D/'ramsey_tight_vertex_blockers.json').write_text(json.dumps(out)+'\n')
