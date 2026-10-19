// Audit prerequisites for an untargeted formation trial; does not supply dynamics.
import assert from 'node:assert/strict';
import {readFile,readdir,mkdir,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {assembleComponents} from '../demos/particle-overlap-tetrahedron/simplex-components.mjs';
import {items,adjacency,available,reserved,witnessPairs} from '../demos/particle-overlap-tetrahedron/fiber-space-model.mjs';
import {lead208Bodies,lead208Chains} from '../demos/particle-overlap-tetrahedron/lead208-model.mjs';
import {createWindowConstruction,windowProtocol} from '../demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {makeLatticeItem} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';

const source=new URL('../demos/particle-overlap-tetrahedron/',import.meta.url);
const sourceHashes={};
for(const name of (await readdir(source)).filter(n=>n.endsWith('.mjs')).sort())sourceHashes[name]=createHash('sha256').update(await readFile(new URL(name,source))).digest('hex');
sourceHashes['../../checkers/check_pb208_formation_gate.mjs']=createHash('sha256').update(await readFile(new URL(import.meta.url))).digest('hex');
sourceHashes['../../../nima/generative-phase-assembly.mjs']=createHash('sha256').update(await readFile(new URL('../../nima/generative-phase-assembly.mjs',import.meta.url))).digest('hex');
// The broader native grammar must not be mistaken for the terminal UI packet.
const rules=new GenerativeAssemblyRules(),depth=new Map([[rules.root,0]]),queue=[rules.root],operationKinds={},speciesPackets={};
for(let qi=0;qi<queue.length;qi++){
  const id=queue[qi],species=rules.charts[rules.packets[id].chart].species;
  speciesPackets[species]=(speciesPackets[species]??0)+1;
  if(species==='electron')assert.equal(rules.outgoing(id).length,0);
  if(depth.get(id)===4)continue;
  for(const index of rules.outgoing(id)){
    const op=rules.operations[index];operationKinds[op.kind]=(operationKinds[op.kind]??0)+1;
    if(!depth.has(op.target)){depth.set(op.target,depth.get(id)+1);queue.push(op.target);}
  }
}
const nativeGrammar={maxDepth:4,packets:queue.length,speciesPackets,operationKinds,scope:'Bounded inventory of existing marked transitions, not a stochastic formation simulation or a global assembly certificate.'};
assert.ok(operationKinds['inverse-PN']>0&&operationKinds['NN-phase-advance']>0);
const assembly=assembleComponents();
const layers=assembly.layers.map((layer,index)=>({layer:index,items:layer.items.length,tetrahedra:layer.items.filter(i=>i.kind==='tetrahedron').length,octahedra:layer.items.filter(i=>i.kind==='octahedron').length}));
const inner=items.filter(i=>i.layer===2).map(i=>i.index),outer=items.filter(i=>i.layer===3).map(i=>i.index);
const outerSet=new Set(outer);
function matching(order,reverse=false){
  const paired=new Map();
  function augment(a,seen){
    const candidates=adjacency[a].filter(b=>outerSet.has(b));if(reverse)candidates.reverse();
    for(const b of candidates){if(seen.has(b))continue;seen.add(b);if(!paired.has(b)||augment(paired.get(b),seen)){paired.set(b,a);return true;}}
    return false;
  }
  for(const a of order)augment(a,new Set());
  return [...paired].map(([outer,inner])=>({inner,outer})).sort((a,b)=>a.inner-b.inner);
}
const forward=matching(inner),reversed=matching([...inner].reverse(),true);
assert.equal(forward.length,inner.length);assert.equal(reversed.length,inner.length);
assert.deepEqual(forward,witnessPairs);
const counts=Object.fromEntries(['proton','neutron','electron'].map(species=>[species,lead208Bodies.filter(b=>b.species===species).length]));
const derived={proton:outer.length-forward.length,neutron:forward.length+lead208Chains.length,electron:lead208Chains.length};
assert.equal(lead208Chains.length,available.size);assert.equal(reserved.size,forward.length);assert.deepEqual(counts,derived);
const sharedVertices=lead208Chains.map(chain=>{
  const incoming=new Set(chain.protonNeutronFace.map(p=>p.join(',')));
  return chain.neutronElectronFace.filter(p=>incoming.has(p.join(','))).length;
});
const faceIntersectionHistogram={};for(const count of sharedVertices)faceIntersectionHistogram[count]=(faceIntersectionHistogram[count]??0)+1;
const unbound=lead208Bodies.filter(b=>b.species==='proton'&&(b.shape.vertices.length!==4||b.components.length!==1));
const permutations=a=>a.length?a.flatMap((x,i)=>permutations(a.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];
const seed=makeLatticeItem('tetrahedron',[0,0,0,0]),runs=[];
for(const frame of permutations([0,1,2,3])){
  const bindings=Object.fromEntries(windowProtocol[0].nodes.map((name,i)=>[name,seed.vertices[frame[i]]]));
  const engine=createWindowConstruction({seed,bindings});
  let state=engine.snapshot(),steps=0;
  while(state.status==='ready'&&steps<10){state=engine.step();steps++;}
  assert.equal(state.status,'complete');assert.equal(steps,2);
  const terminal=engine.snapshot();
  for(let i=0;i<32;i++)assert.equal(engine.step().committed,false);
  assert.deepEqual(engine.snapshot().items,terminal.items);
  runs.push({frame,steps,status:state.status,species:state.items.map(i=>i.species),additionalCommits:0});
}
const resolutionTrials=[3,5,7,9,11].map(resolution=>{
  try{return {resolution,status:'supported',items:assembleComponents(resolution).items.length};}
  catch(error){return {resolution,status:'rejected',reason:error.message};}
});
assert.equal(resolutionTrials.filter(t=>t.status==='supported').length,1);
const report={schema:'marici.pb208-formation-gate.v1',status:'audit-passed-formation-gate-not-met',
  layers,counts,nativeGrammar,derivedCountRecipe:{outerItems:outer.length,matchedWitnesses:forward.length,protons:'outer - witnesses',neutrons:'witnesses + one connector per proton',electrons:'one endpoint per proton'},
  matching:{forwardSize:forward.length,reversedSize:reversed.length,sameAssignment:JSON.stringify(forward)===JSON.stringify(reversed),sameReservedSet:JSON.stringify(forward.map(p=>p.outer).sort((a,b)=>a-b))===JSON.stringify(reversed.map(p=>p.outer).sort((a,b)=>a-b))},
  legacyWindowCompatibility:{chains:lead208Chains.length,faceIntersectionHistogram,chainsSharingRequiredTwoVertices:sharedVertices.filter(n=>n===2).length,missingFourVertexProtonBindings:unbound.map(b=>b.id)},
  nativePacket:{seedMarkings:runs.length,runs,scope:'24 supplied seed markings on the fixed native subdivision; not formation trials or a global symmetry certificate.'},resolutionTrials,
  missingPrerequisites:['A target-independent reason for the four-layer resolution-7 envelope.','A justified global assembly evolution/selection on the available PN, inverse-PN, NN and reader moves; E is terminal in the reviewed grammars.','An admitted carrier interpretation for whole-octahedron protons and composite neutron bodies.','A specified evolution/selection and stability criterion, not address-order search.'],
  decision:'Do not run a Pb-208 formation simulation under these rules: the reviewed source supplies packing, a terminal local packet and a broader admissible-transition grammar, but not a justified autonomous formation/selection dynamics.',
  scope:'This is an audit of the current legacy Pb and native window implementations. It neither proves Pb-208 impossible nor identifies the A4 x C2 x C2 operator symmetry with a particle-selection law.',sourceHashes};
const out=new URL('../results/pb208-formation-gate/',import.meta.url);await mkdir(out,{recursive:true});await writeFile(new URL('verification.json',out),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:report.status,layers,counts,matching:report.matching,legacyWindowCompatibility:report.legacyWindowCompatibility,nativeGrammar,seedMarkings:runs.length,terminalPacket:runs[0].species,resolutionTrials},null,2));
