from collections import Counter
from itertools import combinations
from ramsey_contact_path_parity import D, json, save, sha256, path_capacity


def profile(blocked):
    ends=[-1,*[i for i in range(8) if blocked>>i&1],8];runs=[]
    for a,b in zip(ends,ends[1:]):
        runs.append((b-a-1,((1<<(b-a))-1)<<(a+1)))
    return [8-blocked.bit_count()+sum((size+(mask&s).bit_count())%2 for size,s in runs) for mask in range(512)]


def run():
    src=json.loads((D.parent/'ramsey_double_flank_contact.json').read_text());families=sorted({tuple(map(tuple,c['rows'])) for z in src['charts'] for c in z['cases'] if c['gap'] in (z['first'],z['first']+1)})
    prior=json.loads((D.parent/'ramsey_history_run_state.json').read_text())['example'];base=[profile(b) for b in range(256)];counts=Counter();sizes=[];witness=None
    for ss in families:
        rows=[sum(1<<(i-1) for i in s) for s in ss];edges=[(a,b) for a,b in combinations(range(5),2) if not rows[a]&rows[b]]
        for red in ([],edges[:1],edges[1:],edges):
            profiles={}
            for p in range(32):
                if any((p>>a)&(p>>b)&1 for a,b in red):continue
                u=0
                for i,row in enumerate(rows):
                    if p>>i&1:u|=row
                v=bytes(x+2*p.bit_count() for x in base[u]);assert v[0]==2*(p.bit_count()+path_capacity(8,u));profiles.setdefault(v,[]).append(p)
            best=max(v[0] for v in profiles)
            if best>=14:continue
            keep=[v for v in profiles if not any(w!=v and w[0]>=v[0] and all(i<=j for i,j in zip(v,w)) for w in profiles)]
            assert list(map(max,zip(*profiles)))==list(map(max,zip(*keep)))
            counts['sources']+=1;counts['groups']+=sum(map(len,profiles.values()));counts['distinct_profiles']+=len(profiles);counts['retained']+=len(keep);sizes.append(len(keep))
            for v,ps in profiles.items():
                n=len(ps)-int(v in keep);counts['removed_initially_max' if v[0]==best else 'removed_initially_smaller']+=n
            if ss==tuple(map(tuple,prior['rows'])) and [[a+1,b+1] for a,b in red]==prior['red']:
                parity=0
                for g in prior['history']:parity^=1<<g
                d=len(prior['history']);winner=max(keep,key=lambda v:v[parity]);score=(winner[parity]+d)//2;assert score==prior['actual'];witness=dict(kept=len(keep),groups=sum(map(len,profiles.values())),score=score,winning_ports=[i+1 for i in range(5) if profiles[winner][0]>>i&1])
    assert counts['sources']==154 and witness;out=dict(counts=counts,range_retained=[min(sizes),max(sizes)],prior_replay=witness,protocol_sha=sha256((D.parent/'ramsey_history_dominance_protocol.md').read_bytes()).hexdigest());print(out);save(D.parent/'ramsey_history_dominance.json',out)

if __name__=='__main__':run()
