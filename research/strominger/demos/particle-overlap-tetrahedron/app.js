import * as M from './model.mjs';
import {mountIdentity} from './identity.mjs?v=face-centers';
import * as Carrier from './carrier.mjs?v=face-centers';

try {
  const THREE=globalThis.THREE;
  if(!THREE?.OrbitControls) throw new Error('The local Three.js / OrbitControls files could not be loaded.');
  const $=selector=>document.querySelector(selector);
  const host=$('#scene');
  const renderer=new THREE.WebGLRenderer({antialias:true,alpha:true});
  renderer.setPixelRatio(Math.min(devicePixelRatio,2));
  renderer.setClearColor(0x091119,0);
  renderer.domElement.setAttribute('role','img');
  renderer.domElement.tabIndex=0;
  host.prepend(renderer.domElement);
  const scene=new THREE.Scene();
  const camera=new THREE.OrthographicCamera(-3,3,2.25,-2.25,.03,100);
  function createOrbit() {
    const controls=new THREE.OrbitControls(camera,renderer.domElement);
    controls.enableDamping=true;controls.dampingFactor=.075;controls.minZoom=.4;controls.maxZoom=3;
    return controls;
  }
  let orbit=createOrbit();
  scene.add(new THREE.HemisphereLight(0xdaedff,0x17222d,1.3));
  const light=new THREE.DirectionalLight(0xffffff,1.1);light.position.set(3,5,6);scene.add(light);
  const root=new THREE.Group();scene.add(root);
  const requested=new URL(location.href).searchParams.get('view');
  const initialView=Object.hasOwn(M.views,requested)?requested:'lattice';
  const state={view:initialView,electronTrial:new URL(location.href).searchParams.get('electron')==='m2',geometry:initialView==='lattice'&&new URL(location.href).searchParams.get('geometry')!=='chart'?'carrier':'chart',projection:'orthographic',cell:'none',route:'all',selectedPoint:null,angle:initialView==='pentachoron'?M.pentachoronProjectionRange.default:35,faces:true,context:initialView!=='barycenter',rays:false,progress:0,playing:false};
  const identity=mountIdentity({THREE,scene,host,getState:()=>state,onRoute:id=>selectRoute(id)});
  const isCarrier=()=>state.geometry==='carrier';
  const isTrial=()=>isCarrier()&&state.electronTrial;
  const carrierModel=()=>isTrial()?Carrier.trial:Carrier;
  const activeRoutes=()=>M.routes.filter(r=>!isCarrier()||carrierModel().bodies.some(b=>b.id===r.id));
  const isLattice=()=>!isCarrier()&&M.isLatticeView(state.view);
  const viewMeta=()=>isCarrier()?carrierModel().meta:state.view==='barycenter'?{...M.views.barycenter,description:'Four vertices lie on a tetrahedral facet; C₂ is the pentachoron barycenter, distinct from its fifth vertex V₄.'}:M.views[state.view];
  const labels=new Map();
  let faceMeshes=[],nodeMeshes=[],routeObjects=[],contextGroup,raysGroup,frameCount=0,lastTick=0;
  const coordinates=()=>isCarrier()?carrierModel().points:M.coordinatesFor(state.view);
  const display=p=>new THREE.Vector3(...(isCarrier()?p:M.displayPoint(p,state.view,state.angle)));
  const V=name=>display(coordinates()[name]);
  const axisPoints={X:[1.72,0,0],Y:[0,1.72,0],Z:[0,0,1.72],NX:[-1.72,0,0],NY:[0,-1.72,0],NZ:[0,0,-1.72]};
  const axisPositions=()=>state.view==='hex'
    ?Object.fromEntries(Object.entries(M.tetraAxisDirections).map(([n,p])=>[n,p.map(v=>v*2.58)]))
    :Object.fromEntries(['X','Y','Z'].map(n=>[n,axisPoints[n]]));
  const cursor=new THREE.Mesh(new THREE.SphereGeometry(.047,20,14),new THREE.MeshBasicMaterial({color:0xd8fff0,depthTest:false}));
  cursor.renderOrder=20;scene.add(cursor);
  const halo=new THREE.Mesh(new THREE.SphereGeometry(.087,20,14),new THREE.MeshBasicMaterial({color:0xa4efd0,transparent:true,opacity:.13,depthWrite:false}));
  halo.renderOrder=19;scene.add(halo);

  for(const name of [...M.carriers,'M2','V4','O',...Object.keys(axisPoints)]) {
    const axis=Object.hasOwn(axisPoints,name),decorative=axis||name==='O';
    const el=document.createElement(decorative?'span':'button');
    el.className='point-label';el.dataset.point=name;el.dataset.role=axis?'axis':name.startsWith('M')?'M':'C';
    el.textContent=axis?name.toLowerCase():name==='M2'?'M₂':M.names[name]||'facet center';
    if(!decorative){el.type='button';el.addEventListener('click',()=>selectPoint(name));}
    host.append(el);labels.set(name,el);
  }
  const carrierLabels=Carrier.trial.bodies.map(body=>{const el=document.createElement('span');el.className='carrier-label';el.textContent=body.name;host.append(el);return {body,el};});
  for(const cell of M.simplexCells) {
    const option=document.createElement('option');option.value=cell.id;
    option.textContent=cell.nodes.map(n=>M.names[n]).join(' ')+' · omit '+M.names[cell.omitted];$('#cell').append(option);
  }
  function line(a,b,color=0x64869b,opacity=.45,dashed=true) {
    const material=dashed?new THREE.LineDashedMaterial({color,transparent:true,opacity,dashSize:.055,gapSize:.04})
      :new THREE.LineBasicMaterial({color,transparent:true,opacity});
    const obj=new THREE.Line(new THREE.BufferGeometry().setFromPoints([a,b]),material);
    if(dashed)obj.computeLineDistances();return obj;
  }
  function face(names,color,opacity) {
    const geometry=new THREE.BufferGeometry().setFromPoints(names.map(V));geometry.setIndex([0,1,2]);geometry.computeVertexNormals();
    return new THREE.Mesh(geometry,new THREE.MeshBasicMaterial({color,side:THREE.DoubleSide,transparent:true,opacity,depthWrite:false,polygonOffset:true,polygonOffsetFactor:-1,polygonOffsetUnits:-1}));
  }
  function arrow(a,b,route) {
    const start=V(a),end=V(b),direction=end.clone().sub(start).normalize();
    const ordered=[a,b].sort(),key=ordered.join('|');
    const canonical=V(ordered[1]).sub(V(ordered[0])).normalize();
    const normal=new THREE.Vector3().crossVectors(canonical,new THREE.Vector3(0,1,0));
    if(normal.lengthSq()<.01)normal.crossVectors(canonical,new THREE.Vector3(0,0,1));normal.normalize();
    // Two display lanes make equal and reversed shared directions independently legible.
    const offset=key==='C1|M0'?(route.id==='proton'?-.10:.10):key==='C1|M1'?(route.id==='neutron'?-.10:.10):0;
    const middle=start.clone().add(end).multiplyScalar(.5).addScaledVector(normal,offset);
    const curve=new THREE.QuadraticBezierCurve3(start.clone().addScaledVector(direction,.075),middle,end.clone().addScaledVector(direction,-.075));
    const mat=new THREE.MeshBasicMaterial({color:route.color,transparent:true,opacity:.95,depthWrite:false});
    const tube=new THREE.Mesh(new THREE.TubeGeometry(curve,24,.013,7,false),mat);
    const tip=new THREE.Mesh(new THREE.ConeGeometry(.044,.13,10),mat);
    tip.position.copy(curve.getPoint(.64));tip.quaternion.setFromUnitVectors(new THREE.Vector3(0,1,0),curve.getTangent(.64).normalize());
    const group=new THREE.Group();group.add(tube,tip);return group;
  }
  function disposeRoot() {
    const geometries=new Set(),materials=new Set();
    root.traverse(o=>{if(o.geometry)geometries.add(o.geometry);if(o.material)(Array.isArray(o.material)?o.material:[o.material]).forEach(m=>materials.add(m));});
    geometries.forEach(g=>g.dispose());materials.forEach(m=>m.dispose());root.clear();
  }
  function tetrahedralGrid() {
    const grid=M.boundedTetrahedralGrid(4),points=[],colors=[],base=new THREE.Color(0x8babbd);
    // One geometry contains every edge, including the CMC-plane edges.
    for(const edge of grid.edges) {
      const layer=Math.max(...edge.map(i=>Math.abs(grid.vertices[i][1])));
      const fade=layer===0?1:.28/layer**1.6;
      for(const i of edge) {
        points.push(new THREE.Vector3(...grid.vertices[i]));
        colors.push(base.r*fade,base.g*fade,base.b*fade);
      }
    }
    const geometry=new THREE.BufferGeometry().setFromPoints(points);
    geometry.setAttribute('color',new THREE.Float32BufferAttribute(colors,3));
    const mesh=new THREE.LineSegments(geometry,new THREE.LineBasicMaterial({vertexColors:true,transparent:true,opacity:.24,depthWrite:false}));
    contextGroup.add(mesh);
    const positions=geometry.getAttribute('position'),bounds=new THREE.Box3().setFromObject(mesh);
    let maxRadius=0;
    for(let i=0;i<positions.count;i++)maxRadius=Math.max(maxRadius,Math.hypot(positions.getX(i),positions.getY(i),positions.getZ(i)));
    const matches=(i,p)=>Math.hypot(positions.getX(i)-p[0],positions.getY(i)-p[1],positions.getZ(i)-p[2])<1e-6;
    const routeEdgesPresent=M.routes.every(route=>route.nodes.every((n,i)=>{
      const a=M.hex[n],b=M.hex[route.nodes[(i+1)%3]];
      for(let j=0;j<positions.count;j+=2)if((matches(j,a)&&matches(j+1,b))||(matches(j,b)&&matches(j+1,a)))return true;
      return false;
    }));
    contextGroup.userData.tetraGrid={radius:grid.radius,center:grid.center,maxRadius,
      latticeObjectCount:contextGroup.children.filter(o=>o.isLineSegments).length,
      tetrahedronCount:grid.tetrahedra.length,vertexCount:grid.vertices.length,edgeCount:grid.edges.length,
      segmentCount:positions.count/2,routeEdgesPresent,bounds:[bounds.min.toArray(),bounds.max.toArray()]};
  }
  function latticeGrid() {
    const vec=p=>new THREE.Vector3(...p);
    if(state.view==='hex')tetrahedralGrid();
    else {
      for(const z of [0,1])for(const [a,b] of [
        [[-1.5,0,z],[1.5,0,z]],[[0,-1.5,z],[0,1.5,z]],
      ])contextGroup.add(line(vec(a),vec(b),0x7e9caf,.15,false));
      for(const i of [-1,0,1])for(const [a,b] of [
        [[i,0,0],[i,0,1.5]],[[0,i,0],[0,i,1.5]],
        [[-1.5,i,0],[1.5,i,0]],[[i,-1.5,0],[i,1.5,0]],
      ])contextGroup.add(line(vec(a),vec(b),0x7e9caf,.10,false));
    }
    Object.entries(axisPositions()).forEach(([name,p])=>{
      const length=vec(p).length()-.12,direction=vec(p).normalize();
      const color=[0xe7a0a0,0xa4d3ae,0x9fbee5][['X','Y','Z'].indexOf(name.replace(/^N/,''))];
      const arrow=new THREE.ArrowHelper(direction,new THREE.Vector3(),length,color,.09,.045);
      arrow.userData.axis=name;contextGroup.add(arrow);
    });
  }
  function buildCarriers() {
    const indices=[0,2,1,0,1,3,0,3,2,1,2,3];
    for(const body of carrierModel().bodies) {
      const geometry=new THREE.BufferGeometry().setFromPoints(body.nodes.map(V));geometry.setIndex(indices);geometry.computeVertexNormals();
      const mesh=new THREE.Mesh(geometry,new THREE.MeshPhongMaterial({color:body.color,transparent:true,opacity:.23,side:THREE.DoubleSide,depthWrite:false,flatShading:true,shininess:28}));
      mesh.userData.carrier=body.id;root.add(mesh);
    }
    for(const [a,b] of carrierModel().edges) {
      const shared=carrierModel().sharedFaces.some(f=>f.includes(a)&&f.includes(b));
      const mesh=new THREE.Mesh(new THREE.TubeGeometry(new THREE.LineCurve3(V(a),V(b)),1,.014,8,false),new THREE.MeshBasicMaterial({color:shared?0xe9df9c:0xa9cddd,transparent:true,opacity:.9}));
      mesh.userData.carrierEdge=[a,b];contextGroup.add(mesh);
    }
  }
  function rebuild() {
    disposeRoot();faceMeshes=[];nodeMeshes=[];routeObjects=[];
    contextGroup=new THREE.Group();raysGroup=new THREE.Group();root.add(contextGroup,raysGroup);
    if(isCarrier())buildCarriers();
    else if(isLattice())latticeGrid();
    if(state.view==='pentachoron') {
      for(const [a,b] of M.simplexEdges)contextGroup.add(line(V(a),V(b),0x8aabba,.38));
      const cell=M.simplexCells.find(c=>c.id===state.cell);
      if(cell) {
        for(const f of M.simplexFaces.filter(f=>f.every(n=>cell.nodes.includes(n))))root.add(face(f,0xb6d9ed,.045));
        for(const [a,b] of M.simplexEdges.filter(e=>e.every(n=>cell.nodes.includes(n))))root.add(line(V(a),V(b),0xb6d9ed,.72));
      }
    }
    if(state.view==='barycenter') {
      for(const f of M.facetFaces)root.add(face(f,0x8cb6cd,.018));
      for(const [a,b] of M.facetEdges)root.add(line(V(a),V(b),0x7b9db2,.48));
      for(const a of M.facet)contextGroup.add(line(V(a),V('V4'),0x6d899b,.30));
      contextGroup.add(line(new THREE.Vector3(),V('V4'),0xa4efd0,.5));
      for(const a of M.facet)raysGroup.add(line(V(a),V('C2'),0xa4efd0,.26));
      contextGroup.add(new THREE.Mesh(new THREE.SphereGeometry(.025,12,8),new THREE.MeshBasicMaterial({color:0x7a95a5})));
    }
    Object.keys(coordinates()).forEach(name=>{
      const endpoint=name==='C2',isM=name.startsWith('M');
      const mesh=new THREE.Mesh(new THREE.SphereGeometry(endpoint ? .075 : name==='V4' ? .045 : .062,24,16),new THREE.MeshPhongMaterial({color:endpoint?0xa4efd0:isM?0xffd6a1:name==='V4'?0x69899d:0xe4f1fa,shininess:45}));
      mesh.position.copy(V(name));mesh.userData.point=name;nodeMeshes.push(mesh);
      (name==='V4'?contextGroup:root).add(mesh);
    });
    activeRoutes().forEach((route,index)=>{
      const mesh=face(route.nodes,route.color,.15);mesh.userData.route=route.id;mesh.renderOrder=2+index;root.add(mesh);faceMeshes.push(mesh);
      const closing=line(V(route.nodes[0]),V(route.nodes[2]),route.color,.40);root.add(closing);
      const arrows=new THREE.Group();
      for(const [a,b] of M.directedEdges(route))arrows.add(arrow(a,b,route));
      root.add(arrows);routeObjects.push({route,mesh,closing,arrows});
    });
    styleSelection();updateCursor();
  }
  function styleSelection() {
    contextGroup.visible=state.context;raysGroup.visible=state.view==='barycenter'&&state.rays;
    for(const mesh of root.children.filter(o=>o.userData.carrier)) {
      const selected=state.route==='all'||state.route===mesh.userData.carrier;
      mesh.material.opacity=state.route==='all'?.23:selected?.34:.07;
    }
    for(const {route,mesh,closing,arrows} of routeObjects) {
      const selected=state.route==='all'||state.route===route.id;
      mesh.visible=state.faces;mesh.material.opacity=selected ? (state.route==='all' ? .16 : .29) : .025;
      closing.material.opacity=selected ? .46 : .08;
      arrows.traverse(o=>{if(o.material)o.material.opacity=selected ? .95 : .12;});
    }
    for(const [name,el] of labels) {
      el.classList.toggle('active',name===state.selectedPoint);
      const axis=Object.hasOwn(axisPoints,name);
      el.hidden=name==='M2'?!isTrial():axis?!isLattice()||!state.context||!Object.hasOwn(axisPositions(),name):(name==='V4'||name==='O')?state.view!=='barycenter'||!state.context:false;
      if(name==='C2')el.setAttribute('aria-label',viewMeta().centerTitle);
    }
    document.querySelectorAll('[data-route]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.route===state.route)));
    $('#view-badge').textContent=state.route==='all'?'Shared configuration':M.routes.find(r=>r.id===state.route).name+' window';
    identity.refresh();
  }
  function showDetail(title,text,formula,extra) {
    $('#detail-title').textContent=title;$('#detail-text').textContent=text;
    $('#detail-formula').textContent=formula;$('#detail-extra').textContent=extra;
  }
  function refreshDetail() {
    const name=state.selectedPoint;
    if(isTrial()&&name==='M2')showDetail('M₂ · electron continuation vertex','M₂ is the reflection of M₀ across M₁ C₁ C₂. It is distinct from M₀ and extends the five-vertex geometry.','E: M₁ C₁ C₂ [M₂]','M₂ = (−31/9, −1/9, −1/9). It is the electron carrier’s fourth vertex, not part of the active MCC face.');
    else if(isTrial()&&name==='C1')showDetail('C₁ · shared identity','The same C₁ belongs to the active proton, neutron and electron windows. The electron traverses M₁ → C₁, reversing the neutron’s C₁ → M₁.','CMC[M] → MCM[C] → MCC[M]','P/N share M₀ C₁ M₁; N/E share M₁ C₁ C₂.');
    else if(isTrial()&&!name&&state.route==='all')showDetail('Three consecutive carriers','The electron carrier joins the neutron across the MCC face, with M₂ as its fourth vertex.','P: C₀ M₀ C₁ [M₁] · N: M₀ C₁ M₁ [C₂] · E: M₁ C₁ C₂ [M₂]','P/N share M₀ C₁ M₁; N/E share M₁ C₁ C₂. Brackets mark continuation vertices.');
    else if(isCarrier()&&name==='C1')showDetail('C₁ · shared face vertex','C₁ belongs to both active windows and both tetrahedral carriers.','P: C₀ M₀ C₁ [M₁] · N: M₀ C₁ M₁ [C₂]','The shared face is M₀ C₁ M₁.');
    else if(isCarrier()&&name==='M1')showDetail('M₁ · proton continuation vertex','The bracketed fourth vertex of the proton also belongs to the neutron’s active MCM face.','CMC[M] → MCM[C]','The neutron retains C₂ as its own fourth vertex.');
    else if(isCarrier()&&!name&&state.route==='all')showDetail('Two consecutive carriers','The proton’s continuation face is the neutron’s active face. The whole M₀ C₁ M₁ face is shared.','C₀ M₀ C₁ [M₁] → M₀ C₁ M₁ [C₂]','C₂ is the neutron continuation vertex. This view assigns only proton and neutron carriers.');
    else if(name==='C1')showDetail('C₁ · the shared carrier','All three windows meet here. The directed walk visits this same point twice.','C₁ → M₁ → C₁','Occurrences 3 and 5 of the six-position walk share one geometric vertex.');
    else if(name==='M1')showDetail('M₁ · the returning excursion','The neutron window reaches M₁; the electron window traverses the shared edge back to C₁.','C₁ ⇄ M₁','The two C occurrences surrounding M₁ are both C₁.');
    else if(name==='C2'&&isCarrier())showDetail(Carrier.meta.centerTitle,'This is the retained fifth source vertex, unfolded across the shared MCM face to make the second tetrahedral carrier volumetric in3D.','C₂(unfolded) = (−5/3, −5/3, −5/3)','Its original source remains (0,0,0,√5). This is a facet-wise isometry, not one global projection of the pentachoron.');
    else if(name==='C2') {
      const meta=viewMeta();
      showDetail(meta.centerTitle,state.view==='pentachoron'?'C₂ is the fifth original vertex. The electron is an original triangular face, just like the other two windows.':isLattice()?'The electron window descends from M₁ to the C layer at C₁, then advances along the realization axis to C₂.':'The radial triangle ends here. This is the first carrier of the next series.',state.view==='barycenter'?'b = (0, 0, 0, √5 / 5)':state.view==='pentachoron'?'C₂ = (0, 0, 0, √5)':'C₂ = (1, 0, 0)',state.view==='pentachoron'?'Its displayed position depends on the orthogonal projection; it remains an original 4D vertex.':meta.note);
    }
    else if(name==='V4')showDetail('V₄ · the fifth outer vertex','Together with the four facet vertices, V₄ completes the regular pentachoron.','V₄ = (0, 0, 0, √5)','The center lies one fifth of the way from the facet center toward V₄.');
    else if(name)showDetail(M.names[name]+' · '+(isLattice()?'lattice site':'vertex'),name==='C0'?'The proton window begins here.':'This point belongs to both the proton and neutron windows.',M.names[name]+' = ('+coordinates()[name].map(v=>Number(v.toFixed(3))).join(', ')+')',name==='M0'?'The oriented segment M₀ → C₁ is shared by both windows.':viewMeta().footer);
    else if(state.route==='all')showDetail('The shared edges','Proton and neutron share M₀ → C₁. Neutron and electron traverse C₁ ⇄ M₁ in opposite directions.','C₁ → M₁ → C₁','Two occurrences of the same C₁ surround M₁.');
    else {
      const r=M.routes.find(r=>r.id===state.route);
      const body=carrierModel().bodies.find(b=>b.id===r.id);
      showDetail(r.name+(isCarrier()&&body?' carrier':' window'),isCarrier()?(body?'The first three vertices form the active window; the bracketed fourth vertex is retained for continuation.':'The MCC window continues on the neutron carrier; no separate fourth electron vertex is assigned here.'):M.routeDetail(r,state.view),isCarrier()&&body?body.notation:r.nodes.map(n=>M.names[n]).join(' → '),isCarrier()?(body?.id==='proton'?'Proton: C₀ M₀ C₁ [M₁]. Its continuation face is the neutron’s active MCM face.':body?.id==='neutron'?'Neutron: M₀ C₁ M₁ [C₂]. Its fourth vertex is the original retained C₂, not C₀.':'Electron: M₁ C₁ C₂ [M₂]. M₂ completes the tetrahedron across the neutron’s MCC face.'):state.view==='pentachoron'?'All three vertices belong to the original regular 4-simplex.':'The dashed third edge records the two-step composite.');
    }
  }
  function updateViewUI() {
    const meta=viewMeta();
    $('#carrier-note').hidden=!isCarrier();
    document.querySelectorAll('[data-route="electron"],[data-identity-route="electron"]').forEach(el=>el.hidden=isCarrier()&&!isTrial());
    $('#electron-carrier-note').hidden=!isTrial();$('#pn-only-note').hidden=isTrial();
    $('#carrier-sequence').textContent=isTrial()?'CMC[M] → MCM[C] → MCC[M]':'CMC[M] → MCM[C]';
    $('#electron-trial').setAttribute('aria-pressed',String(isTrial()));
    $('[data-route="electron"] code').textContent=isTrial()?'M₁ C₁ C₂ [M₂]':'M₁ → C₁ → C₂';
    $('.walk-panel').hidden=isCarrier();
    const overview=$('[data-route="all"]');overview.firstElementChild.textContent=isTrial()?'All three carriers':isCarrier()?'Both carriers':'All windows';overview.lastElementChild.textContent=isTrial()?'two shared faces':isCarrier()?'shared MCM face':'shared edges';
    $('[data-identity-route="all"]').textContent=isTrial()?'P/N/E overview':isCarrier()?'P/N overview':'Follow walk';
    $('.identity-panel > p.small').textContent=isCarrier()?'Select a carrier to see its active-face center and spectral mode. The center averages the three unbracketed vertices; it is not the center of the whole tetrahedron.':'Select a window to see its active-face center and spectral mode. “Follow walk” follows the selected path.';
    $('#carrier-mode').setAttribute('aria-pressed',String(isCarrier()&&!isTrial()));
    $('#page-title').textContent=meta.title;$('#view-description').textContent=meta.description;
    $('#projection-badge').textContent=meta.badge;
    $('#center-title').textContent=meta.centerTitle;$('#center-formula').textContent=meta.formula;$('#center-note').textContent=meta.note;
    $('#context-label').textContent=meta.context;$('#geometry-note').textContent=meta.footer;
    $('#scene-hint').textContent='Drag to orbit freely · scroll / pinch to zoom · select a triangle or label';
    $('#pentachoron-controls').hidden=state.view!=='pentachoron';
    $('#projection-controls').hidden=isCarrier()||isLattice();
    for(const name of Object.keys(axisPoints))labels.get(name).textContent=state.view==='hex'?M.tetraAxisLabels[name]:name.toLowerCase();
    const range=state.view==='pentachoron'?M.pentachoronProjectionRange:{min:-70,max:70};
    $('#projection').min=range.min;$('#projection').max=range.max;$('#projection').value=state.angle;
    $('#projection-value').textContent=state.angle+'°';
    $('#rays-control').hidden=state.view!=='barycenter';
    $('#context').checked=state.context;$('#rays').checked=state.rays;
    renderer.domElement.setAttribute('aria-label',meta.title+'. '+meta.description);
    document.querySelectorAll('[data-view]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.view===state.view&&!isCarrier())));
    const cell=M.simplexCells.find(c=>c.id===state.cell);
    $('#cell-note').textContent=!cell?'Five original 4D boundary cells; their orthogonal images can overlap.':'Original boundary cell on '+cell.nodes.map(n=>M.names[n]).join(', ')+'.';
    refreshDetail();
  }
  function selectView(view) {
    M.coordinatesFor(view);setPlaying(false);state.view=view;state.geometry='chart';state.electronTrial=false;state.context=view!=='barycenter';state.rays=false;
    if(state.selectedPoint==='M2')state.selectedPoint=null;
    state.angle=view==='pentachoron'?M.pentachoronProjectionRange.default:35;
    if(state.selectedPoint==='V4')state.selectedPoint=null;
    const url=new URL(location.href);url.searchParams.set('view',view);url.searchParams.set('geometry','chart');url.searchParams.delete('electron');history.replaceState(null,'',url);
    updateViewUI();rebuild();resetCamera();
  }
  function selectCarrier(electronTrial=false) {
    setPlaying(false);state.view='lattice';state.geometry='carrier';state.electronTrial=electronTrial===true;state.context=true;state.rays=false;state.route='all';state.progress=0;
    if(state.selectedPoint==='M2')state.selectedPoint=null;
    if(state.selectedPoint==='V4')state.selectedPoint=null;
    const url=new URL(location.href);url.searchParams.set('view','lattice');url.searchParams.set('geometry','carrier');if(state.electronTrial)url.searchParams.set('electron','m2');else url.searchParams.delete('electron');history.replaceState(null,'',url);
    updateViewUI();rebuild();resetCamera();
  }
  function selectRoute(id) {
    if(id!=='all'&&!activeRoutes().some(r=>r.id===id))throw new Error('Window is not part of this view');
    state.route=id;state.selectedPoint=null;setPlaying(false);
    if(id!=='all')setProgress(M.routes.find(r=>r.id===id).start);
    refreshDetail();styleSelection();
  }
  function selectPoint(name) {
    if(!Object.hasOwn(coordinates(),name))throw new Error('Point is absent from this view');
    state.selectedPoint=name;refreshDetail();styleSelection();
  }
  M.walk.forEach((name,index)=>{
    if(index){const arrow=document.createElement('span');arrow.className='walk-arrow';arrow.textContent='→';arrow.setAttribute('aria-hidden','true');$('#walk-nodes').append(arrow);}
    const button=document.createElement('button');button.type='button';button.className='walk-node';button.dataset.occurrence=index;button.dataset.carrier=name;button.textContent=M.names[name];
    button.setAttribute('aria-label',`${M.names[name]}, occurrence ${index+1} of 6`);
    button.addEventListener('click',()=>{setPlaying(false);setProgress(index);selectPoint(name);});$('#walk-nodes').append(button);
  });
  function updateCursor() {
    cursor.visible=halo.visible=!isCarrier();
    const p=display(M.pointOnWalk(state.progress,coordinates()));cursor.position.copy(p);halo.position.copy(p);
    const current=Math.min(5,Math.floor(state.progress+.00001));
    document.querySelectorAll('[data-occurrence]').forEach(button=>{
      button.classList.toggle('current',Number(button.dataset.occurrence)===current);
      button.classList.toggle('same-point',button.dataset.carrier==='C1'&&M.walk[current]==='C1');
    });
    const atVertex=Math.abs(state.progress-current)<.0001;
    const text=state.progress===5?'C₂ · next series starts here':atVertex?`${M.names[M.walk[current]]} · occurrence ${current+1} / 6`:`${M.names[M.walk[current]]} → ${M.names[M.walk[current+1]]} · segment ${current+1} / 5`;
    if($('#walk-location').textContent!==text)$('#walk-location').textContent=text;
    $('#progress').value=state.progress;
    identity.refresh();
  }
  function setProgress(value) {state.progress=Math.max(0,Math.min(5,Number(value)));updateCursor();}
  function setPlaying(value) {state.playing=value;$('#play').setAttribute('aria-pressed',String(value));$('#play').textContent=value?'Ⅱ Pause':'▶ Trace';}
  function resetCamera() {
    const up=isLattice()?new THREE.Vector3(0,0,1):new THREE.Vector3(0,1,0);
    if(!camera.up.equals(up)) {
      orbit.dispose();camera.up.copy(up);orbit=createOrbit();
    }
    const damping=orbit.enableDamping;orbit.enableDamping=false;
    orbit.minPolarAngle=0;orbit.maxPolarAngle=Math.PI;orbit.update();
    if(isCarrier()){camera.position.set(5,2,-4.5);orbit.target.set(-1/3,-1/3,-1/3);}
    else if(isLattice()){
      camera.position.set(-3.6,-5.2,1.8);orbit.target.set(0,state.view==='hex'?0:-.3,state.view==='hex'?0:.5);
    } else {camera.position.set(2.2,1.2,5.5);orbit.target.set(0,-.08,0);}
    camera.zoom=1;resize();
    orbit.update();orbit.enableDamping=damping;
  }
  const pixelOffsets={C0:[0,-24],M0:[0,26],C1:[0,-25],M1:[0,26],C2:[0,-27],M2:[0,-25],V4:[0,25],O:[0,-16],X:[8,0],Y:[0,-12],Z:[0,12],NX:[-8,0],NY:[14,22],NZ:[0,-12]};
  function positionLabels() {
    const width=host.clientWidth,height=host.clientHeight;
    for(const [name,el] of labels) {
      if(el.hidden)continue;
      const point=name==='O'?new THREE.Vector3():axisPoints[name]?new THREE.Vector3(...axisPositions()[name]):V(name);
      const p=point.project(camera);
      const offset=isLattice()&&M.carriers.includes(name)?[state.view==='hex'?{C0:-10,M0:-10,C1:0,M1:10,C2:10}[name]:0,name.startsWith('M')?-26:26]:pixelOffsets[name];
      const x=(p.x*.5+.5)*width+offset[0],y=(-p.y*.5+.5)*height+offset[1];
      el.style.left=`${x}px`;el.style.top=`${y}px`;el.style.visibility=p.z>-1&&p.z<1&&x>20&&x<width-20&&y>45&&y<height-30?'visible':'hidden';
    }
    for(const {body,el} of carrierLabels) {
      el.hidden=!isCarrier()||!carrierModel().bodies.some(b=>b.id===body.id);if(el.hidden)continue;
      const center=body.nodes.map(n=>coordinates()[n]).reduce((a,p)=>a.map((x,i)=>x+p[i]/4),[0,0,0]);
      const p=new THREE.Vector3(...center).project(camera);el.style.left=((p.x*.5+.5)*width+25)+'px';el.style.top=((-p.y*.5+.5)*height+(body.id==='electron'?-18:12))+'px';
    }
    identity.positionLabels(camera);
  }
  function resize() {
    const w=host.clientWidth,h=host.clientHeight,aspect=w/h;
    const height=Math.max(isCarrier()?6.3:state.view==='hex'?8.8:isLattice()?3.7:4.5,(isCarrier()?6.0:state.view==='hex'?8.8:isLattice()?3.6:4.0)/aspect);
    renderer.setSize(w,h);camera.left=-height*aspect/2;camera.right=height*aspect/2;
    camera.top=height/2;camera.bottom=-height/2;camera.updateProjectionMatrix();positionLabels();
  }
  new ResizeObserver(resize).observe(host);
  $('#projection').addEventListener('input',event=>{
    const range=state.view==='pentachoron'?M.pentachoronProjectionRange:{min:-70,max:70};
    state.angle=Math.max(range.min,Math.min(range.max,Number(event.target.value)));
    $('#projection-value').textContent=state.angle+'°';rebuild();
  });
  $('#carrier-mode').addEventListener('click',()=>selectCarrier(false));
  $('#electron-trial').addEventListener('click',()=>selectCarrier(true));
  $('#cell').addEventListener('change',event=>{state.cell=event.target.value;updateViewUI();rebuild();});
  for(const key of ['faces','context','rays'])$('#'+key).addEventListener('change',event=>{state[key]=event.target.checked;styleSelection();});
  document.querySelectorAll('[data-view]').forEach(button=>button.addEventListener('click',()=>selectView(button.dataset.view)));
  document.querySelectorAll('[data-route]').forEach(button=>button.addEventListener('click',()=>selectRoute(button.dataset.route)));
  $('#progress').addEventListener('input',event=>{setPlaying(false);setProgress(event.target.value);});
  $('#play').addEventListener('click',()=>{if(state.progress>=5)setProgress(0);setPlaying(!state.playing);});
  $('#restart').addEventListener('click',()=>{setPlaying(false);setProgress(0);});
  $('#reset-view').addEventListener('click',resetCamera);
  const raycaster=new THREE.Raycaster(),pointer=new THREE.Vector2();let down=null;
  renderer.domElement.addEventListener('pointerdown',event=>{down=[event.clientX,event.clientY];});
  renderer.domElement.addEventListener('pointerup',event=>{
    if(!down||Math.hypot(event.clientX-down[0],event.clientY-down[1])>5)return;down=null;
    const box=renderer.domElement.getBoundingClientRect();pointer.set((event.clientX-box.left)/box.width*2-1,-(event.clientY-box.top)/box.height*2+1);raycaster.setFromCamera(pointer,camera);
    const node=raycaster.intersectObjects(nodeMeshes.filter(o=>o.userData.point!=='V4'||state.context))[0];
    if(node){selectPoint(node.object.userData.point);return;}
    if(state.faces){const hit=raycaster.intersectObjects(faceMeshes)[0];if(hit)selectRoute(hit.object.userData.route);}
  });
  document.addEventListener('visibilitychange',()=>{if(document.hidden)setPlaying(false);});
  function animate(t) {
    const dt=lastTick?Math.min(.05,(t-lastTick)/1000):0;lastTick=t;
    if(state.playing){setProgress(state.progress+dt*.9);if(state.progress>=5)setPlaying(false);}
    orbit.update();positionLabels();renderer.render(scene,camera);frameCount++;requestAnimationFrame(animate);
  }
  updateViewUI();rebuild();resetCamera();resize();$('#loading').hidden=true;requestAnimationFrame(animate);
  globalThis.ParticleOverlapViewer={selectView,selectCarrier,selectRoute,setProgress,selectPoint,
    projectWorld:point=>new THREE.Vector3(...point).project(camera).toArray(),snapshot:()=>({
    state:{...state},identity:identity.snapshot(),coordinates:coordinates(),originalPentachoron:M.pentachoron,points4D:M.points,barycenter4D:M.barycenter,walk:M.walk,routes:activeRoutes().map(r=>({id:r.id,nodes:r.nodes})),originalRoutes:M.routes.map(r=>({id:r.id,nodes:r.nodes})),
    cursor4D:M.pointOnWalk(state.progress,coordinates()),cursor3D:cursor.position.toArray(),camera:camera.position.toArray(),frameCount,
    cameraType:camera.type,cameraZoom:camera.zoom,cameraTarget:orbit.target.toArray(),cameraUp:camera.up.toArray(),projectionMatrix:camera.projectionMatrix.elements.slice(),
    orbitPolarLimits:[orbit.minPolarAngle,orbit.maxPolarAngle],latticeAxes:isCarrier()?null:state.view==='hex'?M.hexAxes:M.latticeAxes,
    hexBasis:state.view==='hex'?M.hexBasis:null,hexAxialCoordinates:state.view==='hex'?M.lattice:null,
    axisDirections:Object.fromEntries(contextGroup.children.filter(o=>o.userData.axis).map(o=>[o.userData.axis,new THREE.Vector3(0,1,0).applyQuaternion(o.quaternion).toArray()])),
    axisLabels:Object.fromEntries(Object.keys(isLattice()?axisPositions():{}).map(n=>[n,labels.get(n).textContent])),
    cameraFrustum:{left:camera.left,right:camera.right,top:camera.top,bottom:camera.bottom},viewport:[host.clientWidth,host.clientHeight],
    geometry:{renderedCarrierBodies:root.children.filter(o=>o.userData.carrier).map(o=>({id:o.userData.carrier,positions:Array.from(o.geometry.getAttribute('position').array),triangles:o.geometry.index.count/3})),carrierBodies:isCarrier()?carrierModel().bodies.map(b=>({id:b.id,nodes:b.nodes,window:b.window,continuation:b.continuation,notation:b.notation,volume:Math.abs(Carrier.orientedVolume(b.nodes,coordinates()))})):[],carrierEdges:isCarrier()?carrierModel().edges.length:0,sharedCarrierFace:isCarrier()?Carrier.sharedFace:null,sharedCarrierFaces:isCarrier()?carrierModel().sharedFaces:[],trialExtension:isTrial()?Carrier.trial.extension:null,pointCount:Object.keys(coordinates()).length,particleTriangleCount:routeObjects.length,facetEdgeCount:M.facetEdges.length,outerVertexCount:5,
      triangleGrid:contextGroup.userData.triangleGrid||null,tetraGrid:contextGroup.userData.tetraGrid||null,
      simplexEdgeCount:state.view==='pentachoron'?M.simplexEdges.length:0,simplexFaceCount:state.view==='pentachoron'?M.simplexFaces.length:0,simplexCellCount:state.view==='pentachoron'?M.simplexCells.length:0,
      cell:state.view==='pentachoron'?M.simplexCells.find(c=>c.id===state.cell)||null:null},
    projected:Object.fromEntries(Object.entries(coordinates()).map(([name,p])=>[name,isCarrier()?p:M.displayPoint(p,state.view,state.angle)])),
    webgl:renderer.getContext()!==null,renderCalls:renderer.info.render.calls,
  })};
} catch(error) {
  document.querySelector('#loading').hidden=true;
  const el=document.querySelector('#error');el.hidden=false;el.textContent=error.message;
  console.error(error);
}
