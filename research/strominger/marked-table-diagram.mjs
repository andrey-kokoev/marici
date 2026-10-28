import {boundary,composeEvidence} from './fibration-evidence.mjs';
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b),clone=structuredClone;
function validateRows(rows,carriers){
 if(!Array.isArray(rows)||!carriers||!['label','source','target'].every(k=>Array.isArray(carriers[k])&&new Set(carriers[k]).size===carriers[k].length))throw Error('Invalid finite table carriers');
 if(new Set(rows.map(r=>r?.id)).size!==rows.length||rows.some(r=>!r||typeof r.id!=='string'||!['label','source','target'].every(k=>carriers[k].includes(r[k]))))throw Error('Invalid retained row or endpoint');
 if(new Set(rows.map(r=>JSON.stringify([r.source,r.target]))).size!==rows.length)throw Error('Duplicate endpoint pair');
}
export function table(rows,carriers,history=[]){validateRows(rows,carriers);if(!Array.isArray(history))throw Error('Invalid history');return {kind:'marked-table',rows:clone(rows),carriers:clone(carriers),history:clone(history)};}
export function groupSource(t){
 if(t.kind!=='marked-table')throw Error('Expected marked table');validateRows(t.rows,t.carriers);
 return {kind:'marked-source-fibers',selector:'source',carriers:clone(t.carriers),groups:t.carriers.source.map(key=>({key,children:t.rows.filter(r=>r.source===key).map(({source,...r})=>clone(r))})),history:[...clone(t.history),{operation:'group',selector:'source'}]};
}
export function restoreSource(f){
 if(f.kind!=='marked-source-fibers'||f.selector!=='source'||!Array.isArray(f.groups)||!Array.isArray(f.history)||!f.carriers||!same(f.groups.map(g=>g?.key),f.carriers.source))throw Error('Invalid source-fiber marker or coverage');
 const rows=f.groups.flatMap(g=>{if(!Array.isArray(g.children))throw Error('Invalid fiber');return g.children.map(r=>{if(!r||Object.hasOwn(r,'source'))throw Error('Unexpected hidden source column');return {...clone(r),source:g.key};});});validateRows(rows,f.carriers);return rows;
}
export function unpackReversed(f){
 const rows=restoreSource(f).map(r=>({...r,source:r.target,target:r.source}));
 return table(rows,{label:f.carriers.label,source:f.carriers.target,target:f.carriers.source},[...clone(f.history),{operation:'unpack',wiring:'reverse-endpoints'}]);
}
export function retainedKeyProjection(t){const fibers=groupSource(t);return {keys:fibers.groups.map(g=>g.key),retainedContext:fibers};}
export function restoreKeyProjection(p){if(!p||!p.retainedContext||!same(p.keys,p.retainedContext.groups.map(g=>g.key)))throw Error('Missing or mismatched retained context');return restoreSource(p.retainedContext);}
export const canonicalRows=rows=>[...rows].sort((a,b)=>a.id.localeCompare(b.id)).map(r=>Object.fromEntries(Object.keys(r).sort().map(k=>[k,r[k]])));
export function verifyMarkedReference(reference){
 const plain=rows=>rows.map(r=>[r.label,r.source,r.target]).sort((a,b)=>a[0]-b[0]||a[1]-b[1]||a[2]-b[2]);
 const failures=[];reference.cases.forEach((c,index)=>{const [nl,ns,nt]=c.dimensions,range=n=>Array.from({length:n},(_,i)=>i),input=table(c.rows.map(([label,source,target],i)=>({id:`row:${i}`,label,source,target})),{label:range(nl),source:range(ns),target:range(nt)}),result=runMarkedTableDiagram(input);
  const fibers=result.stages[1].groups.map(g=>[g.key,g.children.map(r=>[r.label,r.target]).sort((a,b)=>a[0]-b[0]||a[1]-b[1])]);
  if(!same(fibers,c.sourceFibers)||!same(plain(result.stages[2].rows),c.twice)||!same(plain(result.stages[4].rows),c.four)||!result.tableDataRecovered||result.composition.status!=='verified-conditionally')failures.push(index);
 });return {status:failures.length?'rejected':'verified-finite-reference',cases:reference.cases.length,failures,referenceSource:reference.source,referenceHash:reference.sha256,scope:reference.scope};
}
export function runMarkedTableDiagram(input){
 const stages=[input];stages.push(groupSource(stages.at(-1)));stages.push(unpackReversed(stages.at(-1)));stages.push(groupSource(stages.at(-1)));stages.push(unpackReversed(stages.at(-1)));
 const premises=[{id:'marked-table:finite-contract',status:'assumed',statement:'Finite endpoint-unique tables with explicit carriers, retained row payloads and a source-column marker.'},{id:'marked-table:reverse-wiring',status:'assumed',statement:'Reversed endpoint unpacking is the declared wiring convention, not a law forced by fibration.'}];
 const records=stages.slice(1).map((output,i)=>({id:`table:${i+1}`,adapter:'marked-table',input:boundary(stages[i].kind,stages[i]),output:boundary(output.kind,output),dependsOn:i?[`table:${i}`]:[],premises,claim:i%2?'Reversed unpacking transposes endpoints and retains payload/history.':'Source grouping retains every row, carrier and membership key.',checks:[{id:'row-payload-recovery',passed:i%2?same(canonicalRows(output.rows),canonicalRows(restoreSource(stages[i]).map(r=>({...r,source:r.target,target:r.source})))):same(canonicalRows(restoreSource(output)),canonicalRows(stages[i].rows))},{id:'history-extension',passed:output.history.length===stages[i].history.length+1&&same(output.history.slice(0,-1),stages[i].history)}]}));
 const composition=composeEvidence(records,records.slice(1).map((r,i)=>({from:records[i].id,to:r.id})));
 return {adapter:'marked-table',stages,records,composition,tableDataRecovered:same(canonicalRows(input.rows),canonicalRows(stages[4].rows))&&same(input.carriers,stages[4].carriers),historyPreservedAndExtended:stages[4].history.length===input.history.length+4,scope:'Finite adapter of the existing marked-table formulas. No new Agda proof or equality of execution histories with the initial history is claimed.'};
}
