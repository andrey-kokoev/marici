#!/usr/bin/env python3
"""Render the 24-object tetrahedral complete-schedule category as an SVG."""
from itertools import permutations
from pathlib import Path
P=list(permutations(range(1,5)))
def inv(p):return sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))
layers={k:[p for p in P if inv(p)==k] for k in range(7)}
W,H=1200,790;pos={}
for k,ps in layers.items():
 y=115+k*92
 for i,p in enumerate(ps):pos[p]=(W*(i+1)/(len(ps)+1),y)
edges=[]
for p in P:
 for i in range(3):
  q=list(p);q[i],q[i+1]=q[i+1],q[i];q=tuple(q)
  if inv(q)==inv(p)+1:edges.append((p,q,i+1))
def esc(p):return ''.join(map(str,p))
parts=[f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">
<title id="title">Tetrahedral complete-schedule category</title><desc id="desc">Twenty-four complete flags arranged by inversion degree, with thirty-six adjacent-swap morphisms.</desc><defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 8 4 0 8z" fill="context-stroke"/></marker><filter id="glow"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>
<style>.bg{{fill:#071117}}.edge{{fill:none;stroke-width:1.7;opacity:.62;marker-end:url(#arrow)}}.s1{{stroke:#65bfff}}.s2{{stroke:#bd92ff}}.s3{{stroke:#ffb85f}}.node{{fill:#10242d;stroke:#78909a;stroke-width:1.4}}.node:hover{{stroke:#fff;stroke-width:3;filter:url(#glow)}}.txt{{fill:#edf5f7;font:12px ui-monospace;text-anchor:middle;pointer-events:none}}.rank{{fill:#8198a1;font:11px ui-monospace}}.head{{fill:#edf5f7;font:600 22px system-ui}}.sub{{fill:#9cb0b8;font:13px system-ui}}.legend{{fill:#bfd0d6;font:12px system-ui}}</style><rect class="bg" width="100%" height="100%"/><text class="head" x="28" y="34">Complete evaluation schedules · localized weak-order presentation</text><text class="sub" x="28" y="58">Objects are maximal flags. Arrows swap adjacent contractions and increase inversion degree; localization formally inverts them.</text>''']
for k in range(7):parts.append(f'<text class="rank" x="18" y="{120+k*92}">degree {k}</text>')
for a,b,s in edges:
 x1,y1=pos[a];x2,y2=pos[b];parts.append(f'<path class="edge s{s}" d="M{x1:.1f},{y1+17:.1f} L{x2:.1f},{y2-17:.1f}"><title>{esc(a)} → {esc(b)} by adjacent swap s{s}</title></path>')
for p,(x,y) in pos.items():
 parts.append(f'<g><circle class="node" cx="{x:.1f}" cy="{y:.1f}" r="22"><title>schedule {esc(p)}; inversion degree {inv(p)}</title></circle><text class="txt" x="{x:.1f}" y="{y+4:.1f}">{esc(p)}</text></g>')
parts.append('''<g transform="translate(28 755)"><text class="legend"><tspan fill="#65bfff">s1</tspan><tspan> first adjacent swap · </tspan><tspan fill="#bd92ff">s2</tspan><tspan> middle adjacent swap · </tspan><tspan fill="#ffb85f">s3</tspan><tspan> last adjacent swap · labels: 1=S, 2=R, 3=S∨, 4=R∨</tspan></text></g></svg>''')
out=Path(__file__).resolve().parents[3]/'public/experiments/variance-aware-evaluation-complex/tetrahedral-schedule-category.svg';out.write_text('\n'.join(parts),encoding='utf-8');print(out)
