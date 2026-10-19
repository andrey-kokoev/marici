// Pre-Be-9 lithium acceptance fingerprints; do not regenerate to hide drift.
import assert from 'node:assert/strict';
import {readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
const expected=[
 [5,0,0,0,'4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945'],
 [6,96,2304,5,'ed35cb4748969d05ed54b2ba247feadf3b45a6423d98fede8cfb71e424113c48'],
 [7,528,26880,32,'3a2b6a20d389127cc400570339215b3440a344e1a7eac54da91d6625c150210f'],
 [8,3744,119808,10,'74d15c03ee8b65dbce4d87d5a843593253a911fd2d1b17956da5fb8ba7c3a2b2']
],rows=[];
// The summarizer checks receipt/source freshness and recompiles every acceptance.
await import('./summarize_lithium_discrimination.mjs');
for(const [mass,geometryCandidates,readerAssignments,admittedAssignments,expectedHash] of expected){
 const {summary:s,acceptedGeometries}=JSON.parse(await readFile(`research/strominger/results/lithium-discrimination/li${mass}.json`,'utf8'));
 assert.deepEqual([s.geometryCandidates,s.readerAssignments,s.admittedAssignments],[geometryCandidates,readerAssignments,admittedAssignments]);
 const hash=createHash('sha256').update(JSON.stringify(acceptedGeometries)).digest('hex');assert.equal(hash,expectedHash);
 rows.push({isotope:s.isotope,geometryCandidates,readerAssignments,admittedAssignments,acceptedGeometryAndReaderSha256:hash,unchanged:true});
}
await writeFile('research/strominger/results/beryllium9-assembly/lithium-regression.json',JSON.stringify({status:'pass-unchanged-lithium-search',rows,scope:'Generalizing electron combinations and target counts for Be-9 preserves all prior lithium acceptance records, not just their totals. Unstable targets remain test controls only.'},null,2)+'\n');
console.log('PASS Be-9 search generalization: all prior lithium acceptance records unchanged.');
