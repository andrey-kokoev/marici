import {lattice,items,connections,traversal,transport,pathBetween,adjacency,witnessPairs,reserved,available,loadout,itemByCell} from './fiber-space-model.mjs';
import {faces,edges,worldPoint} from './simplex-model.mjs';
import {lead208Bodies,lead208Construction} from './lead208-model.mjs';
import {makeAtom} from './atom-model.mjs';
import {createDeuteriumTunnel} from './deuterium-tunnel-model.mjs';
import {auditWindowCoverage} from './fiber-coverage-model.mjs';
import {createAssemblyDisplay} from './assembly-display-model.mjs';
import {itemKey} from './lattice-items.mjs';
import {createPhaseAssembly} from './phase-assembly-model.mjs';
import {createLocalReferenceDisplay,localReferenceIds} from './local-reference-display.mjs';
import {createEdgeSegments} from './edge-segments.mjs';
try {
 const THREE=globalThis.THREE,$=id=>document.getElementById(id),host=$('scene'),vec=p=>new THREE.Vector3(...p);
 const renderer=new THREE.WebGLRenderer({antialias:true,alpha:true});renderer.setPixelRatio(Math.min(devicePixelRatio,2));host.prepend(renderer.domElement);
 renderer.domElement.setAttribute('role','img');renderer.domElement.setAttribute('aria-label','Solid lattice cells with loadout and scoped identity transport');
 const scene=new THREE.Scene(),camera=new THREE.OrthographicCamera(-6,6,5,-5,.02,150),orbit=new THREE.OrbitControls(camera,renderer.domElement);orbit.enableDamping=true;
 const primaryGroup=new THREE.Group(),secondaryGroup=new THREE.Group();scene.add(primaryGroup,secondaryGroup);secondaryGroup.visible=false;
 const rotationFrames=[primaryGroup,secondaryGroup].map(group=>({group,center:new THREE.Vector3(),anchor:new THREE.Vector3()}));
 const localRotation=()=>!!comparison&&$('rotate-shapes').checked;
 function applyShapeRotation(){for(const {group,center,anchor} of rotationFrames)group.position.copy(anchor).sub(center.clone().applyQuaternion(group.quaternion));}
 function updateRotationMode(){orbit.enableRotate=!localRotation();$('rotate-shapes').disabled=!comparison;}
 $('rotate-shapes').addEventListener('change',()=>{orbit.enableDamping=false;orbit.update();orbit.enableDamping=true;updateRotationMode();});
 const colors={base:0x344653,proton:0x50cfff,neutron:0xffcf72,electron:0xff7edb,witness:0xad78db};
 const mats=Object.fromEntries(Object.entries(colors).map(([k,color])=>[k,new THREE.MeshLambertMaterial({color,side:THREE.DoubleSide,flatShading:true,polygonOffset:true,polygonOffsetFactor:1,polygonOffsetUnits:1})]));
 function updateFaceTransparency(){
  const percent=Number($('face-transparency').value),opacity=1-percent/100;
  for(const material of Object.values(mats)){
   const transparent=opacity<1;if(material.transparent!==transparent)material.needsUpdate=true;
   material.opacity=opacity;material.transparent=transparent;material.depthWrite=!transparent;
  }
  $('face-transparency-value').textContent=percent+'%';
 }
 $('face-transparency').addEventListener('input',updateFaceTransparency);updateFaceTransparency();
 scene.add(new THREE.AmbientLight(0xffffff,.8));const light=new THREE.DirectionalLight(0xffffff,.8);light.position.set(5,8,7);scene.add(light);
 // Exactly one solid mesh per existing primitive. Channels only change its material.
 const cellMeshes=lattice.cells.map((cell,id)=>{const g=new THREE.BufferGeometry().setFromPoints(cell.map(n=>vec(lattice.nodes[n].point)));g.setIndex(faces.flat());g.computeVertexNormals();const m=new THREE.Mesh(g,mats.base);m.visible=false;m.userData.cell=id;m.userData.coordinateKey=itemKey(cell.map(n=>lattice.nodes[n].address));primaryGroup.add(m);return m;});
 const leadMeshes=new Map(),addedMeshes=[];
 for(const body of lead208Bodies){
  const meshes=body.shape.itemIndex!==undefined?items[body.shape.itemIndex].children.map(id=>cellMeshes[id]):body.components.map(c=>{const g=new THREE.BufferGeometry().setFromPoints(c.map(p=>vec(worldPoint(p))));g.setIndex(faces.flat());g.computeVertexNormals();const m=new THREE.Mesh(g,mats[body.species]);m.visible=false;m.userData.coordinateKey=itemKey(c);primaryGroup.add(m);addedMeshes.push(m);return m;});
  meshes.forEach(m=>m.userData.leadBody=body.id);leadMeshes.set(body.id,meshes);
 }
 const coverageCells=cellMeshes.map(m=>m.userData.coordinateKey);
 const allMeshes=[...cellMeshes,...addedMeshes],meshByCell=new Map(allMeshes.map(m=>[m.userData.coordinateKey,m]));
 function sequentialMesh(c){
  const key=itemKey(c);if(meshByCell.has(key))return meshByCell.get(key);
  const g=new THREE.BufferGeometry().setFromPoints(c.map(p=>vec(worldPoint(p))));g.setIndex(faces.flat());g.computeVertexNormals();
  const m=new THREE.Mesh(g,mats.base);m.userData.coordinateKey=key;primaryGroup.add(m);allMeshes.push(m);meshByCell.set(key,m);return m;
 }
 const edgeStrokes=[];
 function lines(color=0x000000,opacity=1,dashed=false,group=primaryGroup){const l=createEdgeSegments(THREE,{color,width:2,dashed});edgeStrokes.push(l);group.add(l);return l;}
 function setPairs(mesh,pairs){mesh.setPairs(pairs);}
 const electronEdges=lines(0x000000,1,true),selectedElectronEdges=lines(0x000000,1,true);
 const contextEdges=lines(),bodyEdges=lines(),dual=lines(),fiber=lines(),pointerOutline=lines();
 pointerOutline.material.depthTest=true;
 const secondaryEdges=lines(0,1,false,secondaryGroup),secondaryElectronEdges=lines(0,1,true,secondaryGroup),secondaryPointer=lines(0,1,false,secondaryGroup),secondarySelectedElectron=lines(0,1,true,secondaryGroup),secondaryMeshes=new Map();
 secondaryPointer.material.depthTest=true;
 const labels=[];function clearLabels(){labels.forEach(l=>l.el.remove());labels.length=0;}
 function label(text,p,color='#dcebf1',group=primaryGroup,vertexLabel=true){const el=document.createElement('span');el.className='realization-label '+(vertexLabel?'node':'carrier');el.textContent=text;el.style.color=color;el.style.whiteSpace='pre';el.hidden=vertexLabel&&!$('show-vertex-labels').checked;el.dataset.slot=group===primaryGroup?'primary':'secondary';host.append(el);labels.push({el,p,group,vertexLabel});}
 function phaseLabels(state,group){
  if(state.displayVertexLabels?.length)for(const entry of state.displayVertexLabels){label(entry.text,worldPoint(entry.point),undefined,group);const el=labels.at(-1).el;el.dataset.vertex=entry.vertex;el.dataset.itemIndices=[...new Set(entry.occurrences.map(o=>o.itemIndex))].join(',');}
  else for(const [name,p] of Object.entries(state.displayBindings))label(name,worldPoint(p),undefined,group);
 }
 let trialIsotope='deuterium';
 const makeDisplay=id=>localReferenceIds.includes(id)?createLocalReferenceDisplay(id):createAssemblyDisplay(()=>['deuterium','sequential'].includes(id)?createDeuteriumTunnel():createPhaseAssembly(id),{loop:true,initiallyAssembled:true});
 const newTunnel=()=>makeDisplay(trialIsotope);
 let layoutCount=1,layoutTotal=0,comparison=null,comparisonKind='none',comparisonStep=1;
 let sequential=newTunnel();
 function restartSequential(){sequential=newTunnel();atomKind='sequential';$('atom').value=trialIsotope==='deuterium'?atomKind:trialIsotope;resetComparison();refresh(true);reset();}
 function previousItem(){if(comparison){setComparisonStep(comparisonStep-1);return;}if(atomKind==='sequential'){const a=sequential.snapshot().assemblyDisplay;sequential.setShown((a.shown+a.total-2)%a.total+1);}else layoutCount=(layoutCount+primaryTotal()-2)%primaryTotal()+1;refresh(atomKind!=='sequential');}
 function nextItem(){
  if(comparison){setComparisonStep(comparisonStep+1);return;}
  if(atomKind!=='sequential'){layoutCount=layoutCount%primaryTotal()+1;refresh(true);return;}
  const a=sequential.snapshot().assemblyDisplay,result=sequential.setShown(a.shown%a.total+1);refresh();
  if(atomKind==='sequential'){
   camera.updateMatrixWorld();const extent=Math.max(...result.items.flatMap(s=>s.vertices.map(p=>{const q=vec(worldPoint(p)).project(camera);return Math.max(Math.abs(q.x),Math.abs(q.y));})));
   if(extent>.85){camera.zoom*=.85/extent;camera.updateProjectionMatrix();}
  }
  return result;
 }
 let step=0,perspective=0,frameCount=0,atomKind='sequential',atom=null,route=[-1,...traversal,-2],scope=new Set(items.map(i=>i.index)),occupiedCells=new Set(),visibleEdges=0,selectedChain=null,coverage=null;
 function untrackedMeshCount(){const known=new Set([...allMeshes,...secondaryMeshes.values()]);let count=0;scene.traverse(o=>{if(o.isMesh&&!known.has(o)&&!o.userData.edgeStroke)count++;});return count;}
 function primaryTotal(){return atomKind==='sequential'?sequential.snapshot().assemblyDisplay.total:atomKind==='lead208'?lead208Bodies.length:atomKind==='none'?1:makeAtom(atomKind).bodies.length;}
 function comparisonTotal(){return Math.max(primaryTotal(),comparison?.snapshot().assemblyDisplay.total??1);}
 function resetComparison(){for(const {group} of rotationFrames)group.quaternion.identity();comparison=comparisonKind==='none'?null:makeDisplay(comparisonKind);comparisonStep=comparisonTotal();if(atomKind==='sequential')sequential.setShown(primaryTotal());else layoutCount=primaryTotal();if(comparison)comparison.setShown(comparison.snapshot().assemblyDisplay.total);}
 function setComparisonStep(value){
  const total=comparisonTotal();comparisonStep=((value-1)%total+total)%total+1;
  if(atomKind==='sequential')sequential.setShown(Math.min(comparisonStep,primaryTotal()));else layoutCount=Math.min(comparisonStep,primaryTotal());
  comparison.setShown(Math.min(comparisonStep,comparison.snapshot().assemblyDisplay.total));refresh(atomKind!=='sequential');
 }
 function primaryFullPoints(){return atomKind==='sequential'?sequential.fullItems().flatMap(s=>s.vertices.map(worldPoint)):atomKind==='lead208'?lead208Bodies.flatMap(b=>b.points):atomKind==='none'?lattice.nodes.map(n=>n.point):Object.values(makeAtom(atomKind).points);}
 function secondaryFullPoints(){return comparison.fullItems().flatMap(s=>s.vertices.map(worldPoint));}
 function comparisonPoints(){scene.updateMatrixWorld(true);return [...primaryFullPoints().map(p=>primaryGroup.localToWorld(vec(p)).toArray()),...secondaryFullPoints().map(p=>secondaryGroup.localToWorld(vec(p)).toArray())];}
 function renderComparison(){
  for(const mesh of secondaryMeshes.values())mesh.visible=false;
  secondaryGroup.visible=!!comparison;$('comparison-readout').hidden=!comparison;
  updateRotationMode();
  if(!comparison){for(const {group} of rotationFrames){group.position.set(0,0,0);group.quaternion.identity();}return;}
  const a=new THREE.Box3().setFromPoints(primaryFullPoints().map(vec)),b=new THREE.Box3().setFromPoints(secondaryFullPoints().map(vec));
  const ca=a.getCenter(new THREE.Vector3()),cb=b.getCenter(new THREE.Vector3()),union=a.clone().union(b),center=union.getCenter(new THREE.Vector3()),gap=.5;
  primaryGroup.position.set(-gap/2-a.max.x,-center.y,-center.z);secondaryGroup.position.set(gap/2-b.min.x,-center.y,-center.z);
  for(const [i,center] of [ca,cb].entries()){const f=rotationFrames[i];f.center.copy(center);f.anchor.copy(f.group.position).add(center);}applyShapeRotation();
  const state=comparison.snapshot();
  for(const item of state.items)for(const c of item.components){
   const key=itemKey(c);let mesh=secondaryMeshes.get(key);
   if(!mesh){const source=meshByCell.get(key)??sequentialMesh(c);mesh=new THREE.Mesh(source.geometry,mats[item.species]);mesh.userData.coordinateKey=key;secondaryMeshes.set(key,mesh);secondaryGroup.add(mesh);}
   mesh.visible=true;mesh.material=mats[item.species];
  }
  setPairs(secondaryEdges,leadEdgePairs(state.items.filter(s=>s.species!=='electron').map(shape=>({shape}))));
  setPairs(secondaryElectronEdges,leadEdgePairs(state.items.filter(s=>s.species==='electron').map(shape=>({shape}))));
  const last=state.items.at(-1);secondaryPointer.visible=last.species!=='electron';setPairs(secondaryPointer,last.species!=='electron'?leadEdgePairs([{shape:last}]):[]);setPairs(secondarySelectedElectron,last.species==='electron'?leadEdgePairs([{shape:last}]):[]);
  phaseLabels(state,secondaryGroup);
  label('Shape 1 · '+$('atom').selectedOptions[0].textContent.split(' ·')[0],[ca.x,a.max.y+.18,ca.z],undefined,primaryGroup,false);
  label('Shape 2 · '+$('comparison-atom').selectedOptions[0].textContent.split(' ·')[0],[cb.x,b.max.y+.18,cb.z],undefined,secondaryGroup,false);
  $('comparison-readout').textContent=`Step ${comparisonStep}/${comparisonTotal()} · Shape 1: ${Math.min(comparisonStep,primaryTotal())}/${primaryTotal()} · Shape 2: ${state.items.length}/${state.assemblyDisplay.total}`;
  $('previous-item').disabled=false;$('next-item').disabled=false;
 }
 function leadEdgePairs(bodies){const map=new Map();for(const body of bodies)for(const c of body.shape.faces)for(const [a,b] of [[0,1],[1,2],[2,0]]){const pair=[c[a],c[b]].sort((p,q)=>p.join(',').localeCompare(q.join(',')));map.set(pair.map(p=>p.join(',')).join('|'),pair.map(worldPoint));}return [...map.values()];}
 function leadVisible(body){return atomKind==='lead208'&&lead208Bodies.indexOf(body)<layoutCount&&$(body.species+'-channel').checked;}
 function selectChain(id){if(id!==null&&(!Number.isInteger(id)||id<1||id>82))throw RangeError('Unknown chain');selectedChain=id;refresh();}
 const currentState=()=>{const path=route.slice(0,step+1).filter(i=>i>=0);return transport(path.length?path:[0],perspective);};
 function edgePairs(cellIds){const map=new Map();for(const id of cellIds)for(const [a,b] of edges){const pair=[lattice.cells[id][a],lattice.cells[id][b]].sort((a,b)=>a-b);map.set(pair.join(','),pair.map(i=>lattice.nodes[i].point));}return [...map.values()];}
 function configureScope(){
  if(atomKind==='sequential'){route=[0];scope=new Set([0]);return;}
  if(!atom){route=[-1,...traversal,-2];scope=new Set(items.map(i=>i.index));return;}
  const targets=[...new Set(atom.bodies.map(b=>itemByCell.get(b.cellId)))];
  const root=targets[0];route=[root];
  for(const target of targets.slice(1)){const path=pathBetween(root,target);route.push(...path.slice(1),...path.slice(0,-1).reverse());}
  scope=new Set(route);for(const id of [...scope])for(const neighbor of adjacency[id])scope.add(neighbor);
 }
 function updatePointer(){
  if(atomKind==='sequential'){
   const state=sequential.snapshot(),shape=state.items[state.tunnel.position];pointerOutline.visible=shape.species!=='electron';
   setPairs(pointerOutline,shape.species!=='electron'?leadEdgePairs([{shape}]):[]);
   setPairs(selectedElectronEdges,shape.species==='electron'?leadEdgePairs([{shape}]):[]);return;
  }
  const bodies=atomKind==='lead208'&&selectedChain!==null?lead208Bodies.filter(b=>b.chain===selectedChain&&leadVisible(b)):[];
  pointerOutline.visible=bodies.length>0;
  setPairs(pointerOutline,leadEdgePairs(bodies.filter(b=>b.species!=='electron')));
  setPairs(selectedElectronEdges,leadEdgePairs(bodies.filter(b=>b.species==='electron')));
 }
 function setStep(value){if(!Number.isInteger(value)||value<0||value>=route.length)throw RangeError('Invalid fiber step');step=value;updatePointer();}
 function refresh(reconfigure=false){
  coverage=null;clearLabels();for(const m of allMeshes){m.visible=false;m.material=mats.base;}
  atom=['lead208','none','sequential'].includes(atomKind)?null:makeAtom(atomKind);
  layoutTotal=atomKind==='lead208'?lead208Bodies.length:atom?.bodies.length??0;
  if(atom){atom={...atom,bodies:atom.bodies.slice(0,layoutCount)};atom.counts=Object.fromEntries(['proton','neutron','electron'].map(s=>[s,atom.bodies.filter(b=>b.species===s).length]));}
  if(reconfigure){configureScope();step=0;selectedChain=null;}
  occupiedCells=new Set();
  if(atomKind==='sequential'){
   const state=sequential.snapshot();coverage=state.assemblyDisplay.mode==='native-template'?auditWindowCoverage(state,coverageCells):state.assemblyDisplay.mode==='phase-reference'&&state.assemblyDisplay.shown===state.assemblyDisplay.total?state.phaseAudit.coverage:null;
   for(const item of state.items)for(const c of item.components){const m=sequentialMesh(c);m.visible=true;m.material=mats[item.species];if(m.userData.cell!==undefined)occupiedCells.add(m.userData.cell);}
   phaseLabels(state,primaryGroup);
   const a=state.assemblyDisplay;
   $('loadout-readout').textContent=`${a.shown}/${a.total} items · ${state.counts.proton}P / ${state.counts.neutron}N / ${state.counts.electron}e · `+(a.mode==='native-template'?'native phase template':a.mode==='phase-reference'?`phase reference · R${state.displayPhase.origin}: ${state.displayPhase.word}`:a.mode==='local-reference'?'local contact/exit reference · no global sewing or stability proof':'geometry only · phase unresolved');
  }else if(atomKind==='lead208'){
   for(const body of lead208Bodies){
    if(!leadVisible(body))continue;
    for(const mesh of leadMeshes.get(body.id)){mesh.visible=true;mesh.material=mats[body.species];if(mesh.userData.cell!==undefined)occupiedCells.add(mesh.userData.cell);}
    if(selectedChain!==null&&body.chain===selectedChain)label(body.id,body.center,'#'+body.color.toString(16));
   }
   $('loadout-readout').textContent=`${layoutCount}/${layoutTotal} items · legacy geometry`; 
  }else if(atom){
   const aliases=new Map();
   for(const body of atom.bodies){occupiedCells.add(body.cellId);cellMeshes[body.cellId].material=mats[body.species];label(body.symbol,body.center,'#'+body.color.toString(16));
    body.nodeIds.forEach(id=>aliases.set(id,'vertex-'+id));
   }
   for(const [id,name] of aliases)label(name,lattice.nodes[id].point);
   $('loadout-readout').textContent=`${atom.name} · ${layoutCount}/${layoutTotal} items · legacy geometry`;
  }else $('loadout-readout').textContent='1 · 4 · 44 · 126';
  const contextCells=new Set([...scope].flatMap(i=>items[i].children));
  if(atomKind==='none')for(const id of contextCells)cellMeshes[id].visible=true;
  for(const id of occupiedCells)cellMeshes[id].visible=true;
  setPairs(contextEdges,edgePairs([...contextCells].filter(id=>cellMeshes[id].visible&&!occupiedCells.has(id))));
  const electronCells=new Set(atom?.bodies.filter(b=>b.species==='electron').map(b=>b.cellId)??[]);
  const outlines=atomKind==='sequential'?leadEdgePairs(sequential.snapshot().items.filter(s=>s.species!=='electron').map(shape=>({shape}))):atomKind==='lead208'?leadEdgePairs(lead208Bodies.filter(b=>leadVisible(b)&&b.species!=='electron')):edgePairs([...occupiedCells].filter(id=>!electronCells.has(id)));
  const dotted=atomKind==='sequential'?leadEdgePairs(sequential.snapshot().items.filter(s=>s.species==='electron').map(shape=>({shape}))):atomKind==='lead208'?leadEdgePairs(lead208Bodies.filter(b=>leadVisible(b)&&b.species==='electron')):edgePairs([...electronCells]);
  setPairs(bodyEdges,outlines);setPairs(electronEdges,dotted);visibleEdges=outlines.length+dotted.length;
  setPairs(dual,connections.filter(e=>scope.has(e.a)&&scope.has(e.b)).map(e=>[items[e.a].center,items[e.b].center]));
  const path=route.filter(i=>i>=0);setPairs(fiber,path.slice(1).map((id,i)=>[items[path[i]].center,items[id].center]));
  dual.visible=false;fiber.visible=false;
  $('lead-controls').hidden=atomKind!=='lead208';
  $('previous-item').disabled=atomKind==='none';
  $('next-item').disabled=atomKind==='none';
  updatePointer();renderComparison();
 }
 function resize(){const w=host.clientWidth,h=host.clientHeight,a=w/h,span=Math.max(9,10/a);camera.left=-span*a/2;camera.right=span*a/2;camera.top=span/2;camera.bottom=-span/2;camera.updateProjectionMatrix();renderer.setSize(w,h);edgeStrokes.forEach(l=>l.setResolution(w,h));}
 function reset(){
  orbit.enableDamping=false;orbit.target.set(0,0,0);camera.position.set(0,0,12);camera.zoom=1;orbit.update();resize();
  if(comparison||atom||['lead208','sequential'].includes(atomKind)){const points=(comparison?comparisonPoints():atom?Object.values(atom.points):atomKind==='sequential'?[...sequential.snapshot().items.flatMap(s=>s.vertices.map(worldPoint)),...(sequential.snapshot().exit?.point?[worldPoint(sequential.snapshot().exit.point)]:[])]:lead208Bodies.flatMap(b=>b.points)).map(vec),box=new THREE.Box3().setFromPoints(points),target=box.getCenter(new THREE.Vector3());camera.position.add(target.clone().sub(orbit.target));orbit.target.copy(target);orbit.update();camera.updateMatrixWorld();
   const projected=points.map(p=>p.clone().project(camera));const width=Math.max(...projected.map(p=>p.x))-Math.min(...projected.map(p=>p.x)),height=Math.max(...projected.map(p=>p.y))-Math.min(...projected.map(p=>p.y));camera.zoom=Math.min(6,1.4/Math.max(width,height,.1));camera.updateProjectionMatrix();
  }orbit.enableDamping=true;
 }
 const syncRSpaceLink=()=>{const selected=$('atom').value,isReference=[...localReferenceIds,'helium3','helium4','lithium6','lithium7','beryllium9','boron10','boron11','carbon12','carbon13','nitrogen15'].includes(selected),isotope=isReference?selected:selected==='helium'?'helium4':['hydrogen','deuterium'].includes(selected)?selected:'deuterium';const link=$('r-space-link');if(link)link.href='/experiments/particle-overlap-tetrahedron/tessellated-space.html?isotope='+encodeURIComponent(isotope)+'&view=isotope';};
 syncRSpaceLink();
 $('atom').addEventListener('change',()=>{const selection=$('atom').value,isReference=[...localReferenceIds,'helium3','helium4','lithium6','lithium7','beryllium9','boron10','boron11','carbon12','carbon13','nitrogen15'].includes(selection);atomKind=isReference?'sequential':selection;layoutCount=1;if(atomKind==='sequential'){trialIsotope=isReference?selection:'deuterium';sequential=newTunnel();}syncRSpaceLink();resetComparison();refresh(true);reset();});
 $('comparison-atom').addEventListener('change',()=>{comparisonKind=$('comparison-atom').value;layoutCount=1;if(atomKind==='sequential')sequential.setShown(1);resetComparison();refresh(true);reset();});
 for(const id of ['proton-channel','neutron-channel','electron-channel'])$(id).addEventListener('change',()=>refresh());
 $('previous-item').addEventListener('click',previousItem);$('next-item').addEventListener('click',nextItem);
 new ResizeObserver(resize).observe(host);
 // Shared camera-relative rotation, but each full assembly keeps its own fixed center.
 let shapeDrag=null;
 renderer.domElement.addEventListener('pointerdown',e=>{if(!localRotation()||e.button!==0||e.ctrlKey||e.metaKey||e.shiftKey)return;shapeDrag={id:e.pointerId,x:e.clientX,y:e.clientY};renderer.domElement.setPointerCapture(e.pointerId);});
 renderer.domElement.addEventListener('pointermove',e=>{
  if(!shapeDrag||shapeDrag.id!==e.pointerId||!localRotation())return;
  const dx=e.clientX-shapeDrag.x,dy=e.clientY-shapeDrag.y;shapeDrag.x=e.clientX;shapeDrag.y=e.clientY;
  const scale=2*Math.PI/Math.max(1,host.clientHeight),delta=new THREE.Quaternion().setFromEuler(new THREE.Euler(dy*scale,dx*scale,0,'YXZ'));
  delta.premultiply(camera.quaternion).multiply(camera.quaternion.clone().invert());
  for(const {group} of rotationFrames)group.quaternion.premultiply(delta).normalize();applyShapeRotation();
 });
 const endShapeDrag=e=>{if(shapeDrag?.id===e.pointerId)shapeDrag=null;};
 for(const event of ['pointerup','pointercancel','lostpointercapture'])renderer.domElement.addEventListener(event,endShapeDrag);
 // Pick only visible physical cells, and do not select while dragging to orbit.
 const raycaster=new THREE.Raycaster(),mouse=new THREE.Vector2();let down=null;
 renderer.domElement.addEventListener('pointerdown',e=>down=[e.clientX,e.clientY]);
 renderer.domElement.addEventListener('pointerup',e=>{if(!down||Math.hypot(e.clientX-down[0],e.clientY-down[1])>4)return;down=null;const r=renderer.domElement.getBoundingClientRect();mouse.set((e.clientX-r.left)/r.width*2-1,-(e.clientY-r.top)/r.height*2+1);raycaster.setFromCamera(mouse,camera);const hit=raycaster.intersectObjects(allMeshes.filter(m=>m.visible))[0];if(atomKind==='lead208'){const body=hit&&lead208Bodies.find(b=>b.id===hit.object.userData.leadBody);selectChain(body?.chain??null);}else if(atomKind!=='sequential'&&hit){const index=route.indexOf(itemByCell.get(hit.object.userData.cell));if(index>=0)setStep(index);}});
 refresh(true);reset();$('loading').hidden=true;
 function animate(){orbit.update();
  camera.updateMatrixWorld();scene.updateMatrixWorld(true);for(const {el,p,group,vertexLabel} of labels){const q=group.localToWorld(vec(p)).project(camera);el.style.left=(q.x*.5+.5)*host.clientWidth+'px';el.style.top=((-q.y*.5+.5)*host.clientHeight-15)+'px';el.hidden=(vertexLabel&&!$('show-vertex-labels').checked)||Math.abs(q.x)>1||Math.abs(q.y)>1||Math.abs(q.z)>1;}
  renderer.render(scene,camera);
  frameCount++;requestAnimationFrame(animate);
 }requestAnimationFrame(animate);
 globalThis.FiberSpaceViewer={setStep,selectChain,restartSequential,previousItem,nextItem,sequentialSnapshot:()=>sequential.snapshot(),comparisonSnapshot:()=>comparison?.snapshot()??null,snapshot:()=>({step,routeLength:route.length,perspective,atomKind,trialIsotope:atomKind==='sequential'?trialIsotope:null,frameCount,identity:atomKind==='sequential'?sequential.snapshot().identity:currentState().identity,canonical:currentState().canonical,local:currentState().local,
  comparison:comparison?{kind:comparisonKind,layout:'side-by-side',step:comparisonStep,total:comparisonTotal(),primaryShown:atomKind==='sequential'?sequential.snapshot().items.length:layoutCount,primaryTotal:primaryTotal(),secondary:comparison.snapshot().assemblyDisplay,primaryOffset:primaryGroup.position.toArray(),secondaryOffset:secondaryGroup.position.toArray(),visibleComponents:[...secondaryMeshes.values()].filter(m=>m.visible).length,faceOpacities:[...new Set([...secondaryMeshes.values()].filter(m=>m.visible).map(m=>m.material.opacity))]}:null,
  coverage:coverage?{status:coverage.status,requiredCells:coverage.requiredCells,coveredCells:coverage.coveredCells,fromEntryCells:coverage.fromEntryCells,toExitCells:coverage.toExitCells,unmodeledCells:coverage.unmodeledCells.length}:null,
  tunnel:atomKind==='sequential'?sequential.snapshot().tunnel:null,
  assemblyDisplay:atomKind==='sequential'?sequential.snapshot().assemblyDisplay:{shown:layoutTotal?layoutCount:0,total:layoutTotal,mode:'legacy-geometry'},
  phaseAudit:atomKind==='sequential'?sequential.snapshot().phaseAudit:null,
  sequential:atomKind==='sequential'?{status:sequential.snapshot().status,choices:sequential.snapshot().candidates.length,added:sequential.snapshot().added}:null,itemCount:items.length,layers:lattice.assembly.layers.map(l=>l.items.length),loadout,matching:witnessPairs,available:[...available],reserved:[...reserved],
  shapeRotation:{enabled:localRotation(),frames:rotationFrames.map(({group,center,anchor})=>({quaternion:group.quaternion.toArray(),anchor:anchor.toArray(),worldCenter:group.localToWorld(center.clone()).toArray()}))},
  projection:{type:camera.isOrthographicCamera?'orthographic':'perspective',direction:camera.getWorldDirection(new THREE.Vector3()).toArray()},showVertexLabels:$('show-vertex-labels').checked,faceTransparencyPercent:Number($('face-transparency').value),faceStyles:Object.fromEntries(['proton','neutron','electron'].map(species=>[species,{opacity:mats[species].opacity,transparent:mats[species].transparent,depthWrite:mats[species].depthWrite}])),edgeStyle:{color:'#000000',widthPx:2,rendering:'LineSegments2',strokes:edgeStrokes.map(l=>({type:l.type,material:l.material.type,color:'#'+l.material.color.getHexString(),widthPx:l.material.linewidth,opacity:l.material.opacity,depthTest:l.material.depthTest,depthWrite:l.material.depthWrite,transparent:l.material.transparent}))},pointerCount:comparison?2:1,decorativeMeshCount:untrackedMeshCount(),opaque:allMeshes.every(m=>!m.material.transparent),nonElectronOpaque:allMeshes.filter(m=>m.material!==mats.electron).every(m=>!m.material.transparent),electronStyle:{opacity:mats.electron.opacity,depthWrite:mats.electron.depthWrite,dotted:electronEdges.userData.dashed,edgeCount:electronEdges.userData.segmentCount},componentMeshCount:allMeshes.length,visibleComponentCount:allMeshes.filter(m=>m.visible).length,uniqueVisibleCells:new Set(allMeshes.filter(m=>m.visible).map(m=>m.userData.coordinateKey)).size,baseComponentMeshCount:cellMeshes.length,addedComponentMeshCount:addedMeshes.length,visibleAddedComponents:addedMeshes.filter(m=>m.visible).length,leadCounts:atomKind==='lead208'?lead208Construction.counts:null,visibleLeadBodies:lead208Bodies.filter(leadVisible).map(b=>({id:b.id,species:b.species,chain:b.chain})),selectedChain,visibleCells:cellMeshes.filter(m=>m.visible).map(m=>m.userData.cell),
  visited:new Set(route.slice(0,step+1).filter(i=>i>=0)).size,atomCounts:atomKind==='sequential'?sequential.snapshot().counts:atom?.counts??null,scopeItems:[...scope],routeItems:[...new Set(route.filter(i=>i>=0))],routeVisible:fiber.visible,outlineEdgeCount:visibleEdges,cameraZoom:camera.zoom,
  channels:{proton:$('proton-channel').checked,neutron:$('neutron-channel').checked,electron:$('electron-channel').checked},geometryIds:allMeshes.map(m=>m.uuid)})};
}catch(error){document.getElementById('loading').hidden=true;const el=document.getElementById('error');el.hidden=false;el.textContent=error.message;console.error(error);}
