import {loadIsotopeGeometry} from './isotope-geometry-loader.js';
import {createTessellatedSpace} from './tessellated-space.js';
import {isotopeStructureData,isotopeStructureIds} from './isotope-structure-data.mjs';
const host=document.querySelector('#scene'),error=document.querySelector('#error');
try{
  const THREE=globalThis.THREE;
  if(!THREE?.OrbitControls)throw new Error('Three.js or OrbitControls failed to load.');
  const renderer=new THREE.WebGLRenderer({antialias:true,alpha:true});
  renderer.setPixelRatio(Math.min(devicePixelRatio,2));host.prepend(renderer.domElement);
  const scene=new THREE.Scene();scene.background=new THREE.Color(0x0b1218);
  const camera=new THREE.PerspectiveCamera(42,1,.1,200);camera.position.set(6,4.5,8);
  const controls=new THREE.OrbitControls(camera,renderer.domElement);controls.enableDamping=true;
  const view=createTessellatedSpace(THREE,{halfLevels:1,radius:3,level:0,opacity:.25});scene.add(view.group);view.group.visible=false;
  let loadController=null,pendingIsotope=null;
  let isotopeRequest=0,activeStructure=null,activeGrid=null;
  const selector=document.querySelector('#isotope');
  selector.replaceChildren(...isotopeStructureIds.map(id=>{const option=document.createElement('option');option.value=id;option.textContent=isotopeStructureData[id].label;return option;}));
  const requested=new URLSearchParams(location.search).get('isotope');selector.value=isotopeStructureData[requested]?requested:'nitrogen15';
  let structureGroup=null,isotopeGridGroup=null,activeView=(new URLSearchParams(location.search).get('view')==='isotope'||(requested&&!new URLSearchParams(location.search).has('view')))?'isotope':'space',gridExtent=4;
  const speciesColors={proton:0x50cfff,neutron:0xffcf72,electron:0xff7edb},tetraFaces=[0,2,1,0,1,3,0,3,2,1,2,3];
  function showIsotope(id,items,sourceGrid){
    activeStructure={id,items};activeGrid=sourceGrid;
    pendingIsotope=null;error.hidden=true;
    for(const old of [structureGroup,isotopeGridGroup])if(old){scene.remove(old);old.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});}
    structureGroup=null;isotopeGridGroup=null;
    const record=isotopeStructureData[id];if(!record)return;
    const counts=Object.fromEntries(['proton','neutron','electron'].map(species=>[species,items.filter(item=>item.species===species).length]));
    if(counts.proton!==record.protons||counts.neutron!==record.neutrons||counts.electron!==record.electrons)throw new Error(`${record.label}: construction geometry disagrees with the structure-data counts.`);
    structureGroup=new THREE.Group();structureGroup.name=`${record.label} native construction geometry`;
    isotopeGridGroup=new THREE.Group();isotopeGridGroup.name='source tetrahedral tessellation around isotope construction';
    const nodeByAddress=new Map(sourceGrid.nodes.map((node,i)=>[JSON.stringify(node.address),i]));
    const cellByVertices=new Map(sourceGrid.cells.map((cell,i)=>[cell.slice().sort((a,b)=>a-b).join(','),i]));
    const occupied=new Set();
    for(const item of items)for(const tetra of item.tetrahedra){
      const ids=tetra.addresses.map(address=>nodeByAddress.get(JSON.stringify(address)));
      if(ids.some(id=>id===undefined))throw new Error(`${record.label}: construction vertex is outside its native tessellation.`);
      const cell=cellByVertices.get(ids.slice().sort((a,b)=>a-b).join(','));if(cell===undefined)throw new Error(`${record.label}: construction cell is absent from its native tessellation.`);occupied.add(cell);
    }
    const faceOwners=new Map();
    sourceGrid.cells.forEach((cell,id)=>{for(const face of [[0,2,1],[0,1,3],[0,3,2],[1,2,3]]){const key=face.map(i=>cell[i]).sort((a,b)=>a-b).join(',');if(!faceOwners.has(key))faceOwners.set(key,[]);faceOwners.get(key).push(id);}});
    const neighbors=Array.from({length:sourceGrid.cells.length},()=>new Set());
    for(const owners of faceOwners.values())if(owners.length===2){neighbors[owners[0]].add(owners[1]);neighbors[owners[1]].add(owners[0]);}
    const distance=new Map([...occupied].map(id=>[id,0])),queue=[...occupied];
    for(let qi=0;qi<queue.length;qi++){const id=queue[qi],d=distance.get(id);if(d>=gridExtent)continue;for(const next of neighbors[id])if(!distance.has(next)){distance.set(next,d+1);queue.push(next);}}
    const context=new Set(distance.keys());
    const gridEdges=new Map();for(const id of context){const cell=sourceGrid.cells[id];for(let i=0;i<4;i++)for(let j=i+1;j<4;j++){const edge=[cell[i],cell[j]].sort((a,b)=>a-b),key=edge.join(',');if(!gridEdges.has(key))gridEdges.set(key,edge);}}
    const gridGeometry=new THREE.BufferGeometry().setFromPoints([...gridEdges.values()].flatMap(edge=>edge.map(id=>new THREE.Vector3(...sourceGrid.nodes[id].point))));
    isotopeGridGroup.add(new THREE.LineSegments(gridGeometry,new THREE.LineBasicMaterial({color:0x8caeb8,transparent:true,opacity:.42,depthWrite:false})));
    const structurePositions={proton:[],neutron:[],electron:[]},structureEdges=[];
    for(const item of items)for(const tetraData of item.tetrahedra){
      const positions=tetraData.points;
      for(const index of tetraFaces)structurePositions[item.species].push(...positions[index]);
      for(const [a,b] of [[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]])structureEdges.push([positions[a],positions[b]]);
    }
    for(const [species,positions] of Object.entries(structurePositions))if(positions.length){
      const geometry=new THREE.BufferGeometry().setAttribute('position',new THREE.Float32BufferAttribute(positions,3));geometry.computeVertexNormals();
      const mesh=new THREE.Mesh(geometry,new THREE.MeshBasicMaterial({color:speciesColors[species],side:THREE.DoubleSide,transparent:true,opacity:.82,depthWrite:false}));
      mesh.name=`${record.id} batched ${species} construction cells`;mesh.userData={isotope:record.id,species,structureData:true,coordinateFrame:'native isotope construction'};structureGroup.add(mesh);
    }
    const edgeGeometry=new THREE.BufferGeometry().setFromPoints(structureEdges.flatMap(pair=>pair.map(p=>new THREE.Vector3(...p))));
    structureGroup.add(new THREE.LineSegments(edgeGeometry,new THREE.LineBasicMaterial({color:0xf6f1e8,transparent:true,opacity:.92})));
    scene.add(isotopeGridGroup,structureGroup);
    document.querySelector('#summary').textContent=`${record.label}: ${counts.proton}P / ${counts.neutron}N / ${counts.electron}e · ${items.length} construction cells + ${context.size-occupied.size} native grid cells of context (extent ${gridExtent}). This is not the separate R-space PNE lattice.`;
    switchView(activeView);
  }
  function fitView(group,extra=null){
    const box=new THREE.Box3().setFromObject(group);if(extra)box.union(new THREE.Box3().setFromObject(extra));
    const center=box.getCenter(new THREE.Vector3()),size=box.getSize(new THREE.Vector3()),radius=Math.max(size.x,size.y,size.z,1);
    controls.target.copy(center);camera.position.copy(center).add(new THREE.Vector3(radius*1.35,radius*1.05,radius*1.65));camera.near=Math.max(.01,radius/100);camera.far=radius*20;camera.updateProjectionMatrix();controls.update();
  }
  function switchView(mode){
    activeView=mode==='space'?'space':'isotope';view.group.visible=activeView==='space';if(structureGroup)structureGroup.visible=activeView==='isotope';if(isotopeGridGroup)isotopeGridGroup.visible=activeView==='isotope';
    document.querySelectorAll('[data-view]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.view===activeView)));
    extentInput.disabled=activeView==='space'||pendingIsotope!==null;
    const url=new URL(location.href);url.searchParams.set('view',activeView);url.searchParams.set('isotope',selector.value);history.replaceState(null,'',url);
    if(activeView==='isotope'&&activeStructure?.id!==selector.value){
      if(structureGroup)structureGroup.visible=false;if(isotopeGridGroup)isotopeGridGroup.visible=false;
      if(pendingIsotope!==selector.value)requestIsotope(selector.value);
      return;
    }
    if(activeView==='space')fitView(view.group);else if(structureGroup)fitView(structureGroup,isotopeGridGroup);
    if(activeView==='space')document.querySelector('#summary').textContent=`2×2 axial cross-section · ${view.cells.repeatCount} PNE triples · ${view.cells.bodies.length} tetrahedra across ${view.cells.tilingExtent.RIntervals} R intervals. Isotope construction is shown separately in its native coordinates; no R-space placement map is asserted.`;
    else {const record=isotopeStructureData[selector.value];document.querySelector('#summary').textContent=structureGroup?`${record.label}: ${record.protons}P / ${record.neutrons}N / ${record.electrons}e · construction on its native tetrahedral grid (extent ${gridExtent}). Not mapped onto the separate R-space PNE lattice.`:`Loading ${record.label} structure in the background…`;}
  }
  function failLoad(message){
    pendingIsotope=null;error.hidden=false;error.textContent=`${message} Select the isotope again or press Retry.`;
    document.querySelector('#retry').hidden=false;
    document.querySelector('#summary').textContent='Construction unavailable. R-space remains available.';
    loadController?.abort();loadController=null;
  }
  async function requestIsotope(id){
    const requestId=++isotopeRequest;
    loadController?.abort();loadController=new AbortController();
    pendingIsotope=id;error.hidden=true;document.querySelector('#retry').hidden=true;
    if(activeView==='isotope'){
      if(structureGroup)structureGroup.visible=false;if(isotopeGridGroup)isotopeGridGroup.visible=false;
      extentInput.disabled=true;
      document.querySelector('#summary').textContent=`Loading ${isotopeStructureData[id].label} construction in the background… R-space remains interactive.`;
    }
    try{
      const data=await loadIsotopeGeometry(id,{signal:loadController.signal});
      if(requestId!==isotopeRequest)return;
      showIsotope(id,data.items,data.grid);loadController=null;
    }catch(error){if(requestId===isotopeRequest&&error.name!=='AbortError')failLoad(error.message);}
  }
  document.querySelector('#retry').addEventListener('click',()=>requestIsotope(selector.value));
  document.querySelectorAll('[data-view]').forEach(button=>button.addEventListener('click',()=>switchView(button.dataset.view)));
  const extentInput=document.querySelector('#grid-extent'),extentOutput=document.querySelector('#grid-extent-value');
  gridExtent=Number(extentInput.value);extentOutput.textContent=`${gridExtent} cell layers`;
  extentInput.addEventListener('input',()=>{gridExtent=Number(extentInput.value);extentOutput.textContent=`${gridExtent} cell layers`;if(activeStructure)showIsotope(activeStructure.id,activeStructure.items,activeGrid);});
  selector.addEventListener('change',()=>switchView('isotope'));
  switchView(activeView);
  const resize=()=>{const w=host.clientWidth,h=host.clientHeight;renderer.setSize(w,h);camera.aspect=w/h;camera.updateProjectionMatrix();};
  new ResizeObserver(resize).observe(host);resize();
  const animate=()=>{requestAnimationFrame(animate);controls.update();renderer.render(scene,camera);};animate();
  document.querySelector('#loading').remove();
}catch(e){error.hidden=false;error.textContent=e.message;document.querySelector('#loading')?.remove();}
