// Executes the registered inventory-bridge attempt; no new inventory law.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {GenerativeAssemblyRules,applyBatch} from '../native-retained-batch-attempt.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const registration='research/strominger/contracts/pb208-inventory-fibration-attempt.v1.json';
const snapshot='research/strominger/contracts/persistent-seam-pe-conjecture-net.snapshot.rev24.json';
const out='research/strominger/results/pb208-inventory-fibration';
const checks=[];function check(name,fn){fn();checks.push(name);}
const registered=JSON.parse(await fs.readFile(path.join(root,registration),'utf8'));
const pre=JSON.parse(await fs.readFile(path.join(root,snapshot),'utf8'));
check('attempt exists in the pre-execution net snapshot with no established bridge',()=>{
 const n=pre.conjectures.find(n=>n.id==='pb208-inventory-fibration-attempt');
 assert.equal(n.status,'open');assert.equal(n.registration_before_execution,true);assert.equal(n.inventory_bridge_established,false);
 assert.ok(n.evidence.includes(registration));assert.equal(registered.parentTask,'pb208-retained-native-construction');
});
const r=new GenerativeAssemblyRules();
const pn=r.outgoing(r.root).map(i=>r.operations[i]).find(o=>o.kind==='PN');
const outgoing=r.outgoing(pn.target).map(i=>r.operations[i]);
const ne=outgoing.find(o=>o.kind==='NE'),nn=outgoing.find(o=>o.kind==='NN-phase-advance');
const E=applyBatch(r,[r.root,pn.target],[ne.id]),N=applyBatch(r,[r.root,pn.target],[nn.id]);
const rows=state=>[...r.describe(state.packets).bodies].map(([cell,species])=>({label:species,from:r.geometry.cells[cell].key,to:r.geometry.cells[cell].key})).sort((a,b)=>a.from.localeCompare(b.from));
const eRows=rows(E),nRows=rows(N);
const inventory=rows=>Object.fromEntries(['proton','neutron','electron'].map(s=>[s,rows.filter(r=>r.label===s).length]));
const recover=(row,depth)=>{for(let i=0;i<depth;i++)row=row.previous;return row;};
const canonical=rows=>JSON.stringify([...rows].sort((a,b)=>a.from.localeCompare(b.from)));
function tower(initial){
 let current=initial;const stages=[];
 for(let depth=0;depth<8;depth++){
  const field=['label','from','to'][depth%3],fibers=new Map();
  for(const row of current){const key=recover(row,depth)[field];if(!fibers.has(key))fibers.set(key,[]);fibers.get(key).push(row);}
  const next=[...fibers].flatMap(([key,fiber])=>fiber.map(previous=>({field,key,previous})));
  check(`retained total ${initial===eRows?'E':'N'} depth${depth+1} preserves records, keys and inventory`,()=>{
   assert.equal(next.length,initial.length);
   for(const item of next)assert.equal(recover(item.previous,depth)[field],item.key);
   assert.equal(canonical(next.map(row=>recover(row,depth+1))),canonical(initial));
   assert.deepEqual(inventory(next.map(row=>recover(row,depth+1))),inventory(initial));
  });
  stages.push({field,inventory:inventory(next.map(row=>recover(row,depth+1))),rows:next.length});current=next;
 }
 return {stages,final:current};
}
check('body table convention reproduces the unchanged native composition reader',()=>{
 assert.deepEqual(inventory(eRows),E.inspection.counts);assert.deepEqual(inventory(nRows),N.inspection.counts);
 assert.deepEqual(eRows.map(r=>r.from),nRows.map(r=>r.from));
});
const eTower=tower(eRows),nTower=tower(nRows);
const permutations=xs=>xs.length?xs.flatMap((x,i)=>permutations(xs.filter((_,j)=>i!==j)).map(rest=>[x,...rest])):[[]];
const trials=permutations([0,1,2]).map(p=>({permutation:p,labelsPreserved:eRows.every((row,i)=>row.label===nRows[p[i]].label),geometryPreserved:eRows.every((row,i)=>row.from===nRows[p[i]].from)}));
check('all six row bijections fail species preservation, including geometry identity',()=>{
 assert.equal(trials.length,6);assert.equal(trials.filter(t=>t.labelsPreserved).length,0);assert.equal(trials.filter(t=>t.geometryPreserved).length,1);
});
check('retained membership paths do not turn different field values into equal inventory',()=>{
 assert.notDeepEqual(eTower.stages.at(-1).inventory,nTower.stages.at(-1).inventory);
});
const value=[2,3,5,7,11];
const coefficientRecovery=op=>{const p=r.packets[op.target].permutation;const v=p.map(i=>value[i]);return p.map((_,i)=>v[p.indexOf(i)]);};
check('coefficient recovery forgets the inventory distinction',()=>{
 assert.deepEqual(coefficientRecovery(ne),value);assert.deepEqual(coefficientRecovery(nn),value);
 assert.notDeepEqual(inventory(eRows),inventory(nRows));
});
check('freezing the seed or PN inventory fails the existing native reader',()=>{
 const prior=r.inspect([r.root,pn.target]);assert.notDeepEqual(prior.counts,E.inspection.counts);assert.notDeepEqual(prior.counts,N.inspection.counts);
});
const artifact={registration,preExecutionSnapshot:snapshot,criterionDisposition:'candidate-insufficient-for-inventory-bridge',
 sourceConvention:'Occupied primitive row: species label, canonical cell as both identity endpoints. Finite test convention, not a new native arrow.',
 sourceRows:{electron:eRows,neutron:nRows},retainedTowers:{electron:eTower,neutron:nTower},bijectionTrials:trials,
 recoveredRootCoefficients:{electron:coefficientRecovery(ne),neutron:coefficientRecovery(nn)},
 inventoryBridgeEstablished:false,retainedTotalRecoveryPassed:true,genericFibrationRefuted:false,allWholeAssemblyModelsRefuted:false,
 fullPbConstructionEstablished:false,
 missingDatum:'The source fibration preserves a supplied inventory; it does not construct a cross-alternative inventory/carrier identification. A separately grounded retained-whole object and its particle reader are still required.'};
await fs.mkdir(path.join(root,out),{recursive:true});await fs.writeFile(path.join(root,out,'attempt.json'),JSON.stringify(artifact,null,2)+'\n');
const priorReceipt='research/strominger/results/native-reader-comparison/verification.json';
const prior=JSON.parse(await fs.readFile(path.join(root,priorReceipt),'utf8'));
for(const [p,d] of Object.entries(prior.sourceHashes))assert.equal(crypto.createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex'),d,'stale input '+p);
const inputs=[registration,snapshot,registered.candidateSource,registered.candidateKernel,'research/nima/checkers/check_label_from_to_fibration_tower.py',priorReceipt,...Object.keys(prior.sourceHashes),
 'research/strominger/checkers/check_pb208_inventory_fibration.mjs','research/strominger/pb208-inventory-fibration-result-v1.md',out+'/attempt.json'];
const sourceHashes={};for(const p of inputs)sourceHashes[p]=crypto.createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex');
const report={status:'passed',check_count:checks.length,checks,criterionDisposition:artifact.criterionDisposition,
 inventoryBridgeEstablished:false,retainedTotalRecoveryPassed:true,genericFibrationRefuted:false,allWholeAssemblyModelsRefuted:false,fullPbConstructionEstablished:false,sourceHashes};
await fs.writeFile(path.join(root,out,'verification.json'),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:report.status,checks:checks.length,criterionDisposition:report.criterionDisposition}));
