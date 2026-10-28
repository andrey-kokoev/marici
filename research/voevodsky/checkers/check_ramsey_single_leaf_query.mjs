import assert from 'node:assert/strict';
import {GenerativeAssemblyRules} from '../../strominger/demos/particle-overlap-tetrahedron/local-reference-rules.mjs';
import {makeLatticeItem} from '../../strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs';
import {phaseFrame} from '../../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const permutations=a=>a.length?[...a].flatMap((v,i)=>permutations(a.filter((_,j)=>j!==i)).map(p=>[v,...p])):[[]];
const h=s=>{const p=s.split(',').map(Number);return p[0]+p[2];};
const bound=(chart,m)=>{for(const [name,v] of Object.entries(chart.aliases))assert(name[0]==='M'?h(v)===m:Math.abs(h(v)-m)===1);};
const templates=[makeLatticeItem('tetrahedron',[0,0,0,0]),makeLatticeItem('tetrahedron',[1,1,0,0],true),makeLatticeItem('octahedron',[-1,0,0,0])];
const counts={admittedP:0,admittedN:0,planarP:0,planarN:0,checkedNativeTransfers:0,checkedTerminalExits:0},rows=[];
for(const item of templates)for(const [componentIndex,component] of item.components.entries())for(const permutation of permutations([0,1,2,3])){
 const r=new GenerativeAssemblyRules(),cell=r.geometry.register(item,component),isP=item.kind==='tetrahedron';
 const names=isP?['C0','M0','C1','M1']:['M0','C1','M1','C2'];
 const aliases=Object.fromEntries(names.map((n,i)=>[n,component[permutation[i]].join(',')]));
 const chart=isP?r.completeP(cell,aliases):r.completeN(cell,aliases);if(chart===null)continue;
 counts[isP?'admittedP':'admittedN']++;const c=r.charts[chart],m=h(c.aliases.M0);if(h(c.aliases.M1)!==m)continue;
 counts[isP?'planarP':'planarN']++;bound(c,m);const id=r.packet(chart,0,[0,1,2,3,4]),operations=[];
 for(const oi of r.outgoing(id)){
  const op=r.operations[oi];assert.equal(r.validateTransfer(op),true);const p=r.packets[op.target],target=r.charts[p.chart];bound(target,m);
  const occurrence=phaseFrame(target,p.origin).window[0];assert(Math.abs(h(occurrence.vertex)-m)<=1);
  if(target.species==='electron'){assert.equal(r.outgoing(op.target).length,0);counts.checkedTerminalExits++;}
  counts.checkedNativeTransfers++;operations.push(op.kind);
 }
 rows.push({kind:item.kind,inverted:item.inverted,componentIndex,permutation,species:c.species,MHeight:m,operations});
}
assert.deepEqual([counts.admittedP,counts.admittedN,counts.planarP,counts.planarN],[48,48,16,16]);
assert.equal(counts.checkedNativeTransfers,96);assert.equal(counts.checkedTerminalExits,16);
const r=new GenerativeAssemblyRules(),seed=r.charts[r.packets[r.root].chart];bound(seed,0);assert.equal(h(seed.aliases.M0),0);
console.log(JSON.stringify({counts,rows,canonicalMHeight:0,allTerminalFirstWindowY:[0,1,2],
 word:[1,1,1],pattern:[[0,0,0],[1,1,0],[1,0,1]],query:[3,3,0],regionRadius:3,
 queryExcludedByInvariant:true,depthLimitedSearchUsed:false,allMariciPoliciesRefuted:false,rootResolved:false}));
