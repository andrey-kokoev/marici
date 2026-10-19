// Four available native N readers in one octahedron; not an exit-certified assembly.
import assert from 'node:assert/strict';
import {mkdir,writeFile,readFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {phaseFrame,phaseAdvanceWitness} from '../demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const r=new GenerativeAssemblyRules(),operations=[],readers=[];
function next(id,kind){const op=r.operations[r.outgoing(id).find(i=>r.operations[i].kind===kind)];assert(op);r.validateTransfer(op);operations.push(op);return op.target;}
let id=next(r.root,'PN');
for(let origin=0;origin<4;origin++){
 const packet=r.packets[id],chart=r.charts[packet.chart],cell=r.geometry.cells[chart.cell];
 assert.equal(packet.origin,origin);
 readers.push({packet,chart,cell,frame:phaseFrame(chart,origin)});
 if(origin<3)id=next(id,'NN-phase-advance');
}
assert.equal(new Set(readers.map(x=>x.cell.id)).size,4);
const ids=[r.root,...readers.map(x=>x.packet.id)];assert(r.describe(ids).valid);
const witnesses=operations.filter(op=>op.phaseDelta===1).map(op=>phaseAdvanceWitness(r.charts[r.packets[op.source].chart],r.charts[r.packets[op.target].chart],r.packets[op.source].origin));
const root=new URL('../../../',import.meta.url),out=new URL('../results/eight-sector-readers/',import.meta.url);
const rootPacket=r.packets[r.root],rootChart=r.charts[rootPacket.chart];
const rootReader={packet:rootPacket,chart:rootChart,cell:r.geometry.cells[rootChart.cell],frame:phaseFrame(rootChart,rootPacket.origin)};
const report={schema:'marici.eight-sector-readers.v1',status:'pass',rootReader,readers,operations,witnesses,inspection:r.inspect(ids),sourceHashes:{},scope:'Available native reader contexts with absolute origins; no E exit or occupied-assembly certificate is asserted.'};
assert.equal(report.inspection.certifiedExit,false);
for(const path of ['research/strominger/checkers/export_eight_sector_readers.mjs',...['local-reference-rules','phase-advance-model','phase-discipline-model','window-construction-model','lattice-items','simplex-components'].map(n=>'research/strominger/demos/particle-overlap-tetrahedron/'+n+'.mjs')])report.sourceHashes[path]=createHash('sha256').update(await readFile(new URL(path,root))).digest('hex');
await mkdir(out,{recursive:true});await writeFile(new URL('verification.json',out),JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:'pass',readers:4,origins:readers.map(r=>r.packet.origin),certifiedExit:false}));
