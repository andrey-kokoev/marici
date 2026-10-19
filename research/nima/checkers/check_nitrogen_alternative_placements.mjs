import assert from 'node:assert/strict';
import {readFileSync,writeFileSync,mkdirSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {phaseUniverse} from '../origin-bounded-assemblies.mjs';
import {fileURLToPath} from 'node:url';
import {resolve} from 'node:path';

// Finite CNF search. Packet variables preserve origin, chart and full map;
// body variables count occupied cells, never retained packet multiplicity.
export function compile(D,{exits=true}={}){
 const universe=phaseUniverse({maxOrigin:D});assert.ok(universe.complete);
 const {rules:g}=universe,packets=universe.packets,ops=universe.operations.map(i=>g.operations[i]);
 let n=0;const variable=()=>++n,clauses=[],add=(...l)=>clauses.push([...new Set(l)]);
 const x=new Map(packets.map(p=>[p,variable()]));add(x.get(g.root));
 const and=vs=>{const y=variable();for(const v of vs)add(-y,v);add(y,...vs.map(v=>-v));return y;};
 const or=vs=>{const y=variable();add(-y,...vs);for(const v of vs)add(-v,y);return y;};
 const edge=ops.map(o=>and([x.get(o.source),x.get(o.target)]));
 for(let i=0;i<packets.length;i++)for(let j=i+1;j<packets.length;j++)if(!g.describe([packets[i],packets[j]]).valid)add(-x.get(packets[i]),-x.get(packets[j]));
 const parent=new Map(packets.map(p=>[p,p])),find=p=>parent.get(p)===p?p:find(parent.get(p));
 for(const o of ops)if(o.kind==='PN'||o.kind==='inverse-PN')parent.set(find(o.source),find(o.target));
 const groups=new Map();for(const p of packets){const k=find(p);if(!groups.has(k))groups.set(k,[]);groups.get(k).push(p);}
 for(const group of groups.values()){assert.ok(group.length<=2);if(group.length===2)for(const p of group)assert.ok(ops.some(o=>o.source===p&&o.target===group.find(q=>q!==p)));}
 const successors=new Map([...groups.keys()].map(k=>[k,new Set()])),degree=new Map([...groups.keys()].map(k=>[k,0]));
 for(const o of ops){const a=find(o.source),b=find(o.target);if(a!==b&&!successors.get(a).has(b)){successors.get(a).add(b);degree.set(b,degree.get(b)+1);}}
 const topo=[...degree].filter(([,v])=>!v).map(([k])=>k);for(let i=0;i<topo.length;i++)for(const b of successors.get(topo[i])){degree.set(b,degree.get(b)-1);if(!degree.get(b))topo.push(b);}assert.equal(topo.length,groups.size);
 for(const [k,group]of groups){
 const incoming=ops.flatMap((o,i)=>find(o.target)===k&&find(o.source)!==k?[edge[i]]:[]);
 const outgoing=ops.flatMap((o,i)=>find(o.source)===k&&find(o.target)!==k?[edge[i]]:[]);
 for(const p of group){if(!group.includes(g.root))add(-x.get(p),...incoming);if(exits&&!group.every(q=>g.charts[g.packets[q].chart].species==='electron'))add(-x.get(p),...outgoing);}
 }
 const bodyMap=new Map();for(const p of packets){const c=g.charts[g.packets[p].chart],k=c.cell+':'+c.species;if(!bodyMap.has(k))bodyMap.set(k,{cell:c.cell,species:c.species,packets:[]});bodyMap.get(k).packets.push(p);}
 const bodies=[...bodyMap.values()];for(const b of bodies)b.variable=or(b.packets.map(p=>x.get(p)));
 if(exits){add(...bodies.filter(b=>b.species==='electron').map(b=>b.variable));
 for(let i=0;i<bodies.length;i++)for(let j=i+1;j<bodies.length;j++){
 const a=bodies[i],b=bodies[j];if(a.cell===b.cell||g.geometry.cells[a.cell].vertices.filter(v=>g.geometry.cells[b.cell].vertices.includes(v)).length!==3)continue;
 const links=ops.flatMap((o,i)=>a.packets.includes(o.source)&&b.packets.includes(o.target)||b.packets.includes(o.source)&&a.packets.includes(o.target)?[edge[i]]:[]);
 add(-a.variable,-b.variable,...links);
 }}
 return {g,universe,ops,x,bodies,n,clauses,exits};
}
export function solve(f,counts,{extra=[],maxNodes=1000000,maxMilliseconds=Infinity}={}){
 const started=Date.now();
 const clauses=[...f.clauses,...extra],cards=Object.entries(counts).map(([s,count])=>({vars:f.bodies.filter(b=>b.species===s).map(b=>b.variable),count}));let nodes=0;
 const assign=(a,l)=>{const v=Math.abs(l),value=l>0?1:-1;if(a[v]&&a[v]!==value)return false;a[v]=value;return true;};
 function visit(a){if(++nodes>maxNodes)throw Error('search-node-resource-limit');if(Date.now()-started>maxMilliseconds)throw Error('search-time-resource-limit');
 for(let changed=true;changed;){changed=false;
 for(const c of clauses){let satisfied=false,free=0,last=0;for(const l of c){const v=a[Math.abs(l)];if(v===(l>0?1:-1)){satisfied=true;break;}if(!v){free++;last=l;}}
 if(satisfied)continue;if(!free)return null;if(free===1){if(!assign(a,last))return null;changed=true;}}
 for(const {vars,count}of cards){let yes=0;const free=[];for(const v of vars){if(a[v]===1)yes++;else if(!a[v])free.push(v);}if(yes>count||yes+free.length<count)return null;
 if(free.length&&(yes===count||yes+free.length===count)){for(const v of free)a[v]=yes===count?-1:1;changed=true;}}
 }
 // Choose the most frequent unresolved variable in shortest open clauses.
 let shortest=Infinity;const scores=new Map();for(const c of clauses){if(c.some(l=>a[Math.abs(l)]===(l>0?1:-1)))continue;const free=c.filter(l=>!a[Math.abs(l)]);if(free.length<shortest){shortest=free.length;scores.clear();}if(free.length===shortest)for(const l of free)scores.set(Math.abs(l),(scores.get(Math.abs(l))??0)+1);}
 let v=[...scores].sort((a,b)=>b[1]-a[1])[0]?.[0];if(!v)v=cards.flatMap(c=>c.vars).find(v=>!a[v]);if(!v)return a;
 for(const value of [-1,1]){const b=a.slice();b[v]=value;const answer=visit(b);if(answer)return answer;}return null;
 }
 try{const a=visit(new Int8Array(f.n+1));if(a){for(const c of clauses)assert.ok(c.some(l=>a[Math.abs(l)]===(l>0?1:-1)));for(const c of cards)assert.equal(c.vars.filter(v=>a[v]===1).length,c.count);}return {status:a?'sat':'unsat',nodes,assignment:a};}catch(e){if(!['search-node-resource-limit','search-time-resource-limit'].includes(e.message))throw e;return {status:'incomplete',nodes,reason:e.message};}
}
export function witness(f,a){const ids=[...f.x].filter(([,v])=>a[v]===1).map(([p])=>p),selected=new Set(ids),reached=new Set([f.g.root]),word=[];
 for(let changed=true;changed;){changed=false;for(const o of f.ops)if(reached.has(o.source)&&selected.has(o.target)&&!reached.has(o.target)){reached.add(o.target);word.push(f.g.operations.indexOf(o));changed=true;assert.ok(f.g.describe([...reached]).valid);}}
 assert.equal(reached.size,selected.size);const audit=f.g.inspect(ids);assert.ok(audit.valid);if(f.exits)assert.ok(audit.certifiedExit);
 return {packets:ids,word,grade:Math.max(...ids.map(p=>f.g.packets[p].origin)),counts:audit.counts,certifiedExit:audit.certifiedExit,pendingContacts:audit.pendingContacts,allPacketsCanReachExit:audit.allPacketsCanReachExit,nuclearFootprint:f.bodies.filter(b=>b.species!=='electron'&&a[b.variable]===1).map(b=>({cell:b.cell,species:b.species}))};}
if(process.argv[1]&&resolve(process.argv[1])===fileURLToPath(import.meta.url)){
// Truth-table controls for generic DPLL plus native positive/negative controls.
for(let mask=0;mask<256;mask++){
 const clauses=Array.from({length:8},(_,i)=>i).filter(i=>mask&(1<<i)).map(i=>[0,1,2].map(j=>(i&(1<<j)?1:-1)*(j+1)));
 const f={clauses,n:3,bodies:[]},s=solve(f,{});const expected=Array.from({length:8},(_,i)=>i).some(i=>clauses.every(c=>c.some(l=>Boolean(i&(1<<(Math.abs(l)-1)))===(l>0))));assert.equal(s.status,expected?'sat':'unsat');
}
const control=compile(0);assert.equal(solve(control,{proton:1,neutron:1,electron:1}).status,'sat');assert.equal(solve(control,{proton:2}).status,'unsat');witness(control,solve(control,{proton:1,neutron:1,electron:1}).assignment);
for(let count=0;count<=5;count++)for(let mask=0;mask<16;mask++){
 const bodies=Array.from({length:4},(_,i)=>({species:'proton',variable:i+1})),clauses=bodies.filter((_,i)=>mask&(1<<i)).map(b=>[b.variable]);
 const result=solve({n:4,bodies,clauses},{proton:count});const expected=count<=4&&clauses.length<=count;assert.equal(result.status,expected?'sat':'unsat');}
const report={schema:'marici.nima.nitrogen-alternative-placements.v1',scope:'Search from seed, no retained D2 footprint/history. Exact nuclear counts; electrons unrestricted. Local selected-record exit only, not global sewing or physical stability.',controls:354,cases:[]};
for(const exits of [true,false]){
 const model=compile(3,{exits});
 for(const neutron of [7,8]){
 const extra=[],results=[];let stop='witness-limit';
 for(let i=0;i<5;i++){
 const s=solve(model,{proton:7,neutron},{extra,maxNodes:1000000});const {assignment,...meta}=s;
 if(s.status!=='sat'){results.push(meta);stop=s.status;break;}
 const w=witness(model,assignment);assert.equal(w.counts.proton,7);assert.equal(w.counts.neutron,neutron);results.push({...meta,witness:w});
 // Block exactly this nuclear footprint, not merely this packet selection.
 extra.push(model.bodies.filter(b=>b.species!=='electron').map(b=>assignment[b.variable]===1?-b.variable:b.variable));
 }
 const row={maxOrigin:3,neutron,proton:7,requireExit:exits,packetUniverse:model.universe.packets.length,variables:model.n,clauses:model.clauses.length,stop,results};report.cases.push(row);console.log(JSON.stringify(row));
 }
 report.registry={packets:model.g.packets,charts:model.g.charts,cells:model.g.geometry.cells.map(({owner,...c})=>c),operations:model.g.operations};
}
// Independent regression against all previously validated D0/D1/D2 exit
// selections. Block packets rather than auxiliary CNF assignments.
report.exitFamilyRegression=[];
for(const [D,expected]of [[0,1],[1,14],[2,459]]){
 const f=compile(D),extra=[];let count=0;
 while(true){const s=solve(f,{}, {extra});assert.notEqual(s.status,'incomplete');if(s.status==='unsat')break;witness(f,s.assignment);count++;assert.ok(count<=expected);extra.push([...f.x.values()].map(v=>s.assignment[v]===1?-v:v));}
 assert.equal(count,expected);report.exitFamilyRegression.push({maxOrigin:D,count,exhausted:true});
}
const neutralModel=compile(3);report.neutralCompositionTests=[];
for(const neutron of [7,8]){const s=solve(neutralModel,{proton:7,neutron,electron:7}),{assignment,...meta}=s;report.neutralCompositionTests.push({neutron,...meta,...(assignment?{witness:witness(neutralModel,assignment)}:{})});}
const previousPath='research/nima/results/nitrogen-contact-extensions/verification.json',previous=JSON.parse(readFileSync(previousPath,'utf8'));
const footprint=(packets,r)=>new Set(packets.map(p=>r.charts[r.packets[p].chart]).filter(c=>c.species!=='electron').map(c=>c.species+':'+r.cells[c.cell].key));
for(const row of report.cases)for(const result of row.results)if(result.witness){
 const current=footprint(result.witness.packets,report.registry),old=row.neutron===7?previous.rows:previous.extensions;let nearest=null;
 for(const a of old){const f=footprint(a.selectedPackets,previous.registry),removed=[...f].filter(k=>!current.has(k)),added=[...current].filter(k=>!f.has(k));if(!nearest||removed.length<nearest.removed.length)nearest={previousAtlasNode:a.atlasNode,previousExtensionOperation:a.operation??null,removed,added};}
 result.witness.nearestPreviousFootprint=nearest;
 if(row.requireExit)assert.ok(nearest.removed.length>0,'Exit-certified witness should not retain a previously impossible fixed footprint');
}
report.sourceHashes=Object.fromEntries([previousPath,'research/nima/checkers/check_nitrogen_alternative_placements.mjs','research/nima/origin-bounded-assemblies.mjs','research/nima/generative-phase-assembly.mjs'].map(p=>[p,createHash('sha256').update(readFileSync(p)).digest('hex')]));
const out='research/nima/results/nitrogen-alternative-placements';mkdirSync(out,{recursive:true});writeFileSync(out+'/verification.json',JSON.stringify(report,null,2)+'\n');
}
