import assert from 'node:assert/strict';
import {readFile,writeFile} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import {chromium} from '@playwright/test';

const determinant=(a,b,c)=>a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]);
const root=new URL('./',import.meta.url);
const source=JSON.parse(await readFile(new URL('../../results/twelve-triangle-positive-geometry.json',root),'utf8'));
const browser=await chromium.launch({headless:true,args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
try {
  const page=await browser.newPage({viewport:{width:1440,height:1000},reducedMotion:'no-preference'});
  const errors=[],network=[];
  page.on('pageerror',e=>errors.push(e.message));
  page.on('request',request=>{if(/^https?:/.test(request.url()))network.push(request.url());});
  await page.route(/^https?:/,route=>route.abort());
  await page.goto(new URL('./index.html',root).href);
  try {
    await page.waitForFunction(()=>window.protonCarrier?.snapshot().renderCalls>0 || !document.getElementById('error').hidden,null,{timeout:10000});
  } catch(error) {
    console.error({errors,state:await page.evaluate(()=>({ready:document.readyState,three:window.THREE?.REVISION,
      api:window.protonCarrier?.snapshot(),error:document.getElementById('error')?.textContent}))});
    throw error;
  }
  assert.equal(await page.locator('#error').isVisible(),false,await page.locator('#error').textContent());
  const snapshot=()=>page.evaluate(()=>window.protonCarrier.snapshot());
  let state=await snapshot();
  assert.ok(state.phase>=0&&state.phase<1);
  assert.ok(state.guidePositions.flat().every(Number.isFinite));
  assert.equal(Object.keys(state.points).length,8);
  assert.equal(state.triangles.length,12);assert.equal(state.edges.length,18);
  const expected=new Map(source.triangles_and_transports.map(t=>[t.outer_arrow,t.triangle]));
  let volume=0;
  for(const triangle of state.triangles) {
    assert.deepEqual(triangle.vertices,expected.get(triangle.id));
    const coordinates=triangle.vertices.map(v=>state.points[v]);
    const cone=determinant(...coordinates)/6;
    assert.ok(Math.abs(cone-2/9)<1e-12);volume+=cone;
    const flat=coordinates.flat();
    for(let i=0;i<9;i++)assert.ok(Math.abs(flat[i]-triangle.renderedPositions[i])<1e-7);
  }
  assert.ok(Math.abs(volume-8/3)<1e-12);
  const adjacency=Object.fromEntries(state.triangles.map(t=>[t.id,new Set()]));
  for(const edge of state.edges) {
    assert.equal(edge.agents.length,2);assert.deepEqual(edge.arrows[0],edge.arrows[1].toReversed());
    const [a,b]=edge.agents;adjacency[a].add(b);adjacency[b].add(a);
  }
  assert.ok(Object.values(adjacency).every(neighbours=>neighbours.size===3));
  for(const vertex of Object.keys(state.points)) {
    const incident=state.triangles.filter(t=>t.vertices.includes(vertex)).map(t=>t.id);
    assert.equal(incident.length,vertex.startsWith('F_')?3:6);
    const nodes=new Set(incident);
    assert.ok(incident.every(v=>[...adjacency[v]].filter(w=>nodes.has(w)).length===2));
    const visited=new Set([incident[0]]),queue=[incident[0]];
    while(queue.length)for(const next of adjacency[queue.pop()])if(nodes.has(next)&&!visited.has(next)){visited.add(next);queue.push(next);}
    assert.equal(visited.size,incident.length);
  }
  await page.locator('#play').click();
  assert.equal((await snapshot()).playing,false);
  const stopped=(await snapshot()).phase;await page.waitForTimeout(120);
  assert.equal((await snapshot()).phase,stopped);
  await page.locator('#triangle').selectOption('AB');
  assert.equal(await page.locator('#packets').textContent(),'(F_ABC, A)\n(A, B)\n(B, F_ABC)');
  await page.locator('#triangle').selectOption('');
  const clickPoint=await page.evaluate(()=>{
    const s=window.protonCarrier.snapshot(),canvas=document.querySelector('canvas'),rect=canvas.getBoundingClientRect();
    const camera=new THREE.PerspectiveCamera(40,rect.width/rect.height,0.1,60);
    camera.position.fromArray(s.camera);camera.lookAt(0,0,0);camera.updateMatrixWorld();
    const tri=s.triangles.find(t=>t.id==='AB'),p=new THREE.Vector3();
    for(const k of tri.vertices)p.add(new THREE.Vector3(...s.points[k]));p.divideScalar(3).project(camera);
    return {x:rect.left+(p.x+1)*rect.width/2,y:rect.top+(1-p.y)*rect.height/2};
  });
  await page.mouse.click(clickPoint.x,clickPoint.y);
  assert.equal((await snapshot()).selected,'AB','Raycasting must select the visible source triangle.');
  await page.locator('#triangle').selectOption('');
  await page.screenshot({path:fileURLToPath(new URL('./preview.png',root)),fullPage:true});
  await page.locator('[data-view="both"]').click();
  state=await snapshot();assert.equal(state.surfaceVisible,true);assert.equal(state.dualVisible,true);
  await page.screenshot({path:fileURLToPath(new URL('./preview-both.png',root)),fullPage:true});
  await page.locator('[data-view="dual"]').click();
  state=await snapshot();assert.equal(state.surfaceVisible,false);assert.equal(state.dualVisible,true);
  assert.equal(state.guidesVisible,false);assert.equal(await page.locator('#label-a').textContent(),'agents');
  await page.screenshot({path:fileURLToPath(new URL('./preview-dual.png',root)),fullPage:true});
  const canvas=page.locator('canvas');const bounds=await canvas.boundingBox();
  const cameraBefore=(await snapshot()).camera;
  await page.mouse.move(bounds.x+bounds.width/2,bounds.y+bounds.height/2);
  await page.mouse.down();await page.mouse.move(bounds.x+bounds.width/2+120,bounds.y+bounds.height/2+35,{steps:10});await page.mouse.up();
  await page.waitForTimeout(300);
  assert.notDeepEqual((await snapshot()).camera,cameraBefore,'Orbit control must change the camera.');
  await page.locator('#reset').click();await page.waitForTimeout(150);
  const restored=(await snapshot()).camera;
  for(let i=0;i<3;i++)assert.ok(Math.abs(restored[i]-cameraBefore[i])<1e-9,'Reset must clear orbit inertia.');
  await page.locator('[data-view="surface"]').click();
  await page.locator('#phase-guides').uncheck();await page.waitForTimeout(40);
  assert.equal((await snapshot()).guidesVisible,false);
  await page.locator('#phase-guides').check();await page.locator('#play').click();
  await page.waitForFunction(p=>window.protonCarrier.snapshot().phase!==p,stopped);
  await page.locator('#play').click();
  await page.setViewportSize({width:390,height:844});
  await page.waitForTimeout(150);
  assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
  await page.screenshot({path:fileURLToPath(new URL('./preview-mobile.png',root)),fullPage:true});
  assert.deepEqual(network,[],'Viewer must load offline.');assert.deepEqual(errors,[]);
  const reduced=await browser.newPage({viewport:{width:900,height:700},reducedMotion:'reduce'});
  await reduced.route(/^https?:/,route=>route.abort());
  await reduced.goto(new URL('./index.html',root).href);
  await reduced.waitForFunction(()=>window.protonCarrier?.snapshot().renderCalls>0);
  assert.equal(await reduced.evaluate(()=>window.protonCarrier.snapshot().playing),false);
  await reduced.close();
  const report={passed:true,sourceGeometryMatched:true,vertices:8,edges:18,triangles:12,volume,
    dualAgents:12,dualWires:18,dualCycles:{triangular:4,hexagonal:4},
    offline:true,tests:['source triangles','opposite seam arrows','positive rendered geometry','dual incidence and cycles',
      'triangle packet inspector and raycast selection','three view modes','pause and resume','orbit and inertia-free reset','phase visibility','mobile layout','reduced motion'],
    browserErrors:errors};
  await writeFile(new URL('./verification.json',root),JSON.stringify(report,null,2)+'\n');
  console.log('PASS: offline Three.js viewer; source-matched 12-triangle geometry, 8 vertices, 18 edges, positive volume 8/3; dual 4+4 cycles; controls and mobile layout.');
} finally {await browser.close();}
