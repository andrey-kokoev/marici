import {lattice,worldPoint} from '../strominger/demos/particle-overlap-tetrahedron/simplex-model.mjs';
import {makeAtom} from '../strominger/demos/particle-overlap-tetrahedron/atom-model.mjs';
import {createWindowConstruction} from '../strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {itemKey} from '../strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {corners,cornerPlacement} from './corner-placements.mjs';
try {
const THREE=globalThis.THREE,scene=new THREE.Scene();scene.background=new THREE.Color(0x101923);
const renderer=new THREE.WebGLRenderer({antialias:true});renderer.setPixelRatio(Math.min(devicePixelRatio,2));document.querySelector('#scene').append(renderer.domElement);
const camera=new THREE.PerspectiveCamera(43,1,.01,200),controls=new THREE.OrbitControls(camera,renderer.domElement);controls.enableDamping=true;
const keys=lattice.cells.map(c=>itemKey(c.map(i=>lattice.nodes[i].address))),keySet=new Set(keys);
const model=createWindowConstruction();model.step();const triple=model.step();if(triple.status!=='complete')throw Error('Native triple failed');
const root=keys.indexOf(triple.items[0].key),pair=makeAtom('hydrogen',root);
const pairBodies=pair.bodies.map(b=>({species:b.species,vertices:lattice.cells[b.cellId].map(i=>lattice.nodes[i].address)}));
const pairPlacement=cornerPlacement(pairBodies,corners[0]);
const placement=cornerPlacement(triple.items,corners[1]);
if(!pairPlacement||!placement)throw Error('Complete shapes cannot be placed at selected envelope corners');
const structures=[pairPlacement.bodies,placement.bodies],colors={proton:0x46b6e0,neutron:0xedb65d,electron:0xed80c2};
const edgeIndices=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]],faceIndices=[0,2,1,0,1,3,0,3,2,1,2,3];
const vector=p=>new THREE.Vector3(...worldPoint(p));
function lines(points,color,opacity=1){return new THREE.LineSegments(new THREE.BufferGeometry().setFromPoints(points),new THREE.LineBasicMaterial({color,transparent:true,opacity,depthWrite:false}));}
const grid=lines(lattice.edges.flatMap(([a,b])=>[new THREE.Vector3(...lattice.nodes[a].point),new THREE.Vector3(...lattice.nodes[b].point)]),0x9db3c9,.17);scene.add(grid);
const bodiesGroup=new THREE.Group(),interfaces=new THREE.Group(),sectors=new THREE.Group();scene.add(bodiesGroup,interfaces,sectors);
scene.add(lines(edgeIndices.flatMap(([i,j])=>[vector(corners[i]),vector(corners[j])]),0xb6d0e4,.65));
for(const placed of [pairPlacement,placement]){
 const marker=new THREE.Mesh(new THREE.SphereGeometry(.045,12,8),new THREE.MeshBasicMaterial({color:0xffffff}));
 marker.position.copy(vector(placed.corner));bodiesGroup.add(marker);
}
const allSectorLines=[];
for(const cell of lattice.cells){
 const v=cell.map(i=>new THREE.Vector3(...lattice.nodes[i].point)),c=v.reduce((s,p)=>s.add(p),new THREE.Vector3()).multiplyScalar(.25);
 for(let i=0;i<4;i++)for(let j=0;j<4;j++)if(i!==j){
  const a=v[i].clone().lerp(c,.2),b=v[j].clone().lerp(c,.2),d=b.clone().sub(a),side=new THREE.Vector3().crossVectors(d,c.clone().sub(a)).normalize(),offset=side.clone().multiplyScalar(.012);
  a.add(offset);b.add(offset);const back=b.clone().addScaledVector(d,-.12);
  allSectorLines.push(a,b,b,back.clone().addScaledVector(side,.018),b,back.clone().addScaledVector(side,-.018));
 }
}
const latticeSectors=lines(allSectorLines,0x91aac1,.12);sectors.add(latticeSectors);
function label(text,at,color='#ffffff'){
 const canvas=document.createElement('canvas');canvas.width=text.length===1?96:512;canvas.height=96;const ctx=canvas.getContext('2d');ctx.fillStyle='#101923bb';ctx.fillRect(0,0,canvas.width,96);ctx.fillStyle=color;ctx.textAlign='center';ctx.font='bold 42px sans-serif';ctx.fillText(text,canvas.width/2,63);
 const texture=new THREE.CanvasTexture(canvas),sprite=new THREE.Sprite(new THREE.SpriteMaterial({map:texture,depthTest:false,transparent:true}));sprite.position.copy(at);sprite.scale.set(text.length===1?.23:1.5,text.length===1?.23:.28,1);bodiesGroup.add(sprite);
}
let sectorCount=0;const sharedCounts=[];
for(const [index,bodies] of structures.entries()){
 for(const b of bodies){
 const v=b.vertices.map(vector),positions=faceIndices.flatMap(i=>v[i].toArray());
 const geom=new THREE.BufferGeometry().setAttribute('position',new THREE.Float32BufferAttribute(positions,3));geom.computeVertexNormals();
 bodiesGroup.add(new THREE.Mesh(geom,new THREE.MeshBasicMaterial({color:colors[b.species],side:THREE.DoubleSide,transparent:true,opacity:.48,depthWrite:false})));
 bodiesGroup.add(lines(edgeIndices.flatMap(([a,c])=>[v[a],v[c]]),colors[b.species]));
 const center=v.reduce((s,p)=>s.add(p),new THREE.Vector3()).multiplyScalar(.25);
 label(({proton:'P',electron:'E',neutron:'N'})[b.species],center);
 // All twelve ordered sectors, slightly inset and separated from the reverse
 // sector toward each face-independent carrier centroid. No absent sector.
 for(let i=0;i<4;i++)for(let j=0;j<4;j++)if(i!==j){
 const start=v[i].clone().lerp(center,.20),end=v[j].clone().lerp(center,.20),direction=end.clone().sub(start).normalize();
 const offset=new THREE.Vector3().crossVectors(direction,center.clone().sub(start)).normalize().multiplyScalar(.016);
 start.add(offset);end.add(offset);const length=start.distanceTo(end);
 sectors.add(new THREE.ArrowHelper(direction,start,length,colors[b.species],length*.13,length*.055));sectorCount++;
 }
 }
 for(let i=0;i<bodies.length;i++)for(let j=i+1;j<bodies.length;j++){
 const shared=bodies[i].vertices.filter(p=>bodies[j].vertices.some(q=>itemKey([p])===itemKey([q])));sharedCounts.push(shared.length);
 if(shared.length===3){const geom=new THREE.BufferGeometry().setFromPoints(shared.map(vector));interfaces.add(new THREE.Mesh(geom,new THREE.MeshBasicMaterial({color:0xa3ffbc,side:THREE.DoubleSide,transparent:true,opacity:.6,depthWrite:false})));}
 if(shared.length===2)interfaces.add(lines(shared.map(vector),0xffffff));
 }
 const center=bodies.flatMap(b=>b.vertices).map(vector).reduce((s,p)=>s.add(p),new THREE.Vector3()).multiplyScalar(1/(4*bodies.length));center.y+=.85;
 label(index?'P–N–E triple':'P–E pair',center);
}
if(sectorCount!==60||sharedCounts.join(',')!=='3,3,2,3')throw Error('Sector or interface audit failed');
function fit(object){const box=new THREE.Box3().setFromObject(object),center=box.getCenter(new THREE.Vector3()),size=box.getSize(new THREE.Vector3()),r=Math.max(size.x,size.y,size.z);controls.target.copy(center);camera.position.copy(center).add(new THREE.Vector3(1,.7,1.25).multiplyScalar(r));controls.update();}
document.querySelector('#fit').onclick=()=>fit(grid);document.querySelector('#focus').onclick=()=>fit(bodiesGroup);
document.querySelector('#grid').onchange=e=>grid.visible=e.target.checked;document.querySelector('#opacity').oninput=e=>grid.material.opacity=Number(e.target.value);document.querySelector('#sectors').onchange=e=>sectors.visible=e.target.checked;document.querySelector('#faces').onchange=e=>interfaces.visible=e.target.checked;
document.querySelector('#summary').textContent=`${lattice.cells.length} native primitive cells · ${lattice.nodes.length} shared vertices · 5 highlighted carriers · 12 directed sectors each. Each proton occupies a corner tetrahedron at a different outer vertex; its attached cells extend inward.`;
function resize(){const width=document.querySelector('#scene').clientWidth;renderer.setSize(width,innerHeight);camera.aspect=width/innerHeight;camera.updateProjectionMatrix();}addEventListener('resize',resize);resize();fit(grid);
globalThis.latticePairAudit={cells:lattice.cells.length,vertices:lattice.nodes.length,sectorCount,fullLatticeSectors:lattice.cells.length*12,sharedCounts,cornerAnchors:[pairPlacement.corner,placement.corner],placementTransforms:[pairPlacement.transform,placement.transform],allBodiesInNativeLattice:true};
function animate(){requestAnimationFrame(animate);controls.update();renderer.render(scene,camera);}animate();
}catch(error){document.querySelector('#error').textContent=error.stack;console.error(error);}
