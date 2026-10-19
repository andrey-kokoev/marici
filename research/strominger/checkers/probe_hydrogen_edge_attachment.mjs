// H-1/H-2 endpoint geometry and composition probe. No new admitted rule.
import assert from 'node:assert/strict';
import {readFile,writeFile,mkdir} from 'node:fs/promises';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {makeLatticeItem} from '../demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {windowProtocol} from '../demos/particle-overlap-tetrahedron/window-construction-model.mjs';
function* permutations(a){if(!a.length)yield [];for(const x of a)for(const p of permutations(a.filter(y=>y!==x)))yield [x,...p];}
const seed=makeLatticeItem('tetrahedron',[0,0,0,0]),marks=['C0','M0','C1','M1'],rows=[];
for(const marking of permutations([0,1,2,3])){
 const seedBindings=Object.fromEntries(marks.map((k,i)=>[k,seed.vertices[marking[i]].join(',')])),r=new GenerativeAssemblyRules({seedBindings}),p=r.root;
 const pn=r.outgoing(p).map(i=>r.operations[i]).find(o=>o.kind==='PN');assert.ok(pn);const n=pn.target,ne=r.outgoing(n).map(i=>r.operations[i]).find(o=>o.kind==='NE');assert.ok(ne);const e=ne.target;
 r.validateTransfer(pn);r.validateTransfer(ne);
 const pc=r.charts[r.packets[p].chart],nc=r.charts[r.packets[n].chart],ec=r.charts[r.packets[e].chart],vertices=c=>r.geometry.cells[c.cell].vertices;
 const shared=vertices(pc).filter(v=>vertices(ec).includes(v));assert.equal(shared.length,2);assert.deepEqual([...shared].sort(),[pc.aliases.C1,pc.aliases.M1].sort());
 const h2=r.inspect([p,n,e]),h1=r.inspect([p,e]);assert.deepEqual(h2.counts,{proton:1,neutron:1,electron:1});assert.equal(h2.certifiedExit,true);assert.deepEqual(h1.counts,{proton:1,neutron:0,electron:1});assert.equal(h1.valid,true);assert.equal(h1.certifiedExit,false);assert.equal(h1.allPacketsCanReachExit,false);
 const outgoing=r.outgoing(p).map(i=>r.operations[i]);assert.ok(!outgoing.some(o=>o.target===e));
 const composite=ne.permutation.map(i=>pn.permutation[i]);assert.deepEqual(composite.map(i=>r.packets[p].permutation[i]),r.packets[e].permutation);assert.deepEqual([...composite].sort(),[0,1,2,3,4]);
 assert.throws(()=>r.validateTransfer({source:p,target:e,kind:'PE-edge',phaseDelta:0,permutation:composite,face:shared}),/Unknown native transfer/);
 const point=v=>r.geometry.points.get(v),bodies=[pc,nc,ec].map(c=>({species:c.species,cell:c.cell,vertices:vertices(c).map(point),aliases:c.aliases}));
 const liveShared=windowProtocol[0].window.filter(k=>windowProtocol[2].window.includes(k));assert.deepEqual(liveShared,['C1']);
 rows.push({marking,seedBindings,sharedEdge:{marks:['C1','M1'],vertices:shared.map(point)},sharedActiveWindowMarks:liveShared,electronGeometry:r.geometry.cells[ec.cell].geometry,h1:{inspection:h1,rootCanReachElectron:false},h2:{inspection:h2,rootCanReachElectron:true},referenceNeutronCell:nc.cell,packets:[r.packets[p],r.packets[n],r.packets[e]],operations:[pn,ne],compositePermutation:composite,bodies});
}
const sourceHashes={};for(const f of ['./probe_hydrogen_edge_attachment.mjs','../../nima/generative-phase-assembly.mjs','../demos/particle-overlap-tetrahedron/lattice-items.mjs','../demos/particle-overlap-tetrahedron/simplex-components.mjs','../demos/particle-overlap-tetrahedron/window-construction-model.mjs'])sourceHashes[f]=createHash('sha256').update(await readFile(new URL(f,import.meta.url))).digest('hex');
const out='research/strominger/results/hydrogen-edge-attachment';await mkdir(out,{recursive:true});const result={status:'edge-geometry-confirmed-direct-transfer-not-admitted',markings:rows.length,allEndpointsShareEdge:true,allH2NativeCertified:true,allH1FailNativeExit:true,compositePermutations:[...new Set(rows.map(r=>JSON.stringify(r.compositePermutation)))].map(JSON.parse),electronGeometryCounts:Object.fromEntries(['proton','split'].map(k=>[k,rows.filter(r=>r.electronGeometry===k).length])),sourceHashes,rows,scope:'All 24 seed markings, existing uniform subdivision, grade-zero native PN then NE. Removing N preserves P/E endpoints and C/M roles but deletes their rooted native transfer path. Composition is a two-face reference map, not evidence of a direct edge interaction, virtual particle, global field sewing, spin or binding law. Production/viewer untouched.'};await writeFile(out+'/verification.json',JSON.stringify(result,null,2)+'\n');console.log(JSON.stringify({status:result.status,markings:result.markings,compositePermutations:result.compositePermutations,electronGeometryCounts:result.electronGeometryCounts}));
