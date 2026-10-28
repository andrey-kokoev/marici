import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {buildOctahedralCoherentRouting,validateOctahedralCoherentRouting} from '../../realization-tower/octahedral-coherent-routing.mjs';
import {buildFiveSideOctRoutingObligations} from '../../realization-tower/five-side-oct-routing-obligations.mjs';

// Audit the existing candidate, NOT a construction/acceptance checker.
// Exit 1 means it remains inadmissible, even when reproducing expected defects.
const model=buildOctahedralCoherentRouting(2),links=new Map(model.links.map(l=>[l.id,l]));
const probes=[];
function probe(id,mutate,expected){
 const candidate=structuredClone(model);mutate(candidate);
 try{const result=validateOctahedralCoherentRouting(candidate);probes.push({id,expected,actual:'accepted',defectConfirmed:true,reportedStatus:result.status});}
 catch(error){probes.push({id,expected,actual:'rejected',defectConfirmed:false,message:error.message});}
}
probe('merge-all-groups',m=>{m.coherenceGroups=[{id:'arbitrary-all-in-one',members:m.coherenceGroups.flatMap(g=>g.members),slots:m.slots.map(s=>s.id),wireIds:m.routes.map(r=>r.id),internalLinks:m.links.filter(l=>l.kind==='N-interior').map(l=>l.id)}];},'reject: not the connected-component partition claimed by this constructor');
probe('seams-relabeled-native',m=>{for(const l of m.links)if(l.kind==='boundary-seam')l.kind='native-interface';},'reject: shared-face geometry is absent');
probe('internal-path-outside-owner',m=>{const l=m.links.find(l=>l.kind==='N-interior');l.points[1]=l.points[1].map((x,i)=>x+(i===0?100:i===1?-100:0));},'reject: path leaves its owning N cell while preserving coordinate sum');

const f=model.fibration,cells=new Map(f.sector.cells.map(c=>[c.id,c])),faces=new Map(f.sector.faces.map(x=>[x.id,x]));
const base=(cell,role)=>[0,1,2,3].map(i=>Math[role==='proton'?'max':'min'](...cell.vertices.map(v=>v[i])));
const mod=x=>((x%4)+4)%4,phase=q=>q.slice(0,3).map(x=>mod(x-q[3])).join(',');
const alternate=structuredClone(f.wires),buckets=new Map();
for(const w of alternate)if(w.transport.some(Boolean)){const k=`${w.axis}|${phase(base(cells.get(w.target),'electron'))}`;if(!buckets.has(k))buckets.set(k,[]);buckets.get(k).push(w);}
for(const ws of buckets.values()){
 const targets=ws.map(w=>w.target).reverse();
 ws.forEach((w,i)=>{w.target=targets[i];const expected=base(cells.get(w.source),'proton').map((x,j)=>x-1+2*Number(j===w.axis));w.transport=base(cells.get(w.target),'electron').map((x,j)=>x-expected[j]);});
}
for(const w of alternate){assert.equal(w.transport.reduce((s,x)=>s+x,0),0);assert(w.transport.every(x=>mod(x)===mod(w.transport[3])));}
for(let axis=0;axis<4;axis++)assert.equal(new Set(alternate.filter(w=>w.axis===axis).map(w=>w.target)).size,80);
assert(f.wires.every((w,i)=>w.transport.some(Boolean)||w.target===alternate[i].target));
function componentCount(wires){
 const adj=new Map(f.sector.cells.filter(c=>c.role==='neutron').map(c=>[c.id,new Set()]));
 for(const w of wires){
  const near=id=>{const c=cells.get(id),face=c.faces.find(vs=>vs.every(p=>p[w.axis]===vs[0][w.axis]));return faces.get(face.map(String).sort().join('|')).owners.find(o=>o!==id);};
  const a=near(w.source),b=near(w.target);if(a&&b){adj.get(a).add(b);adj.get(b).add(a);}
 }
 const seen=new Set();let count=0;
 for(const id of adj.keys())if(!seen.has(id)){count++;const todo=[id];seen.add(id);for(let i=0;i<todo.length;i++)for(const n of adj.get(todo[i]))if(!seen.has(n)){seen.add(n);todo.push(n);}}
 return count;
}
const contractPath='research/strominger/contracts/five-side-oct-routing-obligations-v1.json',contract=JSON.parse(await fs.readFile(contractPath,'utf8'));
const paths=[contractPath,'research/strominger/five-side-oct-routing-obligations-v1.md',...contract.sources.flatMap(s=>s.path?[s.path]:[]),'research/realization-tower/octahedral-full-fibration.mjs','research/realization-tower/octahedral-coherent-routing.mjs','research/realization-tower/five-side-oct-routing-obligations.mjs','research/strominger/checkers/audit_five_side_oct_construction.mjs'];
const evidence=[];for(const path of [...new Set(paths)].sort())evidence.push({path,sha256:createHash('sha256').update(await fs.readFile(path)).digest('hex')});
const obligations=buildFiveSideOctRoutingObligations();
const report={schema:'five-side-oct.construction-audit.v1',verdict:'candidate-not-admitted',constructionAdmitted:false,
 candidate:{wires:model.routes.length,wiresDependingOnAssumedSeams:model.routes.filter(r=>r.links.some(id=>links.get(id).kind==='boundary-seam')).length,nearestLiftAdmissions:model.routes.filter(r=>r.interiorAdmission).length,maxNCellsPerRoute:Math.max(...model.routes.map(r=>r.cells.length))},
 hostileProbes:probes,
 alternativeBoundaryChoice:{changedEndpointMatches:alternate.filter((w,i)=>w.target!==f.wires[i].target).length,nativeMatchesPreserved:true,periodConditionPreserved:true,targetBijectionsPreserved:true,originalComponents:componentCount(f.wires),alternateComponents:componentCount(alternate),scope:'Ambiguity witness inside the existing phase/endpoint conditions, not an alternative coherent solution.'},
 obligationPacket:{inventory:obligations.inventory,readings:obligations.readings.length,entryComparisonIncidences:obligations.readings.reduce((n,r)=>n+r.comparisons.length,0),globalCoherenceObligationsComplete:false},
 gates:contract.completionGates,evidence};
if(process.argv.includes('--record')){const out='research/strominger/results/five-side-oct-obligations-v1';await fs.mkdir(out,{recursive:true});await fs.writeFile(`${out}/audit.json`,JSON.stringify(report,null,2)+'\n');await fs.writeFile(`${out}/obligations.json`,JSON.stringify(obligations,null,2)+'\n');}
console.log(JSON.stringify({...report,evidence:report.evidence.map(e=>e.path)},null,2));
process.exitCode=1;
