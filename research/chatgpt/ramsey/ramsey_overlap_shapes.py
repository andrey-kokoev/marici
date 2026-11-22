"""All valid attachments including nonmaximal supports, via downwards deletion from valid maximal multisets. Classify overlap multigraph up to permuting four slots, find size of individual tight rows preventing loss of each shared incidence."""
from ramsey_capacity_transfer_78 import D,json,decode,inds,bits,check,combinations,Counter
from itertools import permutations
from functools import reduce
from operator import and_,or_

def run():
    cases=json.loads((D/'ramsey_overlap_diversity.json').read_text());lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[]
    for r in cases:
        if r.get('true_min')!=4:continue
        H=decode(lines[r['record']-1]);I=inds(H);M=[];check(H,lambda S,tag:M.append(tuple(sorted(S))) if tag=='valid' else None);T=[s for s in I if s.bit_count()>=4];seen=set();stack=list(M);hist=Counter();wsets=set();sizes=Counter();guard=Counter();geoms=Counter();example=None
        while stack:
            S=stack.pop()
            if S in seen:continue
            seen.add(S);tight=[t for t in T if t.bit_count()+sum(not s&t for s in S)==7];W=reduce(or_,(a&b for a,b in combinations(S,2)));pairs=[(i,j) for i,j in combinations(range(4),2)];canon=min(tuple((S[a[i]]&S[a[j]]).bit_count() for i,j in pairs) for a in permutations(range(4)));hist[str(canon)]+=1;wsets.add(W);sizes[str(tuple(sorted(s.bit_count() for s in S)))]+=1;geoms[str(tuple(sorted((H[v]&W).bit_count() for v in bits(W))))]+=1
            for i,s in enumerate(S):
                for v in bits(s):
                    reasons=[t.bit_count() for t in tight if t&s==1<<v];
                    if W>>v&1:guard[max(reasons,default=0)]+=1
                    if not reasons:stack.append(tuple(sorted(S[:i]+(s^(1<<v),)+S[i+1:])))
            if example is None:example=S
        out.append(dict(record=r['record'],all=len(seen),maximal=len(M),shapes=hist,sets=sorted(wsets),intersection=reduce(and_,wsets),sizes=sizes,old_degrees=geoms,largest_blocking_row=guard,example=example))
    return out

def matching_screen(z):
    look={r['record']:set(r['sets']) for r in z};summary=Counter();total=productive=0
    for j,line in enumerate((D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines(),1):
        H=decode(line)
        if min(x.bit_count() for x in H)!=5:continue
        W=(sum(1<<i for i in v) for v in combinations([i for i,x in enumerate(H) if x.bit_count()==5],4));cand={w for w in W if all((H[i]&w).bit_count()==1 for i in bits(w))};summary[str((bool(cand),j in look))]+=1;total+=len(cand);productive+=len(cand&look.get(j,set()))
    return dict(counts=summary,candidates=total,productive=productive)
if __name__=='__main__':
    z=run();print(len(z),sum(r['all'] for r in z),sum(r['maximal'] for r in z));
    (D/'ramsey_overlap_matching_screen.json').write_text(json.dumps(matching_screen(z))+'\n')
    for k in ('shapes','old_degrees','largest_blocking_row','sizes'):print(k,sum((Counter(r[k]) for r in z),Counter()))
    print(Counter(len(r['sets']) for r in z),Counter(r['intersection'].bit_count() for r in z));(D/'ramsey_overlap_shapes.json').write_text(json.dumps(z)+'\n')
