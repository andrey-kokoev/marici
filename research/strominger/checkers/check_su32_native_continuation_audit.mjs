// Test existing operations only. No cochain observer or signed-to-spinor encoder.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSulfur32Wiring,groupSulfurPayloads,restoreSulfurPayloads} from '../../realization-tower/sulfur-32-wiring.mjs';
import {sulfur32Process} from '../../realization-tower/sulfur-32-process.mjs';
import {buildSulfurIncomingBundle} from '../../realization-tower/sulfur-32-incoming-bundle.mjs';
import {GenerativeAssemblyRules,applyPhasePermutation} from '../../nima/generative-phase-assembly.mjs';
import {spectralReadout} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,reconcileBothOrders,readRecords} from '../su32-layer4-comparison.mjs';
const clone=x=>structuredClone(x),sorted=rows=>clone(rows).sort((a,b)=>a.wire.localeCompare(b.wire));
const fixturePath='research/strominger/results/su32-hopf-tests-v1/fixture.json';
const fixture=JSON.parse(await fs.readFile(fixturePath,'utf8'));
for(const [p,h] of Object.entries(fixture.sourceHashes))assert.equal(createHash('sha256').update(await fs.readFile(p)).digest('hex'),h);
const atlas=buildSu32SignedReferenceAtlas(fixture),layout=comparisonLayout(atlas,fixture,atlas.charts[0].id,[0,0]);
const records={'P+':{value:1},'P-':{value:2},'E+':{value:3},'E-':{value:4}};
const target=reconcileBothOrders(layout,records);
assert.deepEqual(readRecords(layout,target.byE),readRecords(layout,target.byP));
assert.deepEqual(target.byE.anchor,target.byP.anchor);assert.equal(target.byE.at,target.byP.at);
assert.notDeepEqual(target.byE.children,target.byP.children);

// These rows are a generic test of the existing 64-wire interface, NOT an
// asserted adapter from four signed records to 64 wires.
const model=buildSulfur32Wiring();assert.equal(model.wires.length,64);
const rows=sorted(model.wires.map((w,i)=>({wire:w.id,payload:{index:i,coefficients:[i,-i],context:{retained:true}}})));
let commandWords=0,commandSteps=0;
function replay(word){
 let state=clone(rows);
 for(const direction of word){
  state=restoreSulfurPayloads(groupSulfurPayloads(model,state,direction));
  assert.deepEqual(state,rows);commandSteps++;
 }
 commandWords++;
}
for(let n=0;n<=6;n++)for(let bits=0;bits<2**n;bits++)replay(Array.from({length:n},(_,i)=>(bits>>i)&1?'E|P':'P|E'));
assert.throws(()=>groupSulfurPayloads(model,rows.slice(1)),/Every wire payload/);
const duplicate=clone(rows);duplicate[0]=clone(duplicate[1]);
assert.throws(()=>groupSulfurPayloads(model,duplicate),/Every wire payload/);
const changed=clone(rows);changed[0].payload.coefficients[0]+=1;
assert.notDeepEqual(restoreSulfurPayloads(groupSulfurPayloads(model,changed)),rows);
// A raw output inequality obtained merely by carrying route tags is NOT a detector.
const left=rows.map(r=>({...clone(r),auditHistory:['left']}));
const right=rows.map(r=>({...clone(r),auditHistory:['right']}));
const lout=restoreSulfurPayloads(groupSulfurPayloads(model,left,'P|E'));
const rout=restoreSulfurPayloads(groupSulfurPayloads(model,right,'P|E'));
assert.notDeepEqual(lout,rout);
const erase=xs=>xs.map(({auditHistory,...r})=>r);
assert.deepEqual(erase(lout),erase(rout));assert.deepEqual(erase(lout),rows);
// The target packets do not satisfy this interface as-is. This is not a theorem
// that an encoding is impossible; no such encoding is supplied by these APIs.
assert.throws(()=>groupSulfurPayloads(model,Object.entries(records).map(([wire,payload])=>({wire,payload}))),/Every wire payload/);
assert.equal(sulfur32Process(7,1).canAdvance,false);
assert.throws(()=>sulfur32Process(7,2),/stages/);

// Existing incoming-bundle endpoint paths differ, but so do their preparations.
const bundle=buildSulfurIncomingBundle(),endpointControls=[];
for(const p of ['+','-'])for(const e of ['+','-']){
 const family=bundle.strands.filter(s=>s.polarities.p===p&&s.polarities.e===e);
 assert.equal(family.length,4);
 assert.equal(new Set(family.map(s=>s.inputSlot)).size,4);
 assert.equal(new Set(family.map(s=>s.outputSlot)).size,4);
 endpointControls.push({p,e,inputs:family.map(s=>s.inputSlot),outputs:family.map(s=>s.outputSlot),
  disposition:'Not a matched-preparation or closed-cycle witness; a,b are independent route choices in this candidate.'});
}

// Positive control: a genuinely preexisting coefficient observer can detect
// retained context. It is NOT typed on the four signed Su-32 record packets.
const rules=new GenerativeAssemblyRules();
const pn=rules.outgoing(rules.root).map(i=>rules.operations[i]).find(o=>o.kind==='PN');assert(pn);
const advance=rules.outgoing(pn.target).map(i=>rules.operations[i]).find(o=>o.kind==='reader-phase-advance');assert(advance);
assert(rules.validateTransfer(advance));
const a=[[1,0],[2,0],[3,0],[4,0],[5,0]],b=clone(a);b[4]=[6,0];
const beforeA=spectralReadout('neutron',a),beforeB=spectralReadout('neutron',b);
assert.deepEqual(beforeA.components,beforeB.components);
assert.notDeepEqual(beforeA.complement,beforeB.complement);
const advancedA=applyPhasePermutation(a,advance.permutation),advancedB=applyPhasePermutation(b,advance.permutation);
const afterA=spectralReadout('neutron',advancedA),afterB=spectralReadout('neutron',advancedB);
assert.notDeepEqual(afterA.components,afterB.components);
assert.deepEqual(afterA.slots.map(i=>advancedA[i]),[[4,0],[5,0],[2,0]]);
assert.deepEqual(afterB.slots.map(i=>advancedB[i]),[[4,0],[6,0],[2,0]]);
assert.throws(()=>applyPhasePermutation([[1,0],[2,0],[3,0],[4,0]],advance.permutation),/five-slot/);
// Equal complete native coefficient packets remain equal under the same command.
assert.deepEqual(spectralReadout('neutron',applyPhasePermutation(a,advance.permutation)),
                 spectralReadout('neutron',applyPhasePermutation(clone(a),advance.permutation)));
const sourcePaths=[fixturePath,
 'research/realization-tower/sulfur-32-wiring.mjs','research/realization-tower/sulfur-32-process.mjs',
 'research/realization-tower/sulfur-32-incoming-bundle.mjs','research/realization-tower/sulfur-32-handlebody.mjs',
 'research/realization-tower/sulfur-32-tubes-path-audit.mjs','research/strominger/checkers/check_sulfur32_middle_layer.mjs',
 'research/nima/generative-phase-assembly.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs',
 'research/strominger/su32-layer4-comparison.mjs','research/strominger/su32-signed-reference-encoder.mjs',
 'research/strominger/checkers/check_su32_native_continuation_audit.mjs'];
const hashes={};for(const p of sourcePaths)hashes[p]=createHash('sha256').update(await fs.readFile(p)).digest('hex');
const report={schema:'su32.native-continuation-audit.v1',passed:true,
 classification:'no admitted Su-32 route discriminator in audited interfaces; coefficient-context positive control is a different carrier',
 conjectureStatus:'not verified and not universally falsified; target test blocked at missing typed continuation binding',
 target:{anchor:layout.anchor,at:target.byE.at,byE:target.byE,byP:target.byP,decodedRecordsEqual:true,derivationsDifferent:true},
 wireInterface:{wireCount:64,commandWords,commandSteps,maximumWordLength:6,
  sourceArgument:'group stores each row once by fixed wire id; restore flattens and sorts those same rows. Each closed regroup/restore command is identity on valid wire-indexed row families (array presentation is canonically sorted), so every finite word is identity on those assignments.',
  doesNotEstablish:'No binding from four signed records or their reconciliation routes to these 64 rows.'},
 rejectedFalsePositives:{historyTagOnly:'Raw output inequality disappears after erasing only the carried audit tag.',differentInitialLanes:endpointControls},
 nativeCoefficientControl:{operation:advance,sourcePacket:rules.packets[advance.source],targetPacket:rules.packets[advance.target],
  beforeActiveEqual:true,fullPacketsEqual:false,afterActiveA:afterA.slots.map(i=>advancedA[i]),afterActiveB:afterB.slots.map(i=>advancedB[i]),
  readout:'spectralReadout(neutron, applyPhasePermutation(value, actual-reader-permutation))',
  disposition:'Real preexisting context-sensitive continuation, but not a witness for equal four-record Su-32 routes; no signed-record/native-chart coefficient adapter.'},
 residuals:['No native continuation accepting the two layer4 reconciliation packets was found in the audited source interfaces.',
  'A valid witness needs a source-defined embedding preserving occurrence, geometric frame, full coefficients and equal preparation; arbitrary padding or path-selected embeddings are not admitted.',
  'No cochain model or newly invented detector was used; no search over all possible future native operations is claimed.'],
 sourceHashes:hashes};
const dir='research/strominger/results/su32-native-continuation-audit-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,target:undefined,sourceHashes:undefined},null,2));
