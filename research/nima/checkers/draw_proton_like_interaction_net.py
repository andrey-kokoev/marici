"""Draw the recorded 1836-arrow net, its exact support matrices, and carrier.

No layout edges are invented: every interaction path comes from the endpoint
manifest. Spatial carrier edges are shown separately in an inset.
"""
from collections import Counter
from html import escape
from math import cos, sin, pi, sqrt
from pathlib import Path
import json
import xml.etree.ElementTree as ET
from check_twelve_triangle_positive_geometry import POINTS, mean

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'results'


def main():
    arrows=json.loads((DEST/'twelve-triangle-1836-arrows.json').read_text())
    geometry=json.loads((DEST/'twelve-triangle-positive-geometry.json').read_text())
    stages=('raw','local','aligned')
    sites=sorted({a['source'][1] for a in arrows})
    assert len(sites)==12 and len(arrows)==1836
    ports={tuple(a[k]) for a in arrows for k in ('source','target')}
    assert len(ports)==108
    assert len({(tuple(a['source']),tuple(a['target'])) for a in arrows})==1836
    counts=Counter(a['source'][0] for a in arrows)
    assert [counts[s] for s in stages]==[108,432,1296]
    colors={'raw':'#087f8c','local':'#2563c5','aligned':'#a14286'}
    opacity={'raw':.72,'local':.16,'aligned':.043}
    centers={'raw':-90,'local':30,'aligned':150}
    cx,cy,r=530,540,326
    def polar(radius,degrees):
        angle=degrees*pi/180
        return cx+radius*cos(angle),cy+radius*sin(angle)
    def angle(port):
        stage,site,axis=port
        return centers[stage]-50+(sites.index(site)+.5)*100/12+('xyz'.index(axis)-1)*2
    def point(port,radius=r): return polar(radius,angle(port))
    lines=['<svg xmlns="http://www.w3.org/2000/svg" width="1510" height="1050" viewBox="0 0 1510 1050" role="img" aria-labelledby="title desc">',
           '<title id="title">Proton-like interaction net: 1836 directed arrows</title>',
           '<desc id="desc">Three stages with twelve triangle groups and three coordinate ports per group. Every one of the 1836 recorded arrows is drawn. Insets show the spatial tetrahedral carrier and exact adjacency supports.</desc>',
           '<defs>']
    for s,col in colors.items():
        lines.append(f'<marker id="head-{s}" markerWidth="5" markerHeight="5" refX="4.6" refY="2.5" orient="auto" markerUnits="userSpaceOnUse"><path d="M0,0 L5,2.5 L0,5 Z" fill="{col}"/></marker>')
    lines+=['</defs>',
            '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#17253a} .edge:hover{stroke-opacity:1;stroke-width:2.5} .small{font-size:12px;fill:#586779}</style>',
            '<rect width="1510" height="1050" fill="#fbfcfe"/>',
            '<text x="35" y="43" font-size="28" font-weight="650">Proton-like interaction net</text>',
            '<text x="35" y="73" font-size="16" fill="#586779">12 triangles · 3 coordinate ports per triangle · 3 stages · 1836 directed arrows</text>',
            '<path d="M1040 103 V1007" stroke="#dce3ec"/>']
    # Draw all actual edges, with sparse local selection above the dense return.
    for stage in ('aligned','local','raw'):
        lines.append(f'<g id="edges-{stage}">')
        for i,a in enumerate(arrows):
            if a['source'][0]!=stage: continue
            src,dst=tuple(a['source']),tuple(a['target'])
            assert stages[(stages.index(stage)+1)%3]==dst[0]
            x,y=point(src,r-4);tx,ty=point(dst,r-5)
            bx,by=point(src,r*.39);ex,ey=point(dst,r*.39)
            label=f'{src[0]} {src[1]}.{src[2]} → {dst[0]} {dst[1]}.{dst[2]}; weight {a["weight_real"]} + ({a["weight_imag_sqrt3"]}) i√3'
            width=1.1 if stage=='raw' else .7
            lines.append(f'<path class="edge" id="interaction-{i}" d="M{x:.3f},{y:.3f} C{bx:.3f},{by:.3f} {ex:.3f},{ey:.3f} {tx:.3f},{ty:.3f}" fill="none" stroke="{colors[stage]}" stroke-width="{width}" stroke-opacity="{opacity[stage]}" marker-end="url(#head-{stage})"><title>{escape(label)}</title></path>')
        lines.append('</g>')
    headings={'raw':('RAW','Local selection · 12 × 3²'),
              'local':('LOCAL MODES','Alignment · 12² × 3'),
              'aligned':('ALIGNED MODES','Feedback · 12² × 3²')}
    for stage in stages:
        for site in sites:
            centre=centers[stage]-50+(sites.index(site)+.5)*100/12
            x1,y1=polar(r+20,centre-3.1);x2,y2=polar(r+20,centre+3.1)
            lines.append(f'<path d="M{x1:.3f},{y1:.3f} A{r+20},{r+20} 0 0 1 {x2:.3f},{y2:.3f}" fill="none" stroke="{colors[stage]}" stroke-width="2"/>')
            x,y=polar(r+38,centre)
            lines.append(f'<text x="{x:.3f}" y="{y+4:.3f}" font-size="12" text-anchor="middle" font-weight="600">{site}</text>')
            for axis in 'xyz':
                port=(stage,site,axis);x,y=point(port)
                lines.append(f'<circle class="port" cx="{x:.3f}" cy="{y:.3f}" r="3.4" fill="white" stroke="{colors[stage]}" stroke-width="1.6"><title>{stage} {site}.{axis}</title></circle>')
                tx,ty=point(port,r+11)
                lines.append(f'<text x="{tx:.3f}" y="{ty+2.5:.3f}" text-anchor="middle" font-size="7.5">{axis}</text>')
        x,y=polar(r+120,centers[stage]);title,subtitle=headings[stage]
        lines.append(f'<text x="{x:.3f}" y="{y:.3f}" text-anchor="middle" font-size="16" font-weight="700">{title}</text>')
        lines.append(f'<text x="{x:.3f}" y="{y+22:.3f}" text-anchor="middle" font-size="13">{subtitle}</text>')
    # Geometry is a separate view, not a placement of the three-stage ports.
    lines.append('<text x="1080" y="123" font-size="17" font-weight="650">Spatial carrier</text>')
    points=dict(POINTS)
    for row in geometry['triangles_and_transports']:
        label=row['triangle'][0]
        face=label.split('_')[1]
        points[label]=mean([POINTS[k] for k in face])
    def spatial(p):
        x,y,z=map(float,p)
        return 1250+66*(4*x-3*y)/5,222-66*(3*x+4*y-5*z)/sqrt(50)
    tris=[row['triangle'] for row in geometry['triangles_and_transports']]
    def depth(t): return sum(3*float(points[k][0])+4*float(points[k][1])+5*float(points[k][2]) for k in t)/3
    for t in sorted(tris,key=depth):
        pts=' '.join(f'{x:.3f},{y:.3f}' for x,y in (spatial(points[k]) for k in t))
        lines.append(f'<polygon points="{pts}" fill="#647f9f" fill-opacity=".065" stroke="#667e98" stroke-opacity=".7" stroke-width="1.1"><title>{escape(" – ".join(t))}</title></polygon>')
    for label,p in points.items():
        x,y=spatial(p)
        lines.append(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="{3 if label in POINTS else 1.8}" fill="#334f6d"/>')
        if label in POINTS: lines.append(f'<text x="{x+7:.3f}" y="{y-6:.3f}" font-size="13" font-weight="600">{label}</text>')
    lines.append('<text x="1080" y="337" class="small">Four faces, three triangles per face.</text>')
    # Exact source-column/target-row support matrices make the dense graph legible.
    cell=4.7;size=36*cell;mx=1160
    matrix_titles={'raw':'Local selection — 108 arrows',
                   'local':'Frame alignment — 432 arrows',
                   'aligned':'Collective return — 1296 arrows'}
    for stage,my in zip(stages,(395,608,821)):
        lines.append(f'<text x="1080" y="{my-33}" font-size="15" font-weight="600">{matrix_titles[stage]}</text>')
        lines.append(f'<rect x="{mx}" y="{my}" width="{size}" height="{size}" fill="white" stroke="#a7b4c4"/>')
        entries=0
        for a in arrows:
            if a['source'][0]!=stage: continue
            si=sites.index(a['source'][1])*3+'xyz'.index(a['source'][2])
            ti=sites.index(a['target'][1])*3+'xyz'.index(a['target'][2])
            lines.append(f'<rect class="matrix-entry" x="{mx+si*cell:.3f}" y="{my+ti*cell:.3f}" width="{cell}" height="{cell}" fill="{colors[stage]}"/>')
            entries+=1
        assert entries==counts[stage]
        for g,site in enumerate(sites):
            pos=(g*3+1.5)*cell
            lines.append(f'<text x="{mx+pos:.3f}" y="{my-7}" font-size="7.5" text-anchor="middle">{site}</text>')
            lines.append(f'<text x="{mx-6}" y="{my+pos+2.5:.3f}" font-size="7.5" text-anchor="end">{site}</text>')
        for k in range(1,12):
            off=k*3*cell
            lines.append(f'<path d="M{mx+off:.3f},{my} v{size} M{mx},{my+off:.3f} h{size}" stroke="#e4e9f0" stroke-width=".65" fill="none"/>')
        lines.append(f'<text x="{mx+size+13:.3f}" y="{my+20}" class="small">Columns:</text>')
        lines.append(f'<text x="{mx+size+13:.3f}" y="{my+37}" class="small">source ports</text>')
        lines.append(f'<text x="{mx+size+13:.3f}" y="{my+70}" class="small">Rows:</text>')
        lines.append(f'<text x="{mx+size+13:.3f}" y="{my+87}" class="small">target ports</text>')
    lines+=['<text x="35" y="976" font-size="15" font-weight="600">AB … DC label the twelve triangles. Each group contains x, y, z ports.</text>',
            '<text x="35" y="1001" class="small">Every curve is one recorded directed arrow. Hover an edge for its endpoints and exact weight.</text>',
            '<text x="35" y="1022" class="small">The circular layout separates processing stages; the inset shows the spatial body. This depicts the proposed 1836-arrow implementation.</text>',
            '</svg>']
    path=DEST/'proton-like-interaction-net.svg'
    path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    tree=ET.parse(path);ns={'s':'http://www.w3.org/2000/svg'}
    assert len(tree.findall('.//s:path[@class="edge"]',ns))==1836
    assert len(tree.findall('.//s:circle[@class="port"]',ns))==108
    assert len(tree.findall('.//s:rect[@class="matrix-entry"]',ns))==1836
    print(str(path))
    print('Verified SVG: all 1836 recorded arrows, 108 ports, three exact support matrices, and separate twelve-triangle carrier.')

if __name__=='__main__': main()
