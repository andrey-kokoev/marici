/* Offline Three.js view of the checked paw-rotor-tetrahedron construction. */
(() => {
  'use strict';
  const $ = id => document.getElementById(id);
  const host = $('scene');
  function fail(message) { $('error').textContent = message; $('error').classList.remove('hidden'); $('play').disabled = true; }
  if (!window.THREE || !THREE.OrbitControls) { fail('The local Three.js files are missing. Keep the vendor folder beside index.html.'); return; }
  const T = THREE;
  let renderer;
  try { renderer = new T.WebGLRenderer({ antialias: true, alpha: true }); }
  catch (_) { fail('WebGL is unavailable. Try a browser with hardware acceleration enabled.'); return; }
  renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
  renderer.outputEncoding = T.sRGBEncoding;
  host.prepend(renderer.domElement);
  const scene = new T.Scene();
  const camera = new T.PerspectiveCamera(42, 1, .01, 100);
  camera.up.set(0, 0, 1);
  const controls = new T.OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true; controls.dampingFactor = .09;
  controls.minDistance = 1.6; controls.maxDistance = 12;
  function resetCamera() { camera.position.set(2.5, -3.3, 2.4); controls.target.set(0, .22, -.05); controls.update(); }
  resetCamera();
  scene.add(new T.HemisphereLight(0xe3efff, 0x263b56, 1.3));
  const light = new T.DirectionalLight(0xffffff, .8); light.position.set(3, -2, 5); scene.add(light);
  const grid = new T.GridHelper(7, 28, 0x31445c, 0x1c2b3d);
  grid.rotation.x = Math.PI / 2; grid.position.z = -1.12; grid.material.transparent = true; grid.material.opacity = .55; scene.add(grid);

  // Equilateral ABC and a unit leg AD. Around AC, cos(theta)=-1/3
  // is the closure condition BD=1; CD remains1 throughout that rotation.
  const height = Math.sqrt(3) / 2;
  const base = { A: new T.Vector3(0, 0, 0), B: new T.Vector3(1, 0, 0), C: new T.Vector3(.5, height, 0), D: new T.Vector3(-.5, height, 0) };
  const points = Object.fromEntries(Object.entries(base).map(([k,v]) => [k,v.clone()]));
  const legAxis = base.D.clone().normalize(), bodyAxis = base.C.clone().normalize();
  const PHI = Math.PI / 3, THETA = Math.acos(-1 / 3);
  const qBody = new T.Quaternion(), qLeg = new T.Quaternion(), transported = new T.Quaternion();
  const colors = { old: 0x7dd3fc, fresh: 0xfbbf24, witness: 0xc084fc };
  const spheres = {}, labels = {};
  const sphereGeometry = new T.SphereGeometry(.037, 20, 16);
  for (const key of Object.keys(points)) {
    const sphere = new T.Mesh(sphereGeometry, new T.MeshStandardMaterial({color: key === 'D' ? 0xfde68a : 0xe5f4ff, roughness: .35}));
    scene.add(sphere); spheres[key] = sphere;
    const label = document.createElement('span'); label.className = 'label'; label.textContent = key; host.append(label); labels[key] = label;
  }
  const cylinderGeometry = new T.CylinderGeometry(1, 1, 1, 10);
  const UP = new T.Vector3(0, 1, 0);
  function segment(color, radius = .012, opacity = 1) {
    const material = new T.MeshStandardMaterial({color, transparent: true, opacity, roughness: .45, depthWrite: opacity === 1});
    const mesh = new T.Mesh(cylinderGeometry, material); mesh.userData.radius = radius; scene.add(mesh); return mesh;
  }
  function place(mesh, a, b) {
    const end = b, delta = end.clone().sub(a), length = delta.length();
    mesh.visible = length > 1e-6;
    if (!mesh.visible) return;
    mesh.position.copy(a).add(end).multiplyScalar(.5);
    mesh.scale.set(mesh.userData.radius, length, mesh.userData.radius);
    mesh.quaternion.setFromUnitVectors(UP, delta.multiplyScalar(1 / length));
  }
  const oldPairs = ['AB','AC','BC','AD'];
  const oldEdges = Object.fromEntries(oldPairs.map(pair => [pair, segment(colors.old)]));
  const freshEdges = Object.fromEntries(['BD','CD'].map(pair => [pair, segment(colors.fresh, .016)]));
  const witnessEdges = Object.fromEntries(['BA','CA','AD'].map(pair => [pair, segment(colors.witness, .022, .75)]));
  const marker = new T.Mesh(new T.SphereGeometry(.045, 16, 12), new T.MeshBasicMaterial({color:colors.witness})); scene.add(marker);

  function polyline(color, opacity, count = 65, dashed = false) {
    const geometry = new T.BufferGeometry(); geometry.setAttribute('position', new T.BufferAttribute(new Float32Array(count * 3), 3));
    const material = dashed ? new T.LineDashedMaterial({color, transparent:true, opacity, dashSize:.07, gapSize:.05}) : new T.LineBasicMaterial({color, transparent:true, opacity});
    const line = new T.Line(geometry, material); scene.add(line); return line;
  }
  function setLine(line, vertices) {
    const attr = line.geometry.attributes.position;
    vertices.forEach((v,i) => attr.setXYZ(i,v.x,v.y,v.z)); attr.needsUpdate = true;
    line.geometry.setDrawRange(0, vertices.length); line.geometry.computeBoundingSphere();
    if (line.material.isLineDashedMaterial) line.computeLineDistances();
  }
  const bodyArc = polyline(colors.witness,.5), legArc = polyline(colors.fresh,.65);
  const axisLine = polyline(0xf1f5f9,.45,2,true);
  const ghosts = Array.from({length:7},() => polyline(colors.witness,.1,4));
  const faceGeometry = new T.BufferGeometry();
  faceGeometry.setAttribute('position',new T.BufferAttribute(new Float32Array(36),3));
  const faceMesh = new T.Mesh(faceGeometry,new T.MeshBasicMaterial({color:0x63b3ed, side:T.DoubleSide, transparent:true, opacity:0, depthWrite:false})); scene.add(faceMesh);
  const faceIndices = ['BCD','ADC','ABD','ACB'];

  const titles = ['1. Identity: the paw','2. 1:many — body around leg','3. Many:1 — leg around body','4. Identity: tetrahedral closure'];
  const descriptions = [
    'Equilateral triangle ABC and unit leg AD lie in one plane. Every original relationship has length 1.',
    'AD stays fixed. The triangle rotates around its leg, leaving a family of witnessed orientations.',
    'The triangle stays fixed. D rotates about the triangle’s AC axis, moving the leg out of its plane.',
    'B → A → D and C → A → D witness the missing connections. Unit edges BD and CD close a regular tetrahedron.'
  ];
  const clamp = x => Math.max(0,Math.min(1,x));
  const smooth = x => { x=clamp(x); return x*x*(3-2*x); };
  let progress = 0, playing = false, lastTime = null, state = {};
  function setProgress(value) {
    progress = clamp(Number(value) || 0);
    const stage = progress < .15 ? 0 : progress < .45 ? 1 : progress < .75 ? 2 : 3;
    const phi = PHI*smooth((progress-.15)/.30), theta = THETA*smooth((progress-.45)/.30);
    const closure = clamp((progress-.75)/.25);
    const edgeFraction = smooth((closure-.25)/.5), faceFraction = smooth((closure-.72)/.28);
    qBody.setFromAxisAngle(legAxis,phi); qLeg.setFromAxisAngle(bodyAxis,theta);
    transported.copy(qBody).multiply(qLeg).multiply(qBody.clone().invert());
    points.A.copy(base.A); points.B.copy(base.B).applyQuaternion(qBody); points.C.copy(base.C).applyQuaternion(qBody);
    points.D.copy(base.D).applyQuaternion(transported);
    for (const k of Object.keys(points)) spheres[k].position.copy(points[k]);
    for (const [pair,mesh] of Object.entries(oldEdges)) place(mesh,points[pair[0]],points[pair[1]]);
    for (const [pair,mesh] of Object.entries(freshEdges)) {
      place(mesh,points[pair[0]],points[pair[1]]);
      mesh.visible = edgeFraction > 0;
      mesh.material.opacity = edgeFraction;
      mesh.material.depthWrite = edgeFraction >= 1;
    }
    for (const [pair,mesh] of Object.entries(witnessEdges)) {
      place(mesh,points[pair[0]],points[pair[1]]);
      mesh.visible = stage === 3 && closure < .8;
      mesh.material.opacity = .7*(1-smooth((closure-.5)/.3));
    }
    marker.visible = stage === 3 && closure < .6;
    if (marker.visible) {
      const pathT = (closure/.6*2)%1, start = closure < .3 ? points.B : points.C;
      marker.position.copy(pathT < .5 ? start.clone().lerp(points.A,pathT*2) : points.A.clone().lerp(points.D,(pathT-.5)*2));
    }
    const facePos=faceGeometry.attributes.position;
    faceIndices.join('').split('').forEach((key,i) => facePos.setXYZ(i,points[key].x,points[key].y,points[key].z));
    facePos.needsUpdate=true;faceGeometry.computeBoundingSphere();
    faceMesh.material.opacity=.23*faceFraction;faceMesh.visible=$('faces').checked && faceFraction>0;
    const showTraces=$('traces').checked;
    bodyArc.visible=showTraces && phi>0;legArc.visible=showTraces && theta>0;
    setLine(bodyArc,Array.from({length:65},(_,i)=>base.C.clone().applyAxisAngle(legAxis,phi*i/64)));
    setLine(legArc,Array.from({length:65},(_,i)=>base.D.clone().applyAxisAngle(bodyAxis,theta*i/64).applyQuaternion(qBody)));
    ghosts.forEach((line,i)=>{
      const ghostPhi=PHI*i/(ghosts.length-1);
      line.visible=showTraces && i>0 && ghostPhi<=phi+1e-8;
      setLine(line,[base.A,base.B,base.C,base.A].map(v=>v.clone().applyAxisAngle(legAxis,ghostPhi)));
      line.material.opacity=stage===1?.17:.07;
    });
    axisLine.visible=stage===1 || stage===2;
    const activeAxis=stage===1?legAxis:bodyAxis.clone().applyQuaternion(qBody);
    setLine(axisLine,[activeAxis.clone().multiplyScalar(-1.45),activeAxis.clone().multiplyScalar(1.45)]);
    const geometricVolume=Math.abs(points.B.clone().sub(points.A).dot(points.C.clone().sub(points.A).cross(points.D.clone().sub(points.A))))/6;
    const closed = edgeFraction >= 1-1e-9;
    $('stage-title').textContent=titles[stage];$('description').textContent=descriptions[stage];$('badge').textContent=titles[stage];
    $('edges').textContent=closed?'6':edgeFraction>0?'4 → 6':'4';
    $('packets').textContent=closed?'12':edgeFraction>0?'8 → 12':'8';
    $('volume').textContent=closed?geometricVolume.toFixed(4):'0.0000';
    $('phi').textContent=`${(phi*180/Math.PI).toFixed(0)}°`;$('theta').textContent=`${(theta*180/Math.PI).toFixed(0)}°`;
    $('witness').textContent=stage===3?'BD: BA + AD · CD: CA + AD':'Triangle ABC · leg AD';
    $('timeline').value=String(progress);$('progress').textContent=`${Math.round(progress*100)}%`;
    document.querySelectorAll('[data-stage]').forEach((b,i)=>b.setAttribute('aria-pressed',String(i===stage)));
    state={progress,stage,phi,theta,closed,edgeFraction,geometricVolume,packetCount:closed?12:8,
      points:Object.fromEntries(Object.entries(points).map(([k,v])=>[k,v.toArray()])),
      visibleEdges:Object.fromEntries(Object.entries({...oldEdges,...freshEdges}).filter(([,m])=>m.visible).map(([k,m])=>[k,m.scale.y]))};
  }
  function setPlaying(on) { playing=on;lastTime=null;$('play').textContent=playing?'Pause':'Play'; }
  $('play').addEventListener('click',()=>{ if(!playing && progress>=1)setProgress(0);setPlaying(!playing); });
  $('reset').addEventListener('click',()=>{setPlaying(false);setProgress(0);});
  $('camera-reset').addEventListener('click',resetCamera);
  $('timeline').addEventListener('input',e=>{setPlaying(false);setProgress(e.target.value);});
  const stops=[0,.449,.749,1];
  document.querySelectorAll('[data-stage]').forEach(button=>button.addEventListener('click',()=>{setPlaying(false);setProgress(stops[Number(button.dataset.stage)]);}));
  ['traces','faces'].forEach(id=>$(id).addEventListener('change',()=>setProgress(progress)));
  document.addEventListener('keydown',e=>{if(e.code==='Space' && !['INPUT','SELECT','BUTTON','TEXTAREA'].includes(document.activeElement.tagName)){e.preventDefault();$('play').click();}});
  document.addEventListener('visibilitychange',()=>{lastTime=null;});
  new ResizeObserver(()=>{
    const w=host.clientWidth,h=host.clientHeight;renderer.setSize(w,h);camera.aspect=w/h;camera.updateProjectionMatrix();
  }).observe(host);
  function tick(time) {
    requestAnimationFrame(tick);
    if(playing && !document.hidden){
      if(lastTime!==null)setProgress(progress+Math.min((time-lastTime)/1000,.1)*Number($('speed').value)/18);
      lastTime=time;if(progress>=1)setPlaying(false);
    }
    controls.update();renderer.render(scene,camera);
    for(const [key,v] of Object.entries(points)){
      const p=v.clone().project(camera),label=labels[key];
      label.style.left=`${(p.x*.5+.5)*host.clientWidth}px`;label.style.top=`${(-p.y*.5+.5)*host.clientHeight-18}px`;
      label.style.display=p.z>1 || p.z< -1?'none':'';
    }
  }
  // Small deterministic inspection interface for local regression tests.
  window.pawCycle=Object.freeze({setProgress:value=>{setPlaying(false);setProgress(value);},snapshot:()=>JSON.parse(JSON.stringify(state))});
  setProgress(0);requestAnimationFrame(tick);
})();
