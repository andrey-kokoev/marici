import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {searchCounts} from './proton-rich-probe-model.mjs';
import {searchLithiumAssemblies} from '../demos/particle-overlap-tetrahedron/lithium6-assembly-model.mjs';
const files=['./check_proton_rich_counts.mjs','./proton-rich-probe-model.mjs','./n14-probe-model.mjs',...['lithium6-assembly-model.mjs','simplex-model.mjs','simplex-components.mjs','lattice-items.mjs'].map(f=>'../demos/particle-overlap-tetrahedron/'+f)],hash=b=>createHash('sha256').update(b).digest('hex'),sourceHashes={};
for(const f of files)sourceHashes[f]=hash(await readFile(new URL(f,import.meta.url)));
const controls=[];
for(const n of [2,3,4,5]){const r=searchCounts(3,n,3),production=searchLithiumAssemblies({allowNN:true,neutronCount:n});assert.deepEqual(r.candidates,production.candidates);controls.push({protons:3,neutrons:n,electrons:3,candidateListsIdentical:true,candidates:r.candidates.length});}
const baseline=searchCounts(7,7,7);assert.equal(baseline.typedNuclei,2384);assert.deepEqual(baseline.electronPools,{'7':1920,'8':464});assert.equal(baseline.adjacencyRejected,5632);assert.equal(baseline.candidates.length,0);
const cases=[];
for(const counts of [[7,6,6],[7,6,7],[8,6,6],[8,6,7],[8,6,8]]){
 const r=searchCounts(...counts);assert.equal(r.geometryComplete,true);assert.equal(r.candidates.length,0);
 cases.push({...r,geometryCandidates:r.candidates.length,phaseAssignmentsTested:0,status:'no-complete-geometry-in-bounded-domain'});
}
assert.deepEqual(cases.map(r=>r.typedNuclei),[2064,0,288,0,0]);assert.deepEqual(cases.map(r=>r.adjacencyRejected),[352,0,48,0,0]);
for(const f of files)assert.equal(hash(await readFile(new URL(f,import.meta.url))),sourceHashes[f]);
const result={status:'bounded-proton-rich-count-searches-complete',sourceHashes,controls,baseline:{typedNuclei:baseline.typedNuclei,electronPools:baseline.electronPools,adjacencyRejected:baseline.adjacencyRejected},cases,scope:'Unrestricted arrangements within the existing rooted 343-cell domain and all six MMCC root markings. Original PN/NN contacts, occupied native-P reference for each N, split nonadjacent electrons. Electron-count-dependent NN port bound is necessary, not a stability law. No phase candidates survive. Not a whole-domain physical impossibility theorem; more strongly ionized states, other domains and broader geometries not tested.'};
await mkdir('research/strominger/results/n13-o14-capture',{recursive:true});await writeFile('research/strominger/results/n13-o14-capture/unrestricted-counts.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(cases.map(({candidates,...r})=>r),null,2));
