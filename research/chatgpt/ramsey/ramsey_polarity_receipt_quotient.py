"""Identify dual vertices; record loops and their two nonloop neighbours. Suppress degree-two vertices to expose underlying core."""
from ramsey_antipode_extension import run,m,mate,P,T,D,json

def check():
    pol,=run();f=pol['map'];classes={}
    for j,t in enumerate(T,15):
        for d in t:
            i=P.index(d);e=(i,j);key=tuple(sorted((i,f[j])));classes.setdefault(key,set()).add(int(e in m)+int(e in mate))
    assert all(len(v)==1 for v in classes.values());marks=sorted(x for x,y in classes if x==y);core={e for e in classes if not set(e)&set(marks)};links=[]
    for x in marks:
        opts=sorted((next(iter(c)),sum(e)-x) for e,c in classes.items() if x in e and e!=(x,x));(c,a),(d,b)=opts;assert (c,d)==(0,2);links.append([a,x,b]);core.add(tuple(sorted((a,b))))
    outer=[0,4,13,12,7];spokes={a:b for a,_,b in links};inner=[spokes[a] for a in outer];edge=lambda a,b:tuple(sorted((a,b)));assert core=={e for i in range(5) for e in (edge(outer[i],outer[(i+1)%5]),edge(outer[i],inner[i]),edge(inner[i],inner[(i+2)%5]))}
    return dict(petersen_outer=outer,petersen_inner=inner,receipts=marks,neither_receipt_both=links,core_edges=sorted(core),single_owner_edges=[e for e,c in classes.items() if c=={1}],nonloop_neither_edges=[e for e,c in classes.items() if c=={0} and not set(e)&set(marks)])
if __name__=='__main__':
    out=check();print(out);(D/'ramsey_polarity_receipt_quotient.json').write_text(json.dumps(out)+'\n')
