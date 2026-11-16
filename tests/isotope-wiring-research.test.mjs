import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import vm from 'node:vm';
import { inspectDefinition, compareDefinitions, trialPairPlacement, trialWitnessPlacement, surveyPlacements } from '../examples/isotope-wiring/core/editor-research.mjs';
import { importLegacyAbsolute } from '../examples/isotope-wiring/core/legacy-adapter.mjs';
import { verifyModel } from '../examples/isotope-wiring/core/model-predicates.mjs';
const html = readFileSync(new URL('../examples/isotope-wiring/index.html', import.meta.url), 'utf8');
const context = vm.createContext({});
vm.runInContext(html.match(/<script>([\s\S]*?)<\/script>/)[1], context);
const fixtures = JSON.parse(JSON.stringify(context.IsotopeWiring.fixtures()));
const clone = value => JSON.parse(JSON.stringify(value));
const withoutCells = report => report.checks.map(check => ({ ...check, issues: check.issues.map(({ cells, ...issue }) => issue) }));

test('all 13 stable pre-oxygen nuclides have exact inventories and explicitly unestablished placements', () => {
  const expected={H1:[1,0],H2:[1,1],He3:[2,1],He4:[2,2],Li6:[3,3],Li7:[3,4],Be9:[4,5],B10:[5,5],B11:[5,6],C12:[6,6],C13:[6,7],N14:[7,7],N15:[7,8]};
  assert.deepEqual(Object.keys(fixtures).filter(id=>fixtures[id].Z<8).sort(),Object.keys(expected).sort());
  for(const [id,[Z,N]] of Object.entries(expected)){
    const d=fixtures[id];assert.equal(d.Z,Z);assert.equal(d.N,N);
    assert.equal(d.graph.pairs.length,Z);assert.equal(d.graph.witnesses.length,N);
    assert.deepEqual(d.expectedByShell,Z<=2?[Z]:[2,Z-2]);
    assert.equal(d.status,'unresolved');assert.match(d.notes,/illustrative/);
    assert.equal(context.IsotopeWiring.validate(d).valid,true,id);
    assert.equal(inspectDefinition(d).status,'verified',id);
    assert.deepEqual(d.placementQuestions[0].cellIds,d.graph.cells.map(c=>c.id));
    assert.doesNotMatch(context.IsotopeWiring.renderSVG(d),/data-question-cell=|class="question-badge"/);
  }
});

test('hydrogen sketches are open/closed triangles and He4 is a square with both diagonals', () => {
  const render=context.IsotopeWiring.renderSVG;
  for(const id of ['H1','H2','He4']){
    const before=JSON.stringify(fixtures[id]),svg=render(fixtures[id],{neutronVs:true,standalone:true});
    assert.doesNotMatch(svg,/<path class="(?:ep |question-shape)/);
    if(id==='He4'){
      assert.equal([...svg.matchAll(/class="neutron neutron-v"/g)].length,2);
      assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,2);
    }else{
      const d=svg.match(/class="neutron hydrogen-sketch"[^>]* d="([^"]+)"/)[1];
      assert.equal([...d.matchAll(/L/g)].length,2);assert.equal(d.endsWith(' Z'),id==='H2');
      assert.doesNotMatch(svg,/class="neutron sketch-cross"/);
    }
    assert.equal(JSON.stringify(fixtures[id]),before);
    assert.match(render(fixtures[id]),/<path class="ep /);
  }
});

test('He3 closes the outer Vs vertically without changing its square or inventory', () => {
  const before=JSON.stringify(fixtures.He3),svg=context.IsotopeWiring.renderSVG(fixtures.He3,{neutronVs:true,standalone:true});
  assert.doesNotMatch(svg,/helium3-frame|sketch-cross/);
  assert.equal([...svg.matchAll(/class="neutron helium3-square"/g)].length,1);
  assert.equal([...svg.matchAll(/class="neutron helium3-v"/g)].length,2);
  assert.match(svg,/data-side="left" d="M-100 34 L-50 84 L-100 134 Z"/);
  assert.match(svg,/data-side="right" d="M100 34 L50 84 L100 134 Z"/);
  assert.match(svg,/class="neutron helium3-square" d="M0,34 L50,84 L0,134 L-50,84 Z"/);
  assert.match(svg,/viewBox="-120 0 240 164"/);
  assert.doesNotMatch(svg,/<path class="ep /);
  assert.doesNotMatch(svg,/class="placement-question"|Placement unresolved|visual prototype|legacy checks only/);
  assert.equal(JSON.stringify(fixtures.He3),before);assert.equal(fixtures.He3.N,1);
});

test('Li6 green sketch directly attaches a closed triangle without a sector frame', () => {
  const before=JSON.stringify(fixtures.Li6),svg=context.IsotopeWiring.renderSVG(fixtures.Li6,{neutronVs:true,standalone:true});
  assert.equal([...svg.matchAll(/class="neutron neutron-v"/g)].length,2);
  assert.equal([...svg.matchAll(/class="neutron lithium-triangle"/g)].length,1);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,2);
  assert.equal([...svg.matchAll(/class="space-frame"/g)].length,0);
  const anchor=context.IsotopeWiring.geometry(fixtures.Li6).point('s1-00','B');
  assert(svg.includes(`data-cell="s2-01" d="M${anchor.join(' ')} L-50 ${anchor[1]+50} L50 ${anchor[1]+50} Z"`),'Closed triangle shares its apex exactly with the first-shell bottom vertex');
  assert.doesNotMatch(svg,/<path class="ep /);
  assert.equal(JSON.stringify(fixtures.Li6),before);
});

test('Li7 encloses a single second-shell triangle in a square', () => {
  const before=JSON.stringify(fixtures.Li7),svg=context.IsotopeWiring.renderSVG(fixtures.Li7,{neutronVs:true,standalone:true});
  assert.equal([...svg.matchAll(/class="neutron lithium-triangle"/g)].length,1);
  assert.match(svg,/d="M0 144 L-50 194 L50 194 Z"/);
  assert.match(svg,/class="space-frame lithium-sector" d="M0 134 L60 194 L0 254 L-60 194 Z"/);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,2,'Only shell 1 has crossing diagonals');
  assert.equal([...svg.matchAll(/class="space-frame lithium-sector"/g)].length,1);assert.match(svg,/viewBox="-86 14 172 250"/);
  assert.equal(JSON.stringify(fixtures.Li7),before);
});

test('Be9 replaces the Li7 inner triangle with a fully crossed square', () => {
  const before=JSON.stringify(fixtures.Be9),svg=context.IsotopeWiring.renderSVG(fixtures.Be9,{neutronVs:true,standalone:true});
  assert.equal([...svg.matchAll(/class="space-frame lithium-sector"/g)].length,1);
  assert.equal([...svg.matchAll(/class="neutron beryllium-square"/g)].length,1);
  assert.match(svg,/class="neutron beryllium-square" data-cell="s2-01" d="M0,144 L50,194 L0,244 L-50,194 Z"/);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,4);
  assert.doesNotMatch(svg,/lithium-triangle|data-witness="s2-/);
  assert.equal(JSON.stringify(fixtures.Be9),before);assert.equal(fixtures.Be9.N,5);
});

test('B10 retains its crossed square and bottom triangle without a shell-2 wrapper', () => {
  const before=JSON.stringify(fixtures.B10),svg=context.IsotopeWiring.renderSVG(fixtures.B10,{neutronVs:true,standalone:true});
  assert.equal([...svg.matchAll(/class="neutron beryllium-square"/g)].length,1);
  assert.doesNotMatch(svg,/<path class="space-frame|lithium-sector/);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,4);
  assert.equal([...svg.matchAll(/class="neutron boron-triangle"/g)].length,1);
  assert.match(svg,/class="neutron boron-triangle" data-cell="s2-10" d="M0,234 L-50,284 L50,284 Z"/);
  assert.match(svg,/class="neutron beryllium-square" data-cell="s2-01" d="M0,134 L50,184 L0,234 L-50,184 Z"/);
  assert.match(svg,/data-cell="s1-00" d="M-50 84 L0 134 L50 84"/,'The first square bottom and second square top share (0,134)');
  assert.match(svg,/viewBox="-136 14 272 370"/);assert.equal(JSON.stringify(fixtures.B10),before);
});

test('B11 adds only the shell-2 wrapper to B10', () => {
  const before=JSON.stringify(fixtures.B11),svg=context.IsotopeWiring.renderSVG(fixtures.B11,{neutronVs:true,standalone:true});
  assert.doesNotMatch(svg,/boron-growth-square|boron-slot-square|data-cell="s2-00"/);
  assert.match(svg,/class="neutron boron-triangle" data-cell="s2-10" d="M0,244 L-50,294 L50,294 Z"/);
  assert.match(svg,/class="neutron beryllium-square" data-cell="s2-01" d="M0,144 L50,194 L0,244 L-50,194 Z"/);
  assert.match(svg,/class="space-frame lithium-sector" d="M0 134 L110 244 L0 354 L-110 244 Z"/);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,4,'Only the two existing squares are crossed');
  assert.match(svg,/viewBox="-136 14 272 370"/);assert.equal(JSON.stringify(fixtures.B11),before);
});

test('C12 has three joined crossed squares without a wrapper or empty square', () => {
  const before=JSON.stringify(fixtures.C12),svg=context.IsotopeWiring.renderSVG(fixtures.C12,{standalone:true});
  assert.match(svg,/class="neutron carbon-bottom-square" data-cell="s2-10" d="M0,234 L50,284 L0,334 L-50,284 Z"/);
  assert.match(svg,/class="neutron beryllium-square" data-cell="s2-01" d="M0,134 L50,184 L0,234 L-50,184 Z"/);
  assert.match(svg,/data-cell="s1-00" d="M-50 84 L0 134 L50 84"/);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,6);
  assert.match(svg,/class="neutron sketch-cross" data-cell="s2-10" d="M-50 284 L50 284"/);
  assert.match(svg,/class="neutron sketch-cross" data-cell="s2-10" d="M0 234 L0 334"/);
  assert.doesNotMatch(svg,/<path class="space-frame|boron-growth-square|boron-slot-square|boron-triangle|drawing-unavailable|data-cell="s2-00"|data-cell="s2-11"/);
  assert.match(svg,/viewBox="-136 14 272 370"/);assert.equal(JSON.stringify(fixtures.C12),before);
});

test('C13 adds a shell-2 wrapper around two crossed squares without an empty square', () => {
  const before=JSON.stringify(fixtures.C13),svg=context.IsotopeWiring.renderSVG(fixtures.C13,{standalone:true});
  assert.match(svg,/class="neutron beryllium-square" data-cell="s2-01" d="M0,144 L50,194 L0,244 L-50,194 Z"/);
  assert.match(svg,/class="neutron carbon-bottom-square" data-cell="s2-10" d="M0,244 L50,294 L0,344 L-50,294 Z"/);
  assert.match(svg,/class="space-frame lithium-sector" d="M0 134 L110 244 L0 354 L-110 244 Z"/);
  assert.equal([...svg.matchAll(/class="space-frame lithium-sector"/g)].length,1);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,6);
  assert.match(svg,/data-cell="s2-10" d="M-50 294 L50 294"/);
  assert.match(svg,/data-cell="s2-10" d="M0 244 L0 344"/);
  assert.doesNotMatch(svg,/boron-growth-square|boron-triangle|drawing-unavailable|data-cell="s2-00"|data-cell="s2-11"/);
  assert.match(svg,/viewBox="-136 14 272 370"/);assert.equal(JSON.stringify(fixtures.C13),before);
});

test('N14 keeps C12 squares fixed and rotates the added triangle 90 degrees counterclockwise', () => {
  const before=JSON.stringify(fixtures.N14),svg=context.IsotopeWiring.renderSVG(fixtures.N14,{standalone:true});
  assert.match(svg,/class="neutron beryllium-square" data-cell="s2-01" d="M0,134 L50,184 L0,234 L-50,184 Z"/);
  assert.match(svg,/class="neutron carbon-bottom-square" data-cell="s2-10" d="M0,234 L50,284 L0,334 L-50,284 Z"/);
  assert.match(svg,/class="neutron nitrogen-middle-triangle" data-cell="s2-00" d="M0,234 L50,284 L50,184 Z"/);
  assert.match(svg,/data-cell="s2-10" d="M-50 284 L50 284"/);
  assert.match(svg,/data-cell="s2-10" d="M0 234 L0 334"/);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,6);
  assert.doesNotMatch(svg,/<path class="space-frame|boron-growth-square|drawing-unavailable|data-cell="s2-11"/);
  assert.match(svg,/viewBox="-136 14 272 370"/);assert.equal(JSON.stringify(fixtures.N14),before);
});

test('N15 adds a shell-2 wrapper to the N14 squares and rotated triangle', () => {
  const before=JSON.stringify(fixtures.N15),svg=context.IsotopeWiring.renderSVG(fixtures.N15,{standalone:true});
  assert.match(svg,/class="neutron beryllium-square" data-cell="s2-01" d="M0,144 L50,194 L0,244 L-50,194 Z"/);
  assert.match(svg,/class="neutron carbon-bottom-square" data-cell="s2-10" d="M0,244 L50,294 L0,344 L-50,294 Z"/);
  assert.match(svg,/class="neutron nitrogen-middle-triangle" data-cell="s2-00" d="M0,244 L50,294 L50,194 Z"/);
  assert.match(svg,/class="space-frame lithium-sector" d="M0 134 L110 244 L0 354 L-110 244 Z"/);
  assert.equal([...svg.matchAll(/class="space-frame lithium-sector"/g)].length,1);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,6);
  assert.doesNotMatch(svg,/boron-growth-square|drawing-unavailable|data-cell="s2-11"/);
  assert.match(svg,/viewBox="-136 14 272 370"/);assert.equal(JSON.stringify(fixtures.N15),before);
});

test('Ca42 Ca43 Ca44 Ca46 Sc45 retain their specified wrapper allocations', () => {
 for(const [id,Z,N,shells,counts,top,height,width] of [
  ['Ca42',20,22,[2,8,8,2],[1,1,0],574,690,312],['Ca43',20,23,[2,8,8,2],[1,2,0],594,710,312],
  ['Ca44',20,24,[2,8,8,2],[1,2,1],584,710,602],['Ca46',20,26,[2,8,8,2],[1,2,3],594,760,752],['Sc45',21,24,[2,8,9,2],[1,2,0],694,810,372]
 ]){
  const d=fixtures[id],before=JSON.stringify(d),svg=context.IsotopeWiring.renderSVG(d,{standalone:true});
  assert.equal(d.Z,Z,id);assert.equal(d.N,N,id);assert.deepEqual(d.expectedByShell,shells,id);assert.equal(d.graph.pairs.length,Z,id);assert.equal(d.graph.witnesses.length,N,id);
  assert.equal(context.IsotopeWiring.validate(d).valid,true,id);assert.equal(inspectDefinition(d).status,'verified',id);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,20,id);assert.equal([...svg.matchAll(/class="space-frame/g)].length,N-Z,id);
  counts.forEach((n,i)=>assert.equal([...svg.matchAll(new RegExp(`class="space-frame trial-shell${i+2}-wrapper"`,'g'))].length,n,id));
  // Ca44 starts filling shell 4 after shell 3 reaches two wrappers;
  // a partially filled outer shell need not satisfy the earlier monotonic rule.
  if(id==='Ca46'){
   assert.deepEqual(counts,[1,2,3]);
   for(const [order,span,y,r] of [[2,'s1 s2',194,170],[3,'s2 s3',364,220],[3,'s1 s2 s3',304,290],[4,'s3 s4',534,170],[4,'s2 s3 s4',424,290],[4,'s1 s2 s3 s4',364,360]])assert.ok(svg.includes(`data-shell="s${order}" data-shells="${span}" d="M0 ${y-r} L${r} ${y} L0 ${y+r} L${-r} ${y} Z"`));
   assert.match(svg,/beryllium-square" data-cell="s2-01" d="M0,154 L50,204 L0,254 L-50,204 Z"/);
   assert.match(svg,/carbon-bottom-square" data-cell="s2-10" d="M0,254 L50,304 L0,354 L-50,304 Z"/);
   assert.match(svg,/magnesium-bottom-square" data-cell="s3-00" d="M0,374 L50,424 L0,474 L-50,424 Z"/);
   assert.match(svg,/silicon-bottom-square" data-cell="s3-10" d="M0,474 L50,524 L0,574 L-50,524 Z"/);
   assert.deepEqual(d.graph.pairs,fixtures.Ca44.graph.pairs);
  }
  if(id==='Ca44'){
   for(const [order,span,y,r] of [[2,'s1 s2',189,165],[3,'s2 s3',354,220],[3,'s1 s2 s3',299,285],[4,'s3 s4',524,170]])assert.ok(svg.includes(`data-shell="s${order}" data-shells="${span}" d="M0 ${y-r} L${r} ${y} L0 ${y+r} L${-r} ${y} Z"`));
   assert.deepEqual(d.graph.pairs,fixtures.Ca43.graph.pairs);
  }
  assert.ok(counts[0]>0,'These wrapped trials start at shell 2');
  if(id==='Ca43'){assert.equal(counts[1],counts[0]+1);assert.doesNotMatch(svg,/trial-shell4-wrapper/);assert.match(svg,/data-shell="s3" d="M0 364 L110 474 L0 584 L-110 474 Z"/);assert.match(svg,/data-shell="s3" d="M0 354 L120 474 L0 594 L-120 474 Z"/);}
  if(id==='Ca42'){assert.match(svg,/data-shell="s2" d="M0 134 L110 244 L0 354 L-110 244 Z"/);assert.match(svg,/data-shell="s3" d="M0 354 L110 464 L0 574 L-110 464 Z"/);assert.doesNotMatch(svg,/trial-shell4-wrapper/);}
  assert.ok(svg.includes(`class="neutron trial-shell4-square" data-cell="s4-00" d="M0,${top} L50,${top+50} L0,${top+100} L-50,${top+50} Z"`),id);
  if(id==='Sc45'){assert.match(svg,/trial-shell3-triangle" data-cell="s3-02" d="M0,584 L-50,634 L50,634 Z"/);assert.match(svg,/data-shell="s3" d="M0 364 L110 474 L0 584 L-110 474 Z"/);assert.match(svg,/data-shell="s3" d="M0 354 L170 524 L0 694 L-170 524 Z"/);assert.doesNotMatch(svg,/trial-shell4-wrapper/);assert.deepEqual(d.graph.pairs.slice(0,-1),fixtures.Ca43.graph.pairs);assert.deepEqual(d.graph.witnesses.slice(0,-1),fixtures.Ca43.graph.witnesses);}else assert.doesNotMatch(svg,/trial-shell3-triangle/);
  assert.ok(svg.includes(`viewBox="${-width/2} ${id==='Ca46'?-6:id==='Ca44'?4:14} ${width} ${height}"`),id);assert.doesNotMatch(svg,/drawing-unavailable/);assert.equal(JSON.stringify(d),before,id);
 }
});

test('Ar38 Ar40 K39 K41 Ca40 retain declared inventories and trial shape counts', () => {
  for(const [id,Z,N,shells,wrappers,crosses,height,top] of [
    ['Ar38',18,20,[2,8,8],2,18,590],['Ar40',18,22,[2,8,8],4,18,630],
    ['K39',19,20,[2,8,8,1],1,18,620,554],['K41',19,22,[2,8,8,1],3,18,660,594],['Ca40',20,20,[2,8,8,2],0,20,650,534]
  ]){
    const d=fixtures[id],before=JSON.stringify(d),svg=context.IsotopeWiring.renderSVG(d,{standalone:true});
    assert.equal(d.Z,Z,id);assert.equal(d.N,N,id);assert.deepEqual(d.expectedByShell,shells,id);
    assert.equal(d.graph.pairs.length,Z,id);assert.equal(d.graph.witnesses.length,N,id);
    assert.equal(context.IsotopeWiring.validate(d).valid,true,id);assert.equal(inspectDefinition(d).status,'verified',id);
    assert.deepEqual(d.graph.pairs.filter(p=>p.shell!=='s4'),fixtures.Ar36.graph.pairs,id);
    assert.equal([...svg.matchAll(/class="space-frame/g)].length,wrappers,id);
    assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,crosses,id);
    const shell2=id==='Ar40'?2:['Ar38','K41'].includes(id)?1:0,shell3=wrappers-shell2;
    const wrappedShells=[shell2,shell3].filter(count=>count>0);
    assert.ok(wrappedShells.every((count,i)=>i===0||wrappedShells[i-1]<=count),'Drawing rule: wrapper counts cannot decrease among wrapped shells; unwrapped shells do not participate');
    assert.equal([...svg.matchAll(/class="space-frame trial-shell2-wrapper"/g)].length,shell2,id);
    assert.equal([...svg.matchAll(/class="space-frame trial-shell3-wrapper"/g)].length,shell3,id);
    for(let i=0;i<shell2;i++){const r=110+10*i,y=234+10*shell2;assert.ok(svg.includes(`data-shell="s2" d="M0 ${y-r} L${r} ${y} L0 ${y+r} L${-r} ${y} Z"`),id);}
    for(let i=0;i<shell3;i++){const r=110+10*i,y=434+10*shell3+20*shell2;assert.ok(svg.includes(`data-shell="s3" d="M0 ${y-r} L${r} ${y} L0 ${y+r} L${-r} ${y} Z"`),id);assert.ok(y-r>=334+20*shell2,'Wrappers must not overlap shell 2');assert.ok(r<156&&y+r<14+height,'Wrapper fits viewport');}
    if(top){const shape=id==='Ca40'?`M0,${top} L50,${top+50} L0,${top+100} L-50,${top+50} Z`:`M0,${top} L-50,${top+50} L50,${top+50} Z`;assert.ok(svg.includes(`data-cell="s4-00" d="${shape}"`),id);}
    assert.ok(svg.includes(`viewBox="-156 14 312 ${height}"`),id);assert.doesNotMatch(svg,/drawing-unavailable|lithium-sector|sulfur-left-triangle/);
    assert.equal(JSON.stringify(d),before,id);
  }
});

test('Ar36 completes nine crossed squares with no neutron wrappers', () => {
  const d=fixtures.Ar36,before=JSON.stringify(d),svg=context.IsotopeWiring.renderSVG(d,{standalone:true});
  assert.equal(d.Z,18);assert.equal(d.N,18);assert.deepEqual(d.expectedByShell,[2,8,8]);
  assert.equal(d.graph.pairs.length,18);assert.equal(d.graph.witnesses.length,18);
  assert.equal(context.IsotopeWiring.validate(d).valid,true);assert.equal(inspectDefinition(d).status,'verified');assert.deepEqual(d.graph.witnesses,fixtures.Cl35.graph.witnesses);
  assert.match(svg,/class="neutron beryllium-square" data-cell="s2-01" d="M0,134 L50,184 L0,234 L-50,184 Z"/);
  assert.match(svg,/class="neutron carbon-bottom-square" data-cell="s2-10" d="M0,234 L50,284 L0,334 L-50,284 Z"/);
  assert.match(svg,/class="neutron magnesium-bottom-square" data-cell="s3-00" d="M0,334 L50,384 L0,434 L-50,384 Z"/);
  assert.match(svg,/class="neutron silicon-bottom-square" data-cell="s3-10" d="M0,434 L50,484 L0,534 L-50,484 Z"/);
  assert.match(svg,/class="neutron chlorine-right-square" data-cell="s3-01" d="M50,384 L100,434 L50,484 L0,434 Z"/);
  assert.match(svg,/class="neutron argon-left-square" data-cell="s3-11" d="M-50,384 L0,434 L-50,484 L-100,434 Z"/);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,18);
  for(const cell of ['s1-00','s2-01','s2-10','s2-00','s2-11','s3-00','s3-10','s3-01','s3-11'])assert.equal([...svg.matchAll(new RegExp(`class="neutron sketch-cross" data-cell="${cell}"`,'g'))].length,2);
  assert.match(svg,/data-cell="s3-11" d="M-100 434 L0 434"/);assert.match(svg,/data-cell="s3-11" d="M-50 384 L-50 484"/);
  assert.doesNotMatch(svg,/class="space-frame|phosphorus-side-triangle|sulfur-left-triangle|drawing-unavailable/);
  assert.match(svg,/viewBox="-136 14 272 550"/);assert.equal(JSON.stringify(d),before);
});

test('Cl37 provisionally adds two neutron contours without changing its PE shapes', () => {
  const d=fixtures.Cl37,before=JSON.stringify(d),svg=context.IsotopeWiring.renderSVG(d,{standalone:true});
  assert.equal(d.Z,17);assert.equal(d.N,20);assert.deepEqual(d.expectedByShell,[2,8,7]);
  assert.equal(d.graph.pairs.length,17);assert.equal(d.graph.witnesses.length,20);
  assert.equal(context.IsotopeWiring.validate(d).valid,true);assert.equal(inspectDefinition(d).status,'verified');assert.deepEqual(d.graph.pairs,fixtures.Cl35.graph.pairs);
  assert.match(svg,/class="space-frame lithium-sector" d="M0 144 L110 254 L0 364 L-110 254 Z"/);
  assert.match(svg,/class="space-frame magnesium-sector" d="M0 374 L110 484 L0 594 L-110 484 Z"/);
  assert.match(svg,/class="space-frame chlorine-extra-wrapper" data-shell="s3" d="M0 364 L120 484 L0 604 L-120 484 Z"/);
  assert.doesNotMatch(svg,/chlorine-extra-wrapper" data-shell="s2"/);
  assert.match(svg,/class="neutron magnesium-bottom-square" data-cell="s3-00" d="M0,384 L50,434 L0,484 L-50,434 Z"/);
  assert.match(svg,/class="neutron silicon-bottom-square" data-cell="s3-10" d="M0,484 L50,534 L0,584 L-50,534 Z"/);
  assert.match(svg,/class="neutron chlorine-right-square" data-cell="s3-01" d="M50,434 L100,484 L50,534 L0,484 Z"/);
  assert.match(svg,/class="neutron sulfur-left-triangle" data-cell="s3-11" d="M0,484 L-50,534 L-50,434 Z"/);
  assert.equal([...svg.matchAll(/class="space-frame/g)].length,3);assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,16);
  assert.match(svg,/data-cell="s3-01" d="M0 484 L100 484"/);assert.match(svg,/data-cell="s3-01" d="M50 434 L50 534"/);
  assert.doesNotMatch(svg,/phosphorus-side-triangle|class="neutron sketch-cross" data-cell="s3-11"|drawing-unavailable/);
  assert.match(svg,/viewBox="-136 14 272 610"/);assert.equal(JSON.stringify(d),before);
});

test('Cl35 completes the right shell-3 square and removes its wrapper', () => {
  const d=fixtures.Cl35,before=JSON.stringify(d),svg=context.IsotopeWiring.renderSVG(d,{standalone:true});
  assert.equal(d.Z,17);assert.equal(d.N,18);assert.deepEqual(d.expectedByShell,[2,8,7]);
  assert.equal(d.graph.pairs.length,17);assert.equal(d.graph.witnesses.length,18);
  assert.equal(context.IsotopeWiring.validate(d).valid,true);assert.equal(inspectDefinition(d).status,'verified');assert.deepEqual(d.graph.witnesses,fixtures.S34.graph.witnesses);
  assert.match(svg,/class="space-frame lithium-sector" d="M0 134 L110 244 L0 354 L-110 244 Z"/);
  assert.match(svg,/class="neutron magnesium-bottom-square" data-cell="s3-00" d="M0,354 L50,404 L0,454 L-50,404 Z"/);
  assert.match(svg,/class="neutron silicon-bottom-square" data-cell="s3-10" d="M0,454 L50,504 L0,554 L-50,504 Z"/);
  assert.match(svg,/class="neutron chlorine-right-square" data-cell="s3-01" d="M50,404 L100,454 L50,504 L0,454 Z"/);
  assert.match(svg,/class="neutron sulfur-left-triangle" data-cell="s3-11" d="M0,454 L-50,504 L-50,404 Z"/);
  assert.equal([...svg.matchAll(/class="space-frame/g)].length,1);assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,16);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross" data-cell="s3-01"/g)].length,2);
  assert.match(svg,/data-cell="s3-01" d="M0 454 L100 454"/);assert.match(svg,/data-cell="s3-01" d="M50 404 L50 504"/);
  assert.doesNotMatch(svg,/magnesium-sector|phosphorus-side-triangle|class="neutron sketch-cross" data-cell="s3-11"|drawing-unavailable/);
  assert.match(svg,/viewBox="-136 14 272 570"/);assert.equal(JSON.stringify(d),before);
});

test('S36 consolidates its PE triangles on the right and adds a neutron-only square on the left', () => {
  const d=fixtures.S36,before=JSON.stringify(d),svg=context.IsotopeWiring.renderSVG(d,{standalone:true});
  assert.equal(d.Z,16);assert.equal(d.N,20);assert.deepEqual(d.expectedByShell,[2,8,6]);
  assert.equal(d.graph.pairs.length,16);assert.equal(d.graph.witnesses.length,20);
  assert.equal(context.IsotopeWiring.validate(d).valid,true);assert.equal(inspectDefinition(d).status,'verified');assert.equal(d.graph.pairs.filter(p=>p.cell==='s3-01').length,2);assert.equal(d.graph.pairs.filter(p=>p.cell==='s3-11').length,0);
  assert.match(svg,/class="space-frame lithium-sector" d="M0 144 L110 254 L0 364 L-110 254 Z"/);
  assert.match(svg,/class="space-frame magnesium-sector" d="M0 384 L110 494 L0 604 L-110 494 Z"/);
  assert.doesNotMatch(svg,/sulfur-extra-wrapper" data-shell="s2"/);
  assert.match(svg,/data-shell="s3" d="M0 374 L120 494 L0 614 L-120 494 Z"/);
  assert.match(svg,/class="neutron beryllium-square" data-cell="s2-01" d="M0,154 L50,204 L0,254 L-50,204 Z"/);
  assert.match(svg,/class="neutron carbon-bottom-square" data-cell="s2-10" d="M0,254 L50,304 L0,354 L-50,304 Z"/);
  assert.match(svg,/class="neutron magnesium-bottom-square" data-cell="s3-00" d="M0,394 L50,444 L0,494 L-50,444 Z"/);
  assert.match(svg,/class="neutron silicon-bottom-square" data-cell="s3-10" d="M0,494 L50,544 L0,594 L-50,544 Z"/);
  assert.match(svg,/class="neutron sulfur-right-square" data-cell="s3-01" data-source-cells="s3-11 s3-01" d="M50,444 L100,494 L50,544 L0,494 Z"/);
  assert.match(svg,/class="neutron sulfur-neutron-square" data-cell="s3-11" d="M-50,444 L0,494 L-50,544 L-100,494 Z"/);
  assert.equal([...svg.matchAll(/class="space-frame/g)].length,3);assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,16);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross" data-cell="s3-01"/g)].length,2);
  assert.doesNotMatch(svg,/phosphorus-side-triangle|sulfur-left-triangle|class="neutron sketch-cross" data-cell="s3-11"|drawing-unavailable/);
  assert.match(svg,/viewBox="-136 14 272 630"/);assert.equal(JSON.stringify(d),before);
});

test('S34 adds a shell-3 wrapper around the crossed squares and mirrored triangles', () => {
  const d=fixtures.S34,before=JSON.stringify(d),svg=context.IsotopeWiring.renderSVG(d,{standalone:true});
  assert.equal(d.Z,16);assert.equal(d.N,18);assert.deepEqual(d.expectedByShell,[2,8,6]);
  assert.equal(d.graph.pairs.length,16);assert.equal(d.graph.witnesses.length,18);
  assert.equal(context.IsotopeWiring.validate(d).valid,true);assert.equal(inspectDefinition(d).status,'verified');
  assert.deepEqual(d.graph.pairs,fixtures.S33.graph.pairs);
  assert.match(svg,/class="space-frame lithium-sector" d="M0 134 L110 244 L0 354 L-110 244 Z"/);
  assert.match(svg,/class="space-frame magnesium-sector" d="M0 354 L110 464 L0 574 L-110 464 Z"/);
  assert.match(svg,/class="neutron magnesium-bottom-square" data-cell="s3-00" d="M0,364 L50,414 L0,464 L-50,414 Z"/);
  assert.match(svg,/class="neutron silicon-bottom-square" data-cell="s3-10" d="M0,464 L50,514 L0,564 L-50,514 Z"/);
  assert.match(svg,/class="neutron phosphorus-side-triangle" data-cell="s3-01" d="M0,464 L50,514 L50,414 Z"/);
  assert.match(svg,/class="neutron sulfur-left-triangle" data-cell="s3-11" d="M0,464 L-50,514 L-50,414 Z"/);
  assert.equal([...svg.matchAll(/class="space-frame/g)].length,2);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,14);
  assert.doesNotMatch(svg,/class="neutron sketch-cross" data-cell="s3-01"|class="neutron sketch-cross" data-cell="s3-11"|drawing-unavailable/);
  assert.match(svg,/viewBox="-136 14 272 590"/);assert.equal(JSON.stringify(d),before);
});

test('S33 adds a shell-2 wrapper while retaining the mirrored shell-3 triangles', () => {
  const d=fixtures.S33,before=JSON.stringify(d),svg=context.IsotopeWiring.renderSVG(d,{standalone:true});
  assert.equal(d.Z,16);assert.equal(d.N,17);assert.deepEqual(d.expectedByShell,[2,8,6]);
  assert.equal(d.graph.pairs.length,16);assert.equal(d.graph.witnesses.length,17);
  assert.equal(context.IsotopeWiring.validate(d).valid,true);assert.equal(inspectDefinition(d).status,'verified');
  assert.deepEqual(d.graph.pairs,fixtures.S32.graph.pairs);
  assert.match(svg,/class="space-frame lithium-sector" d="M0 134 L110 244 L0 354 L-110 244 Z"/);
  assert.match(svg,/class="neutron magnesium-bottom-square" data-cell="s3-00" d="M0,354 L50,404 L0,454 L-50,404 Z"/);
  assert.match(svg,/class="neutron silicon-bottom-square" data-cell="s3-10" d="M0,454 L50,504 L0,554 L-50,504 Z"/);
  assert.match(svg,/class="neutron phosphorus-side-triangle" data-cell="s3-01" d="M0,454 L50,504 L50,404 Z"/);
  assert.match(svg,/class="neutron sulfur-left-triangle" data-cell="s3-11" d="M0,454 L-50,504 L-50,404 Z"/);
  assert.equal([...svg.matchAll(/class="space-frame/g)].length,1);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,14);
  assert.doesNotMatch(svg,/magnesium-sector|drawing-unavailable/);
  assert.match(svg,/viewBox="-136 14 272 570"/);assert.equal(JSON.stringify(d),before);
});

test('S32 adds the mirrored shell-3 triangle and removes the shell-2 wrapper', () => {
  const d=fixtures.S32,before=JSON.stringify(d),svg=context.IsotopeWiring.renderSVG(d,{standalone:true});
  assert.equal(d.Z,16);assert.equal(d.N,16);assert.deepEqual(d.expectedByShell,[2,8,6]);
  assert.equal(d.graph.pairs.length,16);assert.equal(d.graph.witnesses.length,16);
  assert.equal(context.IsotopeWiring.validate(d).valid,true);assert.equal(inspectDefinition(d).status,'verified');
  assert.deepEqual(d.graph.witnesses,fixtures.P31.graph.witnesses);
  assert.match(svg,/class="neutron beryllium-square" data-cell="s2-01" d="M0,134 L50,184 L0,234 L-50,184 Z"/);
  assert.match(svg,/class="neutron magnesium-bottom-square" data-cell="s3-00" d="M0,334 L50,384 L0,434 L-50,384 Z"/);
  assert.match(svg,/class="neutron silicon-bottom-square" data-cell="s3-10" d="M0,434 L50,484 L0,534 L-50,484 Z"/);
  assert.match(svg,/class="neutron phosphorus-side-triangle" data-cell="s3-01" d="M0,434 L50,484 L50,384 Z"/);
  assert.match(svg,/class="neutron sulfur-left-triangle" data-cell="s3-11" d="M0,434 L-50,484 L-50,384 Z"/);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,14);
  assert.doesNotMatch(svg,/<path class="space-frame|class="neutron sketch-cross" data-cell="s3-01"|class="neutron sketch-cross" data-cell="s3-11"|drawing-unavailable/);
  assert.match(svg,/viewBox="-136 14 272 550"/);assert.equal(JSON.stringify(d),before);
});

test('P31 replaces the shell-3 wrapper with a right-hand PE triangle', () => {
  const d=fixtures.P31,before=JSON.stringify(d),svg=context.IsotopeWiring.renderSVG(d,{standalone:true});
  assert.equal(d.Z,15);assert.equal(d.N,16);assert.deepEqual(d.expectedByShell,[2,8,5]);
  assert.equal(d.graph.pairs.length,15);assert.equal(d.graph.witnesses.length,16);
  assert.equal(context.IsotopeWiring.validate(d).valid,true);assert.equal(inspectDefinition(d).status,'verified');
  assert.deepEqual(d.graph.witnesses,fixtures.Si30.graph.witnesses);
  assert.match(svg,/class="space-frame lithium-sector" d="M0 134 L110 244 L0 354 L-110 244 Z"/);
  assert.match(svg,/class="neutron magnesium-bottom-square" data-cell="s3-00" d="M0,354 L50,404 L0,454 L-50,404 Z"/);
  assert.match(svg,/class="neutron silicon-bottom-square" data-cell="s3-10" d="M0,454 L50,504 L0,554 L-50,504 Z"/);
  assert.match(svg,/class="neutron phosphorus-side-triangle" data-cell="s3-01" d="M0,454 L50,504 L50,404 Z"/);
  assert.equal([...svg.matchAll(/class="space-frame/g)].length,1);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,14);
  assert.doesNotMatch(svg,/magnesium-sector|class="neutron sketch-cross" data-cell="s3-01"|drawing-unavailable/);
  assert.match(svg,/viewBox="-136 14 272 570"/);assert.equal(JSON.stringify(d),before);
});

test('Si30 adds a shell-3 wrapper enclosing its two lower crossed squares', () => {
  const d=fixtures.Si30,before=JSON.stringify(d),svg=context.IsotopeWiring.renderSVG(d,{standalone:true});
  assert.equal(d.Z,14);assert.equal(d.N,16);assert.deepEqual(d.expectedByShell,[2,8,4]);
  assert.equal(d.graph.pairs.length,14);assert.equal(d.graph.witnesses.length,16);
  assert.equal(context.IsotopeWiring.validate(d).valid,true);assert.equal(inspectDefinition(d).status,'verified');
  assert.deepEqual(d.graph.pairs,fixtures.Si29.graph.pairs);
  assert.match(svg,/class="space-frame lithium-sector" d="M0 134 L110 244 L0 354 L-110 244 Z"/);
  assert.match(svg,/class="space-frame magnesium-sector" d="M0 354 L110 464 L0 574 L-110 464 Z"/);
  assert.match(svg,/class="neutron magnesium-bottom-square" data-cell="s3-00" d="M0,364 L50,414 L0,464 L-50,414 Z"/);
  assert.match(svg,/class="neutron silicon-bottom-square" data-cell="s3-10" d="M0,464 L50,514 L0,564 L-50,514 Z"/);
  assert.equal([...svg.matchAll(/class="space-frame/g)].length,2);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,14);
  for(const cell of ['s3-00','s3-10'])assert.equal([...svg.matchAll(new RegExp('class="neutron sketch-cross" data-cell="'+cell+'"','g'))].length,2);
  assert.match(svg,/data-cell="s3-10" d="M-50 514 L50 514"/);
  assert.match(svg,/data-cell="s3-10" d="M0 464 L0 564"/);
  assert.match(svg,/viewBox="-136 14 272 590"/);assert.equal(JSON.stringify(d),before);
});

test('Si29 adds a shell-2 wrapper to seven crossed squares', () => {
  const d=fixtures.Si29,before=JSON.stringify(d),svg=context.IsotopeWiring.renderSVG(d,{standalone:true});
  assert.equal(d.Z,14);assert.equal(d.N,15);assert.deepEqual(d.expectedByShell,[2,8,4]);
  assert.equal(d.graph.pairs.length,14);assert.equal(d.graph.witnesses.length,15);
  assert.equal(context.IsotopeWiring.validate(d).valid,true);assert.equal(inspectDefinition(d).status,'verified');
  assert.deepEqual(d.graph.pairs,fixtures.Si28.graph.pairs);
  assert.match(svg,/class="space-frame lithium-sector" d="M0 134 L110 244 L0 354 L-110 244 Z"/);
  assert.match(svg,/class="neutron magnesium-bottom-square" data-cell="s3-00" d="M0,354 L50,404 L0,454 L-50,404 Z"/);
  assert.match(svg,/class="neutron silicon-bottom-square" data-cell="s3-10" d="M0,454 L50,504 L0,554 L-50,504 Z"/);
  assert.equal([...svg.matchAll(/class="space-frame/g)].length,1);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,14);
  assert.match(svg,/data-cell="s3-10" d="M-50 504 L50 504"/);
  assert.match(svg,/data-cell="s3-10" d="M0 454 L0 554"/);
  assert.doesNotMatch(svg,/magnesium-sector|aluminium-bottom-triangle|drawing-unavailable/);
  assert.match(svg,/viewBox="-136 14 272 570"/);assert.equal(JSON.stringify(d),before);
});

test('Si28 completes the bottom square and removes the remaining wrapper', () => {
  const d=fixtures.Si28,before=JSON.stringify(d),svg=context.IsotopeWiring.renderSVG(d,{standalone:true});
  assert.equal(d.Z,14);assert.equal(d.N,14);assert.deepEqual(d.expectedByShell,[2,8,4]);
  assert.equal(d.graph.pairs.length,14);assert.equal(d.graph.witnesses.length,14);
  assert.equal(context.IsotopeWiring.validate(d).valid,true);assert.equal(inspectDefinition(d).status,'verified');
  assert.deepEqual(d.graph.witnesses,fixtures.Al27.graph.witnesses);
  assert.match(svg,/class="neutron beryllium-square" data-cell="s2-01" d="M0,134 L50,184 L0,234 L-50,184 Z"/);
  assert.match(svg,/class="neutron carbon-bottom-square" data-cell="s2-10" d="M0,234 L50,284 L0,334 L-50,284 Z"/);
  assert.match(svg,/class="neutron magnesium-bottom-square" data-cell="s3-00" d="M0,334 L50,384 L0,434 L-50,384 Z"/);
  assert.match(svg,/class="neutron silicon-bottom-square" data-cell="s3-10" d="M0,434 L50,484 L0,534 L-50,484 Z"/);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,14);
  assert.match(svg,/data-cell="s3-10" d="M-50 484 L50 484"/);
  assert.match(svg,/data-cell="s3-10" d="M0 434 L0 534"/);
  assert.doesNotMatch(svg,/<path class="space-frame|aluminium-bottom-triangle|drawing-unavailable/);
  assert.match(svg,/viewBox="-136 14 272 550"/);assert.equal(JSON.stringify(d),before);
});

test('Al27 replaces the shell-3 wrapper with a bottom PE triangle', () => {
  const d=fixtures.Al27,before=JSON.stringify(d),svg=context.IsotopeWiring.renderSVG(d,{standalone:true});
  assert.equal(d.Z,13);assert.equal(d.N,14);assert.deepEqual(d.expectedByShell,[2,8,3]);
  assert.equal(d.graph.pairs.length,13);assert.equal(d.graph.witnesses.length,14);
  assert.equal(context.IsotopeWiring.validate(d).valid,true);assert.equal(inspectDefinition(d).status,'verified');
  assert.deepEqual(d.graph.witnesses,fixtures.Mg26.graph.witnesses);
  assert.match(svg,/class="space-frame lithium-sector" d="M0 134 L110 244 L0 354 L-110 244 Z"/);
  assert.match(svg,/class="neutron magnesium-bottom-square" data-cell="s3-00" d="M0,354 L50,404 L0,454 L-50,404 Z"/);
  assert.match(svg,/class="neutron aluminium-bottom-triangle" data-cell="s3-10" d="M0,454 L-50,504 L50,504 Z"/);
  assert.equal([...svg.matchAll(/class="space-frame/g)].length,1);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,12);
  assert.doesNotMatch(svg,/magnesium-sector|class="neutron sketch-cross" data-cell="s3-10"|drawing-unavailable/);
  assert.match(svg,/viewBox="-136 14 272 520"/);assert.equal(JSON.stringify(d),before);
});

test('Mg26 adds a shell-3 wrapper while retaining six crossed squares', () => {
  const d=fixtures.Mg26,before=JSON.stringify(d),svg=context.IsotopeWiring.renderSVG(d,{standalone:true});
  assert.equal(d.Z,12);assert.equal(d.N,14);assert.deepEqual(d.expectedByShell,[2,8,2]);
  assert.equal(d.graph.pairs.length,12);assert.equal(d.graph.witnesses.length,14);
  assert.equal(context.IsotopeWiring.validate(d).valid,true);assert.equal(inspectDefinition(d).status,'verified');
  assert.deepEqual(d.graph.pairs,fixtures.Mg25.graph.pairs);
  assert.match(svg,/class="space-frame lithium-sector" d="M0 134 L110 244 L0 354 L-110 244 Z"/);
  assert.match(svg,/class="space-frame magnesium-sector" d="M0 354 L60 414 L0 474 L-60 414 Z"/);
  assert.match(svg,/class="neutron magnesium-bottom-square" data-cell="s3-00" d="M0,364 L50,414 L0,464 L-50,414 Z"/);
  assert.equal([...svg.matchAll(/class="space-frame/g)].length,2);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,12);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross" data-cell="s3-00"/g)].length,2);
  assert.match(svg,/data-cell="s3-00" d="M-50 414 L50 414"/);
  assert.match(svg,/data-cell="s3-00" d="M0 364 L0 464"/);
  assert.match(svg,/viewBox="-136 14 272 490"/);assert.equal(JSON.stringify(d),before);
});

test('Mg25 adds a shell-2 neutron wrapper to six crossed squares', () => {
  const d=fixtures.Mg25,before=JSON.stringify(d),svg=context.IsotopeWiring.renderSVG(d,{standalone:true});
  assert.equal(d.Z,12);assert.equal(d.N,13);assert.deepEqual(d.expectedByShell,[2,8,2]);
  assert.equal(d.graph.pairs.length,12);assert.equal(d.graph.witnesses.length,13);
  assert.equal(context.IsotopeWiring.validate(d).valid,true);assert.equal(inspectDefinition(d).status,'verified');
  assert.deepEqual(d.graph.pairs,fixtures.Mg24.graph.pairs);
  assert.equal(d.graph.witnesses.filter(w=>w.kind==='boundary'&&w.shell==='s2').length,1);
  assert.match(svg,/class="neutron magnesium-bottom-square" data-cell="s3-00" d="M0,354 L50,404 L0,454 L-50,404 Z"/);
  assert.match(svg,/class="space-frame lithium-sector" d="M0 134 L110 244 L0 354 L-110 244 Z"/);
  assert.equal([...svg.matchAll(/class="space-frame/g)].length,1);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,12);
  assert.match(svg,/data-cell="s3-00" d="M-50 404 L50 404"/);
  assert.match(svg,/data-cell="s3-00" d="M0 354 L0 454"/);
  assert.doesNotMatch(svg,/sodium-bottom-triangle|drawing-unavailable/);
  assert.match(svg,/viewBox="-136 14 272 470"/);assert.equal(JSON.stringify(d),before);
});

test('Mg24 has six crossed squares joined without a neutron wrapper', () => {
  const d=fixtures.Mg24,before=JSON.stringify(d),svg=context.IsotopeWiring.renderSVG(d,{standalone:true});
  assert.equal(d.Z,12);assert.equal(d.N,12);assert.deepEqual(d.expectedByShell,[2,8,2]);
  assert.equal(d.graph.pairs.length,12);assert.equal(d.graph.witnesses.length,12);
  assert.equal(context.IsotopeWiring.validate(d).valid,true);
  assert.equal(inspectDefinition(d).status,'verified');
  assert.match(svg,/class="neutron magnesium-bottom-square" data-cell="s3-00" d="M0,334 L50,384 L0,434 L-50,384 Z"/);
  assert.match(svg,/class="neutron beryllium-square" data-cell="s2-01" d="M0,134 L50,184 L0,234 L-50,184 Z"/);
  assert.match(svg,/class="neutron carbon-bottom-square" data-cell="s2-10" d="M0,234 L50,284 L0,334 L-50,284 Z"/);
  assert.doesNotMatch(svg,/<path class="space-frame/);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,12);
  assert.match(svg,/data-cell="s3-00" d="M-50 384 L50 384"/);
  assert.match(svg,/data-cell="s3-00" d="M0 334 L0 434"/);
  assert.doesNotMatch(svg,/sodium-bottom-triangle|drawing-unavailable/);
  assert.match(svg,/viewBox="-136 14 272 450"/);assert.equal(JSON.stringify(d),before);
});

test('Na23 wraps the Ne20 squares and grows a triangle from the wrapper bottom', () => {
  const before=JSON.stringify(fixtures.Na23),svg=context.IsotopeWiring.renderSVG(fixtures.Na23,{standalone:true});
  assert.match(svg,/class="neutron beryllium-square" data-cell="s2-01" d="M0,144 L50,194 L0,244 L-50,194 Z"/);
  assert.match(svg,/class="neutron carbon-bottom-square" data-cell="s2-10" d="M0,244 L50,294 L0,344 L-50,294 Z"/);
  assert.match(svg,/class="neutron oxygen-right-square" data-cell="s2-00" d="M50,194 L100,244 L50,294 L0,244 Z"/);
  assert.match(svg,/class="neutron oxygen-left-square" data-cell="s2-11" d="M-50,194 L0,244 L-50,294 L-100,244 Z"/);
  assert.match(svg,/class="space-frame lithium-sector" d="M0 134 L110 244 L0 354 L-110 244 Z"/);
  assert.match(svg,/class="neutron sodium-bottom-triangle" data-cell="s3-00" d="M0,354 L-50,404 L50,404 Z"/);
  assert.equal([...svg.matchAll(/class="space-frame/g)].length,1);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,10);
  for(const cell of ['s1-00','s2-01','s2-10','s2-00','s2-11'])assert.equal([...svg.matchAll(new RegExp('class="neutron sketch-cross" data-cell="'+cell+'"','g'))].length,2);
  assert.doesNotMatch(svg,/class="neutron sketch-cross" data-cell="s3-|drawing-unavailable/);
  assert.match(svg,/viewBox="-136 14 272 420"/);assert.equal(JSON.stringify(fixtures.Na23),before);
});

test('Ne20 removes the wrapper and fully crosses both side squares', () => {
  const before=JSON.stringify(fixtures.Ne20),svg=context.IsotopeWiring.renderSVG(fixtures.Ne20,{standalone:true});
  assert.match(svg,/class="neutron beryllium-square" data-cell="s2-01" d="M0,134 L50,184 L0,234 L-50,184 Z"/);
  assert.match(svg,/class="neutron carbon-bottom-square" data-cell="s2-10" d="M0,234 L50,284 L0,334 L-50,284 Z"/);
  assert.match(svg,/class="neutron oxygen-right-square" data-cell="s2-00" d="M50,184 L100,234 L50,284 L0,234 Z"/);
  assert.match(svg,/class="neutron oxygen-left-square" data-cell="s2-11" d="M-50,184 L0,234 L-50,284 L-100,234 Z"/);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,10);
  for(const cell of ['s1-00','s2-01','s2-10','s2-00','s2-11'])assert.equal([...svg.matchAll(new RegExp('class="neutron sketch-cross" data-cell="'+cell+'"','g'))].length,2);
  assert.match(svg,/data-cell="s2-11" d="M-100 234 L0 234"/);
  assert.match(svg,/data-cell="s2-11" d="M-50 184 L-50 284"/);
  assert.doesNotMatch(svg,/<path class="space-frame|middle-triangle|left-triangle|drawing-unavailable/);
  assert.match(svg,/viewBox="-136 14 272 370"/);assert.equal(JSON.stringify(fixtures.Ne20),before);
});

test('F19 replaces only the O17 right triangle with a fully crossed square', () => {
  const before=JSON.stringify(fixtures.F19),svg=context.IsotopeWiring.renderSVG(fixtures.F19,{standalone:true});
  assert.match(svg,/class="neutron beryllium-square" data-cell="s2-01" d="M0,144 L50,194 L0,244 L-50,194 Z"/);
  assert.match(svg,/class="neutron carbon-bottom-square" data-cell="s2-10" d="M0,244 L50,294 L0,344 L-50,294 Z"/);
  assert.match(svg,/class="neutron oxygen-right-square" data-cell="s2-00" d="M50,194 L100,244 L50,294 L0,244 Z"/);
  assert.match(svg,/class="neutron oxygen-left-triangle" data-cell="s2-11" d="M0,244 L-50,294 L-50,194 Z"/);
  assert.match(svg,/class="space-frame lithium-sector" d="M0 134 L110 244 L0 354 L-110 244 Z"/);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,8);
  for(const cell of ['s1-00','s2-01','s2-10','s2-00'])assert.equal([...svg.matchAll(new RegExp('class="neutron sketch-cross" data-cell="'+cell+'"','g'))].length,2);
  assert.doesNotMatch(svg,/class="neutron sketch-cross" data-cell="s2-11"/);
  assert.doesNotMatch(svg,/middle-triangle|oxygen-left-square|drawing-unavailable/);
  assert.match(svg,/viewBox="-136 14 272 370"/);assert.equal(JSON.stringify(fixtures.F19),before);
});

test('O18 extends C13 with a crossed right square and uncrossed left square', () => {
  const before=JSON.stringify(fixtures.O18),svg=context.IsotopeWiring.renderSVG(fixtures.O18,{standalone:true});
  assert.match(svg,/class="neutron beryllium-square" data-cell="s2-01" d="M0,144 L50,194 L0,244 L-50,194 Z"/);
  assert.match(svg,/class="neutron carbon-bottom-square" data-cell="s2-10" d="M0,244 L50,294 L0,344 L-50,294 Z"/);
  assert.match(svg,/class="neutron oxygen-right-square" data-cell="s2-00" d="M50,194 L100,244 L50,294 L0,244 Z"/);
  assert.match(svg,/class="neutron oxygen-left-square" data-cell="s2-11" d="M-50,194 L0,244 L-50,294 L-100,244 Z"/);
  assert.match(svg,/class="space-frame lithium-sector" d="M0 134 L110 244 L0 354 L-110 244 Z"/);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,8);
  assert.match(svg,/class="neutron sketch-cross" data-cell="s2-00" d="M0 244 L100 244"/);
  assert.match(svg,/class="neutron sketch-cross" data-cell="s2-00" d="M50 194 L50 294"/);
  assert.doesNotMatch(svg,/class="neutron sketch-cross" data-cell="s2-11"|middle-triangle|left-triangle|drawing-unavailable/);
  assert.match(svg,/viewBox="-136 14 272 370"/);assert.equal(JSON.stringify(fixtures.O18),before);
});

test('O17 adds the shell-2 wrapper around the O16 squares and mirrored triangles', () => {
  const before=JSON.stringify(fixtures.O17),svg=context.IsotopeWiring.renderSVG(fixtures.O17,{standalone:true});
  assert.match(svg,/class="neutron beryllium-square" data-cell="s2-01" d="M0,144 L50,194 L0,244 L-50,194 Z"/);
  assert.match(svg,/class="neutron carbon-bottom-square" data-cell="s2-10" d="M0,244 L50,294 L0,344 L-50,294 Z"/);
  assert.match(svg,/class="neutron nitrogen-middle-triangle" data-cell="s2-00" d="M0,244 L50,294 L50,194 Z"/);
  assert.match(svg,/class="neutron oxygen-left-triangle" data-cell="s2-11" d="M0,244 L-50,294 L-50,194 Z"/);
  assert.match(svg,/class="space-frame lithium-sector" d="M0 134 L110 244 L0 354 L-110 244 Z"/);
  assert.equal([...svg.matchAll(/class="space-frame lithium-sector"/g)].length,1);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,6);
  assert.doesNotMatch(svg,/boron-growth-square|drawing-unavailable/);
  assert.match(svg,/viewBox="-136 14 272 370"/);assert.equal(JSON.stringify(fixtures.O17),before);
});

test('O16 mirrors the N14 triangle across the axis without moving crossed squares', () => {
  const original=JSON.stringify(fixtures.O16),svg=context.IsotopeWiring.renderSVG(fixtures.O16,{standalone:true});
  assert.match(svg,/class="neutron beryllium-square" data-cell="s2-01" d="M0,134 L50,184 L0,234 L-50,184 Z"/);
  assert.match(svg,/class="neutron carbon-bottom-square" data-cell="s2-10" d="M0,234 L50,284 L0,334 L-50,284 Z"/);
  assert.match(svg,/class="neutron nitrogen-middle-triangle" data-cell="s2-00" d="M0,234 L50,284 L50,184 Z"/);
  assert.match(svg,/class="neutron oxygen-left-triangle" data-cell="s2-11" d="M0,234 L-50,284 L-50,184 Z"/);
  assert.equal([...svg.matchAll(/class="neutron neutron-v"/g)].length,2);
  assert.equal([...svg.matchAll(/class="neutron sketch-cross"/g)].length,6);
  assert.doesNotMatch(svg,/<path class="ep |<path class="space-frame|drawing-unavailable/);
  assert.match(svg,/viewBox="-136 14 272 370"/);
  assert.equal(JSON.stringify(fixtures.O16),original);
});

test('interactive diagrams have one keyboard entry and read-only diagrams retain labels without controls', () => {
  const render = context.IsotopeWiring.renderSVG;
  const svg = render(fixtures.V51, { focusCell: 's3-10' });
  assert.equal([...svg.matchAll(/tabindex="0"/g)].length, 1);
  assert.match(svg, /data-cell="s3-10"[^>]*tabindex="0"[^>]*aria-label="s3-10: 1 EP, 2 N"/);
  assert.match(svg, /role="group"/);
  const comparison = render(fixtures.O16, { interactive: false, labels: true });
  assert.doesNotMatch(comparison, /class="cell-hit"/);
  assert.match(comparison, /class="cell-number"/);
  assert.match(comparison, /role="img"/);
});

test('bounded destination surveys agree with individual checks and preserve the source', () => {
  const source = clone(fixtures.O16), before = clone(source);
  const all = surveyPlacements(source, 'witnesses', 's2-01-H');
  assert.equal(all.total, 3); assert.equal(all.sourceStatus, 'verified'); assert.equal(all.complete, true);
  assert.deepEqual(all.rows.map(r => r.cell), ['s2-00','s2-10','s2-11']);
  assert.equal(all.rows.filter(r => r.status === 'verified').length, 1);
  for (const row of all.rows) {
    assert.equal(row.status, trialWitnessPlacement(source, 's2-01-H', row.cell).report.status);
    assert.equal(row.inventoryStatus, 'verified', 'Inventory alone does not distinguish the failed destinations');
  }
  assert(all.rows[1].findings.some(f => f.codes.includes('duplicate-witness-slot')));
  const first = surveyPlacements(source, 'witnesses', 's2-01-H', { limit: 2 });
  assert.equal(first.complete, false);
  const last = surveyPlacements(source, 'witnesses', 's2-01-H', { offset: first.nextOffset, limit: 2 });
  assert.deepEqual([...first.rows, ...last.rows], all.rows); assert(last.complete);
  assert.deepEqual(source, before);
  const ep = surveyPlacements(fixtures.V51, 'pairs', 's3-10-upper');
  assert.equal(ep.rows.length, 8);
  assert.equal(ep.rows.find(r => r.cell === 's3-01').status, 'verified');
  assert.equal(ep.rows.find(r => r.cell === 's3-00').status, 'refuted');
  assert.match(ep.scope, /not a physical uniqueness test/);
});

test('survey bounds, ownership, empty shells and unknown targets are explicit', () => {
  const source = clone(fixtures.O16);
  for (const options of [{ limit: 9 }, { limit: 0 }, { offset: -1 }, { offset: 4 }, { limit: 1.5 }]) {
    assert.throws(() => surveyPlacements(source, 'witnesses', 's2-01-H', options), /Survey/);
  }
  assert.throws(() => surveyPlacements(source, 'other', 's2-01-H'), /pairs or witnesses/);
  assert.throws(() => surveyPlacements(fixtures.Ti48, 'witnesses', 's3-boundary'), /cell-owned/);
  const empty = surveyPlacements(source, 'witnesses', 's1-00-H');
  assert.equal(empty.total, 0); assert.deepEqual(empty.rows, []); assert(empty.complete);
  delete source.N;
  const unknown = surveyPlacements(source, 'witnesses', 's2-01-H');
  assert.equal(unknown.sourceStatus, 'unknown');
  assert.equal(unknown.rows.find(r => r.cell === 's2-00').status, 'unknown');
  assert(unknown.rows.every(r => r.inventoryStatus === 'unknown'));
});

test('neutron line trials preserve identity, axis, inventories and source while retaining uncertainty', () => {
  const source = clone(fixtures.O16), before = clone(source);
  const { definition, report, difference } = trialWitnessPlacement(source, 's2-01-H', 's2-00');
  assert.deepEqual(source, before);
  assert.equal(report.status, 'verified');
  assert.equal(definition.status, 'unresolved');
  const witness = definition.graph.witnesses.find(w => w.id === 's2-01-H');
  assert.equal(witness.cell, 's2-00'); assert.equal(witness.axis, 'H'); assert.equal(witness.shell, 's2');
  assert.deepEqual(definition.graph.pairs, source.graph.pairs);
  assert.equal(definition.graph.witnesses.length, source.graph.witnesses.length);
  for (const key of ['Z','N','expectedByShell']) assert.deepEqual(definition[key], source[key]);
  assert.equal(difference.changes.length, 1); assert.equal(difference.changes[0].collection, 'witnesses');
  assert.deepEqual(JSON.parse(JSON.stringify(context.IsotopeWiring.placementReview(definition))).cells, ['s2-00']);
  const delta = context.IsotopeWiring.diff(source, definition);
  const replay = context.IsotopeWiring.compile(delta, { [source.id]: source });
  assert.deepEqual(clone(replay).graph, definition.graph);
  assert.deepEqual(clone(replay).placementQuestions, definition.placementQuestions);
});

test('witness trials reject invalid ownership and expose occupied-axis failures without deleting records', () => {
  const source = clone(fixtures.O16);
  const failed = trialWitnessPlacement(source, 's2-01-H', 's2-10');
  assert.equal(failed.report.status, 'refuted');
  assert(failed.report.checks.some(c => c.issues.some(i => i.code === 'duplicate-witness-slot')));
  assert.equal(failed.definition.graph.witnesses.length, source.graph.witnesses.length);
  assert.throws(() => trialWitnessPlacement(source, 's2-01-H', 's1-00'), /same shell/);
  assert.throws(() => trialWitnessPlacement(source, 's2-01-H', 's2-01'), /different cell/);
  assert.throws(() => trialWitnessPlacement(source, 'missing', 's2-00'), /existing neutron/);
  assert.throws(() => trialWitnessPlacement(fixtures.Ti48, 's3-boundary', 's3-00'), /shell-owned/);
  source.graph.witnesses.find(w => w.id === 's2-01-H').history = null;
  assert.throws(() => trialWitnessPlacement(source, 's2-01-H', 's2-00'), /history/);
});

test('witness question anchors follow records and malformed or shell-owned anchors stay unlocated', () => {
  const source = clone(fixtures.Ti48);
  source.placementQuestions = [{ witnessIds: ['s2-01-H'], reason: 'Question' }];
  const review = doc => clone(context.IsotopeWiring.placementReview(doc));
  assert.deepEqual(review(source).cells, ['s2-01']);
  source.graph.witnesses.find(w => w.id === 's2-01-H').cell = 's2-00';
  assert.deepEqual(review(source).cells, ['s2-00']);
  for (const witnessIds of ['bad', [null], ['missing'], ['s3-boundary']]) {
    source.placementQuestions = [{ witnessIds, reason: 'Question' }];
    assert.deepEqual(review(source).cells, []); assert(review(source).questions[0].missing);
  }
});

test('live editor checks match the Node core for all fixtures and malformed model inputs', () => {
  const badRoute = clone(fixtures.O16); badRoute.graph.pairs[0].red = ['T', 'B'];
  const missingTarget = clone(fixtures.O16); delete missingTarget.N;
  for (const source of [...Object.values(fixtures), badRoute, missingTarget]) {
    const packet = importLegacyAbsolute(source), expected = verifyModel(packet.object, packet.modelContext), actual = inspectDefinition(source);
    assert.equal(actual.status, expected.status, source.id);
    assert.deepEqual(withoutCells(actual), expected.checks);
    assert.equal(Object.hasOwn(actual, 'inputDigest'), false, 'Live checks do not claim an archival digest');
  }
});

test('invalid structural references surface as import failure, not a passing model', () => {
  const source = clone(fixtures.O16); source.graph.pairs[0].cell = 'absent';
  const result = inspectDefinition(source);
  assert.equal(result.status, 'invalid'); assert.match(result.error, /ownership/);
  assert.deepEqual(result.checks, []);
});

test('failed shell checks identify inspectable cells', () => {
  const source = fixtures['V51-conflict'], result = inspectDefinition(source);
  const issue = result.checks.flatMap(c => c.issues).find(i => i.code === 'shell-count');
  assert(issue.cells.length > 0);
  for (const id of issue.cells) assert(source.graph.cells.some(c => c.id === id && c.shell === issue.id));
});

test('structural neighborhoods use occupied shell-local support, not screen coincidence', () => {
  const source = fixtures.O16, result = inspectDefinition(source);
  assert.equal(result.cells['s1-00'].ports.length, 4);
  assert.deepEqual(result.cells['s1-00'].neighbors, []);
  assert(Object.values(result.cells).some(c => c.neighbors.length > 0));
  for (const [id, cell] of Object.entries(result.cells)) for (const neighbor of cell.neighbors) {
    assert.equal(source.graph.cells.find(c => c.id === id).shell, source.graph.cells.find(c => c.id === neighbor).shell);
    assert(result.cells[neighbor].neighbors.includes(id));
  }
});

test('working-definition comparison identifies added, removed and changed records with before/after data', () => {
  const source = fixtures.O16, target = clone(fixtures.O17);
  target.graph.pairs[0].history.push('research edit');
  target.graph.witnesses.splice(0, 1);
  const result = compareDefinitions(source, target);
  for (const kind of ['added', 'removed', 'changed']) assert(result.changes.some(c => c.change === kind), kind);
  const changed = result.changes.find(c => c.change === 'changed');
  assert.deepEqual(changed.before, source.graph.pairs[0]);
  assert.deepEqual(changed.after, target.graph.pairs[0]);
  assert.deepEqual(changed.cells, [target.graph.pairs[0].cell]);
});

test('comparison distinguishes metadata deletion, null and absent values without mutating inputs', () => {
  const source = clone(fixtures.O16), target = clone(source);
  source.extra = 'remove'; target.nullable = null; delete target.notes;
  const before = JSON.stringify([source, target]), result = compareDefinitions(source, target);
  assert.equal(result.changes.length, 0);
  assert(result.metadata.some(m => m.key === 'extra' && m.before === 'remove' && m.after === undefined));
  assert(result.metadata.some(m => m.key === 'nullable' && m.before === undefined && m.after === null));
  assert.equal(JSON.stringify([source, target]), before);
  const checked = inspectDefinition(source);
  assert(Object.isFrozen(checked.cells));
  assert.equal(JSON.stringify([source, target]), before);
});

const core = context.IsotopeWiring;
const overlayPaths = svg => [...svg.matchAll(/<path class="difference-mark [^"]+" data-change="([^"]+)" data-side="([^"]+)" data-record="([^"]+)" d="([^"]+)"/g)]
  .map(([, change, side, id, path]) => ({ change, side, id, path }));

test('graphical differences preserve added/removed/changed ownership and do not mutate definitions', () => {
  const before = fixtures.O16, after = clone(fixtures.O17);
  after.graph.pairs[0].history.push('changed history'); after.graph.witnesses.splice(0, 1);
  const original = JSON.stringify([before, after]), difference = compareDefinitions(before, after);
  const paths = overlayPaths(core.renderSVG(after, { before, changes: difference.changes }));
  for (const kind of ['added', 'removed', 'changed']) assert(paths.some(p => p.change === kind));
  assert(paths.filter(p => p.change === 'removed').every(p => p.side === 'before'));
  assert(paths.filter(p => p.change === 'added').every(p => p.side === 'after'));
  assert.equal(paths.filter(p => p.id === after.graph.pairs[0].id).length, 4, 'Both colored routes retain both versions');
  assert.equal(JSON.stringify([before, after]), original);
  assert.equal(overlayPaths(core.renderSVG(after)).length, 0);
});

test('changed witness shows its old horizontal and new vertical geometry', () => {
  const before = fixtures.O17, after = clone(before);
  const witness = after.graph.witnesses.find(w => w.id === 's2-00-H'); witness.axis = 'V';
  const paths = overlayPaths(core.renderSVG(after, { before, changes: compareDefinitions(before, after).changes })).filter(p => p.id === witness.id);
  assert.equal(paths.length, 2);
  assert.notEqual(paths[0].path, paths[1].path);
  assert.deepEqual(paths.map(p => p.side), ['before', 'after']);
});

test('removed shells/cells stay visible and the comparison viewport fits both definitions', () => {
  const before = fixtures.V51, after = fixtures.O16, difference = compareDefinitions(before, after);
  const svg = core.renderSVG(after, { before, changes: difference.changes });
  const paths = overlayPaths(svg), view = svg.match(/viewBox="([^"]+)"/)[1].split(' ').map(Number);
  assert(paths.some(p => p.id === 's4' && p.change === 'removed'));
  assert(paths.some(p => p.id === 's4-00' && p.change === 'removed'));
  for (const doc of [before, after]) {
    const g = core.geometry(doc);
    assert(view[2] >= g.width + 10); assert(view[3] >= g.height);
  }
  const exported = core.renderSVG(after, { standalone: true, before, changes: difference.changes });
  assert.match(exported, /Removed: dashed pink/);
  assert.match(exported, /Independent layouts, not a physical transition/);
  assert.match(exported, /stroke-dasharray:8 5/);
  assert(overlayPaths(exported).length > 0);
});

test('placement metadata is retained without question overlays or export caveats', () => {
  const source = fixtures.V51, review = core.placementReview(source);
  assert.equal(inspectDefinition(source).status, 'verified');
  assert.equal(review.unresolved, true);
  assert.deepEqual(clone(review.cells), ['s3-10']);
  assert.doesNotMatch(core.renderSVG(source), /data-question-cell=/);
  const exported = core.renderSVG(source, { standalone: true });
  assert.doesNotMatch(exported, /Placement unresolved|question-badge/);
  const unlocated = clone(source); delete unlocated.placementQuestions;
  assert.equal(core.placementReview(unlocated).cells.length, 0);
  assert.equal(core.placementReview(unlocated).questions[0].missing, true);
  assert.doesNotMatch(core.renderSVG(unlocated), /data-question-cell=/);
});

test('malformed and missing placement anchors are surfaced rather than guessed', () => {
  for (const questions of [{ wrong: true }, [{ reason: 'Unknown location', pairIds: ['absent'] }], [{ reason: 'Bad type', cellIds: 's3-10' }]]) {
    const source = { ...clone(fixtures.O16), placementQuestions: questions };
    const review = core.placementReview(source);
    assert.equal(review.unresolved, true); assert.equal(review.cells.length, 0);
    assert(review.questions.some(q => q.missing));
  }
});

test('same-shell placement trial preserves inventory and identity without resolving the question', () => {
  const source = fixtures.V51, before = JSON.stringify(source);
  const result = trialPairPlacement(source, 's3-10-upper', 's3-01'), target = result.definition;
  assert.equal(result.report.status, 'verified');
  assert.equal(target.graph.pairs.find(p => p.id === 's3-10-upper').cell, 's3-01');
  assert.deepEqual([target.Z, target.N, target.expectedByShell], [source.Z, source.N, source.expectedByShell]);
  assert.equal(target.graph.pairs.length, source.graph.pairs.length);
  assert.deepEqual(target.graph.witnesses, source.graph.witnesses);
  assert.equal(result.difference.changes.length, 1);
  assert.equal(result.difference.changes[0].change, 'changed');
  assert.equal(target.status, 'unresolved');
  assert.deepEqual(clone(core.placementReview(target).cells), ['s3-01']);
  assert.equal(JSON.stringify(source), before);
  assert.equal(source.graph.pairs.find(p => p.id === 's3-10-upper').cell, 's3-10');
  assert.deepEqual(clone(core.compile(core.diff(source, target), { V51: source })), target);
  assert.doesNotMatch(core.renderSVG(target, { interactive: false }), /class="cell-hit"/);
});

test('invalid trial requests are rejected; overfilled destinations remain explicit failed candidates', () => {
  const source = fixtures.V51, before = JSON.stringify(source);
  for (const [pair, cell, message] of [['absent','s3-01',/existing EP/],['s3-10-upper','absent',/existing destination/],['s3-10-upper','s4-00',/same shell/],['s3-10-upper','s3-10',/different cell/]]) {
    assert.throws(() => trialPairPlacement(source, pair, cell), message);
  }
  const failed = trialPairPlacement(source, 's3-10-upper', 's3-00');
  assert.equal(failed.report.status, 'refuted');
  assert(failed.report.checks.flatMap(c => c.issues).some(i => i.code === 'cell-capacity'));
  assert.equal(failed.definition.graph.pairs.length, source.graph.pairs.length);
  assert.equal(JSON.stringify(source), before);
});
