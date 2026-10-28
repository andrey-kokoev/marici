import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {GenerativeAssemblyRules} from '../demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const source='research/strominger/results/native-screw-patch/verification.json';
const r=JSON.parse(await fs.readFile(path.join(root,source),'utf8'));
const spec='research/strominger/contracts/pb208-screw-field-attempt.v1.json';
const snapshot='research/strominger/contracts/persistent-seam-pe-conjecture-net.snapshot.rev30.json';
const pre=JSON.parse(await fs.readFile(path.join(root,snapshot),'utf8')).conjectures.find(n=>n.id==='pb208-screw-field-attempt');
assert.equal(pre.status,'open');assert.equal(pre.screw_field_sewing_established,false);
for(const [p,d] of Object.entries(r.sourceHashes))assert.equal(crypto.createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex'),d);
const packets=new Map(r.packets.map(p=>[p.id,p])),charts=new Map(r.charts.map(c=>[Number(c.id.slice(6)),c])),operations=new Map(r.operations.map(o=>[o.id,o]));
const fresh=new GenerativeAssemblyRules(),mapping=new Map([[0,fresh.root]]);
for(const i of r.construction){
 const expected=operations.get(i);assert.ok(expected);const sourceId=mapping.get(expected.source);assert.notEqual(sourceId,undefined);
 const op=fresh.outgoing(sourceId).map(i=>fresh.operations[i]).find(o=>o.kind===expected.kind);assert.ok(op);fresh.validateTransfer(op);
 const p=fresh.packets[op.target],e=packets.get(expected.target),c=fresh.charts[p.chart],ec=charts.get(e.chart);
 assert.equal(p.origin,e.origin);assert.deepEqual(p.permutation,e.permutation);assert.equal(c.species,ec.species);assert.deepEqual(c.aliases,ec.aliases);
 mapping.set(expected.target,op.target);assert.equal(fresh.describe([...mapping.values()]).valid,true);
}
const audit=fresh.inspect([...mapping.values()]);assert.equal(audit.certifiedExit,true);assert.deepEqual(audit.counts,r.inspection.counts);
// Match every retained operation by semantic source/target mapping, not lazy IDs.
for(const expected of r.operations){const actual=fresh.outgoing(mapping.get(expected.source)).map(i=>fresh.operations[i]).find(o=>o.kind===expected.kind&&o.target===mapping.get(expected.target));
 assert.ok(actual);fresh.validateTransfer(actual);assert.deepEqual(actual.face,expected.face);assert.deepEqual(actual.permutation,expected.permutation);}
assert.equal(audit.links.length,r.operations.length);assert.equal(mapping.size,r.packets.length);
assert.equal(r.sparseInspection.pendingContacts.length,4);assert.equal(r.inspection.pendingContacts.length,0);
const inputs=[source,spec,snapshot,'research/strominger/checkers/export_screw_field_fixture.mjs',...Object.keys(r.sourceHashes)];
const sourceHashes={};for(const p of inputs)sourceHashes[p]=crypto.createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex');
const fixture={status:'certified-native-retained-assembly',rootPacket:0,packets:r.packets,
 charts:[...charts].map(([index,c])=>({index,...c})),cells:r.cells,operations:r.operations,audit:r.inspection,
 expectedPacketCount:r.packets.length,expectedInterfaceCount:r.operations.length,
 histories:[{kind:'construction',operations:r.construction},{kind:'walk',operations:r.walk},...r.repairs.map(x=>({kind:'contact-repair',...x}))],
 originalPackets:r.originalPackets,blocks:r.blocks,boundaries:r.boundaries,repairs:r.repairs,
 nativeReplay:{packets:mapping.size,interfaces:audit.links.length,counts:audit.counts},sourceHashes,
 scope:'Actual native screw patch, not an esd7 cell assignment or Pb isotope. Preserve source cap and non-complete intermediate-prefix limitations.'};
const dest='research/strominger/results/screw-field-fixture.json';await fs.writeFile(path.join(root,dest),JSON.stringify(fixture,null,2)+'\n');
console.log(JSON.stringify({packets:fixture.packets.length,interfaces:fixture.operations.length,exitHistories:fixture.audit.exitPackets.length,counts:fixture.audit.counts}));
