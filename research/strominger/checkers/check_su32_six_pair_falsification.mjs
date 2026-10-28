// Exhaustive falsification attempt for a stated conditional six-pair task.
// Uses the complete fixed-reading incidence covers, never local path extension.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSu32SignedReferenceAtlas} from '../su32-signed-reference-encoder.mjs';
import {comparisonLayout,reconcileBothOrders} from '../su32-layer4-comparison.mjs';
const input='research/strominger/results/su32-fixed-reading-trace-v1/verification.json';
const trace=JSON.parse(await fs.readFile(input,'utf8'));
for(const [p,h] of Object.entries(trace.sourceHashes))assert.equal(createHash('sha256').update(await fs.readFile(p)).digest('hex'),h,`Stale trace: ${p}`);
const labels=['P+','P-','E+','E-'];
const pairs=labels.flatMap((a,i)=>labels.slice(i+1).map(b=>[a,b]));assert.equal(pairs.length,6);
const assignments=[];
function enumerate(prefix,remaining){if(!remaining.length){assignments.push(prefix);return;}for(const i of remaining)enumerate([...prefix,i],remaining.filter(j=>j!==i));}
enumerate([],pairs.map((_,i)=>i));assert.equal(assignments.length,720);
const contains=(support,pair)=>pair.every(k=>support.includes(k));
const payloads=node=>Object.fromEntries(Object.entries(node.records).map(([k,v])=>[k,v.payload]));
const views=new Map(trace.layer4.map(x=>[x.cell,x.operand]));
const results=[];let recoveryChecks=0;
for(const cover of trace.middleAssignments){
 const routes=cover.routes;
 const jointAllowed=routes.map(r=>pairs.flatMap((pair,i)=>contains(r.availableRecordLabels,pair)?[i]:[]));
 const eitherAllowed=routes.map(r=>pairs.flatMap((pair,i)=>contains(r.sourcePSupport,pair)&&contains(r.sourceESupport,pair)?[i]:[]));
 const solve=allowed=>assignments.filter(choice=>choice.every((pair,i)=>allowed[i].includes(pair)));
 const joint=solve(jointAllowed),either=solve(eitherAllowed);
 // Neither native E view contains both P records, and neither P view both E.
 // Therefore either-operand reconstruction of all six pairs is impossible.
 assert(routes.every(r=>!contains(r.sourceESupport,['P+','P-'])));
 assert(routes.every(r=>!contains(r.sourcePSupport,['E+','E-'])));
 assert.equal(either.length,0);
 // For every surviving JOINT assignment, materialize a conditional information
 // codec. Retain the offered operands verbatim; do not pretend this is a native
 // middle operation or a transfer to layer6/outgoing N.
 for(const choice of joint){
  const packed=routes.map((r,i)=>{
   const left=structuredClone(views.get(r.sourceP)),right=structuredClone(views.get(r.sourceE));
   const values={...payloads(left),...payloads(right)};
   for(const k of r.sharedRecordLabels)assert.deepEqual(payloads(left)[k],payloads(right)[k]);
   return {channel:r.channel,active: Object.fromEntries(pairs[choice[i]].map(k=>[k,values[k]])),
    context:Object.fromEntries(Object.entries(values).filter(([k])=>!pairs[choice[i]].includes(k))),
    retainedOperands:{left,right}};
  });
  const replay=JSON.parse(JSON.stringify(packed)),recovered={};
  for(let i=0;i<routes.length;i++){
   assert.deepEqual(replay[i].retainedOperands.left,views.get(routes[i].sourceP));
   assert.deepEqual(replay[i].retainedOperands.right,views.get(routes[i].sourceE));
   for(const [k,v] of Object.entries({...replay[i].active,...replay[i].context})){
    if(Object.hasOwn(recovered,k))assert.deepEqual(recovered[k],v);else recovered[k]=v;
   }
  }
  assert.deepEqual(recovered,trace.registry);recoveryChecks++;
 }
 // Small Hall obstruction: these two required pairs have no eligible channel
 // in the either-operand task. Each singleton already violates Hall's bound.
 const impossiblePairs=pairs.filter((_,p)=>eitherAllowed.every(xs=>!xs.includes(p)));
 assert(impossiblePairs.some(p=>JSON.stringify(p)===JSON.stringify(['P+','P-'])));
 assert(impossiblePairs.some(p=>JSON.stringify(p)===JSON.stringify(['E+','E-'])));
 results.push({cover:cover.index,channels:routes.map(r=>r.channel),jointAllowed,eitherAllowed,
  jointSolutions:joint.length,eitherOperandSolutions:either.length,impossibleEitherOperandPairs:impossiblePairs,
  jointAssignments:joint,examples:joint.slice(0,2).map(choice=>routes.map((r,i)=>({channel:r.channel,pair:pairs[choice[i]],
   context:r.availableRecordLabels.filter(k=>!pairs[choice[i]].includes(k))})))});
}
// Concrete non-reconstruction witness for the stronger task, with all other
// record values fixed. An E view missing P- cannot recover the pair (P+,P-).
const ppWitness=trace.middleAssignments[0].routes.find(r=>r.sourceESupport.includes('P+')&&!r.sourceESupport.includes('P-'));
assert(ppWitness);
const a=Object.fromEntries(labels.map(k=>[k,0])),b={...a,'P-':1};
const select=(r,ks)=>Object.fromEntries(ks.map(k=>[k,r[k]]));
assert.deepEqual(select(a,ppWitness.sourceESupport),select(b,ppWitness.sourceESupport));
assert.notDeepEqual(select(a,['P+','P-']),select(b,['P+','P-']));
// Confirm indistinguishability of the COMPLETE existing operand trees, not
// just an invented projection that might have discarded distinguishing data.
const fixture=JSON.parse(await fs.readFile('research/strominger/results/su32-hopf-tests-v1/fixture.json','utf8'));
const atlas=buildSu32SignedReferenceAtlas(fixture),anchor=trace.centralReconciliation.byE.anchor;
const layout=comparisonLayout(atlas,fixture,anchor.chartId,anchor.binding);
function actualOperand(cell,records){
 const result=reconcileBothOrders(layout,records),row=trace.layer4.find(x=>x.cell===cell);assert(row);
 return row.kind==='outer-single-channel-view'?result.channels[row.inputCells[0]]:result.comparisons.find(c=>c.at===cell);
}
let fullOperandCounterexamples=0;
for(const cover of trace.middleAssignments)for(const r of cover.routes)for(const [side,pair] of [['sourceE',['P+','P-']],['sourceP',['E+','E-']]]){
 const support=side==='sourceE'?r.sourceESupport:r.sourcePSupport,missing=pair.find(k=>!support.includes(k));assert(missing);
 const changed={...a,[missing]:1};
 assert.deepEqual(actualOperand(r[side],a),actualOperand(r[side],changed));
 assert.notDeepEqual(select(a,pair),select(changed,pair));fullOperandCounterexamples++;
}
const report={schema:'su32.six-pair-falsification.v1',passed:true,
 hypothesis:'Conditional interpretation: the six outputs are all unordered pairs of P+,P-,E+,E-. This interpretation is not promoted to a native requirement.',
 sourceReading:trace.reading,signBinding:trace.binding,pairs,permutationsPerCover:assignments.length,
 completeCovers:results.length,assignmentsTestedPerAccessModel:assignments.length*results.length,recoveryChecks,fullOperandCounterexamples,
 tasks:{joint:'The active pair must be available in the union of both offered operands. Other records and both derivations may be retained as context.',
 eitherOperand:'The same active pair must be independently reconstructible from each existing P-side and E-side operand, without communication or extra state.'},
 results,nonReconstructionWitness:{channel:ppWitness.channel,EView:ppWitness.sourceESupport,inputA:a,inputB:b,pair:['P+','P-']},
 verdict:{jointExistence:results.some(r=>r.jointSolutions>0)?'survives this necessary information-level test':'falsified within all four tested covers',
 labelledJointUniqueness:results.reduce((n,r)=>n+r.jointSolutions,0)>1?'falsified: multiple assignments on fixed labelled channels; no symmetry quotient tested':'not falsified',
 eitherOperandExistence:'falsified within these covers; same-role pairs cannot be recovered independently from the opposite-role offered views'},
 limits:['Joint solutions are conditional active/context labellings, not native signal transformations.',
 'The information codec retains full original operands; its reversibility does not establish a physical reversible wiring.',
 'No layer6 or outgoing-N record map is supplied. No central reconciliation-to-periphery communication is added.',
 'The stronger either-operand condition is a rival hypothesis, not inferred merely from P/E duality.',
 'No zero-context, fixed capacity, preferred pairing, circular order or phase law is assumed.'],
 sourceHashes:{[input]:createHash('sha256').update(await fs.readFile(input)).digest('hex'),
  'research/strominger/checkers/check_su32_six_pair_falsification.mjs':createHash('sha256').update(await fs.readFile('research/strominger/checkers/check_su32_six_pair_falsification.mjs')).digest('hex')}};
const dir='research/strominger/results/su32-six-pair-falsification-v1';await fs.mkdir(dir,{recursive:true});
await fs.writeFile(dir+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({...report,results:results.map(({jointAssignments,examples,...r})=>r),sourceHashes:undefined},null,2));
