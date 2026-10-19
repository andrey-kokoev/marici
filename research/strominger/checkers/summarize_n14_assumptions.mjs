import assert from 'node:assert/strict';
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const out='research/strominger/results/n14-assumptions',rows=[];let sourceHashes=null;
for(const [mode,cells,nuclei,candidates] of [['baseline',343,2384,0],['ee',343,2384,5632],['regular',343,2384,0],['larger',875,2912,0],['larger-regular',875,2912,0]]){
 const {summary:s,witness}=JSON.parse(await readFile(`${out}/${mode}.json`,'utf8'));
 assert.equal(s.geometryComplete,true);assert.equal(s.stop,null);assert.equal(s.domainCells,cells);assert.equal(s.typedNuclei,nuclei);assert.equal(s.geometryCandidates,candidates);
 if(sourceHashes)assert.deepEqual(s.sourceHashes,sourceHashes);else sourceHashes=s.sourceHashes;
 if(mode==='ee'){assert.equal(witness.geometryOnly,true);assert.ok(witness.candidate.interfaces.some(e=>e.kind==='EE'));assert.match(witness.admissionError,/Unsupported physical face contact/);assert.equal(s.phaseCompatible,false);}else {assert.equal(witness,null);assert.equal(s.phaseAssignmentsTested,0);}
 rows.push({mode,cells,typedNuclei:nuclei,geometryCandidates:candidates,phaseCompatible:s.phaseCompatible,geometryOnly:mode==='ee'});
}
for(const [f,h] of Object.entries(sourceHashes))assert.equal(createHash('sha256').update(await readFile(new URL(f,import.meta.url))).digest('hex'),h,'Stale probe: '+f);
const result={status:'complete-controlled-geometry-probes',rows,sourceHashes,conclusion:'The E/E full-face exclusion is the immediate packing obstruction in these domains. Permitting regular electrons or adding one complete item shell, separately or together, does not remove it. Allowing EE yields packings only: no EE law or phase admission was supplied.',limits:'No conclusion about all larger/unbounded domains, non-tetrahedral electron representations, physical stability, or a valid replacement contact rule. Production rules and viewer remain unchanged.'};
await writeFile(out+'/verification.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify(rows,null,2));console.log(result.conclusion);
