"""Exploratory repair AFTER fan results: glue two native triangles on opposite arrows, cancel common outer edge, read the remaining oriented radial square. Test point–side queries and reverse-arrow control."""
from ramsey_sector_corner_side import rows,ws,D,json,Counter
from ramsey_sector_arrow_bridge import T
cycles={}
for f,a,b in [r['triangle'] for r in T]:
    g,=[r['triangle'][0] for r in T if r['outer_arrow']==b+a];c=(b,f,a,g);q=frozenset(c)
    if q in cycles:assert any(c[i:]+c[:i]==cycles[q] for i in range(4))
    cycles[q]=c
assert len(cycles)==6;ct=Counter();err=rev=0
for n,s,x,side,m,_,_,_ in rows:
    matches=[c for q,c in cycles.items() if x in q and set(side)<=q];y=bool(ws[s]>>n&1);p=r=False
    if matches:
        c,=matches;i=c.index(x);forward={c[(i+1)%4],c[(i+2)%4]}==set(side);p=(m in c)!=forward;r=not p;ct['forward' if forward else 'reverse']+=1
    else:ct['no_square']+=1
    err+=p!=y;rev+=r!=y
out=dict(counts=ct,errors=err,reversed_errors=rev,decisions=len(rows),rims=list(cycles.values()));print(out);(D/'ramsey_sector_square_rim.json').write_text(json.dumps(out,indent=2)+'\n')
