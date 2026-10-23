// Source-driven incremental assembly. The decoder never reads a target fixture.
import assert from 'node:assert/strict';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {windowProtocol} from '../demos/particle-overlap-tetrahedron/window-construction-model.mjs';
export const CHANNEL_SCHEMA='marici.native-retained-channel.v1';
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const names=['C0','M0','C1','M1'];
const inverse={PN:'inverse-PN','inverse-PN':'PN','P-reader':'P-reader',NE:'NE'};
const fields={open:['type','schema','fieldConvention','seedBindings','root','context'],begin:['type','history','source'],
 execute:['type','occurrence','history','source','target','operation','context'],
 witness:['type','witness','source','target','operation','context'],
 compare:['type','comparison','left','right'],close:['type','histories']};
function exactKeys(record,keys){assert.deepEqual(Object.keys(record).sort(),[...keys].sort(),'record fields');}
function name(s){assert(typeof s==='string'&&s.length>0&&s.length<=128,'nonempty bounded identifier');return s;}
function normalize(word){const out=[];for(const x of word){if(out.length&&inverse[x]===out.at(-1))out.pop();else out.push(x);}return out;}
function context(chart){const mark=windowProtocol.find(p=>p.species===chart.species).continuation;return {mark,vertex:chart.aliases[mark]};}
function checkContext(given,chart){exactKeys(given,['mark','vertex']);assert.deepEqual(given,context(chart),'missing or incorrect contextual witness');}

export function encodeFixture(fixture){
 const packets=new Map(fixture.packets.map(p=>[p.id,p]));const charts=new Map(fixture.charts.map(c=>[c.index,c]));
 const ops=new Map(fixture.operations.map(o=>[o.id,o]));const label=id=>'packet-'+id;
 const rootChart=charts.get(packets.get(fixture.rootPacket).chart);
 const records=[{type:'open',schema:CHANNEL_SCHEMA,fieldConvention:'prior-full-five-joint-ordered-corner',
  seedBindings:Object.fromEntries(names.map(n=>[n,rootChart.aliases[n]])),root:label(fixture.rootPacket),context:context(rootChart)}];
 const executed=new Set();
 fixture.histories.forEach((h,i)=>{
  const history='history-'+i;records.push({type:'begin',history,source:label(h.packets[0])});
  h.operations.forEach((id,j)=>{
   const op=ops.get(id);assert(op);assert.equal(op.source,h.packets[j]);assert.equal(op.target,h.packets[j+1]);
   records.push({type:'execute',occurrence:history+':'+j,history,source:label(op.source),target:label(op.target),operation:op.kind,context:context(charts.get(packets.get(op.target).chart))});
   executed.add(id);
  });
 });
 for(const op of fixture.operations)if(!executed.has(op.id))records.push({type:'witness',witness:'interface-'+op.id,
  source:label(op.source),target:label(op.target),operation:op.kind,context:context(charts.get(packets.get(op.target).chart))});
 const positions=fixture.comparisonPackets.map((id,i)=>({history:'history-'+i,after:fixture.histories[i].packets.indexOf(id)}));
 records.push({type:'compare',comparison:'retained-frame-comparison',left:positions[0],right:positions[1]});
 records.push({type:'close',histories:fixture.histories.map((_,i)=>'history-'+i)});
 return records;
}

export class NativeChannelAssembler {
 constructor(){this.rules=null;this.closed=false;this.failed=false;this.references=new Map();this.labels=new Map();this.histories=new Map();
  this.occurrences=new Set();this.witnesses=new Set();this.links=new Set();this.frames=new Map();this.comparisons=[];this.log=[];this.prefixes=[];}
 lookup(ref){name(ref);assert(this.references.has(ref),'unresolved packet reference '+ref);return this.references.get(ref);}
 chart(id){return this.rules.charts[this.rules.packets[id].chart];}
 bind(ref,id){
  name(ref);
  if(this.references.has(ref))assert.equal(this.lookup(ref),id,'reference rebound to a different packet');
  else {assert(!this.labels.has(id),'same packet given a second identity');this.references.set(ref,id);this.labels.set(id,ref);}
 }
 edge(record){
  const from=this.lookup(record.source);
  const candidates=this.rules.outgoing(from).map(i=>this.rules.operations[i]).filter(o=>o.kind===record.operation);
  assert.equal(candidates.length,1,'native operation must be uniquely realizable at this source');
  const op=candidates[0];assert(this.rules.validateTransfer(op));checkContext(record.context,this.chart(op.target));
  const kind=op.kind==='reader-phase-advance'?(this.chart(from).species==='proton'?'P-reader':null):op.kind==='NN-phase-advance'?null:op.kind;
  const word=normalize([...this.frames.get(from),...(kind?[kind]:[])]);
  if(this.frames.has(op.target))assert.deepEqual(word,this.frames.get(op.target),'field frame conflict');
  else this.frames.set(op.target,word);
  return op;
 }
 feed(input){
  assert(!this.failed,'assembler is failed; start a fresh replay');
  try{return this._feed(input);}catch(error){this.failed=true;throw error;}
 }
 _feed(input){
  assert(!this.closed,'record after close');const r=structuredClone(input);
  assert(r&&fields[r.type],'unknown record type');exactKeys(r,fields[r.type]);
  if(!this.rules){
   assert.equal(r.type,'open','opening record required');assert.equal(r.schema,CHANNEL_SCHEMA);
   assert.equal(r.fieldConvention,'prior-full-five-joint-ordered-corner');exactKeys(r.seedBindings,names);
   this.rules=new GenerativeAssemblyRules({seedBindings:r.seedBindings});
   checkContext(r.context,this.chart(this.rules.root));this.bind(r.root,this.rules.root);this.frames.set(this.rules.root,[]);
  }else if(r.type==='begin'){
   name(r.history);assert(!this.histories.has(r.history),'duplicate history');
   const id=this.lookup(r.source);assert.equal(id,this.rules.root,'this contract begins histories at the retained root');
   this.histories.set(r.history,{id:r.history,word:[],packets:[id],operations:[],occurrences:[]});
  }else if(r.type==='execute'){
   name(r.occurrence);assert(!this.occurrences.has(r.occurrence),'duplicate occurrence');
   const h=this.histories.get(r.history);assert(h,'unknown history');
   assert.equal(this.lookup(r.source),h.packets.at(-1),'history order/source mismatch');
   const op=this.edge(r);this.bind(r.target,op.target);this.links.add(op.id);this.occurrences.add(r.occurrence);
   h.word.push(op.kind);h.packets.push(op.target);h.operations.push(op.id);h.occurrences.push(r.occurrence);
  }else if(r.type==='witness'){
   name(r.witness);assert(!this.witnesses.has(r.witness),'duplicate interface witness');
   const target=this.lookup(r.target),op=this.edge(r);assert.equal(op.target,target,'wrong interface target');
   assert(!this.links.has(op.id),'duplicate interface declaration');this.links.add(op.id);this.witnesses.add(r.witness);
  }else if(r.type==='compare'){
   name(r.comparison);assert(!this.comparisons.some(c=>c.id===r.comparison),'duplicate comparison');
   const resolve=position=>{exactKeys(position,['history','after']);const h=this.histories.get(position.history);
    assert(h&&Number.isSafeInteger(position.after)&&position.after>=0&&position.after<h.packets.length,'invalid history position');return h.packets[position.after];};
   const left=resolve(r.left),right=resolve(r.right);assert.notEqual(r.left.history,r.right.history,'distinct history references required');
   const a=this.rules.packets[left],b=this.rules.packets[right];assert.equal(a.chart,b.chart);assert.equal(a.origin,b.origin);
   const relative=b.permutation.map(i=>a.permutation.indexOf(i));let power=[0,1,2,3,4],order=0;
   do{power=relative.map(i=>power[i]);order++;assert(order<=120);}while(!same(power,[0,1,2,3,4]));
   this.comparisons.push({id:r.comparison,left,right,leftPosition:r.left,rightPosition:r.right,relativePermutation:relative,order});
  }else if(r.type==='close'){
   assert(Array.isArray(r.histories));assert.deepEqual([...r.histories].sort(),[...this.histories.keys()].sort());
   assert.equal(new Set(r.histories).size,r.histories.length);assert(r.histories.length>0&&this.comparisons.length>0);
   for(const id of r.histories)assert.equal(this.chart(this.histories.get(id).packets.at(-1)).species,'electron','nonterminal history');
   const audit=this.rules.inspect([...this.references.values()]);
   assert(audit.valid&&audit.certifiedExit&&audit.allContactsWitnessed&&audit.allPacketsCanReachExit&&audit.allCellsOnEntryExitPaths);
   assert.deepEqual([...this.links].sort((a,b)=>a-b),[...audit.links].sort((a,b)=>a-b),'missing retained interface witness');
   this.audit=audit;this.historyOrder=[...r.histories];this.closed=true;
  }else throw Error('duplicate opening');
  const prefixAudit=this.rules.inspect([...this.references.values()]);
  assert(prefixAudit.valid,'incompatible retained assembly prefix');
  const pending=prefixAudit.links.filter(id=>!this.links.has(id)).map(id=>{
   const op=this.rules.operations[id];return {source:this.labels.get(op.source),target:this.labels.get(op.target),operation:op.kind};
  });
  this.log.push(r);this.prefixes.push({records:this.log.length,packets:this.references.size,histories:this.histories.size,
   executedOccurrences:this.occurrences.size,interfaces:this.links.size,pendingInterfaceWitnesses:pending,closed:this.closed});
  return this.prefixes.at(-1);
 }
 finish(){assert(!this.failed,'failed assembler');assert(this.closed,'closing record required');return this.fixture();}
 fixture(){
  assert(!this.failed,'failed assembler');assert(this.closed,'assembly is incomplete');const r=this.rules;
  const packets=[...this.references.values()].map(id=>structuredClone(r.packets[id]));
  const charts=[...new Set(packets.map(p=>p.chart))].map(i=>({index:i,...structuredClone(r.charts[i])}));
  return {status:'certified-native-retained-assembly',rootPacket:r.root,packets,charts,
   cells:[...new Set(charts.map(c=>c.cell))].map(i=>structuredClone(r.geometry.cells[i])),
   operations:[...this.links].map(i=>structuredClone(r.operations[i])),
   histories:this.historyOrder.map(id=>structuredClone(this.histories.get(id))),
   comparisonPackets:[this.comparisons[0].left,this.comparisons[0].right],audit:structuredClone(this.audit),
   channelReferences:Object.fromEntries(this.references),fieldFrames:Object.fromEntries([...this.frames].filter(([id])=>this.labels.has(id))),
   comparisons:structuredClone(this.comparisons),channelLog:structuredClone(this.log),prefixes:structuredClone(this.prefixes),
   scope:'Derived by native operation replay from a single bounded channel, not decoded from supplied cell/readout tables. Field equations checked by the separate exact sewing verifier.'};
 }
}

export function decodeChannel(records){const a=new NativeChannelAssembler();for(const r of records)a.feed(r);return a.finish();}

// Compare semantic identities, not allocation-dependent native integer IDs.
export function semanticAssembly(f,refs=Object.fromEntries(f.packets.map(p=>['packet-'+p.id,p.id]))){
 const labels=new Map(Object.entries(refs).map(([label,id])=>[id,label]));
 const charts=new Map(f.charts.map(c=>[c.index,c]));const cells=new Map(f.cells.map(c=>[c.id,c]));
 const packet=p=>{const c=charts.get(p.chart);return {ref:labels.get(p.id),species:c.species,aliases:c.aliases,
  origin:p.origin,permutation:p.permutation,vertices:[...cells.get(c.cell).vertices].sort()};};
 const interfaces=f.operations.map(o=>({source:labels.get(o.source),target:labels.get(o.target),kind:o.kind,
  phaseDelta:o.phaseDelta,permutation:o.permutation,face:o.face?[...o.face].sort():null}));
 return {packets:f.packets.map(packet).sort((a,b)=>a.ref.localeCompare(b.ref)),
  interfaces:interfaces.sort((a,b)=>JSON.stringify(a).localeCompare(JSON.stringify(b))),
  histories:f.histories.map(h=>({word:h.word,packets:h.packets.map(id=>labels.get(id))})),
  comparisonPackets:f.comparisonPackets.map(id=>labels.get(id)),counts:f.audit.counts,
  exits:f.audit.exitPackets.map(id=>labels.get(id)).sort(),certifiedExit:f.audit.certifiedExit};
}
