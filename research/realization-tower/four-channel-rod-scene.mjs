import {fourChannelRod} from './four-channel-rod.mjs';
import {cells,worldPoint} from './normal-ray-model.mjs';
const $=id=>document.getElementById(id),svg=$('view'),colors=['#ff81c4','#71d7ff','#f3cd71','#8de7b3'];
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],unit=a=>a.map(x=>x/Math.hypot(...a));
const base=fourChannelRod(7),up=unit(base.vertexPoints[0]),right=unit(cross(up,[0,0,1])),front=cross(right,up);
let yaw=.25,pitch=.65;
function draw(){
 const k=Number($('k').value),model=fourChannelRod(k,$('anchor').value),originY=model.anchor==='center'?330:135;
 function project(p){const x=dot(p,right),y=dot(p,up),z=dot(p,front),a=x*Math.cos(yaw)+z*Math.sin(yaw),b=-x*Math.sin(yaw)+z*Math.cos(yaw);return [500+90*a,originY-90*(y*Math.cos(pitch)-b*Math.sin(pitch)),y*Math.sin(pitch)+b*Math.cos(pitch)];}
 const point=p=>project(worldPoint(p).map((x,i)=>x-model.reference[i]));
 const c=project(model.centerPoint),v=model.vertexPoints.map(project),xy=p=>p.slice(0,2).join(',');
 let html='<defs>'+colors.map((color,i)=>`<marker id="arrow${i}" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 Z" fill="${color}"/></marker>`).join('')+'</defs>';
 for(let i=0;i<4;i++)for(let j=i+1;j<4;j++)html+=`<line x1="${v[i][0]}" y1="${v[i][1]}" x2="${v[j][0]}" y2="${v[j][1]}" stroke="#8194ad" stroke-width="1.5" opacity=".65"/>`;
 if($('carriers').checked){
  const faces=model.centerCandidates.flatMap(id=>[0,1,2,3].map(omit=>({id,points:cells[id].vertices.filter((_,i)=>i!==omit).map(point)}))).sort((a,b)=>a.points.reduce((s,p)=>s+p[2],0)-b.points.reduce((s,p)=>s+p[2],0));
  for(const f of faces)html+=`<polygon points="${f.points.map(xy).join(' ')}" fill="${model.centralCell===null?'#b9c1d0':'#42bbff'}" fill-opacity=".08" stroke="#71a3bb" stroke-width="1" stroke-opacity=".55"/>`;
 }
 for(const f of model.channels){
  const i=f.vertex-1,end=v[i],mid=c.map((x,j)=>(x+end[j])/2);
  html+=`<line data-fiber="${f.id}" x1="${c[0]}" y1="${c[1]}" x2="${end[0]}" y2="${end[1]}" stroke="${colors[i]}" stroke-width="${i===0?4:2.5}" ${i?'stroke-dasharray="8 6"':''}/>`;
  if(i===0){const lerp=t=>c.map((x,j)=>x+t*(end[j]-x)),a=lerp(.30),b=lerp(.70);html+=`<line x1="${a[0]}" y1="${a[1]}" x2="${b[0]}" y2="${b[1]}" stroke="${colors[i]}" stroke-width="2" marker-start="url(#arrow0)" marker-end="url(#arrow0)"/>`;}
  html+=`<text x="${mid[0]+12}" y="${mid[1]-10}" fill="${colors[i]}" font-size="17">F${i+1}${i===0?' · rod':''}</text>`;
 }
 v.forEach((p,i)=>{html+=`<circle cx="${p[0]}" cy="${p[1]}" r="6" fill="${colors[i]}"/><text x="${p[0]+12}" y="${p[1]-12}" fill="${colors[i]}" font-size="20">${i===0?'E · V₁':`V${['₁','₂','₃','₄'][i]}`}</text>`;});
 html+=`<path d="M${c[0]},${c[1]-9} l9,9 l-9,9 l-9,-9 Z" fill="#72d6ff"/><text x="${c[0]+16}" y="${c[1]+25}" fill="#72d6ff" font-size="20">P reference</text><text x="24" y="36" fill="#d7e4f6" font-size="18">k = ${k} · four retained channels · ${model.anchor==='center'?'P-centered':'E-anchored'}</text>`;
 svg.innerHTML=html;$('size').value=k;$('prev').disabled=k===1;$('next').disabled=k===7;
 $('status').textContent=model.centerStatus==='shared-seed-cell'?'k=1: the center lies in the E seed cell. P/E are proposed reference roles here, not two separately assigned particles. Four channel identities are retained.':model.centralCell!==null?`Center-containing tetrahedron: cell ${model.centralCell}. The rod and four channels are specified before choosing any neighboring P/N/E roles. No channel-to-face matching is assumed.`:`Center lies in ${model.centerCandidates.length} triangulation pieces (${model.centerCandidates.join(', ')}). No arbitrary piece is selected as P. The center reference and all four channels remain defined.`;
 $('channels').innerHTML=model.channels.map(f=>`<li>${f.id}: center [${f.from.join(', ')}] → V${f.vertex} [${f.to.join(', ')}]; ${f.status}</li>`).join('');
 globalThis.fourChannelAudit={...model,projection:{center:c,vertices:v},yaw,pitch};
}
for(const id of ['k','anchor','carriers'])$(id).addEventListener('input',draw);
$('prev').onclick=()=>{$('k').value=Number($('k').value)-1;draw();};$('next').onclick=()=>{$('k').value=Number($('k').value)+1;draw();};$('reset').onclick=()=>{yaw=.25;pitch=.65;draw();};
let drag=null;svg.onpointerdown=e=>{drag=[e.clientX,e.clientY];svg.setPointerCapture(e.pointerId);};svg.onpointermove=e=>{if(!drag)return;yaw+=(e.clientX-drag[0])*.008;pitch=Math.max(-1.4,Math.min(1.4,pitch+(e.clientY-drag[1])*.008));drag=[e.clientX,e.clientY];draw();};svg.onpointerup=svg.onpointercancel=()=>{drag=null;};
draw();
