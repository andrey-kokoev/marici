import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';

// Global incidence assignments for the operator's layered proposal. This does
// not impose the earlier periodic model's coordinate-axis wire pairing.
const s=buildPESymmetricSector(1),axes=[[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]];
const key=vs=>vs.map(v=>v.join(',')).sort().join('|');
const center=c=>[0,1,2,3].map(i=>c.vertices.reduce((n,q)=>n+q[i],0)/c.vertices.length);
const byShape=new Map(s.cells.map(c=>[key(c.vertices),c]));
const adjacent=(c,ids)=>s.faces.some(f=>f.owners.includes(c.id)&&f.owners.some(id=>id!==c.id&&ids.includes(id)));
const results=[];
for(const [axisIndex,a] of axes.entries())for(const sign of [-1,1]){
 const height=c=>Math.round(a.reduce((z,x,i)=>z+x*(center(c)[i]-s.centre[i]),0)*2)/4;
 const mirror=c=>byShape.get(key(c.vertices.map(q=>{const x=a.reduce((z,v,i)=>z+v*(q[i]-s.centre[i]),0)/2;return q.map((v,i)=>v-x*a[i]);})));
 const mid=s.cells.filter(c=>c.role==='neutron'&&height(c)===0),groups=new Map(),central=[];
 for(const c of mid){
  assert.equal(mirror(c).id,c.id);
  const r2=center(c).reduce((n,x,i)=>n+(x-s.centre[i])**2,0);
  if(r2<.1){central.push(c.id);continue;}
  const dual=byShape.get(key(c.vertices.map(q=>q.map((x,i)=>2*s.centre[i]-x))));
  const id=r2>3?[c.id,dual.id].sort()[0]:c.id;
  if(!groups.has(id))groups.set(id,[]);groups.get(id).push(c.id);
 }
 assert.equal(mid.length,9);assert.equal(groups.size,6);assert.equal(central.length,1);
 assert.equal([...groups.values()].filter(ids=>ids.length===2).length,2);
 function matchings(role){
  const cells=s.cells.filter(c=>height(c)===sign*.5&&c.role===role),out=[];assert.equal(cells.length,6);
  function go(i,used,pairs){
   if(i===cells.length){out.push(pairs);return;}
   for(const [channel,members] of groups)if(!used.has(channel)&&adjacent(cells[i],members))go(i+1,new Set([...used,channel]),[...pairs,{cell:cells[i],channel}]);
  }
  go(0,new Set(),[]);return out;
 }
 const p=matchings('proton'),e=matchings('electron');assert.equal(p.length,2);assert.equal(e.length,2);
 const assignments=[];
 for(const ps of p)for(const es of e){
  const routes=[...groups].map(([channel,members])=>{
   const sourceP=ps.find(r=>r.channel===channel).cell,sourceE=es.find(r=>r.channel===channel).cell,targetE=mirror(sourceP),targetP=mirror(sourceE);
   assert.equal(targetE.role,'electron');assert.equal(targetP.role,'proton');
   for(const c of [targetP,targetE]){assert.equal(height(c),-sign*.5);assert(adjacent(c,members));assert.equal(mirror(mirror(c)).id,c.id);}
   return {channel,members,sourceP:sourceP.id,sourceE:sourceE.id,targetP:targetP.id,targetE:targetE.id};
  });
  for(const side of ['sourceP','sourceE','targetP','targetE'])assert.equal(new Set(routes.map(r=>r[side])).size,6);
  assignments.push(routes);
 }
 results.push({axisIndex,incomingSign:sign,middleCells:9,peripheralChannels:6,centralCell:central[0],assignments});
}
const report={status:'six-peripheral-channels-suffice-for-incidence-recombination',testedOrientations:results.length,assignmentsPerOrientation:4,results,scope:'Complete P/E face-incidence cover on both adjacent planes, using six peripheral N groups and no central cell. Recombination allowed; not a binding of signed input strands, not uniqueness, and not verification under the earlier coordinate-axis wire rule.'};
const out='research/strominger/results/sulfur-32-middle-layer';await fs.mkdir(out,{recursive:true});await fs.writeFile(out+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log(JSON.stringify({status:report.status,testedOrientations:results.length,assignmentsPerOrientation:4,middleNCells:9,peripheralChannels:6,centralCellsUnused:1},null,2));
