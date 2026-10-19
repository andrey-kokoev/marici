import assert from 'node:assert/strict';
import {createServer} from 'node:http';
import {readFile,writeFile,mkdir,stat,copyFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {chromium} from '@playwright/test';
import {frameAt,latticePatch,makeSpace,axisLabel} from '../demos/particle-overlap-tetrahedron/vacuum-model.mjs';
import {latticeCarriers} from '../demos/particle-overlap-tetrahedron/vacuum-carriers.mjs';
import {trial,orientedVolume} from '../demos/particle-overlap-tetrahedron/carrier.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const source='research/strominger/demos/particle-overlap-tetrahedron';
const out=path.join(root,'research/strominger/results/vacuum-space-viewer');
const checks={},check=(name,condition)=>{assert.ok(condition,name);checks[name]=true;};
const near=(a,b)=>Math.abs(a-b)<1e-10;
const dist=(a,b)=>Math.hypot(...a.map((x,i)=>x-b[i]));
const hash=bytes=>createHash('sha256').update(bytes).digest('hex');
let browser,server;
try {
  await mkdir(out,{recursive:true});
  const prior=await readFile(path.join(out,'verification.json'),'utf8').catch(()=>null);
  if(prior&&JSON.parse(prior).checks.combined_carrier_overlay_preserves_three_bodies_six_vertices_two_shared_faces) {
    await writeFile(path.join(out,'verification-overlay-v6.json'),prior);
    for(const name of ['lone-proton-scene','lone-neutron-scene','lone-electron-scene','all-carriers-scene','all-carriers-mobile-scene'])
      await copyFile(path.join(out,name+'.png'),path.join(out,name+'-overlay-v6.png'));
  }
  const patch=latticePatch();
  check('hexagonal_patch_has_37_sites',patch.sites.length===37);
  check('default_realization_step_rotates_60_degrees',makeSpace().parameters.turn===60&&frameAt(1).angle-frameAt(0).angle===60);
  const plain=makeSpace();
  check('seven_discrete_R_levels_and_no_occupants',plain.frames.length===7&&plain.frames.every(f=>Number.isInteger(f.level))&&plain.occupants.length===0);
  check('normal_axis_is_R_realization',plain.normalAxis.name==='R'&&plain.normalAxis.meaning==='realization'&&plain.transition.includes('R[n]'));
  check('two_M_C_axes_and_one_C_M_axis',plain.frames.every(f=>f.axes.map(a=>a.roles.join('|')).join(',')==='M|C,M|C,C|M'));
  const flipped=makeSpace({assignment:'CCM'});
  check('reference_XOR_exchanges_all_roles_at_every_level',plain.frames.every((f,i)=>f.axes.every((a,j)=>a.role!==flipped.frames[i].axes[j].role)));
  check('even_R_has_two_M_and_odd_R_has_two_C',plain.frames.every(f=>f.axes.map(a=>a.role).join('')===(f.level%2===0?'MMC':'CCM')));
  check('every_adjacent_R_step_exchanges_all_roles',plain.frames.slice(1).every((f,i)=>f.axes.every((a,j)=>a.role!==plain.frames[i].axes[j].role)));
  check('negative_and_positive_R_obey_the_same_exchange_rule',[-5,-3,-1,1,3,5].every(level=>frameAt(level).assignment==='CCM')&&[-4,-2,0,2,4].every(level=>frameAt(level).assignment==='MMC'));
  check('role_assignment_does_not_move_the_geometry',JSON.stringify(plain.frames.map(f=>f.points))===JSON.stringify(flipped.frames.map(f=>f.points)));
  check('each_axis_has_independent_positive_and_negative_signs',plain.frames.every(f=>f.axes.every(a=>axisLabel(a,1)===a.role+'+'&&axisLabel(a,-1)===a.role+'-')));
  check('exceptional_axis_rotates_and_its_role_exchanges',exceptionalAxisExchanges());
  function exceptionalAxisExchanges(){const a=frameAt(0,{turn:120}),b=frameAt(1,{turn:120});return a.axes[2].role==='C'&&b.axes[2].role==='M'&&dist(a.axes[2].direction,b.axes[2].direction)>1;}
  check('three_geometrically_equivalent_unit_axes_normal_to_R',plain.frames.every(f=>f.axes.every(a=>near(Math.hypot(...a.direction),1)&&a.direction[1]===0)&&f.axes.every((a,i)=>near(a.direction.reduce((s,x,k)=>s+x*f.axes[(i+1)%3].direction[k],0),-.5))));
  check('three_axes_sum_to_zero',plain.frames.every(f=>[0,1,2].every(k=>near(f.axes.reduce((s,a)=>s+a.direction[k],0),0))));
  check('all_patch_edges_have_unit_length',plain.frames.every(f=>patch.edges.every(([a,b])=>near(dist(f.points[a],f.points[b]),1))));
  check('sites_stay_on_their_declared_R_level',plain.frames.every(f=>f.points.every(p=>near(p[1],f.level*plain.parameters.spacing))));
  for(const turn of [-120,-30,0,30,60,120]) {
    const s=makeSpace({turn,initialAngle:17});
    assert.ok(s.frames.slice(1).every((f,i)=>near(f.angle-s.frames[i].angle,turn)));
  }
  checks.adjacent_frames_obey_previous_orientation_plus_declared_turn=true;
  const f0=frameAt(0,{turn:120}),f1=frameAt(1,{turn:120}),f3=frameAt(3,{turn:120});
  check('120_degree_step_permutes_axes_and_three_steps_restore_geometric_frame',dist(f1.axes[0].direction,f0.axes[1].direction)<1e-10&&f3.axes.every((a,i)=>dist(a.direction,f0.axes[i].direction)<1e-10));
  check('three_geometric_steps_do_not_silently_restore_role_types',f3.assignment!==f0.assignment&&frameAt(6,{turn:120}).assignment===f0.assignment);
  const reverse=frameAt(-1,{turn:30});
  check('negative_R_levels_use_inverse_rotation',near(reverse.angle,-30));
  assert.throws(()=>frameAt(.5));assert.throws(()=>makeSpace({spacing:0}));assert.throws(()=>makeSpace({halfLevels:1.5}));
  checks.non_discrete_levels_and_invalid_geometry_rejected=true;
  assert.throws(()=>makeSpace({assignment:'MMM'}));assert.throws(()=>makeSpace({assignment:'MCM'}));assert.throws(()=>axisLabel(plain.frames[0].axes[0],0));
  checks.independent_axis_role_choices_and_invalid_signs_are_rejected=true;
  const allCarriers=latticeCarriers(plain,'all');
  const boundToNodes=(cells,space)=>Object.entries(cells.points).every(([name,p])=>{
    const address=cells.bindings[name],frame=space.frames.find(f=>f.level===address.level);
    return frame&&p===frame.points[address.siteIndex]&&space.patch.sites[address.siteIndex][0]===address.q&&space.patch.sites[address.siteIndex][1]===address.r;
  });
  check('all_carrier_vertices_are_exact_lattice_node_references',boundToNodes(allCarriers,plain));
  check('lattice_prism_preserves_three_cells_six_vertices_and_two_shared_faces',allCarriers.bodies.length===3&&Object.keys(allCarriers.points).length===6&&allCarriers.edges.length===12&&allCarriers.sharedFaces.length===2);
  const cellVolume=Math.sqrt(3)*plain.parameters.spacing/12;
  check('three_cells_partition_the_elementary_prism_volume',near(allCarriers.bodies.reduce((s,b)=>s+b.volume,0),Math.sqrt(3)*plain.parameters.spacing/4));
  const side=(face,apex)=>orientedVolume([...face,apex],allCarriers.points);
  check('shared_faces_have_opposite_apices_and_disjoint_cell_interiors',side(['M0','C1','M1'],'C0')*side(['M0','C1','M1'],'C2')<0&&side(['M1','C1','C2'],'M0')*side(['M1','C1','C2'],'M2')<0&&side(['M0','C1','M1'],'C0')*side(['M0','C1','M1'],'M2')<0);
  for(const turn of [-120,-60,0,60,120])for(const spacing of [.6,1.1,2])for(const level of [-3,-2,0,1,3]) {
    const space=makeSpace({turn,spacing,initialAngle:17}),cells=latticeCarriers(space,'all',level);
    assert.equal(cells.status,'constructed');assert.ok(boundToNodes(cells,space));assert.ok(cells.bodies.every(body=>near(body.volume,Math.sqrt(3)*spacing/12)));
  }
  checks.lattice_membership_and_cell_volumes_survive_rotation_spacing_and_R_boundary_cases=true;
  const blocked=latticeCarriers(makeSpace({turn:30}),'all');
  check('non_lattice_rotation_is_blocked_instead_of_snapped',blocked.status==='blocked'&&blocked.bodies.length===0&&Object.keys(blocked.points).length===0);
  for(const id of ['proton','neutron','electron']) {
    const lone=latticeCarriers(plain,id),body=lone.bodies[0];
    assert.equal(lone.bodies.length,1);assert.equal(body.id,id);assert.equal(body.nodes.length,4);assert.equal(Object.keys(lone.points).length,4);assert.equal(lone.edges.length,6);
    assert.ok(boundToNodes(lone,plain));
    for(const [name,p] of Object.entries(lone.points))assert.deepEqual(p,allCarriers.points[name]);
    assert.ok(near(body.volume,cellVolume));
  }
  checks.lone_views_select_one_lattice_cell_without_repositioning=true;
  check('empty_mode_contains_no_carrier_nodes_or_edges',latticeCarriers(plain,'none').bodies.length===0&&Object.keys(latticeCarriers(plain,'none').points).length===0);
  assert.throws(()=>latticeCarriers(plain,'unknown'));checks.invalid_occupant_selection_is_rejected=true;
  const source_sha256={};
  for(const file of ['vacuum.html','vacuum.css','vacuum-model.mjs','vacuum-app.js','vacuum-carriers.mjs','planes.html','carrier.mjs','model.mjs']) {
    const bytes=await readFile(path.join(root,source,file));source_sha256[source+'/'+file]=hash(bytes);
    for(const dir of ['public','website/public'])assert.equal(hash(await readFile(path.join(root,dir,'experiments/particle-overlap-tetrahedron',file))),hash(bytes));
  }
  checks.both_public_mirrors_match_owned_sources=true;
  const mime={'.html':'text/html','.js':'text/javascript','.mjs':'text/javascript','.css':'text/css'};
  const publicRoot=path.join(root,'public');
  server=createServer(async(req,res)=>{try {
    let file=path.resolve(publicRoot,'.'+new URL(req.url,'http://localhost').pathname);
    if(path.relative(publicRoot,file).startsWith('..'))throw Error('path');
    if((await stat(file)).isDirectory())file=path.join(file,'index.html');
    res.setHeader('Content-Type',mime[path.extname(file)]||'text/plain');res.end(await readFile(file));
  }catch{res.writeHead(404);res.end();}});
  await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
  browser=await chromium.launch({headless:true,args:['--enable-webgl','--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
  const page=await browser.newPage({viewport:{width:1480,height:1040},hasTouch:true}),errors=[];
  page.on('pageerror',error=>errors.push(String(error)));
  const base=process.argv.find(arg=>arg.startsWith('--base-url='))?.slice('--base-url='.length)||'http://127.0.0.1:'+server.address().port;
  await page.goto(base+'/experiments/particle-overlap-tetrahedron/planes.html');
  await page.waitForFunction(()=>globalThis.VacuumSpaceViewer?.snapshot().frameCount>2);
  const snapshot=()=>page.evaluate(()=>globalThis.VacuumSpaceViewer.snapshot());
  let s=await snapshot();
  check('browser_defaults_to_60_degree_R_steps',s.state.turn===60&&s.space.frames.slice(1).every((f,i)=>near(f.angle-s.space.frames[i].angle,60)));
  check('browser_renders_empty_space_with_seven_frames',s.webgl&&s.renderCalls>0&&s.renderedFrameCount===7&&s.renderedSegments>0&&s.occupantCount===0&&s.particlePathCount===0);
  check('three_central_planes_have_concrete_signed_labels',s.typedLabels.length===18&&[-1,0,1].every(level=>{
    const labels=s.typedLabels.filter(l=>l.level===level).map(l=>l.text);
    return ['M+','M-'].every(text=>labels.filter(l=>l===text).length===(level%2===0?2:1))&&['C+','C-'].every(text=>labels.filter(l=>l===text).length===(level%2===0?1:2));
  }));
  const planeStyle=(snapshot,level)=>snapshot.planeFormatting.filter(p=>p.level===level).map(({part,opacity,color})=>({part,opacity,color}));
  check('R_minus_one_and_plus_one_match_R_zero_actual_materials',[-1,1].every(level=>JSON.stringify(planeStyle(s,level))===JSON.stringify(planeStyle(s,0)))&&planeStyle(s,0).length===5);
  check('schema_alternatives_are_not_rendered_as_labels',s.typedLabels.every(l=>/^[MC][+-]$/.test(l.text)));
  check('visible_realization_axis_replaces_Y',s.normalAxis.name==='R'&&/R = 0/.test(await page.locator('#level-readout').textContent())&&!/\bY\b/.test(await page.locator('body').innerText()));
  await page.locator('#assignment').selectOption('CCM');s=await snapshot();
  check('browser_reference_switch_inverts_the_alternating_sequence',s.state.assignment==='CCM'&&s.space.frames.every(f=>f.axes.map(a=>a.role).join('')===(f.level%2===0?'CCM':'MMC')));
  check('reference_XOR_exchanges_the_repeated_pair_on_each_plane',[-1,0,1].every(level=>{
    const labels=s.typedLabels.filter(l=>l.level===level).map(l=>l.text);
    return ['C+','C-'].every(text=>labels.filter(l=>l===text).length===(level%2===0?2:1))&&['M+','M-'].every(text=>labels.filter(l=>l===text).length===(level%2===0?1:2));
  }));
  await page.locator('#assignment').selectOption('MMC');
  check('particle_controls_and_labels_absent',await page.locator('[data-route],[data-point],.identity-panel,.walk-panel').count()===0);
  await page.screenshot({path:path.join(out,'empty-space-desktop.png'),fullPage:true});
  await page.locator('#scene').screenshot({path:path.join(out,'empty-space-scene.png')});
  const loneSnapshots={};
  for(const id of ['proton','neutron','electron']) {
    await page.locator(`[data-occupants="${id}"]`).click();s=await snapshot();loneSnapshots[id]=s;
    assert.equal(s.occupantCount,1);assert.equal(s.renderedCarrierBodies.length,1);assert.equal(s.renderedCarrierBodies[0].id,id);assert.equal(s.renderedCarrierNodeNames.length,4);
    const body=s.occupantOverlay.bodies[0],actual=s.renderedCarrierBodies[0];assert.equal(actual.triangles,4);
    const points=Object.fromEntries(body.nodes.map((name,i)=>[name,actual.positions.slice(i*3,i*3+3)]));
    assert.ok(Math.abs(Math.abs(orientedVolume(body.nodes,points))-cellVolume)<1e-6);
    assert.deepEqual(s.renderedCarrierNodeNames.slice().sort(),trial.bodies.find(b=>b.id===id).nodes.slice().sort());
    for(const [name,address] of Object.entries(s.occupantOverlay.bindings)) {
      const node=s.space.frames.find(f=>f.level===address.level).points[address.siteIndex];
      assert.deepEqual(s.occupantOverlay.points[name],node);assert.ok(dist(points[name],node)<1e-6);
    }
    assert.equal(await page.locator(`[data-occupants="${id}"]`).getAttribute('aria-pressed'),'true');
    assert.equal(await page.locator('#node-bindings li').count(),4);
    await page.locator('#focus-carriers').click();
    const focused=await snapshot();assert.deepEqual(focused.occupantOverlay.points,s.occupantOverlay.points);
    assert.equal(focused.cameraZoom,3);assert.ok(Object.values(focused.projectedCarrierNodes).every(p=>Math.abs(p[0])<.95&&Math.abs(p[1])<.95));
    await page.locator('#scene').screenshot({path:path.join(out,`lone-${id}-scene.png`)});
    await page.locator('#reset-view').click();
  }
  checks.each_lone_selector_renders_exactly_its_own_four_vertex_body=true;
  checks.actual_carrier_meshes_have_four_faces_and_predicted_lattice_cell_volume=true;
  checks.every_rendered_carrier_vertex_is_a_real_lattice_node=true;
  await page.locator('[data-occupants="all"]').click();s=await snapshot();
  check('all_three_selector_renders_three_connected_source_carriers',s.occupantCount===3&&s.renderedCarrierBodies.length===3&&s.renderedCarrierNodeNames.length===6&&s.occupantOverlay.sharedFaces.length===2);
  for(const previous of Object.values(loneSnapshots))for(const [name,p] of Object.entries(previous.occupantOverlay.points))assert.deepEqual(p,s.occupantOverlay.points[name]);
  checks.switching_between_lone_and_combined_views_does_not_move_source_vertices=true;
  await page.locator('#focus-carriers').click();
  const focusedAll=await snapshot();
  check('focus_enlarges_cells_by_camera_only_and_keeps_all_vertices_in_frame',focusedAll.cameraZoom===3&&JSON.stringify(focusedAll.occupantOverlay.points)===JSON.stringify(s.occupantOverlay.points)&&Object.values(focusedAll.projectedCarrierNodes).every(p=>Math.abs(p[0])<.95&&Math.abs(p[1])<.95));
  check('all_six_lattice_addresses_are_visible_in_inspector',await page.locator('#node-bindings li').count()===6);
  await page.locator('#scene').screenshot({path:path.join(out,'all-carriers-scene.png')});
  await page.locator('#reset-view').click();
  await page.evaluate(()=>globalThis.VacuumSpaceViewer.setState({level:1}));s=await snapshot();
  check('carrier_selection_survives_R_frame_changes',s.state.occupants==='all'&&s.occupantOverlay.level===1&&s.occupantCount===3&&s.occupantOverlay.bodies.every(b=>near(b.volume,cellVolume)));
  await page.evaluate(()=>globalThis.VacuumSpaceViewer.setState({level:0}));
  await page.locator('[data-turn="30"]').click();s=await snapshot();
  check('UI_reports_unsewn_lattice_rotation_without_rendering_fake_cells',s.occupantOverlay.status==='blocked'&&s.renderedCarrierBodies.length===0&&/no vertices are snapped/.test(await page.locator('#occupant-readout').textContent()));
  await page.locator('[data-turn="60"]').click();check('admitted_rotation_restores_lattice_cells',(await snapshot()).occupantCount===3);
  await page.locator('[data-occupants="none"]').click();s=await snapshot();
  check('empty_selector_removes_all_carrier_bodies_and_labels',s.occupantCount===0&&s.renderedCarrierBodies.length===0&&s.renderedCarrierNodeNames.length===0&&await page.locator('.vacuum-label.carrier,.vacuum-label.carrier-node').count()===0);
  check('invalid_UI_occupant_choice_does_not_mutate_state',await page.evaluate(()=>{try{globalThis.VacuumSpaceViewer.setState({occupants:'unknown'});return false;}catch{return globalThis.VacuumSpaceViewer.snapshot().state.occupants==='none';}}));
  const planeButton=level=>page.locator(`button.vacuum-label.level[data-level="${level}"]`);
  check('all_R_labels_are_accessible_plane_toggle_buttons',await page.locator('button.vacuum-label.level[aria-pressed]').count()===7);
  await planeButton(0).click();s=await snapshot();
  check('R_label_click_replaces_full_plane_with_traces',!s.state.fullLevels.includes(0)&&s.state.level===0&&s.typedLabels.every(l=>l.level!==0)&&planeStyle(s,0).every(p=>p.part!=='boundary')&&planeStyle(s,0).find(p=>p.part==='grid').opacity===.12);
  await planeButton(0).click();s=await snapshot();
  check('second_label_click_restores_full_plane',s.fullPlaneLevels.join(',')==='-1,0,1'&&s.typedLabels.length===18&&planeStyle(s,0).some(p=>p.part==='boundary'));
  await planeButton(2).click();s=await snapshot();
  check('outer_plane_can_be_enabled_without_selecting_it',s.fullPlaneLevels.includes(2)&&s.state.level===0&&s.typedLabels.filter(l=>l.level===2).length===6&&await planeButton(2).getAttribute('aria-pressed')==='true');
  await page.locator('[data-turn="120"]').click();s=await snapshot();
  check('plane_visibility_survives_frame_rebuild',s.state.fullLevels.includes(2)&&s.typedLabels.filter(l=>l.level===2).length===6);
  await page.locator('[data-turn="60"]').click();
  await planeButton(2).focus();await page.keyboard.press('Enter');
  check('keyboard_can_hide_plane_and_retains_label_focus',!(await snapshot()).state.fullLevels.includes(2)&&await planeButton(2).evaluate(el=>el===document.activeElement));
  await page.keyboard.press('Space');
  check('keyboard_can_restore_plane', (await snapshot()).state.fullLevels.includes(2));
  await planeButton(2).click();
  for(const level of [-2,2]) {
    let node=await page.evaluate(level=>globalThis.VacuumSpaceViewer.projectLevel(level),level);
    await page.mouse.click(node.x,node.y);s=await snapshot();
    assert.ok(s.state.fullLevels.includes(level));assert.equal(s.typedLabels.filter(l=>l.level===level).length,6);
    node=await page.evaluate(level=>globalThis.VacuumSpaceViewer.projectLevel(level),level);
    await page.mouse.click(node.x,node.y);assert.ok(!(await snapshot()).state.fullLevels.includes(level));
  }
  checks.positive_and_negative_R_nodes_toggle_their_own_planes=true;
  const node=await page.evaluate(()=>globalThis.VacuumSpaceViewer.projectLevel(2));
  const visibilityBeforeDrag=(await snapshot()).state.fullLevels;
  await page.mouse.move(node.x,node.y);await page.mouse.down();await page.mouse.move(node.x+35,node.y+15,{steps:6});await page.mouse.move(node.x,node.y,{steps:6});await page.mouse.up();
  assert.deepEqual((await snapshot()).state.fullLevels,visibilityBeforeDrag);
  checks.orbit_drag_from_node_does_not_toggle_even_when_returning_to_start=true;
  await page.locator('#reset-view').click();
  await page.locator('#next-level').click();s=await snapshot();
  check('R_step_selects_next_linked_frame',s.state.level===1&&await page.locator('#angle-readout').textContent()==='0° → 60° (Δ 60°)' );
  check('R1_readout_has_one_M_axis_and_two_C_axes',await page.locator('#axis-pattern').textContent()==='2 × C± + 1 × M±'&&await page.locator('#assignment-readout').textContent()==='R = 1: (C, C, M)');
  check('selection_does_not_change_central_plane_formatting',[-1,1].every(level=>JSON.stringify(planeStyle(s,level))===JSON.stringify(planeStyle(s,0)))&&s.typedLabels.length===18);
  for(const angle of [0,60,120,30]) {
    await page.locator(`[data-turn="${angle}"]`).click();s=await snapshot();assert.equal(s.state.turn,angle);
    assert.ok(s.space.frames.every(f=>near(f.angle,f.level*angle)));
  }
  checks.rotation_comparisons_rebuild_using_one_shared_rule=true;
  await page.locator('#stack').uncheck();s=await snapshot();
  check('single_frame_view_preserves_underlying_space',s.renderedFrameCount===1&&s.space.frames.length===7&&s.typedLabels.length===6&&s.typedLabels.every(l=>l.level===1));
  await page.locator('#stack').check();
  await page.evaluate(()=>globalThis.VacuumSpaceViewer.setState({initialAngle:25,turn:-30,level:-2}));s=await snapshot();
  check('initial_orientation_and_reverse_turn_apply_to_every_level',s.space.frames.every(f=>near(f.angle,25-30*f.level)));
  check('invalid_fractional_selection_is_rejected_without_state_change',await page.evaluate(()=>{try{globalThis.VacuumSpaceViewer.setState({level:.5});return false;}catch{return globalThis.VacuumSpaceViewer.snapshot().state.level===-2;}}));
  await page.evaluate(()=>globalThis.VacuumSpaceViewer.setState({halfLevels:1,level:5}));s=await snapshot();
  check('selected_level_clamps_to_display_extent',s.state.level===1&&s.space.frames.length===3&&await page.locator('#next-level').isDisabled());
  await page.evaluate(()=>globalThis.VacuumSpaceViewer.setState({halfLevels:3,level:0,turn:60,initialAngle:0}));
  await page.locator('#links').uncheck();await page.locator('#grid').uncheck();s=await snapshot();
  check('guides_and_lattice_can_be_hidden_independently',!s.state.links&&!s.state.grid&&s.renderedSegments>0);
  await page.locator('#links').check();await page.locator('#grid').check();
  await page.locator('#top-view').click();s=await snapshot();
  check('look_along_R_is_available',s.camera[1]===18&&near(s.camera[0],0));
  await page.locator('#reset-view').click();
  const canvas=page.locator('canvas');await canvas.hover();await page.mouse.down();await page.mouse.move(600,380,{steps:8});await page.mouse.up();
  check('orbit_controls_change_camera',dist((await snapshot()).camera,[10,8,12])>.1);
  await page.locator('#reset-view').click();
  await page.setViewportSize({width:430,height:930});await page.waitForTimeout(150);
  check('mobile_layout_has_no_horizontal_overflow',await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  check('mobile_shows_signed_labels_on_all_three_central_planes',await page.locator('.vacuum-label.typed:visible').count()===18);
  await planeButton(-1).tap();check('mobile_R_label_toggles_plane',!(await snapshot()).state.fullLevels.includes(-1));
  await planeButton(-1).tap();
  await page.screenshot({path:path.join(out,'empty-space-mobile.png'),fullPage:true});
  await page.locator('#scene').screenshot({path:path.join(out,'empty-space-mobile-scene.png')});
  await page.locator('[data-occupants="all"]').tap();s=await snapshot();
  check('mobile_can_select_all_three_without_layout_overflow',s.occupantCount===3&&await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
  await page.locator('#focus-carriers').click();
  await page.locator('#scene').screenshot({path:path.join(out,'all-carriers-mobile-scene.png')});
  await page.goto(base+'/experiments/particle-overlap-tetrahedron/');
  await page.waitForFunction(()=>globalThis.ParticleOverlapViewer?.snapshot().frameCount>2);
  check('existing_carrier_view_still_renders',await page.evaluate(()=>globalThis.ParticleOverlapViewer.snapshot().geometry.renderedCarrierBodies.length===2));
  await page.getByRole('link',{name:'Empty structured space'}).click();
  await page.waitForFunction(()=>globalThis.RealizationSpaceViewer?.snapshot().frameCount>2);
  check('current_three_axis_space_is_linked_from_existing_experiment',page.url().endsWith('/vacuum.html'));
  check('no_browser_exceptions',errors.length===0);
  await writeFile(path.join(out,'verification.json'),JSON.stringify({schema:'marici.vacuum-space-viewer.v1',status:'pass',checked_at:new Date().toISOString(),checks,source_sha256,
    route:'/experiments/particle-overlap-tetrahedron/planes.html',scope:'Forward geometric realization and typed frame continuation with alternating 2+1 C/M assignments from a single R=0 reference choice on discrete realization R. No particle operators, energy or source-selected rotation law.'},null,2)+'\n');
  console.log(JSON.stringify({status:'pass',checks:Object.keys(checks).length,route:'/experiments/particle-overlap-tetrahedron/planes.html',screenshots:out}));
} finally {await browser?.close();if(server)await new Promise(resolve=>server.close(resolve));}
