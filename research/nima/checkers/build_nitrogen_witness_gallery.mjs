import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {phaseUniverse} from '../origin-bounded-assemblies.mjs';
const paths=['research/nima/results/nitrogen-alternative-placements/verification.json','research/nima/results/nitrogen-neutral-depth/verification.json','research/nima/demos/nitrogen-witnesses.template.html'];
const [alternatives,neutral]=paths.slice(0,2).map(p=>JSON.parse(readFileSync(p,'utf8')));
const data={schema:'marici.nima.nitrogen-gallery.v1',witnessOnly:true,registries:{},witnesses:[],searches:neutral.cases.flatMap(c=>c.results.map(({witness,...r})=>r))};
const byDepth=new Map();
function append(w,D,id,original){
 if(!byDepth.has(D))byDepth.set(D,phaseUniverse({maxOrigin:D}));const u=byDepth.get(D),g=u.rules;assert.ok(u.complete);
 // Packet IDs are meaningful only after verifying chart, body and map identity.
 for(const p of w.packets){assert.deepEqual(g.packets[p],original.packets[p]);const c=g.packets[p].chart;assert.deepEqual(g.charts[c],original.charts[c]);assert.equal(g.geometry.cells[g.charts[c].cell].key,original.cells[original.charts[c].cell].key);}
 const selected=new Set([g.root]),prefixes=[],record=()=>{const packets=[...selected].sort((a,b)=>a-b),a=g.inspect(packets);assert.ok(a.valid);prefixes.push({packets,counts:a.counts,grade:Math.max(...packets.map(p=>g.packets[p].origin)),certifiedExit:a.certifiedExit,pendingContacts:a.pendingContacts.length});};record();
 for(const oi of w.word){assert.ok(u.operations.includes(oi));const o=g.operations[oi];assert.deepEqual(o,original.operations[oi]);assert.ok(selected.has(o.source));assert.ok(!selected.has(o.target));selected.add(o.target);record();}
 assert.deepEqual([...selected].sort((a,b)=>a-b),[...w.packets].sort((a,b)=>a-b));assert.ok(prefixes.at(-1).certifiedExit);assert.deepEqual(prefixes.at(-1).counts,w.counts);
 data.witnesses.push({id,maxOrigin:D,counts:w.counts,word:w.word,prefixes,comparison:w.nearestPreviousFootprint??null});
 data.registries[D]={packets:g.packets,charts:g.charts,cells:g.geometry.cells.map(({owner,...c})=>c),operations:g.operations,points:Object.fromEntries(g.geometry.points)};
}
for(const c of alternatives.cases.filter(c=>c.requireExit))for(const [i,r]of c.results.entries())if(r.witness)append(r.witness,c.maxOrigin,`D${c.maxOrigin}-N${7+c.neutron}-${i+1}`,alternatives.registry);
for(const c of neutral.cases)for(const r of c.results)if(r.witness)append(r.witness,c.maxOrigin,`D${c.maxOrigin}-N${7+r.counts.neutron}-7e`,c.registry);
assert.equal(data.witnesses.length,11);
const out='research/nima/results/assembly-atlas';mkdirSync(out,{recursive:true});const template=readFileSync(paths[2],'utf8');assert.equal(template.split('__NITROGEN_JSON__').length,2);
writeFileSync(out+'/nitrogen.html',template.replace('__NITROGEN_JSON__',JSON.stringify(data).replaceAll('<','\\u003c')));
writeFileSync(out+'/index.html',`<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Assembly atlas</title><style>body{font:18px system-ui;max-width:850px;margin:40px;color:#17283c}li{margin:24px 0}</style><h1>Assembly atlas</h1><p>Origin budget is maximum realization origin, not operation count.</p><ul><li><a href="../origin-bounded-assemblies/index.html">Complete D=0–2 configuration explorer</a><br>Complete local configuration families at those budgets.</li><li><a href="nitrogen.html">D=3 nitrogen placements and D=4 seven-electron N-15 witness</a><br>11 saved exit-certified constructions, with operation replay. Witness-only—not a complete higher-depth atlas.</li></ul><h2>Seven-electron search status</h2><p>N-15 composition: a 7P/8N/7e local exit witness exists at D=4. N-14 composition: none at D=4 under the model; D=5 search hit its time limit and remains unresolved.</p><p>Local certificates do not establish global field sewing, physical binding or stable atoms.</p></html>\n`);
const sha=p=>createHash('sha256').update(readFileSync(p)).digest('hex');
writeFileSync(out+'/gallery-verification.json',JSON.stringify({status:'pass-gallery-source-replay',witnesses:data.witnesses.length,checkedPrefixes:data.witnesses.reduce((n,w)=>n+w.prefixes.length,0),witnessOnly:true,sourceHashes:Object.fromEntries([...paths,'research/nima/checkers/build_nitrogen_witness_gallery.mjs'].map(p=>[p,sha(p)])),htmlSha256:sha(out+'/nitrogen.html')},null,2)+'\n');
console.log(JSON.stringify({status:'pass-gallery-source-replay',witnesses:data.witnesses.length}));
