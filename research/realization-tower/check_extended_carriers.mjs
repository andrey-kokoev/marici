import fs from 'node:fs/promises';
import {createWindowConstruction} from '../strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {makeLatticeItem,itemKey} from '../strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
import assert from 'node:assert/strict';
const receipt=JSON.parse(await fs.readFile(new URL('./results/extended-probe-diagonal-v1.json',import.meta.url),'utf8'));
const points=receipt.extended.find(r=>r.depth_each_side===2).shortest_walk_union;
const key=p=>p.join(','),allowed=new Set(points.map(key));
const toSource=([x,y,z])=>[1-(x+y+z)/2,(x+y-z)/2,(x+z-y)/2,(y+z-x)/2];
const toFCC=([a,b,c,d])=>[b+c,b+d,c+d];
const permutations=a=>a.length?a.flatMap((v,i)=>permutations(a.filter((_,j)=>j!==i)).map(rest=>[v,...rest])):[[]];
const seeds=[];
for(let x=-1;x<=4;x++)for(let y=-3;y<=2;y++)for(let z=-3;z<=2;z++){
 const vertices=[];for(let a=0;a<=1;a++)for(let b=0;b<=1;b++)for(let c=0;c<=1;c++){const p=[x+a,y+b,z+c];if((p[0]+p[1]+p[2])%2===0)vertices.push(p);}
 if(!vertices.every(p=>allowed.has(key(p))))continue;
 const source=vertices.map(toSource),center=source[0].map((_,i)=>source.reduce((s,p)=>s+p[i],0)/4);
 const candidates=[];for(const inverted of [false,true]){const origin=center.map(v=>v+(inverted?.25:-.25));if(origin.every(Number.isInteger)){const seed=makeLatticeItem('tetrahedron',origin,inverted);if(seed.key===itemKey(source))candidates.push(seed);}}
 assert.equal(candidates.length,1);seeds.push(candidates[0]);
}
assert.equal(seeds.length,8);
const marks=['C0','M0','C1','M1'],cases=[];
for(const [seedIndex,seed] of seeds.entries())for(const order of permutations([0,1,2,3])){
 const bindings=Object.fromEntries(marks.map((mark,i)=>[mark,seed.vertices[order[i]]]));
 const model=createWindowConstruction({seed,bindings});model.step();const state=model.step();
 const bodies=state.items.map(item=>({species:item.species,vertices:item.vertices.map(toFCC),sourceKey:item.key}));
 const inside=bodies.every(body=>body.vertices.every(p=>allowed.has(key(p))));
 const entry=bodies[0].vertices.some(p=>key(p)===key(receipt.entry));
 const exit=state.status==='complete'&&bodies.at(-1).vertices.some(p=>key(p)===key(receipt.new_exit));
 cases.push({seedIndex,order,status:state.status,inside,entryIncidence:entry,exitIncidence:exit,spansPoles:inside&&entry&&exit&&state.status==='complete',bodies,
  events:state.events,reason:state.reason});
}
assert.equal(cases.length,192);
const completed=cases.filter(c=>c.status==='complete');
const inside=completed.filter(c=>c.inside),spanning=cases.filter(c=>c.spansPoles);
const distinctInside=new Set(inside.map(c=>c.bodies.map(b=>b.sourceKey).join(' -> ')));
const report={status:'pass',scope:'Existing marked window constructor on all 8 regular seed tetrahedra and all 24 seed markings in the four-step point-probe interval. Fixed owning octahedral subdivision and phase law retained.',
 inputRegionVertices:points.length,seeds:seeds.length,markingsPerSeed:24,cases:cases.length,
 completed:completed.length,contained:inside.length,distinctContainedChains:distinctInside.size,spanningPoles:spanning.length,
 endpointInterpretation:'P body contains entry pole, E body contains exit pole; weaker than the owning centre-entry/centre-exit protocol, not its identification.',
 trials:cases};
await fs.writeFile(new URL('./results/extended-carrier-search-v1.json',import.meta.url),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,trials:undefined}));
