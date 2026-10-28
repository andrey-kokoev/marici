import {fileURLToPath} from 'node:url';import path from 'node:path';
import {presentCentralBelt} from '../../realization-tower/central-belt-layout.mjs';
import {doubleEsd7RuleProcess,doubleEsd7Rules} from '../../realization-tower/double-esd7-process.mjs';
import {filterBeltView} from '../../../examples/normal-ray/complex-visibility.js';
const pointKey=(p,digits=8)=>p.map(v=>Number(v.toFixed(digits))).join(','),edgeKey=(a,b,digits)=>[pointKey(a,digits),pointKey(b,digits)].sort().join('|');
export function chargedFaceComponentAudit({digits=8}={}){
 const source=presentCentralBelt(doubleEsd7RuleProcess(7,doubleEsd7Rules.map(r=>r.id))),view=filterBeltView(source,'geometry'),surfaces=[...view.parentCellulations,view.beltSurface];
 const faces=surfaces.flatMap(s=>s.faces.filter(f=>f.owners.length===1).map(f=>({id:`${s.id}/${f.id}`,shape:s.copy??'belt',role:f.colorRole,owner:`${s.id}/${f.owners[0]}`,vertices:f.indices.map(i=>s.vertices[i]),tipReplacement:Boolean(f.tipReplacement)})));
 const summarize=cs=>Object.fromEntries(['proton','electron'].map(role=>[role,cs.filter(c=>c.role===role).length]));
 function components(rule){
  const parent=faces.map((_,i)=>i),find=i=>parent[i]===i?i:(parent[i]=find(parent[i])),buckets=new Map();
  for(const [i,f] of faces.entries()){
   const keys=rule==='shared-edge'?f.vertices.map((v,j)=>edgeKey(v,f.vertices[(j+1)%3],digits)):rule==='shared-vertex'?f.vertices.map(p=>pointKey(p,digits)):[f.owner];
   for(const key of keys){const k=f.role+'|'+key;if(buckets.has(k))parent[find(i)]=find(buckets.get(k));else buckets.set(k,i);}
  }
  const groups=new Map();for(let i=0;i<faces.length;i++){const root=find(i);if(!groups.has(root))groups.set(root,[]);groups.get(root).push(faces[i]);}
  const records=[...groups.values()].map((fs,i)=>({id:`${rule}:${i}`,role:fs[0].role,faces:fs.map(f=>f.id),owners:[...new Set(fs.map(f=>f.owner))],shapes:[...new Set(fs.map(f=>f.shape))],tipReplacement:fs.some(f=>f.tipReplacement)}));
  const histogram=Object.fromEntries(['proton','electron'].map(role=>[role,records.filter(r=>r.role===role).reduce((a,r)=>(a[r.faces.length]=(a[r.faces.length]??0)+1,a),{})]));
  return {rule,counts:summarize(records),byShape:Object.fromEntries(['original','clone','belt'].map(shape=>[shape,summarize(records.filter(r=>r.shapes.includes(shape)))])),histogram,crossShapeComponents:records.filter(r=>r.shapes.length>1).map(r=>r.id),components:records};
 }
 const rules=['shared-edge','shared-vertex','same-native-cell'].map(components),neutronFillers=surfaces.reduce((n,s)=>n+(s.cellulation?.counts.octahedra??s.counts.octahedra),0),matches=rules.filter(r=>r.counts.proton===82&&r.counts.electron===82).map(r=>r.rule);
 return {obligation:'readout grouping of retained exposed-face records; no native field-map claim',inputs:{parentRules:doubleEsd7Rules.map(r=>r.id),tipPolicy:'two explicit E replacements',belt:'staggered-native-middle',pointTolerance:10**-digits},faceCounts:summarize(faces),neutronFillers,faceRecords:faces,rules,target:{proton:82,neutron:126,electron:82},matchingRules:matches,status:matches.length?'count-match-requires-physical-binding':'no-match-for-tested-groupings',scope:'Rules fixed by adjacency or owner identity, not tuned to 82. Shared-vertex includes existing tip contacts. By-shape counts may share a cross-shape component and must not be added. Connectedness alone is not a particle definition.'};
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url)){
 const result=chargedFaceComponentAudit();console.log(JSON.stringify(process.argv.includes('--full')?result:{faceCounts:result.faceCounts,neutronFillers:result.neutronFillers,rules:result.rules.map(({components,...r})=>r),matchingRules:result.matchingRules,status:result.status},null,2));
}
