// Canonical direct PN route. Make the prediction before requesting N's outgoing operations. No face order, numeric indices, or target marks in the selector.
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {GenerativeAssemblyRules} from '../../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
const r=new GenerativeAssemblyRules();
const ops=id=>r.outgoing(id).map(i=>r.operations[i]);
const pn=ops(r.root).find(o=>o.kind==='PN');
const n=r.charts[r.packets[pn.target].chart];
assert(!r.charts.some(c=>c.species==='electron'));
const kinds=new Map(Object.entries(n.aliases).map(([name,v])=>[v,name[0]]));
const incomingC=pn.face.filter(v=>kinds.get(v)==='C');assert.equal(incomingC.length,1);
const predicted=incomingC[0];
const ne=ops(pn.target).find(o=>o.kind==='NE');const target=r.charts[r.packets[ne.target].chart];
assert.equal(predicted,target.aliases.C1);assert(!pn.face.includes(target.aliases.C2));
const o={incoming:pn.face,predicted,actualC1:target.aliases.C1,actualC2:target.aliases.C2};console.log(o);fs.writeFileSync(new URL('../results/pne_pre_e_face.json',import.meta.url),JSON.stringify(o,null,2)+'\n');
