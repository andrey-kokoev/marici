import assert from 'node:assert/strict';
import {readFileSync,mkdirSync,writeFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {phaseUniverse} from '../origin-bounded-assemblies.mjs';
import {BooleanDiagram} from '../origin-assembly-family.mjs';
const atlasPath='research/nima/results/origin-bounded-assemblies/index.html';
const html=readFileSync(atlasPath,'utf8'),atlas=JSON.parse(html.split('<script id="data" type="application/json">')[1].split('</script>')[0]).cases['2'];
const u=phaseUniverse({maxOrigin:3}),g=u.rules;assert.ok(u.complete);
const signature=(p,charts,cells)=>{const c=charts[p.chart];return JSON.stringify([cells[c.cell].key,c.species,c.aliases,p.origin,p.permutation]);};
const lookup=new Map(u.packets.map(id=>[signature(g.packets[id],g.charts,g.geometry.cells),id]));
const remap=id=>{const p=lookup.get(signature(atlas.packets[id],atlas.charts,atlas.cells));assert.notEqual(p,undefined);return p;};
const cell=p=>g.charts[g.packets[p].chart].cell;
const rows=[],extensions=[],hist={};
function missingAudit(ids){
 const a=g.inspect(ids);assert.ok(a.valid);
 return {counts:a.counts,selectedPackets:ids,allPacketsCanReachExit:a.allPacketsCanReachExit,certifiedExit:a.certifiedExit,
 missing:a.pendingContacts.map(contact=>{
  const candidates=u.operations.filter(i=>{const op=g.operations[i];return contact.cells.includes(cell(op.source))&&contact.cells.includes(cell(op.target))&&cell(op.source)!==cell(op.target);});
  const witnesses=candidates.map(i=>{const op=g.operations[i],added=[...new Set([...ids,op.source,op.target])],d=g.describe(added);return {operation:i,kind:op.kind,source:op.source,target:op.target,origins:[g.packets[op.source].origin,g.packets[op.target].origin],compatible:d.valid,reason:d.reason??null};});
  return {...contact,witnesses,compatibleWitnesses:witnesses.filter(w=>w.compatible).length};
 })};
}
for(let id=0;id<atlas.nodes.length;id++){
 const c=atlas.profiles[atlas.nodes[id][5]].counts;if(c.proton!==7||c.neutron!==7)continue;
 const selected=new Set([remap(atlas.root)]);for(let i=id;atlas.nodes[i][0]>=0;i=atlas.nodes[i][0])selected.add(remap(atlas.operations[atlas.nodes[i][1]].target));
 const ids=[...selected].sort((a,b)=>a-b),a=missingAudit(ids);assert.deepEqual(a.counts,c);rows.push({atlasNode:id,...a});
 const targets=new Set();
 for(const p of ids)for(const oi of g.outgoing(p)){
  const op=g.operations[oi],t=g.packets[op.target],ch=g.charts[t.chart];if(t.origin>3||ch.species!=='neutron'||selected.has(op.target)||targets.has(op.target))continue;targets.add(op.target);
  const ext=[...ids,op.target].sort((a,b)=>a-b),desc=g.describe(ext);if(!desc.valid){hist[desc.reason]=(hist[desc.reason]??0)+1;continue;}
  const b=g.inspect(ext,desc);if(b.counts.neutron!==8)continue;
  assert.equal(b.counts.proton,7);assert.equal(t.origin,3);
  const nucleus=new Set([...desc.bodies].filter(([,s])=>s!=='electron').map(([c])=>c));
  const contacts=desc.contacts.filter(x=>x.cells.includes(ch.cell)&&x.cells.every(c=>nucleus.has(c)));
  extensions.push({atlasNode:id,operation:oi,kind:op.kind,target:op.target,newCell:ch.cell,newNuclearContacts:contacts,...missingAudit(ext)});
 }
}
assert.equal(rows.length,256);assert.equal(extensions.length,464);assert.equal(new Set(extensions.map(x=>x.atlasNode)).size,248);
function summarize(xs){const m={total:xs.length,exitCertified:0,withUnrepairableContactAtD3:0,missingContactKinds:{},contactObstructions:{},compatibleWitnessCounts:{}};
 for(const a of xs){m.exitCertified+=+a.certifiedExit;m.withUnrepairableContactAtD3+=+a.missing.some(x=>!x.compatibleWitnesses);
 for(const c of a.missing){m.missingContactKinds[c.kind]=(m.missingContactKinds[c.kind]??0)+1;const k=c.witnesses.length===0?'no-operation-in-D3-universe':c.compatibleWitnesses?'compatible-witness-available':'all-witnesses-incompatible';m.contactObstructions[k]=(m.contactObstructions[k]??0)+1;m.compatibleWitnessCounts[c.compatibleWitnesses]=(m.compatibleWitnessCounts[c.compatibleWitnesses]??0)+1;}}
 return m;}
// Exact fixed-nuclear-footprint completion: retain all selected records, allow
// extra charts on existing nuclear bodies and arbitrary compatible electrons.
// This is intentionally narrower than all D3 assemblies of the same counts.
const ops=u.operations.map(i=>g.operations[i]);
const parent=new Map(u.packets.map(p=>[p,p]));
const find=p=>parent.get(p)===p?p:find(parent.get(p));
for(const o of ops)if(o.kind==='PN'||o.kind==='inverse-PN')parent.set(find(o.target),find(o.source));
const groups=new Map();for(const p of u.packets){const k=find(p);if(!groups.has(k))groups.set(k,[]);groups.get(k).push(p);}
for(const group of groups.values()){assert.ok(group.length<=2);if(group.length===2)for(const p of group)assert.ok(ops.some(o=>o.source===p&&o.target===group.find(q=>q!==p)));}
const successors=new Map([...groups.keys()].map(k=>[k,new Set()])),indegree=new Map([...groups.keys()].map(k=>[k,0]));
for(const o of ops){const a=find(o.source),b=find(o.target);if(a!==b&&!successors.get(a).has(b)){successors.get(a).add(b);indegree.set(b,indegree.get(b)+1);}}
const topo=[...indegree].filter(([,n])=>!n).map(([k])=>k);for(let i=0;i<topo.length;i++)for(const b of successors.get(topo[i])){indegree.set(b,indegree.get(b)-1);if(!indegree.get(b))topo.push(b);}assert.equal(topo.length,groups.size);
function completeFixedFootprint(row){
 const seed=row.selectedPackets,selected=new Set(seed),desc=g.describe(seed),nuclear=new Map([...desc.bodies].filter(([,s])=>s!=='electron'));
 const candidates=u.packets.filter(p=>{if(selected.has(p))return true;const c=g.charts[g.packets[p].chart];return (c.species==='electron'||nuclear.get(c.cell)===c.species)&&g.describe([...seed,p]).valid;});
 const free=candidates.filter(p=>!selected.has(p)),bdd=new BooleanDiagram(free.length,{maxNodes:200000}),x=new Map(u.packets.map(p=>[p,selected.has(p)?1:0]));free.forEach((p,i)=>x.set(p,bdd.variable(i)));
 let root=1;const both=o=>bdd.and(x.get(o.source),x.get(o.target));
 for(let i=0;i<free.length;i++)for(let j=i+1;j<free.length;j++)if(!g.describe([free[i],free[j]]).valid)root=bdd.and(root,bdd.not(bdd.and(x.get(free[i]),x.get(free[j]))));
 for(const [k,group]of groups){const active=bdd.or(...group.map(p=>x.get(p)));
 if(!group.includes(g.root))root=bdd.and(root,bdd.implies(active,bdd.or(...ops.filter(o=>find(o.target)===k&&find(o.source)!==k).map(both))));
 if(!group.every(p=>g.charts[g.packets[p].chart].species==='electron'))root=bdd.and(root,bdd.implies(active,bdd.or(...ops.filter(o=>find(o.source)===k&&find(o.target)!==k).map(both))));
 }
 root=bdd.and(root,bdd.or(...candidates.filter(p=>g.charts[g.packets[p].chart].species==='electron').map(p=>x.get(p))));
 const bodies=new Map();for(const p of candidates){const c=cell(p);if(!bodies.has(c))bodies.set(c,[]);bodies.get(c).push(p);}
 const cells=[...bodies.keys()];for(let i=0;i<cells.length;i++)for(let j=i+1;j<cells.length;j++){
 const a=cells[i],b=cells[j];if(g.geometry.cells[a].vertices.filter(v=>g.geometry.cells[b].vertices.includes(v)).length!==3)continue;
 const present=bdd.and(bdd.or(...bodies.get(a).map(p=>x.get(p))),bdd.or(...bodies.get(b).map(p=>x.get(p))));
 root=bdd.and(root,bdd.implies(present,bdd.or(...ops.filter(o=>cell(o.source)===a&&cell(o.target)===b||cell(o.source)===b&&cell(o.target)===a).map(both))));
 }
 // Independent necessary-condition audit: even the union of all individually
 // compatible candidates cannot supply exits for these blocked seed records.
 const candidateSet=new Set(candidates),canExit=new Set(candidates.filter(p=>g.charts[g.packets[p].chart].species==='electron'));
 for(let changed=true;changed;){changed=false;for(const o of ops)if(candidateSet.has(o.source)&&candidateSet.has(o.target)&&canExit.has(o.target)&&!canExit.has(o.source)){canExit.add(o.source);changed=true;}}
 const blockedSeedPackets=seed.filter(p=>!canExit.has(p));
 const count=bdd.count(root),models=bdd.models(root,1001);if(blockedSeedPackets.length)assert.equal(count,0n);let witness=null;
 for(const model of models){const ids=[...seed,...model.map(i=>free[i])].sort((a,b)=>a-b),s=new Set(ids),reached=new Set([g.root]),word=[];
 for(let changed=true;changed;){changed=false;for(const o of ops)if(reached.has(o.source)&&s.has(o.target)&&!reached.has(o.target)){reached.add(o.target);word.push(o.id??g.operations.indexOf(o));changed=true;assert.ok(g.describe([...reached]).valid);}}
 assert.equal(reached.size,s.size);const a=g.inspect(ids);assert.ok(a.certifiedExit);assert.equal(a.counts.proton,row.counts.proton);assert.equal(a.counts.neutron,row.counts.neutron);
 if(!witness)witness={packets:ids,counts:a.counts,word};
 }
 return {count:count.toString(),freePackets:free.length,diagramNodes:bdd.nodes.length,checkedModels:models.length,blockedSeedPacketsEvenInRelaxedUnion:blockedSeedPackets,witness};
}
const pn=ops.find(o=>o.source===g.root&&o.kind==='PN'),ne=ops.find(o=>o.source===pn.target&&o.kind==='NE');
const controlIds=[g.root,pn.target,ne.target],control=completeFixedFootprint({selectedPackets:controlIds,counts:g.inspect(controlIds).counts});assert.ok(BigInt(control.count)>0n);assert.ok(control.checkedModels>0);
for(const row of [...rows,...extensions])row.fixedFootprintCompletion=completeFixedFootprint(row);
const completionSummary=xs=>({parents:xs.length,completable:xs.filter(x=>x.fixedFootprintCompletion.count!=='0').length,independentlyBlockedByRelaxedExitUnion:xs.filter(x=>x.fixedFootprintCompletion.blockedSeedPacketsEvenInRelaxedUnion.length).length,completionIncidences:xs.reduce((n,x)=>n+BigInt(x.fixedFootprintCompletion.count),0n).toString(),checkedModels:xs.reduce((n,x)=>n+x.fixedFootprintCompletion.checkedModels,0)});
const degrees={},kinds={};for(const e of extensions){degrees[e.newNuclearContacts.length]=(degrees[e.newNuclearContacts.length]??0)+1;kinds[e.kind]=(kinds[e.kind]??0)+1;}
const report={schema:'marici.nima.nitrogen-contact-extensions.v1',scope:'All D2 atlas N14 selections and their one-new-neutron extensions through D3. Complete D3 packet universe, NOT complete D3 configuration enumeration. No global sewing or physical stability claim.',packetUniverse:u.packets.length,allowedOperations:u.operations.length,n14:summarize(rows),n15Extensions:summarize(extensions),extendableN14Parents:new Set(extensions.map(x=>x.atlasNode)).size,newNeutronNuclearContactDegrees:degrees,extensionKinds:kinds,rejectedTargets:hist,fixedFootprintCompletion:{positiveControl:control,n14:completionSummary(rows),n15:completionSummary(extensions),scope:'Exact D3 supersets retaining selected history and nuclear footprint; electrons unrestricted. Counts are parent-completion incidences, not globally unique assemblies.'},
 sourceHashes:Object.fromEntries([atlasPath,'research/nima/origin-bounded-assemblies.mjs','research/nima/generative-phase-assembly.mjs','research/nima/checkers/check_nitrogen_contact_extensions.mjs'].map(p=>[p,createHash('sha256').update(readFileSync(p)).digest('hex')])),rows,extensions,
 registry:{packets:g.packets,charts:g.charts,cells:g.geometry.cells.map(({owner,...c})=>c),operations:g.operations,allowedOperations:u.operations}};
const out='research/nima/results/nitrogen-contact-extensions';mkdirSync(out,{recursive:true});writeFileSync(out+'/verification.json',JSON.stringify(report,null,2)+'\n');
const {rows:_,extensions:__,registry:___,...summary}=report;console.log(JSON.stringify(summary,null,2));
