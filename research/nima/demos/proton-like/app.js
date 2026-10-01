/* Exact source incidence; floating-point coordinates are for rendering only. */
(() => {
'use strict';
const $ = id => document.getElementById(id);
try {
  if (!window.THREE) throw new Error('The local Three.js library did not load.');
  const T = window.THREE;
  const viewport = $('viewport');
  const renderer = new T.WebGLRenderer({antialias:true,alpha:true});
  renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1,2));
  renderer.setClearColor(0x000000,0);
  renderer.outputEncoding = T.sRGBEncoding;
  renderer.toneMapping = T.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 0.95;
  viewport.prepend(renderer.domElement);
  renderer.domElement.setAttribute('aria-label','Drag to rotate the 3D carrier');
  renderer.domElement.tabIndex = 0;
  const scene = new T.Scene();
  const camera = new T.PerspectiveCamera(40,1,0.1,60);
  camera.position.set(3.3,2.6,3.4);
  const controls = new T.OrbitControls(camera,renderer.domElement);
  controls.enableDamping = true; controls.dampingFactor = 0.07;
  controls.enablePan = false; controls.minDistance = 3.7; controls.maxDistance = 12;
  controls.autoRotateSpeed = 0.6; controls.target.set(0,0,0); controls.saveState();
  scene.add(new T.HemisphereLight(0xc3e8ff,0x172139,0.8));
  const key = new T.DirectionalLight(0xfff1df,1.0); key.position.set(3,6,5);scene.add(key);
  const rim = new T.DirectionalLight(0x78afee,0.45);rim.position.set(-4,2,-3);scene.add(rim);
  const grid = new T.GridHelper(7,28,0x436078,0x25374a);
  grid.position.y = -1.24;grid.material.transparent=true;grid.material.opacity=0.21;scene.add(grid);

  const surface = new T.Group(),primal = new T.Group(),dual = new T.Group(),guides = new T.Group();
  scene.add(surface,primal,dual,guides);
  const dualSurfacePaths=new T.Group(),dualStraightPaths=new T.Group();
  dual.add(dualSurfacePaths,dualStraightPaths);
  const points = {
    A:new T.Vector3(1,1,1),B:new T.Vector3(1,-1,-1),
    C:new T.Vector3(-1,1,-1),D:new T.Vector3(-1,-1,1)
  };
  const parents = [
    {id:'ABC',cycle:['A','B','C'],color:0x65d5c8},
    {id:'ABD',cycle:['A','D','B'],color:0x819df1},
    {id:'ACD',cycle:['A','C','D'],color:0xdeb674},
    {id:'BCD',cycle:['B','D','C'],color:0xd28faa}
  ];
  const triangles=[],edgeMap=new Map(),faceMeshes=[],labels=[],movers=[];
  const sphereGeometry = new T.SphereGeometry(1,16,12);
  const Y = new T.Vector3(0,1,0);
  const edgeKey = (a,b) => [a,b].sort().join('|');
  const average = list => list.reduce((sum,v)=>sum.add(v),new T.Vector3()).multiplyScalar(1/list.length);
  function ball(position,radius,material,group) {
    const mesh=new T.Mesh(sphereGeometry,material);mesh.position.copy(position);mesh.scale.setScalar(radius);group.add(mesh);return mesh;
  }
  function segment(a,b,radius,material,group) {
    const direction=b.clone().sub(a);
    const mesh=new T.Mesh(new T.CylinderGeometry(radius,radius,direction.length(),8),material);
    mesh.position.copy(a).add(b).multiplyScalar(0.5);
    mesh.quaternion.setFromUnitVectors(Y,direction.normalize());group.add(mesh);return mesh;
  }
  function arrow(a,b,color,group) {
    const direction=b.clone().sub(a).normalize();
    const material=new T.MeshBasicMaterial({color,transparent:true,opacity:0.65});
    const cone=new T.Mesh(new T.ConeGeometry(0.019,0.052,9),material);
    cone.position.copy(a).lerp(b,0.64);cone.quaternion.setFromUnitVectors(Y,direction);group.add(cone);
  }
  for (const parent of parents) {
    const f='F_'+parent.id;
    points[f]=average(parent.cycle.map(k=>points[k]));
    parent.normal=points[f].clone().normalize();
    for(let i=0;i<3;i++) {
      const a=parent.cycle[i],b=parent.cycle[(i+1)%3];
      const vertices=[f,a,b],p=vertices.map(k=>points[k]);
      const normal=p[1].clone().sub(p[0]).cross(p[2].clone().sub(p[0])).normalize();
      const centre=average(p);
      const material=new T.MeshStandardMaterial({color:parent.color,side:T.DoubleSide,
        transparent:true,opacity:0.92,roughness:0.65,metalness:0.04,
        emissive:parent.color,emissiveIntensity:0.08,depthWrite:false});
      material.color.convertSRGBToLinear().multiplyScalar([1,0.91,0.82][i]);
      material.emissive.convertSRGBToLinear();
      const geometry=new T.BufferGeometry();
      geometry.setAttribute('position',new T.Float32BufferAttribute(p.flatMap(v=>v.clone().sub(centre).toArray()),3));
      geometry.computeVertexNormals();
      const mesh=new T.Mesh(geometry,material);mesh.position.copy(centre);
      mesh.userData.triangle=a+b;surface.add(mesh);faceMeshes.push(mesh);
      const triangle={id:a+b,parent:parent.id,vertices,normal,centre,mesh,
        dualPosition:centre.clone().addScaledVector(normal,0.065),color:parent.color};
      triangles.push(triangle);
      for(let j=0;j<3;j++) {
        const from=vertices[j],to=vertices[(j+1)%3],key=edgeKey(from,to);
        if(!edgeMap.has(key)) edgeMap.set(key,{ends:[from,to].sort(),owners:[],arrows:[]});
        edgeMap.get(key).owners.push(triangle);edgeMap.get(key).arrows.push([from,to]);
      }
      // Inset paths keep orientation marks distinct from the shared structural edges.
      const path=p.map(v=>centre.clone().lerp(v,0.72).addScaledVector(normal,0.021));
      const loopGeometry=new T.BufferGeometry().setFromPoints([...path,path[0]]);
      guides.add(new T.Line(loopGeometry,new T.LineBasicMaterial({color:parent.color,transparent:true,opacity:0.34})));
      for(let j=0;j<3;j++) arrow(path[j],path[(j+1)%3],parent.color,guides);
      const markerMaterial=new T.MeshBasicMaterial({color:0xeafff9});
      const marker=ball(path[0],0.023,markerMaterial,guides);
      movers.push({marker,path});
      const option=document.createElement('option');option.value=triangle.id;
      option.textContent=triangle.id+' · ('+vertices.join(', ')+')';$('triangle').append(option);
    }
  }
  const outsideMaterial=new T.MeshStandardMaterial({color:0xe7dfd0,roughness:0.35,metalness:0.15});
  const insideMaterial=new T.MeshStandardMaterial({color:0xa4d4e4,roughness:0.45,transparent:true,opacity:0.70});
  const dualMaterial=new T.MeshBasicMaterial({color:0xbedff2,transparent:true,opacity:0.80});
  for(const edge of edgeMap.values()) {
    if(edge.owners.length!==2) throw new Error('Unpaired geometric edge '+edge.ends.join(','));
    const [a,b]=edge.ends;
    const outer=!a.startsWith('F_')&&!b.startsWith('F_');
    segment(points[a],points[b],outer?0.012:0.0065,outer?outsideMaterial:insideMaterial,primal);
    const [t,u]=edge.owners;
    const raised=average([points[a],points[b]]).addScaledVector(t.normal.clone().add(u.normal).normalize(),0.065);
    segment(t.dualPosition,raised,0.006,dualMaterial,dualSurfacePaths);
    segment(raised,u.dualPosition,0.006,dualMaterial,dualSurfacePaths);
    segment(t.dualPosition,u.dualPosition,0.007,dualMaterial,dualStraightPaths);
  }
  for(const [name,p] of Object.entries(points)) {
    const isCentre=name.startsWith('F_');
    ball(p,isCentre?0.033:0.050,isCentre?insideMaterial:outsideMaterial,primal);
    const el=document.createElement('div');el.className='vertex-label'+(isCentre?' centre':'');
    el.textContent=name;viewport.append(el);
    labels.push({name,el,position:p.clone().addScaledVector(p.clone().normalize(),isCentre?0.09:0.15),
      normal:isCentre?p.clone().normalize():null});
  }
  for(const triangle of triangles) {
    const node=ball(triangle.dualPosition,0.048,new T.MeshStandardMaterial({color:triangle.color,
      emissive:triangle.color,emissiveIntensity:0.3,roughness:0.3}),dual);
    node.material.color.convertSRGBToLinear();node.material.emissive.convertSRGBToLinear();
    node.userData.triangle=triangle.id;triangle.dualNode=node;
    const el=document.createElement('div');el.className='vertex-label agent';el.textContent=triangle.id;viewport.append(el);
    labels.push({name:triangle.id,el,isAgent:true,position:triangle.dualPosition.clone().addScaledVector(triangle.normal,0.12)});
  }

  let mode='surface',selected='',phase=0;
  let playing=!window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  $('play').textContent=playing?'Pause guides':'Play guides';
  let last=null,disposed=false;
  function selectTriangle(id) {
    selected=id;$('triangle').value=id;
    const t=triangles.find(t=>t.id===id);
    $('packets').textContent=t?t.vertices.map((a,i)=>'('+a+', '+t.vertices[(i+1)%3]+')').join('\n'):
      'Select a face triangle\nto inspect its three\nendpoint pairs.';
    $('selected-note').textContent=t?'Triangle '+id+' · parent face '+t.parent:
      'Corner vertices are ivory; face-centre vertices are blue.';
    for(const triangle of triangles) {
      triangle.mesh.material.emissiveIntensity=triangle.id===id?0.42:0.08;
      triangle.dualNode.scale.setScalar(triangle.id===id?0.066:0.048);
    }
  }
  function setMode(value) {
    mode=value;surface.visible=value!=='dual';primal.visible=value!=='dual';dual.visible=value!=='surface';
    dualSurfacePaths.visible=value==='both';dualStraightPaths.visible=value==='dual';
    guides.visible=value!=='dual'&&$('phase-guides').checked;
    for(const b of document.querySelectorAll('[data-view]')) b.setAttribute('aria-pressed',String(b.dataset.view===value));
    $('view-title').textContent={surface:'Triangulated surface',both:'Surface + shared-edge dual',dual:'Twelve-agent interaction net'}[value];
    $('view-detail').textContent=value==='dual'?'One node per triangle · one wire per shared edge':'Four faces, each divided into three triangles';
    const stats=value==='dual'?['12','agents','18','wires','4 + 4','3- and 6-cycles']:['12','triangles','8','shared vertices','18','shared edges'];
    for(let i=0;i<3;i++) {const suffix='abc'[i];$('count-'+suffix).textContent=stats[2*i];$('label-'+suffix).textContent=stats[2*i+1];}
  }
  for(const b of document.querySelectorAll('[data-view]'))b.addEventListener('click',()=>setMode(b.dataset.view));
  $('triangle').addEventListener('change',e=>selectTriangle(e.target.value));
  $('phase-guides').addEventListener('change',()=>setMode(mode));
  $('auto-rotate').addEventListener('change',()=>{controls.autoRotate=$('auto-rotate').checked;});
  $('opacity').addEventListener('input',()=>{for(const t of triangles){
    t.mesh.material.opacity=Number($('opacity').value);t.mesh.material.depthWrite=t.mesh.material.opacity>=0.99;
  }});
  $('play').addEventListener('click',()=>{playing=!playing;$('play').textContent=playing?'Pause guides':'Play guides';});
  $('reset').addEventListener('click',()=>{
    controls.autoRotate=false;$('auto-rotate').checked=false;
    controls.enableDamping=false;controls.update();controls.reset();controls.enableDamping=true;
  });
  renderer.domElement.addEventListener('keydown',event=>{
    if(event.key.toLowerCase()==='r')$('reset').click();
  });
  const raycaster=new T.Raycaster(),pointer=new T.Vector2();let down=null;
  renderer.domElement.addEventListener('pointerdown',e=>{down=[e.clientX,e.clientY];});
  renderer.domElement.addEventListener('pointercancel',()=>{down=null;});
  renderer.domElement.addEventListener('pointerup',e=>{
    if(!down||Math.hypot(e.clientX-down[0],e.clientY-down[1])>5){down=null;return;}down=null;
    const rect=renderer.domElement.getBoundingClientRect();
    pointer.set(2*(e.clientX-rect.left)/rect.width-1,1-2*(e.clientY-rect.top)/rect.height);
    raycaster.setFromCamera(pointer,camera);
    const objects=mode==='dual'?triangles.map(t=>t.dualNode):faceMeshes;
    const hit=raycaster.intersectObjects(objects)[0];selectTriangle(hit?hit.object.userData.triangle:'');
  });
  const resize=new ResizeObserver(()=>{
    const w=viewport.clientWidth,h=viewport.clientHeight;
    renderer.setSize(w,h);camera.aspect=w/h;camera.fov=camera.aspect<1?47:40;camera.updateProjectionMatrix();
  });resize.observe(viewport);
  function updateLabels() {
    for(const label of labels) {
      const inView=label.isAgent?mode==='dual':mode!=='dual';
      const visible=$('labels').checked&&inView&&(!label.normal||label.normal.dot(camera.position.clone().sub(label.position))>0);
      label.el.hidden=!visible;
      if(visible) {
        const q=label.position.clone().project(camera);
        label.el.hidden=q.z>1||q.z<-1;
        label.el.style.left=((q.x+1)*0.5*viewport.clientWidth)+'px';
        label.el.style.top=((-q.y+1)*0.5*viewport.clientHeight)+'px';
      }
    }
  }
  function animate(now) {
    if(disposed)return;
    const dt=last===null?0:Math.max(0,Math.min((now-last)/1000,0.1));last=now;
    if(playing)phase=(phase+dt/7)%1;
    for(const {marker,path} of movers) {
      const t=phase*3,k=Math.floor(t)%3;
      marker.position.copy(path[k]).lerp(path[(k+1)%3],t-k);
    }
    controls.update();updateLabels();renderer.render(scene,camera);requestAnimationFrame(animate);
  }
  setMode('surface');requestAnimationFrame(animate);
  // Read-only inspection surface for offline browser regression checks.
  window.protonCarrier={snapshot:()=>({
    points:Object.fromEntries(Object.entries(points).map(([k,v])=>[k,v.toArray()])),
    triangles:triangles.map(t=>({id:t.id,parent:t.parent,vertices:t.vertices,
      renderedPositions:Array.from(t.mesh.geometry.attributes.position.array,(x,i)=>x+t.mesh.position.getComponent(i%3))})),
    edges:[...edgeMap.values()].map(e=>({vertices:e.ends,agents:e.owners.map(t=>t.id),arrows:e.arrows})),
    phase,playing,mode,selected,camera:camera.position.toArray(),renderCalls:renderer.info.render.calls,
    guidePositions:movers.map(m=>m.marker.position.toArray()),
    surfaceVisible:surface.visible,dualVisible:dual.visible,guidesVisible:guides.visible
  })};
  window.addEventListener('pagehide',()=>{
    disposed=true;resize.disconnect();controls.dispose();
    const geometries=new Set(),materials=new Set();
    scene.traverse(object=>{if(object.geometry)geometries.add(object.geometry);
      if(object.material)for(const m of Array.isArray(object.material)?object.material:[object.material])materials.add(m);});
    for(const g of geometries)g.dispose();for(const m of materials)m.dispose();renderer.dispose();
  },{once:true});
} catch(error) {
  const panel=$('error');panel.hidden=false;
  panel.textContent='The 3D view could not start. Enable WebGL and keep this folder beside paw-cycle/vendor. '+error.message;
  console.error(error);
}
})();
