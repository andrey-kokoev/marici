// Search/recovery audit only. Do not rewrite the historical spectral receipt
// or silently repair the current Pb geometry to make it pass this contract.
import assert from 'node:assert/strict';
import {readFile,mkdir,writeFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {trial} from '../demos/particle-overlap-tetrahedron/carrier.mjs';
import {lead208Chains} from '../demos/particle-overlap-tetrahedron/lead208-model.mjs';
const intersection=(a,b)=>a.filter(x=>b.includes(x)),setKey=a=>[...a].sort().join('|');
const [p,n,e]=trial.bodies;
assert.deepEqual(p.nodes,['C0','M0','C1','M1']);assert.deepEqual(n.nodes,['M0','C1','M1','C2']);assert.deepEqual(e.nodes,['M1','C1','C2','M2']);
assert.deepEqual(intersection(p.nodes,n.nodes),['M0','C1','M1']);
assert.deepEqual(e.window,['M1','C1','C2']);assert.deepEqual(n.window.slice(-2),e.window.slice(0,2).reverse());
const eligible=n.nodes.map(omit=>({omit,face:n.nodes.filter(id=>id!==omit)})).filter(f=>setKey(f.face)===setKey(e.window));
assert.equal(eligible.length,1);assert.equal(eligible[0].omit,'M0');
const retainedEdge=intersection(intersection(p.nodes,n.nodes),e.window);assert.deepEqual(retainedEdge,['C1','M1']);
const receiptPath='research/strominger/results/cmc-mcm-identity-attachment/verification.json';
const receipt=JSON.parse(await readFile(receiptPath,'utf8')),sourceHashes=[];
for(const [file,expected] of Object.entries(receipt.source_sha256)){
 const actual=createHash('sha256').update(await readFile(file)).digest('hex');sourceHashes.push({file,matches:actual===expected});
}
assert.equal(receipt.status,'pass');
assert.equal(receipt.transitions[0].mode_transport.positive.target_mode,'positive');
assert.equal(receipt.transitions[1].mode_transport.positive.target_mode,'negative');
assert.equal(receipt.checks.NE_same_forward_cycle_square_rejected,true);
const rows=lead208Chains.map(c=>{
 const incoming=c.protonNeutronFace.map(p=>p.join(',')),outgoing=c.neutronElectronFace.map(p=>p.join(','));
 const shared=intersection(incoming,outgoing);
 return {chain:c.id,sharedVertices:shared.length,passesNecessaryRetainedEdgeCondition:shared.length===2};
});
const histogram={};rows.forEach(r=>histogram[r.sharedVertices]=(histogram[r.sharedVertices]??0)+1);
const report={status:'audit-completed',sourceWindowRecovered:true,sourceFace:e.window,omittedNeutronVertex:'M0',retainedEdge,edgeReversal:{neutron:n.window.slice(-2),electron:e.window.slice(0,2)},
 historicalReceipt:{path:receiptPath,recordedAt:receipt.recorded_at,sourceHashes,allSourcesStillMatch:sourceHashes.every(r=>r.matches),modeTransfers:receipt.transitions.map(t=>({from:t.from,to:t.to,positive:t.mode_transport.positive,cycle:t.cyclic_target_convention}))},
 currentPbLayout:{compatibleChains:rows.filter(r=>r.passesNecessaryRetainedEdgeCondition).length,totalChains:rows.length,faceIntersectionHistogram:histogram,rows},
 scope:'The marked carrier protocol selects the N face M1/C1/C2 and its order. The current Pb layout is audited against a necessary incidence condition, not certified as window-compatible. This does not derive a native physical operator or a lattice-wide marking for composite neutron gaps.'};
const out='research/strominger/results/window-attachment-recovery';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({sourceWindowRecovered:true,face:report.sourceFace,sourceHashesMatch:report.historicalReceipt.allSourcesStillMatch,currentPbCompatibleChains:report.currentPbLayout.compatibleChains,total:rows.length,histogram,disposition:report.currentPbLayout.compatibleChains===rows.length?'necessary-incidence-condition-passes':'current-Pb-window-incidence-rejected'},null,2));
