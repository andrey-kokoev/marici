// Predict from the original PN attachment only; count later on-cell reader advances, not NE transfers or NN moves.
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {GenerativeAssemblyRules} from '../../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
const r=new GenerativeAssemblyRules(),ops=id=>r.outgoing(id).map(i=>r.operations[i]);
const pn=ops(r.root).find(op=>op.kind==='PN');let id=pn.target;
const chart=id=>r.charts[r.packets[id].chart];const initial=chart(id);
const cs=r.geometry.cells[initial.cell].vertices.filter(v=>Object.entries(initial.aliases).some(([k,a])=>k.startsWith('C')&&a===v));
const inside=cs.filter(v=>pn.face.includes(v)),outside=cs.filter(v=>!pn.face.includes(v));assert.equal(inside.length,1);assert.equal(outside.length,1);
const rows=[];for(let k=0;k<=4;k++){
 const predicted=(k%2?outside:inside)[0], available=ops(id),ne=available.find(o=>o.kind==='NE');assert(ne);
 const actual=chart(ne.target).aliases.C1;assert.equal(actual,predicted);assert.equal(chart(id).cell,initial.cell);
 rows.push({advances:k,predicted,actual,origin:r.packets[ne.target].origin});if(k<4)id=available.find(o=>o.kind==='reader-phase-advance').target;
}
console.log(rows);fs.writeFileSync(new URL('../results/pne_advance_face_control.json',import.meta.url),JSON.stringify(rows,null,2)+'\n');
