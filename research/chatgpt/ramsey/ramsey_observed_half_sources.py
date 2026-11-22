"""Only observed flags on the finite entry-to-exit half. Compare time-ordered streaming with a buffer of distinct observed sources; no reflected incidences used for event provenance."""
from itertools import permutations
from ramsey_folded_entry_handoff import X,P,D,json

def run():
    seed=json.loads((D.parents[1]/'strominger/inputs/photon-shared-edge-seed.json').read_text());E={''.join(e) for e in seed['arrows']};out=[]
    for p in permutations('ABCD'):
        if {p[0],p[3]}!={'A','B'}:continue
        records=[]
        for w,t in [('BRNN',[0,16,13,19,7,29]),('BNRN',[0,17,12,27,4,29])]:
            tail=p[w.index('R')];head,={'C','D'}-{tail};word,=[(a,b) for a in E for b in E if a[0]==tail and a[1]==b[0] and b[1]==head];slots=[]
            for a,b in zip(t,t[1:]):
                s=[{p[i-1] for i in X[k]} for k in P[min(a,b)]];slots.append({e for e in E if set(e) in s})
            pairs=sorted((i+1,j+1) for i,a in enumerate(slots) for j,b in enumerate(slots) if i!=j and word[0] in a and word[1] in b);assert pairs;ordered=[s for s in pairs if s[0]<s[1]];records.append(dict(row=w,events=word,buffer_ready=min(map(max,pairs)),stream_sources=ordered,buffer_sources=pairs))
        assert sum(bool(q['stream_sources']) for q in records)==1;out.append(dict(binding=''.join(p),rows=records))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_observed_half_sources.json').write_text(json.dumps(out)+'\n')
