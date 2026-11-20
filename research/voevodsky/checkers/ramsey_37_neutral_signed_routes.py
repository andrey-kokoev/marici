"""Compare recorded signed incidence readouts at the ends of the red diamonds. No composition law for an entire path assumed."""
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results'
def get(k):return json.loads((D/(k+'.json')).read_text())
g=get('ramsey_37_dual_stars');rows=g['rows'];poles=[0,6];F=[rows[0],rows[3]];A={}
for r in get('ramsey_37_ordered_star_sign'):
 p=int(r['pole'][4:]);via=F[poles.index(p)][r['source']];A[p,via,r['slot']]=(r['local_step'],r['change'],r['red'])
out=[]
for case in get('ramsey_37_two_neutral_routes'):
 sides=[]
 for d in case['side_diamonds']:
    p,u=d['source'],d['target'];v,w=d['via'];x,y=A[p,v,u],A[p,w,u];assert x[0]==-y[0] and x[1]==-y[1] and x[2]==y[2];sides.append([p,u,v,x,w,y])
 # At the cross-pole contact use the two via-vertices from the second branch of the reflected side diamonds.
 v,w=[next(d['via'][1] for d in case['side_diamonds'] if d['source']==p) for p in poles];cross={u:(A[0,v,u],A[6,w,u]) for u in range(22) if (0,v,u) in A and (6,w,u) in A};fixed=[u for u,(x,y) in cross.items() if x==y];assert fixed==[case['apex']];out.append(dict(center=case['center'],apex=case['apex'],sides=sides,cross_endpoints=[v,w],cross=cross))
print(out[:2]);(D/'ramsey_37_neutral_signed_routes.json').write_text(json.dumps(out,indent=2)+'\n')
