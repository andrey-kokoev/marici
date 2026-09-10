"""Generate the typed three-plane/requirement-dual Three.js RH viewer."""
import json
from pathlib import Path
from rh_net_state_compiler import compile_rh_net_state

def render_rh_net(contract):
    report=compile_rh_net_state(contract)
    if not report.get("passed"):raise ValueError(str(report))
    payload=json.dumps({"contract":contract,"report":report},separators=(",",":"))
    return f'''<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>SCC RH typed span</title>
<style>:root{{color-scheme:dark;font-family:system-ui;background:#071117;color:#e9f0f3}}*{{box-sizing:border-box}}body{{margin:0;display:grid;grid-template-rows:auto 1fr;height:100vh}}header{{display:flex;gap:12px;align-items:center;padding:12px 18px;border-bottom:1px solid #29414c}}h1{{font-size:20px;margin:0 auto 0 0}}button{{background:#132a35;color:#dcebf0;border:1px solid #42606d;border-radius:6px;padding:7px}}button.active{{background:#37647a}}main{{display:grid;grid-template-columns:1fr 340px;min-height:0}}#scene{{position:relative;overflow:hidden}}aside{{padding:14px;border-left:1px solid #29414c;overflow:auto}}.node{{width:210px;padding:9px;border:2px solid var(--c);border-radius:8px;background:#0b1a22;box-shadow:0 5px 18px #000a;font-size:12px}}.node.selected{{box-shadow:0 0 20px var(--c)}}.node small{{display:block;color:#9db0b9}}pre{{white-space:pre-wrap;font-size:11px}}.legend{{position:absolute;z-index:3;left:12px;top:12px;background:#071117d9;padding:8px;border:1px solid #29414c}}@media(max-width:800px){{main{{grid-template-columns:1fr;grid-template-rows:60vh auto}}}}</style>
<script type="importmap">{{"imports":{{"three":"https://cdn.jsdelivr.net/npm/three@0.180.0/build/three.module.js","three/addons/":"https://cdn.jsdelivr.net/npm/three@0.180.0/examples/jsm/"}}}}</script></head><body><header><h1>SCC · RH typed span</h1><button id="span" class="active">R → Q ← P</button><button id="dual">requirement dual</button><button id="simulate">simulate locally</button></header><main><div id="scene"><div class="legend">Fixed semantic depth bands; depth is not physical time or evidential rank.</div></div><aside><b id="selection">Select a node</b><pre id="detail"></pre></aside></main>
<script type="application/json" id="payload">{payload.replace('</','<\\/')}</script><script type="module">
import * as THREE from 'three';import {{CSS3DRenderer,CSS3DObject}} from 'three/addons/renderers/CSS3DRenderer.js';import {{OrbitControls}} from 'three/addons/controls/OrbitControls.js';
const payload=JSON.parse(document.querySelector('#payload').textContent), sourceSnapshot=JSON.stringify(payload.contract), view=payload.report.visualization;
let mode='span',selected=null,simulated=false,objects=[];const scene=new THREE.Scene(),camera=new THREE.PerspectiveCamera(45,1,1,6000),renderer=new CSS3DRenderer();camera.position.set(0,600,1450);document.querySelector('#scene').append(renderer.domElement);renderer.domElement.style.position='absolute';renderer.domElement.style.inset=0;const controls=new OrbitControls(camera,renderer.domElement);controls.enableDamping=true;
const colors={{realization:'#55c2ff',invariant:'#62e6a7',presentation:'#d899ff',unclassified:'#ffb35c',requirement:'#ffe27a'}};
function clear(){{objects.forEach(o=>scene.remove(o));objects=[]}}
function card(id,kind,data,x,y,z){{const e=document.createElement('div');e.className='node'+(id===selected?' selected':'');e.style.setProperty('--c',colors[kind]);e.innerHTML=`<b>${{id}}</b><small>${{kind}}</small>`;e.onclick=()=>{{selected=id;document.querySelector('#selection').textContent=id;document.querySelector('#detail').textContent=JSON.stringify(data,null,2);render()}};const o=new CSS3DObject(e);o.position.set(x,y,z);scene.add(o);objects.push(o)}}
function render(){{clear();if(mode==='span'){{const ns=view.span.nodes;const groups={{}};for(const n of ns)(groups[n.semantic_plane]??=[]).push(n);for(const [plane,items] of Object.entries(groups))items.forEach((n,i)=>card(n.id,plane,{{node:n,fibers:view.span.fibers[n.id]||null,witnesses:(view.span.fibers[n.id]||{{}}).witnesses||[]}},(i-(items.length-1)/2)*245,(plane==='unclassified'?-350:0),n.semantic_depth));}}else{{const es=view.requirement_dual.edges;const cs=[...new Set(es.map(e=>e.constructor))];cs.forEach((id,i)=>card(id,'realization',{{requirements:view.requirement_dual.neighborhoods[id],candidate_only:true}},-330,(i-(cs.length-1)/2)*105,0));view.requirement_dual.requirements.forEach((r,i)=>card(r.id,'requirement',r,330,(i-(view.requirement_dual.requirements.length-1)/2)*150,0));}}}}
function resize(){{const d=document.querySelector('#scene'),w=d.clientWidth,h=d.clientHeight;camera.aspect=w/h;camera.updateProjectionMatrix();renderer.setSize(w,h)}}window.addEventListener('resize',resize);for(const id of ['span','dual'])document.querySelector('#'+id).onclick=()=>{{mode=id==='span'?'span':'requirement_dual';document.querySelector('#span').classList.toggle('active',mode==='span');document.querySelector('#dual').classList.toggle('active',mode!=='span');render()}};document.querySelector('#simulate').onclick=()=>{{simulated=!simulated;document.querySelector('#simulate').classList.toggle('active',simulated);if(JSON.stringify(payload.contract)!==sourceSnapshot)throw Error('simulation mutated contract')}};resize();render();(function loop(){{controls.update();renderer.render(scene,camera);requestAnimationFrame(loop)}})();
</script></body></html>'''

def write_rh_net_viewer(source, output):
    """Render one RH net contract path (or mapping) to an HTML output path."""
    contract = (json.loads(Path(source).read_text(encoding="utf-8"))
                if not isinstance(source, dict) else source)
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_rh_net(contract), encoding="utf-8")
    return {
        "passed": True,
        "output": str(output),
        "bytes": output.stat().st_size,
        "renderer": "three-css3d",
    }


def main():
    root=Path(__file__).resolve().parents[3]
    source=root/'research/aspect/contracts/theta-rh-interaction-net-state.v2.json'
    out=root/'research/aspect/results/rh_net_viewer.html'
    print(json.dumps(write_rh_net_viewer(source, out)))
if __name__=='__main__':main()
