import {coordinateBounds,nextLayerCell,layerReferenceCellId,cellFaceLayers,spaceScale,outerSpaceEdges,protonAnchor,lattice,edges,faces,selectCarriers} from './simplex-model.mjs';
import {makeAtom} from './atom-model.mjs';
try {
  const THREE=globalThis.THREE,$=id=>document.getElementById(id),host=$('scene');
  const renderer=new THREE.WebGLRenderer({antialias:true,alpha:true});renderer.setPixelRatio(Math.min(devicePixelRatio,2));host.prepend(renderer.domElement);
  renderer.domElement.setAttribute('role','img');renderer.domElement.setAttribute('aria-label','3-simplex and barycentric carrier constructions');
  const scene=new THREE.Scene(),root=new THREE.Group(),cellRoot=new THREE.Group();scene.add(root,cellRoot);
  // One permanent mesh per assembled component. P/N/E only change its material
  // and visibility; they never create or reposition a separate particle solid.
  const highlightMaterials={proton:0x6baec8,neutron:0xd7ae77,electron:0xf19ad0,inspection:0x39ff14};
  for(const id of Object.keys(highlightMaterials))highlightMaterials[id]=new THREE.MeshBasicMaterial({color:highlightMaterials[id],side:THREE.DoubleSide,transparent:true,opacity:.28,depthWrite:false});
  const cellMeshes=lattice.cells.map((cell,cellId)=>{
    const geometry=new THREE.BufferGeometry().setFromPoints(cell.map(id=>new THREE.Vector3(...lattice.nodes[id].point)));geometry.setIndex(faces.flat());
    const mesh=new THREE.Mesh(geometry,highlightMaterials.proton);mesh.visible=false;mesh.userData.cellId=cellId;cellRoot.add(mesh);return mesh;
  });
  // Outlines trace the existing component edges; no extra solid or offset.
  // Tubes give consistent visible width on WebGL implementations ignoring linewidth.
  const outlineRoot=new THREE.Group();scene.add(outlineRoot);
  const outlineMaterials={proton:0x55d7ff,neutron:0xffcb63,electron:0xff7edb,shared:0xffffff,inspection:0x39ff14};
  for(const id of Object.keys(outlineMaterials))outlineMaterials[id]=new THREE.MeshBasicMaterial({color:outlineMaterials[id],depthTest:false,depthWrite:false});
  const outlineEdges=new Map();
  function clearOutlines(){outlineRoot.traverse(o=>o.geometry?.dispose());outlineRoot.clear();outlineEdges.clear();}
  function outlineCell(body){
    const cell=lattice.cells[body.cellId];
    for(const [a,b] of edges){
      const key=[cell[a],cell[b]].sort((a,b)=>a-b).join(',');
      if(outlineEdges.has(key)){outlineEdges.get(key).material=body.id==='inspection'?outlineMaterials.inspection:outlineMaterials.shared;continue;}
      const start=new THREE.Vector3(...lattice.nodes[cell[a]].point),end=new THREE.Vector3(...lattice.nodes[cell[b]].point);
      const direction=end.clone().sub(start);
      const mesh=new THREE.Mesh(new THREE.CylinderGeometry(.009,.009,direction.length(),8),outlineMaterials[body.species??body.id]);
      mesh.position.copy(start).add(end).multiplyScalar(.5);mesh.quaternion.setFromUnitVectors(new THREE.Vector3(0,1,0),direction.normalize());mesh.renderOrder=10;
      mesh.userData.cellId=body.cellId;outlineRoot.add(mesh);outlineEdges.set(key,mesh);
    }
  }
  const camera=new THREE.OrthographicCamera(-5,5,5,-5,.02,150),orbit=new THREE.OrbitControls(camera,renderer.domElement);orbit.enableDamping=true;
  const tooltip=document.createElement('span');tooltip.className='realization-label node';tooltip.hidden=true;tooltip.style.transform='translate(12px,12px)';tooltip.setAttribute('role','tooltip');host.append(tooltip);
  let hoveredNode=null,pointer=null;
  const hideHover=()=>{tooltip.hidden=true;hoveredNode=null;};
  function updateHover(){
    if(!pointer||!$('hover-coordinates').checked||!$('grid').checked){hideHover();return;}
    camera.updateMatrixWorld();
    let best=null,bestDistance=12**2,bestDepth=Infinity;
    lattice.nodes.forEach((node,id)=>{
      const p=new THREE.Vector3(...node.point).project(camera);
      if(Math.abs(p.x)>1||Math.abs(p.y)>1||Math.abs(p.z)>1)return;
      const x=(p.x*.5+.5)*host.clientWidth,y=(-p.y*.5+.5)*host.clientHeight;
      const d=(x-pointer.x)**2+(y-pointer.y)**2;
      if(d<bestDistance||(Math.abs(d-bestDistance)<1e-6&&p.z<bestDepth)){best=id;bestDistance=d;bestDepth=p.z;}
    });
    if(best===null){hideHover();return;}
    hoveredNode=best;const node=lattice.nodes[best];
    tooltip.textContent='Node '+best+' · grid ('+node.address.join(', ')+') · structural '+format(node.coordinate);
    tooltip.hidden=false;tooltip.style.left=Math.max(0,Math.min(pointer.x,host.clientWidth-tooltip.offsetWidth-16))+'px';tooltip.style.top=Math.max(0,Math.min(pointer.y,host.clientHeight-tooltip.offsetHeight-16))+'px';
  }
  renderer.domElement.addEventListener('pointermove',event=>{const rect=renderer.domElement.getBoundingClientRect();pointer={x:event.clientX-rect.left,y:event.clientY-rect.top};});
  renderer.domElement.addEventListener('pointerleave',()=>{pointer=null;hideHover();});
  $('hover-coordinates').addEventListener('change',updateHover);
  const elementOrder=lattice.assembly.items;
  const itemIndexByCell=new Map(elementOrder.flatMap((item,i)=>item.children.map(id=>[id,i])));
  let inspectedIndex=0,inspectedElement=elementOrder[0].children[0];
  function inspectElement(index,cellId){if(!Number.isInteger(index)||index<0||index>=elementOrder.length)return;inspectedIndex=index;inspectedElement=cellId??elementOrder[index].children[0];rebuild();}
  $('previous-element').addEventListener('click',()=>inspectElement(inspectedIndex-1));
  $('next-element').addEventListener('click',()=>inspectElement(inspectedIndex+1));
  $('previous-ten-elements').addEventListener('click',()=>inspectElement(Math.max(0,inspectedIndex-10)));
  $('next-ten-elements').addEventListener('click',()=>inspectElement(Math.min(elementOrder.length-1,inspectedIndex+10)));
  let centerCell=layerReferenceCellId;
  const layerControls=[];
  for(let axis=0;axis<4;axis++){
    const row=document.createElement('div');row.style.cssText='display:flex;align-items:center;gap:12px;margin:8px 0';
    const output=document.createElement('output');output.style.cssText='min-width:90px;text-align:center';output.id='layer-'+axis;
    const buttons=[-1,1].map(step=>{
      const button=document.createElement('button');button.type='button';button.textContent=step<0?'<':'>';button.dataset.layerAxis=axis;button.dataset.layerStep=step;
      button.setAttribute('aria-label',`λ${axis} ${step<0?'previous':'next'} layer`);
      button.addEventListener('click',()=>{const id=nextLayerCell(inspectedElement,axis,step);if(id!==null){centerCell=id;inspectElement(itemIndexByCell.get(id),id);}});
      return {button,step};
    });
    row.append(buttons[0].button,output,buttons[1].button);$('layer-flippers').append(row);layerControls.push({axis,output,buttons});
  }
  let labels=[],mode=[],atomKind='manual',selection,frameCount=0;
  const vec=p=>new THREE.Vector3(...p),format=q=>'('+q.map(x=>Number(x.toFixed(6))).join(', ')+')';
  function label(text,p,color='#dcebf1') {const el=document.createElement('span');el.className='realization-label node';el.textContent=text;el.style.color=color;host.append(el);labels.push({el,p});return el;}
  function lines(points,pairs,color,opacity=1) {const g=new THREE.BufferGeometry().setFromPoints(pairs.flatMap(e=>e.map(i=>vec(points[i]))));root.add(new THREE.LineSegments(g,new THREE.LineBasicMaterial({color,transparent:true,opacity})));}
  function rebuild() {
    root.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});root.clear();labels.forEach(l=>l.el.remove());labels=[];
    if($('grid').checked){
      const points=lattice.nodes.map(n=>n.point);
      lines(points,lattice.edges,0x7996a5,.3);
      const geometry=new THREE.BufferGeometry().setFromPoints(points.map(vec));
      root.add(new THREE.Points(geometry,new THREE.PointsMaterial({color:0xdcebf1,size:.045})));
    }
    selection=atomKind==='manual'?selectCarriers(mode,centerCell):makeAtom(atomKind,centerCell);
    if(atomKind!=='manual'){
      selection.bodies=selection.bodies.filter(b=>mode.includes(b.species));
      const names=new Set(selection.bodies.flatMap(b=>b.names));
      selection.points=Object.fromEntries(Object.entries(selection.points).filter(([name])=>names.has(name)));
    }
    $('atom-readout').textContent=atomKind==='manual'?'':`${selection.name}: ${selection.counts.proton}P · ${selection.counts.neutron}N · ${selection.counts.electron}e`;
    clearOutlines();
    for(const mesh of cellMeshes){mesh.visible=false;delete mesh.userData.carrier;}
    for(const body of selection.bodies){const mesh=cellMeshes[body.cellId];mesh.visible=true;mesh.material=highlightMaterials[body.species??body.id];mesh.userData.carrier=body.id;outlineCell(body);}
    const item=elementOrder[inspectedIndex];
    if(atomKind==='manual')for(const id of item.children){const mesh=cellMeshes[id];mesh.visible=true;mesh.material=highlightMaterials.inspection;outlineCell({id:'inspection',cellId:id});}
    const itemNodes=[...new Set(item.children.flatMap(id=>lattice.cells[id]))];
    const inspectionCenter=itemNodes.reduce((s,v)=>s.map((x,i)=>x+lattice.nodes[v].point[i]/itemNodes.length),[0,0,0]);
    const inspectionLabel=item.id;
    if(atomKind==='manual')label(inspectionLabel,inspectionCenter,'#39ff14');
    $('element-id').textContent=inspectionLabel+' · '+(inspectedIndex+1)+'/'+elementOrder.length;
    for(const {axis,output,buttons} of layerControls){
      output.textContent=`λ${axis} · ${cellFaceLayers(inspectedElement)[axis].layer}/${coordinateBounds[axis].max-coordinateBounds[axis].min}`;
      for(const {button,step} of buttons)button.disabled=nextLayerCell(inspectedElement,axis,step)===null;
    }
    $('previous-element').disabled=$('previous-ten-elements').disabled=inspectedIndex===0;
    $('next-element').disabled=$('next-ten-elements').disabled=inspectedIndex===elementOrder.length-1;
    if(atomKind==='manual')for(const [name,p] of Object.entries(selection.points))label(name,p);
    else {
      const vertexAliases=new Map();
      for(const body of selection.bodies){
        label(body.symbol,body.center,'#'+body.color.toString(16));
        body.nodeIds.forEach((id,i)=>{
          if(!vertexAliases.has(id))vertexAliases.set(id,[]);
          vertexAliases.get(id).push(body.symbol+':'+body.vertexLabels[i]);
        });
      }
      for(const [id,aliases] of vertexAliases){
        const el=label(aliases.join('\n'),lattice.nodes[id].point);
        el.classList.add('atom-vertex-label');el.dataset.nodeId=id;
        el.style.whiteSpace='pre';el.style.lineHeight='1.2';el.title='Lattice node '+id;
      }
    }
    $('focus-carriers').disabled=!selection.bodies.length;
    document.querySelectorAll('[data-carrier]').forEach(b=>b.checked=mode.includes(b.dataset.carrier));
  }
  function resize(){const w=host.clientWidth,h=host.clientHeight,a=w/h,span=spaceScale*Math.max(8,8/a);camera.left=-span*a/2;camera.right=span*a/2;camera.top=span/2;camera.bottom=-span/2;camera.updateProjectionMatrix();renderer.setSize(w,h);}
  function reset(){orbit.target.set(0,0,0);camera.position.set(8,6,4);camera.zoom=1;camera.updateProjectionMatrix();orbit.update();}
  $('atom').addEventListener('change',()=>{atomKind=$('atom').value;mode=atomKind==='manual'?[]:['proton','neutron','electron'];rebuild();});
  document.querySelectorAll('[data-carrier]').forEach(b=>b.addEventListener('change',()=>{mode=[...document.querySelectorAll('[data-carrier]:checked')].map(input=>input.dataset.carrier);rebuild();}));
  $('grid').addEventListener('change',rebuild);$('reset-view').addEventListener('click',reset);
  $('focus-carriers').addEventListener('click',()=>{const points=Object.values(selection.points);if(!points.length)return;const target=new THREE.Box3().setFromPoints(points.map(vec)).getCenter(new THREE.Vector3());camera.position.add(target.clone().sub(orbit.target));orbit.target.copy(target);camera.zoom=3*spaceScale;camera.updateProjectionMatrix();orbit.update();});
  new ResizeObserver(resize).observe(host);rebuild();resize();reset();$('loading').hidden=true;
  function animate(){orbit.update();updateHover();for(const {el,p,edge} of labels){const q=vec(p).project(camera);el.style.left=(q.x*.5+.5)*host.clientWidth+'px';el.style.top=((-q.y*.5+.5)*host.clientHeight-(edge?0:14))+'px';
      if(edge){const a=vec(edge.start).project(camera),b=vec(edge.end).project(camera);let angle=Math.atan2(-(b.y-a.y)*host.clientHeight,(b.x-a.x)*host.clientWidth)*180/Math.PI;if(angle>90)angle-=180;if(angle<-90)angle+=180;el.style.transform=`translate(-50%,-50%) rotate(${angle}deg)`;}
      el.hidden=Math.abs(q.x)>1||Math.abs(q.y)>1||Math.abs(q.z)>1;}renderer.render(scene,camera);frameCount++;requestAnimationFrame(animate);}animate();
  globalThis.SimplexSpaceViewer={snapshot:()=>({mode,atomKind,selection,frameCount,protonAnchor:selection.anchor,centerCell,hoveredNode,hoverText:tooltip.hidden?null:tooltip.textContent,lattice:{nodes:lattice.nodes.length,cells:lattice.cells.length,edges:lattice.edges.length,visible:$('grid').checked},inspectedElement,inspectedIndex,inspectedItemId:elementOrder[inspectedIndex].id,inspectedCellIds:elementOrder[inspectedIndex].children,layerCounts:lattice.assembly.layers.map(l=>l.items.length),coordinateLayer:cellFaceLayers(inspectedElement)[2].layer,inspectedMeshId:cellMeshes[inspectedElement].uuid,componentMeshCount:cellMeshes.length,outlineEdgeCount:outlineRoot.children.length,highlightedCells:cellMeshes.filter(o=>o.visible).map(o=>({cellId:o.userData.cellId,meshId:o.uuid})),renderedCarriers:cellMeshes.filter(o=>o.visible&&o.userData.carrier).map(o=>({id:o.userData.carrier,cellId:o.userData.cellId,nodeIds:lattice.cells[o.userData.cellId],positions:Array.from(o.geometry.getAttribute('position').array)}))})};
}catch(error){document.getElementById('loading').hidden=true;const el=document.getElementById('error');el.hidden=false;el.textContent=error.message;console.error(error);}
