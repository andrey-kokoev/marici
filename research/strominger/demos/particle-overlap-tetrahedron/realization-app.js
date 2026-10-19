import {makeRealizationSpace,realizationBasis,carrierModes} from './realization-model.mjs';
try {
  const THREE=globalThis.THREE;if(!THREE?.OrbitControls)throw Error('Local Three.js / OrbitControls unavailable');
  const $=id=>document.getElementById(id),host=$('scene');
  const state={address:[0,0,0],carrier:'none',assignment:'MMC',extent:2,grid:true,typed:true,realizationAxes:true};
  const renderer=new THREE.WebGLRenderer({antialias:true,alpha:true});renderer.setPixelRatio(Math.min(devicePixelRatio,2));renderer.domElement.setAttribute('role','img');renderer.domElement.setAttribute('aria-label','Unsubdivided tetrahedral 3-simplex with realization axes and a signed M/C frame');host.prepend(renderer.domElement);
  const scene=new THREE.Scene(),root=new THREE.Group();scene.add(root);
  const camera=new THREE.OrthographicCamera(-5,5,5,-5,.02,150),orbit=new THREE.OrbitControls(camera,renderer.domElement);orbit.enableDamping=true;orbit.dampingFactor=.08;orbit.minZoom=.3;orbit.maxZoom=5;
  let model,labels=[],frameCount=0;
  const vec=p=>new THREE.Vector3(...p),rColors=[0xb9e1d2,0xaccce9,0xd7c0ec];
  function label(text,p,kind,color,action) {
    const el=document.createElement(action?'button':'span');el.className='realization-label '+kind;el.textContent=text;
    if(color)el.style.color=color;if(action){el.type='button';el.addEventListener('click',action);}host.append(el);labels.push({el,p});return el;
  }
  function line(pairs,color,opacity=1) {
    const geometry=new THREE.BufferGeometry().setFromPoints(pairs.flatMap(pair=>pair.map(vec))),mesh=new THREE.LineSegments(geometry,new THREE.LineBasicMaterial({color,transparent:true,opacity,depthWrite:false}));root.add(mesh);return mesh;
  }
  function clear(){root.traverse(o=>{o.geometry?.dispose();o.material?.dispose();});root.clear();labels.forEach(({el})=>el.remove());labels=[];}
  function arrow(direction,length,color,kind,text,action) {
    const dir=vec(direction),origin=vec(model.frame.origin),mesh=new THREE.ArrowHelper(dir,origin,length,color,.11,.055);root.add(mesh);
    label(text,origin.addScaledVector(dir,length+.1).toArray(),kind,'#'+color.toString(16).padStart(6,'0'),action);
  }
  function rebuild() {
    clear();model=makeRealizationSpace(state);
    if(state.grid) {
      const {vertices,edges,faces}=model.space;
      const boundary=line(edges.map(([a,b])=>[vertices[a],vertices[b]]),0x7996a5,.65);
      boundary.userData.simplexEdges=true;
      const geometry=new THREE.BufferGeometry().setFromPoints(vertices.map(vec));
      const corners=new THREE.Points(geometry,new THREE.PointsMaterial({color:0xcce9ef,size:.09}));
      corners.userData.simplexVertices=true;root.add(corners);
      const surface=new THREE.BufferGeometry().setFromPoints(vertices.map(vec));surface.setIndex(faces.flat());
      const shell=new THREE.Mesh(surface,new THREE.MeshBasicMaterial({color:0x7996a5,side:THREE.DoubleSide,transparent:true,opacity:.045,depthWrite:false}));
      shell.userData.simplexFaces=true;root.add(shell);
    }
    const current=new THREE.Mesh(new THREE.SphereGeometry(.065,16,10),new THREE.MeshBasicMaterial({color:0xd9fff0}));current.position.copy(vec(model.frame.origin));root.add(current);
    if(state.realizationAxes)realizationBasis.forEach((axis,i)=>{for(const sign of [-1,1])arrow(axis.map(x=>x*sign),2.6,rColors[i],'r','R'+'₁₂₃'[i]+(sign===1?'+':'−'),()=>step(i,sign));});
    if(state.typed)model.frame.axes.forEach(axis=>{for(const sign of [-1,1])arrow(axis.direction.map(x=>x*sign),1.8,axis.role==='M'?0xf6b75a:0x66cfff,'typed',axis.role+(sign===1?'+':'-'));});
    const {bodies,points,bindings}=model.carriers,edges=new Map();
    for(const body of bodies) {
      const geometry=new THREE.BufferGeometry().setFromPoints(body.names.map(name=>vec(points[name])));geometry.setIndex([0,1,2,0,3,1,0,2,3,1,3,2]);geometry.computeVertexNormals();
      const mesh=new THREE.Mesh(geometry,new THREE.MeshBasicMaterial({color:body.color,side:THREE.DoubleSide,transparent:true,opacity:.25,depthWrite:false}));mesh.userData.carrier=body.id;root.add(mesh);
      for(let i=0;i<4;i++)for(let j=i+1;j<4;j++){const edge=[body.names[i],body.names[j]].sort();edges.set(edge.join('|'),{edge,color:body.color});}
      const center=body.names.reduce((s,name)=>s.map((x,i)=>x+points[name][i]/4),[0,0,0]);label(body.symbol,center,'carrier '+body.id,'#'+body.color.toString(16));
    }
    for(const {edge,color} of edges.values())line([[points[edge[0]],points[edge[1]]]],color,1);
    for(const [name,p] of Object.entries(points)) {
      const dot=new THREE.Mesh(new THREE.SphereGeometry(.045,12,8),new THREE.MeshBasicMaterial({color:name[0]==='M'?0xffd6a1:0xd8fff0}));dot.position.copy(vec(p));root.add(dot);
      const el=label(name,p,'node');el.title='R = ('+bindings[name]+')';
    }
    const address='('+state.address.join(', ')+')';$('address-readout').textContent=address;$('coordinate-badge').textContent='R = '+address;
    $('frame-readout').textContent=`${model.frame.angleDegrees}° · ${model.frame.roles.split('').join('/')} · grade ${model.frame.grade}`;
    $('binding-readout').textContent=Object.entries(bindings).map(([name,id])=>name+' ↦ ('+id+')').join(' · ')||'No occupants';
    state.address.forEach((x,i)=>$('r'+(i+1)+'-output').textContent=x);
    $('carrier-readout').textContent=bodies.map(body=>body.symbol+' '+body.signature).join(' · ')||'No occupants.';$('focus-carriers').disabled=!bodies.length;
    $('node-bindings').replaceChildren(...Object.entries(bindings).map(([name,id])=>{const el=document.createElement('li');el.textContent=name+': ('+id+')';return el;}));
    document.querySelectorAll('[data-carrier]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.carrier===state.carrier)));$('assignment').value=state.assignment;
    positionLabels();
  }
  function positionLabels(){for(const {el,p} of labels){const q=vec(p).project(camera),x=(q.x*.5+.5)*host.clientWidth+(el.classList.contains('proton')?-22:el.classList.contains('neutron')?22:el.classList.contains('electron')?-35:0),y=(-q.y*.5+.5)*host.clientHeight+(el.classList.contains('node')?-14:el.classList.contains('electron')?-20:el.classList.contains('carrier')?14:0);el.style.left=x+'px';el.style.top=y+'px';el.hidden=q.z<-1||q.z>1||x<12||x>host.clientWidth-12||y<48||y>host.clientHeight-30;}}
  function setState(patch){const next={...state,...patch};makeRealizationSpace(next);Object.assign(state,next,{address:[...next.address]});rebuild();}
  function step(axis,sign){if(!Number.isInteger(axis)||axis<0||axis>2||![1,-1].includes(sign))throw RangeError('Invalid signed realization step');const address=[...state.address];address[axis]+=sign;setState({address});}
  function resize(){const w=host.clientWidth,h=host.clientHeight,aspect=w/h,span=Math.max(9.8,9/aspect);camera.left=-span*aspect/2;camera.right=span*aspect/2;camera.top=span/2;camera.bottom=-span/2;camera.updateProjectionMatrix();renderer.setSize(w,h);positionLabels();}
  function focus(p,zoom){camera.position.add(vec(p).sub(orbit.target));orbit.target.copy(vec(p));camera.zoom=zoom;orbit.update();resize();}
  function resetCamera(){orbit.enableDamping=false;orbit.target.copy(vec(model.frame.origin));camera.position.copy(orbit.target).add(new THREE.Vector3(8,6,4));camera.zoom=1.3;orbit.update();orbit.enableDamping=true;resize();}
  document.querySelectorAll('[data-axis]').forEach(button=>button.addEventListener('click',()=>step(Number(button.dataset.axis),Number(button.dataset.sign))));
  document.querySelectorAll('[data-carrier]').forEach(button=>button.addEventListener('click',()=>setState({carrier:button.dataset.carrier})));
  $('origin').addEventListener('click',()=>{setState({address:[0,0,0]});resetCamera();});$('assignment').addEventListener('change',event=>setState({assignment:event.target.value}));
  for(const [id,key] of [['grid','grid'],['typed','typed'],['realization-axes','realizationAxes']])$(id).addEventListener('change',event=>setState({[key]:event.target.checked}));
  $('focus-current').addEventListener('click',()=>focus(model.frame.origin,1.7));$('focus-carriers').addEventListener('click',()=>{const points=Object.values(model.carriers.points);if(points.length)focus(new THREE.Box3().setFromPoints(points.map(vec)).getCenter(new THREE.Vector3()).toArray(),3);});$('reset-view').addEventListener('click',resetCamera);
  new ResizeObserver(resize).observe(host);rebuild();resetCamera();$('loading').hidden=true;
  function animate(){orbit.update();positionLabels();renderer.render(scene,camera);frameCount++;requestAnimationFrame(animate);}requestAnimationFrame(animate);
  globalThis.RealizationSpaceViewer={step,setState,snapshot:()=>({state:{...state,address:[...state.address]},model,frameCount,webgl:renderer.getContext()!==null,
    realizationLabels:labels.filter(({el})=>el.classList.contains('r')).map(({el})=>el.textContent),typedLabels:labels.filter(({el})=>el.classList.contains('typed')).map(({el})=>el.textContent),
    renderedSimplex:{vertices:root.children.find(o=>o.userData.simplexVertices)?.geometry.getAttribute('position').count??0,edges:(root.children.find(o=>o.userData.simplexEdges)?.geometry.getAttribute('position').count??0)/2,faces:(root.children.find(o=>o.userData.simplexFaces)?.geometry.index.count??0)/3},
    renderedCarriers:root.children.filter(o=>o.userData.carrier).map(o=>({id:o.userData.carrier,positions:Array.from(o.geometry.getAttribute('position').array)})),camera:camera.position.toArray(),cameraTarget:orbit.target.toArray(),cameraZoom:camera.zoom})};
}catch(error){document.getElementById('loading').hidden=true;const el=document.getElementById('error');el.hidden=false;el.textContent=error.message;console.error(error);}
