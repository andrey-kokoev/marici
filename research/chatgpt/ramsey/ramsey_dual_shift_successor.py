"""Predict the dual reading of a single thread by a direct reading one alternating turn away. Compare individual output flags, not just permutations of sources, on all four ordered states."""
from ramsey_iterated_thread_operator import step,final,R,move,flags,D,json
from ramsey_row_quotient_constructor import action,P,T
from ramsey_antipode_extension import run as polarity

def direct(s,t):
    unused=flags-(s|t);owner={j:d for d,j in s};out={}
    for j in {k for _,k in s^t}:
        x,=[d for d,k in unused if k==j];k,=[z for d,z in unused if d==x and z!=j];i,=[d for d,z in unused if z==k and d!=x];p=list(range(6))
        for e in T[j-15]:
            if e!=P[owner[j]]:a,b=e;p[a],p[b]=b,a
        h=action(p);out[j]=(i,(h[i],h[k]))
    return out

def run():
    f=polarity()[0]['map'];m,=final;pair=(m,move(m,R));rows=[]
    for state in range(4):
        for s,t in (pair,pair[::-1]):
            dd=direct(s,t);rev=direct(move(s,f),move(t,f));incoming={j:d for d,j in t};forward=dict(s);witness=[]
            for j,(i,_) in sorted(dd.items()):
                dual=tuple(sorted(f[v] for v in rev[f[i]][1]));x=incoming[j];z=forward[x];assert z!=j and dd[z][1]==dual;witness.append(dict(turn=[j,x,z],output=dual))
            rows.append(dict(state=state,checks=witness))
        pair=step(*pair)
    return rows
if __name__=='__main__':
    out=run();print(out[0]);(D/'ramsey_dual_shift_successor.json').write_text(json.dumps(out)+'\n')
