// Explicit post-repair successor, not a rewrite of the historical Be-9 baseline.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
await import('./summarize_lithium_discrimination.mjs');
const cases=[
 [5,0,0,0,'4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945'],
 [6,96,2304,5,'ed35cb4748969d05ed54b2ba247feadf3b45a6423d98fede8cfb71e424113c48'],
 [7,528,26880,32,'3a2b6a20d389127cc400570339215b3440a344e1a7eac54da91d6625c150210f'],
 [8,3744,119808,5,'08f25c04d86094c06e48825213f8ef6ead4ce55035c94ad79212387ee529c425']
],rows=[];
for(const [mass,geometry,assignments,accepted,expectedHash] of cases){
 const {summary:s,acceptedGeometries}=JSON.parse(await readFile(`research/strominger/results/lithium-discrimination/li${mass}.json`));
 assert.deepEqual([s.geometryCandidates,s.readerAssignments,s.admittedAssignments],[geometry,assignments,accepted]);
 const hash=createHash('sha256').update(JSON.stringify(acceptedGeometries)).digest('hex');assert.equal(hash,expectedHash);
 if(mass===8)assert.equal(s.rejections['unwitnessed-physical-contact'],36);
 rows.push({mass,geometryCandidates:geometry,readerAssignments:assignments,acceptedAssignments:accepted,acceptedSha256:hash,historicalAcceptedAssignments:mass===8?10:accepted,intentionalContactGateDelta:mass===8?-5:0});
}
await mkdir('research/strominger/results/assembly-contact-coverage',{recursive:true});await writeFile('research/strominger/results/assembly-contact-coverage/lithium-regression.json',JSON.stringify({status:'explicit-post-contact-repair-regression',rows,historicalLi8Sha256:'74d15c03ee8b65dbce4d87d5a843593253a911fd2d1b17956da5fb8ba7c3a2b2',scope:'Li-5/6/7 exact accepted records unchanged. Li-8 loses five acceptances under the stronger contact gate but remains compatible and empirically radioactive. Historical Be-9 unchanged-baseline checker deliberately preserved; its Li-8 expectation is superseded, not silently rewritten.'},null,2)+'\n');console.log('PASS post-contact lithium regression: Li-5/6/7 unchanged; Li-8 intentionally reduced from 10 to 5 acceptances.');
