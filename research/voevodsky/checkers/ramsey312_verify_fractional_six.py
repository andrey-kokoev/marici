"""Exact independent replay. Enumerate supports by SAT and check integer-scaled weighted cover on each. No LP, graph coloring, or saved support domains used."""
from ramsey312_google_two_step import *
from collections import Counter

def main():
 E=list(sets(F,11));catalog=set(E);out=[]
 paths=[Path(x) for x in sys.argv[1:]] or [D/'ramsey312_exact_fractional_six.json'];
 for r in [r for p in paths for r in json.loads(p.read_text())]:
    d=r['d'];h=F^d;den=r['den'];rows=r['rows'];assert all(isinstance(w,int) and w>0 and g!=0 and g&~d==0 and b.bit_count()==1 and b&h and not t&~h and t|g in catalog and all(b&adj[i] for i in bits(g)) for g,b,t,w in rows);total=sum(g.bit_count()*w for g,b,t,w in rows);assert total==d.bit_count()*den;low=sum(1<<i for i in bits(h) if (adj[i]&h).bit_count()<11);C=[[-i-1,-j-1] for i in bits(low) for j in bits(adj[i]&low&((1<<i)-1))]+[[i+1 for i in bits(y)] for y in {x&low for x in E if not x&d}];n=tight=0
    with Solver(name='g4',bootstrap_with=C) as sl:
        while sl.solve():
            x=sum(1<<(i-1) for i in sl.get_model() if i>0)&low;v=sum(w for g,b,t,w in rows if x&b and not x&t);assert v>=den;tight+=int(v==den);n+=1;sl.add_clause([(-i-1 if x>>i&1 else i+1) for i in bits(low)])
    assert n==r.get('supports',r.get('n'));print(list(bits(d)),n,'legal supports, tight',tight,'budget',total//den);out.append(dict(d=d,n=n,tight=tight,budget=total//den))
 (D/('ramsey312_fractional_pressure_replay.json' if sys.argv[1:] else 'ramsey312_fractional_six_replay.json')).write_text(json.dumps(out))
if __name__=='__main__':main()
