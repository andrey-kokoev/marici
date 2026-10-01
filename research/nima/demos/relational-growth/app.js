(() => {
'use strict';
const $=id=>document.getElementById(id), T=window.THREE;
let renderer;
try { renderer=new T.WebGLRenderer({antialias:true}); }
catch(e){$('error').textContent='WebGL unavailable: '+e.message;return;}
const host=$('scene'),scene=new T.Scene();scene.background=new T.Color(0x0b1220);
renderer.setPixelRatio(Math.min(devicePixelRatio,2));host.prepend(renderer.domElement);
const camera=new T.PerspectiveCamera(45,1,.01,100);camera.position.set(4,-6,4);camera.up.set(0,0,1);
const controls=new T.OrbitControls(camera,renderer.domElement);controls.enableDamping=true;controls.minDistance=1;controls.maxDistance=20;
scene.add(new T.HemisphereLight(0xffffff,0x253a52,2));
const primitive=[[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]].map(v=>new T.Vector3(...v).multiplyScalar(.5));
const colors=[0x7dd3fc,0xfbbf24,0xc084fc,0x86efac];
// A fixed linear projection from separate coordinate blocks, chosen for legibility.
// The diminishing block scales are display choices, not a metric on the source.
const axes=[new T.Vector3(1,2,3).normalize(),new T.Vector3(2,-1,3).normalize(),new T.Vector3(-2,3,1).normalize(),new T.Vector3(3,1,-2).normalize()];
function project(tuple){const v=new T.Vector3();tuple.forEach((x,i)=>v.add(primitive[x].clone().applyAxisAngle(axes[i],i*.83).multiplyScalar(Math.pow(.43,i))));return v;}
const levels=[];
for(let level=0;level<3;level++){
 const arity=2**level,tuples=[];
 for(let i=0;i<4**arity;i++){let n=i;const t=Array(arity);for(let j=arity-1;j>=0;j--){t[j]=n%4;n=Math.floor(n/4);}tuples.push(t);}
 const pairs=[];for(let i=0;i<tuples.length;i++)for(let j=i+1;j<tuples.length;j++)if(tuples[i].every((v,k)=>v!==tuples[j][k]))pairs.push([i,j]);
 levels.push({arity,tuples,pairs,positions:tuples.map(project)});
}
const group=new T.Group();scene.add(group);group.scale.setScalar(2.2);
const ballGeometry=new T.SphereGeometry(1,12,8),materials=colors.map(color=>new T.MeshStandardMaterial({color}));
let meshes=[],edgeLines,parentLines,current=-1,progress=0,playing=false,last=null,state;
function lineObject(count,color,opacity){const g=new T.BufferGeometry();g.setAttribute('position',new T.BufferAttribute(new Float32Array(count*6),3));const m=new T.LineBasicMaterial({color,transparent:true,opacity,depthWrite:false});const line=new T.LineSegments(g,m);group.add(line);return line;}
function disposeLine(line){if(line){group.remove(line);line.geometry.dispose();line.material.dispose();}}
function selectLevel(level){
 if(level===current)return;current=level;
 meshes.forEach(m=>group.remove(m));disposeLine(edgeLines);disposeLine(parentLines);
 const data=levels[level];meshes=data.tuples.map((t,i)=>{const m=new T.Mesh(ballGeometry,materials[t[0]]);m.scale.setScalar(level===2?.019:level===1?.04:.06);m.userData.index=i;group.add(m);return m;});
 edgeLines=lineObject(data.pairs.length,0x7dd3fc,level===2?.035:level===1?.22:.7);
 parentLines=lineObject(data.tuples.length,0xfbbf24,.22);
}
const smooth=x=>x*x*(3-2*x),clamp=x=>Math.max(0,Math.min(2,x));
function update(value){
 progress=clamp(Number(value)||0);const level=Math.ceil(progress),phase=level===0?1:progress-(level-1),f=smooth(phase);selectLevel(level);
 const data=levels[level];
 const starts=data.tuples.map(t=>level?project(t.slice(0,t.length/2)):project(t));
 meshes.forEach((m,i)=>m.position.copy(starts[i]).lerp(data.positions[i],f));
 const ep=edgeLines.geometry.attributes.position;
 data.pairs.forEach(([a,b],i)=>{const x=meshes[a].position,y=meshes[b].position;ep.setXYZ(2*i,x.x,x.y,x.z);ep.setXYZ(2*i+1,y.x,y.y,y.z);});ep.needsUpdate=true;edgeLines.geometry.computeBoundingSphere();edgeLines.visible=$('edges').checked;
 const pp=parentLines.geometry.attributes.position;
 starts.forEach((x,i)=>{const y=meshes[i].position;pp.setXYZ(2*i,x.x,x.y,x.z);pp.setXYZ(2*i+1,y.x,y.y,y.z);});pp.needsUpdate=true;parentLines.geometry.computeBoundingSphere();parentLines.visible=$('parents').checked&&level>0&&phase<1;
 $('growth').value=progress;
 $('stage').textContent=level===0?'Present · primitive tetrahedral relation':`Square ${level} · ${phase===1?'complete':'unfolding ordered parent pairs'}`;
 $('stats').textContent=`${data.tuples.length} records · ${data.pairs.length} undirected relationships · ${data.pairs.length*2} directed arrows · ${data.arity} independent operands · product-model dimension ${2*data.arity}`;
 $('description').textContent=level===0?'Each of A, B, C, D is related to the other three. The Dowker complex of this relation is the tetrahedral boundary.':`Each ${levels[level-1].tuples.length}-record parent set is paired with itself. The new tuples start at their left parent's projection and unfold along the right operand's independent coordinate blocks. Both parents remain recorded; the line count is the complete target relation even during the illustrative motion.`;
 state={progress,level,phase,arity:data.arity,recordCount:data.tuples.length,edgeCount:data.pairs.length,arrowCount:2*data.pairs.length,modelDimension:2*data.arity,tuples:data.tuples,pairs:data.pairs,positions:meshes.map(m=>m.position.toArray()),parents:level?data.tuples.map(t=>[t.slice(0,t.length/2),t.slice(t.length/2)]):null};
}
function setPlaying(on){playing=on;last=null;$('play').textContent=on?'Pause':'Play growth';}
$('play').onclick=()=>{if(!playing&&progress===2)update(0);setPlaying(!playing);};$('reset').onclick=()=>{setPlaying(false);update(0);};
$('growth').oninput=e=>{setPlaying(false);update(e.target.value);};
document.querySelectorAll('[data-level]').forEach(b=>b.onclick=()=>{setPlaying(false);update(b.dataset.level);});
$('edges').onchange=$('parents').onchange=()=>update(progress);
const raycaster=new T.Raycaster(),mouse=new T.Vector2();
const name=t=>t.map(i=>'ABCD'[i]).join('');
renderer.domElement.addEventListener('pointermove',e=>{const r=renderer.domElement.getBoundingClientRect();mouse.set((e.clientX-r.left)/r.width*2-1,-(e.clientY-r.top)/r.height*2+1);raycaster.setFromCamera(mouse,camera);const hit=raycaster.intersectObjects(meshes)[0];if(hit){const i=hit.object.userData.index,t=levels[current].tuples[i];$('hover').textContent=current?`${name(t)} = (${name(t.slice(0,t.length/2))}, ${name(t.slice(t.length/2))}) · ordered parents`:`${name(t)} · primitive record`;}else $('hover').textContent='Drag to orbit · scroll to zoom · hover a record for its parents';});
new ResizeObserver(()=>{renderer.setSize(host.clientWidth,host.clientHeight);camera.aspect=host.clientWidth/host.clientHeight;camera.updateProjectionMatrix();}).observe(host);
function tick(time){requestAnimationFrame(tick);if(playing){if(last!==null&&!document.hidden)update(progress+Math.min((time-last)/1000,.1)/9);last=time;if(progress===2)setPlaying(false);}controls.update();renderer.render(scene,camera);}
window.relationalGrowth=Object.freeze({setProgress:v=>{setPlaying(false);update(v);},snapshot:()=>JSON.parse(JSON.stringify(state))});update(0);requestAnimationFrame(tick);
})();
