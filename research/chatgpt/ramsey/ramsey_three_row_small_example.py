"""Independent small-target search. Require EVERY tight row pair repairable, not only pairs of the displayed three. Also require initial three ports legal and the core itself four-port extendible if possible."""
from itertools import combinations,combinations_with_replacement
from ramsey_hall_center_conjecture import decode
from ramsey_fork_audit_uniform import D,json,inds,grow,verify

def test(H):
    I=inds(H);M=[s for s in I if all(s>>v&1 or s&r for v,r in enumerate(H))];k=max(map(int.bit_count,I))+2;hit={s:sum(1<<i for i,m in enumerate(M) if s&m) for s in I};
    for q in combinations_with_replacement(M,3):
        slack={s:k-1-s.bit_count()-sum(not(s&t) for t in q) for s in I};
        if min(slack.values())<0:continue
        rows=[s for s,b in slack.items() if b==0];
        if any(not(hit[s]&hit[t]) for s,t in combinations(rows,2)):continue
        for a,b,c in combinations(rows,3):
            if hit[a]&hit[b]&hit[c]:continue
            repairs=[M[((z&-z).bit_length()-1)] for z in (hit[a]&hit[b],hit[a]&hit[c],hit[b]&hit[c])];verify(grow(H,q),k);return dict(core=H,k=k,fixed=q,rows=[a,b,c],repairs=repairs,total_tight=len(rows))
if __name__=='__main__':
    from random import Random
    rng=Random(37);out=None
    for n in range(5,11):
        for _ in range(200):
            H=[0]*n;E=list(combinations(range(n),2));rng.shuffle(E)
            for x,y in E:
                if not H[x]&H[y] and rng.random()<.7:H[x]|=1<<y;H[y]|=1<<x
            if max(map(int.bit_count,inds(H)))<3:continue
            out=test(H)
            if out:break
        if out:break
    print(out);(D/'ramsey_three_row_small_example.json').write_text(json.dumps(out)+'\n')
