// Exploratory typing probe. Geometry: two complete-face growth rounds from the
// seed, not an asserted identification with the user's length-indexed shells.
// Freeze only the C/M interfaces of the actual ordered P/N/E templates.
import assert from 'node:assert/strict';
import {GenerativeAssemblyRules} from '../demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {windowProtocol} from '../demos/particle-overlap-tetrahedron/window-construction-model.mjs';

const rules=new GenerativeAssemblyRules(), geometry=rules.geometry;
const root=rules.charts[rules.packets[rules.root].chart];
const central=geometry.cells[root.cell];
const base=new Set(central.vertices);
const pairKey=xs=>[...xs].sort().join('|');
const seedEdges=central.vertices.flatMap((v,i)=>central.vertices.slice(i+1).map(w=>[v,w]));
assert.equal(seedEdges.length,6);
const s2=[...new Set(central.faces.map(face=>geometry.neighbor(central.id,face)))];
assert.equal(s2.length,4);
const old=new Set([central.id,...s2]);
const s3=[...new Set(s2.flatMap(id=>geometry.cells[id].faces.map(face=>geometry.neighbor(id,face))))].filter(id=>!old.has(id));
const all=[central.id,...s2,...s3];
const edgeFans=seedEdges.map(edge=>({edge,cells:s3.filter(id=>edge.every(v=>geometry.cells[id].vertices.includes(v)))}));
const edgeFirst=[...new Set(edgeFans.flatMap(f=>f.cells))];
const rest=s3.filter(id=>!edgeFirst.includes(id));

// All three actual windows contain two C and two M marks. This is a necessary
// shared-interface condition, not full native operation/history admission.
assert.ok(windowProtocol.every(p=>p.nodes.filter(n=>n[0]==='C').length===2 && p.nodes.filter(n=>n[0]==='M').length===2));
const initial=new Map(Object.entries(root.aliases).filter(([,v])=>base.has(v)).map(([n,v])=>[v,n[0]]));
assert.equal(initial.size,4);
function close(order) {
  const marks=new Map(initial), deductions=[];
  let changed=true;
  while(changed) {
    changed=false;
    for(const id of order) {
      const vertices=geometry.cells[id].vertices;
      const cs=vertices.filter(v=>marks.get(v)==='C').length;
      const ms=vertices.filter(v=>marks.get(v)==='M').length;
      const unknown=vertices.filter(v=>!marks.has(v));
      if(cs>2||ms>2||cs+unknown.length<2||ms+unknown.length<2) return {marks,deductions,conflict:id};
      const role=cs===2?'M':ms===2?'C':null;
      if(role) for(const v of unknown) {marks.set(v,role);deductions.push({cell:id,vertex:v,role});changed=true;}
    }
  }
  return {marks,deductions,conflict:null};
}
const forward=close([central.id,...s2,...edgeFirst,...rest]);
const reverse=close([central.id,...s2,...rest.toReversed(),...edgeFirst.toReversed()]);
const simultaneous=close(all);
assert.equal(forward.conflict,null);
assert.deepEqual([...forward.marks].sort(),[...reverse.marks].sort());
assert.deepEqual([...forward.marks].sort(),[...simultaneous.marks].sort());
function permutations(xs) {
  return xs.length ? xs.flatMap((x,i)=>permutations(xs.filter((_,j)=>i!==j)).map(t=>[x,...t])) : [[]];
}
function options(id) {
  const vertices=geometry.cells[id].vertices;
  return windowProtocol.map(p=>({type:p.species,frames:permutations(vertices).filter(vs=>p.nodes.every((name,i)=>!forward.marks.has(vs[i]) || forward.marks.get(vs[i])===name[0])).length})).filter(p=>p.frames);
}
const cells=s3.map(id=>({id,marks:geometry.cells[id].vertices.map(v=>forward.marks.get(v)??'?').join(''),seedEdgeContacts:seedEdges.filter(e=>e.every(v=>geometry.cells[id].vertices.includes(v))).map(pairKey),options:options(id)}));
assert.ok(cells.every(c=>c.options.length===3));
assert.ok(cells.every(c=>!c.marks.includes('?') && c.options.every(o=>o.frames===4)));
const stage2Options=s2.map(options);
assert.ok(stage2Options.every(os=>os.length===3));
console.log(JSON.stringify({
  scope:'Two face-growth rounds; six seed-edge fans processed before the remaining cells; C/M template constraints only',
  stage2PatternPNEEAdmittedAtThisScope:true,
  sizes:{central:1,firstShell:s2.length,secondShell:s3.length},
  sixEdges:edgeFans,
  secondShellProcessedAlongEdges:edgeFirst.length,remainingSecondShell:rest.length,
  vertexMarksForced:forward.deductions.length,
  orderIndependentMarkClosure:true,
  uniqueTypedSecondShellCells:cells.filter(c=>c.options.length===1).length,
  ambiguousTypedSecondShellCells:cells.filter(c=>c.options.length>1).length,
  secondShellTypeAssignmentsAtThisScope:String(3n**BigInt(s3.length)),
  example:cells[0],
  allCells:cells,
  missingConstraints:['ordered entry/exit interfaces and frame propagation','admission of trajectory transitions beyond C/M role agreement','identification of these growth rounds with the proposed length-indexed stages'],
  fullNativeAdmissionClaimed:false,userConjectureRefuted:false
},null,2));
