from ramsey_repair_next_seam import graph,grow,sevens,check,D,sha256,json,combinations
from itertools import permutations

def probe(ss,c):
    res={}
    for gap in range(10):
        base=grow(ss,gap)
        for p in combinations(range(5),2):
            a=graph(10,[(*s,gap) if i in p else s for i,s in enumerate(base)],c);ok=check(a,32767,3,7);tri=next((t for t in combinations(range(15),3) if all(a[i]>>j&1 for i,j in combinations(t,2))),None);q=tri or next(sevens(a),None);assert ok==(q is None);res[(gap,tuple(i+1 for i in p))]=None if ok else dict(color='red' if tri else 'blue',sites=[i+1 for i in q if i<10],ports=[i-9 for i in q if i>=10])
    return res

def run():
    src=D.parent/'ramsey_port_repair_orbits.json';data=json.loads(src.read_text());S=grow(tuple(tuple(x-1 for x in s) for s in data['supports']),data['gap']);F=lambda s:tuple(8-x for x in reversed(s));T=tuple(F(s) for s in S);bind=[p for p in permutations(range(5)) if all(F(s)==T[p[i]] for i,s in enumerate(S))];pairs=list(combinations(range(5),2));mats=[];reports=[]
    for rep in data['representatives']:
        c=sum(1<<pairs.index((i-1,j-1)) for i,j in rep['edits']);m=probe(S,c);valid={k for k,v in m.items() if v is None};ref={k for k,v in probe(T,c).items() if v is None};diff=[len(ref^{(9-g,tuple(sorted(p[i-1]+1 for i in v))) for g,v in valid}) for p in bind];assert diff[0]==0;reports.append(dict(count=len(valid),frame_mismatches=diff));mats.append((valid,m))
    (a,ma),(b,mb)=mats;diff=[len(b^{(g,tuple(sorted(p[i-1]+1 for i in v))) for g,v in a}) for p in bind];examples=[]
    for moves,reject in [(a-b,mb),(b-a,ma)]:
        examples.append([dict(move=m,obstruction=reject[m]) for m in sorted(moves)])
    out=dict(protocol_sha=sha256((D.parent/'ramsey_two_port_frame_protocol.md').read_bytes()).hexdigest(),bindings=bind,repairs=reports,common=len(a&b),cross_mismatches=diff,only_shared_then_only_disjoint=examples);print(out);p=D.parent/'ramsey_two_port_frame.json';s=json.dumps(out,indent=2)+'\n';assert not p.exists() or p.read_text()==s;p.write_text(s)
if __name__=='__main__':run()
