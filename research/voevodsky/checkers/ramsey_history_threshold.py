from itertools import combinations
from collections import Counter
from ramsey_history_dominance import D, json, save, sha256, profile
from ramsey_relative_sign_joint_context import grow, graph, verdict


def run():
    charts=json.loads((D.parent/'ramsey_double_flank_contact.json').read_text())['charts'];families=sorted({tuple(map(tuple,c['rows'])) for z in charts for c in z['cases'] if c['gap'] in (z['first'],z['first']+1)})
    base=[profile(b) for b in range(256)];hist=Counter();examples={};unique=Counter();pairs=list(combinations(range(5),2))
    for ss in families:
        rows=[sum(1<<(i-1) for i in s) for s in ss];edges=[(a,b) for a,b in pairs if not rows[a]&rows[b]]
        for red in ([],edges[:1],edges[1:],edges):
            profiles={}
            for p in range(32):
                if any((p>>a)&(p>>b)&1 for a,b in red):continue
                u=0
                for i,m in enumerate(rows):
                    if p>>i&1:u|=m
                profiles.setdefault(bytes(x+2*p.bit_count() for x in base[u]),p)
            if max(v[0] for v in profiles)>=14:continue
            keep=[v for v in profiles if not any(w!=v and w[0]>=v[0] and all(i<=j for i,j in zip(v,w)) for w in profiles)];k=len(keep);demands={};ids=lambda p:[i+1 for i in range(5) if p>>i&1]
            for s in range(512):
                lo=s.bit_count();d=max(lo,14-max(v[s] for v in keep));assert (d-lo)%2==0
                hit=sum(1<<i for i,v in enumerate(keep) if v[s]+d>=14);demands.setdefault(hit,(s,d))
            covers=[m for m in range(1,1<<k) if all(m&h for h in demands)];r=min(m.bit_count() for m in covers);mins=[m for m in covers if m.bit_count()==r];hist[k,r]+=1;unique[len(mins)]+=1
            if (k,r) not in examples:
                m=mins[0];ex=dict(rows=ss,red=[(a+1,b+1) for a,b in red],profiles=[ids(profiles[v]) for v in keep],keep_indices=[i for i in range(k) if m>>i&1],private=[])
                for i in ex['keep_indices']:
                    h=next(h for h in demands if (m&h)==1<<i);s,d=demands[h];gaps=[j for j in range(9) if s>>j&1]+[0]*(d-s.bit_count());t=[tuple(v-1 for v in row) for row in ss]
                    for g in sorted(gaps,reverse=True):t=grow(t,g)
                    assert not verdict(graph(8+d,t,sum(1<<pairs.index(e) for e in red)));ex['private'].append(dict(index=i,gaps=gaps,threshold_hits=h))
                examples[k,r]=ex
    assert sum(hist.values())==154 and sum(k*n for (k,r),n in hist.items())==256
    enc=lambda a:{f'{k}->{r}':v for (k,r),v in a.items()};out=dict(transitions=enc(hist),minimum_total=sum(r*n for (k,r),n in hist.items()),number_of_minima=unique,examples=enc(examples),protocol_sha=sha256((D.parent/'ramsey_history_threshold_protocol.md').read_bytes()).hexdigest());print(out['transitions'],out['minimum_total'],unique);save(D.parent/'ramsey_history_threshold.json',out)

if __name__=='__main__':run()
