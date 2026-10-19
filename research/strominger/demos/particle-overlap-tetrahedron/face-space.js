import {makeFaceComplex,centroid,carrierModes,interiorsOverlap} from './face-model.mjs';

try {
  const THREE=globalThis.THREE;if(!THREE?.OrbitControls)throw Error('Local Three.js / OrbitControls unavailable');
  const $=id=>document.getElementById(id),host=$('scene'),complex=makeFaceComplex();
  const state={path:[],anchor:[],carrier:'none',neighbors:true,trail:true,nodes:true};
  const renderer=new THREE.WebGLRenderer({antialias:true,alpha:true});renderer.setPixelRatio(Math.min(devicePixelRatio,2));
  renderer.domElement.setAttribute('role','img');renderer.domElement.setAttribute('aria-label','Face realization complex with three local continuation directions');host.prepend(renderer.domElement);
  const scene=new THREE.Scene(),root=new THREE.Group();scene.add(root);
  const camera=new THREE.OrthographicCamera(-2,2,2,-2,.02,150),orbit=new THREE.OrbitControls(camera,renderer.domElement);
  orbit.enableDamping=true;orbit.dampingFactor=.08;orbit.minZoom=.3;orbit.maxZoom=4;
  let labels=[],faces=[],visible=[],overlaps=[],current,exits,selection,frameCount=0;
  const vec=p=>new THREE.Vector3(...p),point=id=>vec(complex.nodes.get(id));
  const labelName=id=>id.startsWith('v')?id:'n'+id.replace('node:','').replaceAll('R','').replaceAll('/','');
  const exitButtons=[0,1,2].map(i=>{
    const button=document.createElement('button');button.type='button';button.dataset.exit=i;button.style.setProperty('--exit','#'+[0xf6b75a,0x66cfff,0xf19ad0][i].toString(16));
    button.addEventListener('click',()=>cross(i));$('exit-controls').append(button);return button;
  });
  function addLabel(text,p,kind,color,onClick) {
    const el=document.createElement(onClick?'button':'span');el.className='face-label '+kind;el.textContent=text;
    if(color)el.style.color=color;if(onClick){el.type='button';el.addEventListener('click',onClick);}
    host.append(el);labels.push({el,p});return el;
  }
  function segments(pairs,color,opacity=1,dashed=false) {
    const geometry=new THREE.BufferGeometry().setFromPoints(pairs.flatMap(pair=>pair.map(vec)));
    const material=dashed?new THREE.LineDashedMaterial({color,transparent:true,opacity,dashSize:.035,gapSize:.03}):new THREE.LineBasicMaterial({color,transparent:true,opacity});
    const mesh=new THREE.LineSegments(geometry,material);if(dashed)mesh.computeLineDistances();root.add(mesh);return mesh;
  }
  function triangle(ids,color,opacity) {
    const geometry=new THREE.BufferGeometry().setFromPoints(ids.map(point));geometry.setIndex([0,1,2]);geometry.computeVertexNormals();
    const mesh=new THREE.Mesh(geometry,new THREE.MeshBasicMaterial({color,transparent:true,opacity,side:THREE.DoubleSide,depthWrite:false}));root.add(mesh);return mesh;
  }
  function clear() {root.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});root.clear();labels.forEach(({el})=>el.remove());labels=[];faces=[];}
  function rebuild() {
    clear();current=complex.describe(complex.getCell(state.path));exits=complex.exits(state.path);selection=complex.carriers(state.carrier,state.anchor);
    const shown=new Map([[current.id,complex.getCell(state.path)]]);
    if(state.neighbors)exits.forEach(exit=>shown.set(exit.childId,complex.getCell(exit.path)));
    if(state.trail)for(let i=0;i<state.path.length;i++){const cell=complex.getCell(state.path.slice(0,i));shown.set(cell.id,cell);}
    selection.bodies.forEach(body=>shown.set(body.cellId,complex.cells.get(body.cellId)));visible=[...shown.values()];
    const edgeMap=new Map(),nodeIds=new Set();
    for(const cell of visible) {
      const occupant=selection.bodies.find(body=>body.cellId===cell.id),active=cell.id===current.id;
      const geometry=new THREE.BufferGeometry().setFromPoints(cell.vertices.map(point));geometry.setIndex([0,1,2,0,3,1,0,2,3,1,3,2]);geometry.computeVertexNormals();
      const mesh=new THREE.Mesh(geometry,new THREE.MeshBasicMaterial({color:occupant?.color||0x8eafbf,side:THREE.DoubleSide,transparent:true,opacity:occupant?.26:active?.055:.018,depthWrite:false}));
      mesh.userData.cellId=cell.id;mesh.userData.carrier=occupant?.id||null;root.add(mesh);
      for(let i=0;i<4;i++)for(let j=i+1;j<4;j++) {
        const edge=[cell.vertices[i],cell.vertices[j]].sort(),key=edge.join('|'),opacity=occupant||active?1:.23;
        if(!edgeMap.has(key)||edgeMap.get(key).opacity<opacity)edgeMap.set(key,{edge,opacity,color:occupant?.color||0x9bbac8});
      }
      cell.vertices.forEach(id=>nodeIds.add(id));
      if(occupant)addLabel(occupant.symbol,centroid(cell.vertices.map(id=>complex.nodes.get(id))),'carrier','#'+occupant.color.toString(16));
    }
    for(const {edge,color,opacity} of edgeMap.values())segments([edge.map(id=>complex.nodes.get(id))],color,opacity);
    const aliases=Object.fromEntries(Object.entries(selection.bindings).map(([name,id])=>[id,name]));
    for(const id of nodeIds) {
      const node=new THREE.Mesh(new THREE.SphereGeometry(.024,12,8),new THREE.MeshBasicMaterial({color:aliases[id]?0xd8fff0:0xa2bac8}));node.position.copy(point(id));node.userData.nodeId=id;root.add(node);
      if(state.nodes){const label=addLabel(aliases[id]||labelName(id),complex.nodes.get(id),'node');label.title=id;}
    }
    segments(current.incoming.map((id,i)=>[complex.nodes.get(id),complex.nodes.get(current.incoming[(i+1)%3])]),0xa4efd0,.9,true);
    exits.forEach(exit=>{
      const face=triangle(exit.face,exit.color,.15);face.userData.exit=exit.index;face.renderOrder=5;faces.push(face);
      const start=vec(current.center),delta=vec(exit.target).sub(start),length=delta.length(),direction=delta.normalize();
      const arrow=new THREE.ArrowHelper(direction,start.addScaledVector(direction,.04),length-.07,exit.color,.08,.045);root.add(arrow);
      const labelPoint=exit.target.map((x,i)=>current.center[i]+1.5*(x-current.center[i]));
      addLabel(exit.name,labelPoint,'exit','#'+exit.color.toString(16),()=>cross(exit.index));
      const button=exitButtons[exit.index];button.replaceChildren(document.createTextNode(exit.name));
      const detail=document.createElement('small');detail.textContent=exit.face.map(id=>aliases[id]||labelName(id)).join(' · ');button.append(detail);button.disabled=state.path.length>=16;
    });
    $('address').textContent=current.id;$('cell-badge').textContent='Current cell · '+current.id;
    $('incoming').textContent=current.incoming.map(id=>aliases[id]||labelName(id)).join(' · ');
    $('binding-readout').textContent=Object.entries(selection.bindings).map(([name,id])=>name+' ↦ '+id).join(' · ')||[...nodeIds].map(labelName).join(' · ');
    $('step-readout').textContent=`${state.path.length} face crossings · ${state.path.length%2?'odd':'even'} reflection parity`;
    $('carrier-readout').textContent=selection.bodies.length?selection.bodies.map(body=>body.symbol+' '+body.signature).join(' · ')+' · anchor '+complex.getCell(state.anchor).id:'No occupants.';
    overlaps=[];
    for(let i=0;i<visible.length;i++)for(let j=i+1;j<visible.length;j++)if(interiorsOverlap(visible[i].vertices.map(id=>complex.nodes.get(id)),visible[j].vertices.map(id=>complex.nodes.get(id))))overlaps.push([visible[i].id,visible[j].id]);
    $('geometry-readout').textContent=`${visible.length} displayed cells · ${nodeIds.size} generated nodes · current volume ${current.volume.toFixed(6)} · ${overlaps.length} interior overlaps`;
    $('embedding-warning').hidden=overlaps.length===0;
    $('embedding-warning').textContent=`Embedding conflict: ${overlaps.length} cell pairs overlap in 3D. This route is not a non-overlapping spatial tiling.`;
    $('back').disabled=!state.path.length;$('place-carriers').disabled=state.carrier==='none';$('focus-carriers').disabled=!selection.bodies.length;
    document.querySelectorAll('[data-carrier]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.carrier===state.carrier)));
    positionLabels();
  }
  function positionLabels() {
    for(const {el,p} of labels) {
      const q=vec(p).project(camera),x=(q.x*.5+.5)*host.clientWidth,y=(-q.y*.5+.5)*host.clientHeight+(el.classList.contains('node')?-13:el.classList.contains('carrier')?12:0);
      el.style.left=x+'px';el.style.top=y+'px';el.hidden=q.z<-1||q.z>1||x<12||x>host.clientWidth-12||y<48||y>host.clientHeight-30;
    }
  }
  function focus(center,zoom=1) {camera.position.add(vec(center).sub(orbit.target));orbit.target.copy(vec(center));camera.zoom=zoom;orbit.update();resize();}
  function setPath(path) {complex.getCell(path);state.path=[...path];rebuild();focus(current.center,camera.zoom);}
  function cross(index) {if(!Number.isInteger(index)||index<0||index>2)throw RangeError('Invalid local exit');if(state.path.length>=16)return;setPath([...state.path,index]);}
  function setCarrier(mode) {if(!carrierModes.includes(mode))throw RangeError('Invalid carrier mode');state.carrier=mode;rebuild();}
  function resize() {
    const w=host.clientWidth,h=host.clientHeight,aspect=w/h,span=Math.max(3.8,3.6/aspect);
    camera.left=-span*aspect/2;camera.right=span*aspect/2;camera.top=span/2;camera.bottom=-span/2;camera.updateProjectionMatrix();renderer.setSize(w,h);positionLabels();
  }
  function resetCamera() {orbit.enableDamping=false;camera.position.copy(vec(current.center).add(new THREE.Vector3(3.5,2.7,4.5)));orbit.target.copy(vec(current.center));camera.zoom=1;orbit.update();orbit.enableDamping=true;resize();}
  $('back').addEventListener('click',()=>{if(state.path.length)setPath(state.path.slice(0,-1));});$('root').addEventListener('click',()=>setPath([]));
  document.querySelectorAll('[data-carrier]').forEach(button=>button.addEventListener('click',()=>setCarrier(button.dataset.carrier)));
  $('place-carriers').addEventListener('click',()=>{state.anchor=[...state.path];rebuild();});
  for(const key of ['neighbors','trail','nodes'])$(key).addEventListener('change',event=>{state[key]=event.target.checked;rebuild();});
  $('focus-current').addEventListener('click',()=>focus(current.center,1.5));
  $('focus-carriers').addEventListener('click',()=>{if(selection.bodies.length)focus(centroid(Object.values(selection.points)),1.4);});
  $('reset-view').addEventListener('click',resetCamera);
  const raycaster=new THREE.Raycaster(),pointer=new THREE.Vector2();let down=null;
  renderer.domElement.addEventListener('pointerdown',event=>{down=event.button===0?{id:event.pointerId,x:event.clientX,y:event.clientY,drag:false}:null;});
  renderer.domElement.addEventListener('pointermove',event=>{if(down?.id===event.pointerId&&Math.hypot(event.clientX-down.x,event.clientY-down.y)>5)down.drag=true;});
  renderer.domElement.addEventListener('pointercancel',()=>{down=null;});
  renderer.domElement.addEventListener('pointerup',event=>{
    const start=down;down=null;if(!start||start.drag||start.id!==event.pointerId)return;
    const box=renderer.domElement.getBoundingClientRect();pointer.set((event.clientX-box.left)/box.width*2-1,-(event.clientY-box.top)/box.height*2+1);raycaster.setFromCamera(pointer,camera);
    const hit=raycaster.intersectObjects(faces)[0];if(hit)cross(hit.object.userData.exit);
  });
  new ResizeObserver(resize).observe(host);rebuild();resetCamera();$('loading').hidden=true;
  function animate(){orbit.update();positionLabels();renderer.render(scene,camera);frameCount++;requestAnimationFrame(animate);}requestAnimationFrame(animate);
  globalThis.FaceSpaceViewer={cross,setPath,setCarrier,projectExit:index=>{
    const p=vec(exits[index].center).project(camera),box=renderer.domElement.getBoundingClientRect();
    return {x:box.left+(p.x*.5+.5)*box.width,y:box.top+(-p.y*.5+.5)*box.height};
  },snapshot:()=>({state:{...state,path:[...state.path],anchor:[...state.anchor]},current,exits,selection,
    overlaps,cells:visible.map(cell=>complex.describe(cell)),nodes:Object.fromEntries([...new Set(visible.flatMap(cell=>cell.vertices))].map(id=>[id,complex.nodes.get(id)])),
    rendered:root.children.filter(o=>o.userData.cellId).map(o=>({cellId:o.userData.cellId,carrier:o.userData.carrier,positions:Array.from(o.geometry.getAttribute('position').array)})),
    frameCount,webgl:renderer.getContext()!==null,camera:camera.position.toArray(),cameraTarget:orbit.target.toArray(),cameraType:camera.type,
    scope:'Cell-local face reflections, not a global space-filling tiling; no planar 60-degree or C/M exchange law imposed.'})};
} catch(error) {document.getElementById('loading').hidden=true;const el=document.getElementById('error');el.hidden=false;el.textContent=error.message;console.error(error);}
