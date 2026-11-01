import {mkdir,readFile,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildCellulationStep} from '../research/realization-tower/cellulation-steps.mjs';
import {createCellulation} from '../examples/normal-ray/cellulation-renderer.js';
import {renderedCellulationWitnessInput} from '../examples/normal-ray/cellulation-loop-validation.js';
import {auditShellCellOrders,auditShellFaceOrders} from '../research/realization-tower/cellulation-shell-confluence.mjs';
const reports=[];
for(let step=23;step<=26;step++){
 const model=buildCellulationStep(step),previous=createCellulation(model.previous);previous.userData.animate(Infinity,{});
 const report=auditShellCellOrders(model,renderedCellulationWitnessInput(previous),{randomTrials:64});reports.push(report);
 console.log(`Step ${step}: ${report.status}; ${report.trials} trials / ${report.uniqueCellSchedules} distinct cell schedules; differences: ${Object.keys(report.differingTrialsByField).join(', ')||'none'}`);
 console.log(`  Octahedral arrival permutations: ${report.octahedralArrivalOrders.tested} tested, ${report.octahedralArrivalOrders.conflicting} conflicts`);
 if(report.adjacentWitness)console.log(`  adjacent pair ${report.adjacentWitness.cells.join(' / ')}: ${JSON.stringify(report.adjacentWitness.firstDifference)}`);
}
const base=buildCellulationStep(22),root=createCellulation(base);root.userData.animate(Infinity,{});
const faceOrders=auditShellFaceOrders(base,renderedCellulationWitnessInput(root));
console.log(`Macro-face orders: ${faceOrders.status}; ${faceOrders.completed}/${faceOrders.tested} complete; differences: ${Object.keys(faceOrders.differingTrialsByField).join(', ')||'none'}`);
const sources=await Promise.all(['research/realization-tower/cellulation-shell-witness.mjs','research/realization-tower/cellulation-shell-confluence.mjs','research/realization-tower/cellulation-shell.mjs','research/realization-tower/cellulation-steps.mjs','examples/normal-ray/cellulation-shell-renderer.js','examples/normal-ray/cellulation-loop-validation.js'].map(async path=>({path,sha256:createHash('sha256').update(await readFile(path)).digest('hex')})));
const report={schema:'cellulation-shell-order-audit-v1',sources,status:reports.some(r=>r.status==='order-dependent')||faceOrders.status==='order-dependent'?'order-dependent':'no-counterexample-in-tested-orders',cellOrders:reports,faceOrders,limitations:['Whole-cell transactions are atomic; arbitrary interleavings inside different tetrahedral protocols are not explored.','Tetrahedral return order remains fixed by the retained source protocol.','Octahedral permutations are uniform across each plan, not independently exhaustive for every octahedron.','A passing bounded sample is not a universal confluence proof.','This checker reports conflicts; it does not alter renderer priority or choose a new conflict-resolution rule.']};
await mkdir('test-results',{recursive:true});await writeFile('test-results/cellulation-shell-confluence.json',JSON.stringify(report,null,2)+'\n');
console.log('Report: test-results/cellulation-shell-confluence.json');
// Exit 2 means a reproduced semantic conflict, not a checker crash.
if(report.status==='order-dependent')process.exitCode=2;
