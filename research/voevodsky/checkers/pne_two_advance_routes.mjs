// Canonical PN then zero to four neutron advances (both kinds), immediate NE when available. Enumerate packet walks, not simultaneous assemblies.
import assert from 'node:assert/strict';
import fs from 'node:fs';
import {GenerativeAssemblyRules} from '../../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
const r=new GenerativeAssemblyRules(),ops=id=>r.outgoing(id).map(i=>r.operations[i]),chart=id=>r.charts[r.packets[id].chart];
const pn=ops(r.root).find(o=>o.kind==='PN'),cs=r.geometry.cells[chart(pn.target).cell].vertices.filter(v=>Object.entries(chart(pn.target).aliases).some(([k,a])=>k.startsWith('C')&&a===v));
const pair=[true,false].map(on=>cs.filter(v=>pn.face.includes(v)===on));assert(pair.every(p=>p.length===1));
const rows=[];function walk(id,path){const k=path.length,pred=pair[k%2][0],a=chart(id).aliases;assert.equal(a.C1,pred);assert.equal(a.C2,pair[1-k%2][0]);const next=ops(id),e=next.find(o=>o.kind==='NE');let window=null;if(e){const b=chart(e.target).aliases;window=[b.M1,b.C1,b.C2];assert.equal(window[1],pred)}rows.push({path,id,cell:chart(id).cell,window});if(k<4)for(const op of next)if(['reader-phase-advance','NN-phase-advance'].includes(op.kind))walk(op.target,path+(op.kind==='reader-phase-advance'?'R':'N'))}
walk(pn.target,'');const one=rows.filter(t=>t.path.length===1);assert.equal(one.length,2);assert.notEqual(one[0].window[0],one[1].window[0]);const summary=Array.from({length:5},(_,k)=>{const q=rows.filter(x=>x.path.length===k);return [q.length,q.filter(x=>x.window).length]});console.log({summary,one});fs.writeFileSync(new URL('../results/pne_two_advance_routes.json',import.meta.url),JSON.stringify({summary,rows},null,2)+'\n');
