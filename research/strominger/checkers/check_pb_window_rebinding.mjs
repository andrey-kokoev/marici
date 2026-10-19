// Feasibility audit of the existing Pb proton sites. Enumeration supplies an
// upper bound on possible bindings, not permission to choose a separate frame
// for every proton or to call a global packing search sequential construction.
import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import {lead208Bodies} from '../demos/particle-overlap-tetrahedron/lead208-model.mjs';
import {createWindowConstruction,windowProtocol} from '../demos/particle-overlap-tetrahedron/window-construction-model.mjs';
import {itemKey} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
const permutations=a=>a.length?a.flatMap((x,i)=>permutations(a.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];
const frames=permutations([0,1,2,3]),protons=lead208Bodies.filter(b=>b.species==='proton'),witnesses=lead208Bodies.filter(b=>b.role==='witness');
const occupied=new Map([...protons,...witnesses].flatMap(b=>b.components.map(c=>[itemKey(c),b.id])));
assert.equal(protons.length,82);assert.equal(witnesses.length,44);
const rows=[],domains=[];
for(const proton of protons){
 if(proton.shape.vertices.length!==4||proton.components.length!==1){rows.push({proton:proton.id,site:proton.shape.itemId,status:'missing-carrier-binding',kind:proton.shape.kind,vertices:proton.shape.vertices.length,components:proton.components.length,reason:'The retained proton carrier has four marked vertices; this whole six-vertex octahedron has no supplied binding. No child is selected arbitrarily.'});continue;}
 const options=new Map(),blockedBy=new Set();let compatibleFrames=0;
 for(const frame of frames){
  const bindings=Object.fromEntries(windowProtocol[0].nodes.map((name,i)=>[name,proton.shape.vertices[frame[i]]]));
  const engine=createWindowConstruction({seed:proton.shape,bindings});let state=engine.snapshot();
  while(state.status==='ready')state=engine.step();
  if(state.status!=='complete')continue;
  const resources=state.items.slice(1).map(s=>s.key),blockers=resources.filter(k=>occupied.has(k));
  blockers.forEach(k=>blockedBy.add(occupied.get(k)));if(blockers.length)continue;
  compatibleFrames++;const key=resources.join('>');if(!options.has(key))options.set(key,{resources,frame});
 }
 rows.push({proton:proton.id,site:proton.shape.itemId,status:options.size?'requires-transported-frame':'no-free-binding-with-fixed-occupants',framesExamined:frames.length,compatibleFrames,distinctGeometricOptions:options.size,blockingOccupants:[...blockedBy]});
 domains.push({proton:proton.id,options:[...options.values()]});
}
let possibleConflicts=0;
for(let i=0;i<domains.length;i++)for(let j=i+1;j<domains.length;j++)if(domains[i].options.some(a=>domains[j].options.some(b=>a.resources.some(k=>b.resources.includes(k)))))possibleConflicts++;
const summary={fixedProtons:protons.length,fixedWitnessNeutrons:witnesses.length,fourVertexProtonSites:domains.length,missingCarrierBindings:rows.filter(r=>r.status==='missing-carrier-binding').length,sitesWithNoFreeBinding:rows.filter(r=>r.status==='no-free-binding-with-fixed-occupants').length,sitesWithMultipleGeometricOptions:rows.filter(r=>r.distinctGeometricOptions>1).length,sitesWithOneGeometricOption:rows.filter(r=>r.distinctGeometricOptions===1).length,pairsOfSitesWithPotentialPlacementConflict:possibleConflicts};
const report={status:'full-layout-not-constructed',summary,rows,scope:'Necessary local feasibility conditions only, retaining all old proton bodies and 44 witness neutron bodies. Legacy outward neutron/electron placements are discarded for this audit. No independent frames are chosen and no partial result is presented as full Pb-208.',missingRules:['A four-vertex marked-carrier binding or authorized role reassignment for the eight octahedral proton sites.','Transport of the incoming marked state between the 82 proton instances; the retained P→N→E packet terminates at E and does not supply an E→next-P construction.','A shared construction order resolving occupation of cells needed by different packets without coordinate-order or count-based tie-breaking.']};
const out='research/strominger/results/pb-window-rebinding';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify({status:report.status,...summary},null,2));
