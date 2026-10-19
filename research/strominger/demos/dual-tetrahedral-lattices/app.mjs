import * as M from './model.mjs';
const pair=M.pair(),patch=M.patch(),ring=M.elementaryLoop();
const initial={ax:-.38,ay:.55};let camera={...initial},family='both';
const color={P:'#f3a47e',N:'#75c6e8',A:'#ffb38b',B:'#87d8f1'};
const options=()=>({faces:document.querySelector('#faces').checked,centers:document.querySelector('#centers').checked,ring:document.querySelector('#ring').checked});
function rotation(p,origin){const [x0,y0,z0]=p.map((x,i)=>x-origin[i]),cy=Math.cos(camera.ay),sy=Math.sin(camera.ay),cx=Math.cos(camera.ax),sx=Math.sin(camera.ax),x=cy*x0+sy*z0,z=-sy*x0+cy*z0;return{x,y:cx*y0-sx*z,z:sx*y0+cx*z};}
function draw(canvas,source,isPair){
 const rect=canvas.getBoundingClientRect(),w=rect.width,h=rect.height,dpr=Math.min(devicePixelRatio||1,2);canvas.width=Math.round(w*dpr);canvas.height=Math.round(h*dpr);const c=canvas.getContext('2d');c.scale(dpr,dpr);c.clearRect(0,0,w,h);
 const origin=isPair?[.5,.5,.5]:[0,0,0],extent=isPair?3.15:7.4,scale=Math.min(w*.43,h*.46)/extent,cx=w/2,cy=h/2+5;
 const project=p=>{const q=rotation(p,origin);return{x:cx+q.x*scale,y:cy-q.y*scale,z:q.z};};
 const cells=source.filter(t=>family==='both'||t.kind===family),vertices=new Map(),triangles=[],edges=[];
 for(const t of cells){for(const v of t.vertices)vertices.set(v.id,v);vertices.set(t.center.id,t.center);
  for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)edges.push({p:project(t.vertices[i].point),q:project(t.vertices[j].point),kind:t.kind});
  if(options().faces)for(const indices of [[0,1,2],[0,1,3],[0,2,3],[1,2,3]]){const p=indices.map(i=>project(t.vertices[i].point));triangles.push({p,depth:p.reduce((s,q)=>s+q.z,0)/3,kind:t.kind});}
 }
 triangles.sort((a,b)=>a.depth-b.depth);
 for(const f of triangles){c.beginPath();f.p.forEach((p,i)=>i?c.lineTo(p.x,p.y):c.moveTo(p.x,p.y));c.closePath();c.fillStyle=color[f.kind];c.globalAlpha=isPair?.17:.025;c.fill();}c.globalAlpha=1;
 if(options().centers){c.setLineDash([3,4]);c.strokeStyle='#adc7dc';c.globalAlpha=isPair?.45:.14;c.lineWidth=.8;for(const t of cells)for(const v of t.vertices){const p=project(t.center.point),q=project(v.point);c.beginPath();c.moveTo(p.x,p.y);c.lineTo(q.x,q.y);c.stroke();}c.setLineDash([]);c.globalAlpha=1;}
 edges.sort((a,b)=>a.p.z+a.q.z-b.p.z-b.q.z);for(const e of edges){c.strokeStyle=color[e.kind];c.globalAlpha=isPair?.9:.26;c.lineWidth=isPair?1.8:.8;c.beginPath();c.moveTo(e.p.x,e.p.y);c.lineTo(e.q.x,e.q.y);c.stroke();}c.globalAlpha=1;
 if(!isPair&&options().ring&&family==='both'){c.strokeStyle='#f4da84';c.lineWidth=2.7;c.beginPath();ring.forEach((v,i)=>{const p=project(v.point);i?c.lineTo(p.x,p.y):c.moveTo(p.x,p.y);});c.closePath();c.stroke();}
 const dots=[...vertices.values()].map(v=>({...v,screen:project(v.point)})).sort((a,b)=>a.screen.z-b.screen.z);
 for(const v of dots){const p=v.screen,r=isPair?5:2.5;c.beginPath();c.arc(p.x,p.y,r,0,Math.PI*2);c.fillStyle=color[v.family];c.globalAlpha=isPair?1:.8;c.fill();}c.globalAlpha=1;
 if(isPair)for(const t of cells){const p=project(t.center.point),dx=t.kind==='P'?52:-135,dy=t.kind==='P'?-44:44,label=`${t.kind} center / ${t.vertexFamily==='A'?'B':'A'} site`;c.strokeStyle=color[t.kind];c.lineWidth=1;c.beginPath();c.moveTo(p.x,p.y);c.lineTo(p.x+dx*.7,p.y+dy);c.stroke();const x=Math.max(12,Math.min(w-144,p.x+dx*.7+(dx<0?-100:0))),y=p.y+dy-10;c.fillStyle='#091321ee';c.fillRect(x-6,y-4,132,25);c.fillStyle=color[t.kind];c.font='12px system-ui';c.fillText(label,x,y+12);c.beginPath();c.arc(p.x,p.y,9,0,Math.PI*2);c.stroke();}
 return {tetrahedra:cells.length,sites:vertices.size};
}
let counts={};function render(){counts.pair=draw(document.querySelector('#pair'),pair,true);counts.patch=draw(document.querySelector('#patch'),patch,false);document.querySelector('#patch-count').textContent=`${counts.patch.tetrahedra} displayed tetrahedra · halo retained`;}
for(const canvas of document.querySelectorAll('canvas')){let last=null;canvas.addEventListener('pointerdown',e=>{last=[e.clientX,e.clientY];canvas.setPointerCapture(e.pointerId);});canvas.addEventListener('pointermove',e=>{if(!last)return;camera.ay+=(e.clientX-last[0])*.009;camera.ax+=(e.clientY-last[1])*.009;last=[e.clientX,e.clientY];render();});for(const event of ['pointerup','pointercancel'])canvas.addEventListener(event,()=>last=null);canvas.addEventListener('keydown',e=>{const changes={ArrowLeft:[0,-.12],ArrowRight:[0,.12],ArrowUp:[-.12,0],ArrowDown:[.12,0]};if(changes[e.key]){e.preventDefault();camera.ax+=changes[e.key][0];camera.ay+=changes[e.key][1];render();}});}
for(const button of document.querySelectorAll('[data-family]'))button.addEventListener('click',()=>{family=button.dataset.family;document.querySelectorAll('[data-family]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));render();});
for(const input of document.querySelectorAll('input'))input.addEventListener('change',render);
document.querySelector('#reset').addEventListener('click',()=>{camera={...initial};render();});
window.dualTetra={model:M,pair,patch,ring,get camera(){return{...camera};},get family(){return family;},get counts(){return counts;},render};
new ResizeObserver(render).observe(document.querySelector('.views'));render();
