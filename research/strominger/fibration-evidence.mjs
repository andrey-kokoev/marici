import {createHash} from 'node:crypto';
// Small evidence envelope. Native payloads remain owned by their adapters.
// These records are checker output, NOT externally supplied proof certificates.
function canonical(value){
 if(value===null||typeof value==='string'||typeof value==='boolean')return value;
 if(typeof value==='number'&&Number.isFinite(value))return value;
 if(Array.isArray(value))return value.map(canonical);
 if(value&&typeof value==='object'&&Object.getPrototypeOf(value)===Object.prototype)return Object.fromEntries(Object.keys(value).sort().map(k=>[k,canonical(value[k])]));
 throw Error('Boundary payload must be finite JSON data; unsupported values cannot be silently erased');
}
export const digest=value=>createHash('sha256').update(JSON.stringify(canonical(value))).digest('hex');
export const boundary=(carrier,payload)=>({carrier,stateHash:digest(payload)});
export const adapterContracts=Object.freeze({'native-channel':[['retained-channel','native-diagram']],'native-field-sewing':[['native-diagram','full44-sewn-section']],'marked-table':[['marked-table','marked-source-fibers'],['marked-source-fibers','marked-table']],'native-table-bridge':[['native-diagram','marked-table'],['marked-table','native-diagram']],'native-window-stars':[['native-diagram','native-window-star-views']],'native-window-transport':[['native-diagram','native-window-transport-audit']]});
export function validateEvidence(record){
 const errors=[],string=x=>typeof x==='string'&&x.length>0;
 if(!record||typeof record!=='object')return ['Expected evidence record'];
 for(const key of ['id','adapter','claim'])if(!string(record[key]))errors.push(`Invalid ${key}`);
 for(const key of ['input','output',...(record.adapter==='native-table-bridge'||record.retainedContext!==undefined?['retainedContext']:[])]){const b=record[key];if(!b||!string(b.carrier)||!/^([0-9a-f]{64})$/.test(b.stateHash))errors.push(`Invalid ${key} boundary`);}
 if(!Array.isArray(record.premises)||record.premises.some(p=>!p||!string(p.id)||!['assumed','missing'].includes(p.status)||!string(p.statement)))errors.push('Invalid premises');
 if(!Array.isArray(record.checks)||record.checks.length===0||record.checks.some(c=>!c||!string(c.id)||typeof c.passed!=='boolean'))errors.push('Invalid check results');
 if(!Array.isArray(record.dependsOn)||record.dependsOn.some(x=>!string(x)))errors.push('Invalid dependencies');
 return errors;
}
export function composeEvidence(records,links=[]){
 if(!Array.isArray(records)||records.length===0||!Array.isArray(links))return {status:'rejected',failures:[{category:'malformed-evidence',errors:['Expected a nonempty evidence array and explicit boundary links']}],assumptions:[],missing:[],claims:[]};
 const failures=[],byId=new Map(),premises=new Map();
 for(const r of records){const errors=validateEvidence(r);if(errors.length){failures.push({category:'malformed-evidence',id:r?.id??null,errors});continue;}if(byId.has(r.id))failures.push({category:'duplicate-evidence',id:r.id});byId.set(r.id,r);}
 const active=new Set(),done=new Set();
 function visit(id){if(done.has(id))return;if(active.has(id)){failures.push({category:'cyclic-evidence',id});return;}const r=byId.get(id);if(!r){failures.push({category:'missing-evidence',id});return;}active.add(id);for(const dep of r.dependsOn)visit(dep);active.delete(id);done.add(id);}
 for(const r of byId.values()){
  visit(r.id);if(!Object.hasOwn(adapterContracts,r.adapter))failures.push({category:'unsupported-adapter',id:r.adapter});else if(!adapterContracts[r.adapter].some(([a,b])=>a===r.input.carrier&&b===r.output.carrier))failures.push({category:'adapter-type-mismatch',id:r.id});for(const p of r.premises){if(premises.has(p.id)&&JSON.stringify(premises.get(p.id))!==JSON.stringify(p))failures.push({category:'conflicting-premise',id:p.id});premises.set(p.id,p);}
  for(const c of r.checks)if(!c.passed)failures.push({category:'failed-equation',id:r.id,check:c.id});
 }
 for(const link of links){if(!link||typeof link.from!=='string'||typeof link.to!=='string'){failures.push({category:'malformed-boundary-link'});continue;}const from=byId.get(link.from),to=byId.get(link.to);if(!from||!to){failures.push({category:'missing-boundary',...link});continue;}const fromPort=link.fromPort??'output',toPort=link.toPort??'input';if(!['output','retainedContext'].includes(fromPort)||!['input','retainedContext'].includes(toPort)||!from[fromPort]||!to[toPort]){failures.push({category:'missing-boundary-port',...link});continue;}const a=from[fromPort],b=to[toPort];if(a.carrier!==b.carrier||a.stateHash!==b.stateHash)failures.push({category:'boundary-mismatch',...link,expected:a,actual:b});}
 const required=[...premises.values()],missing=required.filter(p=>p.status==='missing'),assumptions=required.filter(p=>p.status==='assumed');
 return {status:failures.length?'rejected':missing.length?'incomplete':assumptions.length?'verified-conditionally':'verified',failures,assumptions,missing,claims:[...byId.values()].map(r=>({id:r.id,adapter:r.adapter,claim:r.claim})),trustBoundary:'Only registered adapter/checker outputs may create these records; hashes identify exact boundaries, not mathematical proofs.'};
}
