"""Compose actual nonreversing Hall walks after a fork-bit intervention. Contrast inherited departure at the next 29 with a separately declared, old-duad departure. No abbreviated exit edge is treated as primitive."""
from ramsey_fork_missing_corner import run,partner,apexes,D,json
from ramsey_folded_entry_handoff import P,T

def test():
    source=json.loads((D/'ramsey_join_nonreturn_scale.json').read_text());lookup={tuple(r['previous'][::2]):r for r in source};results=[]
    for key,r in lookup.items():
        a,b=key;s=r['stay_or_reflect'];n=r['onward_no_flag_reversal'];k=next(i for i in range(len(s)) if s[i]!=n[i]);assert len(s[:k])==4;branches={}
        for prev in set([4,7,9])-{b}:
            v=partner(prev);choice,=[q for q in (s[k],n[k]) if any(v in fan for fan in apexes(q))];branches[prev]=choice
        assert branches[a]==n[k] and len(set(branches.values()))==2
        for policy in ['inherit','previous']:
            state=key;states=[];path=[29,b];departures=[]
            while state not in states:
                states.append(state);x,y=state;w=lookup[state]['onward_no_flag_reversal'];assert path[-2:]==w[:2];z=w[-3];nxt=y if policy=='inherit' else x;path+=w[2:-1]+[nxt];departures.append(nxt);state=(z,nxt)
            assert state==key and len(states)==(2 if policy=='inherit' else 3);assert all(u!=v for u,v in zip(path,path[2:]));assert all(P[min(u,v)] in T[max(u,v)-15] for u,v in zip(path,path[1:]));results.append(dict(initial=key,fork_outputs=branches,policy=policy,transits=states,steps=len(path)-2))
    return results
if __name__=='__main__':
    out=test();print(out[:2]);(D/'ramsey_fork_bit_iteration.json').write_text(json.dumps(out)+'\n')
