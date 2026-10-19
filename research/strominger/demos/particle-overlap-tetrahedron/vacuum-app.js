import {makeSpace, axisLabel} from './vacuum-model.mjs?v=plane-nodes-60';
import {latticeCarriers,occupantModes} from './vacuum-carriers.mjs?v=lattice-nodes';

try {
  const THREE = globalThis.THREE;
  if (!THREE?.OrbitControls) throw new Error('Local Three.js / OrbitControls could not be loaded.');
  const $ = id => document.getElementById(id), host = $('scene');
  const state = {turn:60, initialAngle:0, halfLevels:3, spacing:1.1, assignment:'MMC', occupants:'none', level:0, fullLevels:[-1,0,1], stack:true, grid:true, links:true};
  const renderer = new THREE.WebGLRenderer({antialias:true, alpha:true});
  renderer.setPixelRatio(Math.min(devicePixelRatio,2));
  renderer.domElement.setAttribute('role','img');
  renderer.domElement.setAttribute('aria-label','Empty structured space with discrete R realization levels and signed C/M axes');
  host.prepend(renderer.domElement);
  const scene = new THREE.Scene(), root = new THREE.Group(); scene.add(root);
  const camera = new THREE.OrthographicCamera(-6,6,6,-6,.1,150);
  const orbit = new THREE.OrbitControls(camera,renderer.domElement);
  orbit.enableDamping = true; orbit.dampingFactor = .08; orbit.minZoom = .35; orbit.maxZoom = 4;
  let space, occupants, frameCount = 0, labels = [];
  const v = p => new THREE.Vector3(...p);
  const tip = (frame,axis,sign=1) => frame.origin.map((x,i) => x+sign*3.45*axis.direction[i]);
  function addLabel(text,point,color,kind='',typed=null) {
    const el = document.createElement(kind==='level'?'button':'span'); el.className = 'vacuum-label '+kind;
    if(kind==='level') {
      const level=typed.level,full=state.fullLevels.includes(level);
      el.type='button';el.dataset.level=String(level);el.textContent=text;
      el.setAttribute('aria-pressed',String(full));
      el.setAttribute('aria-label',`${text}: ${full?'full plane':'traces only'}`);
      el.title=full?'Click to show traces only':'Click to show full plane';
      el.addEventListener('click',()=>togglePlane(level));
    } else if(typed) {
      const {axis,sign,level}=typed;
      el.dataset.axis=axis.name;el.dataset.role=axis.role;el.dataset.sign=String(sign);
      el.dataset.rolePair=axis.roles.join('|');el.dataset.level=String(level);
      el.textContent=text;el.setAttribute('aria-label',`${text}, R = ${level}`);
    } else el.textContent = text;
    if(color)el.style.color = color; host.append(el); labels.push({el,point});return el;
  }
  function segments(pairs,color,opacity,dashed=false) {
    const geometry = new THREE.BufferGeometry().setFromPoints(pairs.flatMap(pair=>pair.map(v)));
    const material = dashed ? new THREE.LineDashedMaterial({color,transparent:true,opacity,dashSize:.08,gapSize:.09,depthWrite:false})
      : new THREE.LineBasicMaterial({color,transparent:true,opacity,depthWrite:false});
    const line = new THREE.LineSegments(geometry,material); if(dashed)line.computeLineDistances(); root.add(line); return line;
  }
  function clear() {
    root.traverse(o=>{o.geometry?.dispose();o.material?.dispose();}); root.clear();
    labels.forEach(({el})=>el.remove()); labels=[];
  }
  function drawOccupants() {
    for(const body of occupants.bodies) {
      const geometry=new THREE.BufferGeometry().setFromPoints(body.nodes.map(name=>v(occupants.points[name])));
      geometry.setIndex([0,1,2,0,3,1,0,2,3,1,3,2]);geometry.computeVertexNormals();
      const mesh=new THREE.Mesh(geometry,new THREE.MeshBasicMaterial({color:body.color,side:THREE.DoubleSide,transparent:true,opacity:.24,depthWrite:false}));
      mesh.userData.carrierBody=body.id;root.add(mesh);
      const center=body.nodes.reduce((s,name)=>s.map((x,i)=>x+occupants.points[name][i]/4),[0,0,0]);
      addLabel({proton:'P',neutron:'N',electron:'E'}[body.id],center,'#'+body.color.toString(16).padStart(6,'0'),'carrier carrier-'+body.id);
      for(let i=0;i<body.window.length-1;i++) {
        const start=v(occupants.points[body.window[i]]),end=v(occupants.points[body.window[i+1]]),delta=end.clone().sub(start),length=delta.length();
        const arrow=new THREE.ArrowHelper(delta.normalize(),start,length,body.color,.12,.065);
        arrow.userData.carrierRoute=body.id;root.add(arrow);
      }
    }
    for(const edge of occupants.edges) {
      const owners=occupants.bodies.filter(body=>edge.every(name=>body.nodes.includes(name)));
      segments([[occupants.points[edge[0]],occupants.points[edge[1]]]],owners.length>1?0xe8eccb:owners[0].color,.95);
    }
    for(const [name,point] of Object.entries(occupants.points)) {
      const mesh=new THREE.Mesh(new THREE.SphereGeometry(.045,12,8),new THREE.MeshBasicMaterial({color:name[0]==='M'?0xffd6a1:0xd8fff0}));
      mesh.position.copy(v(point));mesh.userData.carrierNode=name;root.add(mesh);
      const label=addLabel(name.replace(/[012]/g,d=>'₀₁₂'[Number(d)]),point,null,'carrier-node');
      const address=occupants.bindings[name];
      label.title=`${name}: R=${address.level}, q=${address.q}, r=${address.r}`;
    }
  }
  function rebuild() {
    clear(); space = makeSpace(state);
    const selected = space.frames.find(f=>f.level===state.level);
    occupants=latticeCarriers(space,state.occupants,state.level);
    const frames = state.stack ? space.frames : [selected];
    const rmax = state.halfLevels*state.spacing+.6;
    segments([[[0,-rmax,0],[0,rmax,0]]],0xa4efd0,.4,true);
    addLabel('R · realization',[0,rmax+.25,0],'#a4efd0');
    const tickGeometry = new THREE.SphereGeometry(.065,12,8);
    for(const frame of space.frames) {
      const dot = new THREE.Mesh(tickGeometry.clone(),new THREE.MeshBasicMaterial({color:frame.level===state.level?0xe0fff2:0x71968f}));
      dot.position.copy(v(frame.origin));root.add(dot);
      addLabel('R = '+frame.level,[.17,frame.origin[1]+.1,.12],null,'level',{level:frame.level});
    }
    tickGeometry.dispose();
    for(const frame of frames) {
      const formatted = state.fullLevels.includes(frame.level);
      if(state.grid) {
        const mesh=segments(space.patch.edges.map(([a,b])=>[frame.points[a],frame.points[b]]),formatted?0xa8cecf:0x6b919f,formatted?.36:.12);
        mesh.userData={planeLevel:frame.level,planePart:'grid'};
      }
      for(const axis of frame.axes) {
        const mesh=segments([[tip(frame,axis,-1),tip(frame,axis)]],axis.color,formatted?1:.22);
        mesh.userData={planeLevel:frame.level,planePart:'axis'};
        for(const sign of [-1,1]) {
          const end = tip(frame,axis,sign), direction = v(axis.direction).multiplyScalar(sign);
          const arrow = new THREE.ArrowHelper(direction,v(end).addScaledVector(direction,-.18),.18,axis.color,.14,.065);
          arrow.line.material.transparent=true;arrow.line.material.opacity=formatted?1:.25;
          arrow.cone.material.transparent=true;arrow.cone.material.opacity=formatted?1:.25;root.add(arrow);
        }
        if(formatted) {
          for(const sign of [1,-1])addLabel(axisLabel(axis,sign),tip(frame,axis,sign),
            '#'+axis.color.toString(16).padStart(6,'0'),'typed',{axis,sign,level:frame.level});
        }
      }
      if(formatted) {
        const boundary = space.patch.sites.filter(([q,r])=>Math.max(Math.abs(q),Math.abs(r),Math.abs(q-r))===space.patch.radius)
          .map(([q,r])=>{const a=frame.axes[0].direction,b=frame.axes[1].direction;return frame.origin.map((x,i)=>x+q*a[i]+r*b[i]);})
          .sort((a,b)=>Math.atan2(a[2],a[0])-Math.atan2(b[2],b[0]));
        const mesh=segments(boundary.map((p,i)=>[p,boundary[(i+1)%boundary.length]]),0xa4efd0,.55);
        mesh.userData={planeLevel:frame.level,planePart:'boundary'};
      }
    }
    if(state.links&&state.stack) {
      const pairs=[];
      for(let i=1;i<space.frames.length;i++)for(let a=0;a<3;a++)for(const sign of [-1,1])
        pairs.push([tip(space.frames[i-1],space.frames[i-1].axes[a],sign),tip(space.frames[i],space.frames[i].axes[a],sign)]);
      segments(pairs,0x9eb5c1,.22,true);
    }
    drawOccupants();
    for(const [id,key] of [['turn','turn'],['initial-angle','initialAngle'],['extent','halfLevels'],['spacing','spacing'],['level','level']]) {
      $(id).value=state[key]; $(id+'-output').textContent=state[key]+(['turn','initial-angle'].includes(id)?'°':'');
    }
    $('level').min=-state.halfLevels;$('level').max=state.halfLevels;
    $('previous-level').disabled=state.level<=-state.halfLevels;$('next-level').disabled=state.level>=state.halfLevels;
    $('level-readout').textContent='R = '+state.level;
    $('assignment').value=state.assignment;
    $('axis-pattern').textContent=`2 × ${selected.axes[0].role}± + 1 × ${selected.axes[2].role}±`;
    $('assignment-readout').textContent=`R = ${selected.level}: (`+selected.axes.map(axis=>axis.role).join(', ')+')';
    $('angle-readout').textContent=`${selected.angle-state.turn}° → ${selected.angle}° (Δ ${state.turn}°)`;
    const count=occupants.bodies.length;
    $('space-readout').textContent=`${frames.length} frames · ${state.grid?frames.length*space.patch.sites.length:0} lattice sites · ${count} carriers`;
    $('occupant-badge').textContent=occupants.status==='blocked'?'Lattice attachment blocked':count?`${count} cell${count===1?'':'s'} · R = ${occupants.realizationLevels.join(' → ')}`:'Unoccupied · 0 particles';
    $('occupant-readout').textContent=occupants.status==='blocked'?occupants.obstruction:count?occupants.bodies.map(body=>body.notation).join(' · '):'No carrier geometry shown.';
    $('focus-carriers').disabled=count===0;
    $('node-bindings').replaceChildren(...Object.entries(occupants.bindings).map(([name,address])=>{
      const row=document.createElement('li');row.textContent=`${name}: R=${address.level}, q=${address.q}, r=${address.r}`;return row;
    }));
    document.querySelectorAll('[data-occupants]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.occupants===state.occupants)));
    renderer.domElement.setAttribute('aria-label',count?'Structured realization space with '+occupants.bodies.map(body=>body.id).join(', '):'Empty structured space with discrete R realization levels and signed C/M axes');
    document.querySelectorAll('[data-turn]').forEach(el=>el.setAttribute('aria-pressed',String(Number(el.dataset.turn)===state.turn)));
    renderer.domElement.dataset.occupants=String(count);
    updateLabels();
  }
  function updateLabels() {
    const width=host.clientWidth,height=host.clientHeight;
    for(const {el,point} of labels) {
      const p=v(point).project(camera), x=(p.x*.5+.5)*width+(el.classList.contains('level')?44:el.classList.contains('carrier-proton')?-30:el.classList.contains('carrier-neutron')?-35:el.classList.contains('carrier-electron')?35:0),y=(-p.y*.5+.5)*height+(el.classList.contains('carrier-node')?-14:el.classList.contains('carrier')?14:0);
      el.style.left=x+'px';el.style.top=y+'px';
      el.hidden=p.z<-1||p.z>1||x<15||x>width-15||y<50||y>height-32;
    }
  }
  function resize() {
    const w=host.clientWidth,h=host.clientHeight,aspect=w/h;
    const span=Math.max(10,2*state.halfLevels*state.spacing+2,9/aspect);
    camera.left=-span*aspect/2;camera.right=span*aspect/2;camera.top=span/2;camera.bottom=-span/2;
    camera.updateProjectionMatrix();renderer.setSize(w,h);updateLabels();
  }
  function resetCamera(top=false) {
    orbit.enableDamping=false;orbit.update();
    camera.up.set(0,1,0); camera.position.set(...(top?[0,18,.001]:[10,8,12]));orbit.target.set(0,0,0);camera.zoom=1;
    orbit.update();orbit.enableDamping=true;resize();
  }
  function setState(patch) {
    const next={...state,...patch};
    makeSpace(next); // Validate parameters before changing the visible state.
    if(!occupantModes.includes(next.occupants))throw new RangeError('Unknown occupant selection');
    if(!Number.isInteger(next.level))throw new TypeError('Selected R level must be discrete');
    if(!Array.isArray(next.fullLevels)||next.fullLevels.some(level=>!Number.isInteger(level)||Math.abs(level)>5))
      throw new TypeError('Full-plane levels must be integers from -5 to 5');
    next.fullLevels=[...new Set(next.fullLevels)].sort((a,b)=>a-b);
    next.level=Math.max(-next.halfLevels,Math.min(next.halfLevels,next.level));
    Object.assign(state,next);rebuild();resize();
  }
  function togglePlane(level) {
    if(!Number.isInteger(level)||Math.abs(level)>state.halfLevels)throw new RangeError('R plane is outside the displayed extent');
    const restoreFocus=document.activeElement?.classList.contains('level')&&document.activeElement.dataset.level===String(level);
    setState({fullLevels:state.fullLevels.includes(level)?state.fullLevels.filter(n=>n!==level):[...state.fullLevels,level]});
    if(restoreFocus)labels.find(({el})=>el.classList.contains('level')&&el.dataset.level===String(level))?.el.focus({preventScroll:true});
  }
  for(const [id,key] of [['turn','turn'],['initial-angle','initialAngle'],['extent','halfLevels'],['spacing','spacing'],['level','level']])
    $(id).addEventListener('input',event=>setState({[key]:Number(event.target.value)}));
  function projectLevel(level) {
    const frame=space.frames.find(f=>f.level===level);
    if(!frame)throw new RangeError('R node is outside the displayed extent');
    const p=v(frame.origin).project(camera),rect=renderer.domElement.getBoundingClientRect();
    return {x:rect.left+(p.x*.5+.5)*rect.width,y:rect.top+(-p.y*.5+.5)*rect.height,visible:p.z>=-1&&p.z<=1};
  }
  let pointerStart=null;
  renderer.domElement.addEventListener('pointerdown',event=>{
    pointerStart=event.button===0?{id:event.pointerId,x:event.clientX,y:event.clientY}:null;
  });
  renderer.domElement.addEventListener('pointermove',event=>{
    if(pointerStart?.id===event.pointerId&&Math.hypot(event.clientX-pointerStart.x,event.clientY-pointerStart.y)>5)pointerStart.dragged=true;
  });
  renderer.domElement.addEventListener('pointercancel',()=>{pointerStart=null;});
  renderer.domElement.addEventListener('pointerup',event=>{
    const start=pointerStart;pointerStart=null;
    if(!start||start.dragged||start.id!==event.pointerId||Math.hypot(event.clientX-start.x,event.clientY-start.y)>5)return;
    const nearest=space.frames.map(frame=>{
      const p=projectLevel(frame.level);
      return {level:frame.level,distance:p.visible?Math.hypot(event.clientX-p.x,event.clientY-p.y):Infinity};
    }).sort((a,b)=>a.distance-b.distance)[0];
    if(nearest?.distance<=14)togglePlane(nearest.level);
  });
  document.querySelectorAll('[data-occupants]').forEach(button=>button.addEventListener('click',()=>setState({occupants:button.dataset.occupants})));
  $('assignment').addEventListener('change',event=>setState({assignment:event.target.value}));
  for(const id of ['stack','grid','links'])$(id).addEventListener('change',event=>setState({[id]:event.target.checked}));
  document.querySelectorAll('[data-turn]').forEach(el=>el.addEventListener('click',()=>setState({turn:Number(el.dataset.turn)})));
  $('previous-level').addEventListener('click',()=>setState({level:state.level-1}));
  $('next-level').addEventListener('click',()=>setState({level:state.level+1}));
  $('focus-carriers').addEventListener('click',()=>{
    if(!occupants.bodies.length)return;
    const center=new THREE.Box3().setFromPoints(Object.values(occupants.points).map(v)).getCenter(new THREE.Vector3());
    camera.position.add(center.clone().sub(orbit.target));orbit.target.copy(center);camera.zoom=3;orbit.update();resize();
  });
  $('reset-view').addEventListener('click',()=>resetCamera());$('top-view').addEventListener('click',()=>resetCamera(true));
  new ResizeObserver(resize).observe(host);
  rebuild();resetCamera();$('loading').hidden=true;
  function animate() {orbit.update();updateLabels();renderer.render(scene,camera);frameCount++;requestAnimationFrame(animate);}
  requestAnimationFrame(animate);
  globalThis.VacuumSpaceViewer={setState,resetCamera,togglePlane,projectLevel,snapshot:()=>({state:{...state,fullLevels:[...state.fullLevels]},space,frameCount,
    fullPlaneLevels:(state.stack?space.frames:space.frames.filter(f=>f.level===state.level)).filter(f=>state.fullLevels.includes(f.level)).map(f=>f.level),
    renderedFrameCount:state.stack?space.frames.length:1,occupantCount:occupants.bodies.length,particlePathCount:occupants.bodies.length,
    occupantOverlay:occupants,
    renderedCarrierBodies:root.children.filter(o=>o.userData.carrierBody).map(o=>({id:o.userData.carrierBody,positions:Array.from(o.geometry.getAttribute('position').array),triangles:o.geometry.index.count/3})),
    renderedCarrierNodeNames:root.children.filter(o=>o.userData.carrierNode).map(o=>o.userData.carrierNode),
    projectedCarrierNodes:Object.fromEntries(Object.entries(occupants.points).map(([name,p])=>[name,v(p).project(camera).toArray()])),
    cameraZoom:camera.zoom,
    typedLabels:labels.filter(({el})=>el.dataset.axis).map(({el})=>({axis:el.dataset.axis,roles:el.dataset.rolePair,role:el.dataset.role,sign:Number(el.dataset.sign),level:Number(el.dataset.level),text:el.textContent})),
    planeFormatting:root.children.filter(o=>o.userData.planePart).map(o=>({level:o.userData.planeLevel,part:o.userData.planePart,opacity:o.material.opacity,color:o.material.color.getHex()})),
    normalAxis:space.normalAxis,
    renderedSegments:root.children.filter(o=>o.isLineSegments).reduce((s,o)=>s+o.geometry.getAttribute('position').count/2,0),
    camera:camera.position.toArray(),cameraTarget:orbit.target.toArray(),cameraType:camera.type,
    webgl:renderer.getContext()!==null,renderCalls:renderer.info.render.calls})};
} catch(error) {
  document.getElementById('loading').hidden=true;
  const el=document.getElementById('error');el.hidden=false;el.textContent=error.message;console.error(error);
}
