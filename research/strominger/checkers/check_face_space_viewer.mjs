import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir,stat} from 'node:fs/promises';
import {createServer} from 'node:http';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {chromium} from '@playwright/test';
import {makeFaceComplex,reflectAcrossFace,cellVolume,centroid,interiorsOverlap} from '../demos/particle-overlap-tetrahedron/face-model.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..'),source='research/strominger/demos/particle-overlap-tetrahedron',out=path.join(root,'research/strominger/results/face-space-viewer');
const checks={},check=(name,ok)=>{assert.ok(ok,name);checks[name]=true;},distance=(a,b)=>Math.hypot(...a.map((x,i)=>x-b[i]));
const near=(a,b)=>Math.abs(a-b)<1e-10,hash=bytes=>createHash('sha256').update(bytes).digest('hex');
let server,browser;
try {
  await mkdir(out,{recursive:true});const c=makeFaceComplex(),seed=c.getCell(),seedPoints=seed.vertices.map(id=>c.nodes.get(id));
  check('unit_regular_seed_cell',seed.vertices.every((id,i)=>seed.vertices.slice(i+1).every(other=>near(distance(c.nodes.get(id),c.nodes.get(other)),1)))&&near(cellVolume(seedPoints),1/(6*Math.sqrt(2))));
  const exits=c.exits();
  check('three_exits_are_exactly_the_nonincoming_faces',exits.length===3&&exits.every((e,i)=>e.omitted===seed.incoming[i]&&e.face.length===3&&e.face.every(id=>id!==e.omitted)));
  for(const exit of exits) {
    const child=c.getCell(exit.path);assert.deepEqual(child.incoming,exit.face);
    assert.deepEqual(child.vertices.filter(id=>seed.vertices.includes(id)),exit.face);
    assert.ok(near(cellVolume(child.vertices.map(id=>c.nodes.get(id))),1/(6*Math.sqrt(2))));
    const face=exit.face.map(id=>c.nodes.get(id)),apex=c.nodes.get(child.vertices[3]);
    assert.ok(distance(reflectAcrossFace(apex,face),c.nodes.get(exit.omitted))<1e-10);
    assert.ok(!interiorsOverlap(seedPoints,child.vertices.map(id=>c.nodes.get(id))));
  }
  checks.each_neighbor_reuses_shared_face_and_reflection_is_reversible=true;
  check('initial_local_star_has_no_interior_overlap',exits.every((e,i)=>exits.slice(i+1).every(other=>!interiorsOverlap(c.getCell(e.path).vertices.map(id=>c.nodes.get(id)),c.getCell(other.path).vertices.map(id=>c.nodes.get(id))))));
  const vectors=exits.map(e=>e.target.map((x,i)=>x-centroid(seedPoints)[i]));
  check('three_realization_directions_are_non_coplanar',cellVolume([[0,0,0],...vectors])>1e-4);
  const transform=p=>[p[2]+2,p[0]-1,p[1]+.4],e=exits[0],face=e.face.map(id=>c.nodes.get(id));
  check('reflection_is_covariant_under_changed_spatial_chart',distance(reflectAcrossFace(transform(c.nodes.get(e.omitted)),face.map(transform)),transform(c.nodes.get(c.getCell(e.path).vertices[3])))<1e-10);
  check('different_exit_orders_are_not_silently_identified',distance(c.describe(c.getCell([0,1])).center,c.describe(c.getCell([1,0])).center)>.1);
  check('overlap_detector_distinguishes_touching_from_identical_cells',!interiorsOverlap(seedPoints,c.getCell([0]).vertices.map(id=>c.nodes.get(id)))&&interiorsOverlap(seedPoints,seedPoints));
  const ringPath=[0,2,2,2,2],ring=c.getCell(ringPath);
  check('longer_edge_ring_has_an_explicit_non_global_embedding_obstruction',interiorsOverlap(seedPoints,ring.vertices.map(id=>c.nodes.get(id))));
  const all=c.carriers('all');
  check('carrier_cells_are_generated_from_two_actual_face_crossings',all.bodies.map(b=>b.cellId).join(',')==='root,R1,R1/R1'&&Object.keys(all.bindings).length===6);
  check('carrier_points_are_literal_complex_node_references',Object.entries(all.points).every(([name,p])=>p===c.nodes.get(all.bindings[name])));
  check('carrier_cells_share_the_complete_prescribed_faces',all.bodies[0].vertices.filter(id=>all.bodies[1].vertices.includes(id)).length===3&&all.bodies[1].vertices.filter(id=>all.bodies[2].vertices.includes(id)).length===3);
  for(const mode of ['proton','neutron','electron'])assert.equal(c.carriers(mode).bodies.length,1);
  checks.lone_modes_select_one_cell_without_new_coordinates=true;
  assert.throws(()=>c.getCell([3]));assert.throws(()=>c.getCell([.5]));assert.throws(()=>c.carriers('unknown'));checks.invalid_paths_and_modes_are_rejected=true;
  const source_sha256={};
  for(const file of ['face-space.html','face-space.css','face-space.js','face-model.mjs']) {
    const bytes=await readFile(path.join(root,source,file));source_sha256[source+'/'+file]=hash(bytes);
    for(const dir of ['public','website/public'])assert.equal(hash(await readFile(path.join(root,dir,'experiments/particle-overlap-tetrahedron',file))),hash(bytes));
  }
  checks.both_owned_public_mirrors_match_sources=true;
  const publicRoot=path.join(root,'public'),mime={'.html':'text/html','.js':'text/javascript','.mjs':'text/javascript','.css':'text/css'};
  server=createServer(async(req,res)=>{try{let file=path.resolve(publicRoot,'.'+new URL(req.url,'http://localhost').pathname);if(path.relative(publicRoot,file).startsWith('..'))throw Error('path');if((await stat(file)).isDirectory())file=path.join(file,'index.html');res.setHeader('Content-Type',mime[path.extname(file)]||'text/plain');res.end(await readFile(file));}catch{res.writeHead(404);res.end();}});
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const base=process.argv.find(arg=>arg.startsWith('--base-url='))?.slice('--base-url='.length)||'http://127.0.0.1:'+server.address().port;
  browser=await chromium.launch({headless:true,args:['--enable-webgl','--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
  const page=await browser.newPage({viewport:{width:1480,height:1040},hasTouch:true}),errors=[];page.on('pageerror',error=>errors.push(String(error)));
  await page.goto(base+'/experiments/particle-overlap-tetrahedron/vacuum.html');await page.waitForFunction(()=>globalThis.FaceSpaceViewer?.snapshot().frameCount>2);
  const snap=()=>page.evaluate(()=>globalThis.FaceSpaceViewer.snapshot());let s=await snap();
  check('existing_space_URL_opens_the_face_realization_view',new URL(page.url()).pathname.endsWith('/face-space.html'));
  check('empty_local_star_renders_four_generated_cells',s.webgl&&s.cells.length===4&&s.state.carrier==='none'&&s.selection.bodies.length===0&&s.exits.length===3&&s.overlaps.length===0);
  check('no_global_R_axis_or_planar_controls',await page.locator('#level,#turn,#spacing').count()===0&&await page.locator('[data-exit]').count()===3);
  for(const rendered of s.rendered) {
    const cell=s.cells.find(c=>c.id===rendered.cellId);
    cell.vertices.forEach((id,i)=>assert.ok(distance(rendered.positions.slice(i*3,i*3+3),s.nodes[id])<1e-6));
  }
  checks.every_rendered_cell_vertex_is_a_generated_complex_node=true;
  await page.locator('#scene').screenshot({path:path.join(out,'empty-local-star.png')});
  await page.locator('[data-exit="0"]').click();s=await snap();
  check('first_exit_crosses_into_R1_and_reuses_incoming_face',s.current.id==='R1'&&s.current.incoming.join(',')===exits[0].face.join(','));
  await page.locator('#back').click();s=await snap();assert.deepEqual(s.current.points,c.describe(seed).points);checks.undo_recovers_exact_parent_cell=true;
  await page.locator('[data-exit="1"]').click();check('second_exit_is_a_distinct_continuation',(await snap()).current.id==='R2');await page.locator('#root').click();
  const facePoint=await page.evaluate(()=>globalThis.FaceSpaceViewer.projectExit(0));await page.mouse.click(facePoint.x,facePoint.y);
  check('clicking_a_face_or_its_scene_label_crosses_it',(await snap()).current.id==='R1');await page.locator('#root').click();
  await page.evaluate(()=>globalThis.FaceSpaceViewer.setPath([0,2,2,2,2]));s=await snap();
  check('UI_reports_actual_route_overlaps_instead_of_claiming_a_tiling',s.overlaps.length>0&&/interior overlaps/.test(await page.locator('#geometry-readout').textContent())&&await page.locator('#embedding-warning').isVisible());
  await page.locator('#scene').screenshot({path:path.join(out,'overlap-edge-ring.png')});
  await page.locator('#root').click();
  for(const mode of ['proton','neutron','electron','all']) {
    await page.locator(`[data-carrier="${mode}"]`).click();s=await snap();
    assert.equal(s.selection.bodies.length,mode==='all'?3:1);assert.equal(s.rendered.filter(mesh=>mesh.carrier).length,mode==='all'?3:1);
    for(const [name,p] of Object.entries(s.selection.points))assert.deepEqual(p,s.nodes[s.selection.bindings[name]]);
  }
  checks.all_four_carrier_modes_use_only_existing_generated_cells=true;
  const anchored=s.selection;await page.locator('[data-exit="2"]').click();s=await snap();
  check('exploring_does_not_relocate_anchored_carriers',JSON.stringify(s.selection)===JSON.stringify(anchored)&&s.current.id==='R3');
  await page.locator('#place-carriers').click();s=await snap();
  check('explicit_placement_anchors_to_current_cell',s.selection.anchor.join(',')==='2'&&s.selection.bodies[0].cellId==='R3');
  await page.locator('#root').click();await page.locator('#place-carriers').click();await page.locator('#focus-carriers').click();
  await page.locator('#scene').screenshot({path:path.join(out,'all-carriers.png')});
  await page.locator('[data-carrier="none"]').click();check('empty_removes_all_occupant_fills',(await snap()).rendered.every(mesh=>mesh.carrier===null));
  await page.locator('#neighbors').uncheck();check('neighbors_can_be_hidden',(await snap()).cells.length===1);await page.locator('#neighbors').check();
  await page.locator('#reset-view').click();const before=(await snap()).state.path;
  const box=await page.locator('canvas').boundingBox();await page.mouse.move(box.x+box.width/2,box.y+box.height/2);await page.mouse.down();await page.mouse.move(box.x+box.width/2+80,box.y+box.height/2+30,{steps:8});await page.mouse.up();assert.deepEqual((await snap()).state.path,before);checks.orbit_drag_does_not_cross_a_face=true;
  await page.setViewportSize({width:430,height:930});await page.locator('#reset-view').click();
  check('mobile_has_no_horizontal_overflow',await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  await page.locator('[data-exit="0"]').tap();check('mobile_exit_controls_work',(await snap()).current.id==='R1');await page.locator('#root').tap();
  await page.locator('#scene').screenshot({path:path.join(out,'mobile-local-star.png')});
  await page.locator('[data-carrier="all"]').tap();await page.locator('#focus-carriers').tap();await page.locator('#scene').screenshot({path:path.join(out,'mobile-all-carriers.png')});
  await page.goto(base+'/experiments/particle-overlap-tetrahedron/vacuum.html?mode=planes');await page.getByRole('link',{name:'Face realizations'}).click();await page.waitForFunction(()=>globalThis.FaceSpaceViewer?.snapshot().frameCount>2);checks.face_view_is_linked_from_planar_comparison=true;
  check('no_browser_exceptions',errors.length===0);
  await writeFile(path.join(out,'verification.json'),JSON.stringify({schema:'marici.face-space-viewer.v1',status:'pass',checked_at:new Date().toISOString(),checks,source_sha256,
    route:'/experiments/particle-overlap-tetrahedron/face-space.html',scope:'Local reflection complex with generated node bindings and three noncoplanar exits. Not a space-filling tiling or derived physical particle/60-degree/C-M exchange law.'},null,2)+'\n');
  console.log(JSON.stringify({status:'pass',checks:Object.keys(checks).length,route:'/experiments/particle-overlap-tetrahedron/face-space.html'}));
}finally{await browser?.close();if(server)await new Promise(resolve=>server.close(resolve));}
