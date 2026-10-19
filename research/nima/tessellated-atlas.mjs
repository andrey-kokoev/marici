import assert from 'node:assert/strict';
import {contractionUniverse,inspectContraction} from './experimental-terminal-pe.mjs';
import {materializationCandidates} from './body-coherent-materialization.mjs';
import {searchExtension} from './guarded-extension-search.mjs';

// Independent compiler from native source objects, not a saved atlas or path catalog.
export function compileTessellatedAtlas({maxOrigin,mode='experimental-terminal-PE'}={}){
 assert.ok(['native','experimental-terminal-PE'].includes(mode));
 const universe=contractionUniverse({maxOrigin}),g=universe.rules,packets=[...universe.packets],index=new Map(packets.map((p,i)=>[p,i])),bits=packets.map((_,i)=>1n<<BigInt(i));
 const mask=ids=>ids.reduce((m,p)=>{assert.ok(index.has(p),'Packet outside bounded universe');return m|bits[index.get(p)];},0n),decode=m=>packets.filter((p,i)=>!!(m&bits[i]));
 const cell=p=>g.charts[g.packets[p].chart].cell,native=universe.operations.map(i=>g.operations[i]);
 const interfaces=native.map(o=>({...o,nativeFactors:[o.id],forbidden:0n}));
 if(mode!=='native')for(const o of universe.shortcuts){const forbidden=packets.filter(p=>cell(p)===o.referenceNeutronCell||native.some(n=>n.source===o.source&&n.target===p));interfaces.push({...o,forbidden:mask(forbidden)});}
 interfaces.forEach((o,i)=>{o.index=i;o.bit=1n<<BigInt(i);o.sourceBit=bits[index.get(o.source)];o.targetBit=bits[index.get(o.target)];o.required=o.sourceBit|o.targetBit;});
 const conflicts=packets.map(()=>0n);for(let i=0;i<packets.length;i++)for(let j=i+1;j<packets.length;j++)if(!g.describe([packets[i],packets[j]]).valid){conflicts[i]|=bits[j];conflicts[j]|=bits[i];}
 const cells=[...new Set(packets.map(cell))],bodyMasks=new Map(cells.map(c=>[c,mask(packets.filter(p=>cell(p)===c))]));
 const contacts=[];for(let i=0;i<cells.length;i++)for(let j=i+1;j<cells.length;j++){
  const a=cells[i],b=cells[j],face=g.geometry.cells[a].vertices.filter(v=>g.geometry.cells[b].vertices.includes(v));if(face.length!==3)continue;
  const witnesses=interfaces.filter(o=>o.kind!=='experimental-terminal-PE'&&cell(o.source)!==cell(o.target)&&[a,b].includes(cell(o.source))&&[a,b].includes(cell(o.target)));
  contacts.push({cells:[a,b],face,witnesses:witnesses.map(o=>o.index),witnessMask:witnesses.reduce((m,o)=>m|o.bit,0n)});
 }
 const root=bits[index.get(g.root)],exits=mask(packets.filter(p=>g.charts[g.packets[p].chart].species==='electron'));
 const enabled=(o,m)=>(m&o.required)===o.required&&!(m&o.forbidden),active=m=>interfaces.reduce((a,o)=>enabled(o,m)?a|o.bit:a,0n);
 const watchers=bits.map(b=>interfaces.filter(o=>!!((o.required|o.forbidden)&b)));
 function update(a,m,slot){for(const o of watchers[slot])a=enabled(o,m)?a|o.bit:a&~o.bit;return a;}
 function reach(m,a,reverse=false){let seen=reverse?m&exits:root;for(let previous=-1n;previous!==seen;){previous=seen;for(const o of interfaces)if(a&o.bit){const from=reverse?o.targetBit:o.sourceBit,to=reverse?o.sourceBit:o.targetBit;if(seen&from)seen|=to;}}return seen;}
 function compatible(m){for(let i=0;i<bits.length;i++)if((m&bits[i])&&(m&conflicts[i]))return false;return true;}
 function obligations(m,a=active(m)){
  const missingContacts=contacts.filter(c=>(m&bodyMasks.get(c.cells[0]))&&(m&bodyMasks.get(c.cells[1]))&&!(a&c.witnessMask));
  const unrooted=m&~reach(m,a),noExit=m&~reach(m,a,true);
  return {unrooted,noExit,missingContacts,certified:!!(m&root)&&compatible(m)&&!unrooted&&!noExit&&missingContacts.length===0};
 }
 // Static geometry and marked records are separate: no quotient by shape or origin parity.
 const geometry={kind:'native-tetrahedron-octahedron',cells:cells.map(id=>{const c=g.geometry.cells[id];return {id,key:c.key,geometry:c.geometry,vertices:[...c.vertices],faces:c.faces.map(f=>[...f])};}),contacts:contacts.map(({cells,face})=>({cells,face}))};
 const readers=packets.map(p=>({packet:p,...g.packets[p],cell:cell(p),chartData:structuredClone(g.charts[g.packets[p].chart])}));
 return {universe,mode,packets,index,bits,mask,decode,interfaces,conflicts,root,active,update,reach,compatible,obligations,geometry,readers,fieldAttachment:{status:'unbound',affectsAdmission:false}};
}

// Obligations prioritize additions, but exploratory moves remain: no missing-face pruning.
export function generateTessellatedAtlas(c,{maxConfigurations=1000000}={}){
 assert.ok(Number.isInteger(maxConfigurations)&&maxConfigurations>=1);
 const nodes=[{mask:c.root,active:c.active(c.root),parent:-1,added:null,via:null}],byMask=new Map([[c.root,0]]),rejected=new Set();let priorityAdditions=0;
 for(let from=0;from<nodes.length;from++){
  const n=nodes[from],needs=c.obligations(n.mask,n.active);let targets=0n,preferred=0n;
  for(const f of needs.missingContacts)for(const i of f.witnesses)preferred|=c.interfaces[i].required;
  for(const o of c.interfaces)if(n.mask&o.sourceBit){targets|=o.targetBit;if(needs.noExit&o.sourceBit)preferred|=o.targetBit;}
  targets&=~n.mask;preferred&=targets;
  const slots=c.bits.map((b,i)=>i).filter(i=>!!(targets&c.bits[i]));slots.sort((a,b)=>Number(!!(preferred&c.bits[b]))-Number(!!(preferred&c.bits[a]))||a-b);
  for(const slot of slots){if(n.mask&c.conflicts[slot])continue;const m=n.mask|c.bits[slot];if(byMask.has(m)||rejected.has(m))continue;
   const a=c.update(n.active,m,slot);if(c.reach(m,a)!==m){rejected.add(m);continue;}
   const edge=c.interfaces.find(o=>(n.mask&o.sourceBit)&&o.targetBit===c.bits[slot]&&(a&o.bit));assert.ok(edge);
   if(nodes.length>=maxConfigurations)return {complete:false,reason:'configuration-resource-limit',nodes,byMask,priorityAdditions};
   priorityAdditions+=Number(!!(preferred&c.bits[slot]));byMask.set(m,nodes.length);nodes.push({mask:m,active:a,parent:from,added:c.packets[slot],via:edge.index});
  }
 }
 return {complete:true,nodes,byMask,priorityAdditions};
}

export function materializeBody(c,ids){
 assert.equal(c.mode,'experimental-terminal-PE','Materialization belongs to the experimental grammar');
 return materializationCandidates(c.universe,ids).map(m=>({...m,kind:'atomic-body-materialization',admitted:m.certified,obligations:m.valid?c.obligations(c.mask(m.selected)):null}));
}

// Plan obligations in required sets; intermediates here are not asserted rooted transitions.
// A returned certificate must be separately scheduled or treated as an audited atomic target.
export function closeContactObligations(c,ids,{maxNodes=5000,maxMilliseconds=5000}={}){
 assert.equal(c.mode,'experimental-terminal-PE');const start=performance.now(),seen=new Set();let nodes=0,faceBranches=0;
 function visit(required){
  const elapsed=performance.now()-start;if(nodes>=maxNodes||elapsed>=maxMilliseconds)return {status:'incomplete',reason:'closure-resource-limit'};
  nodes++;const m=c.mask(required),key=m.toString();if(seen.has(key))return {status:'unsat'};seen.add(key);if(!c.compatible(m))return {status:'unsat'};
  const needs=c.obligations(m);if(needs.certified)return {status:'sat',selectedPackets:c.decode(m)};
  if(needs.missingContacts.length){
   const choices=needs.missingContacts.map(f=>({f,edges:f.witnesses.map(i=>c.interfaces[i]).filter(o=>c.compatible(m|o.required))})).sort((a,b)=>a.edges.length-b.edges.length)[0];
   for(const edge of choices.edges){faceBranches++;const answer=visit(c.decode(m|edge.required));if(answer.status!=='unsat')return answer;}return {status:'unsat'};
  }
  const answer=searchExtension(c.universe,required,{maxNodes:maxNodes-nodes,maxMilliseconds:Math.max(0,maxMilliseconds-(performance.now()-start))});nodes+=answer.nodes;return answer;
 }
 const result=visit([...new Set([c.universe.rules.root,...ids])]);if(result.status==='sat'){const a=inspectContraction(c.universe,result.selectedPackets);assert.ok(a.certifiedExit&&ids.every(p=>result.selectedPackets.includes(p)));}
 return {...result,nodes,faceBranches,elapsedMilliseconds:performance.now()-start,scope:'Required-set completion, not an implicit singleton schedule; unsat is an algorithmic outcome, not a serialized proof certificate.'};
}
