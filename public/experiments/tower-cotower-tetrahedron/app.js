import * as THREE from "three"
import { OrbitControls } from "three/addons/controls/OrbitControls.js"
import { CSS2DRenderer, CSS2DObject } from "three/addons/renderers/CSS2DRenderer.js"

const host=document.querySelector('#scene'),detail=document.querySelector('#detail')
const model=await fetch('./model.json',{cache:'no-cache'}).then(r=>{if(!r.ok)throw new Error(`model ${r.status}`);return r.json()})
const scene=new THREE.Scene(),camera=new THREE.PerspectiveCamera(42,1,.1,100)
camera.position.set(8,6,9)
const renderer=new THREE.WebGLRenderer({antialias:true,alpha:true});renderer.setPixelRatio(Math.min(devicePixelRatio,2));host.append(renderer.domElement)
const labels=new CSS2DRenderer();labels.domElement.style.position='absolute';labels.domElement.style.inset='0';labels.domElement.style.pointerEvents='none';host.append(labels.domElement)
const controls=new OrbitControls(camera,renderer.domElement);controls.enableDamping=true;controls.target.set(0,.1,0)
scene.add(new THREE.HemisphereLight(0xbde8ff,0x14202a,2.2));const light=new THREE.DirectionalLight(0xffffff,2.6);light.position.set(5,8,6);scene.add(light)
const root=new THREE.Group();scene.add(root);const clickable=[];const positions=new Map(model.vertices.map(v=>[v.id,new THREE.Vector3(...v.position)]))
const colors={tower:0x63b3ff,cotower:0xf3b35d,mate:0xb68cff,face:0x77d9a8,vertex:0xe9f0f3}
function label(text,pos,required=false){const el=document.createElement('div');el.className=`label${required?' required':''}`;el.textContent=text;const o=new CSS2DObject(el);o.position.copy(pos);root.add(o);return o}
function select(data){detail.innerHTML=`<strong>${data.id} · ${data.label}</strong>${data.detail??''}${data.rungs?`<hr>${data.rungs.join('<br>')}`:''}`}
function cylinder(a,b,color,r=.035){const d=new THREE.Vector3().subVectors(b,a),m=new THREE.Vector3().addVectors(a,b).multiplyScalar(.5);const g=new THREE.CylinderGeometry(r,r,d.length(),12),x=new THREE.Mesh(g,new THREE.MeshStandardMaterial({color,roughness:.5,metalness:.1}));x.position.copy(m);x.quaternion.setFromUnitVectors(new THREE.Vector3(0,1,0),d.clone().normalize());root.add(x);return x}
for(const v of model.vertices){const p=positions.get(v.id),mesh=new THREE.Mesh(new THREE.SphereGeometry(.16,24,16),new THREE.MeshStandardMaterial({color:colors.vertex,emissive:0x172a33}));mesh.position.copy(p);mesh.userData=v;root.add(mesh);clickable.push(mesh);label(`${v.id} · ${v.label}`,p.clone().add(new THREE.Vector3(0,.34,0)),v.status==='partial')}
const pair={E12:['V1','V2'],E43:['V4','V3'],E13:['V1','V3'],E24:['V2','V4'],E14:['V1','V4'],E23:['V2','V3']}
for(const e of model.edges){const [aId,bId]=pair[e.id],a=positions.get(aId),b=positions.get(bId),line=cylinder(a,b,colors[e.kind],e.kind==='mate'?.025:.055);line.userData=e;clickable.push(line);const mid=a.clone().lerp(b,.5);label(`${e.id} · ${e.label}`,mid.clone().add(new THREE.Vector3(0,.15,0)),e.kind==='mate'&&e.id.startsWith('E2'))
 if(e.rungs)e.rungs.forEach((r,i)=>{const p=a.clone().lerp(b,i/(e.rungs.length-1));const bead=new THREE.Mesh(new THREE.SphereGeometry(.09,16,12),new THREE.MeshStandardMaterial({color:colors[e.kind]}));bead.position.copy(p);bead.userData={...e,label:r};root.add(bead);clickable.push(bead)})}
const faceGroup=new THREE.Group();root.add(faceGroup)
for(const f of model.faces){const pts=f.vertices.map(x=>positions.get(x)),g=new THREE.BufferGeometry().setFromPoints(pts);g.setIndex([0,1,2]);g.computeVertexNormals();const mesh=new THREE.Mesh(g,new THREE.MeshStandardMaterial({color:colors.face,transparent:true,opacity:.09,side:THREE.DoubleSide,depthWrite:false}));mesh.userData=f;faceGroup.add(mesh);clickable.push(mesh);label(`${f.id} · ${f.label}`,pts[0].clone().add(pts[1]).add(pts[2]).multiplyScalar(1/3),true)}
label(`${model.cell3.id} · ${model.cell3.label}`,new THREE.Vector3(0,-.15,0),true)
const ray=new THREE.Raycaster(),pointer=new THREE.Vector2();renderer.domElement.addEventListener('pointerdown',ev=>{const r=renderer.domElement.getBoundingClientRect();pointer.set((ev.clientX-r.left)/r.width*2-1,-(ev.clientY-r.top)/r.height*2+1);ray.setFromCamera(pointer,camera);const hit=ray.intersectObjects(clickable,false)[0];if(hit)select(hit.object.userData)})
document.querySelector('#faces').onclick=()=>faceGroup.visible=!faceGroup.visible
document.querySelector('#reset').onclick=()=>{camera.position.set(8,6,9);controls.target.set(0,.1,0);controls.update()}
function resize(){const w=host.clientWidth,h=host.clientHeight;camera.aspect=w/h;camera.updateProjectionMatrix();renderer.setSize(w,h,false);labels.setSize(w,h)}new ResizeObserver(resize).observe(host);resize()
function frame(){controls.update();renderer.render(scene,camera);labels.render(scene,camera);requestAnimationFrame(frame)}frame()
