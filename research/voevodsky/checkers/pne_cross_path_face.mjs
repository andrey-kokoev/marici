// Compare a marked neutron on a longer reading with an electron on the short one via their shared neutron packet. Do not identify joined-word positions by matching phase triples.
import fs from 'node:fs';
import assert from 'node:assert/strict';
import {enumerateAssemblies,phaseFrame} from '../../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {auditPhaseCombination} from '../../strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';
const result=name=>new URL(`../results/${name}.json`,import.meta.url);
const {rows}=JSON.parse(fs.readFileSync(result('pne_selected_path_balance')));
const pick=seq=>rows.find(r=>String(r.seq)===String(seq));
const short=pick(['PN','NE']),long=pick(['PN','reader-phase-advance','NE']);
const run=enumerateAssemblies({maxTransitions:4,maxStates:50000});
assert(run.complete);assert.deepEqual(short.ids.slice(0,2),long.ids.slice(0,2));
const frame=id=>{const p=run.packets[id];return phaseFrame(run.charts[p.chart],p.origin)};
const n=frame(long.ids[1]),e=frame(short.ids[2]);
const op=run.operations.find(o=>o.source===long.ids[1]&&o.target===short.ids[2]&&o.kind==='NE');assert(run.rules.validateTransfer(op));
const link={from:n.id,to:e.id,kind:'NE',identification:'same-occurrence',vertices:e.window.map(o=>o.vertex)};
const audit=l=>auditPhaseCombination([n,e],[l]).status;
const admitted=audit(link),unmarked=audit({...link,identification:null});assert.equal(admitted,'native-phase-compatible');assert.notEqual(unmarked,admitted);
const marks=e.window.map((target,j)=>{
 const i=[...n.window,n.context].findIndex(x=>x.vertex===target.vertex);assert.deepEqual([...n.window,n.context][i],target);
 const at=(r,k,s)=>r.overlap.slice(0,k).reduce((a,b)=>a+3-b,0)+s;
 return {role:target.role,index:target.index,vertex:target.vertex,longNeutron:i===3?'context':at(long,1,i),shortElectron:at(short,2,j)};
});
const out={short:short.ids,long:long.ids,operation:op.kind,admitted,unmarked,marks};console.log(out);fs.writeFileSync(result('pne_cross_path_face'),JSON.stringify(out,null,2)+'\n');
