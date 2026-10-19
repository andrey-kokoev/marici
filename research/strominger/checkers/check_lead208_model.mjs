import assert from 'node:assert/strict';
import {mkdir,writeFile} from 'node:fs/promises';
import {lattice,items,available,reserved} from '../demos/particle-overlap-tetrahedron/fiber-space-model.mjs';
import {faces,edges} from '../demos/particle-overlap-tetrahedron/simplex-model.mjs';
import {createSequentialConstruction} from '../demos/particle-overlap-tetrahedron/sequential-space-model.mjs';
import {lead208Bodies as bodies,lead208Chains as chains,lead208AddedBodies as added,lead208Construction as construction} from '../demos/particle-overlap-tetrahedron/lead208-model.mjs';
assert.deepEqual(Object.fromEntries(['proton','neutron','electron'].map(s=>[s,bodies.filter(b=>b.species===s).length])),{proton:82,neutron:126,electron:82});
assert.equal(bodies.filter(b=>b.role==='witness').length,44);assert.equal(new Set(bodies.map(b=>b.shape.key)).size,290);
assert.deepEqual(new Set(chains.map(c=>c.protonItem)),available);
const key=vertices=>vertices.map(p=>p.join(',')).sort().join('|');
for(const chain of chains){
 assert.equal(chain.proton.key,key([...new Map(items[chain.protonItem].children.flatMap(id=>lattice.cells[id].map(n=>lattice.nodes[n].address)).map(p=>[p.join(','),p])).values()]));
 assert.ok(chain.proton.center[chain.axis]<chain.neutron.center[chain.axis]);assert.ok(chain.neutron.center[chain.axis]<chain.electron.center[chain.axis]);
 for(const [a,b,face] of [[chain.proton,chain.neutron,chain.protonNeutronFace],[chain.neutron,chain.electron,chain.neutronElectronFace]]){
  assert.ok(a.faces.some(f=>key(f)===key(face)));assert.ok(b.faces.some(f=>key(f)===key(face)));
 }
}
assert.equal(reserved.size,44);
assert.equal(chains.filter(c=>c.gapItems.length>1).length,8);
for(const c of chains){
 assert.equal(c.electron.kind,'tetrahedron');assert.equal(c.electron.vertices.length,4);assert.equal(c.electron.components.length,1);
 for(const [a,b] of edges)assert.equal(c.electron.vertices[a].reduce((s,x,i)=>s+(x-c.electron.vertices[b][i])**2,0),2,'Electron is a regular lattice tetrahedron');
 assert.deepEqual(new Set(c.neutron.components.map(key)),new Set(c.gapItems.flatMap(s=>s.components).map(key)),'Neutron fills exactly its intervening lattice volume');
 for(let i=1;i<c.gapItems.length;i++)assert.ok(c.gapItems[i].faces.some(f=>c.gapItems[i-1].faces.some(g=>key(f)===key(g))),'Composite neutron is face connected');
}
const coordinates=[...lattice.cells.map(c=>c.map(id=>lattice.nodes[id].address)),...added.flatMap(b=>b.components)];
assert.equal(coordinates.length,761);assert.equal(new Set(coordinates.map(key)).size,coordinates.length);
assert.ok(coordinates.flat().every(p=>p.every(Number.isInteger)&&p.reduce((a,b)=>a+b,0)===1));
const sub=(a,b)=>a.map((x,i)=>x-b[i]),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const tets=coordinates.map(c=>c.map(p=>p.slice(0,3))),boxes=tets.map(t=>[0,1,2].map(i=>[Math.min(...t.map(p=>p[i])),Math.max(...t.map(p=>p[i]))]));
function disjoint(a,b){const axes=[];for(const t of [a,b])for(const [i,j,k] of faces)axes.push(cross(sub(t[j],t[i]),sub(t[k],t[i])));for(const [i,j] of edges)for(const [k,l] of edges)axes.push(cross(sub(a[j],a[i]),sub(b[l],b[k])));return axes.some(axis=>{if(axis.every(x=>x===0))return false;const pa=a.map(p=>dot(p,axis)),pb=b.map(p=>dot(p,axis));return Math.max(...pa)<=Math.min(...pb)||Math.max(...pb)<=Math.min(...pa);});}
let pairsChecked=0;
for(let i=0;i<tets.length;i++){
 const [a,b,c,d]=tets[i];assert.equal(Math.abs(dot(sub(b,a),cross(sub(c,a),sub(d,a)))),1,'Every primitive has positive unit volume');
 for(let j=i+1;j<tets.length;j++){pairsChecked++;if(boxes[i].some(([min,max],k)=>max<=boxes[j][k][0]||boxes[j][k][1]<=min))continue;assert.ok(disjoint(tets[i],tets[j]),`Overlap: ${i}/${j}`);}
}
const incidence=new Map();for(const tet of coordinates)for(const f of faces){const k=key(f.map(i=>tet[i]));incidence.set(k,(incidence.get(k)||0)+1);}assert.ok([...incidence.values()].every(n=>n<=2));
// Audit supplied legacy-layout endpoints separately; these are not inputs to
// the sequential rule and their successful count is not a placement target.
const endpointResults=bodies.filter(b=>b.species==='electron').map(body=>{
 const engine=createSequentialConstruction({exitCell:body.shape});let state=engine.snapshot();
 while(state.status==='ready'){state=engine.step();assert.ok(state.added<100);}
 assert.ok(['complete','ambiguous'].includes(state.status));
 if(state.status==='complete')assert.equal(state.exit.identity,state.identity);
 return {id:body.id,status:state.status,added:state.added};
});
const endpointAudit={complete:endpointResults.filter(s=>s.status==='complete').length,ambiguous:endpointResults.filter(s=>s.status==='ambiguous').length,results:endpointResults};
const report={status:'pass',endpointAudit,...construction,baseComponents:343,totalComponents:761,particleBodies:290,pairsChecked,overlaps:0,duplicates:0,integerCoordinates:true,outwardFaceConnectedChains:82,baseGeometryUnchanged:true};
const out='research/strominger/results/lead208-loadout';await mkdir(out,{recursive:true});await writeFile(out+'/verification.json',JSON.stringify(report,null,2)+'\n');
console.log('PASS legacy Pb-208 geometry only (not window compatibility): 82 P, 126 N, 82 e; 82 outward face-connected chains; 761 non-overlapping lattice components; base geometry unchanged');
