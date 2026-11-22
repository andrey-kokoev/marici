"""Keep ONLY the actual shared residual flags of a closing long route and test both short decagons. Distinguish arbitrary shared completions, literal-swap completions and open-shortcut completions."""
from ramsey_boundary_role_table import run as halves,R,D,json
from ramsey_history_matching_provenance import enum,P,T
from ramsey_row_quotient_constructor import move

def run():
    ms=list(enum());flags=lambda w:{tuple(sorted(e)) for e in zip(w,w[1:])};rows=[];cases={}
    for h in halves():
        w=h['path'];
        if w[1]!=16:continue
        cyc=w+[R[x] for x in w[-2:0:-1]];u=frozenset(tuple(sorted((v,cyc[(i+1)%10]))) for i,v in enumerate(cyc) if not i%2);v=move(u,R);assert u.isdisjoint(v);assert len(u|v)==10
        pairs=[(m,m-u|v) for m in ms if u<=m and m-u|v in ms];forbid=set()
        for i in range(1,10,2):
            j=cyc[i];x=cyc[(i+5)%10];d,=[P.index(e) for e in T[j-15] if not set(e)&set(P[x])];k,=[k for k,t in enumerate(T,15) if P[x] in t and P[d] in t];forbid|=flags([j,d,k,x])
        cases[w[2]]=[(a&b,b==move(a,R),not ((a|b)&forbid)) for a,b in pairs]
    for r in json.loads((D/'ramsey_strip_closure_control.json').read_text()):
        w=r['path'];
        if not r['closes'] or w[:2]!=[0,16] or w[-1]!=29:continue
        cyc=w+[R[x] for x in w[-2:0:-1]];remain=set(range(30))-set(cyc);fills={frozenset((i,j) for i,j in m if i in remain and j in remain) for m in ms};fills=[s for s in fills if len(s)==4 and move(s,R)==s];assert fills;res=[]
        for s in fills:
            res.append(dict(fill=sorted(s),controls={k:[sum(s<=c and test(l,o) for c,l,o in candidates) for test in (lambda l,o:True,lambda l,o:l,lambda l,o:o)] for k,candidates in cases.items()}))
        rows.append(dict(path=w,results=res))
    return rows
if __name__=='__main__':
    out=run();print([(q['path'][2],q['path'][-2],q['results']) for q in out]);(D/'ramsey_route_fill_decagon_test.json').write_text(json.dumps(out)+'\n')
