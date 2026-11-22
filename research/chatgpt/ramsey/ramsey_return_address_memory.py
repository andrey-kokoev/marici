"""Check whether the two proposed return policies can be read as fixed matching lookups, vertex successors, or deterministic finite-window successors on their full periodic Hall walks. Enumerate all six initial transit contexts jointly."""
from collections import defaultdict
from ramsey_fork_missing_corner import D,json

def test():
    src=json.loads((D/'ramsey_join_nonreturn_scale.json').read_text());steps={tuple(r['previous'][::2]):r['onward_no_flag_reversal'] for r in src};out={}
    pooled=set()
    for policy in ('inherit','previous','either'):
        words=set(pooled) if policy=='either' else set()
        for init in (steps if policy!='either' else ()):
            st=init;path=[]
            while True:
                a,b=st;w=steps[st];path+=w[:10];st=(w[-3],b if policy=='inherit' else a)
                if st==init:break
            s=tuple(path);words.add(min(s[k:]+s[:k] for k in range(len(s))))
        pooled.update(words)
        stats=[]
        for k in range(1,32):
            succ=defaultdict(set)
            for w in words:
                for i in range(len(w)):succ[tuple(w[(i+j-k)%len(w)] for j in range(k))].add(w[i])
            ambiguous={u:z for u,z in succ.items() if len(z)>1};stats.append(len(ambiguous));
            if not ambiguous:break
            last=next(iter(sorted(ambiguous.items())))
        exits={}
        for w in words:
            for i,x in enumerate(w):
                if x==29:exits.setdefault(w[i-1],set()).add(w[(i+1)%len(w)])
        out[policy]=dict(distinct_cycles=len(words),ambiguous_histories=stats,min_previous_visits=k,last_collision=[last[0],sorted(last[1])],return_map={i:sorted(s) for i,s in exits.items()})
    return out
if __name__=='__main__':
    out=test();print(out);(D/'ramsey_return_address_memory.json').write_text(json.dumps(out)+'\n')
