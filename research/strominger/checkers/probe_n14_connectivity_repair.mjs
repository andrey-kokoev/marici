// Necessary-condition search only: deliberately optimistic graph reachability.
// Dropping pair guards/global diagonal consistency makes failures decisive
// within the stated universe, but successes are NOT admitted witnesses.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {phaseUniverse} from '../../nima/origin-bounded-assemblies.mjs';
import {mixedUniverse} from './mixed-subdivision-model.mjs';
const source='research/strominger/results/reference-n15-search/D4-verification.json',bytes=await readFile(source),w=JSON.parse(bytes).witness,out='research/strominger/results/n14-connectivity-repair';
const bodyKey=b=>b.key+':'+b.species,results=[];
function graph(u,mixed){
 const r=u.rules,keys=new Map(u.packets.map(p=>{const c=r.charts[r.packets[p].chart];return [p,r.geometry.cells[c.cell].key+':'+c.species];})),adj=new Map(u.packets.map(p=>[p,[]]));
 const ops=mixed?u.operations:u.operations.map(i=>r.operations[i]);for(const o of ops)adj.get(o.source).push(o.target);
 const roots=mixed?u.roots:[r.root];
 function reach(wanted){const visited=new Set(roots.filter(p=>wanted.has(keys.get(p)))),queue=[...visited];for(let i=0;i<queue.length;i++)for(const p of adj.get(queue[i])??[])if(wanted.has(keys.get(p))&&!visited.has(p)){visited.add(p);queue.push(p);}const covered=new Set(queue.map(p=>keys.get(p)));return {reachedPackets:queue.length,missing:[...wanted].filter(k=>!covered.has(k))};}
 return {keys,reach};
}
for(const [kind,maxOrigin] of [['uniform',4],['uniform',10],['mixed',8]]){
 const mixed=kind==='mixed',u=mixed?mixedUniverse({maxOrigin}):phaseUniverse({maxOrigin,maxPackets:5000});assert.equal(u.complete,true);const g=graph(u,mixed),neutronSites=[...new Set([...g.keys.values()].filter(k=>k.endsWith(':neutron')))];
 for(const deleted of [8,12]){
  const bodies=w.bodies.filter(b=>b.cell!==deleted),wanted=new Set(bodies.map(bodyKey)),fixed=g.reach(wanted),trials=[],passing=[];
  for(const old of bodies.filter(b=>b.species==='neutron'))for(const replacement of neutronSites){
   if(wanted.has(replacement))continue;const next=new Set(wanted);next.delete(bodyKey(old));next.add(replacement);const r=g.reach(next);trials.push(r.missing.length);if(!r.missing.length)passing.push({movedCell:old.cell,replacement});
  }
  const row={kind,maxOrigin,universePackets:u.packets.length,universeComplete:u.complete,deletedNeutron:deleted,fixedGeometry:{...fixed,missingBodies:bodies.filter(b=>fixed.missing.includes(bodyKey(b))).map(b=>({originalCell:b.cell,species:b.species,key:b.key}))},singleNeutronRelocations:{tested:trials.length,optimisticPasses:passing.length,minimumMissingBodies:Math.min(...trials),passing}};results.push(row);console.log(JSON.stringify({...row,singleNeutronRelocations:{...row.singleNeutronRelocations,passing:passing.slice(0,3)}}));
 }
}
// Identify direct saved-word links removed by each deletion.
const packet=new Map(w.packets.map(p=>[p.id,p])),sourceRules=phaseUniverse({maxOrigin:4,maxPackets:5000}).rules,cell=p=>sourceRules.charts[packet.get(p).chart].cell;
const cutLinks=[8,12].map(deleted=>({deletedNeutron:deleted,operations:w.operations.filter(o=>cell(o.source)===deleted||cell(o.target)===deleted).map(o=>({id:o.id,kind:o.kind,source:o.source,target:o.target,sourceCell:cell(o.source),targetCell:cell(o.target),sourceOrigin:packet.get(o.source).origin,targetOrigin:packet.get(o.target).origin}))}));
await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify({status:'optimistic-connectivity-repair-probed',source,sourceSha256:createHash('sha256').update(bytes).digest('hex'),results,cutLinks,scope:'Fixed N-15-minus-one-neutron body sites, plus relocating exactly one remaining neutron while keeping all P/E sites and all other N sites fixed. All generated readers allowed, even mutually incompatible ones. Mixed graph additionally permits mutually inconsistent diagonal choices and all three root charts. Therefore failures exclude actual witnesses in the tested family; passes require full solver and replay. No full phase/contact certificate claimed. Uniform bounds 4 and 10, mixed bound 8, no unbounded or physical conclusion.'},null,2)+'\n');
