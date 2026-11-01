import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';
import { chromium } from '@playwright/test';

const url=new URL('../public/experiments/hex-edge-grid.html',import.meta.url);
const html=readFileSync(url,'utf8');
const source=readFileSync(new URL('../public/experiments/hex-edge-strands.js',import.meta.url),'utf8')+'\n'+html.slice(html.indexOf('function buildHexGrid'),html.indexOf('const svg=document'));
const {buildHexGrid:build,starAt,growSimplex,simplexEdgeRole,applyProcess1,wireLayers,wireRoles,reflectThroughPoint,cloneRotate120}=
  vm.runInNewContext(`${source}\n({buildHexGrid,starAt,growSimplex,simplexEdgeRole,applyProcess1,wireLayers,wireRoles,reflectThroughPoint,cloneRotate120})`);
const seed=()=>growSimplex(-14,-14,4,2);
function edgeId(a,b) {
  [a,b]=[a,b].sort((a,b)=>a.x-b.x||a.y-b.y);
  return `e[${a.x},${a.y}|${b.x},${b.y}]`;
}
function checkConnectedLattice(scene) {
  const adj=new Map([...scene.vertices.keys()].map(id=>[id,[]]));
  for(const v of scene.vertices.values()) assert.equal(starAt(v.x,v.y).id,v.id);
  for(const edge of scene.edges.values()) {
    const a=scene.vertices.get(edge.a),b=scene.vertices.get(edge.b);
    assert.equal(edgeId(a,b),edge.id);
    assert.ok(starAt(a.x,a.y).neighbors.some(v=>v.id===b.id));
    adj.get(a.id).push(b.id);adj.get(b.id).push(a.id);
  }
  assert.ok([...adj.values()].every(neighbors=>neighbors.length<=3));
  const visited=new Set(),stack=[scene.vertices.keys().next().value];
  while(stack.length) {const id=stack.pop();if(visited.has(id)) continue;visited.add(id);stack.push(...adj.get(id));}
  assert.equal(visited.size,scene.vertices.size);
}

test('integer coordinates define three equal 120-degree arms, consistent at every grid radius',()=>{
  for(let radius=1;radius<=10;radius++) {
    const {vertices,edges,cells}=build(radius);
    assert.equal(cells.size,1+3*radius*(radius+1));
    assert.equal(vertices.size-edges.size+cells.size,1);
    for(const cell of cells.values()) assert.equal(new Set(cell.edges).size,6);
    for(const vertex of vertices.values()) {
      const star=starAt(vertex.x,vertex.y),deltas=[];
      assert.equal(new Set(star.neighbors.map(n=>n.id)).size,3);
      for(const n of star.neighbors) {
        const dx=n.x-vertex.x,dy=n.y-vertex.y;
        assert.equal(dx*dx+3*dy*dy,4);deltas.push([dx,dy]);
        assert.ok(starAt(n.x,n.y).neighbors.some(v=>v.id===vertex.id));
      }
      for(let i=0;i<3;i++) for(let j=i+1;j<3;j++)
        assert.equal(deltas[i][0]*deltas[j][0]+3*deltas[i][1]*deltas[j][1],-2);
      for(const edgeId of vertex.edges) {
        const edge=edges.get(edgeId),other=edge.a===vertex.id?edge.b:edge.a;
        assert.ok(star.neighbors.some(n=>n.id===other));
      }
    }
  }
  for(const invalid of [[0,0],[1,0],[2.5,1],[NaN,0]]) assert.throws(()=>starAt(...invalid));
  for(const id of build(2).vertices.keys()) assert.ok(build(5).vertices.has(id));
});

test('depth counts pairs of edge layers and growth respects 120-degree rotations',()=>{
  const rotate=({x,y})=>({x:(-x-3*y)/2,y:(x-y)/2}),root={x:2,y:0};
  for(let direction=0;direction<3;direction++) {
    let previous=null;
    for(let depth=1;depth<=8;depth++) {
      const growth=growSimplex(root.x,root.y,depth,direction);
      assert.equal(growth.vertices.size,(depth+1)**2);
      assert.equal(growth.edges.size,3*depth*(depth+1)/2);
      if(previous) for(const id of previous.edges.keys()) assert.ok(growth.edges.has(id));
      const r=rotate(root),tip=rotate(starAt(root.x,root.y).neighbors[direction]);
      const arm=starAt(r.x,r.y).neighbors.findIndex(v=>v.x===tip.x&&v.y===tip.y);
      const rotated=growSimplex(r.x,r.y,depth,arm);
      assert.deepEqual([...rotated.vertices.keys()].sort(),[...growth.vertices.values()].map(v=>{
        const p=rotate(v);return `v(${p.x},${p.y})`;
      }).sort());
      checkConnectedLattice(growth);previous=growth;
    }
  }
  for(const depth of [0,-1,1.5,Infinity,9]) assert.throws(()=>growSimplex(2,0,depth,0));
});

test('original palette and the first two axial reflection steps remain unchanged',()=>{
  const original=seed(),result=applyProcess1(original),white=result.whiteStep,red=result.redStep;
  assert.equal(original.vertices.size,25);assert.equal(original.edges.size,30);
  const counts={forward:0,left:0,right:0};
  for(const e of original.edges.values()) {
    const a=original.vertices.get(e.a),b=original.vertices.get(e.b);
    const role=simplexEdgeRole(a,b,original.direction);counts[role]++;
    assert.equal(simplexEdgeRole(b,a,original.direction),role);
    assert.ok(build(10).edges.has(e.id));
  }
  assert.deepEqual(counts,{forward:10,left:10,right:10});
  assert.equal(simplexEdgeRole({x:0,y:0},{x:2,y:0},{dx:1,dy:1}),'left');
  assert.equal(simplexEdgeRole({x:0,y:0},{x:-1,y:1},{dx:1,dy:1}),'right');
  for(const [scene,input,nv,ne,offset,part,seamPart,color] of [
    [white,original,50,65,-30,'reflection','seam','forward'],
    [red,white,100,135,0,'red-reflection','red-seam','left']
  ]) {
    assert.equal(scene.vertices.size,nv);assert.equal(scene.edges.size,ne);assert.equal(scene.axisOffset,offset);
    for(const v of scene.vertices.values()) assert.equal(scene.reflect(scene.reflect(v)).id,v.id);
    const copies=[...scene.edges.values()].filter(e=>e.part===part);
    assert.equal(copies.length,input.edges.size);
    for(const e of copies) {
      const source=input.edges.get(e.sourceEdge);
      assert.equal(e.id,edgeId(scene.reflect(input.vertices.get(source.a)),scene.reflect(input.vertices.get(source.b))));
    }
    const seams=[...scene.edges.values()].filter(e=>e.part===seamPart);
    assert.equal(seams.length,5);
    for(const e of seams) {assert.equal(e.role,color);assert.equal(scene.reflect(scene.vertices.get(e.a)).id,e.b);}
    checkConnectedLattice(scene);
  }
});

test('step 3 is a grid-preserving point reflection about the terminal bond midpoint (0,-1)',()=>{
  const result=applyProcess1(seed()),scene=result.step3,input=result.redStep;
  assert.equal(scene.center.x,0);assert.equal(scene.center.y,-1);
  assert.equal(scene.axisGuide,undefined);
  assert.equal(scene.vertices.size,198);assert.equal(scene.edges.size,269);
  assert.equal(scene.origins.length,6);
  assert.ok(input.edges.has('e[-1,-1|1,-1]'));
  assert.throws(()=>reflectThroughPoint(input,{x:1,y:-1}));
  const union=new Set(input.edges.keys()),images=new Map();
  for(const v of input.vertices.values()) {
    const image=scene.reflect(v);
    assert.equal(image.x,-v.x);assert.equal(image.y,-2-v.y);
    assert.equal(scene.reflect(image).id,v.id);
    assert.ok(scene.vertices.has(image.id));assert.ok(scene.vertices.has(v.id));
  }
  assert.equal(scene.reflect(input.vertices.get('v(-14,-14)')).id,'v(14,12)');
  for(const edge of input.edges.values()) {
    const id=edgeId(scene.reflect(input.vertices.get(edge.a)),scene.reflect(input.vertices.get(edge.b)));
    union.add(id);images.set(edge.id,id);
    assert.ok(wireLayers(scene.edges.get(edge.id)).some(w=>w.role===edge.role&&w.part===edge.part));
    assert.equal(edge.wires,undefined); // No mutation of step 2.
  }
  let copies=0;
  for(const edge of scene.edges.values()) for(const wire of wireLayers(edge)) if(wire.part==='step3-reflection') {
    copies++;assert.equal(edge.id,images.get(wire.sourceEdge));
    assert.equal(wire.role,input.edges.get(wire.sourceEdge).role);
  }
  assert.equal(copies,135);assert.deepEqual([...scene.edges.keys()].sort(),[...union].sort());
  assert.ok([...scene.edges.values()].every(e=>wireRoles(e).length===1));
  assert.equal(wireLayers(scene.edges.get('e[-1,-1|1,-1]')).length,2);
  checkConnectedLattice(scene);
});

test('step 4 adds exactly one clockwise 120-degree copy, retaining wire colors and overlaps',()=>{
  const result=applyProcess1(seed()),scene=result.step4,input=result.step3;
  assert.equal(scene.rotationCenter.x,0);assert.equal(scene.rotationCenter.y,0);
  assert.equal(scene.vertices.size,280);assert.equal(scene.edges.size,386);
  assert.equal([...scene.edges.values()].filter(e=>wireRoles(e).length===2).length,152);
  assert.throws(()=>cloneRotate120(input,{x:0,y:-1}));
  const union=new Set(input.edges.keys());
  for(const v of input.vertices.values()) {
    const image=scene.rotate(v);
    assert.ok(scene.vertices.has(v.id));assert.ok(scene.vertices.has(image.id));
    assert.equal(image.x*image.x+3*image.y*image.y,v.x*v.x+3*v.y*v.y);
    assert.equal(v.x*image.x+3*v.y*image.y,-(v.x*v.x+3*v.y*v.y)/2);
    assert.equal(scene.rotate(scene.rotate(image)).id,v.id);
  }
  assert.equal(scene.rotate(input.vertices.get('v(-14,-14)')).id,'v(28,0)');
  for(const edge of input.edges.values())
    union.add(edgeId(scene.rotate(input.vertices.get(edge.a)),scene.rotate(input.vertices.get(edge.b))));
  assert.deepEqual([...scene.edges.keys()].sort(),[...union].sort());
  let copies=0;
  for(const edge of scene.edges.values()) for(const wire of wireLayers(edge)) {
    if(wire.part==='step4-rotation') {
      copies++;
      const source=input.edges.get(wire.sourceEdge);
      assert.ok(wireRoles(source).includes(wire.role));
      assert.equal(edge.id,edgeId(scene.rotate(input.vertices.get(source.a)),scene.rotate(input.vertices.get(source.b))));
    }
    assert.notEqual(wire.part,'step4-seam');
  }
  assert.equal(copies,270);
  assert.equal([...input.edges.values()].reduce((n,e)=>n+wireLayers(e).length,0),270);
  for(const edge of input.edges.values()) for(const wire of wireLayers(edge))
    assert.ok(wireLayers(scene.edges.get(edge.id)).some(w=>w.role===wire.role&&w.part===wire.part));
  assert.equal([...scene.edges.values()].reduce((n,e)=>n+wireRoles(e).length,0),538);
  checkConnectedLattice(scene);
});

test('steps 5–7 clone each entire preceding stage with the same centers and retain every wire',()=>{
  const result=applyProcess1(seed());
  const cases=[
    [result.step4,result.step5,'step5-reflection','reflect',314,439,1080],
    [result.step5,result.step6,'step6-rotation','rotate',350,491,2160],
    [result.step6,result,'step7-reflection','reflect',386,543,4320]
  ];
  for(const [input,scene,part,operation,vertices,edges,wires] of cases) {
    const transform=scene[operation];
    assert.equal(scene.vertices.size,vertices);assert.equal(scene.edges.size,edges);
    const center=operation==='reflect'?scene.center:scene.rotationCenter;
    assert.equal(center.x,0);assert.equal(center.y,operation==='reflect'?-1:0);
    const union=new Set(input.edges.keys());
    for(const e of input.edges.values()) union.add(edgeId(transform(input.vertices.get(e.a)),transform(input.vertices.get(e.b))));
    assert.deepEqual([...scene.edges.keys()].sort(),[...union].sort());
    let copies=0;
    for(const edge of scene.edges.values()) for(const wire of wireLayers(edge)) if(wire.part===part) {
      copies++;
      const source=input.edges.get(wire.sourceEdge);
      assert.ok(wireRoles(source).includes(wire.role));
      assert.equal(edge.id,edgeId(transform(input.vertices.get(source.a)),transform(input.vertices.get(source.b))));
    }
    const inputCount=[...input.edges.values()].reduce((n,e)=>n+wireLayers(e).length,0);
    assert.equal(copies,inputCount);
    assert.equal([...scene.edges.values()].reduce((n,e)=>n+wireLayers(e).length,0),wires);
    assert.equal(wires,2*inputCount);
    for(const edge of input.edges.values()) for(const wire of wireLayers(edge))
      assert.ok(wireLayers(scene.edges.get(edge.id)).some(w=>w.role===wire.role&&w.part===wire.part&&w.sourceEdge===wire.sourceEdge));
    checkConnectedLattice(scene);
  }
  assert.equal([...result.edges.values()].filter(e=>wireRoles(e).length===3).length,137);
});

test('only axial reflections have line guides; point reflection and rotation have center markers',()=>{
  const result=applyProcess1(seed());
  for(const [step,part] of [[result.whiteStep,'seam'],[result.redStep,'red-seam']]) {
    const midpoints=[...step.edges.values()].filter(e=>wireLayers(e).some(w=>w.part===part))
      .filter(e=>step!==result||result.step3.edges.has(e.id)).map(e=>{
        const a=step.vertices.get(e.a),b=step.vertices.get(e.b);
        return {x:(a.x+b.x)/2,y:(a.y+b.y)/2};
      }).filter(p=>step!==result||p.x>0).sort((a,b)=>a.x-b.x||a.y-b.y);
    for(const [guide,midpoint] of [[step.axisGuide[0],midpoints[0]],[step.axisGuide[1],midpoints.at(-1)]]) {
      assert.equal(guide.x,midpoint.x);assert.equal(guide.y,midpoint.y);
      assert.equal(guide.x*step.axisDirection.dx+3*guide.y*step.axisDirection.dy,step.axisOffset);
    }
  }
  assert.equal(result.axisGuide,undefined);
  assert.equal(result.step3.axisGuide,undefined);
});

test('browser: stages, point marker, parallel wires, inspection, keyboard and mobile',async()=>{
  const browser=await chromium.launch({headless:true});
  try {
    const page=await browser.newPage({viewport:{width:1280,height:900}}),errors=[];
    page.on('pageerror',error=>errors.push(error.message));await page.goto(url.href);
    assert.equal(await page.locator('#process').inputValue(),'process1');
    assert.equal(await page.locator('#process-steps [aria-pressed="true"]').textContent(),'7');
    assert.equal(await page.locator('.simplex-edge').count(),1099);
    assert.equal(await page.locator('.simplex-vertex').count(),386);
    const tripleId=await page.locator('.simplex-edge').evaluateAll(nodes=>{
      const counts=new Map();for(const n of nodes) counts.set(n.dataset.edge,(counts.get(n.dataset.edge)||0)+1);
      return [...counts].find(([,count])=>count===3)[0];
    });
    const triple=page.locator(`.simplex-edge[data-edge="${tripleId}"]`);
    assert.equal(await triple.count(),3);
    assert.equal(new Set(await triple.evaluateAll(nodes=>nodes.map(n=>n.getAttribute('d')))).size,3);
    assert.deepEqual(await triple.evaluateAll(nodes=>nodes.map(n=>n.dataset.role)),['forward','left','right']);
    await page.locator('#process-steps button[data-stage="4"]').click();
    assert.equal(await page.locator('.simplex-edge').count(),538);
    assert.equal(await page.locator('.simplex-vertex').count(),280);
    assert.equal(await page.locator('.simplex-edge[data-overlap="true"]').count(),304);
    const id=await page.locator('.simplex-edge[data-overlap="true"]').first().getAttribute('data-edge');
    const pair=page.locator(`.simplex-edge[data-edge="${id}"]`);
    assert.equal(await pair.count(),2);
    assert.notEqual(await pair.nth(0).getAttribute('d'),await pair.nth(1).getAttribute('d'));
    assert.notEqual(await pair.nth(0).getAttribute('data-role'),await pair.nth(1).getAttribute('data-role'));
    assert.deepEqual(await page.locator('#process-steps li span').allTextContents(),[
      'Reflect crossing white','Reflect crossing red','Point reflection about (0, −1)','Clone, rotate 120° clockwise',
      'Point reflection about (0, −1)','Clone, rotate 120° clockwise','Point reflection about (0, −1)']);
    assert.equal(await page.locator('.reflection-guide').count(),2);
    assert.equal(await page.locator('.reflection-guide[data-step="3"]').count(),0);
    const center=page.locator('#point-reflection-center');
    assert.equal(await center.getAttribute('cx'),'0');
    assert.ok(Math.abs(Number(await center.getAttribute('cy'))+18*Math.sqrt(3))<0.001);
    for(const [step,color] of [[1,'rgb(255, 255, 255)'],[2,'rgb(255, 69, 69)']]) {
      const guide=page.locator(`.reflection-guide[data-step="${step}"]`);
      assert.equal(await guide.evaluate(el=>getComputedStyle(el).stroke),color);
      assert.equal(await guide.getAttribute('stroke-dasharray'),'8 6');
    }
    assert.equal(await page.locator('.reflection-guide[data-step="4"]').count(),0);
    const rotation=page.locator('#rotation-center');
    assert.equal(await rotation.getAttribute('cx'),'0');assert.equal(await rotation.getAttribute('cy'),'0');
    assert.equal(await page.locator('#grow-simplex,#growth-depth,#growth-direction,#clear-growth').count(),0);
    await page.locator('#process').selectOption('original');
    assert.equal(await center.count(),0);assert.equal(await page.locator('.reflection-guide').count(),0);
    assert.equal(await page.locator('.simplex-edge').count(),30);
    const dot=page.locator('.hit[data-id="v(2,0)"]');await dot.hover();
    assert.equal(await page.locator('#vertex-id').textContent(),'(2, 0)');
    assert.equal(await page.locator('.edge.active').count(),3);
    assert.equal(await page.locator('#neighbors button').count(),3);
    await dot.click();await page.mouse.move(5,5);
    assert.equal(await page.locator('.edge.active').count(),3);
    const next=await page.locator('#neighbors button').first().textContent();
    await page.locator('#neighbors button').first().click();
    assert.equal(await page.locator('#vertex-id').textContent(),next);
    await page.keyboard.press('Escape');assert.equal(await page.locator('.edge.active').count(),0);
    await dot.focus();await page.keyboard.press('Enter');
    assert.match(await page.locator('#status').textContent(),/Pinned/);
    await page.locator('#radius').fill('2');
    assert.equal(await page.locator('#vertex-id').textContent(),'(2, 0)');
    await page.locator('#clear').click();
    const boundary=[...build(2).vertices.values()].find(v=>v.edges.length===2);
    await page.locator(`.hit[data-id="${boundary.id}"]`).hover();
    assert.equal(await page.locator('.edge.active').count(),3);
    assert.equal(await page.locator('#neighbors button:disabled').count(),1);
    await page.mouse.move(5,5);assert.equal(await page.locator('.edge.active').count(),0);
    await page.setViewportSize({width:390,height:844});await dot.click();
    assert.match(await page.locator('#status').textContent(),/Pinned/);
    assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),true);
    await page.locator('#process').selectOption('process1');
    const counts={1:[50,65,1,0],2:[100,135,2,0],3:[198,269,2,0],4:[280,538,2,304],
      5:[314,632,2,386],6:[350,995,2,895],7:[386,1099,2,975]};
    for(const stage of [1,2,3,4,5,6,7,2,5,1,6,7]) {
      await page.locator(`#process-steps button[data-stage="${stage}"]`).click();
      const [vertices,strokes,guides,overlapStrokes]=counts[stage];
      assert.equal(await page.locator('.simplex-vertex').count(),vertices);
      assert.equal(await page.locator('.simplex-edge').count(),strokes);
      assert.equal(await page.locator('.reflection-guide').count(),guides);
      assert.equal(await center.count(),stage>=3?1:0);
      assert.equal(await rotation.count(),stage>=4?1:0);
      assert.equal(await page.locator('#process-steps [aria-pressed="true"]').textContent(),String(stage));
      assert.match(await page.locator('#process-description').textContent(),new RegExp(`Stage ${stage} of 7`));
      assert.equal(await page.locator('.simplex-edge[data-overlap="true"]').count(),overlapStrokes);
      assert.equal(await page.evaluate(()=>{
        const ids=[...document.querySelectorAll('[id]')].map(el=>el.id);
        return new Set(ids).size===ids.length;
      }),true);
    }
    await page.locator('#process-steps button[data-stage="3"]').focus();await page.keyboard.press('Enter');
    assert.equal(await page.locator('.simplex-edge').count(),269);
    await page.locator('#radius').fill('1');assert.equal(await page.locator('.simplex-edge').count(),269);
    await page.locator('#process').selectOption('original');
    assert.equal(await page.locator('#process-steps').isVisible(),false);
    await page.locator('#process').selectOption('process1');
    assert.equal(await page.locator('#process-steps [aria-pressed="true"]').textContent(),'3');
    assert.equal(await center.count(),1);assert.deepEqual(errors,[]);
  } finally {await browser.close();}
});
