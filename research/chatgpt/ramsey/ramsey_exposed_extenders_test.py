"""Conjecture 1: inspect ALL missed sixes for every failed quadruple on the calibrated thinned core. Do not infer a negative result from the first missed row."""
from collections import Counter
from functools import lru_cache
from ramsey_final_miss_levels import levels,bits,D,json
from ramsey_fork_audit_uniform import inds,grow

def run():
    p=json.loads((D/'ramsey_pure_port_fork.json').read_text());H=grow(p['stem_graphs'][-1],p['alternate']['to34']);F=(1<<34)-1;rows=[t for t in inds(H) if t.bit_count()==6];failed=[];shapes=Counter();unique=set()
    @lru_cache(None)
    def info(t):
        ban=t
        for v in bits(t):ban|=H[v]
        x=F^ban;deg=[(H[v]&x).bit_count() for v in bits(x)];assert max(deg,default=0)<=1;return x,sum(deg)//2
    def inspect(S,tag,obs):
        if tag!='fails_four':return
        union=S[0]|S[1]|S[2]|S[3];missing=[t for t in rows if not t&union];assert obs in missing;details=[]
        for t in missing:
            x,e=info(t);shapes[x.bit_count(),e]+=1;unique.add(t);details.append(dict(row=t,extenders=x,edges=e))
        failed.append(dict(supports=S,edge_witnesses=sum(r['edges']>0 for r in details),rows=details))
    levels(H,on_classified=inspect);assert len(failed)==404;return dict(tested=len(failed),pass_count=sum(r['edge_witnesses']>0 for r in failed),distinct_rows=len(unique),shape_occurrences={str(k):v for k,v in sorted(shapes.items())},failures=failed)
if __name__=='__main__':
    out=run();print({k:v for k,v in out.items() if k!='failures'});print(next((q for q in out['failures'] if not q['edge_witnesses']),None));(D/'ramsey_exposed_extenders_test.json').write_text(json.dumps(out)+'\n')
