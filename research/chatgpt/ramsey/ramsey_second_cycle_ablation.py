"""Toggle the two disjoint cycles of the retained-matching handoff independently. Compare the next full swap/involution, exit component, closure and active-cycle locality. Controls are perfect matchings, not asserted literal swap outputs."""
from ramsey_hold_matching_switch_swap import final,move,trans,D,json

def cycles(m,n):
    rem=set(m^n);out=[]
    while rem:
        todo=[rem.pop()];verts=set(todo[0]);
        for edge in todo:
            for e in list(rem):
                if set(e)&set(edge):rem.remove(e);todo.append(e);verts.update(e)
        out.append(frozenset(todo))
    return sorted(out,key=lambda c:not any(j==29 for _,j in c))

def run():
    start,=final;base=move(start,trans(3,2));real=move(base,trans(2,4));ec,aux=cycles(base,real);out=[]
    for name,t in [('neither',set()),('aux',aux),('exit',ec),('both',ec|aux)]:
        m=base^t;assert len(m)==len(dict(m))==len({j for i,j in m})==15;h=[];z=m
        for a,b in [(4,3),(3,2),(2,4),(4,3)]:
            n=move(z,trans(a,b));cs=cycles(z,n);h.append(dict(exit=next(i for i,j in n if j==29),components=list(map(len,cs)),exit_component=sorted(cs[0]) if cs and any(j==29 for i,j in cs[0]) else [],common_start=len(n&start)));z=n
        out.append(dict(toggled=name,exact=m==real,history=h))
    return dict(aux=sorted(aux),exit=sorted(ec),variants=out)
if __name__=='__main__':
    out=run();print([(q['toggled'],[(s['exit'],s['components'],s['common_start']) for s in q['history']]) for q in out['variants']]);print([a['exit_component']==b['exit_component'] for a,b in zip(out['variants'][2]['history'],out['variants'][3]['history'])]);(D/'ramsey_second_cycle_ablation.json').write_text(json.dumps(out)+'\n')
