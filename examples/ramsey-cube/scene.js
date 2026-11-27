import * as T from 'three'
import {OrbitControls} from 'three/addons/controls/OrbitControls.js'
import {gradedSolid} from './cellulation.mjs'
import {site,world,route,frame} from './fcc.mjs'
import {vertices,anchors,redEdges,relation} from './model.mjs'

export function createScene(host,onPick){
  const renderer=new T.WebGLRenderer({antialias:true,alpha:true});host.append(renderer.domElement);renderer.setPixelRatio(Math.min(devicePixelRatio,2))
  const scene=new T.Scene(),camera=new T.PerspectiveCamera(38,1,.1,50),controls=new OrbitControls(camera,renderer.domElement)
  controls.minDistance=3;controls.maxDistance=15;controls.enablePan=false
  const solids=new T.Scene();let active=scene
  const draw=()=>renderer.render(active,camera),reset=()=>{camera.position.set(3.8,2.9,5.6);controls.target.set(0,0,0);controls.update();draw()};controls.addEventListener('change',draw)
  const nodes=vertices.map(v=>{const canvas=document.createElement('canvas');canvas.width=canvas.height=96;const ctx=canvas.getContext('2d');ctx.fillStyle='white';ctx.beginPath();if(v===anchors[0]){ctx.moveTo(48,0);ctx.lineTo(96,48);ctx.lineTo(48,96);ctx.lineTo(0,48);ctx.closePath()}else ctx.arc(48,48,42,0,2*Math.PI);ctx.fill();ctx.fillStyle='#111';ctx.font='bold 44px sans-serif';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(v,48,50);const map=new T.CanvasTexture(canvas);map.colorSpace=T.SRGBColorSpace;const s=new T.Sprite(new T.SpriteMaterial({map}));s.position.set(...world(site(v)));s.userData.id=v;s.scale.setScalar(.34);scene.add(s);return s})
  const vec=p=>new T.Vector3(...world(p));const cage=new T.LineSegments(new T.BufferGeometry().setFromPoints(frame.flat().map(vec)),new T.LineBasicMaterial({color:0x739ab3}));scene.add(cage)
  const points=(ps,color,size)=>new T.Points(new T.BufferGeometry().setFromPoints(ps.map(vec)),new T.PointsMaterial({color,size}));const joints=points(frame.flat(),0xb5cddd,.055);scene.add(joints)
  const paths=redEdges.map(([a,b])=>route(a,b));const steps=paths.map(path=>points(path.slice(1,-1),0xffa27f,.045));scene.add(...steps)
  const links=redEdges.map(([a,b],i)=>{const g=new T.BufferGeometry().setFromPoints(paths[i].map(vec));const l=new T.Line(g,new T.LineBasicMaterial({transparent:true}));scene.add(l);return l})
  const wires=(color,opacity)=>new T.LineSegments(new T.BufferGeometry(),new T.LineBasicMaterial({color,opacity,transparent:true,depthWrite:false}));const lattice=wires(0x71d7cf,.39),outline=wires(0xffdb89,1);solids.add(lattice,outline);let lastShape=''
  function update(a,b,all,layer,shape='cube',grade=1){
    const solid=shape==='cube'?null:gradedSolid(shape,grade);active=solid?solids:scene
    if(solid){if(lastShape!==shape+grade){const center=new T.Box3().setFromPoints(solid.bars.flat().map(vec)).getCenter(new T.Vector3());const radius=Math.max(...solid.bars.flat().map(p=>vec(p).distanceTo(center)));for(const [object,segments] of [[lattice,solid.edges],[outline,solid.bars]]){object.geometry.dispose();object.geometry=new T.BufferGeometry().setFromPoints(segments.flat().map(p=>vec(p).sub(center).multiplyScalar(1.85/radius)))}}lastShape=shape+grade;draw();return}
    const coral='#ff967f',blue='#73cbff',gold='#ffd264';
    nodes.forEach((n,i)=>{const w=i+1;const anchor=anchors.includes(w),x=anchor&&relation(w,a)==='R',y=anchor&&relation(w,b)==='R';n.material.color.set(x&&y?gold:w===a||x?coral:w===b||y?blue:'#c3cbd0');n.scale.setScalar(w===a||w===b?.32:.21)})
    links.forEach((l,i)=>{const [u,v]=redEdges[i],touch=r=>(u===r&&anchors.includes(v))||(v===r&&anchors.includes(u));const x=touch(a)&&layer!=='B',y=touch(b)&&layer!=='A',color=x&&y?gold:x?coral:y?blue:'#acc6d7';steps[i].visible=x||y;steps[i].material.color.set(color);l.visible=all||x||y;l.material.color.set(color);l.material.opacity=x||y?1:.16});draw()
  }
  const ro=new ResizeObserver(()=>{const w=host.clientWidth,h=host.clientHeight;if(!w||!h)return;renderer.setSize(w,h);camera.aspect=w/h;camera.updateProjectionMatrix();draw()});ro.observe(host);reset()
  let start;const down=e=>{start=[e.clientX,e.clientY]},up=e=>{if(active!==scene||!start||Math.hypot(start[0]-e.clientX,start[1]-e.clientY)>5)return;const b=renderer.domElement.getBoundingClientRect(),r=new T.Raycaster();r.setFromCamera({x:2*(e.clientX-b.left)/b.width-1,y:1-2*(e.clientY-b.top)/b.height},camera);const hit=r.intersectObjects(nodes)[0];if(hit)onPick(hit.object.userData.id)};host.addEventListener('pointerdown',down);host.addEventListener('pointerup',up)
  return {update,reset,dispose(){ro.disconnect();host.removeEventListener('pointerdown',down);host.removeEventListener('pointerup',up);controls.dispose();for(const o of [...nodes,...links,...steps,cage,joints,lattice,outline]){if(!o.isSprite)o.geometry.dispose();o.material.map?.dispose();o.material.dispose()}renderer.dispose();renderer.domElement.remove()}}
}
