// Minimal source-bound diagnostic: full reversal versus same-chamber P/PN ports.
// Does not strengthen the parent to total domain equivalence or physical motion.
import assert from 'node:assert/strict';
import {readFileSync,writeFileSync} from 'node:fs';
import {createHash} from 'node:crypto';
import {GenerativeAssemblyRules} from '../../nima/generative-phase-assembly.mjs';
import {phaseFrame} from '../../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
import {auditPhaseFrame} from '../../strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs';
const names=['C0','M0','C1','M1'],six=['C0','M0','C1','M1','C2','M2'];
const J={C0:'M2',M0:'C2',C1:'M1',M1:'C1',C2:'M0',M2:'C0'};
const permutations=a=>a.length?a.flatMap((v,i)=>permutations(a.filter((_,j)=>i!==j)).map(p=>[v,...p])):[[]];
const r=new GenerativeAssemblyRules(),cell=r.charts[r.packets[r.root].chart].cell,vertices=r.geometry.cells[cell].vertices;
const faces=r.geometry.cells[cell].faces,faceKey=f=>[...f].sort().join('|'),rows=[];let transfers=0;
function nativePorts(chart){const base=r.packet(chart,0,[0,1,2,3,4]);const ops=r.outgoing(base).map(i=>r.operations[i]);
 const pn=ops.find(o=>o.kind==='PN'),reader=ops.find(o=>o.kind==='reader-phase-advance');assert(pn&&reader);
 const next=r.outgoing(reader.target).map(i=>r.operations[i]).find(o=>o.kind==='PN');assert(next);
 for(const op of [pn,reader,next]){assert(r.validateTransfer(op));transfers++;}
 return {base,pn,reader,ports:[pn,next]};}
for(const marking of permutations([0,1,2,3])){
 const aliases=Object.fromEntries(names.map((n,i)=>[n,vertices[marking[i]]]));
 const a=r.completeP(cell,aliases),source=nativePorts(a);
 const ne=r.outgoing(source.pn.target).map(i=>r.operations[i]).find(o=>o.kind==='NE');assert(ne&&r.validateTransfer(ne));transfers++;
 const oldE=r.charts[r.packets[ne.target].chart],dualAliases=Object.fromEntries(six.map(n=>[n,oldE.aliases[J[n]]]));
 const dualE=r.chart(cell,'electron',dualAliases),dualPacket=r.packet(dualE,0,[4,3,2,1,0]);
 const df=phaseFrame(r.charts[dualE],0);assert.equal(auditPhaseFrame(df).status,'native-template-compatible');
 // The reversed old PN face is genuinely a native NE interface, not PN.
 const oldNCell=r.charts[r.packets[source.pn.target].chart].cell;
 const dualN=r.chart(oldNCell,'neutron',dualAliases),dp=r.packet(dualN,0,[4,3,2,1,0]);
 const reverseNE=r.outgoing(dp).map(i=>r.operations[i]).find(o=>o.kind==='NE'&&r.packets[o.target].chart===dualE);
 assert(reverseNE&&r.validateTransfer(reverseNE));transfers++;
 assert.equal(faceKey(reverseNE.face),faceKey(source.pn.face));
 // The existing complementary chart0/7 rule, uniformly applied to all markings.
 // This is an explicitly declared target-selection convention, not a motion.
 const complementary={C0:aliases.M0,M0:aliases.C0,C1:aliases.M1,M1:aliases.C1};
 const b=r.completeP(cell,complementary);assert.notEqual(b,null);const target=nativePorts(b);
 const bodyRoles=Object.fromEntries(names.map(n=>[aliases[n],n[0]]));
 const targetRoles=Object.fromEntries(names.map(n=>[complementary[n],n[0]]));
 const dualRoles=Object.fromEntries([...df.window,df.context].map(o=>[o.vertex,o.role]));
 for(const v of vertices){assert.notEqual(bodyRoles[v],targetRoles[v]);assert.equal(targetRoles[v],dualRoles[v]);}
 const domainA=source.ports.map(o=>faceKey(o.face)).sort(),domainB=target.ports.map(o=>faceKey(o.face)).sort();
 assert.equal(new Set([...domainA,...domainB]).size,4);assert(domainA.every(f=>!domainB.includes(f)));
 const perFace=faces.map(face=>({face:faceKey(face),sourceMCount:face.filter(v=>bodyRoles[v]==='M').length,
  dualMCount:face.filter(v=>dualRoles[v]==='M').length,complementaryPN:domainB.includes(faceKey(face))}));
 assert(perFace.every(f=>f.sourceMCount+f.dualMCount===3));
 assert(perFace.filter(f=>domainA.includes(f.face)).every(f=>f.dualMCount===1&&!f.complementaryPN));
 const pf=phaseFrame(r.charts[b],0),changes=[...df.window,df.context].map(o=>{
  const target=[...pf.window,pf.context].find(t=>t.vertex===o.vertex);assert(target&&target.role===o.role);
  return {vertex:o.vertex,role:o.role,fromIndex:o.index,toIndex:target.index,delta:target.index-o.index};});
 assert.equal(new Set(changes.map(x=>x.delta)).size,2);assert.deepEqual([...new Set(changes.map(x=>x.delta))].sort(),[-2,0]);
 assert.equal(r.outgoing(dualPacket).length,0);
 // Do not manufacture an obstruction by requiring the target's origin to stay0.
 // At origin2, old E's C2/M2 occurrences are retained and C1/M1 advance by2.
 const shifted=phaseFrame(r.charts[b],2);assert.equal(auditPhaseFrame(shifted).status,'native-template-compatible');
 const shiftedChanges=[...df.window,df.context].map(o=>{const t=[...shifted.window,shifted.context].find(t=>t.vertex===o.vertex);return {...o,targetIndex:t.index,delta:t.index-o.index};});
 assert.deepEqual([...new Set(shiftedChanges.map(x=>x.delta))].sort(),[0,2]);
 assert.equal(shiftedChanges.filter(x=>x.delta===0).length,2);
 const shiftedPacket=r.packet(b,2,[0,1,2,3,4]),shiftedPN=r.outgoing(shiftedPacket).map(i=>r.operations[i]).find(o=>o.kind==='PN');assert(shiftedPN&&r.validateTransfer(shiftedPN));transfers++;
 const outside=r.charts[b].aliases.C2;
 rows.push({marking,sourceChart:a,complementaryChart:b,sourceDomain:domainA,targetDomain:domainB,
   fullFourFaceCover:true,dualSameChamberSpecies:'electron',requestedSameChamberSpecies:'proton',
   reversedOldPNKind:reverseNE.kind,dualElectronOutgoingCount:0,perFace,occurrenceReindexing:changes,
   targetOriginTwoFrame:shifted,targetOriginTwoOccurrenceChanges:shiftedChanges,targetOriginTwoPNValid:true,
   targetOutsideC2:outside,targetOutsideC2AlreadyInOldSix:Object.values(oldE.aliases).includes(outside),
   targetFullReference:r.charts[b].aliases,dualFullReference:r.charts[dualE].aliases});
}
assert.equal(rows.length,24);
const controls=[];const reject=(name,f)=>{assert.throws(f);controls.push(name);};
reject('species rename is a P binding',()=>assert.equal(rows[0].dualSameChamberSpecies,rows[0].requestedSameChamberSpecies));
reject('reversed PN is still PN on same face',()=>assert.equal(rows[0].reversedOldPNKind,'PN'));
reject('complementary PN domains are identical',()=>assert.deepEqual(rows[0].sourceDomain,rows[0].targetDomain));
reject('occurrence relabelling is one origin shift',()=>assert.equal(new Set(rows[0].occurrenceReindexing.map(x=>x.delta)).size,1));
const inputs=['research/voevodsky/checkers/check_ramsey_parent_face_binding_diagnostic.mjs',
 'research/nima/generative-phase-assembly.mjs','research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/phase-discipline-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/lattice-items.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/window-construction-model.mjs',
 'research/strominger/demos/particle-overlap-tetrahedron/carrier.mjs'];
const result={schema:'marici.ramsey-parent-face-binding-diagnostic.v1',checkerStatus:'passed',
 node:'negative-direction-policy-native-descent',parent:'face-chart-transition-descent',
 scientificStatus:'minimal_interface_gap_classified_not_intrinsic_hardness_proved',
 markings:24,validatedTransfers:transfers,rows,controls,
 conclusions:{fourFaceConstructionExistsWithDeclaredComplementaryInputs:true,
  wholeReversalDirectlyProducesParentPToPTransition:false,
  totalPointwiseFixedFacePNDomainMap:false,
  unchangedForwardEToPPrimitive:false,
  generalPassiveComparisonRefuted:false,
  parentSourcePolicyChosen:false,intrinsicMathematicalHardnessEstablished:false},
 scope:'Same regular chamber and fixed geometric vertices, all24 markings. This separates a constructed retained cover, an impossible stronger fixed-face domain equivalence, and a missing direct reader/operation typing. It does not require active physical motion or refute independently admitted higher-incidence comparisons.',
 source_sha256:Object.fromEntries(inputs.map(p=>[p,createHash('sha256').update(readFileSync(p)).digest('hex')]))};
writeFileSync('research/voevodsky/results/ramsey-parent-face-binding-diagnostic-v1.json',JSON.stringify(result,null,2)+'\n');
console.log(JSON.stringify({status:result.checkerStatus,markings:24,validatedTransfers:transfers,
 fullFourFaceCovers:rows.filter(r=>r.fullFourFaceCover).length,
 externalContextsAlreadyInOldSix:rows.filter(r=>r.targetOutsideC2AlreadyInOldSix).length,
 gap:'dual E versus complementary P; NE versus PN. Origin2 gives a valid target P frame retaining two occurrences, but no E->P source operation is installed.',controls:controls.length}));
