import {lattice,items,available,reserved,witnessPairs} from './fiber-space-model.mjs';
import {faces,worldPoint} from './simplex-model.mjs';
import {primitives} from './simplex-components.mjs';
const units=primitives.regular.vertices,permutations=[[0,1,2,3],[3,0,1,2],[2,3,0,1],[1,2,3,0]];
const key=vertices=>vertices.map(p=>p.join(',')).sort().join('|');
const templates=[{kind:'tetrahedron',inverted:false,vertices:units},{kind:'tetrahedron',inverted:true,vertices:units.map(p=>p.map(x=>-x))},{kind:'octahedron',inverted:false,vertices:units.flatMap((a,i)=>units.slice(i+1).map(b=>a.map((x,j)=>x+b[j])))}];
function shape(kind,origin,inverted=false){
 const components=kind==='tetrahedron'?[units.map(p=>origin.map((x,i)=>x+(inverted?-p[i]:p[i])))]:permutations.map(perm=>primitives.splitOctahedron.vertices.map(p=>origin.map((x,i)=>x+p[perm[i]])));
 const vertexMap=new Map(components.flat().map(p=>[p.join(','),p])),vertices=[...vertexMap.values()],table=new Map();
 for(const c of components)for(const face of faces){const f=face.map(i=>c[i]),k=key(f);if(!table.has(k))table.set(k,{vertices:f,count:0});table.get(k).count++;}
 return {kind,origin,inverted,components,vertices,key:key(vertices),faces:[...table.values()].filter(f=>f.count===1).map(f=>f.vertices),center:vertices.reduce((a,p)=>a.map((x,i)=>x+p[i]/vertices.length),[0,0,0,0])};
}
const base=items.map(i=>({...shape(i.kind,i.origin,i.inverted),itemIndex:i.index,itemId:i.id})),occupiedKeys=new Set(base.map(s=>s.key));
const neighborCache=new Map();
function across(source,face){
 const fk=key(face),cacheKey=source.key+'>'+fk;if(neighborCache.has(cacheKey))return neighborCache.get(cacheKey);
 const candidates=new Map();
 for(const t of templates)for(const offset of t.vertices){
  const origin=face[0].map((x,i)=>x-offset[i]);
  const vertices=t.vertices.map(p=>p.map((x,i)=>x+origin[i]));
  if(!face.every(p=>vertices.some(q=>p.every((x,i)=>x===q[i]))))continue;
  const s=shape(t.kind,origin,t.inverted);if(s.key!==source.key&&s.faces.some(f=>key(f)===fk))candidates.set(s.key,s);
 }
 if(candidates.size!==1)throw Error('Expected one neighboring lattice item across '+fk+'; found '+candidates.size);
 const result=[...candidates.values()][0];neighborCache.set(cacheKey,result);return result;
}
function gapShape(parts){
 if(parts.length===1)return parts[0];
 const components=parts.flatMap(p=>p.components),vertices=[...new Map(components.flat().map(p=>[p.join(','),p])).values()],table=new Map();
 for(const c of components)for(const f of faces){const face=f.map(i=>c[i]),k=key(face);if(!table.has(k))table.set(k,{vertices:face,count:0});table.get(k).count++;}
 return {kind:'gap',parts,components,vertices,key:key(vertices),faces:[...table.values()].filter(f=>f.count===1).map(f=>f.vertices),center:components.flat().reduce((a,p)=>a.map((x,i)=>x+p[i]/(4*components.length)),[0,0,0,0])};
}
// Candidate chains follow a supporting face of the original envelope outward.
// They use existing honeycomb shapes, never reflected off-lattice tetrahedral caps.
const domains=[...available].map(index=>{
 const proton=base[index],options=new Map();
 for(const face of proton.faces){
  const axis=[0,1,2,3].find(i=>face.every(p=>p[i]===2));if(axis===undefined)continue;
  const first=across(proton,face);if(occupiedKeys.has(first.key)||first.center[axis]<=proton.center[axis])continue;
  function extend(parts){
   const last=parts.at(-1);
   for(const nextFace of last.faces){
    const next=across(last,nextFace);
    if(occupiedKeys.has(next.key)||next.center[axis]<=last.center[axis])continue;
    if(next.kind==='tetrahedron'){
     const neutron=gapShape(parts),electron=next,resources=[...parts.map(p=>p.key),electron.key];
     options.set(neutron.key+'>'+electron.key,{proton,neutron,electron,axis,resources,gapItems:parts,protonNeutronFace:face,neutronElectronFace:nextFace});
    }else if(parts.length===1){
     // An octahedron is intervening volume, never an electron. Extend to
     // the next regular tetrahedron and fill both intervening lattice items.
     extend([...parts,next]);
    }
   }
  }
  extend([first]);
 }
 return {index,options:[...options.values()].sort((a,b)=>(a.neutron.key+'>'+a.electron.key).localeCompare(b.neutron.key+'>'+b.electron.key))};
});
if(domains.some(d=>!d.options.length))throw Error('A proton has no outward P–N–e lattice chain');
// Constraint search, not independent nearest-cell placement. All constituent
// lattice items must be distinct, including composite neutron gaps.
// Address ordering breaks ties; uniqueness is NOT claimed.
const used=new Set(),chosen=new Map();let searchNodes=0;
function solve(){
 if(++searchNodes>200000)throw Error('Chain search budget exhausted');
 if(chosen.size===domains.length)return true;
 let selected=null,options=null;
 for(const domain of domains){if(chosen.has(domain.index))continue;const valid=domain.options.filter(o=>o.resources.every(k=>!used.has(k)));if(!valid.length)return false;if(!options||valid.length<options.length){selected=domain;options=valid;}}
 for(const option of options){chosen.set(selected.index,option);option.resources.forEach(k=>used.add(k));if(solve())return true;option.resources.forEach(k=>used.delete(k));chosen.delete(selected.index);}
 return false;
}
if(!solve())throw Error('No disjoint 82-chain assignment exists in the enumerated outward neighborhood');
export const lead208Chains=[...chosen].sort(([a],[b])=>a-b).map(([index,chain],i)=>({...chain,id:i+1,protonItem:index}));
const speciesColor={proton:0x50cfff,neutron:0xffcf72,electron:0xff7edb};
function body(id,species,s,role,chain=null){return {id,species,role,chain,color:speciesColor[species],shape:s,components:s.components,center:worldPoint(s.center),points:s.vertices.map(worldPoint)};}
export const lead208Bodies=[
 ...[...reserved].map((index,i)=>body('Nw'+(i+1),'neutron',base[index],'witness')),
 ...lead208Chains.flatMap(c=>[body('P'+c.id,'proton',c.proton,'proton',c.id),body('N'+c.id,'neutron',c.neutron,'outer-neutron',c.id),body('e'+c.id,'electron',c.electron,'electron',c.id)]),
];
export const lead208AddedBodies=lead208Bodies.filter(b=>['outer-neutron','electron'].includes(b.role));
export const lead208WitnessLinks=witnessPairs.map(p=>[items[p.inner].center,items[p.outer].center]);
export const lead208Construction={counts:{proton:82,neutron:126,electron:82},chains:lead208Chains.length,addedItems:lead208AddedBodies.length,addedLatticeItems:lead208Chains.reduce((n,c)=>n+c.gapItems.length+1,0),addedComponents:lead208AddedBodies.reduce((n,b)=>n+b.components.length,0),searchNodes,candidateChains:domains.map(d=>({protonItem:d.index,count:d.options.length})),electronShape:'regular tetrahedron',compositeNeutrons:lead208Chains.filter(c=>c.gapItems.length>1).length,convention:'Regular tetrahedral electrons; neutron volumes fill the connected intervening lattice items in each outward P–N–e chain. This is a local connector-gap construction, not a proof that all global voids are filled. Address ordering breaks ties; no unique or physical derivation is claimed.'};
