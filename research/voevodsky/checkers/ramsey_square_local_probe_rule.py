"""One permanent test from path colors, degree/triangle propagation and two repair formulas."""
from itertools import combinations,permutations
from collections import Counter
from ramsey_pentagon_selector import charts
from ramsey_inherited_swap_selector import D,evaluate
from ramsey_two_repairs_opposite import run
import json


def close(W,r,b):
    es=set(combinations(sorted(W),2));r=r|{e for e in es if e[1]-e[0]==1};b=b|{e for e in es if e[1]-e[0]==2}
    while True:
        if r&b:return None
        nr=set();nb=set()
        for i in W:
            incident={e for e in es if i in e};free=incident-r-b;need=2-len(incident&r)
            if not 0<=need<=len(free):return None
            if need==0:nb|=free
            if need==len(free):nr|=free
        for tri in combinations(sorted(W),3):
            q=set(combinations(tri,2))
            # Both a pentagon and its complement are triangle-free.
            if len(q&r)>=2:nb|=q-r if q-r else q
            if len(q&b)>=2:nr|=q-b if q-b else q
        if not (nr-r or nb-b):return r,b
        r|=nr;b|=nb


def rejection(W,blocks,base,query):
    R,B=base;red=R|{query};row=lambda *s:tuple(sorted(s))
    fallback=[block for block in blocks if block[0] in B]
    if not fallback:
        # Two inner red edges exclude a blue flank by the 2/3 degree count.
        assert all(F in red or sum(set(p)<=W-set(F) for p in red)>=2 for F,X,Y in blocks)
        return None,'all flanks excluded'
    (F,(x,z),Y),=fallback;K=W-set(F)
    if set(query)<=K:
        a,b=query;mode='query is inner red edge'
    else:
        h,=set(query)-set(F);assert all(row(h,i) in red for i in F)
        a,b=sorted(K-{h});mode='query fixes common neighbor'
    h,=K-{a,b};y,w=next((j,k) for j,k in permutations(sorted(Y)) if abs(a-j)!=1 and abs(b-k)!=1)
    return (row(x,h,b),row(z,y,a),row(x,h,a),row(z,w,b)),mode


def positional_colors(W):
    # Degree sums on the 2-site and 3-site sides give red(K) = 1 + red(e).
    R,B=set(),set()
    while True:
        before=len(R|B);R,B=close(W,R,B)
        for e in combinations(sorted(W),2):
            K=set(combinations(sorted(W-set(e)),2));lo=len(K&R);hi=3-len(K&B)
            if lo==2:R.add(e)
            if hi==1:B.add(e)
            if hi==1+int(e in R):R|=K-B
            if lo==2-int(e in B):B|=K-R
        if before==len(R|B):return R,B


def local(sq,all_choices=False):
    U=set().union(*sq);f,=set.intersection(*map(set,sq));mov=U-{f};W=set(range(1,11))-U;blocks=[]
    for x,z in combinations(sorted(mov),2):
        e=(x-1,z+1);Y=mov-{x,z}
        if not any({x,z}<=set(r) for r in sq) and set(e)<=W and all(abs(i-j)!=1 for i in e for j in Y):blocks.append((e,(x,z),Y))
    def leaves(colors):
        if colors is None:return []
        R,B=colors
        if all(e in R for e,X,Y in blocks):return [None]
        res=[]
        for e,X,Y in blocks:
            if e not in B:continue
            for a,b in combinations(sorted(W-set(e)),2):
                h,=W-set(e)-{a,b}
                for x,z in permutations(X):
                    for y,w in permutations(sorted(Y)):
                        def emit(rs):res.append(tuple(tuple(sorted(s)) for s in rs))
                        if (a,b) in R and abs(y-a)!=1 and abs(w-b)!=1:emit(((x,h,b),(z,y,a),(x,h,a),(z,w,b)))
                        if (a,b) in B and all(abs(f-i)!=1 for i in e) and min(abs(h-y),abs(h-w))!=1:emit(((x,a,b),(z,y,h),(z,a,b),(x,w,h)))
        return res
    base=positional_colors(W);direct=leaves(base)
    if direct:return dict(direct=direct[0])
    candidates=sorted({p for flank,_,_ in blocks if flank not in base[0] for p in combinations(sorted(W-set(flank)),2)}-base[0]-base[1]);plans=[]
    from ramsey_two_moves_flank_rule import block_word
    if block_word(sq) in {'fBBh','hBBf','fhBB','BBhf','BfhB','BhfB'}:return None
    for e in candidates if all_choices else candidates[:1]:
        # Two eligible blocks are disjoint and leave only one shared outside
        # site in their complements; a two-site query has a unique host block.
        (host,X,Y),=[b for b in blocks if b[0] not in base[0] and set(e).isdisjoint(b[0])]
        probes=[tuple(sorted((*e,x))) for x in (X if all_choices else X[:1])]
        a,=W-set(host)-set(e);row=lambda *s:tuple(sorted(s))
        repeat=all(abs(f-u)!=1 for u in host) and all(abs(a-y)!=1 for y in Y)
        for r in probes:
            x,=set(r)&U;z,=set(X)-{x}
            if repeat:
                y,w=sorted(Y);q=(r,row(z,y,a),row(z,*e),row(x,w,a));mode='repeat outside pair'
            else:
                red=[i for i in e if row(a,i) in base[0]];possible=[i for i in e if row(a,i) not in base[1]]
                k,=red or possible;h,=set(e)-{k};y,w=next((y,w) for y,w in permutations(sorted(Y)) if abs(a-y)!=1 and abs(k-w)!=1)
                q=(r,row(z,y,a),row(x,h,a),row(z,w,k));mode='switch outside pair'
            no,no_mode=rejection(W,blocks,base,e)
            plans.append(dict(edge=e,host=host,probe=r,partner=row(z,y,a),accept_rule=mode,reject_rule=no_mode,yes=q,no=no))
    return plans if all_choices else plans[0]


def audit():
    labels={tuple(map(tuple,r['square'])):r['outcome'] for r in json.loads((D/'ramsey_square_first_move.json').read_text())['records'] if not r['promise']};keys=run();counts=Counter();out=[]
    for sq,_,cycles in charts():
        p=local(sq);choices=local(sq,True) if p and 'probe' in p else [];kind='unresolved' if p is None else 'first row' if 'probe' in p else 'common' if p['direct'] else 'none';counts[labels[sq],kind]+=1
        for tested in choices or ([p] if p else []):
            for c in cycles:
                if 'probe' in tested:
                    yes=bool(evaluate(10,sq,c,[(tested['probe'],)]));assert yes==(tested['edge'] not in c);q=tested['yes'] if yes else tested['no'];assert not yes or tested['probe'] in q
                else:q=tested['direct']
                if q:
                    assert (sq,tuple(sorted(c)),tuple(sorted(q))) in keys
                    for a,b in (q[:2],q[2:]):assert set(a).isdisjoint(b) and all(set(r)&set(a+b) for r in sq)
                else:assert not any(s==sq and t==tuple(sorted(c)) for s,t,_ in keys)
        out.append(dict(square=sq,policy=p,usable_edges=sorted({q['edge'] for q in choices}),usable_probes=[q['probe'] for q in choices],probe_partners=[(q['probe'],q['partner'],q['accept_rule']) for q in choices],reject_rules=[(q['probe'],q['reject_rule'],q['no']) for q in choices]))
    from ramsey_two_moves_flank_rule import block_word
    assert all((r['policy'] is None)==(block_word(r['square']) in {'fBBh','hBBf','fhBB','BBhf','BfhB','BhfB'}) for r in out)
    assert counts=={('none','none'):26,('common','common'):4,('first row','first row'):18,('no first-row plan','unresolved'):6}
    print(counts);(D/'ramsey_square_local_probe_rule.json').write_text(json.dumps(dict(counts={str(k):v for k,v in counts.items()},plans=out),indent=2)+'\n')
if __name__=='__main__':audit()
