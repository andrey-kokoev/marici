// Bounded extension test, not a lithium construction or physical no-go theorem.
// Keep the He-4 carriers, global C/M types, native PN/NE grammar, and all four
// proton-reader alternatives. No independently seeded packet is glued in.
import {deriveHelium4Core} from './helium4-core-probe.mjs';
import {itemKey} from './lattice-items.mjs';
const copy=x=>structuredClone(x);
export function probeLithium6Growth(helium3){
 const core=deriveHelium4Core(helium3),names=new Map(Object.entries(core.bindings).map(([n,p])=>[itemKey([p]),n]));
 const ports=[];
 for(const body of core.items){
  const expected=body.vertices.map((_,i)=>itemKey(body.vertices.filter((_,j)=>j!==i))),actual=body.faces.map(itemKey);
  if(body.vertices.length!==4||body.key!==itemKey(body.vertices)||actual.length!==4||new Set(actual).size!==4||actual.some(f=>!expected.includes(f)))throw Error('Retained carrier faces must match its actual tetrahedron');
 }
 for(const candidate of core.alternatives.flat())if(Object.entries(candidate.aliases).some(([local,global])=>local[0]!==global[0]))throw Error('Reader alternative changes a global C/M type');
 for(const [index,body] of core.items.entries()){ 
  if(body.species==='electron')continue;
  for(const face of body.faces){
   const marks=face.map(p=>names.get(itemKey([p])));
   if(marks.some(n=>!n))throw Error('Nuclear face has an unbound global mark');
   const mCount=marks.filter(n=>n.startsWith('M')).length;
   if(![1,2].includes(mCount))throw Error('Expected a retained MMCC nuclear carrier');
   const neighbors=core.items.map((other,i)=>({other,i})).filter(({other,i})=>i!==index&&other.faces.some(f=>itemKey(f)===itemKey(face)));
   if(neighbors.length>1)throw Error('Overoccupied retained face');
   const neighbor=neighbors[0],kind=mCount===2?'PN':body.species==='neutron'?'NE':'no-native-nuclear-step';
   if(kind==='PN'&&neighbor&&neighbor.other.species!==(body.species==='proton'?'neutron':'proton'))throw Error('PN port occupied by the wrong species');
   if(kind==='NE'&&neighbor&&neighbor.other.species!=='electron')throw Error('NE port occupied by the wrong species');
   ports.push({item:index,cell:body.key,species:body.species,face:copy(face),marks,kind,occupiedBy:neighbor?.i??null,neighborCell:neighbor?.other.key??null});
  }
 }
 const pn=ports.filter(p=>p.kind==='PN'),freePN=pn.filter(p=>p.occupiedBy===null),freeNE=ports.filter(p=>p.kind==='NE'&&p.occupiedBy===null);
 // Both N2 electron outputs are constructed by the native reference packets
 // in the core probe, not inferred from a geometric nearest-neighbor search.
 const electronCandidates=[...new Map(core.alternatives.flat().map(c=>[c.continuationElectron.key,{item:copy(c.continuationElectron),face:copy(c.continuationFace)}])).values()];
 for(const candidate of electronCandidates){
  if(core.items.some(i=>i.key===candidate.item.key)||!freeNE.some(p=>itemKey(p.face)===itemKey(candidate.face)))throw Error('Unverified free electron continuation');
 }
 const nuclearFaces=[...new Set(pn.map(p=>itemKey(p.face)))].sort();
 const variants=core.variants.map(v=>{
  const nuclearFaceKeys=[...new Set(v.steps.filter(s=>s.kind==='PN').map(s=>itemKey(s.event.face)))].sort();
  if(JSON.stringify(nuclearFaceKeys)!==JSON.stringify(nuclearFaces))throw Error('Reader circuit changes the audited nuclear face set');
  return {choices:[...v.choices],operatorOrder:v.order,nuclearFaceKeys,freeNuclearPorts:freePN.length,canAddProton:freePN.some(p=>p.species==='neutron'),canAddNeutron:freePN.some(p=>p.species==='proton'),disposition:freePN.length?'requires-further-construction-search':'blocked-before-transport'};
 });
 return {status:freePN.length?'open-extension-search':'blocked-retained-core-growth',target:{isotope:'lithium6',proton:3,neutron:3,electron:3},retainedCounts:copy(core.counts),deficit:{proton:1,neutron:1,electron:1},items:copy(core.items),bindings:copy(core.bindings),ports,variants,
  nuclearInterfaces:new Set(pn.map(p=>itemKey(p.face))).size,freeNuclearPorts:freePN.length,freeElectronPorts:freeNE.length,electronCandidates,
  ambiguityResolved:false,constructedLithium:false,newCarriersCommitted:0,
  scope:'Bounded test of face-connected growth from the retained He-4 core under the existing PN/NE grammar and fixed global C/M types. All four proton-reader alternatives are tested without isotope-specific repairs. Saturation blocks the next nuclear addition, not all possible lithium constructions. Rearrangement, independent packet gluing, new interfaces, and changes of C/M type are outside this test.'};
}
