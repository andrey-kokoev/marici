// Structural C-13 + P experiment, not a reaction-rate or photon model.
import assert from 'node:assert/strict';
import {mkdir,readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {lattice} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
import {assemblyDomain} from '../demos/particle-overlap-tetrahedron/lithium6-assembly-model.mjs';
import {selectPhaseAssembly,compilePhaseAssembly,auditPhaseAssembly} from '../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
const files=['phase-assembly-model.mjs','lithium6-assembly-model.mjs','phase-advance-model.mjs','window-construction-model.mjs','simplex-model.mjs','simplex-components.mjs'],hash=b=>createHash('sha256').update(b).digest('hex'),sourceHashes={};
for(const f of files)sourceHashes[f]=hash(await readFile(new URL('../demos/particle-overlap-tetrahedron/'+f,import.meta.url)));
const old=selectPhaseAssembly('carbon13'),{adjacency,species}=assemblyDomain(),chartKey=c=>JSON.stringify([c.cell,c.species,c.aliases]);
function extensions(retainElectrons){
 const electrons=retainElectrons?[...old.candidate.electrons]:[],occupied=[...old.candidate.nucleus,...electrons],nuclearVertices=new Set(old.candidate.nucleus.flatMap(i=>lattice.cells[i]));
 const initialTypes=Object.fromEntries(Object.entries(old.candidate.types).filter(([v])=>retainElectrons||nuclearVertices.has(Number(v))));
 const candidates=[],rejections={};let neighboringProtons=0;
 for(let p=0;p<lattice.cells.length;p++){
  if(species[p]!=='proton'||occupied.includes(p)||!adjacency[p].some(e=>old.candidate.nucleus.includes(e.to)))continue;neighboringProtons++;
  const nucleus=[...old.candidate.nucleus,p].sort((a,b)=>a-b),all=[...nucleus,...electrons],types={...initialTypes};let reason=null;
  for(const e of adjacency[p].filter(e=>old.candidate.nucleus.includes(e.to))){
   if(species[e.to]!=='neutron'||e.face.filter(v=>types[v]==='M').length!==2){reason='PN-role-mismatch';break;}
   const apex=lattice.cells[p].find(v=>!e.face.includes(v));if(types[apex]&&types[apex]!=='C'){reason='retained-role-conflict';break;}types[apex]='C';
  }
  const interfaces=[];
  if(!reason)for(const i of all)for(const e of adjacency[i])if(i<e.to&&all.includes(e.to)){
   const a=electrons.includes(i)?'electron':species[i],b=electrons.includes(e.to)?'electron':species[e.to];
   if(a===b&&a!=='neutron'||[a,b].includes('electron')&&[a,b].includes('proton')){reason='unsupported-contact';continue;}
   const kind=[a,b].includes('electron')?'NE':a===b?'NN':'PN';
   if(e.face.filter(v=>types[v]==='M').length!==(kind==='PN'?2:1)){reason='interface-role-mismatch';continue;}
   interfaces.push({from:i,to:e.to,face:[...e.face],kind});
  }
  if(reason){rejections[reason]=(rejections[reason]??0)+1;continue;}
  for(const i of all)assert.equal(lattice.cells[i].filter(v=>types[v]==='M').length,2);
  candidates.push({addedProton:p,candidate:{nucleus,electrons,types,interfaces,nuclearCycleRank:interfaces.filter(e=>e.kind!=='NE').length-13}});
 }
 return {neighboringProtons,rejections,candidates};
}
const charged=extensions(true),bare=extensions(false),accepted=[],rejections={};let tested=0,witness=null;
for(const {addedProton,candidate} of charged.candidates)for(let orientation=0;orientation<2**candidate.interfaces.filter(e=>e.kind==='PN').length;orientation++){
 tested++;const r=compilePhaseAssembly(candidate,orientation);
 if(r.status!=='phase-coherent-reference'){rejections[r.reason]=(rejections[r.reason]??0)+1;continue;}
 const audit=auditPhaseAssembly(r);assert.equal(audit.coverage.coveredCells,20);
 const preservesReaders=old.charts.every(a=>r.charts.some(b=>chartKey(a)===chartKey(b)));
 accepted.push({addedProton,orientation,preservesReaders});
 if(preservesReaders&&!witness){
  for(const e of old.edges)assert.ok(r.edges.some(f=>chartKey(old.charts[e.from])===chartKey(r.charts[f.from])&&chartKey(old.charts[e.to])===chartKey(r.charts[f.to])&&e.kind===f.kind&&e.phaseDelta===f.phaseDelta&&JSON.stringify(e.permutation)===JSON.stringify(f.permutation)));
  witness={addedProton,orientation,reference:r,audit,oldReadersAndTransportPreserved:true};
 }
}
assert.equal(tested,accepted.length+Object.values(rejections).reduce((a,b)=>a+b,0));
let bareAtWitness=null;
if(witness){
 const c=bare.candidates.find(c=>c.addedProton===witness.addedProton);assert.ok(c);
 bareAtWitness=compilePhaseAssembly(c.candidate,witness.orientation);
 assert.equal(bareAtWitness.status,'rejected');assert.equal(bareAtWitness.reason,'phase-directed-dead-end');
}
for(const f of files)assert.equal(hash(await readFile(new URL('../demos/particle-overlap-tetrahedron/'+f,import.meta.url))),sourceHashes[f]);
const result={status:witness?'retained-C13-plus-proton-reference-found':'no-reader-preserving-reference-in-tested-retained-scope',sourceHashes,counts:{proton:7,neutron:7,electron:6},formalCharge:1,charged:{...charged,readerAssignmentsTested:tested,phaseSearchComplete:true,accepted,rejections},bare:{...bare,atChargedWitness:bareAtWitness,scope:'Geometry only; the existing admission certificate requires E exits. Its bare-nucleus rejection is not physical impossibility.'},witness,scope:'Selected C-13 retained, one adjacent proton added, no seventh electron. All attachment cells in the existing domain and all reader assignments for valid six-electron extensions tested. No change to production rules. No gamma emission, energy balance, capture dynamics, rates or binding derived; no neutral N-14 admission.'};
await mkdir('research/strominger/results/carbon13-proton-capture',{recursive:true});await writeFile('research/strominger/results/carbon13-proton-capture/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:result.status,chargedGeometry:charged.candidates.map(c=>c.addedProton),bareGeometry:bare.candidates.map(c=>c.addedProton),tested,accepted,rejections,witness:witness?{addedProton:witness.addedProton,orientation:witness.orientation,states:witness.audit.phaseStateCount,coveredCells:witness.audit.coverage.coveredCells}:null,bareAtWitness},null,2));
