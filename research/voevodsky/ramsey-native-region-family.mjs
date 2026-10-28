// Prepared indexed INPUT contexts, not paths from the canonical seed.
import {GenerativeAssemblyRules} from '../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {makeLatticeItem} from '../strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {phaseFrame} from '../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {packetSnapshot,same} from './ramsey-native-word-trace.mjs';
const need=(c,m)=>{if(!c)throw new RangeError(m);},copy=x=>structuredClone(x);
export function region3(){const a=[];for(let x=-3;x<=3;x++)for(let y=-3;y<=3;y++)for(let z=-3;z<=3;z++)if((x+y+z)%2===0)a.push([x,y,z]);return a;}
export function shift4([x,y,z]){need([x,y,z].every(Number.isSafeInteger)&&(x+y+z)%2===0,'not a lattice point');return [-(x+y+z)/2,(x+y-z)/2,(x+z-y)/2,(y+z-x)/2];}
export function project4(v){const b=typeof v==='string'?v.split(',').map(Number):v;return [b[1]+b[2],b[1]+b[3],b[2]+b[3]];}
export function prepareRegion(...args){
 need(args.length===0,'prepared family takes no word or answer parameter');
 const rules=new GenerativeAssemblyRules(),rows=[],ids=[];
 for(const point of region3()){
  const owner=makeLatticeItem('tetrahedron',shift4(point)),cell=rules.geometry.register(owner,owner.components[0]);
  const aliases=Object.fromEntries(['C0','M0','C1','M1'].map((n,i)=>[n,owner.vertices[i].join(',')]));
  const chart=rules.completeP(cell,aliases);need(chart!==null,'prepared source reference unavailable');
  const packet=rules.packet(chart,0,[0,1,2,3,4]),ops=rules.outgoing(packet).map(i=>rules.operations[i]).filter(o=>o.kind==='PN');
  need(ops.length===1&&rules.validateTransfer(ops[0])===true,'prepared PN interface invalid');
  const op=ops[0],target=rules.packets[op.target];
  rows.push({index:rows.length,point:[...point],shift:shift4(point),packet:packetSnapshot(rules,packet),
   frame:phaseFrame(rules.charts[chart],0),PN:{operation:copy(op),target:packetSnapshot(rules,op.target),targetFrame:phaseFrame(rules.charts[target.chart],target.origin)}});
  ids.push(packet);
 }
 const joint=rules.describe(ids);
 return {schema:'marici.ramsey-prepared-region-input.v1',radius:3,rows,
  attemptedJointAssembly:{valid:joint.valid,reason:joint.reason??null},
  canonicalPolicyUnchanged:true,preparedPolicyIsDifferent:true,wordToIndexConstructed:false};
}
export function verifyPrepared(value){
 const expected=prepareRegion();need(same(value,expected),'prepared context, region or native interface changed');
 const root=new GenerativeAssemblyRules(),aliases=root.charts[root.packets[root.root].chart].aliases;
 for(const row of value.rows){
  need(same(project4(row.frame.window[0].vertex),row.point),'prepared marked point mismatch');
  for(const [name,v] of Object.entries(aliases)){
   const shifted=v.split(',').map((x,j)=>Number(x)+row.shift[j]).join(',');
   need(row.packet.chart.aliases[name]===shifted,'not a translated full source reference');
  }
  need(same(row.packet.packet.permutation,[0,1,2,3,4]),'prepared coefficient frame changed');
 }
 return true;
}
