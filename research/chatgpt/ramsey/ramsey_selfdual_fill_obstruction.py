"""Direct obstruction certificate: classify a shared residual flag against each cycle's active flags and open antipodal paths. Test fixed residual records beyond the six issued by closing-long-strip enumeration."""
from ramsey_boundary_role_table import run as halves,R,P,T,D,json
from ramsey_antipode_extension import run as polarity
from ramsey_row_quotient_constructor import move,flags

def run():
    f=polarity()[0]['map'];base=frozenset([(9,26),(14,15)]);regions={}
    for h in halves():
        w=h['path'];
        if w[1]!=16:continue
        c=w+[R[x] for x in w[-2:0:-1]];active={tuple(sorted((x,c[(i+1)%10]))) for i,x in enumerate(c)};short=set();middle=set();owners=set()
        for i in range(1,10,2):
            j=c[i];x=c[(i+5)%10];d,=[P.index(e) for e in T[j-15] if set(P[x]).isdisjoint(e)];k,=[k for k,t in enumerate(T,15) if P[x] in t and P[d] in t];short.update([(d,j),(d,k),(x,k)]);middle.add((d,k));l,={v for u,v in flags if u==d}-{j,k};y,={u for u,v in flags if v==k}-{d,x};owners.update([(d,l),(y,k)])
        regions[w[2]]=[active,middle,short,owners]
    out=[];seen=set()
    for e in sorted(flags):
        u=frozenset((e,tuple(R[x] for x in e)));fill=u|base
        if len(u)!=2 or len(dict(fill))!=4 or len({v for _,v in fill})!=4 or u in seen or move(u,f)!=u:continue
        seen.add(u);out.append(dict(extra=sorted(u),selfdual_flags=sum(f[x]==y for x,y in u),hits={k:[len(s&u) for s in regs] for k,regs in regions.items()}))
    blocks={}
    for k,(_,_,_,owners) in regions.items():
        unseen=owners-set(base);parts=[]
        while unseen:
            e=min(unseen);u=frozenset([e,tuple(R[x] for x in e)]);block=u|move(u,f);assert len(block)==4 and block<=unseen;parts.append(sorted(block));unseen-=block
        blocks[k]=parts
    return dict(fixed_controls=out,common_owner_orbits=blocks)
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_selfdual_fill_obstruction.json').write_text(json.dumps(out)+'\n')
