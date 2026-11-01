import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildSulfur32Wiring} from '../../realization-tower/sulfur-32-wiring.mjs';
import {buildPESymmetricSector} from '../pe-symmetric-sector.mjs';
import {buildNativeAxisPortGraph,faceKey} from '../native-axis-port-graph.mjs';
import {projectNativeWindow} from '../sulfur-period-covers.mjs';
import {periodVector,nativeWindowWires,nativeWindowProfile,restoreNativeWindowProfile,applyNativeWindowOperation,completePeriodicWindowProfile} from '../native-window-operation.mjs';
const root='research/strominger',base=buildSulfur32Wiring(),sector=buildPESymmetricSector(2),bulk=buildNativeAxisPortGraph(sector);
const projection=projectNativeWindow(sector,bulk,base),baseCells=new Map(base.groups.map(g=>[g.id,g]));
const physicalCells=new Map(sector.cells.map(c=>[c.id,c]));
// The geometry inverse is explicit, not inferred from the number of labels.
assert.equal(new Set(projection.cells.map(c=>JSON.stringify([c.baseCell,c.periodCoordinates]))).size,sector.cells.length);
for(const c of projection.cells){
 const t=periodVector(c.periodCoordinates),vs=baseCells.get(c.baseCell).representative.vertices.map(v=>v.map((x,i)=>x-t[i]));
 assert.equal(faceKey(vs),faceKey(physicalCells.get(c.physicalCell).vertices));
}
// Exhaust all residue types for each translated native cell shape. Together with
// the inverse integer period formula, this covers the declared Z^3 family.
for(const role of ['proton','neutron','electron']){
 const gs=base.groups.filter(g=>g.role===role),anchor=vs=>[0,1,2,3].map(i=>Math.min(...vs.map(v=>v[i]))),mod4=x=>((x%4)+4)%4;
 const anchors=gs.map(g=>anchor(g.representative.vertices)),sum=anchors[0].reduce((a,b)=>a+b,0);
 assert(anchors.every(a=>a.reduce((s,x)=>s+x,0)===sum));
 assert.equal(new Set(gs.map((g,k)=>faceKey(g.representative.vertices.map(v=>v.map((x,i)=>x-anchors[k][i]))))).size,1);
 const actual=anchors.map(a=>a.slice(0,3).map(x=>mod4(x-a[3])).join(',')).sort(),expected=[];
 for(let a=0;a<4;a++)for(let b=0;b<4;b++)for(let c=0;c<4;c++)if(mod4(a+b+c)===mod4(sum))expected.push([a,b,c].join(','));
 assert.deepEqual(actual,expected.sort());
}
const model=nativeWindowWires(base,sector,projection);assert.equal(model.wires.length,420);
const atPort=new Map();for(const w of model.wires)for(const p of w.portWitnesses){assert(!atPort.has(p.id));atPort.set(p.id,{wire:w.id,port:p});}
assert.equal(atPort.size,1680);for(const p of bulk.ports)assert(atPort.has(p.id));
// Independent geometry verification, not an edge-five periodic extension.
const larger=buildNativeAxisPortGraph(buildPESymmetricSector(4)),largerPorts=new Map(larger.ports.map(p=>[p.id,p]));
const edgeKey=e=>JSON.stringify([e.kind,...[e.from,e.to].sort()]),largerEdges=new Set(larger.edges.map(edgeKey));
for(const w of model.wires){for(const p of w.portWitnesses){assert(largerPorts.has(p.id));assert.equal(p.axis,largerPorts.get(p.id).axis);}
 for(const e of w.edges)assert(largerEdges.has(edgeKey(e)));
}
const completeEdges=new Set(model.wires.flatMap(w=>w.edges.map(edgeKey)));for(const e of bulk.edges)assert(completeEdges.has(edgeKey(e)));
const inside=new Set(model.insideCells),boundary=[];
for(const w of model.wires)for(const e of w.edges){const a=atPort.get(e.from).port,b=atPort.get(e.to).port;
 if(inside.has(a.cell)!==inside.has(b.cell)){
  assert.equal(e.kind,'shared-native-face');const pin=inside.has(a.cell)?a:b,pout=inside.has(a.cell)?b:a;
  boundary.push({wire:w.id,axis:w.axis,insidePort:pin.id,outsidePort:pout.id,outsideCell:pout.cell,
   direction:inside.has(w.source)?'output':'input'});
 }
}
assert.deepEqual(boundary.map(b=>b.insidePort).sort(),[...bulk.boundaryPorts].sort());
assert.equal(boundary.filter(b=>b.direction==='input').length,100);assert.equal(boundary.filter(b=>b.direction==='output').length,100);
assert.equal(model.sourceBoundaryWires.length,100);assert.equal(model.targetBoundaryWires.length,100);
const rows=model.wires.map((w,i)=>({wire:w.id,payload:{index:i,retained:[false,null,{record:'opaque'}]}}));
const input=nativeWindowProfile(model,rows,'P|E'),output=applyNativeWindowOperation(model,input);
assert.equal(input.cells.length,80);assert.equal(output.cells.length,80);
assert.deepEqual(applyNativeWindowOperation(model,output),input);
assert.deepEqual(restoreNativeWindowProfile(model,input),restoreNativeWindowProfile(model,output));
const shuffled={...input,cells:[...input.cells].reverse(),boundary:[...input.boundary].reverse()};assert.deepEqual(applyNativeWindowOperation(model,shuffled),output);
const incomplete=structuredClone(input);incomplete.boundary.pop();assert.throws(()=>applyNativeWindowOperation(model,incomplete));
const wrongSlot=structuredClone(input);[wrongSlot.cells[0].slots[0][0],wrongSlot.cells[0].slots[0][1]]=[wrongSlot.cells[0].slots[0][1],wrongSlot.cells[0].slots[0][0]];
assert.throws(()=>applyNativeWindowOperation(model,wrongSlot));
let independenceChecks=0;let witness;
for(const direction of ['P|E','E|P']){
 const original=nativeWindowProfile(model,rows,direction),target=applyNativeWindowOperation(model,original);
 for(const external of original.boundary){
  const rival=rows.map(r=>r.wire===external.wire?{wire:r.wire,payload:{changed:true}}:r),changed=nativeWindowProfile(model,rival,direction);
  assert.deepEqual(original.cells,changed.cells);assert.notDeepEqual(target.cells,applyNativeWindowOperation(model,changed).cells);
  independenceChecks++;witness??={direction,changedWire:external.wire,left:external,right:rival.find(r=>r.wire===external.wire)};
 }
}
// The actual pullback of a base section is periodic, unlike an arbitrary
// section of the pulled-back bundle. Test this smaller state domain separately.
const baseContents=new Map(base.wires.map((w,i)=>[w.id,{sourceWire:w.id,opaque:[i,null,false]}]));
const periodicRows=model.wires.map(w=>({wire:w.id,payload:structuredClone(baseContents.get(w.baseWire))}));
const periodicInput=nativeWindowProfile(model,periodicRows,'P|E'),periodicOutput=applyNativeWindowOperation(model,periodicInput);
assert.deepEqual(completePeriodicWindowProfile(model,periodicInput.cells,'P|E'),periodicInput);
assert.deepEqual(completePeriodicWindowProfile(model,periodicOutput.cells,'E|P'),periodicOutput);
assert.equal(new Set(periodicInput.cells.flatMap(c=>c.slots.flat().map(r=>r.payload.sourceWire))).size,64);
assert.equal(new Set(periodicOutput.cells.flatMap(c=>c.slots.flat().map(r=>r.payload.sourceWire))).size,64);
const badPeriodic=structuredClone(periodicInput.cells);badPeriodic[0].slots[0][0].payload={changed:true};
assert.throws(()=>completePeriodicWindowProfile(model,badPeriodic,'P|E'),/Nonperiodic/);
const sourceHashes={};for(const p of [root+'/contracts/su32-native-window-operation-v1.json',root+'/native-window-operation.mjs',root+'/sulfur-period-covers.mjs',
 root+'/native-axis-port-graph.mjs',root+'/pe-symmetric-sector.mjs',root+'/checkers/check_su32_native_window_operation.mjs',
 'research/realization-tower/sulfur-32-wiring.mjs'])sourceHashes[p]=createHash('sha256').update(await fs.readFile(p)).digest('hex');
const counts={physicalWindowCells:sector.cells.length,distinctIntegerLiftCells:projection.cells.length,wireValues:model.wires.length,
 inputCellFibres:input.cells.length,outputCellFibres:output.cells.length,externalInputValues:input.boundary.length,externalOutputValues:output.boundary.length,
 internalPassages:model.wires.filter(w=>inside.has(w.source)&&inside.has(w.target)).length,physicalBoundaryFaces:boundary.length,independenceChecks};
const result={schema:'su32.native-window-operation.v1',passed:true,closedEightyFibreModelConstructed:false,
 conclusion:'The integer-indexed lift of the existing global candidate supplies an invertible native open-window operation: 80 four-slot P fibres plus 100 boundary values to 80 four-slot E fibres plus 100 boundary values.',
 counts,model,boundary,input,output,independenceWitness:witness,sourceHashes,
 stateDomains:{unrestrictedLiftedSections:{wireValuesInWindow:420,independentExternalInputs:100},
 canonicalPullbacksOfBaseSections:{baseWireValues:64,externalValuesDeterminedFromInternalViews:true,
 periodicityCheckedInBothPresentations:true,nonperiodicInputRejected:true}}, 
 scope:'Native labelled wire transport and regrouping only. No formal comparison packet identification, finite edge-five closure, supplied exterior state, or physical infinite-universe claim.',
 residual:'Unrestricted sections of the lifted bundle need 100 independent external inputs. Canonical pullbacks determine them but restrict contents to 64 base-wire values. Neither is a closed 80-independent-fibre realization of the fixed carrier.'};
const dir=root+'/results/su32-native-window-operation-v1';await fs.mkdir(dir,{recursive:true});await fs.writeFile(dir+'/verification.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({passed:true,counts,stateDomains:result.stateDomains,conclusion:result.conclusion,residual:result.residual},null,2));
