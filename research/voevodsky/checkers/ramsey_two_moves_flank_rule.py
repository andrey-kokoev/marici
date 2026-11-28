"""Read two permanent tests from the two blocks and the leftover outside site."""
from itertools import combinations,permutations
from ramsey_two_repairs_opposite import run
from ramsey_inherited_swap_selector import D,evaluate
from ramsey_pentagon_selector import charts
import json


def block_word(sq):
    U=set().union(*sq);W=set(range(1,11))-U;f,=set.intersection(*map(set,sq));mov=U-{f};starts=[]
    for x,z in combinations(sorted(mov),2):
        e=(x-1,z+1)
        if any({x,z}<=set(r) for r in sq) or not set(e)<=W:continue
        if any(abs(i-j)==1 for i in e for j in mov-{x,z}):continue
        starts.append((e[0],'B'))
    if len(starts)!=2:return None
    h,=W-{v for u,_ in starts for v in (u,u+3)}
    return ''.join(letter for _,letter in sorted(starts+[(f,'f'),(h,'h')]))


def rule(sq):
    U=set().union(*sq);W=set(range(1,11))-U;mov=U-set.intersection(*map(set,sq));flanks=[]
    for x,z in combinations(sorted(mov),2):
        e=(x-1,z+1)
        if not any({x,z}<=set(r) for r in sq) and set(e)<=W:flanks.append(e)
    e,g=flanks;h,=W-set(e+g)
    if any(abs(h-i)==1 for i in e):e,g=g,e
    p,q=sorted(e,key=lambda i:-abs(i-h));x,z=g[0]+1,g[1]-1;Y=sorted(mov-{x,z});y,w=next((y,w) for y,w in permutations(Y) if abs(y-q)>1 and abs(w-p)>1)
    row=lambda *s:tuple(sorted(s));first=row(x,p,q);second=row(x,h,p)
    return dict(far=e,near=g,leftover=h,first=first,yes=((first,row(z,y,h)),(row(z,p,q),row(x,w,h))),second=second,second_yes=((second,row(z,y,q)),(row(x,h,q),row(z,w,p))))


def audit():
    keys=run();cases=[];comparison=json.loads((D/'ramsey_square_first_move.json').read_text())['records'];need_two={tuple(map(tuple,r['square'])) for r in comparison if not r['promise'] and r['outcome']=='no first-row plan'};hist={}
    for sq,_,cycles in charts():
        word=block_word(sq);two=word is not None and any(w in ('fBBh','fhBB','BfhB') for w in (word,word[::-1]));assert two==(sq in need_two);hist[str(word)]=hist.get(str(word),0)+1
        if not two:continue
        plan=rule(sq);outcomes=[]
        for c in cycles:
            for r,links in [(plan['first'],plan['yes']),(plan['second'],plan['second_yes'])]:
                if evaluate(10,sq,c,[(r,) ]):
                    rs=tuple(sorted(s for p in links for s in p));assert (sq,tuple(sorted(c)),rs) in keys
                    assert all(set(a).isdisjoint(b) and all(set(t)&set(a+b) for t in sq) for a,b in links);outcomes.append(r);break
            else:assert sum(k==sq and cc==tuple(sorted(c)) for k,cc,_ in keys)==0;outcomes.append(None)
        cases.append(dict(square=sq,word=word,plan=plan,outcomes=outcomes))
    assert len(cases)==6 and sum(hist.values())==54;print(hist);print(cases[0]);(D/'ramsey_two_moves_flank_rule.json').write_text(json.dumps(cases,indent=2)+'\n')
if __name__=='__main__':audit()
