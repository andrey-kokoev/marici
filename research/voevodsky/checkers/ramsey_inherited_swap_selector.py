from itertools import combinations,permutations
from functools import reduce
from collections import Counter
from pathlib import Path
import json
from hashlib import sha256


def evaluate(k,sq,outer,pairs):
    core={(i,i+1) for i in range(1,k)}|outer;mask=lambda s:sum(1<<(i-1) for i in s);F=(1<<k)-1;nb={i:mask({b if a==i else a for a,b in core if i in (a,b)}) for i in range(1,k+1)};cap=[0]*(F+1)
    for m in range(1,F+1):
        b=m&-m;cap[m]=max(cap[m^b],1+cap[m&~(b|nb[b.bit_length()])])
    if any(all(e in core for e in combinations(q,2)) for q in combinations(range(1,k+1),3)):return None
    def safe(ss,p):
        return all(n+len(ss)+cap[F&~(mask(set().union(*ss,*sub)))]<7 for n in range(len(p)+1) for sub in combinations(p,n))
    if not safe([],sq):return None
    singles={s for pair in pairs for s in pair if not any(e in core for e in combinations(s,2)) and safe([s],[r for r in sq if set(s)&set(r)])}
    return {pair for pair in pairs if set(pair)<=singles and safe(pair,[r for r in sq if all(set(s)&set(r) for s in pair)])}


def run(on_predecessor=None):
    V=set(range(1,10));rows={frozenset(q) for q in combinations(sorted(V),3) if min(q[1]-q[0],q[2]-q[1])>=2};squares=set()
    for c in rows:
        mv=[{i,i+1} for i in range(1,9) if len(c&{i,i+1})==1 and c^{i,i+1} in rows]
        for a,b in combinations(mv,2):
            if not a&b and c^a^b in rows:squares.add(tuple(sorted(tuple(sorted(s)) for s in (c,c^a,c^b,c^a^b))))
    hist=Counter();counts=Counter();ex={}
    for sq in sorted(squares):
        U=set().union(*sq);W=sorted(V-U);mov=U-set.intersection(*map(set,sq));probes=sorted(tuple(sorted(s)) for s in rows if len(s&U)==1 and s&mov);pairs=[p for p in combinations(probes,2) if sum(abs(x-y) for x,y in zip(*p))==1];children=[]
        for k in (10,9):
            outside=W+([10] if k==10 else []);mandatory={(i,i+1) for i in outside if i+1 in outside}
            for path in permutations(outside):
                if k==10 and (path[0]!=min(outside) or path[1]>path[-1]):continue
                if k==9 and path[0]>path[-1]:continue
                e={tuple(sorted(edge)) for edge in zip(path,path[1:])};
                if k==10:e.add(tuple(sorted((path[0],path[-1]))))
                if not mandatory<=e:continue
                viable=evaluate(k,sq,e,pairs)
                if viable is None:continue
                if k==10:children.append((e,viable));continue
                survive=[c for c,v in children if viable<=v];induced=[c for c,v in children if {z for z in c if 10 not in z}==e];hist[len(children),len(survive)]+=1;counts['old']+=1;counts['nonempty_marks']+=bool(viable);counts['ambiguous_to_one']+=len(children)>1 and len(survive)==1;counts['equals_induced']+=survive==induced
                if on_predecessor is not None:on_predecessor(sq,path,viable,children)
                label=('unique' if len(survive)==1 else 'none' if not survive else 'many');
                if len(children)>1 and viable:ex.setdefault(label,dict(square=sq,old_path=path,marks=sorted(viable),survivors=[sorted(c) for c in survive],candidates=len(children),induced=[sorted(c) for c in induced]))
    out=dict(counts=counts,before_after={str(key):v for key,v in sorted(hist.items())},examples=ex,protocol_sha=sha256((D/'ramsey_inherited_swap_selector_protocol.md').read_bytes()).hexdigest());print(counts,hist);print({k:(v['square'],v['old_path'],len(v['marks']),v['candidates'],len(v['survivors']),len(v['induced'])) for k,v in ex.items()});(D/'ramsey_inherited_swap_selector.json').write_text(json.dumps(out,indent=2)+'\n')
D=Path(__file__).resolve().parents[1]/'results'
if __name__=='__main__':run()
