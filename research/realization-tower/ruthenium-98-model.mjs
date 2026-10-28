const units=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>+(i===j)));
const oct=units.flatMap((a,i)=>units.slice(i+1).map(b=>a.map((x,j)=>x+b[j])));
const templates=[{kind:'tetrahedron',offsets:units},{kind:'tetrahedron',offsets:units.map(p=>p.map(x=>-x))},{kind:'octahedron',offsets:oct}];
export const ruthenium98Envelope=units.map(p=>p.map(x=>5*x-1));
const key=vs=>vs.map(v=>v.join(',')).sort().join('|');
const centre=vs=>vs[0].map((_,i)=>vs.reduce((s,v)=>s+v[i]/vs.length,0));
function compositions(n){const out=[];for(let a=0;a<=n;a++)for(let b=0;b<=n-a;b++)for(let c=0;c<=n-a-b;c++)out.push([a,b,c,n-a-b-c]);return out;}
function shape(kind,vertices){
 const faces=[];for(let i=0;i<vertices.length;i++)for(let j=i+1;j<vertices.length;j++)for(let k=j+1;k<vertices.length;k++){
  const f=[vertices[i],vertices[j],vertices[k]];if(f.every((a,i)=>f.slice(i+1).every(b=>a.reduce((s,x,l)=>s+(x-b[l])**2,0)===2)))faces.push(f);
 }
 return {kind,vertices,faces,key:key(vertices),center:centre(vertices),components:[]};
}
function gap(parts){
 if(parts.length===1)return {...parts[0],parts};
 const table=new Map();for(const part of parts)for(const f of part.faces){const k=key(f);if(!table.has(k))table.set(k,{face:f,count:0});table.get(k).count++;}
 const vertices=[...new Map(parts.flatMap(p=>p.vertices).map(v=>[v.join(','),v])).values()];
 return {kind:'gap',vertices,faces:[...table.values()].filter(f=>f.count===1).map(f=>f.face),center:centre(vertices),key:key(vertices),components:[],parts};
}
let cached,carrier;
export function buildRuthenium98Carrier(){
 if(carrier)return carrier;
 const base=[];
 for(const [kind,origins,offsets,role]of [['tetrahedron',compositions(4),units,'proton'],['tetrahedron',compositions(2),units.map(p=>p.map(x=>1-x)),'electron'],['octahedron',compositions(3),oct,'neutron']])for(const o of origins){
  const s=shape(kind,offsets.map(p=>p.map((x,i)=>x+o[i]-1)));
  base.push({...s,id:`ru:base:${base.length}`,role,outer:s.faces.some(f=>[0,1,2,3].some(i=>f.every(v=>v[i]===-1))),seed:s.center.every(x=>x===.25)});
 }
 carrier=base;return carrier;
}
// Separate retained-witness research construction; not the viewer presentation.
export function buildRuthenium98(){
 if(cached)return cached;
 const base=buildRuthenium98Carrier();
 const faceTable=new Map();for(const c of base)for(const f of c.faces){const k=key(f);if(!faceTable.has(k))faceTable.set(k,[]);faceTable.get(k).push(c.id);}
 const byId=new Map(base.map(c=>[c.id,c])),inner=base.filter(c=>!c.outer&&!c.seed&&c.kind==='tetrahedron'),outer=base.filter(c=>c.outer);
 const adj=new Map(inner.map(c=>[c.id,c.faces.flatMap(f=>faceTable.get(key(f)).filter(id=>byId.get(id).outer))])),matched=new Map();
 function augment(id,seen){for(const j of adj.get(id)){if(seen.has(j))continue;seen.add(j);if(!matched.has(j)||augment(matched.get(j),seen)){matched.set(j,id);return true;}}return false;}
 for(const c of inner)if(!augment(c.id,new Set()))throw Error('Ruthenium witness matching failed');
 let witnesses,protons;const occupied=new Set(base.map(c=>c.key)),neighbors=new Map();
 function across(source,face){
  const cacheKey=source.key+'>'+key(face);if(neighbors.has(cacheKey))return neighbors.get(cacheKey);
  const options=new Map();for(const t of templates)for(const offset of t.offsets){
   const origin=face[0].map((x,i)=>x-offset[i]),vertices=t.offsets.map(p=>p.map((x,i)=>x+origin[i]));
   if(!face.every(p=>vertices.some(q=>String(p)===String(q))))continue;
   const s=shape(t.kind,vertices);if(s.key!==source.key&&s.faces.some(f=>key(f)===key(face)))options.set(s.key,s);
  }
  if(options.size!==1)throw Error('Expected one native face neighbor');
  const result=[...options.values()][0];neighbors.set(cacheKey,result);return result;
 }
 const allDomains=outer.map(proton=>{
  const options=new Map();for(const face of proton.faces){
   const axis=[0,1,2,3].find(i=>face.every(p=>p[i]===-1));if(axis===undefined)continue;
   const first=across(proton,face);if(occupied.has(first.key)||first.center[axis]>=proton.center[axis])continue;
   function extend(parts){const last=parts.at(-1);for(const nextFace of last.faces){
    const next=across(last,nextFace);if(occupied.has(next.key)||next.center[axis]>=last.center[axis])continue;
    if(next.kind==='tetrahedron'){
     const neutron=gap(parts),resources=[...parts.map(p=>p.key),next.key];
     options.set(neutron.key+'>'+next.key,{proton,neutron,electron:next,resources,axis,protonNeutronFace:face,neutronElectronFace:nextFace});
    }else if(parts.length===1)extend([...parts,next]);
   }}extend([first]);
  }
  return {id:proton.id,options:[...options.values()].sort((a,b)=>(a.neutron.key+'>'+a.electron.key).localeCompare(b.neutron.key+'>'+b.electron.key))};
 });
 const used=new Set(),chosen=new Map();let searchNodes=0,trialNodes=0,domains;
 function solve(){
  searchNodes++;if(++trialNodes>1000)return false;
  if(chosen.size===domains.length)return true;
  let selected,options;const remaining=[];for(const domain of domains){if(chosen.has(domain.id))continue;const valid=domain.options.filter(o=>o.resources.every(k=>!used.has(k)));if(!valid.length)return false;remaining.push({domain,valid});if(!options||valid.length<options.length){selected=domain;options=valid;}}
  const cost=o=>remaining.filter(r=>r.domain!==selected).reduce((s,r)=>s+r.valid.filter(v=>v.resources.some(k=>o.resources.includes(k))).length,0);
  options.sort((a,b)=>cost(a)-cost(b));
  for(const o of options){chosen.set(selected.id,o);o.resources.forEach(k=>used.add(k));if(solve())return true;o.resources.forEach(k=>used.delete(k));chosen.delete(selected.id);}return false;
 }
 let solved=false,randomState=98,matchingAttempt=0;
 const random=()=>((randomState=(Math.imul(randomState,1664525)+1013904223)>>>0)/4294967296);
 for(;matchingAttempt<128&&!solved;matchingAttempt++){
  if(matchingAttempt){
   for(const neighbors of adj.values())for(let i=neighbors.length-1;i>0;i--){const j=Math.floor(random()*(i+1));[neighbors[i],neighbors[j]]=[neighbors[j],neighbors[i]];}
   matched.clear();for(const c of inner)if(!augment(c.id,new Set()))throw Error('Ruthenium witness matching failed');
  }
  witnesses=outer.filter(c=>matched.has(c.id));protons=outer.filter(c=>!matched.has(c.id));domains=allDomains.filter(d=>!matched.has(d.id));
  used.clear();chosen.clear();trialNodes=0;solved=solve();
 }
 if(!solved)throw Error('No disjoint Ruthenium outward chain assignment within the bounded matching search');
 const chains=protons.map(p=>chosen.get(p.id));
 const body=(s,id,role,extra={})=>({...s,id,role,...extra});
 const context=base.filter(c=>!c.outer).map(c=>body(c,c.id,null));
 const carrier=outer.map(c=>body(c,c.id,matched.has(c.id)?'neutron':'proton',{witness:matched.has(c.id)}));
 const extensions=chains.flatMap((c,i)=>[body(c.neutron,`ru:N:${i+1}`,'neutron',{chain:i+1}),body(c.electron,`ru:E:${i+1}`,'electron',{chain:i+1})]);
 cached={base,carrier,context,extensions,chains,witnessPairs:[...matched].map(([outer,inner])=>({outer,inner})),
  audit:{edgeUnits:5,baseCells:base.length,outerSites:outer.length,witnesses:witnesses.length,structuralContext:context.length,chains:chains.length,proton:protons.length,neutron:witnesses.length+chains.length,electron:chains.length,compositeNeutrons:chains.filter(c=>c.neutron.parts.length>1).length,searchNodes,matchingAttempts:matchingAttempt,
   convention:'Jointly searched native witness matching and disjoint outward P–N–E chains. Bounded matching alternatives use fixed seed 98; chain choices use least-constraining-first with address-order ties.'}};
 return cached;
}
