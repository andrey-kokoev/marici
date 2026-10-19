import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {contractionUniverse,enumerateContractions,inspectContraction,MODE} from '../experimental-terminal-pe.mjs';
const sort=xs=>[...new Set(xs)].sort((a,b)=>a-b),pair=(a,b)=>[a,b].sort((a,b)=>a-b).join(':');
const catalogPath='research/nima/results/pne-interface-catalog/verification.json',catalog=JSON.parse(readFileSync(catalogPath,'utf8'));
// This interpreter consumes serialized interfaces; it calls neither describe,
// inspectContraction nor source outgoing operations.
function interpret(reg,interfaces,ids){
 const selected=new Set(ids),bodies=new Map(),roles=new Map();let compatible=true;
 for(const p of ids){const c=reg.charts[reg.packets[p].chart];if(bodies.has(c.cell)&&bodies.get(c.cell)!==c.species)compatible=false;bodies.set(c.cell,c.species);for(const [mark,v]of Object.entries(c.aliases)){if(roles.has(v)&&roles.get(v)!==mark[0])compatible=false;roles.set(v,mark[0]);}}
 const contacts=[],entries=[...bodies];for(let i=0;i<entries.length;i++)for(let j=i+1;j<entries.length;j++){
 const [a,sa]=entries[i],[b,sb]=entries[j],face=reg.cells[a].vertices.filter(v=>reg.cells[b].vertices.includes(v));if(face.length!==3)continue;
 if(sa===sb&&sa!=='neutron'||[sa,sb].includes('proton')&&[sa,sb].includes('electron'))compatible=false;
 const kind=[sa,sb].includes('electron')?'NE':sa===sb?'NN':'PN';if(face.filter(v=>roles.get(v)==='M').length!==(kind==='PN'?2:1))compatible=false;contacts.push(pair(a,b));}
 const active=interfaces.filter(o=>selected.has(o.source)&&selected.has(o.target)&&o.requiredOccupied.every(c=>bodies.has(c))&&o.requiredVacant.every(c=>!bodies.has(c))&&o.forbiddenSelected.every(p=>!selected.has(p)));
 const rooted=new Set(selected.has(reg.root)?[reg.root]:[]),exits=new Set(ids.filter(p=>reg.charts[reg.packets[p].chart].species==='electron'));
 for(let changed=true;changed;){changed=false;for(const o of active){if(rooted.has(o.source)&&!rooted.has(o.target)){rooted.add(o.target);changed=true;}if(exits.has(o.target)&&!exits.has(o.source)){exits.add(o.source);changed=true;}}}
 const witnessed=new Set(active.filter(o=>o.faceWitness).map(o=>pair(...o.faceWitness))),missing=contacts.filter(c=>!witnessed.has(c));
 return {compatible,rooted:compatible&&rooted.size===selected.size,certified:compatible&&rooted.size===selected.size&&exits.size===selected.size&&!missing.length,active:active.map(o=>o.key).sort(),missing:missing.sort(),unrooted:ids.filter(p=>!rooted.has(p)),noExit:ids.filter(p=>!exits.has(p))};
}
const report={schema:'marici.nima.pne-guarded-composition.v1',test:'guarded-interface-critical-pairs-D01',status:'pass-interface-composition-source-agreement',cases:[],obstructions:[],occupancyObstructions:[],orderExamples:[],negativeControls:[]};
for(const D of [0,1]){
 const u=contractionUniverse({maxOrigin:D}),g=u.rules,graph=enumerateContractions(u);assert.ok(graph.complete);
 const reg={root:g.root,packets:g.packets,charts:g.charts,cells:g.geometry.cells.map(({owner,...c})=>c)},cell=p=>g.charts[g.packets[p].chart].cell;
 const interfaces=u.operations.map(i=>{const o=g.operations[i];return {key:'native:'+i,source:o.source,target:o.target,permutation:o.permutation,requiredOccupied:sort([cell(o.source),cell(o.target)]),requiredVacant:[],forbiddenSelected:[],faceWitness:cell(o.source)===cell(o.target)?null:[cell(o.source),cell(o.target)]};});
 for(const r of catalog.cases.find(c=>c.summary.maxOrigin===D).records.filter(r=>r.contractedPolicy)){
 const p=r.contractedPolicy,o=u.shortcuts.find(o=>o.source===r.source&&o.target===r.target);assert.ok(o);assert.deepEqual(r.permutation,o.permutation);
 interfaces.push({key:MODE+':'+o.id,source:r.source,target:r.target,permutation:r.permutation,requiredOccupied:p.requiredOccupied,requiredVacant:p.requiredVacant,forbiddenSelected:p.forbiddenSelectedNativeSuccessors,faceWitness:null});
 }
 const keys=new Map(graph.nodes.map((ids,i)=>[ids.join(','),i])),transitions=new Set(graph.edges.map(e=>e.from+':'+e.to)),cache=new Map();
 function audit(ids){const key=ids.join(',');if(cache.has(key))return cache.get(key);const predicted=interpret(reg,interfaces,ids),actual=inspectContraction(u,ids);assert.equal(predicted.compatible,actual.valid);assert.equal(predicted.rooted,!!(actual.valid&&actual.rooted));assert.equal(predicted.certified,!!actual.certifiedExit);assert.equal(predicted.rooted,keys.has(key));
 if(actual.valid){assert.deepEqual(predicted.missing,actual.missingContacts.map(c=>pair(...c.cells)).sort());assert.deepEqual(predicted.active.filter(k=>k.startsWith(MODE)),actual.shortcuts.map(o=>MODE+':'+o.id).sort());}
 cache.set(key,predicted);return predicted;}
 function transition(from,to){const a=audit(from),b=audit(to);if(!a.rooted||!b.rooted)return false;const added=to.find(p=>!from.includes(p));const prediction=interfaces.some(o=>o.target===added&&from.includes(o.source)&&b.active.includes(o.key));assert.equal(prediction,transitions.has(keys.get(from.join(','))+':'+keys.get(to.join(','))));return prediction;}
 // Local dependency index: additions only invalidate/activate interfaces
 // watching that packet as endpoint, forbidden successor or vacant-site occupant.
 const watchers=new Map(u.packets.map(p=>[p,interfaces.filter(o=>o.source===p||o.target===p||o.forbiddenSelected.includes(p)||o.requiredVacant.includes(cell(p))).map(o=>o.key)]));
 function update(active,ids,added){const touched=new Set(added.flatMap(p=>watchers.get(p))),next=new Set(active),selected=new Set(ids),occupied=new Set(ids.map(cell));for(const key of touched){const o=interfaces.find(o=>o.key===key),enabled=selected.has(o.source)&&selected.has(o.target)&&o.requiredOccupied.every(c=>occupied.has(c))&&o.requiredVacant.every(c=>!occupied.has(c))&&o.forbiddenSelected.every(p=>!selected.has(p));if(enabled)next.add(key);else next.delete(key);}return [...next].sort();}
 const incompatiblePairs=new Map();
 function explain(ids){if(audit(ids).compatible)return;let found=false;for(let i=0;i<ids.length;i++)for(let j=i+1;j<ids.length;j++){const pairIds=[ids[i],ids[j]];if(!interpret(reg,interfaces,pairIds).compatible){found=true;const key=pairIds.join(',');if(!incompatiblePairs.has(key)){assert.ok(interpret(reg,interfaces,[ids[i]]).compatible);assert.ok(interpret(reg,interfaces,[ids[j]]).compatible);const direct=g.describe(pairIds);assert.equal(direct.valid,false);incompatiblePairs.set(key,{packets:pairIds,reason:direct.reason});}}}assert.ok(found,'Higher-order compatibility obstruction escaped pair representation');}
 const stats={maxOrigin:D,baseConfigurations:graph.nodes.length,onePacketExtensions:0,twoPacketExtensions:0,oneCompatible:0,oneRooted:0,oneCertified:0,disabledShortcuts:0,disabledWithRootLoss:0,disabledWithRootPreserved:0,orders:{both:0,onlyFirst:0,onlySecond:0,neither:0},finalRootedNeitherOrder:0};
 const obstructions=new Map();
 for(const base of graph.nodes){const start=audit(base),absent=u.packets.filter(p=>!base.includes(p));
 for(const p of absent){stats.onePacketExtensions++;const ids=sort([...base,p]),next=audit(ids);stats.oneCompatible+=+next.compatible;stats.oneRooted+=+next.rooted;stats.oneCertified+=+next.certified;assert.deepEqual(update(start.active,ids,[p]),next.active);explain(ids);
 for(const key of start.active.filter(k=>k.startsWith(MODE)&&!next.active.includes(k))){stats.disabledShortcuts++;if(next.compatible){if(next.rooted)stats.disabledWithRootPreserved++;else stats.disabledWithRootLoss++;}
 const o=interfaces.find(o=>o.key===key),reasons=[];if(o.requiredVacant.includes(cell(p)))reasons.push('vacant-reference-body-occupied');if(o.forbiddenSelected.includes(p))reasons.push('selected-native-successor');assert.ok(reasons.length);
 const id=key+':'+p;if(!obstructions.has(id)){
 const minimal=sort([o.source,o.target]);assert.ok(interpret(reg,interfaces,minimal).active.includes(key));assert.ok(!interpret(reg,interfaces,sort([...minimal,p])).active.includes(key));
 obstructions.set(id,{interface:key,source:o.source,target:o.target,trigger:p,reasons,endpointSupport:minimal,exampleBase:base,exampleAfter:ids,afterCompatible:next.compatible,afterRooted:next.rooted});}
 }
 transition(base,ids);
 }
 for(let i=0;i<absent.length;i++)for(let j=i+1;j<absent.length;j++){
 const p=absent[i],q=absent[j],first=sort([...base,p]),second=sort([...base,q]),final=sort([...base,p,q]),end=audit(final);stats.twoPacketExtensions++;explain(final);assert.deepEqual(update(update(start.active,first,[p]),final,[q]),end.active);assert.deepEqual(update(update(start.active,second,[q]),final,[p]),end.active);
 const pq=transition(base,first)&&transition(first,final),qp=transition(base,second)&&transition(second,final),category=pq?(qp?'both':'onlyFirst'):(qp?'onlySecond':'neither');stats.orders[category]++;
 if(end.rooted&&!pq&&!qp){stats.finalRootedNeitherOrder++;if(!report.orderExamples.some(e=>e.type==='rooted-final-neither-order'&&e.maxOrigin===D))report.orderExamples.push({maxOrigin:D,type:'rooted-final-neither-order',base,added:[p,q],final,first:audit(first),second:audit(second),end});}
 if(pq!==qp&&start.active.some(k=>k.startsWith(MODE))&&!report.orderExamples.some(e=>e.type==='shortcut-guard-repair-order'&&e.maxOrigin===D))report.orderExamples.push({maxOrigin:D,type:'shortcut-guard-repair-order',base,added:[p,q],admittedOrder:pq?[p,q]:[q,p],first:audit(first),second:audit(second),end});
 if(pq!==qp&&!report.orderExamples.some(e=>e.type==='one-order-only'&&e.maxOrigin===D))report.orderExamples.push({maxOrigin:D,type:'one-order-only',base,added:[p,q],admittedOrder:pq?[p,q]:[q,p],first:audit(first),second:audit(second),end});
 }
 }
 // Transport composition is associative for every sequential triple whose
 // packet endpoints match. This algebraic check is separate from support.
 let triples=0;for(const a of interfaces)for(const b of interfaces.filter(b=>b.source===a.target))for(const c of interfaces.filter(c=>c.source===b.target)){
 const compose=(p,q)=>q.map(i=>p[i]);assert.deepEqual(compose(compose(a.permutation,b.permutation),c.permutation),compose(a.permutation,compose(b.permutation,c.permutation)));triples++;}
 report.obstructions.push(...[...obstructions.values()].map(o=>({maxOrigin:D,...o})));report.occupancyObstructions.push(...[...incompatiblePairs.values()].map(p=>({maxOrigin:D,...p})));stats.minimalCompatibilityPairs=incompatiblePairs.size;stats.distinctGuardTriggers=obstructions.size;stats.uniqueSelectedSetsChecked=cache.size;stats.sequentialMapTriples=triples;
 report.cases.push({summary:stats,interfaces,registry:reg});console.log(JSON.stringify(stats));
}
assert.ok(report.obstructions.length);assert.ok(report.orderExamples.some(e=>e.type==='one-order-only'));
// A stale interface cache must disagree on a stored minimal trigger witness.
const o=report.obstructions[0],c=report.cases.find(c=>c.summary.maxOrigin===o.maxOrigin),before=interpret(c.registry,c.interfaces,o.endpointSupport),after=interpret(c.registry,c.interfaces,sort([...o.endpointSupport,o.trigger]));assert.notDeepEqual(before.active,after.active);report.negativeControls.push('frozen-active-interface-cache-rejected');
for(const [reason,field]of [['vacant-reference-body-occupied','requiredVacant'],['selected-native-successor','forbiddenSelected']]){
 const o=report.obstructions.find(o=>o.reasons.length===1&&o.reasons[0]===reason);assert.ok(o);const c=report.cases.find(c=>c.summary.maxOrigin===o.maxOrigin),mutated=structuredClone(c.interfaces);mutated.find(i=>i.key===o.interface)[field]=[];
 const ids=sort([...o.endpointSupport,o.trigger]);assert.ok(interpret(c.registry,mutated,ids).active.includes(o.interface));assert.ok(!interpret(c.registry,c.interfaces,ids).active.includes(o.interface));report.negativeControls.push('omitted-'+field+'-rejected');
}
report.sourceHashes=Object.fromEntries([catalogPath,'research/nima/checkers/check_pne_guarded_composition.mjs','research/nima/experimental-terminal-pe.mjs','research/nima/generative-phase-assembly.mjs'].map(p=>[p,createHash('sha256').update(readFileSync(p)).digest('hex')]));
const out='research/nima/results/pne-guarded-composition';mkdirSync(out,{recursive:true});writeFileSync(out+'/verification.json',JSON.stringify(report,null,2)+'\n');
