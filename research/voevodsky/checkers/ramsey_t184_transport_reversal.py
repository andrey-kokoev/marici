"""Compare named coordinate transport to a geometric selector on the two middle layers. No fitted cube-bit names. rho cycles R,B,N1,N2; sigma swaps the neutral axes. A point reflection must be about the centroid of the eight sites."""
from pathlib import Path
from itertools import product
import json
D=Path(__file__).resolve().parents[1]/'results'

def main():
 d=json.loads((D/'esd7_explicit_analytical_census.json').read_text()); ch=json.loads((D/'ramsey_t184_middle_matching.json').read_text());X={v['id']:tuple(v['barycentric']) for v in d['vertices']};V={x:v for v,x in X.items()};rot=lambda x:x[-1:]+x[:-1];sig=lambda x:(x[0],x[1],x[3],x[2]);families=[];selected=[];result=[]
 for c in ch:
    rows,cols=c['rows'],c['cols'];maps=c['layer_swap_maps'];sites=rows+cols
    totals=tuple(sum(X[v][j] for v in sites) for j in range(4));assert all(t%4==0 for t in totals);twice=tuple(t//4 for t in totals)
    f={v:V[tuple(t-a for t,a in zip(twice,X[v]))] for v in rows};assert f in maps and set(f.values())==set(cols)
    pairs=c['matching'];fixed=sum(f[v]==pairs[v] for v in rows);assert fixed==0
    # Allow an unknown common midpoint even after forgetting the neutral difference.
    proj=lambda x:(x[0],x[1],x[2]+x[3]);choices=[m for m in maps if len({tuple(a+b for a,b in zip(proj(X[v]),proj(X[w]))) for v,w in m.items()})==1];families.append(maps);selected.append(f);result.append(dict(exit=c['exit'],twice_local_center=twice,reflection=f,visible_midpoint_choices=len(choices)))
 def transport(f,g):return {V[g(X[v])]:V[g(X[w])] for v,w in f.items()}
 def cyclic(fs):return all(transport(f,rot)==fs[(i+1)%4] for i,f in enumerate(fs))
 eq=sum(cyclic(fs) for fs in product(*families));assert eq==2 and cyclic(selected)
 # Is neutral swap even a self-action on the four marked middle-layer geometries?
 sig_hits=[any({V[sig(X[v])] for v in c['rows']}==set(t['rows']) and {V[sig(X[v])] for v in c['cols']}==set(t['cols']) for t in ch) for c in ch];out=dict(cyclic_equivariant_families=eq,neutral_swap_transports_layer_pairs=sig_hits,channels=result);print(out);(D/'ramsey_t184_transport_reversal.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
