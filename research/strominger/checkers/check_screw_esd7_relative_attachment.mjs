import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import crypto from 'node:crypto';
import {fileURLToPath} from 'node:url';
import {assembleComponents} from '../demos/particle-overlap-tetrahedron/simplex-components.mjs';
import {makeLatticeItem,itemKey} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {GenerativeAssemblyRules,LocalPrimitiveGeometry} from '../demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'../../..');
const contract='research/strominger/contracts/screw-esd7-relative-attachment-attempt.v1.json';
const snapshot='research/strominger/contracts/persistent-seam-pe-conjecture-net.snapshot.rev34.json';
const output='research/strominger/results/screw-esd7-relative-attachment';
const load=async p=>JSON.parse(await fs.readFile(path.join(root,p),'utf8'));
const fieldPath='research/strominger/results/screw-field-sewing.json';
const spec=await load(contract),pre=await load(snapshot),source=await load(spec.source),prior=await load(spec.priorReceipt),field=await load(fieldPath);
const inputs=new Set([contract,snapshot,spec.source,spec.priorReceipt,fieldPath,'research/strominger/checkers/check_screw_esd7_relative_attachment.mjs','research/strominger/screw-esd7-relative-attachment-result-v1.md']);
for(const receipt of [source,prior,field])for(const [p,d] of Object.entries(receipt.sourceHashes)){
 assert.equal(crypto.createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex'),d,'stale input '+p);inputs.add(p);
}
const checks=[];const check=(name,f)=>{f();checks.push(name);};
const point=v=>typeof v==='string'?v.split(',').map(Number):v;
const {sign,permutation,translation}=spec.frame;
const map=v=>permutation.map((i,j)=>(sign*point(v)[i]+translation[j])||0);
const inverse=v=>{const q=[];permutation.forEach((i,j)=>q[i]=(sign*(point(v)[j]-translation[j]))||0);return q;};
const bind=v=>map(v).join(',');
check('registered frame and open pre-execution task match the prior diagnostic witness',()=>{
 const n=pre.conjectures.find(n=>n.id==='screw-esd7-relative-attachment-attempt');assert.equal(n.status,'open');assert.equal(n.registration_before_execution,true);
 const w=prior.minimalExternalWitness;for(const k of ['sign','permutation','translation'])assert.deepEqual(spec.frame[k],w[k]);
});
const target=assembleComponents(7),geometry=new LocalPrimitiveGeometry();
for(const item of target.items){const owner=makeLatticeItem(item.kind,item.origin,item.inverted);for(const c of owner.components)geometry.register(owner,c);}
const targetIndex=new Map(target.components.map(c=>[itemKey(c.addresses),c.id]));
check('native lattice owners independently reproduce the actual343 target primitives',()=>{
 assert.equal(geometry.cells.length,343);assert.deepEqual(new Set(geometry.byKey.keys()),new Set(targetIndex.keys()));
});
const cells=source.cells.map(c=>{const key=itemKey(c.vertices.map(map));return {sourceCell:c.id,targetComponent:targetIndex.get(key),nativeCell:geometry.byKey.get(key),vertices:c.vertices.map(bind)};});
const cellMap=new Map(cells.map(c=>[c.sourceCell,c.nativeCell]));
check('all occupied primitives map injectively to actual target components',()=>{
 assert.equal(cells.length,24);assert.equal(new Set(cells.map(c=>c.targetComponent)).size,24);for(const c of cells){assert.notEqual(c.targetComponent,undefined);assert.notEqual(c.nativeCell,undefined);}
});
const rules=new GenerativeAssemblyRules();rules.geometry=geometry;rules.charts=[];rules.chartKeys=new Map();rules.packets=[];
const chartBindings=[],failures=[];
// Complete P/N references through actual lattice neighbors before validating E aliases.
for(const c of [...source.charts].sort((a,b)=>Number(a.species==='electron')-Number(b.species==='electron'))){
 const aliases=Object.fromEntries(Object.entries(c.aliases).map(([k,v])=>[k,bind(v)])),cell=cellMap.get(c.cell);
 try{
  const id=c.species==='proton'?rules.completeP(cell,aliases):c.species==='neutron'?rules.completeN(cell,aliases):rules.chart(cell,c.species,aliases);
  assert.notEqual(id,null);assert.deepEqual(rules.charts[id].aliases,aliases);
  chartBindings.push({sourceChart:c.id,nativeChart:id,sourceCell:c.cell,nativeCell:cell,species:c.species,aliases});
 }catch(e){failures.push({stage:'native-reference-completion',sourceChart:c.id,cell,aliases,error:e.message});}
}
const chartMap=new Map(chartBindings.map(c=>[Number(c.sourceChart.slice(6)),c.nativeChart]));
const packets=source.packets.map(p=>({...p,chart:chartMap.get(p.chart)}));for(const p of packets)rules.packets[p.id]=p;
const operations=source.operations.map(o=>({...o,face:o.face===null?null:o.face.map(bind)}));
let validatedInterfaces=0;
if(!failures.length)for(const op of operations){try{rules.validateTransfer(op);validatedInterfaces++;}catch(e){failures.push({stage:'native-transfer',operation:op,error:e.message});}}
check('every native completion or transfer failure is retained with its exact attempted binding',()=>{
 assert.equal(chartBindings.length+failures.filter(f=>f.stage==='native-reference-completion').length,source.charts.length);
 if(!failures.length)assert.equal(validatedInterfaces,source.operations.length);
});
const ledger=new Map();
for(const c of source.charts)for(const [alias,v] of Object.entries(c.aliases))if(map(v).some(x=>x>2)){
 const k=bind(v);if(!ledger.has(k))ledger.set(k,{source:point(v),target:map(v),classification:'external-reference-only',aliases:[]});
 ledger.get(k).aliases.push({sourceChart:c.id,alias,packets:source.packets.filter(p=>p.chart===Number(c.id.slice(6))).map(p=>p.id)});
}
const externalReferences=[...ledger.values()];
check('all transformed coordinates invert exactly and no external C0 is clipped',()=>{
 for(const c of source.cells)for(const v of c.vertices)assert.deepEqual(inverse(map(v)),point(v));
 for(const c of source.charts)for(const v of Object.values(c.aliases))assert.deepEqual(inverse(map(v)),point(v));
 assert.equal(externalReferences.length,1);assert.deepEqual(externalReferences[0].target,[-3,1,3,0]);
});
const validateLedger=records=>{
 assert.deepEqual(records,externalReferences);
 for(const row of records){assert.deepEqual(inverse(row.target),row.source);assert.ok(row.target.some(x=>x>2));}
};
check('deleting or clipping the external reference is rejected',()=>{
 assert.throws(()=>validateLedger([]));const clipped=structuredClone(externalReferences);clipped[0].target=clipped[0].target.map(x=>Math.min(2,x));assert.throws(()=>validateLedger(clipped));
});
check('all origins, coefficient permutations and retained operations survive unchanged',()=>{
 assert.equal(packets.length,66);assert.equal(operations.length,95);
 for(let i=0;i<packets.length;i++)assert.deepEqual({...packets[i],chart:source.packets[i].chart},source.packets[i]);
 for(let i=0;i<operations.length;i++)assert.deepEqual({...operations[i],face:source.operations[i].face},source.operations[i]);
});
check('coefficient-loss control fails the existing native transfer validator',()=>{
 if(failures.length)return;
 const op=structuredClone(operations[0]);op.permutation=[0,1,2,3,4];assert.throws(()=>rules.validateTransfer(op));
});
check('retained interface identities match the live prior field receipt without merging charts',()=>{
 assert.equal(new Set(chartBindings.map(c=>c.nativeChart)).size,chartBindings.length);
 assert.equal(field.interfaces.length,operations.length);
 for(const op of operations){const row=field.interfaces.find(e=>e.operation===op.id);assert.ok(row);for(const k of ['kind','source','target'])assert.equal(row[k],op[k]);
  for(const k of ['full44FieldSquare','full44ReadoutSquare','fiveCoefficientBindingSquare'])assert.equal(row[k],true);}
});
const occupied=new Set(cells.map(c=>c.nativeCell));
const generatedReferenceCells=geometry.cells.slice(343).map(c=>({nativeCell:c.id,key:c.key,vertices:c.vertices,classification:'generated-reference-only',outsideEnvelope:c.vertices.some(v=>point(v).some(x=>x>2))}));
check('native reference completion never enlarges the occupied set',()=>{
 assert.equal(occupied.size,24);for(const c of generatedReferenceCells)assert.ok(!occupied.has(c.nativeCell));
 for(const v of externalReferences)assert.ok(!cells.some(c=>c.vertices.includes(v.target.join(','))));
});
const histories={construction:source.construction,walk:source.walk,repairs:source.repairs,blocks:source.blocks,boundaries:source.boundaries,originalPackets:source.originalPackets};
const artifact={frame:spec.frame,selection:spec.selection,cells,chartBindings,packets,operations,histories,externalReferences,generatedReferenceCells,failures,
 relativeNativeAttachmentEstablished:failures.length===0,validatedInterfaces,
 analyticalDomainObligation:{status:'not-supplied',nativeInterface:{operation:15,kind:'NE',source:5,target:15},externalReference:[-3,1,3,0],
 required:'Specify an analytical carrier/domain or boundary-trace representation supporting the external C0 and comparison with the actual retained esd7 witness. Native lattice completion supplies neither that extension operator nor F006 homotopies.'},
 analyticalDomainExtensionEstablished:false,actualF006BindingEstablished:false,fullPbConstructionEstablished:false,
 fieldScope:'Native operation kinds and full coefficient histories are unchanged from the95-interface sewing receipt; this test checks geometric/native binding, not a new analytical field equation.'};
await fs.mkdir(path.join(root,output),{recursive:true});await fs.writeFile(path.join(root,output,'attachment.json'),JSON.stringify(artifact,null,2)+'\n');inputs.add(output+'/attachment.json');
const sourceHashes={};for(const p of inputs)sourceHashes[p]=crypto.createHash('sha256').update(await fs.readFile(path.join(root,p))).digest('hex');
const receipt={status:'passed',check_count:checks.length,checks,relativeNativeAttachmentEstablished:artifact.relativeNativeAttachmentEstablished,
 occupiedCells:cells.length,packets:packets.length,validatedInterfaces,externalReferenceVertices:externalReferences.length,generatedReferenceCells:generatedReferenceCells.length,failures,
 analyticalDomainExtensionEstablished:false,actualF006BindingEstablished:false,fullPbConstructionEstablished:false,sourceHashes};
await fs.writeFile(path.join(root,output,'verification.json'),JSON.stringify(receipt,null,2)+'\n');console.log(JSON.stringify({...receipt,checks:undefined,sourceHashes:undefined}));
