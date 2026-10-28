import {GenerativeAssemblyRules} from '../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {makeLatticeItem} from '../strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {phaseFrame} from '../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {packetSnapshot,same} from './ramsey-native-word-trace.mjs';
import {region3,shift4} from './ramsey-native-region-family.mjs';
const copy=x=>structuredClone(x),need=(c,m)=>{if(!c)throw new RangeError(m);};
export function region4(){const a=[];for(let x=-4;x<=4;x++)for(let y=-4;y<=4;y++)for(let z=-4;z<=4;z++)if((x+y+z)%2===0)a.push([x,y,z]);return a;}
function record(r,point,index,packet,op){
 const p=r.packets[packet],target=r.packets[op.target];
 return {index,point:[...point],shift:shift4(point),packet:packetSnapshot(r,packet),frame:phaseFrame(r.charts[p.chart],p.origin),
  PN:{operation:copy(op),target:packetSnapshot(r,op.target),targetFrame:phaseFrame(r.charts[target.chart],target.origin)}};
}
function bank(){
 const r=new GenerativeAssemblyRules(),rows=[],handles=[];
 function append(point){
  const owner=makeLatticeItem('tetrahedron',shift4(point)),cell=r.geometry.register(owner,owner.components[0]);
  const a=Object.fromEntries(['C0','M0','C1','M1'].map((n,i)=>[n,owner.vertices[i].join(',')]));
  const chart=r.completeP(cell,a);need(chart!==null,'missing native prepared reference');
  const packet=r.packet(chart,0,[0,1,2,3,4]);const ops=r.outgoing(packet).map(i=>r.operations[i]).filter(o=>o.kind==='PN');
  need(ops.length===1&&r.validateTransfer(ops[0])===true,'invalid appended native interface');
  handles.push({packet,op:ops[0]});rows.push(record(r,point,rows.length,packet,ops[0]));
 }
 return {r,rows,handles,append};
}
export function extendPrepared(...args){
 need(args.length===0,'no word or answer parameter allowed');const b=bank();
 for(const p of region3())b.append(p);
 const old=copy(b.rows),oldIds=b.handles.map(h=>h.packet);const joint3=b.r.describe(oldIds);
 const seen=new Set(old.map(x=>x.point.join(',')));
 for(const p of region4())if(!seen.has(p.join(',')))b.append(p);
 const after=old.map((row,i)=>record(b.r,row.point,i,b.handles[i].packet,b.handles[i].op));
 need(same(old,after),'old live source context mutated on extension');
 const joint4=b.r.describe(b.handles.map(h=>h.packet));
 return {schema:'marici.ramsey-prepared-refinement.v1',oldRadius:3,newRadius:4,oldRows:old,newRows:copy(b.rows),
 embedding:old.map((_,i)=>i),oldLiveContextsUnchanged:true,
 joint3:{valid:joint3.valid,reason:joint3.reason??null},joint4:{valid:joint4.valid,reason:joint4.reason??null}};
}
export function freshRebuild4(){const b=bank();for(const p of region4())b.append(p);return copy(b.rows);}
export function verifyExtension(value){need(same(value,extendPrepared()),'invalid append-only native refinement');return true;}
