import * as THREE from 'three';
import {TrackballControls} from 'three/addons/controls/TrackballControls.js';
import {makeLattice,neighbours,key} from './geometry.js';
import {heliumCandidate,heliumCarriers} from './helium.js';
import './style.css';

const $=id=>document.getElementById(id);
try { start(); } catch(error) { $('fallback').textContent=`Unable to start WebGL: ${error.message}`; }
function start() {
  const host=$('canvas-host'),renderer=new THREE.WebGLRenderer({antialias:true});
  // Bound transparent fill cost on HiDPI screens.
  renderer.setPixelRatio(Math.min(devicePixelRatio,1.5));host.append(renderer.domElement);
  const canvas=renderer.domElement;
  canvas.tabIndex=0;canvas.setAttribute('aria-label','Lattice viewport. Drag or use arrow keys to rotate; tap to inspect a vertex. The vertex list provides keyboard selection.');
  const scene=new THREE.Scene();scene.background=new THREE.Color('#0b1120');
  const camera=new THREE.PerspectiveCamera(42,1,0.05,1000);
  const controls=new TrackballControls(camera,canvas);controls.staticMoving=true;controls.rotateSpeed=2.5;
  controls.minDistance=1;controls.maxDistance=250;
  let world,star,planeGroup,edgeMesh,pointMesh,lattice,positions=[],selected=[0,0,0];
  let heliumGroup,heliumPoints=[],labelPoints=[],frameCandidate=false;
  const poleLabels=['P1','N1','E1','P2','E2','N2'].map(text=>{const el=document.createElement('span');el.className='pole-label';el.textContent=text;el.hidden=true;host.append(el);return el;});
  let frame=0,disposed=false,interacting=false,dirty=false,rendering=false,geometryTimer=0;
  let viewportWidth=1,viewportHeight=1;
  const projectedLabel=new THREE.Vector3();
  const events=new AbortController();
  const on=(target,type,fn)=>target.addEventListener(type,fn,{signal:events.signal});
  const familyColors=[0xf4c430,0x64c5e8,0xd69cf0,0x88d8ad];
  let planeMaterials=[];
  function request(){if(!frame&&!disposed&&!rendering)frame=requestAnimationFrame(render);}
  function render(){
    frame=0;if(disposed)return;rendering=true;
    if(dirty){dirty=false;rebuild();fit();}
    if(frameCandidate){frameCandidate=false;fit(heliumPoints);}
    controls.update();renderer.render(scene,camera);
    poleLabels.forEach((el,i)=>{
      el.hidden=!heliumGroup?.visible||!labelPoints[i];
      if(!el.hidden){const p=projectedLabel.copy(labelPoints[i]).project(camera);el.hidden=p.z< -1||p.z>1||Math.abs(p.x)>1||Math.abs(p.y)>1;el.style.transform=`translate3d(${(p.x+1)*viewportWidth/2}px,${(1-p.y)*viewportHeight/2}px,0) translate(-50%,12px)`;}
    });
    rendering=false;if(interacting)request();
  }
  controls.addEventListener('change',request);
  controls.addEventListener('start',()=>{interacting=true;request();});
  controls.addEventListener('end',()=>{interacting=false;request();});
  function release(object){
    if(!object)return;
    const gs=new Set(),ms=new Set();object.traverse(o=>{if(o.isInstancedMesh)o.dispose();if(o.geometry)gs.add(o.geometry);if(o.material)(Array.isArray(o.material)?o.material:[o.material]).forEach(m=>ms.add(m));});
    gs.forEach(g=>g.dispose());ms.forEach(m=>m.dispose());scene.remove(object);
  }
  function lines(points,color,opacity=1){return new THREE.LineSegments(new THREE.BufferGeometry().setFromPoints(points),new THREE.LineBasicMaterial({color,transparent:opacity<1,opacity}));}
  function updateAppearance(){
    if(!world)return;
    planeGroup.visible=$('planes').checked;edgeMesh.visible=$('edges').checked;pointMesh.visible=$('points').checked;
    edgeMesh.material.opacity=$('helium').checked?0.12:0.48;
    pointMesh.material.transparent=true;pointMesh.material.opacity=$('helium').checked?0.15:1;pointMesh.material.depthWrite=!$('helium').checked;
    // Keep many overlapping patches from turning the larger crop into a fog.
    const densityScale=Math.min(1,12/lattice.planes.length);
    planeMaterials.forEach((m,i)=>{m.opacity=Number($('opacity').value)*densityScale;m.color.setHex($('colors').checked?familyColors[i]:0xd0b86b);});
    $('opacity-value').value=Number($('opacity').value).toFixed(2);
    $('opacity').disabled=!$('planes').checked;$('colors').disabled=!$('planes').checked;
    $('families').hidden=!$('colors').checked||!$('planes').checked;
    if(star)star.visible=$('star').checked;
    request();
  }
  function updateHelium(){
    release(heliumGroup);heliumGroup=new THREE.Group();scene.add(heliumGroup);
    heliumGroup.visible=$('helium').checked;updateAppearance();
    const chosen=$('wedge').value;
    if($('helium-mode').value==='carriers'){
      const items=heliumCarriers(Number($('distance').value)),palette={proton:0xf78c81,neutron:0x78bcf5,electron:0xffdf83};
      heliumPoints=items.flatMap(item=>item.positions.map(p=>new THREE.Vector3(...p)));labelPoints=[];
      items.forEach((item,i)=>{
        poleLabels[i].textContent=item.label;
        if(chosen!=='all'&&Number(chosen)!==i)return;
        const points=item.positions.map(p=>new THREE.Vector3(...p));labelPoints[i]=points.reduce((a,p)=>a.add(p),new THREE.Vector3()).multiplyScalar(.25);
        const triangles=[[0,1,2],[0,3,1],[0,2,3],[1,3,2]].flatMap(face=>face.flatMap(j=>points[j].toArray()));
        const geometry=new THREE.BufferGeometry();geometry.setAttribute('position',new THREE.Float32BufferAttribute(triangles,3));geometry.computeVertexNormals();
        heliumGroup.add(new THREE.Mesh(geometry,new THREE.MeshBasicMaterial({color:palette[item.species],transparent:true,opacity:chosen==='all'?.3:.65,side:THREE.DoubleSide,depthWrite:false,forceSinglePass:true})));
        const ordinary=[],extra=[];
        for(let a=0;a<4;a++)for(let b=a+1;b<4;b++){
          const square=item.indices[a].reduce((sum,x,k)=>sum+(x-item.indices[b][k])**2,0);
          (square===2?ordinary:extra).push(points[a],points[b]);
        }
        heliumGroup.add(lines(ordinary,palette[item.species]));
        if(extra.length){const dashed=new THREE.LineSegments(new THREE.BufferGeometry().setFromPoints(extra),new THREE.LineDashedMaterial({color:palette[item.species],dashSize:lattice.edgeLength*.07,gapSize:lattice.edgeLength*.04}));dashed.computeLineDistances();heliumGroup.add(dashed);}
      });
      $('wedge').disabled=!heliumGroup.visible;
      const inside=items.every(item=>item.indices.every(m=>lattice.lookup.has(key(m))));
      $('helium-info').textContent=`${chosen==='all'?'2 P · 2 N · 2 E':items[Number(chosen)].label} tetrahedral bodies from the retained He-4 core. Red P · blue N · gold E. Exact positions retained; dashed edges are longer than primitive lattice edges. Reader/exit closure remains open.${inside?'':' Some bodies extend beyond the crop.'}`;
      request();return;
    }
    const data=heliumCandidate(Number($('distance').value));heliumPoints=data.positions.map(p=>new THREE.Vector3(...p));
    labelPoints=heliumPoints.slice(0,2);poleLabels[0].textContent='Entry';poleLabels[1].textContent='Exit';
    data.wedges.forEach((ids,i)=>{
      if(chosen!=='all'&&Number(chosen)!==i)return;
      const triangles=[[0,1,2],[0,3,1],[0,2,3],[1,3,2]].flatMap(face=>face.flatMap(j=>heliumPoints[ids[j]].toArray()));
      const geometry=new THREE.BufferGeometry();geometry.setAttribute('position',new THREE.Float32BufferAttribute(triangles,3));geometry.computeVertexNormals();
      heliumGroup.add(new THREE.Mesh(geometry,new THREE.MeshBasicMaterial({color:familyColors[i],transparent:true,opacity:chosen==='all'?0.23:0.48,side:THREE.DoubleSide,depthWrite:false,forceSinglePass:true})));
    });
    heliumGroup.add(lines(data.edges.flatMap(([a,b])=>[heliumPoints[a],heliumPoints[b]]),0xf4ecd4));
    const axis=new THREE.Line(new THREE.BufferGeometry().setFromPoints([heliumPoints[0],heliumPoints[1]]),new THREE.LineDashedMaterial({color:0xffb06c,dashSize:lattice.edgeLength*.09,gapSize:lattice.edgeLength*.06,depthTest:false}));axis.computeLineDistances();axis.renderOrder=5;heliumGroup.add(axis);
    heliumPoints.forEach((p,i)=>{const marker=new THREE.Mesh(new THREE.SphereGeometry(lattice.edgeLength*.04,12,8),new THREE.MeshBasicMaterial({color:i<2?0xffb06c:0xffffff}));marker.position.copy(p);heliumGroup.add(marker);});
    const inWindow=data.indices.every(m=>lattice.lookup.has(key(m)));
    $('wedge').disabled=!heliumGroup.visible;
    $('helium-info').textContent=`${chosen==='all'?'Four equal-volume wedges':`W${Number(chosen)+1} highlighted`} · 6 vertices · 12 lattice edges. Dashed polar diagonal is added, not an elementary edge. No P/N assignment.${inWindow?'':' Some candidate vertices are outside the current lattice crop; use Show & frame candidate.'}`;
    request();
  }
  function updateSelection(){
    release(star);star=new THREE.Group();scene.add(star);
    const distance=Number($('distance').value),origin=positions[lattice.lookup.get(key(selected))],adjacent=neighbours(lattice,selected);
    star.add(lines(adjacent.flatMap(i=>[origin,positions[i]]),0xffd778));
    const marker=new THREE.Mesh(new THREE.SphereGeometry(0.18*distance/0.67,12,8),new THREE.MeshBasicMaterial({color:0xffdf87}));marker.position.copy(origin);star.add(marker);
    for(const i of adjacent){const direction=positions[i].clone().sub(origin);star.add(new THREE.ArrowHelper(direction.clone().normalize(),origin,direction.length(),0xffd778,0.25*distance/0.67,0.12*distance/0.67));}
    star.visible=$('star').checked;$('vertex').value=key(selected);
    $('selection-status').textContent=`[${selected.join(', ')}] · ${adjacent.length}/12 neighbours visible.${adjacent.length<12?' Window boundary: remaining neighbours are outside the crop.':' Complete local neighbourhood.'}`;
    request();
  }
  function rebuild(){
    release(world);world=new THREE.Group();scene.add(world);
    const distance=Number($('distance').value),extent=Number($('extent').value);
    $('extent-value').value=String(extent);$('distance-value').value=distance.toFixed(2);
    lattice=makeLattice(extent,distance);
    if(!lattice.lookup.has(key(selected)))selected=[0,0,0];
    positions=lattice.vertices.map(v=>new THREE.Vector3(...v.position));
    planeGroup=new THREE.Group();world.add(planeGroup);
    const radius=Math.max(...positions.map(p=>p.length()))*1.1,disk=new THREE.CircleGeometry(radius,64);
    planeMaterials=familyColors.map(color=>new THREE.MeshBasicMaterial({color,transparent:true,opacity:0.02,side:THREE.DoubleSide,depthWrite:false,forceSinglePass:true}));
    // Four draws rather than two draws per transparent disk. Patches within a
    // family share a colour/opacity; their ordering does not change that blend.
    for(let family=0;family<4;family++){
      const planes=lattice.planes.filter(p=>p.family===family),mesh=new THREE.InstancedMesh(disk,planeMaterials[family],planes.length),transform=new THREE.Object3D();
      planes.forEach((plane,i)=>{const normal=new THREE.Vector3(...plane.normal);transform.quaternion.setFromUnitVectors(new THREE.Vector3(0,0,1),normal);transform.position.copy(normal).multiplyScalar(plane.offset);transform.updateMatrix();mesh.setMatrixAt(i,transform.matrix);});
      mesh.instanceMatrix.needsUpdate=true;planeGroup.add(mesh);
    }
    edgeMesh=lines(lattice.edges.flatMap(([a,b])=>[positions[a],positions[b]]),0x9bb1cd,0.48);world.add(edgeMesh);
    pointMesh=new THREE.InstancedMesh(new THREE.SphereGeometry(0.075*distance/0.67,8,6),new THREE.MeshBasicMaterial({color:0xa7bad0}),positions.length);
    positions.forEach((p,i)=>pointMesh.setMatrixAt(i,new THREE.Matrix4().makeTranslation(p.x,p.y,p.z)));
    pointMesh.instanceMatrix.needsUpdate=true;world.add(pointMesh);
    const options=document.createDocumentFragment();
    for(const v of lattice.vertices){const option=document.createElement('option');option.value=key(v.index);option.textContent=`[${v.index.join(', ')}]`;options.append(option);}
    $('vertex').replaceChildren(options);
    $('status').textContent=`${positions.length} vertices · ${lattice.edges.length} edges\n${lattice.planes.length} plane patches · edge length ${lattice.edgeLength.toFixed(3)}`;
    updateSelection();updateAppearance();updateHelium();
  }
  function moveTarget(target){const offset=camera.position.clone().sub(controls.target);controls.target.copy(target);camera.position.copy(target).add(offset);camera.lookAt(target);controls.update();request();}
  function fit(points=positions){
    if(!points.length)return;
    const center=new THREE.Box3().setFromPoints(points).getCenter(new THREE.Vector3());
    const radius=Math.max(...points.map(p=>p.distanceTo(center)))*1.22;
    const half=Math.min(THREE.MathUtils.degToRad(camera.fov)/2,Math.atan(Math.tan(THREE.MathUtils.degToRad(camera.fov)/2)*camera.aspect));
    const direction=camera.position.clone().sub(controls.target).normalize();if(!direction.lengthSq())direction.set(1,.8,1.3).normalize();
    controls.target.copy(center);camera.position.copy(center).addScaledVector(direction,radius/Math.sin(half));camera.lookAt(center);controls.update();request();
  }
  function reset(){selected=[0,0,0];camera.up.set(0,1,0);camera.position.copy(controls.target).add(new THREE.Vector3(1,.8,1.3));fit();updateSelection();}
  function focus(){moveTarget(positions[lattice.lookup.get(key(selected))]);}
  function resize(){const {width,height}=host.getBoundingClientRect();viewportWidth=width;viewportHeight=height;renderer.setSize(width,height);camera.aspect=width/Math.max(1,height);camera.updateProjectionMatrix();controls.handleResize();fit();request();}
  const observer=new ResizeObserver(resize);observer.observe(host);
  const commitGeometry=()=>{clearTimeout(geometryTimer);geometryTimer=0;dirty=true;request();};
  for(const id of ['extent','distance']){
    // Topology rebuilds cost tens of ms at the largest crop. Commit on release,
    // or after a short input pause, instead of blocking every drag frame.
    on($(id),'input',()=>{clearTimeout(geometryTimer);geometryTimer=setTimeout(commitGeometry,75);});
    on($(id),'change',commitGeometry);
  }
  for(const id of ['opacity','planes','edges','points','star','colors'])on($(id),'input',updateAppearance);
  on($('vertex'),'change',()=>{selected=$('vertex').value.split(',').map(Number);updateSelection();});
  on($('reset'),'click',reset);on($('focus'),'click',focus);
  function setHeliumMode(){
    const names=$('helium-mode').value==='carriers'?['All six bodies','P1 · proton','N1 · neutron','E1 · electron','P2 · proton','E2 · electron','N2 · neutron']:['All four wedges','W1 · gold','W2 · blue','W3 · purple','W4 · green'];
    $('wedge').replaceChildren(...names.map((name,i)=>{const option=document.createElement('option');option.value=i===0?'all':String(i-1);option.textContent=name;return option;}));
    if(lattice)updateHelium();
  }
  on($('helium-mode'),'change',()=>{setHeliumMode();if($('helium').checked){frameCandidate=true;request();}});
  on($('helium'),'input',updateHelium);on($('wedge'),'change',updateHelium);
  on($('helium-preset'),'click',()=>{
    $('extent').value=String(Math.max(2,Number($('extent').value)));$('helium').checked=true;
    $('planes').checked=false;$('star').checked=false;$('wedge').value='all';
    clearTimeout(geometryTimer);geometryTimer=0;dirty=true;frameCandidate=true;request();
  });

  // Pick projected centres within a CSS-pixel halo, independent of world zoom.
  // Distance wins; depth breaks ties. The list disambiguates overlapping sites.
  function pick(event){
    if(!pointMesh.visible||dirty)return;
    const rect=canvas.getBoundingClientRect(),radius=event.pointerType==='touch'?24:14;
    camera.updateMatrixWorld();let best=null;
    positions.forEach((p,i)=>{
      const screen=p.clone().project(camera);if(screen.z< -1||screen.z>1||Math.abs(screen.x)>1||Math.abs(screen.y)>1)return;
      const x=rect.left+(screen.x+1)*rect.width/2,y=rect.top+(1-screen.y)*rect.height/2;
      const distance=Math.hypot(x-event.clientX,y-event.clientY);
      if(distance<=radius&&(!best||distance<best.distance-0.1||(Math.abs(distance-best.distance)<=0.1&&screen.z<best.depth)))best={i,distance,depth:screen.z};
    });
    if(best){selected=lattice.vertices[best.i].index;updateSelection();}
  }
  let down=null,multi=false;const pointers=new Set();
  on(canvas,'pointerdown',e=>{pointers.add(e.pointerId);if(pointers.size>1){multi=true;down=null;}else down={id:e.pointerId,x:e.clientX,y:e.clientY,moved:false};});
  on(canvas,'pointermove',e=>{if(down&&down.id===e.pointerId&&Math.hypot(e.clientX-down.x,e.clientY-down.y)>6)down.moved=true;});
  // Trackball captures pointers. Multi-touch never becomes a tap on release.
  on(canvas,'pointerup',e=>{const click=!multi&&down?.id===e.pointerId&&!down.moved;pointers.delete(e.pointerId);down=null;if(!pointers.size)multi=false;if(click)pick(e);});
  on(canvas,'pointercancel',e=>{pointers.delete(e.pointerId);down=null;if(!pointers.size)multi=false;});
  on(canvas,'keydown',event=>{
    const k=event.key.toLowerCase(),offset=camera.position.clone().sub(controls.target),axis=new THREE.Vector3();
    if(k==='f'){event.preventDefault();focus();return;}if(k==='r'){event.preventDefault();reset();return;}
    if(k==='arrowleft'||k==='arrowright'){axis.copy(camera.up);offset.applyAxisAngle(axis,k==='arrowleft'?0.12:-0.12);}
    else if(k==='arrowup'||k==='arrowdown'){axis.crossVectors(offset,camera.up).normalize();const a=k==='arrowup'?0.12:-0.12;offset.applyAxisAngle(axis,a);camera.up.applyAxisAngle(axis,a);}
    else if(k==='q'||k==='e')camera.up.applyAxisAngle(offset.clone().normalize(),k==='q'?0.12:-0.12);
    else if(k==='+'||k==='=')offset.multiplyScalar(.9);else if(k==='-')offset.multiplyScalar(1.1);else return;
    event.preventDefault();offset.clampLength(controls.minDistance,controls.maxDistance);camera.position.copy(controls.target).add(offset);camera.lookAt(controls.target);controls.update();request();
  });
  on(canvas,'webglcontextlost',event=>{event.preventDefault();$('fallback').hidden=false;$('fallback').textContent='WebGL context lost. Reload to restore the viewer.';});
  on(window,'pagehide',()=>{disposed=true;cancelAnimationFrame(frame);clearTimeout(geometryTimer);observer.disconnect();controls.dispose();release(world);release(star);release(heliumGroup);poleLabels.forEach(el=>el.remove());renderer.dispose();events.abort();});
  setHeliumMode();rebuild();resize();reset();$('fallback').hidden=true;
}
