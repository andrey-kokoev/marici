"""One-tick image of a disjoint address on an oriented rim. Exploratory rule inferred on AB rim, scored separately on remaining rims, not a blind discovery. Chart-known anchors only give no triangle veto on disjoint rim links (no previously determined exterior red link incident to a rim)."""
from ramsey_sector_square_rim import cycles
from ramsey_sector_arrow_bridge import sides,features,ws,S,point,cal,D,json,combinations,Counter

def allowed(rim,other,tick):
    c=cycles[rim];pi={}
    for x in set(point.values()):
        if x in rim:pi[x]=x;continue
        z,=[v for v in rim if frozenset((x,v)) in sides];pi[x]=z
    moved={c[(c.index(pi[x])+tick)%4] for x in other};return {m for m,v in pi.items() if v in moved}
rows=Counter();red=Counter();errors=Counter();predictions={};asym=0
for n,(i,j) in enumerate((e for e in combinations(range(26),2) if not S[e[0]]&S[e[1]])):
    a,b=sorted((features[i],features[j]),key=len)
    if len(b)!=4:continue
    k=len(a);maps={s:allowed(b,a,s) for s in (-1,0,1)};predictions[n]=maps[1];assert len(maps[1])==2*k
    if k==4:assert allowed(a,b,1)==maps[1]
    for s,w in enumerate(ws):
        m=point[''.join(map(str,cal[str(s)]))];y=bool(w>>n&1);rows[k]+=1;red[k]+=y
        for shift,z in maps.items():errors[str((k,shift))]+=((m in z)!=y)
        asym+=('A' in b and 'B' in b and k!=4)
out=dict(pairs=len(predictions),decisions=dict(rows),red=dict(red),errors_by_size_and_shift=dict(errors),bare_triangle_rule_errors=sum(rows.values())-sum(red.values()),calibration_AB_nonrim_decisions=asym);print(out);(D/'ramsey_sector_rim_tick.json').write_text(json.dumps(out,indent=2)+'\n')
