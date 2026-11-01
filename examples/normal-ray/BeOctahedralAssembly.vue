<script setup>
import {ref,watch,onMounted,onUnmounted} from 'vue';
import * as T from 'three';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';
import {buildBeryllium8Assembly} from '../../research/realization-tower/beryllium-8-assembly.mjs';
const props=defineProps({columns:{type:Array,required:true},reference:{type:Object,required:true},label:{type:String,required:true},highlightId:{type:String,default:null}});
const host=ref(null),error=ref(''),assemblyAudit=ref(null);
let renderer,scene,camera,controls,group,observer;
const lifetime=new AbortController();
function disposeGroup(){
 if(!group)return;
 const geometries=new Set(),materials=new Set();
 group.traverse(o=>{if(o.geometry)geometries.add(o.geometry);if(o.material)for(const m of Array.isArray(o.material)?o.material:[o.material])materials.add(m);});
 geometries.forEach(g=>g.dispose());materials.forEach(m=>m.dispose());scene.remove(group);group=null;
}
function render(){if(renderer&&scene&&camera){renderer.render(scene,camera);if(host.value){host.value.dataset.camera=JSON.stringify(camera.position.toArray());host.value.dataset.target=JSON.stringify(controls.target.toArray());}}}
function highlight(){
 if(host.value)host.value.dataset.highlight=props.highlightId??'';
 group?.traverse(o=>{
  if(!o.userData.strandId||!o.material)return;
  o.visible=true;
  const active=!props.highlightId||o.userData.strandId===props.highlightId;
  for(const material of Array.isArray(o.material)?o.material:[o.material]){
   const transparent=!active;
   if(material.transparent!==transparent){material.transparent=transparent;material.needsUpdate=true;}
   material.opacity=active?1:.2;material.depthWrite=active;
  }
 });
 if(host.value){const visible=new Set(),opacities={};group?.traverse(o=>{if(o.visible&&o.userData.strandId){visible.add(o.userData.strandId);opacities[o.userData.strandId]=(Array.isArray(o.material)?o.material[0]:o.material).opacity;}});host.value.dataset.visibleStrands=JSON.stringify([...visible]);host.value.dataset.strandOpacities=JSON.stringify(opacities);}
 render();
}
function rebuild(){
 if(!renderer)return;
 const model=buildBeryllium8Assembly(props.columns,props.reference);assemblyAudit.value=model.audit;disposeGroup();group=new T.Group();scene.add(group);
 const frame=new T.LineSegments(new T.BufferGeometry().setFromPoints(model.edges.filter(e=>!e.sleeveLink).flatMap(e=>e.guide.map(p=>new T.Vector3(...p)))),new T.LineBasicMaterial({color:0x687589,transparent:true,opacity:.3}));group.add(frame);
 const up=new T.Vector3(0,1,0);
 for(const s of model.strands){
  const curve=new T.CurvePath();for(let i=1;i<s.points.length;i++)curve.add(new T.LineCurve3(new T.Vector3(...s.points[i-1]),new T.Vector3(...s.points[i])));
  const segments=96,radial=6,geometry=new T.TubeGeometry(curve,segments,.012,radial,false);
  const materials=s.colours.map(color=>new T.MeshBasicMaterial({color}));
  if(materials.length>1){geometry.clearGroups();for(let i=0;i<segments;i+=4)geometry.addGroup(i*radial*6,4*radial*6,(i/4)%materials.length);}
  const mesh=new T.Mesh(geometry,materials.length===1?materials[0]:materials);mesh.userData.strandId=s.id;group.add(mesh);
  const arrowMaterial=s.arrows.length?new T.MeshBasicMaterial({color:0xffffff}):null;
  for(const a of s.arrows){
   const arrow=new T.Mesh(new T.ConeGeometry(.024,.09,8),arrowMaterial);arrow.position.fromArray(a.point);arrow.quaternion.setFromUnitVectors(up,new T.Vector3(...a.direction));arrow.userData.strandId=s.id;group.add(arrow);
  }
 }
 if(model.sleeve){
  const shell=new T.Mesh(new T.SphereGeometry(model.sleeve.radius,24,16),new T.MeshBasicMaterial({color:0xffffff,transparent:true,opacity:.18,depthWrite:false,side:T.DoubleSide}));
  shell.position.fromArray(model.sleeve.point);shell.userData.centralSleeve=model.sleeve.id;group.add(shell);
 }
 const start=new T.Mesh(new T.SphereGeometry(.04,12,8),new T.MeshBasicMaterial({color:0xffd36b}));start.position.fromArray(model.inputPole);group.add(start);
 host.value.dataset.audit=JSON.stringify({...model.audit,ids:model.strands.map(s=>s.id),colours:model.strands.map(s=>s.colours)});
 highlight();
}
function reset(){if(!camera)return;camera.position.set(3.2,2.1,3.6);controls.target.set(0,0,0);controls.update();render();}
function resize(){
 if(!renderer||!host.value)return;
 const {width,height}=host.value.getBoundingClientRect();if(!width||!height)return;
 renderer.setSize(width,height,false);camera.aspect=width/height;camera.updateProjectionMatrix();render();
}
onMounted(()=>{
 try{
  scene=new T.Scene();scene.background=new T.Color(0x0b1020);camera=new T.PerspectiveCamera(34,1,.1,30);
  renderer=new T.WebGLRenderer({antialias:true,alpha:false});renderer.setPixelRatio(Math.min(globalThis.devicePixelRatio||1,2));
  const canvas=renderer.domElement;canvas.setAttribute('role','img');canvas.setAttribute('aria-label',props.label);canvas.tabIndex=0;host.value.append(canvas);
  controls=new OrbitControls(camera,canvas);controls.enablePan=true;controls.enableZoom=true;controls.minDistance=.5;controls.maxDistance=20;controls.addEventListener('change',render);
  canvas.addEventListener('keydown',event=>{
   if(!['ArrowLeft','ArrowRight','ArrowUp','ArrowDown','Home'].includes(event.key))return;event.preventDefault();
   if(event.key==='Home'){reset();return;}
   const s=new T.Spherical().setFromVector3(camera.position.clone().sub(controls.target));
   if(event.key==='ArrowLeft')s.theta-=.15;if(event.key==='ArrowRight')s.theta+=.15;
   if(event.key==='ArrowUp')s.phi-=.15;if(event.key==='ArrowDown')s.phi+=.15;s.makeSafe();
   camera.position.copy(controls.target).add(new T.Vector3().setFromSpherical(s));controls.update();render();
  },{signal:lifetime.signal});
  reset();rebuild();observer=new ResizeObserver(resize);observer.observe(host.value);resize();
 }catch(e){error.value='3D assembly unavailable: '+e.message;}
});
watch(()=>[props.columns,props.reference],rebuild);
watch(()=>props.highlightId,highlight);
watch(()=>props.label,label=>renderer?.domElement.setAttribute('aria-label',label));
onUnmounted(()=>{lifetime.abort();observer?.disconnect();controls?.dispose();disposeGroup();renderer?.dispose();renderer?.forceContextLoss();renderer=null;});
</script>
<template>
 <figure class="octahedral-assembly">
  <div ref="host" class="assembly-canvas" :aria-label="label"><p v-if="error" role="status">{{error}}</p></div>
  <figcaption>{{assemblyAudit?.strands??8}} strands · {{assemblyAudit?.edges??12}} traced edges<span v-if="assemblyAudit?.centralSleeves"> · central sleeve: 4 strands / 2 pairs</span> <button type="button" :aria-label="'Reset '+label" @click="reset">Reset</button></figcaption>
 </figure>
</template>
<style scoped>
.octahedral-assembly{margin:8px 0 0;min-width:0;}.assembly-canvas{height:210px;position:relative;background:#0b1020;border-radius:4px;overflow:hidden;}.assembly-canvas :deep(canvas){display:block;width:100%;height:100%;touch-action:none;}.assembly-canvas p{padding:10px;font-size:11px;}figcaption{font-size:10px;line-height:1.4;margin-top:5px;}button{font:inherit;min-height:24px;padding:2px 6px;}@media(max-width:760px){.assembly-canvas{height:240px;}}
</style>
