"""Test joint reads of two fresh rows where the single-row languages agree."""
from itertools import combinations,product
from collections import Counter
import json
from ramsey_cube_diagonal_readout import marked_faces,analyze,charts,path,D,independent_sets


def profile(sq,d,c,rows):
    g=path|c|{(i,11+j) for j,r in enumerate(sq+d) for i in r}|{(11+i,15+j) for i,r in enumerate(sq) for j,s in enumerate(d) if set(r).isdisjoint(s)};sixes=independent_sets(16,g,6);edges=[(1<<i)|(1<<j) for i,j in g];masks={}
    for r in rows:
        base=sum(1<<i for i in r)+sum(1<<(11+i) for i,s in enumerate(sq) if set(r).isdisjoint(s));opts=[15+i for i,s in enumerate(d) if set(r).isdisjoint(s)]
        good=[]
        for n in range(len(opts)+1):
            for es in combinations(opts,n):
                m=base+sum(1<<i for i in es)
                if all(m&e!=e for e in edges) and all(m&q for q in sixes):good.append(m)
        if good:masks[r]=good
    return g,masks


def joint(g,ms):
    fives=independent_sets(16,g,5);result={}
    for a,b in combinations(sorted(ms),2):
        for m,n in product(ms[a],ms[b]):
            blue=all((m|n)&q for q in fives)
            if blue or not (m&n):
                result[a,b]=dict(mutual='blue' if blue else 'red',red_to_diagonal=[[i-15 for i in (15,16) if mask>>i&1] for mask in (m,n)]);break
    return result


def triple_ok(g,ms,t):
    fives=independent_sets(16,g,5);fours=independent_sets(16,g,4);pairs=list(combinations(range(3),2))
    for m in product(*(ms[r] for r in t)):
        required={p for p in pairs if any(not ((m[p[0]]|m[p[1]])&q) for q in fives)};possible={p for p in pairs if not m[p[0]]&m[p[1]]}
        if not required<=possible or len(required)==3:continue
        if possible or all((m[0]|m[1]|m[2])&q for q in fours):return True
    return False


def audit():
    tab=analyze(10);upper=sorted(list(map(tuple,tab['leftover']))+[tuple(r) for p in tab['pieces'] for r in p['new']]);sheets={'upper':upper,'mirror':[tuple(11-i for i in reversed(r)) for r in reversed(upper)]};cs_by_sq={sq:cs for sq,_,cs in charts()};hist=Counter();examples={};same_pairs=Counter();cliques=Counter();triples=Counter();evidence=[]
    for half,start,sq,opp in marked_faces():
        corners=set(sq+opp);rows=sorted(r for r in combinations(range(1,11),3) if r not in corners and all(e not in path for e in combinations(r,2)));sheet=sheets[half];later=sheet[max(sheet.index(r) for r in corners)+1:];d=[p for p in combinations(opp,2) if len(set(p[0])&set(p[1]))==1]
        for c in cs_by_sq.get(sq,[]):
            pf=[profile(sq,p,c,rows) for p in d]
            if pf[0][1].keys()!=pf[1][1].keys():continue
            a,b=[joint(*p) for p in pf];delta=a.keys()^b.keys();after=next((tuple(sorted(p)) for p in combinations(later,2) if tuple(sorted(p)) in delta),None);hist[bool(delta),bool(after)]+=1
            if not delta:
                same_pairs[len(a)]+=1;ts=[t for t in combinations(sorted(pf[0][1]),3) if all(p in a for p in combinations(t,2))];cliques[len(ts)]+=1
                for t in ts:triples[tuple(triple_ok(*p,t) for p in pf)]+=1
            else:
                p=after or min(delta);i=int(p in b);ex=dict(half=half,start=start,parent=sq,diagonals=d,cycle=sorted(c),probes=p,accepted_diagonal=i,links=(a,b)[i][p]);examples.setdefault('later' if after else 'any',ex);evidence.append(ex)
    assert sum(hist.values())==156;out=dict(by_any_and_later={str(k):v for k,v in hist.items()},ties_by_common_pair_count=same_pairs,ties_by_candidate_triples=cliques,candidate_triple_verdicts={str(k):v for k,v in triples.items()},examples=examples,witnesses=evidence);print(hist,same_pairs,examples);(D/'ramsey_cube_diagonal_pairs.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
