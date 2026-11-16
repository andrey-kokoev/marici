import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {extractIsotopeReference,serializeResource,sourcePath,targetPath} from '../scripts/extract-isotope-reference.mjs';
const html=readFileSync(new URL('../'+sourcePath,import.meta.url),'utf8');
const resource=extractIsotopeReference(html);
test('generated FTS resource is reproducible and preserves 96 rows / 80 elements',()=>{
 assert.equal(readFileSync(new URL('../'+targetPath,import.meta.url),'utf8'),serializeResource(resource));
 assert.deepEqual(JSON.parse(serializeResource(resource)),resource);
 assert.equal(resource.profile,'tabular-data-resource');assert.equal(resource.dialect.header,false);
 assert.equal(resource.data.length,96);assert.equal(new Set(resource.data.map(r=>r[1])).size,80);
 assert.equal(resource.schema.fields.length,11);assert.equal(resource.schema.primaryKey,'isotope');
 assert.equal(resource.provenance.sourceSha256,createHash('sha256').update(html).digest('hex'));
});
test('offline editor embeds the exact FTS resource without a runtime fetch',()=>{
 const editor=readFileSync(new URL('../examples/isotope-wiring/index.html',import.meta.url),'utf8');
 const embedded=editor.match(/<script type="application\/json" id="isotope-reference-data">([\s\S]*?)<\/script>/)?.[1];
 assert.deepEqual(JSON.parse(embedded),resource);
});
test('each typed row follows the declared field order and constraints',()=>{
 const names=new Set();
 for(const row of resource.data){assert.equal(row.length,resource.schema.fields.length);assert(!names.has(row[0]));names.add(row[0]);
  row.forEach((v,i)=>{const f=resource.schema.fields[i],c=f.constraints??{};if(v===null){assert(!c.required);return;}if(f.type==='string')assert.equal(typeof v,'string');else{assert.equal(typeof v,'number');assert(Number.isFinite(v));if(f.type==='integer')assert(Number.isInteger(v));}if(c.minimum!==undefined)assert(v>=c.minimum);if(c.maximum!==undefined)assert(v<=c.maximum);if(c.pattern)assert(new RegExp(c.pattern).test(v));});
 }
});
test('lithium values, absent shells and Pb-204 qualifier survive extraction',()=>{
 assert.deepEqual(resource.data.find(r=>r[0]==='Lithium-6'),['Lithium-6',3,3,2,1,null,null,null,null,7.59,'Stable']);
 assert.deepEqual(resource.data.find(r=>r[0]==='Lithium-7'),['Lithium-7',3,4,2,1,null,null,null,null,92.41,'Stable']);
 assert.equal(resource.data.find(r=>r[0]==='Lead-204')[10],'No decay observed; t½ ≥ 1.4 × 10¹⁷ y');
 assert(!resource.schema.fields.some(f=>/spin|moment|radius|binding/.test(f.name)));
});
test('missing metadata stays unknown, while zero abundance stays zero',()=>{
 const missing=extractIsotopeReference(html.replace("'Lithium-6': '7.59', ",''));
 assert.deepEqual(missing.data.find(r=>r[0]==='Lithium-6').slice(9),[null,'Not assessed']);
 const zero=extractIsotopeReference(html.replace("'Lithium-6': '7.59'","'Lithium-6': '0'"));assert.equal(zero.data.find(r=>r[0]==='Lithium-6')[9],0);
});
test('malformed, duplicate and inconsistent source records fail closed',()=>{
 assert.throws(()=>extractIsotopeReference(html.replace("'Lithium-6': '7.59'","'Lithium-6': '101'")),/Abundance outside/);
 assert.throws(()=>extractIsotopeReference(html.replace("'Lithium-6': '7.59'","'Lithium-6': evil()")),/Unsupported syntax/);
 assert.throws(()=>extractIsotopeReference(html.replace('<th scope="row">Lithium-6</th>','<th scope="row">Lithium-8</th>')),/Orphan metadata/);
 const row=html.match(/<tr><th scope="row">Lithium-6[\s\S]*?<\/tr>/)[0];
 assert.throws(()=>extractIsotopeReference(html.replace('<tbody id="isotope-body">','<tbody id="isotope-body">'+row)),/duplicate isotope/);
});
