import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import {createDeuteriumTunnel,transportWindowCoefficients,transportCarrierCoefficients,referenceCarrierMarks,transportWindowMode,windowModeCoefficients} from '../demos/particle-overlap-tetrahedron/deuterium-tunnel-model.mjs';
import {windowProtocol} from '../demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {makeLatticeItem,itemKey} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {lattice} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
const norm=c=>c.reduce((sum,[re,im])=>sum+re*re+im*im,0);
const near=(a,b)=>a.forEach((z,i)=>z.forEach((v,j)=>assert.ok(Math.abs(v-b[i][j])<1e-12)));
function exercise(options={}){
 const model=createDeuteriumTunnel(options),seed=model.snapshot(),input=seed.tunnel.coefficients;
 assert.equal(seed.tunnel.coverage.built,1);assert.equal(seed.tunnel.coverage.complete,false);assert.equal(seed.tunnel.frontier.terminal,false);
 assert.deepEqual(seed.tunnel.frontier.window,['M0','C1','M1']);assert.equal(model.pass(-1).moved,false);assert.equal(model.pass(1).moved,false);
 for(let i=1;i<=2;i++){
  const before=model.snapshot(),after=model.step();assert.equal(after.committed,true);assert.equal(after.items.length,before.items.length+1);assert.deepEqual(after.items.slice(0,-1),before.items);assert.deepEqual(after.items.at(-1).window,before.tunnel.frontier.window);
  assert.equal(after.identity,seed.identity);assert.equal(after.tunnel.identity,seed.identity);assert.ok(after.tunnel.fiberStates.every(s=>s.identity===seed.identity&&s.referenceCarrier.length===5));assert.equal(after.tunnel.position,i);
  assert.equal(after.tunnel.coverage.covered,i+1);assert.equal(after.tunnel.frontier.item,i);assert.deepEqual(after.tunnel.mode,after.mode);near(after.tunnel.coefficients,windowModeCoefficients(after.mode));
  if(i===1){assert.deepEqual(after.tunnel.frontier.window,['M1','C1','C2']);assert.equal(after.tunnel.coverage.complete,false);}
 }
 const end=model.snapshot(),geometry=structuredClone(end.items),history=[...end.history],bindings=structuredClone(end.bindings);
 assert.deepEqual(end.counts,{proton:1,neutron:1,electron:1});assert.equal(end.tunnel.coverage.complete,true);assert.equal(end.tunnel.frontier.terminal,true);assert.equal(end.tunnel.guideEdges.length,4);
 assert.equal(new Set(end.items.map(s=>s.key)).size,3);
 for(let i=0;i<end.events.length;i++){
  const face=end.events[i].face;for(const body of [end.items[i],end.items[i+1]])assert.ok(body.faces.some(f=>itemKey(f)===itemKey(face)));
  const [a,b]=end.tunnel.guideEdges.slice(i*2,i*2+2);assert.deepEqual(a[0],end.items[i].center);assert.deepEqual(a[1],b[0]);assert.deepEqual(b[1],end.items[i+1].center);
  assert.deepEqual(a[1],face[0].map((_,j)=>face.reduce((s,p)=>s+p[j],0)/3));
 }
 assert.equal(model.pass(1).moved,false);model.pass(-1);model.pass(-1);
 const entrance=model.snapshot();assert.equal(entrance.tunnel.position,0);assert.deepEqual(entrance.tunnel.coefficients,input);assert.deepEqual(entrance.tunnel.mode,seed.mode);assert.deepEqual(entrance.tunnel.referenceCarrier,seed.tunnel.referenceCarrier);
 assert.equal(model.pass(-1).moved,false);assert.equal(model.step().committed,false);assert.equal(model.snapshot().tunnel.position,0);
 const originalPayload=structuredClone(entrance.tunnel.coefficients);entrance.tunnel.coefficients[0][0]=999;assert.deepEqual(model.snapshot().tunnel.coefficients,originalPayload);
 for(let repeat=0;repeat<3;repeat++){
  model.pass(1);model.pass(1);assert.deepEqual(model.snapshot().tunnel.coefficients,end.tunnel.coefficients);
  model.pass(-1);model.pass(-1);const back=model.snapshot();
  assert.deepEqual(back.tunnel.coefficients,originalPayload);assert.deepEqual(back.tunnel.referenceCarrier,seed.tunnel.referenceCarrier);assert.deepEqual(back.tunnel.mode,seed.mode);assert.deepEqual(back.items,geometry);assert.deepEqual(back.bindings,bindings);assert.deepEqual(back.history,history);assert.equal(back.identity,seed.identity);
 }
 assert.throws(()=>model.pass(0));return end;
}
assert.throws(()=>windowModeCoefficients({branch:'unknown',phaseExponent:0}));
assert.throws(()=>windowModeCoefficients({branch:'positive',phaseExponent:NaN}));
assert.deepEqual(referenceCarrierMarks,['C0','M0','C1','M1','C2']);
const end=exercise();assert.deepEqual(end.mode,{branch:'negative',phaseExponent:0});
for(const event of end.events){
 const full=[[2,-3],[-.25,4],[0,1.75],[9,-7],[-5,6]],transported=transportCarrierCoefficients(full,event);
 assert.deepEqual(transportCarrierCoefficients(transported,event,-1),full);assert.equal(norm(transported),norm(full));
 const arbitrary=[[2,-3],[-.25,4],[0,1.75]],forward=transportWindowCoefficients(arbitrary,event);
 assert.deepEqual(transportWindowCoefficients(forward,event,-1),arbitrary);assert.equal(norm(forward),norm(arbitrary));
 for(const branch of ['common','positive','negative'])for(const phaseExponent of [0,1,2]){
  const mode={branch,phaseExponent},next=transportWindowMode(mode,event),c=windowModeCoefficients(mode);
  near(transportWindowCoefficients(c,event),windowModeCoefficients(next));assert.deepEqual(transportWindowMode(next,event,-1),mode);
 }
 const bad=structuredClone(event);bad.orderedFace.reverse();assert.throws(()=>transportWindowCoefficients(arbitrary,bad));
}
const permutations=a=>a.length?a.flatMap((x,i)=>permutations(a.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]],seed=makeLatticeItem('tetrahedron',[0,0,0,0]);
for(const permutation of permutations([0,1,2,3]))for(const branch of ['common','positive','negative']){
 exercise({branch,complementCoefficients:[[9,-7],[-5,6]],bindings:Object.fromEntries(windowProtocol[0].nodes.map((n,i)=>[n,seed.vertices[permutation[i]]]))});
}
// The default three carriers tile a closed oblique triangular prism: the
// upper triangle is a translate of the lower one, with no extra cap geometry.
const subtract=(a,b)=>a.slice(0,3).map((x,i)=>x-b[i]);
const determinant=(a,b,c)=>a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]);
const lower=['C0','M0','C1'].map(n=>end.bindings[n]),upper=['M1','C2','M2'].map(n=>end.bindings[n]),shift=upper[0].map((x,i)=>x-lower[0][i]);
lower.forEach((p,i)=>assert.deepEqual(p.map((x,j)=>x+shift[j]),upper[i]));
const prismVolume=Math.abs(determinant(subtract(lower[1],lower[0]),subtract(lower[2],lower[0]),shift.slice(0,3)))/2;
const sumVolume=end.items.reduce((sum,{vertices:[a,b,c,d]})=>sum+Math.abs(determinant(subtract(b,a),subtract(c,a),subtract(d,a)))/6,0);assert.ok(Math.abs(prismVolume-sumVolume)<1e-12);
const cells=lattice.cells.map(c=>itemKey(c.map(id=>lattice.nodes[id].address)));assert.ok(end.items.every(s=>cells.includes(s.key)));
const out='research/strominger/results/deuterium-tunnel';await mkdir(out,{recursive:true});
await writeFile(out+'/verification.json',JSON.stringify({status:'pass-local-deuterium-window-trial',counts:end.counts,cellIds:end.items.map(s=>cells.indexOf(s.key)),coverage:end.tunnel.coverage,initialMode:{branch:'positive',phaseExponent:0},terminalMode:end.mode,steps:end.events,guideEdges:end.tunnel.guideEdges,markings:24,modes:3,noConstructionRevisits:true,algebraicInverseForArbitraryComplexPayload:true,fullFiveSlotReferenceCarrierRetained:true,nonzeroComplementRoundTrips:true,M2HasNoInventedNativeCoefficient:true,roundTripPreservesGeometryBindingsHistoryIdentity:true,defaultPrismVolumeMatches:true,branchingTested:false,physicalInterRealizationTunnelingEstablished:false,scope:end.tunnel.scope},null,2)+'\n');
console.log('PASS deuterium tunnel trial: one-item prefixes, 3/3 local coverage, no construction revisits, algebraic bidirectional transport; 24 markings × 3 modes. Physical inter-realization tunneling remains conjectural.');
