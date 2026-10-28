// Thin adapter for the EXISTING NativeChannelAssembler fixture, not a new
// packet calculus. Exact 44-field equations remain owned by the sewing checker.
import {isDeepStrictEqual as equal} from 'node:util';
const permutation=p=>Array.isArray(p)&&p.length===5&&[...p].sort().every((v,i)=>v===i);
export function validateNativeFixture(f){
 const errors=[],id=x=>(typeof x==='number'&&Number.isSafeInteger(x))||(typeof x==='string'&&x.length>0),object=x=>x!==null&&typeof x==='object'&&!Array.isArray(x),array=(x,p)=>{if(!Array.isArray(x)){errors.push({path:p,expected:'array'});return false;}return true;};
 if(!object(f))return [{path:'fixture',expected:'native fixture object'}];
 for(const key of ['packets','charts','cells','operations','histories'])if(array(f[key],key))f[key].forEach((r,i)=>{const p=`${key}[${i}]`;if(!object(r)){errors.push({path:p,expected:'object'});return;}
  const needId=k=>{if(!id(r[k]))errors.push({path:`${p}.${k}`,expected:'stable native ID'});};
  if(key==='packets'){needId('id');needId('chart');array(r.permutation,`${p}.permutation`);}
  if(key==='charts'){needId('index');if(!['proton','neutron','electron'].includes(r.species))errors.push({path:`${p}.species`,expected:'native species'});if(!object(r.aliases))errors.push({path:`${p}.aliases`,expected:'native marked aliases'});}
  if(key==='cells'){needId('id');array(r.vertices,`${p}.vertices`);}
  if(key==='operations'){for(const k of ['id','source','target'])needId(k);if(typeof r.kind!=='string')errors.push({path:`${p}.kind`,expected:'operation kind'});array(r.permutation,`${p}.permutation`);}
  if(key==='histories'){for(const k of ['packets','operations','word'])if(array(r[k],`${p}.${k}`)&&r[k].some(x=>!id(x)))errors.push({path:`${p}.${k}`,expected:'native IDs / words'});if(r.occurrences!==undefined)array(r.occurrences,`${p}.occurrences`);}
 });
 if(!id(f.rootPacket))errors.push({path:'rootPacket',expected:'native packet ID'});
 return errors;
}
export function auditRetainedDiagram(f,expected){
 const failures=[],fail=(category,at,claim,details={})=>failures.push({category,at,claim,...details});
 const schemaErrors=validateNativeFixture(f);if(schemaErrors.length)return {status:'rejected',failures:schemaErrors.map(e=>({category:'malformed-diagram',at:e.path,claim:`Expected ${e.expected}`}))};
 const packets=new Map(f.packets.map(p=>[p.id,p])),charts=new Map(f.charts.map(c=>[c.index,c])),ops=new Map(f.operations.map(o=>[o.id,o]));
 if(packets.size!==f.packets.length||ops.size!==f.operations.length||charts.size!==f.charts.length)fail('malformed-diagram','diagram','Packet and operation IDs must be unique');
 for(const p of packets.values()){if(!charts.has(p.chart))fail('type-mismatch',`packet:${p.id}`,'Unknown native chart');if(!permutation(p.permutation))fail('type-mismatch',`packet:${p.id}`,'Expected full five-slot permutation');}
 const required=new Map(expected.operations.map(o=>[o.id,o]));
 for(const [id,op] of required){if(!ops.has(id))fail('missing-witness',`interface:${id}`,'Required native interface absent');else if(!equal(ops.get(id),op))fail('native-witness-mismatch',`interface:${id}`,'Interface differs from fresh native reconstruction');}
 for(const id of ops.keys())if(!required.has(id))fail('unsupported-interface',`interface:${id}`,'No witness in the reconstructed native diagram');
 for(const id of packets.keys())if(!expected.packets.some(p=>p.id===id))fail('unsupported-packet',`packet:${id}`,'No packet witness in the reconstructed native diagram');
 for(const key of ['rootPacket','audit','channelReferences','fieldFrames','prefixes'])if(!equal(f[key],expected[key]))fail('retained-data-mismatch',key,'Native root, audit and retained reconstruction metadata must not be replaced');
 for(const p of expected.packets){if(!packets.has(p.id))fail('missing-packet',`packet:${p.id}`,'Retained packet absent');else if(!equal(packets.get(p.id),p))fail('retained-data-mismatch',`packet:${p.id}`,'Native packet data changed');}
 if(!equal(f.charts,expected.charts)||!equal(f.cells,expected.cells))fail('retained-data-mismatch','carriers','Native charts and carriers must be retained');
 if(!equal(f.histories,expected.histories)||!equal(f.channelLog,expected.channelLog))fail('history-erasure','histories','Ordered histories and channel occurrences must remain intact');
 if(!equal(f.comparisons,expected.comparisons)||!equal(f.comparisonPackets,expected.comparisonPackets))fail('comparison-erasure','comparisons','Retained comparison witnesses must remain intact');
 const selected=new Set(f.histories.flatMap(h=>h.operations));
 for(const op of ops.values()){
  const a=packets.get(op.source),b=packets.get(op.target),at=`interface:${op.id}`,incidental=!selected.has(op.id);
  if(!a||!b){fail('type-mismatch',at,'Unknown source/target packet',{incidental});continue;}
  const sa=charts.get(a.chart)?.species,sb=charts.get(b.chart)?.species;
  const allowed={PN:['proton','neutron'],'inverse-PN':['neutron','proton'],NE:['neutron','electron'],'NN-phase-advance':['neutron','neutron']};
  const types=allowed[op.kind]??(op.kind==='reader-phase-advance'&&['proton','neutron'].includes(sa)?[sa,sa]:null);
  if(!types||types[0]!==sa||types[1]!==sb)fail('type-mismatch',at,'Native operation carrier mismatch',{incidental,kind:op.kind,sourceSpecies:sa,targetSpecies:sb});
  if(!permutation(op.permutation)){fail('type-mismatch',at,'Invalid coefficient map',{incidental});continue;}
  if(permutation(a.permutation)&&permutation(b.permutation)){
   const composed=op.permutation.map(i=>a.permutation[i]);
   if(!equal(composed,b.permutation))fail('failed-equation',at,'Pi_edge Pi_source = Pi_target',{incidental,computed:composed,expected:b.permutation});
  }
 }
 for(const h of f.histories){if(h.packets.length!==h.operations.length+1)fail('history-type-mismatch',`history:${h.id}`,'Path length mismatch');h.operations.forEach((id,i)=>{const op=ops.get(id);if(!op||op.source!==h.packets[i]||op.target!==h.packets[i+1])fail('history-type-mismatch',`history:${h.id}:${i}`,'History is not a composable witnessed path');});}
 return {status:failures.length?'rejected':'native-diagram-consistent',counts:{packets:packets.size,interfaces:ops.size,generatingInterfaces:selected.size,incidentalInterfaces:[...ops.keys()].filter(id=>!selected.has(id)).length,histories:f.histories.length},failures,scope:'Fresh native witness comparison, carrier typing, exact coefficient composition and retained-data checks. Full-field sewing is a separate required stage.'};
}
export function inspectPartialBeltDiagram(diagram){
 if(diagram.kind!=='parent-belt-fibration-question-v1')throw Error('Unsupported diagram kind');
 const obligations=[];
 if(!diagram.endpointClaim)obligations.push({category:'undefined-endpoint-claim',at:'whole-diagram',required:'Specify the endpoint presentation change and retained-whole recovery claim; identity shortcuts are not an adequate substitute.'});
 for(const stage of diagram.stages){if(!stage.interpretation)obligations.push({category:'undefined-stage-interpretation',at:stage.id,required:'Bind this displayed stage to a retained native presentation.'});if(!stage.packetType)obligations.push({category:'unbound-packet-type',at:stage.id,required:'Specify the complete carrier, markings, reference bindings and retained context.'});}
 for(const edge of diagram.interfaces){obligations.push({category:edge.adapter?'unsupported-adapter':'missing-interface-map',at:edge.id,from:edge.from,to:edge.to,required:'Supply a source-backed typed operation, actual maps and incidental-interface witnesses. No belt field adapter is registered in this pilot.'});}
 return {status:'incomplete',obligations,equationFailures:[],scope:'Missing bindings are not failed equations or a no-go theorem. Positions and scalar flux balance do not supply these bindings.'};
}
