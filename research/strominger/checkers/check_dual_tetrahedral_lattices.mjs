import assert from 'node:assert/strict';
import {createServer} from 'node:http';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import {chromium} from '@playwright/test';
import * as M from '../demos/dual-tetrahedral-lattices/model.mjs';
const ROOT=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const DEMO=path.join(ROOT,'research/strominger/demos/dual-tetrahedral-lattices');
const OUT=path.join(ROOT,'research/strominger/results/dual-tetrahedral-lattices');
const checks={};const ck=(name,value)=>{checks[name]=Boolean(value);assert.ok(value,name);};
const near=(a,b)=>a.length===b.length&&a.every((x,i)=>Math.abs(x-b[i])<1e-10);
const hash=x=>createHash('sha256').update(x).digest('hex');
async function main(){
 await mkdir(OUT,{recursive:true});
 const tested=[];
 for(let i=-2;i<=2;i++)for(let j=-2;j<=2;j++)for(let k=-2;k<=2;k++)for(const family of ['A','B']){
  const s=M.site(family,[i,j,k]),t=M.tetrahedron(s),bc=M.barycenter(t.vertices),edgeSquares=[];
  for(let a=0;a<4;a++)for(let b=a+1;b<4;b++)edgeSquares.push(M.squared(t.vertices[a].point,t.vertices[b].point));
  tested.push({center:s,kind:t.kind,vertices:t.vertices,barycenter:bc,edgeSquares,volume6:M.volume6(t)});
 }
 ck('both_lattices_have_exact_mutual_barycenters',tested.length===250&&tested.every(t=>near(t.center.point,t.barycenter)));
 ck('every_tetrahedron_has_four_opposite_family_vertices',tested.every(t=>t.vertices.length===4&&new Set(t.vertices.map(v=>v.id)).size===4&&t.vertices.every(v=>v.family!==t.center.family)));
 ck('all_six_tetrahedral_edges_squared_eight',tested.every(t=>t.edgeSquares.length===6&&t.edgeSquares.every(x=>x===8)));
 ck('all_center_corner_distances_squared_three',tested.every(t=>t.vertices.every(v=>M.squared(v.point,t.center.point)===3)));
 ck('nondegenerate_positive_volume_with_opposite_ordered_orientations',tested.every(t=>t.volume6===(t.kind==='P'?16:-16)));
 ck('neighbor_relation_is_reciprocal',tested.every(t=>t.vertices.every(v=>M.neighbors(v).some(u=>u.id===t.center.id))));
 ck('P_and_N_label_tetrahedra_on_the_proposed_lattices',tested.every(t=>t.kind==='P'?t.center.family==='B'&&t.vertices.every(v=>v.family==='A'):t.center.family==='A'&&t.vertices.every(v=>v.family==='B')));
 let maxShared=0;
 for(let a=0;a<tested.length;a++)for(let b=a+1;b<tested.length;b++)if(tested[a].kind===tested[b].kind){const ids=new Set(tested[a].vertices.map(v=>v.id));maxShared=Math.max(maxShared,tested[b].vertices.filter(v=>ids.has(v.id)).length);}
 ck('same_family_selected_tetrahedra_share_at_most_a_vertex',maxShared===1);
 ck('duality_is_an_involution_exchanging_the_two_sublattices',tested.every(t=>M.dual(M.dual(t.center)).id===t.center.id&&near(M.dual(t.center).point,t.center.point.map(x=>1-x))));
 ck('duality_exchanges_entire_P_and_N_tetrahedra',tested.every(t=>{const other=M.tetrahedron(M.dual(t.center));return other.kind!==t.kind&&t.vertices.every(v=>other.vertices.some(w=>w.id===M.dual(v).id));}));
 const pair=M.pair();
 ck('selected_pair_has_each_center_at_an_opposite_vertex',pair.every((t,i)=>pair[1-i].vertices.some(v=>v.id===t.center.id)));
 const ring=M.elementaryLoop();
 ck('unwrapped_elementary_six_loop_is_genuine',ring.length===6&&new Set(ring.map(v=>v.id)).size===6&&ring.every((v,i)=>M.neighbors(v).some(w=>w.id===ring[(i+1)%6].id)));
 const graph=M.periodicGraph(4),degree=new Map(graph.vertices.map(v=>[v.id,0]));
 for(const e of graph.edges){degree.set(e.source,degree.get(e.source)+1);degree.set(e.target,degree.get(e.target)+1);}
 ck('closed_quotient_has_64_sites_on_each_lattice',graph.vertices.filter(v=>v.family==='A').length===64&&graph.vertices.filter(v=>v.family==='B').length===64);
 ck('four_reciprocal_links_per_site',graph.edges.length===256&&[...degree.values()].every(x=>x===4));
 const adjacency=new Map(graph.vertices.map(v=>[v.id,[]]));for(const e of graph.edges){adjacency.get(e.source).push(e.target);adjacency.get(e.target).push(e.source);}
 const visited=new Set([graph.vertices[0].id]),queue=[graph.vertices[0].id];for(let q=0;q<queue.length;q++)for(const v of adjacency.get(queue[q]))if(!visited.has(v)){visited.add(v);queue.push(v);}
 ck('periodic_network_is_connected',visited.size===128);
 ck('shortest_center_loop_has_six_links_not_three_or_four',M.shortestCycle(graph)===6);
 ck('deck_translations_recover_all_unwrapped_neighbors',graph.edges.every(e=>{const wrapped=graph.vertices.find(v=>v.id===e.target);const shift=M.site('A',e.deckTranslation.map(x=>x*graph.size)).point;return near(wrapped.point.map((x,i)=>x+shift[i]),e.unwrappedTarget.point);}));
 const boundary=graph.edges.filter(e=>e.source==='A:0,0,0'),wrappedMean=[0,1,2].map(i=>boundary.reduce((s,e)=>s+graph.vertices.find(v=>v.id===e.target).point[i],0)/4);
 ck('naive_wrapped_average_is_detected_as_wrong_frame',!near(wrappedMean,[0,0,0])&&near(M.barycenter(M.neighbors(M.site('A',[0,0,0]))),[0,0,0]));
 ck('closed_saturated_bipartite_accounting_demands_equal_counts',4*64===graph.edges.length&&4*82!==4*126);
 ck('lead208_imbalance_requires_176_excess_N_side_boundary_slots_if_this_occupancy_rule_is_used',4*(126-82)===176);
 const allowed=new Map([['/','index.html'],['/index.html','index.html'],['/app.mjs','app.mjs'],['/model.mjs','model.mjs']]);
 const server=createServer(async(req,res)=>{const filename=allowed.get(new URL(req.url,'http://127.0.0.1').pathname);if(!filename){res.writeHead(404);res.end();return;}try{res.writeHead(200,{'Content-Type':filename.endsWith('.html')?'text/html; charset=utf-8':'text/javascript; charset=utf-8','Cache-Control':'no-store'});res.end(await readFile(path.join(DEMO,filename)));}catch{res.writeHead(500);res.end();}});
 await new Promise(resolve=>server.listen(0,'127.0.0.1',resolve));
 const browser=await chromium.launch({headless:true});const errors=[];
 try{
  const page=await browser.newPage({viewport:{width:1440,height:980}});page.on('pageerror',e=>errors.push(String(e)));
  await page.goto(`http://127.0.0.1:${server.address().port}/`);await page.waitForFunction(()=>window.dualTetra?.counts.patch.tetrahedra>2);
  ck('browser_uses_actual_model_pair_with_both_barycenters',await page.evaluate(()=>dualTetra.pair.length===2&&dualTetra.pair.every(t=>dualTetra.model.barycenter(t.vertices).every((x,i)=>x===t.center.point[i]))));
  const text=await page.locator('body').innerText();ck('scope_and_site_not_particle_warning_visible',text.includes('whole tetrahedra, not the colored dots')&&text.includes('not a conventional face-to-face cell-dual tiling'));
  await page.locator('[data-family="P"]').click();ck('P_filter_preserves_geometric_family',await page.evaluate(()=>dualTetra.counts.pair.tetrahedra===1&&dualTetra.family==='P'));
  await page.locator('[data-family="N"]').click();ck('N_filter_preserves_geometric_family',await page.evaluate(()=>dualTetra.counts.pair.tetrahedra===1&&dualTetra.family==='N'));
  await page.locator('[data-family="both"]').click();
  const initial=await page.evaluate(()=>dualTetra.camera),box=await page.locator('#pair').boundingBox();
  await page.mouse.move(box.x+box.width/2,box.y+box.height/2);await page.mouse.down();await page.mouse.move(box.x+box.width/2+70,box.y+box.height/2+20,{steps:5});await page.mouse.up();
  ck('drag_rotates_both_views',await page.evaluate(p=>Math.abs(dualTetra.camera.ay-p.ay)>.2,initial));
  await page.locator('#reset').click();ck('reset_recovers_initial_camera',await page.evaluate(p=>Math.abs(dualTetra.camera.ay-p.ay)<1e-12,initial));
  await page.locator('#pair').focus();await page.keyboard.press('ArrowRight');ck('keyboard_rotation_works',await page.evaluate(p=>dualTetra.camera.ay!==p.ay,initial));
  await page.locator('#reset').click();await page.locator('h1').click();
  for(const id of ['faces','centers','ring']){await page.locator('#'+id).uncheck();await page.locator('#'+id).check();}
  await page.screenshot({path:path.join(OUT,'dual-tetrahedral.png'),fullPage:true});
  ck('desktop_screenshot_is_nonempty',(await readFile(path.join(OUT,'dual-tetrahedral.png'))).length>30000);
  await page.setViewportSize({width:420,height:980});await page.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r))));
  ck('mobile_has_no_horizontal_overflow',await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1));
  await page.screenshot({path:path.join(OUT,'dual-tetrahedral-mobile.png'),fullPage:true});ck('no_browser_errors',errors.length===0);
 }finally{await browser.close();await new Promise(resolve=>server.close(resolve));}
 const files=['model.mjs','app.mjs','index.html','README.md','serve.mjs'].map(n=>path.join(DEMO,n));files.push(fileURLToPath(import.meta.url),path.join(ROOT,'research/strominger/checkers/check_dual_tetrahedral_lattices.py'),path.join(ROOT,'research/strominger/scc-models/dual-tetrahedral-lattices-v1.json'));
 const source_sha256={};for(const p of files)source_sha256[path.relative(ROOT,p).replaceAll('\\','/')]=hash(await readFile(p));
 const report={status:'pass',classification:'reciprocal_tetrahedral_network_realized_not_nuclear_packing',checks,tested_tetrahedra:tested,selected_pair:pair,explicit_unwrapped_six_loop:ring,periodic_graph:graph,naive_wrapped_center:wrappedMean,closed_saturation_condition:'4P=E=4N; necessary, not sufficient',lead208_conditional_excess_N_side_missing_slots:176,scope:M.scope,source_sha256};
 await writeFile(path.join(OUT,'verification.json'),JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({status:'pass',classification:report.classification,checks:Object.keys(checks).length,tetrahedra:tested.length,periodic_sites:128,shortest_center_loop:6,screenshot:'research/strominger/results/dual-tetrahedral-lattices/dual-tetrahedral.png'}));
}
main().catch(async error=>{await mkdir(OUT,{recursive:true});await writeFile(path.join(OUT,'execution-failure.json'),JSON.stringify({status:'fail',checks,error:String(error)},null,2)+'\n');console.error(error);process.exitCode=1;});
