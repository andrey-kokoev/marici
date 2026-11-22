"""Exhaust colour-unlabelled partial colourings obeying single-completion rows on core 5. Minimal extra fork constraints and concrete impossibility witnesses."""
from ramsey_fifth_vertex_forks import D,json,graph,bits,inds,combinations,Counter

def run():
    H=graph((D/'pauli-realization-catalogues/r36_17.g6').read_bytes().splitlines()[4]);I=sorted(inds(H));T=[t for t in I if t.bit_count()==5 and max((t&h).bit_count() for h in H)==4];P={q:[t for t in T if q&t==q] for q in I if q.bit_count()==4 and any(q&~h==0 for h in H)};single={r[0] for r in P.values() if len(r)==1};fork=[(q,ts) for q,ts in P.items() if len(ts)==2];miss=[sum(1<<i for i,t in enumerate(sorted(single)) if not s&t) for s in I];N=[sum(1<<j for j in range(i,len(I)) if not s&I[j] and not miss[i]&miss[j]) for i,s in enumerate(I)];counts=Counter();examples={};lost=Counter()
    for i,row in enumerate(N):
        for j in bits(row):
            for k in bits(row&N[j]):
                S=[I[b] for b in (i,j,k)];bad=tuple(v for v,(q,ts) in enumerate(fork) if any(sum(bool(s&t) for s in S)<2 for t in ts));assert bad;counts[bad]+=1;examples.setdefault(bad,S)
                for v in bad:
                    q,ts=fork[v];colors={b for b,s in enumerate(S) if s&q};ends=[t^q for t in ts];ec=[next((b for b,s in enumerate(S) if s&e),None) for e in ends];tag='empty spokes' if not colors else 'blank end' if None in ec else 'reused spoke color';lost[tag]+=1
    cores=[u for size in range(1,5) for u in combinations(range(4),size) if all(set(u)&set(bad) for bad in counts)];minimum=[u for u in cores if len(u)==len(cores[0])];return dict(single_rows=len(single),forks=fork,patterns=[dict(bad=bad,count=c,example=examples[bad]) for bad,c in counts.items()],minimum=minimum,failures=lost)
if __name__=='__main__':
    r=run();print(r);(D/'ramsey_core5_fork_escapes.json').write_text(json.dumps(r)+'\n')
