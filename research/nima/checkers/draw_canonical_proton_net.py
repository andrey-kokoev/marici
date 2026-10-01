"""Draw the intrinsic incidence net and its shared-vertex view.

Triangle agents are the dual of the recorded oriented triangulation. Wires
identify actual shared edges. Layout is a deterministic Tutte/Schlegel drawing,
not processing stages and not a new claim about the 1836 coefficient count.
"""
from collections import defaultdict
from fractions import Fraction as F
from html import escape
from itertools import combinations
from math import hypot
from pathlib import Path
import json
import xml.etree.ElementTree as ET

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results'


def tutte(adjacency,fixed,weights=None):
    names=sorted(set(adjacency)-set(fixed));n=len(names)
    a=[]
    def weight(v,w): return F(1) if weights is None else weights[tuple(sorted((v,w)))]
    for v in names:
        degree=sum(weight(v,w) for w in adjacency[v])
        row=[degree if v==w else -weight(v,w) if w in adjacency[v] else F(0) for w in names]
        row += [sum((weight(v,w)*F(fixed[w][axis]) for w in adjacency[v] if w in fixed),F(0)) for axis in (0,1)]
        a.append(row)
    for j in range(n):
        p=next(i for i in range(j,n) if a[i][j])
        a[p],a[j]=a[j],a[p];v=a[j][j];a[j]=[x/v for x in a[j]]
        for i in range(n):
            if i!=j:
                v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[j])]
    pos={v:tuple(map(F,xy)) for v,xy in fixed.items()}
    pos.update({v:tuple(a[i][-2:]) for i,v in enumerate(names)})
    for v in names:
        assert all(sum(weight(v,w) for w in adjacency[v])*pos[v][axis]==sum(weight(v,w)*pos[w][axis] for w in adjacency[v]) for axis in (0,1))
    return pos


def area(a,b,c): return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
def check_planar(pos,edges):
    assert len(set(pos.values()))==len(pos)
    for (a,b),(c,d) in combinations(edges,2):
        if len({a,b,c,d})<4: continue
        assert not (area(pos[a],pos[b],pos[c])*area(pos[a],pos[b],pos[d])<0
                    and area(pos[c],pos[d],pos[a])*area(pos[c],pos[d],pos[b])<0)


def cycle(adj):
    assert all(len(v)==2 for v in adj.values())
    start=min(adj);route=[start];prev=None;now=start
    while True:
        nxt=min(w for w in adj[now] if w!=prev)
        if nxt==start: break
        assert nxt not in route
        route.append(nxt);prev,now=now,nxt
    assert set(route)==set(adj)
    return route


def opening(title,subtitle):
    return ['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="1110" viewBox="0 0 1100 1110" role="img">',
            f'<title>{escape(title)}</title>',
            '<defs><marker id="arrow" viewBox="0 0 6 6" refX="5.5" refY="3" markerWidth="6" markerHeight="6" orient="auto-start-reverse" markerUnits="userSpaceOnUse"><path d="M0 0 L6 3 L0 6 Z" fill="#30475d"/></marker></defs>',
            '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#203349}.wire:hover,.arrow:hover{stroke:#ca4b16;stroke-width:4}.note{font-size:14px;fill:#53697e}</style>',
            '<rect width="1100" height="1110" fill="#fcfdff"/>',
            f'<text x="40" y="45" font-size="27" font-weight="650">{escape(title)}</text>',
            f'<text x="40" y="76" font-size="16" fill="#53697e">{escape(subtitle)}</text>']


def main():
    data=json.loads((OUT/'twelve-triangle-positive-geometry.json').read_text())
    tris={row['outer_arrow']:tuple(row['triangle']) for row in data['triangles_and_transports']}
    assert len(tris)==12
    incidence=defaultdict(list);primal=defaultdict(set)
    for name,t in tris.items():
        for a,b in zip(t,t[1:]+t[:1]):
            incidence[tuple(sorted((a,b)))].append((name,a,b))
            primal[a].add(b);primal[b].add(a)
    assert len(primal)==8 and len(incidence)==18
    dual={name:set() for name in tris};wires=[]
    for edge,records in sorted(incidence.items()):
        assert len(records)==2
        (p,a,b),(q,c,d)=records
        assert (a,b)==(d,c)
        dual[p].add(q);dual[q].add(p)
        kind='outer' if all(not v.startswith('F_') for v in edge) else 'radial'
        wires.append({'agents':(p,q),'shared_edge':edge,'kind':kind})
    assert all(len(v)==3 for v in dual.values())
    assert sum(w['kind']=='outer' for w in wires)==6
    # Every original vertex becomes one closed face of the agent net.
    loops={}
    for vertex in sorted(primal):
        around={name:set() for name,t in tris.items() if vertex in t}
        for w in wires:
            if vertex in w['shared_edge']:
                a,b=w['agents'];around[a].add(b);around[b].add(a)
        loops[vertex]=cycle(around)
        assert len(loops[vertex])==(3 if vertex.startswith('F_') else 6)
    # Layout-only positive spring weights spread the small triangular faces;
    # they do not change interaction coefficients or topology.
    layout_weights={tuple(sorted(w['agents'])):F(1) if w['kind']=='outer' else F(1,2) for w in wires}
    pos=tutte(dual,{'AB':(550,150),'BC':(980,895),'CA':(120,895)},layout_weights)
    assert min(hypot(float(pos[a][0]-pos[b][0]),float(pos[a][1]-pos[b][1])) for a,b in combinations(pos,2))>70
    check_planar(pos,[w['agents'] for w in wires])
    svg=opening('Intrinsic interaction net — proton-like carrier',
                '12 triangle agents · 18 shared-edge wires · four triangular and four hexagonal cycles')
    # Fill the actual bounded faces of the net. The fourth triangular face is
    # the unbounded exterior, labelled explicitly below the drawing.
    for vertex,route in loops.items():
        if vertex=='F_ABC': continue
        coordinates=' '.join(f'{float(pos[v][0]):.3f},{float(pos[v][1]):.3f}' for v in route)
        fill='#eaf2fb' if vertex.startswith('F_') else '#f3f5f8'
        svg.append(f'<polygon points="{coordinates}" fill="{fill}" stroke="none"><title>Closed cycle around shared vertex {escape(vertex)}</title></polygon>')
        x=sum(pos[v][0] for v in route)/len(route);y=sum(pos[v][1] for v in route)/len(route)
        label=vertex.replace('F_','F ')
        svg.append(f'<text x="{float(x):.3f}" y="{float(y)+5:.3f}" text-anchor="middle" font-size="{14 if vertex.startswith("F_") else 23}" fill="#74869a">{label}</text>')
    ports={}
    for w in wires:
        a,b=w['agents']
        for p,q in ((a,b),(b,a)):
            x,y=map(float,pos[p]);tx,ty=map(float,pos[q]);length=hypot(tx-x,ty-y)
            ports[p,q]=(x+23*(tx-x)/length,y+23*(ty-y)/length)
        x,y=ports[a,b];tx,ty=ports[b,a]
        col='#9a6727' if w['kind']=='outer' else '#426583'
        desc=f"{a} ↔ {b}; shared edge {'–'.join(w['shared_edge'])}"
        svg.append(f'<path class="wire" data-a="{a}" data-b="{b}" d="M{x:.3f} {y:.3f} L{tx:.3f} {ty:.3f}" fill="none" stroke="{col}" stroke-width="2.2" marker-start="url(#arrow)" marker-end="url(#arrow)"><title>{escape(desc)}</title></path>')
    for name in sorted(tris):
        x,y=map(float,pos[name])
        svg.append(f'<g class="agent" id="agent-{name}"><title>Triangle {escape(" – ".join(tris[name]))}</title><circle cx="{x:.3f}" cy="{y:.3f}" r="18" fill="white" stroke="#263f57" stroke-width="2"/><text x="{x:.3f}" y="{y+4.5:.3f}" text-anchor="middle" font-size="12" font-weight="700">{name}</text></g>')
        for other in sorted(dual[name]):
            w=next(w for w in wires if set(w['agents'])=={name,other})
            x,y=ports[name,other];fill='#9a6727' if w['kind']=='outer' else 'white'
            svg.append(f'<circle class="port" cx="{x:.3f}" cy="{y:.3f}" r="3.1" fill="{fill}" stroke="#4c647a" stroke-width="1.2"/>')
    svg+=['<text x="550" y="947" text-anchor="middle" font-size="15">F ABC — the outer triangular cycle</text>',
          '<circle cx="45" cy="995" r="4" fill="#9a6727"/><text x="60" y="1000" class="note">Filled port: parent tetrahedron edge. Open port: centroid edge.</text>',
          '<text x="40" y="1027" class="note">Each wire identifies one shared edge; its two arrowheads retain the opposite boundary orientations.</text>',
          '<text x="40" y="1054" class="note">A–D and F labels mark cycles around the eight shared geometric vertices.</text>',
          '<text x="40" y="1081" class="note">Structural incidence view. The 1836 coefficient-transfer expansion is a separate graph.</text>',
          '</svg>']
    agent_path=OUT/'proton-like-canonical-interaction-net.svg'
    agent_path.write_text('\n'.join(svg)+'\n',encoding='utf-8')
    # Companion primal view: the eight actual shared vertices, eighteen edge
    # pairs, and all twelve oriented triangle loops with no stage duplication.
    # Nested barycentric embedding keeps the eight shared vertices separated.
    ppos={v:tuple(map(F,xy)) for v,xy in {'F_ABC':(550,150),'A':(980,895),'B':(120,895)}.items()}
    ppos['C']=tuple((2*ppos['F_ABC'][i]+ppos['A'][i]+ppos['B'][i])/4 for i in (0,1))
    ppos['D']=tuple(sum(ppos[v][i] for v in 'ABC')/3 for i in (0,1))
    for face in ('ABD','ACD','BCD'):
        ppos['F_'+face]=tuple(sum(ppos[v][i] for v in face)/3 for i in (0,1))
    check_planar(ppos,list(incidence))
    assert min(hypot(float(ppos[a][0]-ppos[b][0]),float(ppos[a][1]-ppos[b][1])) for a,b in combinations(ppos,2))>70
    svg=opening('Shared-vertex interaction net — proton-like carrier',
                '8 shared vertices · 18 edge pairs · 36 directed arrows · 12 triangle cycles')
    face_colors={'F_ABC':'#e6f0fb','F_ABD':'#e8f4ee','F_ACD':'#fbefe3','F_BCD':'#f3eaf8'}
    for name,t in sorted(tris.items()):
        if name=='AB': continue
        xy=' '.join(f'{float(ppos[v][0]):.3f},{float(ppos[v][1]):.3f}' for v in t)
        svg.append(f'<polygon points="{xy}" fill="{face_colors[t[0]]}" stroke="none"/>')
        x=sum(ppos[v][0] for v in t)/3;y=sum(ppos[v][1] for v in t)/3
        svg.append(f'<text x="{float(x):.3f}" y="{float(y)+4:.3f}" text-anchor="middle" font-size="12" fill="#697e92">{name}</text>')
    emitted=set()
    for name,t in sorted(tris.items()):
        for a,b in zip(t,t[1:]+t[:1]):
            assert (a,b) not in emitted;emitted.add((a,b))
            x,y=map(float,ppos[a]);tx,ty=map(float,ppos[b]);length=hypot(tx-x,ty-y)
            ux,uy=(tx-x)/length,(ty-y)/length;nx,ny=-uy,ux
            x,y=x+24*ux+2.6*nx,y+24*uy+2.6*ny
            tx,ty=tx-24*ux+2.6*nx,ty-24*uy+2.6*ny
            svg.append(f'<path class="arrow" d="M{x:.3f} {y:.3f} L{tx:.3f} {ty:.3f}" fill="none" stroke="#30475d" stroke-width="1.5" marker-end="url(#arrow)"><title>{escape(a)} → {escape(b)}; triangle {name}</title></path>')
    assert len(emitted)==36 and all((b,a) in emitted for a,b in emitted)
    for name in sorted(primal):
        x,y=map(float,ppos[name]);centre=name.startswith('F_')
        svg.append(f'<circle class="vertex" cx="{x:.3f}" cy="{y:.3f}" r="18" fill="{"#e9f1f8" if centre else "white"}" stroke="#263f57" stroke-width="2"/>')
        label='F' if centre else name
        svg.append(f'<text x="{x:.3f}" y="{y+5:.3f}" text-anchor="middle" font-size="15" font-weight="700">{label}</text>')
        if centre: svg.append(f'<text x="{x+24:.3f}" y="{y-15:.3f}" font-size="12">{name[2:]}</text>')
    svg+=['<text x="550" y="947" text-anchor="middle" font-size="15">AB — the outer triangle cycle (F ABC → A → B → F ABC)</text>',
          '<text x="40" y="996" class="note">Each shared vertex appears once. Parallel arrows show the two boundary directions on each edge.</text>',
          '<text x="40" y="1024" class="note">This planar drawing preserves incidence; it is not a flattening of the spatial tetrahedral geometry.</text>',
          '<text x="40" y="1052" class="note">Triangle labels match the agents in the companion incidence-net diagram.</text>',
          '<text x="40" y="1080" class="note">These 36 geometric arrows are distinct from the 1836 coefficient-transfer arrows.</text>',
          '</svg>']
    primal_path=OUT/'proton-like-shared-vertex-net.svg'
    primal_path.write_text('\n'.join(svg)+'\n',encoding='utf-8')
    ns={'s':'http://www.w3.org/2000/svg'}
    a=ET.parse(agent_path);p=ET.parse(primal_path)
    assert len(a.findall('.//s:g[@class="agent"]',ns))==12
    assert len(a.findall('.//s:path[@class="wire"]',ns))==18
    assert len(a.findall('.//s:circle[@class="port"]',ns))==36
    assert len(p.findall('.//s:circle[@class="vertex"]',ns))==8
    assert len(p.findall('.//s:path[@class="arrow"]',ns))==36
    manifest={'agents':tris,'shared_wires':wires,'closed_cycles_by_shared_vertex':loops,
              'shared_vertices':8,'shared_edges':18,'geometric_directed_arrows':36,
              'layout':'weighted Tutte dual and nested barycentric primal; no processing-stage vertices',
              'scope':'Structural incidence dual and primal of the carrier. Port markings distinguish outer from centroid edges; no interaction-net rewrite rules are asserted.'}
    (OUT/'proton-like-canonical-net.json').write_text(json.dumps(manifest,indent=2)+'\n')
    print(agent_path);print(primal_path)
    print('Verified: 12 trivalent agents, 18 shared wires, 8 closed face cycles; primal 8 vertices and 36 arrows. Both layouts have no proper edge crossings.')

if __name__=='__main__': main()
