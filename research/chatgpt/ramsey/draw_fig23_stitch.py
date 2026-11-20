"""Draw the actual Tutte 8-cage with one verified local stitch; offline standalone SVG."""
from ramsey_strip_local_stitch import flips,N,s,t
from itertools import combinations
from pathlib import Path
from math import cos,sin,pi
_,idx,good,bad,unused,_,isol,hold=min(flips);guard,=isol
X=[''.join(map(str,p)) for p in combinations(range(1,5),2)];D=list(combinations(range(6),2));M=[m for m in combinations(range(15),3) if len(set(sum((D[i] for i in m),())))==6];name=lambda i:'+'.join(X[j] for j in D[i]);title=lambda v: name(v) if v<15 else ' | '.join(name(i) for i in M[v-15]);
def edges(path):return {tuple(sorted(e)) for e in zip(path,path[1:])}
A=edges((s,*hold,t));G=edges((s,*good,t));B=edges((s,*bad,t));allE={(v,w) for v in range(15) for w in N[v]};assert len(allE)==45 and A|B|G<=allE
# Put the successful circuit on the rim, the eight remaining vertices inside (circular-mean order of attachments).
outer=[s,*good,t,*reversed(hold)];assert len(set(outer))==22
from math import atan2
angle=lambda j:2*pi*j/22-pi/2
angs={v:angle(i) for i,v in enumerate(outer)}
def mean(v):
 a=[angs[w] for w in N[v] if w in angs];return atan2(sum(map(sin,a)),sum(map(cos,a)))
inner=sorted(unused,key=mean);xy={v:(350+265*cos(a),335+265*sin(a)) for v,a in angs.items()};xy.update({v:(350+112*cos(2*pi*j/8-pi),335+112*sin(2*pi*j/8-pi)) for j,v in enumerate(inner)})
svg=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 725" role="img" aria-labelledby="caption desc"><title id="caption">Tutte’s 8-cage with an early stitch</title><desc id="desc">All 30 vertices and 45 edges. Solid green and dashed orange are alternative detours between vertices 16 and 21.</desc><rect width="100%" height="100%" fill="white"/><g font-family="system-ui, sans-serif"><text x="350" y="28" text-anchor="middle" font-size="21">Tutte’s 8-cage · one strip, two detours</text>'];
def line(e):
 a,b=e;(x,y),(z,w)=xy[a],xy[b];col,width,dash=('#087746',4,'') if e in G-B else ('#bc4900',4,' stroke-dasharray="7 4"') if e in B-G else ('#214965',3,'') if e in A|G else ('#c4cbd0',1.5,'');return f'<line x1="{x:.2f}" y1="{y:.2f}" x2="{z:.2f}" y2="{w:.2f}" stroke="{col}" stroke-width="{width}"{dash}/>'
for e in sorted(allE,key=lambda e:(e in A|G|B,e in B-G)):svg.append(line(e))
for v,(x,y) in xy.items():
 c='#ffec77' if v==guard else '#e0f0fa' if v<15 else '#fff0d8';shape=f'<circle cx="{x}" cy="{y}" r="12"' if v<15 else f'<rect x="{x-12}" y="{y-12}" width="24" height="24" rx="3"';svg.append(f'<g><title>{v}: {title(v)}</title>{shape} fill="{c}" stroke="#283848"/><text x="{x}" y="{y+4}" text-anchor="middle" font-size="12">{v}</text></g>')
for i,text in enumerate(['Circle = pair · square = partition · labels = incidence position IDs','Navy = unchanged route links · gray = other cage links','Green (closes): 16 → 10 → 23 → 2 → 21','Dashed orange (fails): 16 → 13 → 24 → 5 → 21','Yellow 27 has neighbors 12, 4, 5. Orange consumes its last partner, 5.']):svg.append(f'<text x="350" y="{630+i*19}" text-anchor="middle" font-size="14">{text}</text>')
svg.append('</g></svg>');dst=Path(__file__).resolve().parents[2]/'voevodsky/ramsey-fig23-stitch.svg';dst.write_text('\n'.join(svg),encoding='utf8')
