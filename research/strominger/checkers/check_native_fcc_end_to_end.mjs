// One actual native packet, independently constructed target, and source esd7 IDs.
// No new operation schedule, central duality, coefficient encoder or particle rule.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {createWindowConstruction,windowProtocol} from '../demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {applyPhasePermutation,activePhaseSlots} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const censusPath='research/voevodsky/results/esd7_explicit_analytical_census.json';
const flagsPath='research/strominger/results/esd7-seven-stage-handoff.json';
const census=JSON.parse(await fs.readFile(path.join(root,censusPath),'utf8'));
const flags=JSON.parse(await fs.readFile(path.join(root,flagsPath),'utf8'));
const key=ps=>ps.map(p=>p.join(',')).sort().join('|');
const points=Object.fromEntries(census.vertices.map(v=>[v.id,v.barycentric]));
const cellIds=new Map(census.vertices.map(v=>[key([v.barycentric]),v.id]));
for(const kind of ['edges','triangles','tetrahedra'])for(const c of census[kind])cellIds.set(key(c.vertices.map(v=>points[v])),c.id);
const embed=p=>p.map(x=>2-x); // Sum-one native FCC lattice -> sum-seven census lattice.
const nativePoint=s=>s.split(',').map(Number);
const embedKey=s=>embed(nativePoint(s));
const fcc=x=>[x[0]+x[1],x[0]+x[2],x[1]+x[2]];
const checkNames=[];
function check(name,f){f();checkNames.push(name);}
const censusDigest=createHash('sha256').update(await fs.readFile(path.join(root,censusPath))).digest('hex');
check('the central flag receipt refers to the live census',()=>assert.equal(flags.source_sha256,censusDigest));
const rules=new GenerativeAssemblyRules();
const initial=[[2,1],[3,-2],[5,3],[7,-4],[11,5]];
const packets=[rules.root],ops=[],values=[structuredClone(initial)];
for(const kind of ['PN','NE']){
 const candidates=rules.outgoing(packets.at(-1)).map(i=>rules.operations[i]).filter(o=>o.kind===kind);
 assert.equal(candidates.length,1);const op=candidates[0];
 check(`${kind}: native transfer validates with all coefficient coordinates`,()=>assert(rules.validateTransfer(op)));
 ops.push(op);packets.push(op.target);values.push(applyPhasePermutation(values.at(-1),op.permutation));
}
const charts=packets.map(id=>rules.charts[rules.packets[id].chart]);
const nativeCells=charts.map(c=>rules.geometry.cells[c.cell]);
const sourceIds=nativeCells.map(c=>cellIds.get(key(c.vertices.map(embedKey))));
const faceIds=ops.map(o=>cellIds.get(key(o.face.map(embedKey))));
check('native FCC cells and shared faces bind actual esd7 IDs',()=>{
 assert.deepEqual(sourceIds,['T184','T242','T256']);assert.deepEqual(faceIds,['F538','F569']);
});
check('the affine embedding preserves all retained-reference displacement norms',()=>{
 const ps=[...new Set(charts.flatMap(c=>Object.values(c.aliases)))].map(nativePoint);
 for(const a of ps)for(const b of ps){
  const squared=(a,b)=>a.reduce((s,x,i)=>s+(x-b[i])**2,0);
  assert.equal(squared(a,b),squared(fcc(embed(a)),fcc(embed(b))));
 }
});
// Independent geometry/identity constructor: no calls to GenerativeAssemblyRules.
const independent=createWindowConstruction({identity:{id:'native-fcc-binding-fixture'}});
const snapshots=[independent.snapshot(),independent.step(),independent.step()];
check('separate window constructor reproduces all three cells and marked contexts',()=>{
 for(let i=0;i<3;i++){
  const snap=snapshots[i],body=snap.items.at(-1);
  assert.equal(body.species,charts[i].species);
  assert.equal(key(body.vertices),key(nativeCells[i].vertices.map(nativePoint)));
  for(const [mark,p] of Object.entries(snap.bindings))assert.deepEqual(p,nativePoint(charts[i].aliases[mark]));
 }
 assert.equal(snapshots[2].status,'complete');assert.equal(snapshots[2].exit.identity.id,'native-fcc-binding-fixture');
});
check('independent native reference swaps give the full target coefficients',()=>{
 // Reference contract: PN exchanges slots0/3; NE exchanges slots1/4.
 assert.deepEqual(values[1],[initial[3],initial[1],initial[2],initial[0],initial[4]]);
 assert.deepEqual(values[2],[initial[3],initial[4],initial[2],initial[0],initial[1]]);
});
const electronReadout=activePhaseSlots.electron.map(i=>values[2][i]);
check('electron active readout matches the independently composed reference law',()=>assert.deepEqual(electronReadout,[initial[0],initial[2],initial[1]]));
check('inverse replay recovers every initial complex coefficient',()=>{
 let back=values[2];for(const op of [...ops].reverse())back=applyPhasePermutation(back,op.permutation,-1);
 assert.deepEqual(back,initial);
});
const a=charts[0].aliases;
const pWindow=windowProtocol.find(p=>p.species==='proton').window;
const nWindow=windowProtocol.find(p=>p.species==='neutron').window;
const eWindow=windowProtocol.find(p=>p.species==='electron').window;
const overlap=nWindow.filter(m=>eWindow.includes(m));
const markViews=[pWindow.slice(0,1),pWindow.slice(0,2),pWindow,
 windowProtocol.find(p=>p.species==='proton').nodes,nWindow,overlap,eWindow.slice(0,1)];
const sevenIds=markViews.map(ms=>cellIds.get(key(ms.map(m=>embedKey(a[m])))));
const matchingFlag=flags.central_flag_bridges.find(b=>JSON.stringify(b.seven_presentations)===JSON.stringify(sevenIds));
const sameAscent=flags.central_flag_bridges.find(b=>JSON.stringify(b.seven_presentations.slice(0,4))===JSON.stringify(sevenIds.slice(0,4)));
check('native seven views are actual consecutive incidences',()=>{
 assert.deepEqual(sevenIds,['V051','E270','F403','T184','F538','E389','V077']);
 for(let i=0;i<6;i++){
  const [small,big]=markViews[i].length<markViews[i+1].length?[markViews[i],markViews[i+1]]:[markViews[i+1],markViews[i]];
  assert(small.every(m=>big.includes(m)));
 }
});
check('native seven views do not equal the quarter-rotated central bridge',()=>{
 assert.equal(matchingFlag,undefined);assert(sameAscent);
 assert.deepEqual(sameAscent.seven_presentations.slice(0,5),sevenIds.slice(0,5));
 assert.deepEqual(sameAscent.seven_presentations.slice(5),['E368','V072']);
});
const inputOrder=markViews[3];
const outgoingFlag=[markViews[6],markViews[5],markViews[4],markViews[3]];
const outputOrder=outgoingFlag.map((ms,i)=>ms.find(m=>i===0||!outgoingFlag[i-1].includes(m)));
const requiredFrame=inputOrder.map(m=>inputOrder.indexOf(outputOrder[inputOrder.indexOf(m)]));
check('the literal native flag comparison requires reversal of order two not a quarter-cycle',()=>{
 assert.deepEqual(requiredFrame,[3,2,1,0]);
 assert.deepEqual(requiredFrame.map(i=>requiredFrame[i]),[0,1,2,3]);
 assert.notDeepEqual(requiredFrame,[0,1,2,3]);
});
check('the two native transfers preserve shared occurrence identities',()=>{
 for(const op of ops){const from=rules.charts[rules.packets[op.source].chart],to=rules.charts[rules.packets[op.target].chart];
  for(const m of ['C0','M0','C1','M1','C2'])assert.equal(from.aliases[m],to.aliases[m]);
 }
});
check('seven presentations do not create seven native time steps',()=>{
 assert.equal(ops.length,2);assert(packets.every(id=>rules.packets[id].origin===0));assert(ops.every(o=>o.phaseDelta===0));
});
// The full E carrier/center is distinct from the E-leading mark in the central flag.
const nativeExit=snapshots[2].exit.point,embeddedExit=embed(nativeExit),dualVertex=[7/4,7/4,7/4,7/4];
check('native electron exit is not the proposed central dual vertex',()=>{
 assert.deepEqual(embeddedExit,[5/2,7/4,3/2,5/4]);assert.notDeepEqual(embeddedExit,dualVertex);
 assert.equal(embeddedExit.reduce((s,x,i)=>s+(x-dualVertex[i])**2,0),7/8);
});
check('final central flag vertex is an E window mark not its full carrier or exit center',()=>{
 assert.equal(eWindow[0],'M1');assert.equal(sevenIds.at(-1),'V077');
 assert.notDeepEqual(embedKey(charts[2].aliases.M1),embeddedExit);assert.notEqual(sourceIds[2],sevenIds.at(-1));
});
check('even the initial native packet retains a context outside central T184',()=>{
 const centralSet=new Set(nativeCells[0].vertices);assert(!centralSet.has(a.C2));
});
check('discarding hidden coefficients can pass the E readout while failing full recovery',()=>{
 let erased=initial.map((v,i)=>i<3?v:[0,0]);for(const op of ops)erased=applyPhasePermutation(erased,op.permutation);
 assert.deepEqual(activePhaseSlots.electron.map(i=>erased[i]),electronReadout);
 assert.notDeepEqual(erased,values[2]);
});
const sourcePaths=[censusPath,flagsPath,'research/nima/generative-phase-assembly.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs',
 'research/strominger/checkers/check_native_fcc_end_to_end.mjs'];
const sourceSha256=Object.fromEntries(await Promise.all(sourcePaths.map(async p=>[p,createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex')])));
const report={status:'passed',checkCount:checkNames.length,checks:checkNames,sourceSha256,
 fixture:{embedding:'native sum-one x -> (2,2,2,2)-x; FCC chart (a+b,a+c,b+c)',initialCoefficients:initial,
  packets:packets.map((id,i)=>({packet:rules.packets[id],chart:charts[i],esd7Cell:sourceIds[i],coefficients:values[i]})),
  operations:ops.map((op,i)=>({...op,esd7SharedFace:faceIds[i]})),
  sevenViews:sevenIds.map((id,i)=>({id,marks:markViews[i],role:['P first mark','P prefix','P active window','P carrier/context','N active window','fixed N/E overlap','E first mark'][i]})),
  quarterRotatedBridge:sameAscent.seven_presentations,requiredNativeFlagPermutation:requiredFrame,
  electronReadout,independentExit:embeddedExit,centralDualVertex:dualVertex},
 disposition:{nativeReplay:'P->N->E reproduced with retained coefficients and independently constructed target geometry',
  sevenPresentations:'Native prefix/context/window/overlap views form a valid source incidence path but disagree with the quarter-rotated bridge on its last two views. Their flag comparison is order two, not four.',
  centralDualization:'Not required by this native replay; identifying its dual vertex with the native E exit is false for this fixture',
  globalEvolution:'Not established. Two native transfers, no prescribed seven-step or28-step clock.'},
 scope:'One fixed native seed and selected PN,NE word; not a proof over all preparations. Independent target geometry uses a separate implementation of the same declared native window contract; coefficient target uses its declared swaps, not an independently derived physical law. No arbitrary coefficient-to-simplex encoder is introduced.'};
const dest=path.join(root,'research/strominger/results/native-fcc-end-to-end.json');
await fs.mkdir(path.dirname(dest),{recursive:true});await fs.writeFile(dest,JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:report.status,checks:report.checkCount,cells:sourceIds,faces:faceIds,sevenViews:sevenIds,centralDualityRequired:false,result:dest}));
