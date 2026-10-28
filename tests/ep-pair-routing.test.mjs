import test from 'node:test';import assert from 'node:assert/strict';
import {routeEpPairs} from '../research/realization-tower/ep-pair-routing.mjs';
import {beltViewerPoint} from '../research/realization-tower/neutron-belt-process.mjs';
// Archived trial fixture: independent of the evolving live belt layout.
function fixture(){
 const structures=[],bodies=[],links=[],square=[];
 for(const [layer,count] of [[1,3],[2,2],[4,2],[5,3]])for(let column=0;column<count;column++){
  const id=`ring:${layer}:${column}`,nodeIds=[];
  for(let i=0;i<6;i++){const node=`${id}:${i}`,angle=i*Math.PI/3;nodeIds.push(node);bodies.push({id:node,role:i%2?'electron':'proton',point:beltViewerPoint([(column-(count-1)/2)*1.6+.55*Math.cos(angle),.55*Math.sin(angle),(3-layer)*1.05]),beltPort:{layer}});}
  structures.push({id,layer,nodeIds});for(let i=0;i<6;i++)links.push({from:nodeIds[i],to:nodeIds[(i+1)%6]});
 }
 for(const [i,[x,y,role]] of [[-.4,.4,'electron'],[.4,.4,'proton'],[.4,-.4,'electron'],[-.4,-.4,'proton']].entries()){const id=`square:${i}`;square.push(id);bodies.push({id,role,point:beltViewerPoint([x,y,0]),beltPort:{layer:3}});}
 for(let i=0;i<4;i++)links.push({from:square[i],to:square[(i+1)%4]});return {structures,bodies,links,square};
}
test('archived EP pair routing respects capacities and square cut',()=>{
 const f=fixture(),before=JSON.stringify(f),run=()=>routeEpPairs(f.structures,f.square,f.bodies,f.links),trial=run(),a=trial.audit,byId=new Map(f.bodies.map(b=>[b.id,b])),all=[...f.links,...trial.links];
 assert.equal(a.pairCableCount,16);assert.equal(a.addedLinks,32);assert.equal(a.connectedNodes,64);assert.equal(a.totalNodes,64);assert.equal(a.maxDegree,4);assert.equal(a.centralSquareRequired,true);
 for(const b of f.bodies)assert.ok(all.filter(e=>e.from===b.id||e.to===b.id).length<=4);
 for(const c of a.cables){assert.equal(c.endpoints.length,2);for(const e of c.endpoints){assert.notEqual(byId.get(e.from).role,byId.get(e.to).role);assert.equal(Math.abs(byId.get(e.from).beltPort.layer-byId.get(e.to).beltPort.layer),1);}}
 assert.equal(new Set(all.map(e=>[e.from,e.to].sort().join('|'))).size,all.length);
 const seen=new Set(),queue=[f.structures[0].nodeIds[0]],blocked=new Set(f.square);while(queue.length){const id=queue.pop();if(seen.has(id)||blocked.has(id))continue;seen.add(id);for(const e of all)if(e.from===id)queue.push(e.to);else if(e.to===id)queue.push(e.from);}
 assert.equal(seen.size,30);assert.ok([...seen].every(id=>byId.get(id).beltPort.layer<3));assert.deepEqual(a,run().audit);assert.equal(JSON.stringify(f),before);
});
