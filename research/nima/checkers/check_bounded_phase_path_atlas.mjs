import assert from 'node:assert/strict';
import {readFile,readdir,mkdir,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
const root=fileURLToPath(new URL('../../../',import.meta.url));
const sourceDir='research/strominger/demos/particle-overlap-tetrahedron';
const output=path.join(root,'research/nima/results/bounded-phase-path-atlas');
const sha=bytes=>createHash('sha256').update(bytes).digest('hex');
async function snapshot(){
 const names=(await readdir(path.join(root,sourceDir))).filter(n=>n.endsWith('.mjs')).sort();
 return Object.fromEntries(await Promise.all(names.map(async n=>{const p=sourceDir+'/'+n;return [p,sha(await readFile(path.join(root,p)))];})));
}
const sources=await snapshot();
const {buildAtlas,checkCoefficientRecovery,traceWord,undo,nativeInverseIndices}=await import('../bounded-phase-path-atlas.mjs');
const {selectPhaseAssembly}=await import('../../strominger/demos/particle-overlap-tetrahedron/phase-assembly-model.mjs');
const maxTransitions=9,previousLimit=8;
const fixtures={helium3:[0,0,1,1,2,3,5,8,13,21],helium4:[0,0,1,1,3,4,10,16,36,64],lithium6:[0,0,0,1,0,3,1,11,7,43]};
const previousCounts={helium3:33,helium4:71,lithium6:23};
const models={};let coefficientCases=0,negativeControls=0;
for(const [name,expected] of Object.entries(fixtures)){
 const r=selectPhaseAssembly(name),atlas=buildAtlas(r,{maxTransitions});
 assert.equal(atlas.bound.maxTotalTransitions,maxTransitions);
 const previous=buildAtlas(r,{maxTransitions:previousLimit});
 assert.equal(previous.summary.paths,previousCounts[name]);
 assert.deepEqual(atlas.paths.filter(p=>p.length<=previousLimit),previous.paths,'Nine-transition extension changed an eight-transition path or inverse certificate');
 assert.deepEqual(atlas.summary.byLength,expected);
 assert.equal(atlas.summary.nativeReverseAdmitted,0);
 const requiredCells=[...new Set(r.charts.map(c=>c.cell))].sort((a,b)=>a-b);
 const exitPathCells=[...new Set(atlas.paths.flatMap(p=>p.trace.map(s=>r.charts[s.chart].cell)))].sort((a,b)=>a-b);
 assert.deepEqual(exitPathCells,requiredCells,'A selected carrier has no exit route within the bound');
 coefficientCases+=checkCoefficientRecovery(r,atlas);
 for(const p of atlas.paths){
  assert.equal(p.entryC.role,'C');assert.equal(p.exitC.role,'C');
  assert.equal(p.exitC.index,p.phaseAdvances+2);
  assert.equal(p.inverseSteps[0].nativeCandidates.length,0,'Terminal readout has no admitted native inverse');
  assert.deepEqual(p.inverseSteps.at(-1).to.history,[]);
  assert.equal(p.inverseSteps.at(-1).to.origin,0);
  for(const s of p.trace)assert.equal(s.history.length,p.trace.indexOf(s));
 }
 // Independent enumeration at every smaller cutoff preserves the corresponding records.
 for(let budget=0;budget<maxTransitions;budget++){
  const sub=buildAtlas(r,{maxTransitions:budget});
  assert.deepEqual(sub.summary.byLength,expected.slice(0,budget+1));
  assert.deepEqual(sub.paths.map(p=>p.id),atlas.paths.filter(p=>p.length<=budget).map(p=>p.id));
 }
 const shortest=[...atlas.paths].sort((a,b)=>a.length-b.length)[0],last=shortest.trace.at(-1);
 const state={chart:last.chart,origin:last.origin,permutation:last.permutation,history:last.history};
 for(const mutate of [s=>s.origin++,s=>s.history.pop(),s=>s.permutation.reverse(),s=>s.chart=r.root]){
  const bad=structuredClone(state);mutate(bad);
  assert.throws(()=>undo(r,bad,shortest.word.at(-1)));negativeControls++;
 }
 assert.throws(()=>traceWord(r,[...shortest.word,shortest.word[0]]));negativeControls++;
 for(const e of r.edges.filter(e=>e.phaseDelta))assert.equal(nativeInverseIndices(r,r.edges.indexOf(e)).length,0,'Positive phase advance is not its negative-origin inverse');
 const graph=atlas.CExitCapGraph;
 const capWalk=word=>{let q=graph.entry;for(const index of word){const options=graph.transitions.filter(e=>e.from===q&&e.sourceEdge===index);assert.equal(options.length,1);q=options[0].to;}return graph.states[q];};
 for(const s of graph.states){const actual=traceWord(r,s.representativeWord).at(-1);assert.equal(actual.chart,s.chart);assert.equal(actual.origin,s.origin);assert.deepEqual(actual.permutation,s.permutation);}
 for(const p of atlas.paths.filter(p=>p.withinC0ThroughC4)){const end=capWalk(p.word);assert.ok(graph.exits.includes(end.id));assert.deepEqual(end.permutation,p.trace.at(-1).permutation);}
 const pump=atlas.pumpingWitness;assert.ok(pump?.unboundedWordsWithinC0ThroughC4);
 assert.equal(capWalk(pump.loop).id,graph.entry);
 for(const n of [0,1,2,10]){
  const word=[...Array.from({length:n},()=>pump.loop).flat(),...pump.suffix],states=traceWord(r,word),end=states.at(-1);
  assert.equal(r.charts[end.chart].species,'electron');assert.equal(end.origin,shortest.phaseAdvances);
  assert.deepEqual(end.permutation,shortest.trace.at(-1).permutation);
  assert.equal(end.history.length,2*n+shortest.length);
  assert.equal(capWalk(word).id,capWalk(pump.suffix).id);
 }
 const broken=structuredClone(r);broken.edges[0].permutation=[0,1,2,3,4];
 assert.throws(()=>buildAtlas(broken));negativeControls++;
 assert.throws(()=>buildAtlas(r,{maxTransitions:-1}));negativeControls++;
 models[name]=atlas;
}
assert.deepEqual(await snapshot(),sources,'Owner sources changed during run: repeat with stable inputs');
const ownInputs=['research/nima/bounded-phase-path-atlas.mjs','research/nima/checkers/check_bounded_phase_path_atlas.mjs','research/nima/demos/bounded-phase-path-atlas.template.html'];
const ownHashes=Object.fromEntries(await Promise.all(ownInputs.map(async p=>[p,sha(await readFile(path.join(root,p))) ])));
const result={schema:'marici.nima.bounded-phase-path-atlas-suite.v1',status:'pass-bounded-native-path-enumeration-and-formal-recovery',
 summary:{totalPaths:Object.values(models).reduce((n,m)=>n+m.summary.paths,0),coefficientCases,negativeControls,
  nativeReverseAdmitted:0,sourceGraphs:3,maxTotalTransitions:maxTransitions,
  previousLimit:{maxTotalTransitions:previousLimit,pathsByModel:previousCounts,allPathRecordsPreserved:true}},
 conclusions:{allEnumeratedPathsHaveFormalInverseCertificates:true,everySelectedCarrierOnSomeBoundedExitPath:true,allNativePathsTraversableBothWays:false,
  phaseBoundAloneBoundsHistoryLength:false,sourceTransitionCMStageCostsEstablished:false,
  CEntryExitBoundaryIsDeclared:true,physicalReversibilityEstablished:false},
 sourceHashes:sources,checkerHashes:ownHashes,models};
await mkdir(output,{recursive:true});
await writeFile(path.join(output,'atlas.json'),JSON.stringify(result,null,2)+'\n');
const template=await readFile(path.join(root,ownInputs[2]),'utf8');
assert.equal(template.split('__ATLAS_JSON__').length,2);
await writeFile(path.join(output,'index.html'),template.replace('__ATLAS_JSON__',JSON.stringify(result).replaceAll('<','\\u003c')));
await writeFile(path.join(output,'verification.json'),JSON.stringify({schema:result.schema,status:result.status,summary:result.summary,conclusions:result.conclusions,
 models:Object.fromEntries(Object.entries(models).map(([n,a])=>[n,{...a.summary,pumpingWitness:a.pumpingWitness}])),
 sourceHashes:sources,checkerHashes:ownHashes},null,2)+'\n');
console.log(JSON.stringify({status:result.status,...result.summary,models:Object.fromEntries(Object.entries(models).map(([n,m])=>[n,m.summary]))},null,2));
