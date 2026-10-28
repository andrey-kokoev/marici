// Frozen receiver/type audit. No invented encoder or replacement receiver.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules,applyPhasePermutation} from '../../nima/generative-phase-assembly.mjs';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,reconcileBothOrders} from '../su32-layer4-comparison.mjs';
import {prepareCentralReferencePacket,validateCentralReferencePacket} from '../su32-central-reference-completion.mjs';
const dir='research/strominger/results/su32-fixed-receiver-encoding-audit-v1';
const contractPath=dir+'/contract.json',contractBytes=await fs.readFile(contractPath);
const contract=JSON.parse(contractBytes),sha=x=>createHash('sha256').update(x).digest('hex');
const fixturePath='research/strominger/results/su32-hopf-tests-v1/fixture.json';
const fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
for(const [p,h] of Object.entries(fixture.sourceHashes))assert.equal(sha(await fs.readFile(p)),h);
const atlas=buildSu32SignedReferenceAtlas(fixture),reading=fixture.readings.find(r=>r.id===contract.reading);
const chart=atlas.charts.find(c=>c.reading===reading.id&&c.source===reading.incomingN);assert(chart);
const layout=comparisonLayout(atlas,fixture,chart.id,contract.binding);
assert.equal(layout.chart.target,contract.fixedFace.from);
const face=fixture.interfaces.find(f=>f.id===contract.fixedFace.id);assert(face);
assert.deepEqual([...face.ports].sort(),[contract.fixedFace.from,contract.fixedFace.to].map(c=>c+'@'+face.id).sort());
// The operation is selected and validated independently of any Su32 payload.
const rules=new GenerativeAssemblyRules();
const pn=rules.outgoing(rules.root).map(i=>rules.operations[i]).filter(o=>o.kind==='PN');assert.equal(pn.length,1);
const ne=rules.outgoing(pn[0].target).map(i=>rules.operations[i]).filter(o=>o.kind==='NE');assert.equal(ne.length,1);
const operation=ne[0];assert(rules.validateTransfer(operation));
const source=rules.packets[operation.source],target=rules.packets[operation.target];
const sourceChart=rules.charts[source.chart],targetChart=rules.charts[target.chart];
assert.equal(sourceChart.species,'neutron');assert.equal(targetChart.species,'electron');
assert.deepEqual(operation.permutation,[0,4,2,3,1]);
// Exact command invertibility includes extreme finite values and signed zero.
const values=[0,-0,1,-1,Number.MIN_VALUE,-Number.MIN_VALUE,Number.MAX_VALUE,-Number.MAX_VALUE,Number.EPSILON,Math.PI];
let inverseChecks=0;
for(let k=0;k<values.length;k++){
 const packet=Array.from({length:5},(_,i)=>[values[(2*i+k)%values.length],values[(2*i+k+1)%values.length]]);
 const before=structuredClone(packet),after=applyPhasePermutation(packet,operation.permutation);
 assert.deepEqual(applyPhasePermutation(after,operation.permutation,-1),packet);
 assert.deepEqual(packet,before);inverseChecks++;
}
let negativeControls=0;const reject=f=>{assert.throws(f);negativeControls++;};
const numeric=[[1,0],[2,0],[3,0],[4,0],[5,0]];
reject(()=>applyPhasePermutation(numeric.slice(0,4),operation.permutation));
reject(()=>applyPhasePermutation([...numeric,[6,0]],operation.permutation));
reject(()=>applyPhasePermutation([[NaN,0],...numeric.slice(1)],operation.permutation));
reject(()=>applyPhasePermutation([[Infinity,0],...numeric.slice(1)],operation.permutation));
reject(()=>applyPhasePermutation([[{history:'sidecar'},0],...numeric.slice(1)],operation.permutation));
reject(()=>applyPhasePermutation(numeric,[0,0,2,3,4]));
reject(()=>rules.validateTransfer({...operation,face:['absent']}));
reject(()=>rules.validateTransfer(operation,source,{...target,origin:target.origin+1}));
// Construct concrete members to check admission of the source family. The
// universal cardinality argument is NOT inferred from enumerating these samples.
const width=641;
const words=['0'.repeat(width),'1'.repeat(width),'1'+'0'.repeat(width-1),'0'.repeat(width-1)+'1'];
const samples=words.map(word=>{
 const registry={'P+':word,'P-':0,'E+':0,'E-':0};
 const built=reconcileBothOrders(layout,registry);
 const packet=prepareCentralReferencePacket(layout,built.byE,built.byP);
 assert(validateCentralReferencePacket(layout,packet));assert.equal(packet.core.records['P+'].payload,word);
 assert.equal(packet.parent,null);assert.equal(packet.operation,null);
 return packet;
});
assert.equal(new Set(samples.map(p=>JSON.stringify(p))).size,words.length);
// ECMAScript Number uses binary64. Ten finite Number coordinates have AT MOST
// 2^640 representations (excluding NaN/infinity only decreases this bound).
// There are 2^641 distinct fixed-length binary payload strings, and each yields
// a distinct valid source packet because its P+ record is retained verbatim.
const sourceCardinality=1n<<641n,receiverUpperBound=1n<<640n;
assert(sourceCardinality>receiverUpperBound);
const sourcePaths=[contractPath,fixturePath,'research/nima/generative-phase-assembly.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs',
 'research/strominger/su32-signed-reference-encoder.mjs','research/strominger/su32-layer4-comparison.mjs',
 'research/strominger/su32-central-reference-completion.mjs','research/strominger/checkers/check_su32_fixed_receiver_encoding_audit.mjs'];
const sourceHashes={};for(const p of sourcePaths)sourceHashes[p]=sha(await fs.readFile(p));
assert.equal(sourceHashes[contractPath],sha(contractBytes),'Frozen contract changed during the test');
const report={schema:'su32.fixed-receiver-encoding-audit.v1',passed:true,
 contractPath,contractHash:sha(contractBytes),fixedFace:contract.fixedFace,
 receiverCandidate:{operation,sourcePacket:source,targetPacket:target,sourceChart,targetChart,
  actualPrimitiveFace:operation.face,bindingToSu32Face:null},
 inverseChecks,negativeControls,sourceSamples:samples,
 capacityArgument:{sourceFamilySize:'2^641',receiverStateUpperBound:'2^640',strictInequalityVerified:true,
  proof:'Every 641-bit payload is valid JSON and is retained in P+. Ten finite binary64 coordinates have at most 640 bits. Pigeonhole principle forces a collision for EVERY encoder into this carrier; composing with the fixed permutation cannot repair it.',
  noExplicitCollisionPair:'The encoder is universally quantified, not specified; the proof establishes a collision for each encoder, not one pair that every encoder must collide.'},
 verdict:{numericalCandidate:'Universal exact encoding of this admitted source family into the fixed five-slot numerical receiver is impossible, even with attachment constraints relaxed.',
  command:'The existing full-vector NE command is bijective; it introduces no additional loss. The obstruction is the encoding capacity.',
  originalExistentialConjecture:'Not universally falsified across other receiver types. No native Su32 face binding or successful native continuation is claimed.'},
 escapeConditions:['Restrict the source family and provenance bounds before defining an encoder.',
  'Use a source-supported larger/native structured state carrier.',
  'Permit an explicitly accounted side channel or a variable-length protocol, which changes this frozen test.',
  'Ideal exact real or symbolic coefficients are a different carrier from this finite JavaScript implementation.'],sourceHashes};
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,sourceSamples:undefined,sourceHashes:undefined},null,2));
