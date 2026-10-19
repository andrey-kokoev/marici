import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {compileTessellatedAtlas} from '../tessellated-atlas.mjs';
import {replayExecution} from '../atlas-execution-plans.mjs';
import {inspectContraction} from '../experimental-terminal-pe.mjs';
const planPath='research/nima/results/atlas-execution-plans/two-reader-plan.json',plan=JSON.parse(readFileSync(planPath)),c=compileTessellatedAtlas({maxOrigin:2}),u=c.universe,g=u.rules;
assert.equal(replayExecution(c,plan).batches,1);assert.deepEqual(plan.steps[0].added,[6,51]);
function snapshot(ids){const a=inspectContraction(u,ids);assert.ok(a.certifiedExit);const selected=new Set(ids),native=u.operations.map(i=>g.operations[i]).filter(o=>selected.has(o.source)&&selected.has(o.target)),d=g.describe(ids);return {selected:ids,construction:a.construction,native,shortcuts:a.shortcuts,contacts:d.contacts.map(contact=>({...contact,witnesses:native.filter(o=>{const cells=[o.source,o.target].map(p=>g.charts[g.packets[p].chart].cell);return cells[0]!==cells[1]&&cells.every(x=>contact.cells.includes(x));}).map(o=>o.id)}))};}
const initial=snapshot(plan.start),final=snapshot(plan.target),partial=plan.steps[0].added.map(p=>{const a=inspectContraction(u,[...plan.start,p]);assert.ok(a.valid&&!a.rooted);return {added:p,unrooted:a.unrooted};});
const paths=[planPath,'research/nima/checkers/export_two_reader_field_fixture.mjs','research/nima/tessellated-atlas.mjs','research/nima/atlas-execution-plans.mjs','research/nima/experimental-terminal-pe.mjs','research/nima/generative-phase-assembly.mjs'];
const result={schema:'marici.nima.two-reader-field-fixture.v1',root:g.root,maxOrigin:2,mode:u.mode,initial,final,partial,packets:g.packets,charts:g.charts,cells:g.geometry.cells.map(({owner,...c})=>c),nativeOperations:u.operations.map(i=>g.operations[i]),sourceHashes:Object.fromEntries(paths.map(p=>[p,createHash('sha256').update(readFileSync(p)).digest('hex')]))};
mkdirSync('research/nima/results/two-reader-field-sewing',{recursive:true});writeFileSync('research/nima/results/two-reader-field-sewing/fixture.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({status:'fixture-replayed',initialContacts:initial.contacts.length,finalContacts:final.contacts.length,nativeEdges:final.native.length}));
