import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import vm from 'node:vm';
const context=vm.createContext({});vm.runInContext(readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8').match(/<script>([\s\S]*?)<\/script>/)[1],context);
const api=context.IsotopeWiring;
test('Li6 local line colors are preserved under the lower triangle reflection, including export',()=>{
 for(const standalone of [false,true]){
  const svg=api.renderSVG(api.fixtures().Li6,{standalone});
  const paths=[...svg.matchAll(/<path class="neutron ([^"]+)"([^>]+)>/g)];assert.equal(paths.length,8);assert.doesNotMatch(svg,/class="neutron sketch-cross" data-cell="s1-00" d="M0 34 L0 134"/);assert.match(svg,/class="neutron sketch-cross" data-cell="s1-00" d="M-50 84 L50 84"/);
  for(const [,cls,attrs] of paths){const coords=attrs.match(/d="([^"]+)"/)[1].match(/-?\d+(?:\.\d+)?/g).map(Number);for(let i=2;i<coords.length;i+=2){const dx=coords[i]-coords[i-2],dy=coords[i+1]-coords[i-1];if(dx&&dy){const nwse=dx*dy>0;assert(attrs.includes(`stroke:${nwse?'#2878c8':'#c64b46'}`));assert(attrs.includes(`data-direction="${nwse?'NW-SE':'NE-SW'}"`));}else assert(!attrs.includes('style="stroke:'));}}
 }
});
test('Li6 retains centered arrows on its original edges, not on the added side bars',()=>{
 for(const standalone of [false,true]){
  const svg=api.renderSVG(api.fixtures().Li6,{standalone}),arrows=[...svg.matchAll(/class="mid-arrow" data-flow="([^"]+)" data-midpoint="([^"]+)" data-vector="([^"]+)"[^>]*fill="([^"]+)"/g)];
  assert.equal(arrows.length,8);assert.equal(arrows.filter(a=>a[1]==='up').length,3);assert.equal(arrows.filter(a=>a[1]==='down').length,3);assert.equal(arrows.filter(a=>a[1]==='right').length,2);
  const edges=[...svg.matchAll(/<path class="neutron (?!lithium-side-bar)[^"]+"[^>]* d="M([^L]+) L([^"]+)"/g)].map(m=>{const a=m[1].trim().split(/\s+/).map(Number),b=m[2].trim().split(/\s+/).map(Number);return `${(a[0]+b[0])/2} ${(a[1]+b[1])/2}`;});
  assert.deepEqual(arrows.map(a=>a[2]).sort(),edges.sort());
  for(const [,flow,,vector,color] of arrows){const [dx,dy]=vector.split(' ').map(Number);if(flow==='up'){assert(dy<0);assert.equal(color,'#2878c8');}else if(flow==='down'){assert(dy>0);assert.equal(color,'#c64b46');}else{assert(dx>0);assert.equal(dy,0);assert.equal(color,'var(--green,#4e824b)');}}
 }
});
test('both lithium drawings mirror the complete lower triangle, including its arrows',()=>{
 for(const id of ['Li6','Li7'])for(const standalone of [false,true]){const svg=api.renderSVG(api.fixtures()[id],{standalone}),group=svg.match(/<g class="lithium-bottom-reflection" transform="scale\(-1 1\)">([\s\S]*?)<\/g>/)?.[1];assert(group);assert.equal((group.match(/class="mid-arrow"/g)||[]).length,3);assert.match(group,/class="neutron lithium-base"/);assert.doesNotMatch(group,/s1-00/);}
});
test('only Li7 adds undirected green side bars to the Li6 geometry',()=>{
 for(const standalone of [false,true]){const svg=api.renderSVG(api.fixtures().Li7,{standalone}),bars=[...svg.matchAll(/<path class="neutron lithium-side-bar" data-side="([^"]+)" d="([^"]+)"[^>]*>/g)];assert.deepEqual(bars.map(m=>m.slice(1)),[['left','M-50 84 L-50 184'],['right','M50 84 L50 184']]);for(const bar of bars)assert.doesNotMatch(bar[0],/marker-|data-flow/);const li6=api.renderSVG(api.fixtures().Li6,{standalone});assert.doesNotMatch(li6,/lithium-side-bar/);const geometry=s=>[...s.matchAll(/<path class="neutron (?!lithium-side-bar)[^"]+"[^>]* d="([^"]+)"/g)].map(m=>m[1]);assert.deepEqual(geometry(svg),geometry(li6));}
});
test('Li7 inherits Li6 layout and scale from its drawing recipe, preserving its own identity',()=>{
 const r6=JSON.parse(JSON.stringify(api.drawingRecipe('Li6'))),r7=JSON.parse(JSON.stringify(api.drawingRecipe('Li7')));assert.equal(r7.template,'Li6');assert.deepEqual(r7.viewBox,r6.viewBox);assert.equal(r7.addEdges.length,2);assert(r7.addEdges.every(e=>e.color==='green'&&!e.directed&&e.from[0]===e.to[0]));
 for(const standalone of [false,true]){const a=api.renderSVG(api.fixtures().Li6,{standalone}),b=api.renderSVG(api.fixtures().Li7,{standalone});assert.equal(a.match(/viewBox="([^"]+)"/)[1],b.match(/viewBox="([^"]+)"/)[1]);assert.match(b,/data-definition="Li7"/);assert.match(b,/data-drawing-base="Li6"/);assert.match(b,/aria-label="Lithium-7 neutron diagram"/);if(!standalone)assert.match(b,/aria-label="s2-01: 1 EP, 2 N"/);}
});
test('Li7 retains its inventory without the rejected subdivision or unresolved-placement label',()=>{
 const doc=api.fixtures().Li7;assert.equal(doc.graph.pairs.length,3);assert.equal(doc.graph.witnesses.length,4);
 for(const standalone of [false,true]){
  const svg=api.renderSVG(doc,{standalone});
  assert.doesNotMatch(svg,/serial-neutral|neutral-junction|neutral-label/);
  assert.match(svg,/class="neutron lithium-base" data-cell="s2-01" d="M-50 184 L50 184"/);
  assert.equal((svg.match(/class="mid-arrow"/g)||[]).length,8);assert.equal((svg.match(/data-flow="right"/g)||[]).length,2);
  assert.doesNotMatch(svg,/Additional neutron: placement unresolved/);
 }
});
test('Be9 inherits Li7 and adds only the reflected top sides, reusing its green base',()=>{
 const recipe=JSON.parse(JSON.stringify(api.drawingRecipe('Be9')));assert.equal(recipe.extends,'Li7');assert.equal(recipe.addEdges.length,4);
 for(const standalone of [false,true]){const svg=api.renderSVG(api.fixtures().Be9,{standalone});assert.match(svg,/data-drawing-base="Li7"/);assert.match(svg,/data-definition="Be9"/);assert.match(svg,/data-edge="bottom-red" style="stroke:#c64b46" d="M0 234 L50 184"/);assert.match(svg,/data-edge="bottom-blue" style="stroke:#2878c8" d="M-50 184 L0 234"/);assert.equal((svg.match(/class="neutron lithium-base"/g)||[]).length,1);assert.equal((svg.match(/class="mid-arrow"/g)||[]).length,10);assert.match(svg,/data-flow="up" data-midpoint="25 209"/);assert.match(svg,/data-flow="down" data-midpoint="-25 209"/);assert.doesNotMatch(svg,/class="boundary-dot"|class="neutron beryllium-square"/);}
});
test('B10 is Li6 plus an identical upper square translated up one hundred units',()=>{
 const recipe=JSON.parse(JSON.stringify(api.drawingRecipe('B10')));assert.equal(recipe.extends,'Li6');assert.equal(recipe.reflectBaseX,true);assert.equal(recipe.addEdges.length,5);assert.deepEqual(recipe.viewBox,[-86,-86,172,300]);
 for(const standalone of [false,true]){const svg=api.renderSVG(api.fixtures().B10,{standalone});assert.match(svg,/data-definition="B10"/);assert.match(svg,/data-drawing-base="Li6"/);assert.match(svg,/<g class="recipe-base-reflection" data-shell="s2" transform="scale\(-1 1\)">/);const additions=[...svg.matchAll(/class="neutron recipe-edge" data-edge="([^"]+)"[^>]* d="([^"]+)"/g)].map(m=>m.slice(1));assert.deepEqual(additions,[['upper-red-top','M0 -66 L-50 -16'],['upper-blue-top','M50 -16 L0 -66'],['upper-red-bottom','M50 -16 L0 34'],['upper-blue-bottom','M0 34 L-50 -16'],['upper-green','M-50 -16 L50 -16']]);assert.equal((svg.match(/class="mid-arrow"/g)||[]).length,13);assert.doesNotMatch(svg,/lithium-side-bar|class="neutron boron-triangle"/);}
});
test('B11 inherits B10 unchanged and adds two undirected top-to-bottom braces',()=>{
 const recipe=JSON.parse(JSON.stringify(api.drawingRecipe('B11')));assert.equal(recipe.extends,'B10');assert.equal(recipe.reflectBaseX,true);assert.deepEqual(recipe.viewBox,JSON.parse(JSON.stringify(api.drawingRecipe('B10').viewBox)));assert.equal(recipe.addEdges.length,7);assert.equal(api.fixtures().B11.N,6);
 for(const standalone of [false,true]){const svg=api.renderSVG(api.fixtures().B11,{standalone}),base=api.renderSVG(api.fixtures().B10,{standalone});assert.match(svg,/data-drawing-base="B10"/);const bars=[...svg.matchAll(/<path class="neutron lithium-side-bar" data-side="([^"]+)" d="([^"]+)"[^>]*>/g)];assert.deepEqual(bars.map(m=>m.slice(1)),[['left','M-50 -16 L-50 184'],['right','M50 -16 L50 184']]);for(const b of bars)assert.doesNotMatch(b[0],/marker-|data-flow/);const geometry=s=>[...s.matchAll(/<path class="neutron (?!lithium-side-bar)[^"]+"[^>]* d="([^"]+)"/g)].map(m=>m[1]);assert.deepEqual(geometry(svg),geometry(base));assert.equal((svg.match(/class="mid-arrow"/g)||[]).length,13);}
});
test('C12 is B10 plus a bottom triangle with red right and blue left, without side bars',()=>{
 const recipe=JSON.parse(JSON.stringify(api.drawingRecipe('C12')));assert.equal(recipe.extends,'B10');assert.equal(recipe.reflectBaseX,true);assert.equal(recipe.addEdges.length,7);assert.equal(api.fixtures().C12.Z,6);assert.equal(api.fixtures().C12.N,6);
 for(const standalone of [false,true]){const svg=api.renderSVG(api.fixtures().C12,{standalone});assert.match(svg,/data-drawing-base="B10"/);assert.match(svg,/data-definition="C12"/);assert.match(svg,/data-edge="bottom-red" style="stroke:#c64b46" d="M50 184 L0 234"/);assert.match(svg,/data-edge="bottom-blue" style="stroke:#2878c8" d="M0 234 L-50 184"/);assert.match(svg,/data-flow="down" data-midpoint="25 209"/);assert.match(svg,/data-flow="up" data-midpoint="-25 209"/);assert.equal((svg.match(/class="neutron lithium-base"/g)||[]).length,1);assert.equal((svg.match(/class="mid-arrow"/g)||[]).length,15);assert.doesNotMatch(svg,/lithium-side-bar|class="neutron carbon-bottom-square"/);}
});
test('C13 adds the B11-style braces to C12 without changing its directed paths',()=>{
 const r=JSON.parse(JSON.stringify(api.drawingRecipe('C13'))),base=JSON.parse(JSON.stringify(api.drawingRecipe('C12'))),boron=JSON.parse(JSON.stringify(api.drawingRecipe('B11')));assert.equal(r.extends,'C12');assert.deepEqual(r.viewBox,base.viewBox);assert.deepEqual(r.addEdges.slice(-2),boron.addEdges.slice(-2));assert.equal(api.fixtures().C13.Z,6);assert.equal(api.fixtures().C13.N,7);
 for(const standalone of [false,true]){const svg=api.renderSVG(api.fixtures().C13,{standalone}),parent=api.renderSVG(api.fixtures().C12,{standalone});assert.match(svg,/data-drawing-base="C12"/);assert.match(svg,/data-definition="C13"/);assert.equal((svg.match(/class="neutron lithium-side-bar"/g)||[]).length,2);const directed=s=>[...s.matchAll(/<path class="neutron (?!lithium-side-bar)[^"]+"[^>]* d="([^"]+)"/g)].map(m=>m[1]);assert.deepEqual(directed(svg),directed(parent));assert.equal((svg.match(/class="mid-arrow"/g)||[]).length,15);}
});
test('N14 extends C12 with an attached red-right triangle and a leftward green base',()=>{
 const r=JSON.parse(JSON.stringify(api.drawingRecipe('N14')));assert.equal(r.extends,'C12');assert.equal(r.addEdges.length,10);assert.equal(api.fixtures().N14.Z,7);assert.equal(api.fixtures().N14.N,7);
 for(const standalone of [false,true]){const svg=api.renderSVG(api.fixtures().N14,{standalone});assert.match(svg,/data-drawing-base="C12"/);assert.match(svg,/data-definition="N14"/);assert.match(svg,/data-edge="nitrogen-red" style="stroke:#c64b46" d="M0 234 L50 284"/);assert.match(svg,/data-edge="nitrogen-blue" style="stroke:#2878c8" d="M-50 284 L0 234"/);assert.match(svg,/data-edge="nitrogen-green" d="M50 284 L-50 284"/);assert.equal((svg.match(/class="mid-arrow"/g)||[]).length,18);assert.doesNotMatch(svg,/lithium-side-bar/);}
});
test('N15 inherits N14 and adds undirected braces from the top green bar to the lowest one',()=>{
 const r=JSON.parse(JSON.stringify(api.drawingRecipe('N15'))),parent=JSON.parse(JSON.stringify(api.drawingRecipe('N14')));assert.equal(r.extends,'N14');assert.deepEqual(r.viewBox,parent.viewBox);assert.equal(api.fixtures().N15.N,8);
 for(const standalone of [false,true]){const svg=api.renderSVG(api.fixtures().N15,{standalone}),base=api.renderSVG(api.fixtures().N14,{standalone});assert.match(svg,/data-drawing-base="N14"/);const bars=[...svg.matchAll(/<path class="neutron lithium-side-bar" data-side="([^"]+)" d="([^"]+)"[^>]*>/g)];assert.deepEqual(bars.map(m=>m.slice(1)),[['left','M-50 -16 L-50 284'],['right','M50 -16 L50 284']]);for(const b of bars)assert.doesNotMatch(b[0],/marker-|data-flow/);const directed=s=>[...s.matchAll(/<path class="neutron (?!lithium-side-bar)[^"]+"[^>]* d="([^"]+)"/g)].map(m=>m[1]);assert.deepEqual(directed(svg),directed(base));assert.equal((svg.match(/class="mid-arrow"/g)||[]).length,18);}
});
test('O16 completes the N14 bottom triangle into a square without altering inherited edges',()=>{
 const r=JSON.parse(JSON.stringify(api.drawingRecipe('O16'))),parent=JSON.parse(JSON.stringify(api.drawingRecipe('N14')));assert.equal(r.extends,'N14');assert.deepEqual(r.addEdges.slice(0,-2),parent.addEdges);assert.deepEqual(r.viewBox,[-86,-86,172,450]);assert.equal(api.fixtures().O16.Z,8);assert.equal(api.fixtures().O16.N,8);
 for(const standalone of [false,true]){const svg=api.renderSVG(api.fixtures().O16,{standalone});assert.match(svg,/data-drawing-base="N14"/);assert.match(svg,/data-definition="O16"/);assert.match(svg,/data-edge="oxygen-red" style="stroke:#c64b46" d="M0 334 L50 284"/);assert.match(svg,/data-edge="oxygen-blue" style="stroke:#2878c8" d="M-50 284 L0 334"/);assert.match(svg,/data-edge="nitrogen-green" d="M50 284 L-50 284"/);assert.equal((svg.match(/class="mid-arrow"/g)||[]).length,20);assert.doesNotMatch(svg,/lithium-side-bar|oxygen-left-triangle/);}
});
test('O17 inherits O16 with two undirected top-to-bottom green bars',()=>{
 const r=JSON.parse(JSON.stringify(api.drawingRecipe('O17'))),base=JSON.parse(JSON.stringify(api.drawingRecipe('O16')));assert.equal(r.extends,'O16');assert.deepEqual(r.viewBox,base.viewBox);assert.deepEqual(r.addEdges.slice(0,-2),base.addEdges);assert.equal(api.fixtures().O17.Z,8);assert.equal(api.fixtures().O17.N,9);
 for(const standalone of [false,true]){const svg=api.renderSVG(api.fixtures().O17,{standalone});assert.match(svg,/data-drawing-base="O16"/);assert.match(svg,/data-definition="O17"/);const bars=[...svg.matchAll(/<path class="neutron lithium-side-bar" data-side="([^"]+)" d="([^"]+)"[^>]*>/g)];assert.deepEqual(bars.map(m=>m.slice(1)),[['left','M-50 -16 L-50 284'],['right','M50 -16 L50 284']]);for(const bar of bars)assert.doesNotMatch(bar[0],/marker-|data-flow/);assert.equal((svg.match(/class="mid-arrow"/g)||[]).length,20);const directed=s=>[...s.matchAll(/<path class="neutron (?!lithium-side-bar)[^"]+"[^>]* d="([^"]+)"/g)].map(m=>m[1]);assert.deepEqual(directed(svg),directed(api.renderSVG(api.fixtures().O16,{standalone})));}
});
test('O18 replaces the long O17 bars with overlapping pairs spanning crossbars 1–3 and 2–4',()=>{
 const r=JSON.parse(JSON.stringify(api.drawingRecipe('O18'))),base=JSON.parse(JSON.stringify(api.drawingRecipe('O16')));assert.equal(r.extends,'O16');assert.deepEqual(r.addEdges.slice(0,-4),base.addEdges);assert.deepEqual(r.viewBox,base.viewBox);assert.equal(api.fixtures().O18.Z,8);assert.equal(api.fixtures().O18.N,10);
 for(const standalone of [false,true]){const svg=api.renderSVG(api.fixtures().O18,{standalone});assert.match(svg,/data-drawing-base="O16"/);assert.match(svg,/data-definition="O18"/);const bars=[...svg.matchAll(/<path class="neutron lithium-side-bar" data-side="([^"]+)" d="([^"]+)"[^>]*>/g)];assert.deepEqual(bars.map(m=>m.slice(1)),[['upper-left','M-50 -16 L-50 184'],['upper-right','M50 -16 L50 184'],['lower-left','M-50 84 L-60 84 L-60 284 L-50 284'],['lower-right','M50 84 L60 84 L60 284 L50 284']]);for(const bar of bars)assert.doesNotMatch(bar[0],/marker-|data-flow/);assert.equal((svg.match(/class="mid-arrow"/g)||[]).length,20);const directed=s=>[...s.matchAll(/<path class="neutron (?!lithium-side-bar)[^"]+"[^>]* d="([^"]+)"/g)].map(m=>m[1]);assert.deepEqual(directed(svg),directed(api.renderSVG(api.fixtures().O16,{standalone})));}
});
test('F19 adds a bottom triangle to O18 and Ne20 completes it, retaining both brace pairs',()=>{
 for(const [id,parent,count,viewBox,edges] of [
  ['F19','O18',23,[-86,-86,172,500],[['fluorine-red','M0 334 L-50 384'],['fluorine-blue','M50 384 L0 334'],['fluorine-green','M-50 384 L50 384']]],
  ['Ne20','F19',25,[-136,-86,272,350],[['neon-red','M50 84 L100 134'],['neon-blue','M100 134 L50 184']]]
 ]){const r=JSON.parse(JSON.stringify(api.drawingRecipe(id))),base=JSON.parse(JSON.stringify(api.drawingRecipe(parent)));assert.equal(r.extends,parent);assert.deepEqual(r.viewBox,viewBox);assert.deepEqual(r.addEdges.slice(0,-edges.length),base.addEdges.map(e=>e.id.startsWith('lower-')?{...e,from:[e.from[0],184],via:[],to:[e.from[0],384]}:e));assert.equal(api.fixtures()[id].Z,id==='F19'?9:10);assert.equal(api.fixtures()[id].N,10);
  for(const standalone of [false,true]){const svg=api.renderSVG(api.fixtures()[id],{standalone});assert(svg.includes(`data-drawing-base="${parent}"`));assert(svg.includes(`data-definition="${id}"`));assert.equal((svg.match(/class="mid-arrow"/g)||[]).length,count);assert.equal((svg.match(/class="neutron lithium-side-bar"/g)||[]).length,id==='Ne20'?0:4);for(const [edge,d] of edges){const path=[...svg.matchAll(/<path class="neutron recipe-edge" data-edge="([^"]+)"[^>]* d="([^"]+)"/g)].find(m=>m[1]===edge);assert.equal(path?.[2],d);}}
 }
});
test('Na23 adds a red-right bottom triangle to Ne20 and retains its two brace pairs',()=>{
 const r=JSON.parse(JSON.stringify(api.drawingRecipe('Na23'))),base=JSON.parse(JSON.stringify(api.drawingRecipe('Ne20')));assert.equal(r.extends,'Ne20');assert.deepEqual(r.addEdges.slice(0,-3),base.addEdges.map(e=>e.id.startsWith('lower-')?{...e,from:[e.from[0],184],via:[],to:[e.from[0],484]}:e));assert.deepEqual(r.viewBox,[-86,-86,172,600]);assert.equal(api.fixtures().Na23.Z,11);assert.equal(api.fixtures().Na23.N,12);
 for(const standalone of [false,true]){const svg=api.renderSVG(api.fixtures().Na23,{standalone});assert.match(svg,/data-drawing-base="Ne20"/);assert.match(svg,/data-definition="Na23"/);assert.match(svg,/data-edge="sodium-red" style="stroke:#c64b46" d="M0 434 L50 484"/);assert.match(svg,/data-edge="sodium-blue" style="stroke:#2878c8" d="M-50 484 L0 434"/);assert.match(svg,/data-edge="sodium-green" d="M50 484 L-50 484"/);assert.equal((svg.match(/class="mid-arrow"/g)||[]).length,28);assert.equal((svg.match(/class="neutron lithium-side-bar"/g)||[]).length,4);}
});
test('second wrapper reaches the lowest green crossbar, retaining F19 endpoints for the Ne20 cap',()=>{
 for(const [id,y] of [['F19',384],['Na23',484]])for(const standalone of [false,true]){const svg=api.renderSVG(api.fixtures()[id],{standalone}),r=JSON.parse(JSON.stringify(api.drawingRecipe(id)));for(const [side,sign] of [['left',-1],['right',1]]){const edge=r.addEdges.find(e=>e.id===`lower-${side}`);const start=184;assert.deepEqual(edge.from,[sign*50,start]);const x=sign*50;assert.deepEqual(edge.to,[x,y]);const d=`M${x} ${start} L${x} ${y}`;assert(svg.includes(`data-side="lower-${side}" d="${d}"`));}assert.equal((svg.match(/class="neutron lithium-side-bar"/g)||[]).length,4);}
});
test('Ne20 hides all wrapper neutrons without removing its directed green bars or changing Na23',()=>{
 for(const standalone of [false,true]){const svg=api.renderSVG(api.fixtures().Ne20,{standalone});assert.doesNotMatch(svg,/lithium-side-bar/);assert.equal((svg.match(/class="mid-arrow"/g)||[]).length,25);for(const id of ['upper-green','nitrogen-green','fluorine-green'])assert(svg.includes(`data-edge="${id}"`));assert.equal((api.renderSVG(api.fixtures().Na23,{standalone}).match(/class="neutron lithium-side-bar"/g)||[]).length,4);}
});
test('Ne20 retains the moved right square and places the fourth diamond to the left',()=>{
 const moved=[['fluorine-red','M0 134 L50 184'],['fluorine-blue','M50 84 L0 134'],['fluorine-green','M50 184 L50 84'],['neon-red','M50 84 L100 134'],['neon-blue','M100 134 L50 184']];
 for(const standalone of [false,true]){const svg=api.renderSVG(api.fixtures().Ne20,{standalone}),edges=[...svg.matchAll(/<path class="neutron recipe-edge" data-edge="([^"]+)"[^>]* d="([^"]+)"/g)].map(m=>m.slice(1));assert.deepEqual(edges.filter(([id])=>moved.some(([key])=>id===key)),moved);assert.match(svg,/viewBox="-136 -86 272 350"/);const left=[['nitrogen-red','M-100 134 L-50 184'],['nitrogen-blue','M-50 84 L-100 134'],['nitrogen-green','M-50 184 L-50 84'],['oxygen-red','M0 134 L-50 184'],['oxygen-blue','M-50 84 L0 134']];assert.match(svg,/data-edge="oxygen-red" style="stroke:#c64b46"/);assert.match(svg,/data-edge="oxygen-blue" style="stroke:#c64b46"/);assert.match(svg,/class="shell2-top-orientation" transform="matrix\(0 -1 -1 0 84 84\)"/);assert.match(svg,/class="shell2-bottom-orientation" transform="matrix\(0 -1 1 0 -184 184\)"/);assert.deepEqual(edges.filter(([id])=>left.some(([key])=>id===key)),left);assert.match(api.renderSVG(api.fixtures().Na23,{standalone}),/data-edge="fluorine-red" style="stroke:#c64b46" d="M0 334 L-50 384"/);}
});
test('Ne20 preserves its current authored color overrides without changing Na23',()=>{
 for(const standalone of [false,true]){const svg=api.renderSVG(api.fixtures().Ne20,{standalone});for(const [id,color] of [['nitrogen-red','#2878c8'],['nitrogen-blue','#2878c8'],['neon-red','#2878c8'],['neon-blue','#c64b46'],['fluorine-red','#c64b46'],['fluorine-blue','#2878c8'],['oxygen-red','#c64b46'],['oxygen-blue','#c64b46']])assert(svg.includes(`data-edge="${id}" style="stroke:${color}"`));const sodium=api.renderSVG(api.fixtures().Na23,{standalone});assert(sodium.includes('data-edge="nitrogen-red" style="stroke:#c64b46"'));assert(sodium.includes('data-edge="neon-blue" style="stroke:#2878c8"'));}
});
test('other isotopes retain their original green lines',()=>{for(const id of ['He4','Ca46'])assert.doesNotMatch(api.renderSVG(api.fixtures()[id]),/stroke:#2878c8/);});
