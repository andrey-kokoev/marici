import assert from 'node:assert/strict';
import {createServer} from 'node:http';
import {readFile,writeFile,mkdir,stat} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import {chromium} from '@playwright/test';
import * as M from '../demos/particle-overlap-tetrahedron/model.mjs';
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const OUT=path.join(ROOT,'research/strominger/results/particle-overlap-viewer');
const PUBLIC=path.join(ROOT,'public');
const checks={};
const ck=(name,value)=>{assert.ok(value,name);checks[name]=true;};
const near=(a,b,tol=1e-11)=>assert.ok(Math.hypot(...a.flat(Infinity).map((v,i)=>v-b.flat(Infinity)[i]))<tol);
const hash=b=>createHash('sha256').update(b).digest('hex');
async function main(){
  const vertices=Object.values(M.outer);
  ck('five_outer_vertices_in_four_dimensions',vertices.length===5&&vertices.every(v=>v.length===4));
  for(let i=0;i<5;i++)for(let j=i+1;j<5;j++)near([M.distanceSquared(vertices[i],vertices[j])],[8]);
  checks.regular_pentachoron_ten_squared_edges_eight=true;
  near(M.barycenter,[0,0,0,Math.sqrt(5)/5]);
  ck('barycenter_is_distinct_from_facet_center',M.barycenter[3]>0);
  for(const v of vertices)near([M.distanceSquared(v,M.barycenter)],[16/5]);
  checks.barycenter_equidistant_from_all_five_vertices=true;
  ck('four_facet_vertices_and_six_edges',M.facet.length===4&&M.facetEdges.length===6);
  assert.deepEqual(M.routes.map(r=>r.nodes),[['C0','M0','C1'],['M0','C1','M1'],['M1','C1','C2']]);
  checks.requested_three_windows_retained=true;
  assert.deepEqual(M.directedEdges(M.routes[0])[1],M.directedEdges(M.routes[1])[0]);
  assert.deepEqual(M.directedEdges(M.routes[1])[1],M.directedEdges(M.routes[2])[0].slice().reverse());
  checks.shared_edges_retain_same_and_opposite_orientations=true;
  ck('C1_is_one_point_with_two_walk_occurrences',M.walk.filter(v=>v==='C1').length===2);
  M.walk.forEach((name,i)=>near(M.pointOnWalk(i),M.points[name]));
  near(M.pointOnWalk(99),M.barycenter);near(M.pointOnWalk(-1),M.points.C0);
  checks.walk_interpolation_has_correct_vertices_and_clamped_endpoints=true;
  for(const angle of [-70,0,35,70])near(M.project4D(M.barycenter,angle),[0,-Math.sin(angle*Math.PI/180)*Math.sqrt(5)/5,0]);
  checks.projection_uses_fourth_coordinate_without_changing_source_geometry=true;
  assert.deepEqual(Object.keys(M.lattice),M.carriers);
  ck('lattice_C_carriers_have_codimension_zero',['C0','C1','C2'].every(n=>M.lattice[n][2]===0));
  ck('lattice_M_carriers_have_codimension_one',['M0','M1'].every(n=>M.lattice[n][2]===1));
  ck('lattice_coordinates_remain_integer',Object.values(M.lattice).flat().every(Number.isInteger));
  assert.deepEqual(['C0','C1','C2'].map(n=>M.lattice[n]),[[-1,0,0],[0,0,0],[1,0,0]]);
  checks.realization_is_the_C_spine_x_coordinate=true;
  ck('realization_x_never_reverses_in_the_displayed_walk',M.walk.slice(1).every((n,i)=>M.lattice[n][0]>=M.lattice[M.walk[i]][0]));
  ck('y_is_unused_and_all_lattice_carriers_lie_in_xz',Object.values(M.lattice).every(p=>p[1]===0));
  assert.deepEqual(M.lattice.M0,[-1,0,1]);assert.deepEqual(M.lattice.M1,[0,0,1]);
  checks.M1_is_directly_above_C1=true;
  assert.deepEqual(Object.keys(M.hex),M.carriers);
  near(M.hex.M0,[-.5,0,Math.sqrt(3)/2]);near(M.hex.M1,[.5,0,Math.sqrt(3)/2]);
  for(const n of M.carriers) {
    const [x,y,z]=M.hex[n];near([x-z/Math.sqrt(3),y,2*z/Math.sqrt(3)],M.lattice[n]);
    near(M.displayPoint(M.hex[n],'hex'),M.hex[n]);
  }
  checks.hex_is_a_separate_invertible_realization_of_the_same_axial_sites=true;
  near([M.hexBasis.a.reduce((s,v,i)=>s+v*M.hexBasis.b[i],0)],[.5]);
  for(const v of Object.values(M.hexBasis))near([Math.hypot(...v)],[1]);
  for(const v of [M.hexBasis.a,M.hexBasis.b])near([v.reduce((s,x,i)=>s+x*M.hexBasis.c[i],0)],[0]);
  checks.hex_basis_has_60_degree_basal_axes_and_perpendicular_stack=true;
  assert.equal(Object.keys(M.tetraAxisDirections).length,6);
  for(const [positive,negative] of [['X','NX'],['Z','NZ'],['Y','NY']]) {
    near(M.tetraAxisDirections[positive].map((v,i)=>v+M.tetraAxisDirections[negative][i]),[0,0,0]);
    near([Math.hypot(...M.tetraAxisDirections[positive])],[1]);
  }
  checks.three_axis_families_have_six_opposite_unit_directions=true;
  for(const p of [[1,0,0],[0,0,1],[-1,0,1],[-1,0,0],[0,0,-1],[1,0,-1]])near([Math.hypot(...M.hexPoint(p))],[1]);
  checks.hex_basal_lattice_has_six_unit_nearest_neighbors=true;
  for(const route of M.routes) {
    for(let i=0;i<3;i++)near([M.distanceSquared(M.hex[route.nodes[i]],M.hex[route.nodes[(i+1)%3]])],[1]);
    checks['hex_'+route.id+'_is_an_equilateral_unit_triangle']=true;
  }
  const grid=M.triangularGrid();
  assert.equal(grid.triangles.length,8*grid.radius**2);
  assert.ok(grid.vertices.every(p=>p[1]===0));
  for(const [a,b] of grid.edges)near([M.distanceSquared(grid.vertices[a],grid.vertices[b])],[1]);
  for(const cell of grid.triangles)for(let i=0;i<3;i++)near([M.distanceSquared(grid.vertices[cell[i]],grid.vertices[cell[(i+1)%3]])],[1]);
  checks.entire_CMC_grid_patch_is_tiled_by_equal_unit_triangles=true;
  for(const route of M.routes) {
    const ids=route.nodes.map(n=>grid.vertices.findIndex(p=>M.distanceSquared(p,M.hex[n])<1e-20));
    ck(route.id+'_occupies_exactly_one_elementary_grid_triangle',ids.every(i=>i>=0)&&grid.triangles.some(cell=>ids.every(i=>cell.includes(i))));
  }
  const origin=grid.vertices.findIndex(p=>M.distanceSquared(p,[0,0,0])<1e-20);
  ck('triangular_grid_has_six_edges_at_each_interior_vertex',grid.edges.filter(e=>e.includes(origin)).length===6);
  for(const radius of [0,-1,1.5])assert.throws(()=>M.triangularGrid(radius),RangeError);
  checks.invalid_triangular_grid_radii_are_rejected=true;
  const tetra=M.tetrahedralGrid();
  const volume=(cell,vertices=tetra.vertices)=>{
    const [a,...rest]=cell.map(i=>vertices[i]),[u,v,w]=rest.map(p=>p.map((x,i)=>x-a[i]));
    return (u[0]*(v[1]*w[2]-v[2]*w[1])-u[1]*(v[0]*w[2]-v[2]*w[0])+u[2]*(v[0]*w[1]-v[1]*w[0]))/6;
  };
  assert.equal(tetra.tetrahedra.length,6*(2*tetra.radius)**3);
  for(const cell of tetra.tetrahedra)near([volume(cell)],[Math.sqrt(3)/12]);
  checks.all_volume_cells_are_positive_equal_volume_tetrahedra=true;
  near([tetra.tetrahedra.reduce((sum,cell)=>sum+volume(cell),0)],[(2*tetra.radius)**3*Math.sqrt(3)/2],1e-9);
  checks.six_tetrahedra_fill_each_primitive_prism_volume=true;
  for(const face of tetra.faces) {
    const coordinates=face.vertices.map(i=>tetra.coefficients[i]);
    const boundary=[0,1,2].some(axis=>[-tetra.radius,tetra.radius].some(k=>coordinates.every(p=>p[axis]===k)));
    assert.equal(face.uses,boundary?1:2);
  }
  checks.volume_mesh_has_no_unpaired_interior_faces_or_nonmanifold_faces=true;
  const removed=tetra.tetrahedra.find(cell=>cell.every(i=>tetra.coefficients[i].every(x=>Math.abs(x)<tetra.radius)));
  const originalUses=new Map(tetra.faces.map(f=>[f.vertices.join(','),f.uses])),damagedUses=new Map(originalUses);
  for(let omitted=0;omitted<4;omitted++) {
    const key=removed.filter((_,i)=>i!==omitted).sort((a,b)=>a-b).join(',');
    damagedUses.set(key,damagedUses.get(key)-1);
  }
  ck('removing_an_interior_tetrahedron_exposes_exactly_four_unpaired_faces',[...damagedUses].filter(([key,n])=>n===1&&originalUses.get(key)===2).length===4);
  ck('off_plane_tetrahedra_are_explicitly_non_regular',tetra.tetrahedra.every(cell=>{
    const lengths=cell.flatMap((a,i)=>cell.slice(i+1).map(b=>M.distanceSquared(tetra.vertices[a],tetra.vertices[b])));
    return Math.max(...lengths)-Math.min(...lengths)>.5;
  }));
  const centralFaces=tetra.faces.filter(f=>f.vertices.every(i=>tetra.vertices[i][1]===0));
  const faceKey=points=>points.map(p=>p.join(',')).sort().join(';');
  const centralKeys=new Set(centralFaces.map(f=>faceKey(f.vertices.map(i=>tetra.vertices[i]))));
  const centralGrid=M.triangularGrid(tetra.radius);
  assert.equal(centralFaces.length,centralGrid.triangles.length);
  for(const face of centralGrid.triangles)assert.ok(centralKeys.has(faceKey(face.map(i=>centralGrid.vertices[i]))));
  checks.volume_mesh_preserves_the_entire_equilateral_CMC_section=true;
  for(const route of M.routes) {
    const key=faceKey(route.nodes.map(n=>M.hex[n]));
    const face=centralFaces.find(f=>faceKey(f.vertices.map(i=>tetra.vertices[i]))===key);
    ck(route.id+'_is_a_shared_face_of_two_volume_tetrahedra',face?.uses===2);
  }
  ck('volume_mesh_extends_to_both_sides_of_CMC_plane',tetra.vertices.some(p=>p[1]<0)&&tetra.vertices.some(p=>p[1]>0));
  for(const radius of [0,-1,1.5])assert.throws(()=>M.tetrahedralGrid(radius),RangeError);
  checks.invalid_tetrahedral_grid_radii_are_rejected=true;
  const bounded=M.boundedTetrahedralGrid(4);
  assert.equal(bounded.radius,4);assert.deepEqual(bounded.center,M.hex.C1);
  ck('all_bounded_lattice_vertices_are_within_four_units',bounded.vertices.every(p=>Math.hypot(...p)<=4+1e-12));
  for(const cell of bounded.tetrahedra)near([volume(cell,bounded.vertices)],[Math.sqrt(3)/12]);
  checks.radius_cutoff_keeps_complete_positive_volume_cells=true;
  assert.equal(new Set(bounded.tetrahedra.flat()).size,bounded.vertices.length);
  ck('bounded_mesh_has_no_orphan_vertices_or_duplicate_edges',new Set(bounded.edges.map(e=>e.join(','))).size===bounded.edges.length);
  assert.ok(bounded.faces.every(f=>f.uses===1||f.uses===2));
  for(const route of M.routes) {
    const face=bounded.faces.find(f=>faceKey(f.vertices.map(i=>bounded.vertices[i]))===faceKey(route.nodes.map(n=>M.hex[n])));
    ck(route.id+'_remains_an_interior_face_after_radius_cutoff',face?.uses===2);
  }
  assert.throws(()=>M.boundedTetrahedralGrid(0),RangeError);
  ck('orthogonal_grid_rival_fails_the_hex_unit_triangle_metric',M.distanceSquared(M.lattice.M0,M.lattice.C1)===2);
  for(const angle of [-20,-10,0,10,20]) {
    const u=-Math.sqrt(5)*Math.tan(angle*Math.PI/180);
    ck('pentachoron_C2_strictly_inside_at_angle_'+angle,[(1+u)/4,(1-u)/4,(1+u)/4,(1-u)/4].every(w=>w>0));
    const weights=[(1+u)/4,(1-u)/4,(1+u)/4,(1-u)/4];
    const vertices=M.facet.map(n=>M.project4D(M.pentachoron[n],angle));
    near(M.project4D(M.pentachoron.C2,angle),[0,1,2].map(i=>vertices.reduce((sum,p,j)=>sum+weights[j]*p[i],0)));
  }
  assert.deepEqual(Object.keys(M.pentachoron),M.carriers);
  for(const [a,b] of M.simplexEdges)near([M.distanceSquared(M.pentachoron[a],M.pentachoron[b])],[8]);
  ck('proper_pentachoron_has_five_vertices_ten_edges_ten_faces_five_cells',Object.keys(M.pentachoron).length===5&&M.simplexEdges.length===10&&M.simplexFaces.length===10&&M.simplexCells.length===5);
  ck('proper_C2_is_a_vertex_distinct_from_the_barycenter',M.distanceSquared(M.pentachoron.C2,M.barycenter)>1);
  for(const route of M.routes)ck('proper_'+route.id+'_is_an_original_face',M.simplexFaces.some(f=>route.nodes.every(n=>f.includes(n))));
  for(const angle of [-70,-35,0,35,70]) {
    const basis=Array.from({length:4},(_,j)=>Array.from({length:4},(_,i)=>Number(i===j)));
    const columns=basis.map(v=>M.project4D(v,angle));
    const rows=Array.from({length:3},(_,i)=>columns.map(v=>v[i]));
    for(let i=0;i<3;i++)for(let j=0;j<3;j++)near([rows[i].reduce((s,x,k)=>s+x*rows[j][k],0)],[Number(i===j)]);
    for(const view of ['pentachoron','barycenter']) {
      for(const p of Object.values(M.coordinatesFor(view)))near(M.displayPoint(p,view,angle),M.project4D(p,angle));
      const centerImage=Object.values(M.pentachoron).map(p=>M.displayPoint(p,view,angle));
      near(M.displayPoint(M.barycenter,view,angle),[0,1,2].map(i=>centerImage.reduce((s,p)=>s+p[i],0)/5));
      const a=M.pentachoron.C1,b=M.pentachoron.C2;
      near(M.displayPoint(a.map((v,i)=>(v+b[i])/2),view,angle),M.displayPoint(a,view,angle).map((v,i)=>(v+M.displayPoint(b,view,angle)[i])/2));
    }
  }
  checks.four_to_three_projection_has_orthonormal_rows_at_five_angles=true;
  checks.all_four_dimensional_views_use_same_parallel_projection=true;
  checks.projection_preserves_midpoints_and_barycentric_averages=true;
  for(const p of Object.values(M.lattice))near(M.displayPoint(p,'lattice'),p);
  checks.lattice_coordinates_pass_to_the_camera_unchanged=true;
  for(const view of Object.keys(M.views))for(const [i,n] of M.walk.entries())near(M.pointOnWalk(i,M.coordinatesFor(view)),M.coordinatesFor(view)[n]);
  checks.same_walk_occurrences_interpolate_correctly_in_all_models=true;
  const files=['index.html','style.css','app.js','model.mjs','identity.mjs','identity-data.mjs','carrier.mjs','vendor/three.min.js','vendor/OrbitControls.js','vendor/THREE-LICENSE.txt'];
  for(const f of files) {
    const authored=f.startsWith('vendor/')?path.join(ROOT,'research/nima/demos/paw-cycle',f):path.join(ROOT,'research/strominger/demos/particle-overlap-tetrahedron',f);
    const expected=hash(await readFile(authored));
    for(const dir of ['public','website/public'])assert.equal(hash(await readFile(path.join(ROOT,dir,'experiments/particle-overlap-tetrahedron',f))),expected);
  }
  checks.both_public_roots_match_authored_assets_and_original_vendors=true;
  const types={'.html':'text/html','.js':'text/javascript','.mjs':'text/javascript','.css':'text/css','.txt':'text/plain'};
  const server=createServer(async(req,res)=>{
    try{const url=new URL(req.url,'http://127.0.0.1');let f=path.resolve(PUBLIC,'.'+decodeURIComponent(url.pathname));
      const relative=path.relative(PUBLIC,f);if(relative.startsWith('..')||path.isAbsolute(relative))throw new Error('path');
      if((await stat(f)).isDirectory())f=path.join(f,'index.html');res.setHeader('Content-Type',types[path.extname(f)]||'application/octet-stream');res.end(await readFile(f));
    }catch{res.writeHead(404);res.end('Not found');}
  });
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  const base='http://127.0.0.1:'+server.address().port;
  let browser;
  try {
    browser=await chromium.launch({headless:true,args:['--enable-webgl','--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
    const page=await browser.newPage({viewport:{width:1480,height:1040},deviceScaleFactor:1});
    const errors=[],external=[];page.on('pageerror',e=>errors.push(String(e)));
    page.on('request',r=>{if(!r.url().startsWith(base))external.push(r.url());});
    await page.goto(base+'/experiments/particle-overlap-tetrahedron/?view=barycenter',{waitUntil:'load'});
    await page.waitForFunction(()=>globalThis.ParticleOverlapViewer?.snapshot().frameCount>2);
    const snap=()=>page.evaluate(()=>globalThis.ParticleOverlapViewer.snapshot());
    async function labelsSeparate(label,names=M.carriers) {
      const boxes=await Promise.all(names.map(n=>page.locator(`[data-point="${n}"]`).boundingBox()));
      const separate=boxes.every((a,i)=>a&&boxes.slice(i+1).every(b=>b&&(a.x+a.width<=b.x||b.x+b.width<=a.x||a.y+a.height<=b.y||b.y+b.height<=a.y)));
      if(!separate){console.error(label,JSON.stringify(Object.fromEntries(names.map((n,i)=>[n,boxes[i]]))));await page.screenshot({path:path.join(OUT,'label-overlap-debug.png'),fullPage:true});}
      ck(label,separate);
    }
    async function assertOrthographic(view) {
      const s=await snap();
      ck(view+'_uses_actual_orthographic_camera',s.cameraType==='OrthographicCamera'&&s.state.projection==='orthographic'&&s.projectionMatrix[11]===0&&s.projectionMatrix[15]===1);
      near([(s.cameraFrustum.right-s.cameraFrustum.left)/(s.cameraFrustum.top-s.cameraFrustum.bottom)],[s.viewport[0]/s.viewport[1]]);
      const d=s.camera.map((v,i)=>v-s.cameraTarget[i]),norm=Math.hypot(...d),offset=d.map(v=>v/norm*.7);
      const projected=await page.evaluate(offset=>{
        const a=[.1,.2,.3],b=[1.1,.2,.3],farther=p=>p.map((v,i)=>v+offset[i]);
        return [a,b,farther(a),farther(b)].map(p=>globalThis.ParticleOverlapViewer.projectWorld(p).slice(0,2));
      },offset);
      near(projected[1].map((v,i)=>v-projected[0][i]),projected[3].map((v,i)=>v-projected[2][i]));
      checks[view+'_parallel_segments_keep_equal_scale_at_different_depths']=true;
    }
    async function assertZoom(view) {
      const box=await page.locator('#scene canvas').boundingBox(),before=(await snap()).cameraZoom;
      await page.mouse.move(box.x+box.width*.85,box.y+box.height*.5);await page.mouse.wheel(0,-160);
      await page.waitForFunction(before=>globalThis.ParticleOverlapViewer.snapshot().cameraZoom>before,before);
      ck(view+'_orthographic_wheel_zoom_works',(await snap()).cameraType==='OrthographicCamera');
      await page.locator('#reset-view').click();near([(await snap()).cameraZoom],[1]);
    }
    await assertOrthographic('barycenter');await assertZoom('barycenter');
    const initial=await snap();ck('actual_Three_WebGL_scene_draws',initial.webgl&&initial.renderCalls>10);
    near(initial.barycenter4D,M.barycenter);
    for(const route of M.routes){await page.locator(`[data-route="${route.id}"]`).click();const s=await snap();assert.equal(s.state.route,route.id);assert.equal(s.state.progress,route.start);assert.match(await page.locator('#detail-title').textContent(),new RegExp(route.name));}
    checks.all_three_window_controls_select_actual_scene_state=true;
    await page.locator('[data-route="all"]').click();await page.locator('[data-point="C1"]').click();
    assert.match(await page.locator('#detail-text').textContent(),/twice/);
    await page.locator('[data-occurrence="2"]').click();const firstC=await snap();
    await page.locator('[data-occurrence="4"]').click();const secondC=await snap();near(firstC.cursor4D,secondC.cursor4D);
    ck('two_C1_occurrences_return_to_identical_carrier',firstC.state.progress===2&&secondC.state.progress===4);
    await page.locator('#context').check();assert.equal((await snap()).state.context,true);
    await page.locator('[data-point="V4"]').click();assert.match(await page.locator('#detail-formula').textContent(),/√5/);
    await page.locator('#rays').check();assert.equal((await snap()).state.rays,true);
    await page.locator('#faces').uncheck();assert.equal((await snap()).state.faces,false);await page.locator('#faces').check();
    checks.context_rays_and_triangle_fill_toggles_work=true;
    await page.locator('#projection').evaluate(el=>{el.value='-50';el.dispatchEvent(new Event('input',{bubbles:true}));});
    const rotated=await snap();assert.equal(rotated.state.angle,-50);near(rotated.barycenter4D,initial.barycenter4D);
    checks.four_dimensional_projection_slider_preserves_original_coordinates=true;
    await page.locator('#projection').evaluate(el=>{el.value='35';el.dispatchEvent(new Event('input',{bubbles:true}));});
    await page.locator('#context').uncheck();await page.locator('#rays').uncheck();await page.locator('[data-route="all"]').click();
    await page.locator('#restart').click();await page.locator('#play').click();
    await page.waitForFunction(()=>globalThis.ParticleOverlapViewer.snapshot().state.progress===5,null,{timeout:12000});
    const final=await snap();ck('trace_stops_at_C2_for_next_series',final.state.playing===false);near(final.cursor4D,M.barycenter);
    await page.waitForTimeout(120);assert.equal((await snap()).state.progress,5);
    const canvas=page.locator('#scene canvas'),box=await canvas.boundingBox();
    const before=await snap();await page.mouse.move(box.x+box.width*.6,box.y+box.height*.65);await page.mouse.down();await page.mouse.move(box.x+box.width*.6+80,box.y+box.height*.65+35,{steps:8});await page.mouse.up();await page.waitForTimeout(200);
    const after=await snap();ck('OrbitControls_drag_changes_camera',Math.hypot(...before.camera.map((x,i)=>x-after.camera[i]))>.1);near(before.barycenter4D,after.barycenter4D);
    await page.locator('#reset-view').click();await page.locator('#restart').click();await page.waitForTimeout(300);
    await mkdir(OUT,{recursive:true});await page.screenshot({path:path.join(OUT,'desktop.png'),fullPage:true});
    await page.locator('[data-route="electron"]').click();await page.screenshot({path:path.join(OUT,'electron.png'),fullPage:true});
    await page.setViewportSize({width:430,height:930});await page.waitForTimeout(200);
    await page.locator('[data-route="all"]').click();await page.screenshot({path:path.join(OUT,'mobile.png'),fullPage:true});
    const overflow=await page.evaluate(()=>({width:innerWidth,scroll:document.documentElement.scrollWidth,elements:[...document.querySelectorAll('body *')].filter(el=>el.getBoundingClientRect().right>innerWidth+1).slice(0,8).map(el=>({tag:el.tagName,id:el.id,class:el.className,right:el.getBoundingClientRect().right}))}));
    if(overflow.scroll>overflow.width)console.error('Overflow evidence:',JSON.stringify(overflow));
    ck('mobile_layout_has_no_horizontal_overflow',overflow.scroll<=overflow.width);
    // New representations use the same UI and retain the legacy assertions above.
    for(const view of ['lattice','hex','pentachoron']) {
      const gridView=M.isLatticeView(view);
      await page.setViewportSize({width:1480,height:1040});
      await page.goto(base+'/experiments/particle-overlap-tetrahedron/?view='+view+'&geometry=chart',{waitUntil:'load'});
      await page.waitForFunction(()=>globalThis.ParticleOverlapViewer?.snapshot().frameCount>2);
      await assertOrthographic(view);await assertZoom(view);
      const s=await snap();assert.equal(s.state.view,view);assert.equal(s.geometry.pointCount,5);
      assert.deepEqual(s.coordinates,M.coordinatesFor(view));
      ck(view+'_direct_link_renders_real_WebGL',s.webgl&&s.renderCalls>10);
      ck(view+'_has_no_extra_V4_or_facet_center_label',await page.locator('[data-point="V4"]').isHidden()&&await page.locator('[data-point="O"]').isHidden());
      assert.match(await page.locator('#center-title').textContent(),gridView?/lattice endpoint/:/fifth pentachoron vertex/);
      for(const route of M.routes){await page.locator(`[data-route="${route.id}"]`).click();assert.equal((await snap()).state.route,route.id);assert.match(await page.locator('#detail-text').textContent(),view==='hex'?/Elementary triangular lattice cell/:gridView?/Codimension-layered lattice window/:/Original triangular pentachoron face/);}
      checks[view+'_all_three_windows_select_with_correct_role_text']=true;
      await page.locator('[data-occurrence="2"]').click();const a=await snap();
      await page.locator('[data-occurrence="4"]').click();near(a.cursor3D,(await snap()).cursor3D);
      checks[view+'_repeated_C1_occurrences_coincide']=true;
      await page.locator('#context').uncheck();assert.equal((await snap()).state.context,false);await page.locator('#context').check();
      if(view==='pentachoron') {
        for(const cell of M.simplexCells){await page.locator('#cell').selectOption(cell.id);assert.deepEqual((await snap()).geometry.cell,cell);}
        assert.match(await page.locator('#cell-note').textContent(),/Original boundary cell/);
        await page.locator('#cell').selectOption('none');
        ck('no_Schlegel_or_perspective_selector_remains',await page.locator('#projection-method').count()===0);
        assert.equal((await snap()).state.angle,0);near((await snap()).projected.C2,[0,0,0]);
        assert.equal(await page.locator('#projection').getAttribute('min'),'-20');
        assert.equal(await page.locator('#projection').getAttribute('max'),'20');
        for(const angle of [-20,20]) {
          await page.locator('#projection').evaluate((el,angle)=>{el.value=angle;el.dispatchEvent(new Event('input',{bubbles:true}));},angle);
          const rotated=await snap();near(rotated.projected.C2,M.project4D(M.pentachoron.C2,angle));assert.deepEqual(rotated.coordinates,M.pentachoron);
        }
        checks.UI_limits_keep_C2_inside_the_projected_volume=true;
        await page.locator('#projection').evaluate(el=>{el.value='0';el.dispatchEvent(new Event('input',{bubbles:true}));});
        near((await snap()).projected.C2,[0,0,0]);
        checks.all_five_original_cells_and_orthogonal_4D_rotation_work=true;
      } else {
        const axes=await page.locator('[data-role="axis"]:visible').count();
        if(axes!==3)await page.screenshot({path:path.join(OUT,'lattice-axis-debug.png'),fullPage:true});
        ck(view+'_has_expected_axis_labels_and_no_4D_slider',axes===(view==='hex'?6:3)&&await page.locator('#projection').isHidden());
        assert.match(await page.locator('#view-description').textContent(),/xz plane/);
        if(view==='hex') {
          assert.deepEqual((await page.locator('[data-role="axis"]:visible').allTextContents()).sort(),['a₁','a₂','b₁','b₂','c₁','c₂']);
          assert.deepEqual(s.axisLabels,M.tetraAxisLabels);
          for(const [key,direction] of Object.entries(M.tetraAxisDirections))near(s.axisDirections[key],direction);
          checks.actual_six_axis_arrows_match_the_three_opposite_pairs=true;
          assert.deepEqual(s.hexBasis,M.hexBasis);assert.deepEqual(s.hexAxialCoordinates,M.lattice);
          assert.deepEqual(s.latticeAxes,M.hexAxes);
          assert.equal(s.geometry.triangleGrid,null);
          assert.equal(s.geometry.tetraGrid.latticeObjectCount,1);
          assert.equal(s.geometry.tetraGrid.radius,4);assert.deepEqual(s.geometry.tetraGrid.center,[0,0,0]);
          ck('single_rendered_lattice_stays_inside_four_unit_radius',s.geometry.tetraGrid.maxRadius<=4+1e-6);
          near(s.cameraTarget,[0,0,0]);
          const projected=await page.evaluate(vertices=>vertices.map(p=>globalThis.ParticleOverlapViewer.projectWorld(p)),bounded.vertices);
          ck('whole_bounded_lattice_fits_in_initial_view',projected.every(p=>Math.abs(p[0])<.93&&Math.abs(p[1])<.93&&Math.abs(p[2])<1));
          ck('actual_rendered_coordinate_lines_contain_every_window_edge',s.geometry.tetraGrid.routeEdgesPresent);
          assert.equal(s.geometry.tetraGrid.tetrahedronCount,bounded.tetrahedra.length);
          assert.equal(s.geometry.tetraGrid.vertexCount,bounded.vertices.length);
          assert.equal(s.geometry.tetraGrid.edgeCount,bounded.edges.length);
          assert.equal(s.geometry.tetraGrid.segmentCount,bounded.edges.length);
          ck('actual_rendered_tetrahedral_lattice_has_volume_on_both_sides',s.geometry.tetraGrid.bounds[0][1]<0&&s.geometry.tetraGrid.bounds[1][1]>0);
          assert.match(await page.locator('#view-description').textContent(),/one elementary coordinate-grid triangle/);
          await page.locator('#faces').uncheck();assert.equal((await snap()).state.faces,false);await page.locator('#faces').check();
          checks.hex_retains_triangle_fill_control=true;
        }
        assert.match(await page.locator('#center-note').textContent(),/All five carriers have y = 0/);
        assert.deepEqual((await snap()).cameraUp,[0,0,1]);
        async function layerOrder() {
          return page.evaluate(()=>{
            const v=globalThis.ParticleOverlapViewer,s=v.snapshot();
            const height=n=>v.projectWorld(s.coordinates[n])[1];
            return Math.min(height('M0'),height('M1'))>Math.max(height('C0'),height('C1'),height('C2'));
          });
        }
        ck(view+'_M_layer_is_visibly_above_C_layer_on_open',await layerOrder());
        const polarAngles=[];
        for(const dy of [-160,160]) {
          await page.locator('#reset-view').click();
          const box=await page.locator('#scene canvas').boundingBox();
          const x=box.x+box.width*.8,y=box.y+box.height*.5;
          await page.mouse.move(x,y);await page.mouse.down();await page.mouse.move(x+75,y+dy,{steps:8});await page.mouse.up();await page.waitForTimeout(250);
          const s=await snap(),d=s.camera.map((v,i)=>v-s.cameraTarget[i]);
          polarAngles.push(Math.acos(d.reduce((sum,v,i)=>sum+v*s.cameraUp[i],0)/Math.hypot(...d)));
          assert.deepEqual(s.coordinates,M.coordinatesFor(view));
        }
        ck(view+'_orbit_can_tilt_above_20_degrees',Math.min(...polarAngles)<70*Math.PI/180);
        ck(view+'_orbit_can_go_below_the_carrier_plane',Math.max(...polarAngles)>Math.PI/2);
        await page.locator('#reset-view').click();
        const limits=(await snap()).orbitPolarLimits;near(limits,[0,Math.PI]);
        checks[view+'_has_no_custom_polar_tilt_restriction']=true;
      }
      await page.locator('[data-route="all"]').click();await page.locator('#restart').click();await page.waitForTimeout(180);
      await labelsSeparate(view+'_desktop_point_labels_do_not_overlap');
      if(view==='hex')await labelsSeparate('tetrahedral_desktop_axis_labels_do_not_overlap_carriers',[...M.carriers,...Object.keys(M.tetraAxisLabels)]);
      await page.screenshot({path:path.join(OUT,view+'-desktop.png'),fullPage:true});
      await page.locator('#progress').evaluate(el=>{el.value='4.85';el.dispatchEvent(new Event('input',{bubbles:true}));});
      await page.locator('#play').click();
      await page.waitForFunction(()=>globalThis.ParticleOverlapViewer.snapshot().state.progress===5,null,{timeout:3000});
      const endpoint=await snap();near(endpoint.cursor4D,M.coordinatesFor(view).C2);assert.equal(endpoint.state.playing,false);
      checks[view+'_trace_reaches_its_own_C2_and_stops']=true;
      await page.setViewportSize({width:430,height:930});
      await page.goto(base+'/experiments/particle-overlap-tetrahedron/?view='+view+'&geometry=chart',{waitUntil:'load'});
      await page.waitForFunction(()=>globalThis.ParticleOverlapViewer?.snapshot().frameCount>2);
      await assertOrthographic(view+'_mobile');
      ck(view+'_fresh_mobile_layout_has_no_overflow',await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
      for(const n of M.carriers)ck(view+'_mobile_label_'+n+'_is_visible',await page.locator(`[data-point="${n}"]`).isVisible());
      await labelsSeparate(view+'_mobile_point_labels_do_not_overlap');
      if(view==='hex')await labelsSeparate('tetrahedral_mobile_axis_labels_do_not_overlap_carriers',[...M.carriers,...Object.keys(M.tetraAxisLabels)]);
      await page.screenshot({path:path.join(OUT,view+'-mobile.png'),fullPage:true});
    }
    await page.locator('[data-route="electron"]').click();
    await page.locator('#progress').evaluate(el=>{el.value='4.25';el.dispatchEvent(new Event('input',{bubbles:true}));});
    await page.locator('[data-point="C2"]').click();
    for(const view of ['lattice','hex','barycenter','pentachoron','hex','lattice','pentachoron']) {
      await page.locator(`[data-view="${view}"]`).click();const s=await snap();
      assert.equal(s.state.view,view);assert.equal(s.state.route,'electron');assert.equal(s.state.progress,4.25);
      assert.deepEqual(s.cameraUp,M.isLatticeView(view)?[0,0,1]:[0,1,0]);
      if(M.isLatticeView(view))assert.deepEqual((await page.locator('[data-role="axis"]:visible').allTextContents()).sort(),view==='hex'?['a₁','a₂','b₁','b₂','c₁','c₂']:['x','y','z']);
      near(s.cursor4D,M.pointOnWalk(4.25,M.coordinatesFor(view)));
      assert.equal(new URL(page.url()).searchParams.get('view'),view);
      assert.equal(await page.locator('#detail-title').textContent(),M.views[view].centerTitle);
    }
    checks.view_switch_preserves_route_occurrence_and_updates_URL_and_C2_role=true;
    ck('invalid_view_rejected_without_state_mutation',await page.evaluate(()=>{try{globalThis.ParticleOverlapViewer.selectView('wrong');return false;}catch{return globalThis.ParticleOverlapViewer.snapshot().state.view==='pentachoron';}}));
    ck('browser_has_zero_external_network_dependencies',external.length===0);
    ck('browser_has_zero_script_errors',errors.length===0);
    const pins={};for(const f of [...files,'../../../research/strominger/checkers/check_particle_overlap_viewer.mjs']){
      const p=f.startsWith('../')?path.join(ROOT,'research/strominger/checkers/check_particle_overlap_viewer.mjs'):path.join(ROOT,'public/experiments/particle-overlap-tetrahedron',f);pins[path.relative(ROOT,p).replaceAll('\\','/')]=hash(await readFile(p));
    }
    const screenshots=['desktop.png','electron.png','mobile.png','lattice-desktop.png','lattice-mobile.png','hex-desktop.png','hex-mobile.png','pentachoron-desktop.png','pentachoron-mobile.png'];
    await writeFile(path.join(OUT,'verification.json'),JSON.stringify({status:'pass',checks,chromium_version:browser.version(),route:'/experiments/particle-overlap-tetrahedron/',representations:Object.keys(M.views),screenshots,source_sha256:pins,scope:M.placementScope},null,2)+'\n');
    console.log(JSON.stringify({status:'pass',check_groups:Object.keys(checks).length,screenshots,browser:browser.version()}));
  }finally{await browser?.close();await new Promise(resolve=>server.close(resolve));}
}
main().catch(e=>{console.error(e);process.exitCode=1;});
