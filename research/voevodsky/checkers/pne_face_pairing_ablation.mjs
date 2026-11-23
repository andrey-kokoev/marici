// Enumerate bijections before applying any identification. Target slots active; source slots on the actual common geometric face, context included.
import {enumerateAssemblies,phaseFrame} from '../../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import assert from 'node:assert/strict';
import fs from 'node:fs';
const run=enumerateAssemblies({maxTransitions:2,maxStates:500});assert(run.complete);
const op=run.operations.find(o=>o.kind==='NE' && run.operations.some(p=>p.kind==='PN'&&p.source===run.rules.root&&p.target===o.source));
const frame=id=>{const p=run.packets[id];return phaseFrame(run.charts[p.chart],p.origin)};
const n=frame(op.source),e=frame(op.target),src=[...n.window,n.context].filter(s=>op.face.includes(s.vertex)),dst=e.window;
assert.equal(src.length,3);assert.equal(dst.length,3);
const cases=[];for(const i of [0,1,2])for(const j of [0,1,2])if(i!==j){const p=[i,j,3-i-j];cases.push({map:p.map(k=>src[k].role+src[k].index),role:p.every((k,t)=>src[k].role===dst[t].role),vertex:p.every((k,t)=>src[k].vertex===dst[t].vertex),phase:p.every((k,t)=>src[k].role===dst[t].role&&src[k].index===dst[t].index)})}
const counts=Object.fromEntries(['role','vertex','phase'].map(key=>[key,cases.filter(c=>c[key]).length]));assert.deepEqual(counts,{role:2,vertex:1,phase:1});assert.deepEqual(cases.find(c=>c.vertex),cases.find(c=>c.phase));
const out={target:dst.map(x=>x.role+x.index),counts,cases};console.log(out);fs.writeFileSync(new URL('../results/pne_face_pairing_ablation.json',import.meta.url),JSON.stringify(out,null,2)+'\n');
