import assert from 'node:assert/strict';
import {writeFile} from 'node:fs/promises';
import {slice,cells,seed,apex} from './normal-ray-model.mjs';
import {nativePhaseFrame,auditPhaseCombination} from '../strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';
const stop=slice(1);assert.deepEqual(stop.traversed,[seed.id]);assert.equal(stop.atStop.length,2);
const next=cells[stop.atStop.find(id=>id!==seed.id)],key=p=>JSON.stringify(p);
const face=seed.vertices.filter(p=>next.vertices.some(q=>key(p)===key(q)));
assert.equal(face.length,3);assert(face.every(p=>p[0]===-4));
assert(seed.vertices.some(p=>key(p)===key(apex)));
assert(next.vertices.some(p=>p[0]>-4));
function permutations(xs){return xs.length?xs.flatMap((x,i)=>permutations(xs.filter((_,j)=>i!==j)).map(p=>[x,...p])):[[]];}
const pNames=['C0','M0','C1','M1'],eNames=['M1','C1','C2','M2'];
let tested=0,compatibleSharedOccurrencePatterns=0,admitted=0;const examples=[];
for(const p of permutations(seed.vertices))for(const e of permutations(next.vertices)){
 const frame=(id,species,names,vertices)=>nativePhaseFrame(id,species,Object.fromEntries(names.map((n,i)=>[n,key(vertices[i])])));
 const frames=[frame('p','proton',pNames,p),frame('e','electron',eNames,e)];
 assert(frames.every(f=>f.window.length===3));
 const audit=auditPhaseCombination(frames,[{from:'p',to:'e',kind:'PE',identification:'same-occurrence',vertices:face.map(key)}]);
 tested++;if(audit.status==='native-phase-compatible')admitted++;
 if(audit.issues.every(issue=>issue.kind==='missing-phase-transition-witness')){
  compatibleSharedOccurrencePatterns++;
  if(!examples.length)examples.push({frames,audit});
 }
}
assert.equal(tested,576);assert.equal(admitted,0);assert(compatibleSharedOccurrencePatterns>0);
const out={status:'checked-not-isotope-verified',candidate:'hydrogen-1 at k=1',
 geometry:{sliceTiles:stop.polygons.length,traversedBeforeStop:stop.traversed,cellsContainingStop:stop.atStop,
 seed:seed.vertices,nextCell:next.vertices,sharedFace:face,fullNextCellExtendsBeyondStop:true},
 markingAudit:{tested,compatibleSharedOccurrencePatterns,admitted,examples},
 conclusions:['One traversed tetrahedron and one uniquely face-adjacent continuation cell are present.',
 'The two-cell pair is obtained by including the cell across the stop face; it is not the volume already traversed.',
 'Some native P/E markings meet same-occurrence face constraints up to a relative origin; markings are not uniquely selected.',
 'The current phase gate has no registered direct PE transition. Its rejection is a missing-witness result, not a geometric impossibility.',
 'Hydrogen-1 counts result only if the two bodies are assigned P and E. No binding, particle-role emergence or physical isotope verification follows.']};
await writeFile(new URL('./results/first-crossing-hydrogen-v1.json',import.meta.url),JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({status:out.status,geometry:out.geometry,markings:{tested,compatibleSharedOccurrencePatterns,admitted}}));
