import * as T from 'three';
import {TrackballControls} from 'three/addons/controls/TrackballControls.js';
import {buildCellulationGeometry} from '../../research/realization-tower/cellulation-geometry.mjs';

// Same native carrier and bundled Three.js/TrackballControls as the normal-ray viewer.
// A small geometry-only entry point leaves its particle/process UI out entirely.
const host=document.querySelector('#viewport'),error=document.querySelector('#error');
const lifetime=new AbortController();
const listen=(target,event,fn)=>target.addEventListener(event,fn,{signal:lifetime.signal});
let renderer,controls,observer,group,frame=0,disposed=false;
function disposeGroup(){if(!group)return;group.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});group.removeFromParent();}
function dispose(){if(disposed)return;disposed=true;cancelAnimationFrame(frame);observer?.disconnect();controls?.dispose();disposeGroup();renderer?.dispose();lifetime.abort();}
try{
 const model=buildCellulationGeometry(),scene=new T.Scene();scene.background=new T.Color(0x0b1020);
 const bounds=new T.Box3().setFromPoints(model.cells.flatMap(c=>c.vertices.map(p=>new T.Vector3(...p)))),center=bounds.getCenter(new T.Vector3()),radius=bounds.getBoundingSphere(new T.Sphere()).radius;
 const camera=new T.OrthographicCamera(-radius,radius,radius,-radius,.01,radius*20);
 renderer=new T.WebGLRenderer({antialias:true});renderer.setPixelRatio(Math.min(devicePixelRatio,2));host.append(renderer.domElement);
 renderer.domElement.tabIndex=0;renderer.domElement.setAttribute('aria-label','Cellulation: drag to rotate, wheel to zoom, right-drag to pan; arrow keys rotate, plus and minus zoom');
 controls=new TrackballControls(camera,renderer.domElement);controls.staticMoving=true;controls.rotateSpeed=3;controls.target.copy(center);
 const inputs=Object.fromEntries(['tetrahedra','octahedra','edges','opacity'].map(id=>[id,document.getElementById(id)]));
 let interacting=false;
 function render(){frame=0;if(disposed)return;controls.update();renderer.render(scene,camera);window.cellulationAudit.camera=camera.position.toArray();window.cellulationAudit.zoom=camera.zoom;if(interacting)request();}
 function request(){if(!frame&&!disposed)frame=requestAnimationFrame(render);}
 function reset(){camera.position.copy(center).add(new T.Vector3(1.3,.8,1.7).normalize().multiplyScalar(radius*4));camera.up.set(0,1,0);camera.zoom=1;camera.updateProjectionMatrix();controls.target.copy(center);camera.lookAt(center);request();}
 function rebuild(){
  disposeGroup();group=new T.Group();scene.add(group);
  const visible=new Set(model.cells.filter(c=>inputs[c.kind==='tetrahedron'?'tetrahedra':'octahedra'].checked).map(c=>c.id));
  const faces=model.faces.filter(f=>f.owners.some(id=>visible.has(id))),edges=model.edges.filter(e=>e.owners.some(id=>visible.has(id)));
  const geometry=new T.BufferGeometry().setFromPoints(faces.flatMap(f=>f.vertices.map(p=>new T.Vector3(...p))));
  group.add(new T.Mesh(geometry,new T.MeshBasicMaterial({color:0xb8cde7,side:T.DoubleSide,transparent:true,opacity:Number(inputs.opacity.value),depthWrite:false})));
  const lines=new T.LineSegments(new T.BufferGeometry().setFromPoints(edges.flatMap(e=>e.vertices.map(p=>new T.Vector3(...p)))),new T.LineBasicMaterial({color:0x8ba9d0,transparent:true,opacity:.65}));lines.visible=inputs.edges.checked;group.add(lines);
  window.cellulationAudit={source:'fibration-12x12',cells:model.cells.length,tetrahedra:119,octahedra:56,visibleCells:visible.size,uniqueFaces:faces.length,uniqueEdges:edges.length,labels:0,overlays:0,internalOctahedralDiagonals:0,opacity:Number(inputs.opacity.value),edgesVisible:lines.visible};request();
 }
 listen(controls,'change',request);
 listen(controls,'start',()=>{interacting=true;request();});
 listen(controls,'end',()=>{interacting=false;request();});
 for(const name of ['tetrahedra','octahedra'])listen(inputs[name],'change',rebuild);
 listen(inputs.opacity,'input',()=>{group.children[0].material.opacity=Number(inputs.opacity.value);window.cellulationAudit.opacity=Number(inputs.opacity.value);request();});
 listen(inputs.edges,'change',()=>{group.children[1].visible=inputs.edges.checked;window.cellulationAudit.edgesVisible=inputs.edges.checked;request();});
 listen(document.querySelector('#reset'),'click',reset);
 listen(renderer.domElement,'keydown',event=>{
  const angle=.12,offset=camera.position.clone().sub(controls.target);
  if(['ArrowLeft','ArrowRight'].includes(event.key))offset.applyAxisAngle(camera.up.clone().normalize(),event.key==='ArrowLeft'?angle:-angle);
  else if(['ArrowUp','ArrowDown'].includes(event.key)){const axis=new T.Vector3().crossVectors(camera.up,offset).normalize(),a=event.key==='ArrowUp'?angle:-angle;offset.applyAxisAngle(axis,a);camera.up.applyAxisAngle(axis,a);}
  else if(['+','=','-'].includes(event.key)){camera.zoom=Math.max(.1,Math.min(20,camera.zoom*(event.key==='-'?.9:1.1)));camera.updateProjectionMatrix();}
  else return;
  event.preventDefault();camera.position.copy(controls.target).add(offset);camera.lookAt(controls.target);request();
 });
 observer=new ResizeObserver(()=>{const {width,height}=host.getBoundingClientRect();if(!width||!height)return;const aspect=width/height,half=radius*1.12;camera.left=-half*Math.max(1,aspect);camera.right=-camera.left;camera.top=half*Math.max(1,1/aspect);camera.bottom=-camera.top;camera.updateProjectionMatrix();renderer.setSize(width,height);controls.handleResize();request();});observer.observe(host);
 listen(renderer.domElement,'webglcontextlost',event=>{event.preventDefault();error.textContent='Graphics context lost. Reload to restore the view.';dispose();});
 listen(window,'pagehide',event=>{if(!event.persisted)dispose();});
 rebuild();reset();error.textContent='';
}catch(cause){dispose();error.textContent=`Unable to open the 3D cellulation: ${cause.message}`;console.error(cause);}
