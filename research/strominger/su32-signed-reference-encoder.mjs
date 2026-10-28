// Lossless occurrence references, not a wiring or a five-slot coefficient binding.
import assert from 'node:assert/strict';
const slots=['P+','P-','E+','E-'];
const copy=x=>structuredClone(x);
const canonical=x=>{
 if(x===null||typeof x==='string'||typeof x==='boolean')return JSON.stringify(x);
 if(typeof x==='number'){assert(Number.isFinite(x));return JSON.stringify(x);}
 if(Array.isArray(x))return '['+x.map(canonical).join(',')+']';
 assert(x&&Object.getPrototypeOf(x)===Object.prototype,'Payload must be JSON data');
 return '{'+Object.keys(x).sort().map(k=>JSON.stringify(k)+':'+canonical(x[k])).join(',')+'}';
};
const equal=(a,b)=>canonical(a)===canonical(b);
export function buildSu32SignedReferenceAtlas(fixture){
 assert.equal(fixture.edgeUnits,3);assert.equal(fixture.nativeHopfBinding,false);
 const roles=new Map(fixture.cells.map(c=>[c.id,c.role]));
 const charts=[];
 for(const reading of fixture.readings)for(const cone of reading.cones){
  const first=[...new Set(cone.paths.map(p=>p.cells[1]))].sort();
  const P=first.filter(c=>roles.get(c)==='proton'),E=first.filter(c=>roles.get(c)==='electron');
  assert.equal(P.length,2);assert.equal(E.length,2);
  const joints=[...new Set(cone.paths.map(p=>p.cells[2]))].sort().map(cell=>{
   const refs=[...new Set(cone.paths.filter(p=>p.cells[2]===cell).map(p=>p.cells[1]))];
   assert.equal(refs.length,2);
   return {cell,P:refs.find(c=>P.includes(c)),E:refs.find(c=>E.includes(c))};
  });
  assert.equal(joints.length,4);
  for(const p of P)for(const e of E)assert.equal(joints.filter(j=>j.P===p&&j.E===e).length,1);
  const comparisons=[...new Set(cone.paths.map(p=>p.cells[3]))].sort().map(cell=>{
   const inputs=[...new Set(cone.paths.filter(p=>p.cells[3]===cell).map(p=>p.cells[2]))].sort();
   assert.equal(inputs.length,2);
   const operands=inputs.map(c=>joints.find(j=>j.cell===c));
   const shared=['P','E'].filter(r=>operands[0][r]===operands[1][r]);assert.equal(shared.length,1);
   const role=shared[0];
   return {cell,inputs,sharedRole:role,sharedCell:operands[0][role],varyingRole:role==='P'?'E':'P'};
  });
  assert.equal(comparisons.length,4);
  charts.push({id:JSON.stringify([reading.id,cone.source,cone.target]),reading:reading.id,source:cone.source,target:cone.target,starCells:[...cone.cellIds].sort(),P,E,joints,comparisons});
 }
 return {schema:'su32.signed-reference-atlas.v1',charts,roles:Object.fromEntries(roles),globalAssignment:null};
}
function getChart(atlas,id){const c=atlas.charts.find(c=>c.id===id);assert(c,'Unknown occurrence chart');return c;}
export function encodeSignedReferences(atlas,chartId,binding,records){
 const chart=getChart(atlas,chartId);
 assert(Array.isArray(binding)&&binding.length===2&&binding.every(i=>i===0||i===1));
 assert.deepEqual(Object.keys(records).sort(),[...slots].sort());canonical(records);
 const refs={};for(const [i,role] of ['P','E'].entries()){
  refs[chart[role][binding[i]]]=role+'+';refs[chart[role][1-binding[i]]]=role+'-';
 }
 return {schema:'su32.signed-reference-packet.v1',chartId,binding:[...binding],
  records:copy(records),referenceBinding:refs,
  channels:chart.joints.map(j=>({cell:j.cell,P:{record:refs[j.P],referenceCell:j.P},E:{record:refs[j.E],referenceCell:j.E}})),
  comparisons:chart.comparisons.map(c=>({...copy(c),sharedRecord:refs[c.sharedCell]})),
  boundary:{source:chart.source,target:chart.target,reconciliation:null},nativeHopfBinding:false};
}
export function decodeSignedReferences(atlas,packet){
 const expected=encodeSignedReferences(atlas,packet.chartId,packet.binding,packet.records);
 assert(equal(packet,expected),'Retained reference packet disagrees with native occurrence chart');
 return copy(packet.records);
}
export function mapReferencePayloads(atlas,packet,map){
 const records=decodeSignedReferences(atlas,packet);
 return encodeSignedReferences(atlas,packet.chartId,packet.binding,Object.fromEntries(slots.map(s=>[s,map(copy(records[s]),s)])));
}
export function cellSignConstraintGraphs(atlas){
 return Object.fromEntries(['P','E'].map(role=>{
  const edges=new Map();
  for(const c of atlas.charts){const pair=[...c[role]].sort(),key=JSON.stringify(pair);
   if(!edges.has(key))edges.set(key,{vertices:pair,occurrences:[]});edges.get(key).occurrences.push(c.id);
  }
  const vertices=[...new Set([...edges.values()].flatMap(e=>e.vertices))].sort();
  const triangles=[];
  for(let i=0;i<vertices.length;i++)for(let j=i+1;j<vertices.length;j++)for(let k=j+1;k<vertices.length;k++){
   const vs=[vertices[i],vertices[j],vertices[k]],es=[[vs[0],vs[1]],[vs[0],vs[2]],[vs[1],vs[2]]].map(p=>edges.get(JSON.stringify(p)));
   if(es.every(Boolean))triangles.push({vertices:vs,edges:es});
  }
  return [role,{vertices,edges:[...edges.values()],triangles}];
 }));
}
