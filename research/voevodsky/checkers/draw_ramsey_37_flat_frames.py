"""Build a standalone SVG/HTML wiring viewer from the verified red-edge record."""
import json, math
from pathlib import Path
H=Path(__file__).resolve().parents[1]
g=json.loads((H/'results/ramsey_37_dual_stars.json').read_text()); E=set(map(tuple,g['red_edges'])); rows=g['rows']; P,Q=0,6
xy={P:(110,348),Q:(790,348)}; names={P:'P',Q:'Q'}; panel=[]; local={}; scale=math.pi/180
for i in range(5):
    x=450+238*math.cos((-90+72*i)*scale);y=340+231*math.sin((-90+72*i)*scale)
    for j,(dx,dy) in enumerate([(0,-46),(-48,0),(48,0),(0,46)]):
        v=rows[j][i];xy[v]=(x+dx,y+dy);names[v]='ABCD'[j]+str(i);local[v]=i
    panel.append(f'<text x="{x}" y="{y-70}" text-anchor="middle" class="frame">Frame {i}</text>')
    for j,k in [(0,1),(0,2),(1,2),(1,3),(2,3)]:
        a,b=rows[j][i],rows[k][i];panel.append(f'<line x1="{xy[a][0]}" y1="{xy[a][1]}" x2="{xy[b][0]}" y2="{xy[b][1]}" stroke="#d4d9df"/>')
assert len(xy)==22 and len(E)==66 and all(sum(v in e for e in E)==6 for v in xy)
wires=[];nodes=[]
for a in sorted(xy):
    for b in sorted(v for v in xy if v>a):
        x,y=xy[a];u,v=xy[b];inside=a in local and local.get(b)==local[a];red=(a,b) in E
        if inside and {names[a][0],names[b][0]}=={'A','D'}:path=f'M{x},{y} C{x+96},{y} {u+96},{v} {u},{v}'
        else:path=f'M{x},{y} L{u},{v}'
        wires.append(f'<path class="wire" data-a="{a}" data-b="{b}" data-red="{int(red)}" data-local="{int(inside)}" d="{path}" fill="none" stroke="{("#b63124" if red else "#2367aa")}" {("" if red else chr(115)+"troke-dasharray=\"5 4\"") }><title>{names[a]} — {names[b]}</title></path>')
    x,y=xy[a];nodes.append(f'<g class="node" role="button" tabindex="0" aria-label="Select {names[a]}" data-id="{a}" transform="translate({x},{y})"><circle r="15"/><text y="4" text-anchor="middle">{names[a]}</text></g>')
html='''<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>22 addresses · five flat frames</title><style>body{font:16px system-ui;margin:1rem auto;padding:0 1rem;max-width:950px;color:#182638}h1{font-size:1.5rem}svg{width:100%;height:auto;border:1px solid #ddd}.node{cursor:pointer}.node circle{fill:white;stroke:#25374a;stroke-width:2}.node.active circle,.node:focus circle{fill:#ffde85}.node text{font:bold 12px system-ui;pointer-events:none}.frame{font:14px system-ui;fill:#566473}.wire{stroke-width:2.4}button,select{font:inherit}p{max-width:80ch}</style><h1>22 addresses · five flat tetrahedral frames</h1><p>Each diamond is ABC above BCD, sharing BC. The curved AD wire is the sixth edge, not a new vertex. Gray lines are frame guides; crossings are not junctions. Solid red and dashed blue are graph colors.</p><label>View <select id="mode"><option value="local">Inside each frame: both colors</option><option value="red">Selected address: 6 red wires</option><option value="blue">Selected address: 15 blue wires</option><option value="all">Whole graph: 66 red wires</option></select></label> · Click any address to trace its red wires.<p id="info" aria-live="polite"></p><svg viewBox="0 0 900 640" aria-label="Five flat frames and two poles">'''+''.join(panel+wires+nodes)+'''</svg><script>const ns=[...document.querySelectorAll('.node')],ws=[...document.querySelectorAll('.wire')],sel=document.querySelector('#mode'),info=document.querySelector('#info');let id='1';const name=i=>ns.find(n=>n.dataset.id===i).textContent;function draw(){let m=sel.value,others=[];for(let w of ws){let {a,b,red,local}=w.dataset,t=a===id||b===id,on=m==='local'?local==='1':m==='all'?red==='1':t&&red===(m==='red'?'1':'0');w.style.display=on?'':'none';if(on&&t)others.push(name(a===id?b:a))}for(let n of ns)n.classList.toggle('active',n.dataset.id===id&&(m==='red'||m==='blue'));info.textContent=m==='local'?'Each frame: AB, AC, AD red; BC, BD, CD blue.':m==='all'?'Every unshown pair is blue.':`${name(id)} · ${m} neighbors: ${others.join(', ')}`;}for(let n of ns){let pick=()=>{id=n.dataset.id;if(sel.value!=='blue')sel.value='red';draw()};n.onclick=pick;n.onkeydown=e=>{if(['Enter',' '].includes(e.key)){e.preventDefault();pick()}}}sel.onchange=draw;draw()</script>'''
p=H/'results/ramsey_37_flat_frames.html';p.write_text(html,encoding='utf8');print(p)
