// Separate the two legs of the neutron window from inter-cell packet transfers.
import assert from 'node:assert/strict';import fs from 'node:fs';
import {GenerativeAssemblyRules,phaseFrame} from '../../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
const r=new GenerativeAssemblyRules(),ops=id=>r.outgoing(id).map(k=>r.operations[k]);
const pn=ops(r.root).find(o=>o.kind==='PN'),p=r.packets[pn.target],c=r.charts[p.chart];
const w=phaseFrame(c,p.origin).window.map(o=>o.vertex),ne=ops(pn.target).find(o=>o.kind==='NE');
const legs=[w.slice(0,2),w.slice(1)].map(e=>({onEntry:e.every(v=>pn.face.includes(v)),onExit:e.every(v=>ne.face.includes(v))}));
assert.deepEqual(legs,[{onEntry:true,onExit:false},{onEntry:true,onExit:true}]);
const o={window:w,entry:pn.face,exit:ne.face,legs};console.log(o);fs.writeFileSync(new URL('../results/pne_neutron_face_readout.json',import.meta.url),JSON.stringify(o,null,2)+'\n');
