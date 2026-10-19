import assert from 'node:assert/strict';
import {readFile,mkdir,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {probeSpace,domainOf,enumerateProbe} from './n14-probe-model.mjs';
import * as production from '../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
const mode=process.argv[2];if(!['baseline','ee','regular','larger','larger-regular'].includes(mode))throw Error('Expected baseline|ee|regular|larger|larger-regular');
const hash=b=>createHash('sha256').update(b).digest('hex');
const fingerprintFiles=['./check_n14_assumptions.mjs','./n14-probe-model.mjs','../n14-assumptions-protocol-v1.md',...['phase-assembly-model.mjs','phase-advance-model.mjs','phase-discipline-model.mjs','simplex-model.mjs','simplex-components.mjs','lattice-items.mjs','window-construction-model.mjs','deuterium-tunnel-model.mjs','fiber-coverage-model.mjs'].map(f=>'../demos/particle-overlap-tetrahedron/'+f)],sourceHashes={};
for(const f of fingerprintFiles)sourceHashes[f]=hash(await readFile(new URL(f,import.meta.url)));
const expanded=mode.startsWith('larger'),regularElectrons=mode.includes('regular'),allowEE=mode==='ee';
const space=probeSpace(expanded),domain=domainOf(space);
if(expanded)assert.ok(domain.adjacency.slice(0,343).every(edges=>edges.length===4),'Original boundary must be fully surrounded');
const result=enumerateProbe(space,{regularElectrons,allowEE});
let compiler=production,adapter=null;
if(expanded){
 // Isolated test adapter: only the module's lattice/domain bindings change.
 // Assert that both admission/audit function bodies are byte-identical.
 const url=new URL('../demos/particle-overlap-tetrahedron/phase-assembly-model.mjs',import.meta.url);
 let text=await readFile(url,'utf8');
 text=text.replace("import {lattice,faces} from './simplex-model.mjs';",`import {faces} from './simplex-model.mjs';\nconst lattice=${JSON.stringify(space)};`);
 text=text.replace('const domain=assemblyDomain(),keys=',`const domain=${JSON.stringify(domain)},keys=`);
 text=text.replace(/from '(\.[^']+)'/g,(_,path)=>`from '${new URL(path,url).href}'`);
 compiler=await import('data:text/javascript;base64,'+Buffer.from(text).toString('base64'));
 for(const f of ['compilePhaseAssembly','auditPhaseAssembly'])assert.equal(compiler[f].toString(),production[f].toString());
 adapter={kind:'isolated-module-domain-rebinding',compileBodySha256:hash(production.compilePhaseAssembly.toString()),auditBodySha256:hash(production.auditPhaseAssembly.toString()),functionBodiesUnchanged:true};
}
const summary={sourceHashes,mode,domainCells:space.cells.length,regularElectrons,allowElectronContacts:allowEE,geometryComplete:result.complete,prefixCounts:result.prefixCounts,typedNuclei:result.typedNuclei,electronPools:result.electronPools,adjacencyRejected:result.adjacencyRejected,geometryCandidates:result.candidates?.length??null,stop:result.stop??null,adapter};
if(mode==='baseline'){
 assert.equal(result.complete,true);assert.equal(result.typedNuclei,2384);assert.deepEqual(result.electronPools,{'7':1920,'8':464});assert.equal(result.adjacencyRejected,5632);assert.equal(result.candidates.length,0);
}
let witness=null,phaseTested=0;const rejections={};
if(result.complete&&allowEE&&result.candidates.length){
 for(const candidate of result.candidates){
  try{const r=compiler.compilePhaseAssembly(candidate,0);assert.equal(r.status,'rejected');}
  catch(error){if(!/Unsupported physical face contact/.test(error.message))throw error;witness={candidate,geometryOnly:true,admissionError:error.message};break;}
 }
 assert.ok(witness,'A root-compatible EE packing must reach the contact-policy rejection');
 summary.productionAdmission='rejects-unsupported-EE-contact';
}else if(result.complete){
 outer:for(const candidate of result.candidates)for(let orientations=0;orientations<2**candidate.interfaces.filter(e=>e.kind==='PN').length;orientations++){
  phaseTested++;const r=compiler.compilePhaseAssembly(candidate,orientations);
  if(r.status!=='phase-coherent-reference'){rejections[r.reason]=(rejections[r.reason]??0)+1;continue;}
  const audit=compiler.auditPhaseAssembly(r);assert.equal(audit.coverage.coveredCells,21);
  witness={candidate,orientations,regularElectronCount:candidate.electrons.filter(i=>domain.species[i]==='proton').length,usesAddedCells:[...candidate.nucleus,...candidate.electrons].some(i=>i>=343),audit,reference:r};break outer;
 }
}
summary.phaseAssignmentsTested=phaseTested;summary.phaseSearchComplete=result.complete&&!allowEE&&!witness;summary.phaseCompatible=!!witness&&!allowEE;summary.phaseRejections=rejections;
summary.scope=allowEE?'Packing diagnostic only: no EE law supplied or admitted.':expanded?'One added complete neighboring-item shell; original phase functions rebound to that domain only.':'Original domain; unchanged phase admission functions.';
for(const f of fingerprintFiles)assert.equal(hash(await readFile(new URL(f,import.meta.url))),sourceHashes[f],'Source changed during probe: '+f);
await mkdir('research/strominger/results/n14-assumptions',{recursive:true});
const spaceRecord=expanded?{cells:space.cells,nodes:space.nodes.map(n=>({address:n.address})),components:space.assembly.components}:null;
await writeFile(`research/strominger/results/n14-assumptions/${mode}.json`,JSON.stringify({summary,witness,space:spaceRecord},null,2)+'\n');console.log(JSON.stringify(summary,null,2));
