(() => {
'use strict';
const $=id=>document.getElementById(id), T=window.THREE;
let renderer;
try {renderer=new T.WebGLRenderer({antialias:true});} catch(e){$('error').textContent='WebGL unavailable: '+e.message;return;}
const host=$('scene'), scene=new T.Scene();scene.background=new T.Color(0x0b1220);
renderer.setPixelRatio(Math.min(devicePixelRatio,2));host.append(renderer.domElement);
const camera=new T.PerspectiveCamera(45,1,.01,100);camera.up.set(0,0,1);camera.position.set(3,-4,3);
const controls=new T.OrbitControls(camera,renderer.domElement);controls.target.set(0,.25,0);controls.enableDamping=true;controls.update();
scene.add(new T.HemisphereLight(0xffffff,0x35445c,2));
const h=Math.sqrt(3)/2, A=new T.Vector3(), B=new T.Vector3(1,0,0), C=new T.Vector3(.5,h,0), D=new T.Vector3(-.5,h,0);
const axis=D.clone().normalize(), ca=C.clone().normalize();
const seed=['AB','AC','AD','BC','AE','AF','EF'], local=['BD','CD','DE','DF'], cross=['BE','BF','CE','CF'];
const edges={}, spheres={}, labels={}, faces=[];
for(const k of 'ABCDEF'){
 const mesh=new T.Mesh(new T.SphereGeometry(.035,16,12),new T.MeshStandardMaterial({color:k==='A'||k==='D'?0xffffff: 'BC'.includes(k)?0x7dd3fc:0xfca5a5}));scene.add(mesh);spheres[k]=mesh;
 const label=document.createElement('span');label.className='label';label.textContent=k;host.append(label);labels[k]=label;
}
for(const k of [...seed,...local,...cross]){
 const mesh=new T.Mesh(new T.CylinderGeometry(.012,.012,1,10),new T.MeshStandardMaterial({color:seed.includes(k)?0x7dd3fc:local.includes(k)?0xfbbf24:0xc084fc,transparent:true}));scene.add(mesh);edges[k]=mesh;
}
for(const [keys,color] of [['ABCD',0x7dd3fc],['AEFD',0xfca5a5]]){
 const geometry=new T.BufferGeometry();geometry.setAttribute('position',new T.BufferAttribute(new Float32Array(36),3));
 const mesh=new T.Mesh(geometry,new T.MeshBasicMaterial({color,side:T.DoubleSide,transparent:true,opacity:.16,depthWrite:false}));scene.add(mesh);faces.push({keys,mesh});
}
const clamp=x=>Math.max(0,Math.min(1,x)), smooth=x=>{x=clamp(x);return x*x*(3-2*x);};
let progress=0,playing=false,last=null,state;
function update(value){
 progress=clamp(Number(value)||0);
 const phi=Math.PI/3*smooth((progress-.15)/.3),theta=Math.acos(-1/3)*smooth((progress-.45)/.3),closure=smooth((progress-.75)/.25);
 const p={A:A.clone(),B:B.clone().applyAxisAngle(ca,theta).applyAxisAngle(axis,phi),C:C.clone().applyAxisAngle(axis,phi),D:D.clone(),E:B.clone().applyAxisAngle(ca,-theta).applyAxisAngle(axis,Math.PI-phi),F:C.clone().applyAxisAngle(axis,Math.PI-phi)};
 const global=$('scope').value==='global', closed=progress===1, active=[...seed,...local,...(global?cross:[])];
 for(const k of 'ABCDEF')spheres[k].position.copy(p[k]);
 for(const [k,mesh] of Object.entries(edges)){
  const delta=p[k[1]].clone().sub(p[k[0]]),len=delta.length();mesh.position.copy(p[k[0]]).add(p[k[1]]).multiplyScalar(.5);mesh.scale.set(1,len,1);mesh.quaternion.setFromUnitVectors(new T.Vector3(0,1,0),delta.normalize());mesh.visible=seed.includes(k)||(closure>0&&active.includes(k));mesh.material.opacity=seed.includes(k)?1:closure;
 }
 const volumes=[];
 for(const {keys,mesh} of faces){
  const vertices=[0,1,2,0,3,1,0,2,3,1,3,2].map(i=>p[keys[i]]),attr=mesh.geometry.attributes.position;
  vertices.forEach((v,i)=>attr.setXYZ(i,v.x,v.y,v.z));attr.needsUpdate=true;mesh.geometry.computeBoundingSphere();mesh.visible=$('faces').checked&&closed;
  const [a,b,c,d]=[...keys].map(k=>p[k]);volumes.push(Math.abs(b.clone().sub(a).dot(c.clone().sub(a).cross(d.clone().sub(a))))/6);
 }
 $('stage').textContent=progress<.15?'1 · Two flat paws':progress<.45?'2 · Bodies turn around shared AD':progress<.75?'3 · Compatible folds, shared AD fixed':'4 · '+(global?'Global closure: K₆':'Local closure: two tetrahedra');
 $('stats').textContent=`Relationships: ${closed?active.length:closure>0?'7 → '+active.length:7} · Directed packets: ${closed?2*active.length:14} · Closed tetrahedron volumes: ${closed?volumes.map(v=>v.toFixed(6)).join(', '):'0, 0'}`;
 $('witness').textContent=global?'Local: B–A–D, C–A–D, E–A–D, F–A–D. Cross-paw: B–A–E, B–A–F, C–A–E, C–A–F.':'Only paths within ABCD or AEFD are admitted; cross-paw paths are excluded.';
 $('timeline').value=progress;
 state={progress,closed,scope:global?'global':'local',edgeCount:closed?active.length:7,volumes,points:Object.fromEntries(Object.entries(p).map(([k,v])=>[k,v.toArray()])),visibleEdges:Object.fromEntries(Object.entries(edges).filter(([,m])=>m.visible).map(([k,m])=>[k,m.scale.y]))};
}
function play(on){playing=on;last=null;$('play').textContent=on?'Pause':'Play';}
$('play').onclick=()=>{if(!playing&&progress===1)update(0);play(!playing);};$('reset').onclick=()=>{play(false);update(0);};
$('timeline').oninput=e=>{play(false);update(e.target.value);};$('scope').onchange=$('faces').onchange=()=>update(progress);
new ResizeObserver(()=>{renderer.setSize(host.clientWidth,host.clientHeight);camera.aspect=host.clientWidth/host.clientHeight;camera.updateProjectionMatrix();}).observe(host);
function tick(time){requestAnimationFrame(tick);if(playing){if(last!==null&&!document.hidden)update(progress+Math.min((time-last)/1000,.1)/14);last=time;if(progress===1)play(false);}controls.update();renderer.render(scene,camera);for(const k of 'ABCDEF'){const p=spheres[k].position.clone().project(camera);labels[k].style.left=`${(p.x*.5+.5)*host.clientWidth}px`;labels[k].style.top=`${(-p.y*.5+.5)*host.clientHeight-20}px`;labels[k].style.display=Math.abs(p.z)>1?'none':'';}}
window.twoPaws={setProgress:v=>{play(false);update(v);},snapshot:()=>JSON.parse(JSON.stringify(state))};update(0);requestAnimationFrame(tick);
})();
