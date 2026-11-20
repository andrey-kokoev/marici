"""Core-only border moments on Exoo's (3,10) graph; same polynomial and enumeration checks as for (3,9)."""
from collections import Counter
from exoo39_symbolic_relations import edges
from ramsey_38_39_walsh_borders import trial

if __name__=='__main__':
    E=edges();red=lambda a,b:tuple(sorted((a,b))) in E
    hist=Counter();results=[]
    for u in range(39):
        z,forced,free,joint=trial(10,[v for v in range(39) if v!=u],red)
        assert all(red(u,v) for v in forced) and all(v in forced or v in dict(free) for v in range(39) if red(u,v))
        hist[z]+=1;results.append((z,u,forced,free,joint))
    print('single deletion histogram',sorted(hist.items()));z,u,forced,free,joint=max(results);print('max example',u,z,forced,free,'perfect pair sample',[t for t in joint if abs(t[-1])==z][:5]);print('first pair readings',joint[:5]);
    z,f,g,j=trial(10,list(range(2,39)),red);print('delete 0,1: count',z,'forced red',f,'variable',g,'perfect pairs',[t for t in j if abs(t[-1])==z][:6]);print('unmodified 39 count',trial(10,list(range(39)),red)[0])
