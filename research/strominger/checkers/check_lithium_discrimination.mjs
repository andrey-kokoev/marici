// Frozen-rule comparison: empirical stability labels are deliberately absent here.
import assert from 'node:assert/strict';
import {mkdir,readFile,readdir,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {searchLithiumAssemblies,assemblyDomain} from '../demos/particle-overlap-tetrahedron/lithium6-assembly-model.mjs';
import {compilePhaseAssembly,auditPhaseAssembly} from '../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
const mass=Number(process.argv[2]);if(![5,6,7,8].includes(mass))throw Error('Usage: node check_lithium_discrimination.mjs 5|6|7|8');
// Conservatively fingerprint every local model module, including dependencies.
const files=(await readdir(new URL('../demos/particle-overlap-tetrahedron/',import.meta.url))).filter(f=>f.endsWith('.mjs')).sort();
const digest=b=>createHash('sha256').update(b).digest('hex'),sourceHashes={};
for(const f of files)sourceHashes[f]=digest(await readFile(new URL('../demos/particle-overlap-tetrahedron/'+f,import.meta.url)));
const search=searchLithiumAssemblies({allowNN:true,neutronCount:mass-3}),domain=assemblyDomain();
console.log(`Li-${mass}: ${search.candidates.length} geometry candidates; prefixes ${search.prefixCounts}`);
let assignments=0,admitted=0,firstWitness=null;const geometries=[],rejections={};
for(const [index,candidate] of search.candidates.entries()){
 assert.equal(candidate.nucleus.filter(i=>domain.species[i]==='proton').length,3);
 assert.equal(candidate.nucleus.filter(i=>domain.species[i]==='neutron').length,mass-3);
 assert.equal(candidate.electrons.length,3);
 assert.equal(new Set([...candidate.nucleus,...candidate.electrons]).size,mass+3);
 const accepted=[];
 for(let orientations=0;orientations<2**candidate.interfaces.filter(e=>e.kind==='PN').length;orientations++){
  assignments++;const r=compilePhaseAssembly(candidate,orientations);
  if(r.status!=='phase-coherent-reference'){assert.equal(r.status,'rejected');rejections[r.reason]=(rejections[r.reason]??0)+1;continue;}
  const audit=auditPhaseAssembly(r);assert.equal(audit.coverage.requiredCells,mass+3);assert.equal(audit.coverage.coveredCells,mass+3);assert.equal(audit.coverage.allEnteredStatesReachExit,true);assert.equal(audit.physicalBindingLawDerived,false);
  admitted++;accepted.push(orientations);
  if(!firstWitness)firstWitness={reference:r,audit};
 }
 if(accepted.length)geometries.push({candidateIndex:index,candidate,orientations:accepted});
}
assert.equal(assignments,admitted+Object.values(rejections).reduce((a,b)=>a+b,0));
assert.equal(assignments,search.candidates.reduce((sum,c)=>sum+2**c.interfaces.filter(e=>e.kind==='PN').length,0));
assert.equal(admitted,geometries.reduce((sum,g)=>sum+g.orientations.length,0));
for(const [f,h] of Object.entries(sourceHashes))assert.equal(digest(await readFile(new URL('../demos/particle-overlap-tetrahedron/'+f,import.meta.url))),h);
const out='research/strominger/results/lithium-discrimination';await mkdir(out,{recursive:true});
const protocolSha256=digest(await readFile(new URL('../lithium-discrimination-protocol-v1.md',import.meta.url))),checkerSha256=digest(await readFile(new URL(import.meta.url)));
const summary={protocolSha256,checkerSha256,isotope:'Li-'+mass,status:admitted?'compatible-reference-exists':'no-compatible-reference-in-bounded-domain',complete:true,counts:{proton:3,neutron:mass-3,electron:3},domainCells:search.primitiveCells,prefixCounts:search.prefixCounts,typedNuclei:search.typedNuclei,geometryCandidates:search.candidates.length,readerAssignments:assignments,admittedAssignments:admitted,admittedGeometries:geometries.length,rejections,retainedPreviousIsotopeRequired:false,allowNN:true,sourceHashes,scope:search.scope};
await writeFile(`${out}/li${mass}.json`,JSON.stringify({summary,acceptedGeometries:geometries,firstWitness},null,2)+'\n');
console.log(JSON.stringify(summary,null,2));
