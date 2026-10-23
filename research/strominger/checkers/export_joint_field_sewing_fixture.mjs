// A retained simultaneous assembly from the prior native holonomy witness.
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const source='research/strominger/results/window-combination-coherence/verification.json';
const previous=JSON.parse(await fs.readFile(path.join(root,source),'utf8'));
const witness=previous.coefficientFrameHolonomyExamples.find(w=>w.paths[0].word.length===3&&w.paths.every(p=>p.retainedCombinationAudit.allContactsWitnessed));
assert(witness);assert.deepEqual(witness.marking,[0,1,2,3]);
const rules=new GenerativeAssemblyRules(),retained=new Set([rules.root]),histories=[],comparisonPackets=[];
for(const p of witness.paths){
 let active=rules.root;const packets=[active],operations=[];
 for(const [i,kind] of [...p.word,'PN','NE'].entries()){
  const op=rules.outgoing(active).map(i=>rules.operations[i]).find(o=>o.kind===kind);
  assert(op);assert(rules.validateTransfer(op));operations.push(op.id);active=op.target;
  retained.add(active);packets.push(active);
  if(i===p.word.length-1){comparisonPackets.push(active);assert.deepEqual(rules.packets[active].permutation,p.permutation);}
 }
 histories.push({word:[...p.word,'PN','NE'],packets,operations});
}
const ids=[...retained],audit=rules.inspect(ids);
assert(audit.valid&&audit.certifiedExit&&audit.allContactsWitnessed&&audit.allPacketsCanReachExit&&audit.allCellsOnEntryExitPaths);
assert.equal(audit.pendingContacts.length,0);
const [p,q]=comparisonPackets.map(i=>rules.packets[i]);
assert.equal(p.chart,q.chart);assert.equal(p.origin,q.origin);assert.notDeepEqual(p.permutation,q.permutation);
const packets=ids.map(i=>rules.packets[i]);
const charts=[...new Set(packets.map(p=>p.chart))].map(i=>({index:i,...rules.charts[i]}));
const operations=audit.links.map(i=>rules.operations[i]); // All retained links, not only the generating paths.
const cells=[...new Set(charts.map(c=>c.cell))].map(i=>rules.geometry.cells[i]);
const sourcePaths=[source,'research/nima/generative-phase-assembly.mjs','research/strominger/checkers/export_joint_field_sewing_fixture.mjs'];
const sourceHashes=Object.fromEntries(await Promise.all(sourcePaths.map(async p=>[p,createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex')])));
const out={status:'certified-native-retained-assembly',rootPacket:rules.root,packets,charts,cells,operations,histories,comparisonPackets,audit,sourceHashes,
 scope:'One contact-certified retained construction-map assembly, not simultaneous cloned physical particles. Two prior holonomy histories plus their native PN,NE exits. Full field sewing is checked separately.'};
const dest=path.join(root,'research/strominger/results/joint-field-sewing-fixture.json');
await fs.writeFile(dest,JSON.stringify(out,null,2)+'\n');
console.log(JSON.stringify({status:out.status,packets:packets.length,interfaces:operations.length,bodies:audit.counts,exits:audit.exitPackets.length,result:dest}));
