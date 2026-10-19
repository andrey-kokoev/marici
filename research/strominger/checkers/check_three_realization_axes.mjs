import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir,stat} from 'node:fs/promises';
import {createServer} from 'node:http';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {chromium} from '@playwright/test';
import {makeRealizationSpace,realizationBasis,frameAt,addressKey} from '../demos/particle-overlap-tetrahedron/realization-model.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..'),src='research/strominger/demos/particle-overlap-tetrahedron',out=path.join(root,'research/strominger/results/three-realization-axes');
const checks={},check=(n,b)=>{assert.ok(b,n);checks[n]=true;},dist=(a,b)=>Math.hypot(...a.map((x,i)=>x-b[i])),dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),near=(a,b)=>Math.abs(a-b)<1e-10;
const hash=b=>createHash('sha256').update(b).digest('hex');let server,browser;
try {
  await mkdir(out,{recursive:true});
  check('three_equivalent_unit_realization_generators_at_60_degrees',realizationBasis.every((a,i)=>near(Math.hypot(...a),1)&&realizationBasis.slice(i+1).every(b=>near(dot(a,b),.5))));
  const determinant=realizationBasis[0][0]*(realizationBasis[1][1]*realizationBasis[2][2]-realizationBasis[1][2]*realizationBasis[2][1]);
  check('three_realization_axes_are_independent',Math.abs(determinant)>.5);
  for(const axis of [0,1,2])for(const sign of [-1,1]) {
    const address=[0,0,0];address[axis]=sign;const frame=frameAt(address);
    assert.equal(frame.angleDegrees,sign*60);assert.equal(frame.roles,'CCM');assert.ok(near(dist(frame.origin,[0,0,0]),1));
  }
  checks.every_signed_R_step_rotates_frame_60_degrees_and_exchanges_types=true;
  check('typed_directions_are_coplanar_unit_axes_at_120_degrees',frameAt([0,0,0]).axes.every((a,i)=>near(Math.hypot(...a.direction),1)&&near(dot(a.direction,frameAt([0,0,0]).normal),0)&&near(dot(a.direction,frameAt([0,0,0]).axes[(i+1)%3].direction),-.5)));
  const space=makeRealizationSpace({carrier:'all'});
  check('lattice_has_125_distinct_integer_nodes',space.nodes.length===125&&new Set(space.nodes.map(n=>n.id)).size===125&&space.nodes.every(n=>n.id===addressKey(n.address)&&n.address.every(Number.isInteger)));
  check('all_lattice_edges_are_unit_nearest_neighbors',space.edges.every(([a,b])=>near(dist(space.nodes[a].point,space.nodes[b].point),1)));
  check('empty_space_is_one_unsubdivided_three_simplex',space.space.vertices.length===4&&space.space.edges.length===6&&space.space.faces.length===4&&space.space.cells.length===1);
  check('simplex_has_six_equal_edges',space.space.edges.every(([a,b])=>near(dist(space.space.vertices[a],space.space.vertices[b]),6)));
  const nodes=new Map(space.nodes.map(n=>[n.id,n]));
  check('every_carrier_vertex_is_an_actual_lattice_node_reference',Object.entries(space.carriers.points).every(([name,p])=>p===nodes.get(space.carriers.bindings[name]).point));
  const proton=space.carriers.bodies[0];
  check('proton_seed_is_a_unit_tetrahedron_of_realization_nodes',proton.names.every((name,i)=>proton.names.slice(i+1).every(other=>near(dist(space.carriers.points[name],space.carriers.points[other]),1))));
  for(const mode of ['proton','neutron','electron'])assert.equal(makeRealizationSpace({carrier:mode}).carriers.bodies.length,1);checks.lone_selectors_retain_exactly_one_cell=true;
  assert.throws(()=>frameAt([.5,0,0]));assert.throws(()=>makeRealizationSpace({carrier:'unknown'}));checks.invalid_coordinates_and_modes_are_rejected=true;
  const source_sha256={};for(const file of ['vacuum.html','realization.css','realization-app.js','realization-model.mjs']){
    const bytes=await readFile(path.join(root,src,file));source_sha256[src+'/'+file]=hash(bytes);
    for(const dir of ['public','website/public'])assert.equal(hash(await readFile(path.join(root,dir,'experiments/particle-overlap-tetrahedron',file))),hash(bytes));
  }checks.public_mirrors_match_sources=true;
  const publicRoot=path.join(root,'public'),mime={'.html':'text/html','.js':'text/javascript','.mjs':'text/javascript','.css':'text/css'};
  server=createServer(async(req,res)=>{try{let file=path.resolve(publicRoot,'.'+new URL(req.url,'http://localhost').pathname);if(path.relative(publicRoot,file).startsWith('..'))throw Error('path');if((await stat(file)).isDirectory())file=path.join(file,'index.html');res.setHeader('Content-Type',mime[path.extname(file)]||'text/plain');res.end(await readFile(file));}catch{res.writeHead(404);res.end();}});await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const base=process.argv.find(arg=>arg.startsWith('--base-url='))?.slice('--base-url='.length)||'http://127.0.0.1:'+server.address().port;
  browser=await chromium.launch({headless:true,args:['--enable-webgl','--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
  const page=await browser.newPage({viewport:{width:1480,height:1040},hasTouch:true}),errors=[];page.on('pageerror',e=>errors.push(String(e)));
  await page.goto(base+'/experiments/particle-overlap-tetrahedron/vacuum.html');await page.waitForFunction(()=>globalThis.RealizationSpaceViewer?.snapshot().frameCount>2);
  const snap=()=>page.evaluate(()=>globalThis.RealizationSpaceViewer.snapshot());let s=await snap();
  check('rendered_empty_space_has_only_simplex_boundary',s.renderedSimplex.vertices===4&&s.renderedSimplex.edges===6&&s.renderedSimplex.faces===4&&s.renderedCarriers.length===0);
  await page.locator('#grid').uncheck();assert.deepEqual((await snap()).renderedSimplex,{vertices:0,edges:0,faces:0});await page.locator('#grid').check();
  check('existing_URL_now_opens_three_axes_not_face_navigation',s.webgl&&s.realizationLabels.length===6&&await page.locator('[data-exit],#exit-controls,#incoming').count()===0);
  check('origin_has_two_signed_M_axes_and_one_signed_C_axis',s.typedLabels.filter(x=>x==='M+').length===2&&s.typedLabels.filter(x=>x==='M-').length===2&&s.typedLabels.filter(x=>x==='C+').length===1&&s.typedLabels.filter(x=>x==='C-').length===1);
  check('all_six_signed_R_labels_and_typed_labels_are_visible',await page.locator('.realization-label.r:visible').count()===6&&await page.locator('.realization-label.typed:visible').count()===6);
  await page.locator('#scene').screenshot({path:path.join(out,'three-R-axes.png')});
  for(const axis of [0,1,2]) {
    await page.locator(`[data-axis="${axis}"][data-sign="1"]`).click();s=await snap();assert.equal(s.state.address[axis],1);assert.equal(s.model.frame.angleDegrees,60);assert.equal(s.model.frame.roles,'CCM');
    await page.locator(`[data-axis="${axis}"][data-sign="-1"]`).click();assert.deepEqual((await snap()).state.address,[0,0,0]);
  }checks.all_three_axis_controls_step_and_reverse_independently=true;
  await page.getByRole('button',{name:'R₃−',exact:true}).first().click();s=await snap();check('negative_realization_step_is_minus_60_degrees',s.state.address[2]===-1&&s.model.frame.angleDegrees===-60);await page.locator('#origin').click();
  for(const mode of ['proton','neutron','electron','all']){
    await page.locator(`[data-carrier="${mode}"]`).click();s=await snap();assert.equal(s.renderedCarriers.length,mode==='all'?3:1);
    for(const mesh of s.renderedCarriers){const body=s.model.carriers.bodies.find(b=>b.id===mesh.id);body.names.forEach((name,i)=>{const id=s.model.carriers.bindings[name],node=s.model.nodes.find(n=>n.id===id);assert.ok(dist(mesh.positions.slice(i*3,i*3+3),node.point)<1e-6);});}
  }checks.every_selected_rendered_vertex_matches_its_lattice_node=true;
  await page.locator('#focus-carriers').click();await page.locator('#scene').screenshot({path:path.join(out,'three-R-all-carriers.png')});
  await page.locator('[data-carrier="none"]').click();check('empty_removes_all_carrier_meshes',(await snap()).renderedCarriers.length===0);await page.locator('#reset-view').click();
  await page.locator('#assignment').selectOption('CCM');check('reference_XOR_remains_available',(await snap()).model.frame.roles==='CCM');await page.locator('#assignment').selectOption('MMC');
  await page.setViewportSize({width:430,height:930});await page.locator('#reset-view').click();check('mobile_has_no_horizontal_overflow',await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  check('mobile_keeps_all_six_realization_labels_visible',await page.locator('.realization-label.r:visible').count()===6);
  await page.locator('[data-axis="1"][data-sign="1"]').tap();check('mobile_realization_control_works',(await snap()).state.address[1]===1);await page.locator('#origin').tap();await page.locator('#scene').screenshot({path:path.join(out,'three-R-mobile.png')});
  await page.goto(base+'/experiments/particle-overlap-tetrahedron/face-space.html');await page.waitForFunction(()=>globalThis.RealizationSpaceViewer?.snapshot().frameCount>2);check('obsolete_face_URL_redirects_to_axes',new URL(page.url()).pathname.endsWith('/vacuum.html')&&await page.locator('[data-exit]').count()===0);
  check('no_browser_exceptions',errors.length===0);
  await writeFile(path.join(out,'verification.json'),JSON.stringify({schema:'marici.three-realization-axes.v1',status:'pass',checked_at:new Date().toISOString(),checks,source_sha256,route:'/experiments/particle-overlap-tetrahedron/vacuum.html',scope:'Three signed discrete lattice generators, 60-degree local typed frame steps, literal carrier-node bindings. No face navigation or inferred physical law.'},null,2)+'\n');
  console.log(JSON.stringify({status:'pass',checks:Object.keys(checks).length,route:'/experiments/particle-overlap-tetrahedron/vacuum.html'}));
}finally{await browser?.close();if(server)await new Promise(resolve=>server.close(resolve));}
