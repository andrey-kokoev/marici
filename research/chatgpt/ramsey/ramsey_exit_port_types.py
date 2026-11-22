"""Classify the three exit duads by directed native endpoint types, then compose by incidence without assuming E-first or F-first. Compare with each row's own incoming exit flag."""
from ramsey_folded_entry_handoff import X,P,T,D,json,permutations

def run():
    edges={''.join(e) for e in json.loads((D.parents[1]/'strominger/inputs/photon-shared-edge-seed.json').read_text())['arrows']};apex={v for v in 'ABCD' if sum(e[0]==v for e in edges)==1};out=[]
    for p in permutations('ABCD'):
        if {p[1],p[2]}!=apex:continue
        blocks={P.index(d):sorted(e for e in edges if any(set(e)=={p[i-1] for i in X[h]} for h in d)) for d in T[29-15]};assert all(len(w)==2 for w in blocks.values());f,=[d for d,w in blocks.items() if all(e[0] in apex for e in w)];g,=[d for d,w in blocks.items() if all(e[1] in apex for e in w)];s,=blocks.keys()-{f,g};assert set(blocks[s])=={'AB','BA'};rows=[]
        for tail,own in [(p[1],7),(p[2],4)]:
            a,=[e for e in blocks[f] if e[0]==tail];b,=[e for e in blocks[g] if e[0]==a[1]];assert b[1] in apex-{tail};rows.append(dict(arc=[a,b],own_flag_first=own==f,bit=int(a[1]==p[0])))
        assert {v['own_flag_first'] for v in rows}=={True,False} and {v['bit'] for v in rows}=={0,1};out.append(dict(binding=''.join(p),blocks=blocks,typed_order=[f,g],rows=rows))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_exit_port_types.json').write_text(json.dumps(out)+'\n')
