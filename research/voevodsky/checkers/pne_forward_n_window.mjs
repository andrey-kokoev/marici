// Predict before expanding the canonical neutron. No E chart, target aliases or target phase frame in prediction. Compare two retained sites alone with the native neutron context rule.
import {GenerativeAssemblyRules,phaseFrame} from '../../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import fs from 'node:fs';import assert from 'node:assert/strict';
const r=new GenerativeAssemblyRules(),ops=id=>r.outgoing(id).map(k=>r.operations[k]);
const id=ops(r.root).find(op=>op.kind==='PN').target,p=r.packets[id],chart=r.charts[p.chart],f=phaseFrame(chart,p.origin);
const start=f.window[2].vertex,turn=f.context.vertex,inactive=f.window[1].vertex;
const across=r.geometry.neighbor(chart.cell,[start,inactive,turn]);
const rows=[['reader-phase-advance',chart.cell],['NN-phase-advance',across]].map(([kind,cell])=>{const ends=r.geometry.cells[cell].vertices.filter(v=>v!==start&&v!==turn);assert.equal(ends.length,2);const allowed=ends.filter(v=>v!==inactive);assert.equal(allowed.length,1);return {kind,cell,ends,predicted:[start,turn,allowed[0]]}});
assert(!r.charts.some(c=>c.species==='electron'));const next=ops(id);
for(const row of rows){const q=r.packets[next.find(op=>op.kind===row.kind).target];assert.equal(q.chart>=0,true);const actual=phaseFrame(r.charts[q.chart],q.origin).window.map(o=>o.vertex);assert.deepEqual(actual,row.predicted)}assert.notEqual(rows[0].predicted[2],rows[1].predicted[2]);console.log(rows);fs.writeFileSync(new URL('../results/pne_forward_n_window.json',import.meta.url),JSON.stringify({inactive,rows},null,2)+'\n');
