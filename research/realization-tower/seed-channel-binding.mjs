// Source-bound four-endpoint candidate. Does not add seed arrows or face equations.
import {readFile} from 'node:fs/promises';
import {createHash} from 'node:crypto';
export async function loadSeed(){
 const source=new URL('../nima/agda/ActualSeedEndpointTable.agda',import.meta.url),text=await readFile(source,'utf8');
 const vertices=text.match(/data Vertex : Type where\s+([A-Z ]+) : Vertex/)[1].trim().split(/\s+/);
 const labels=text.match(/data Occurrence : Type where\s+([A-Z ]+) : Occurrence/)[1].trim().split(/\s+/);
 const rows=labels.map(label=>({label,from:text.match(new RegExp(`^source ${label} = (\\w+)$`,'m'))[1],to:text.match(new RegExp(`^target ${label} = (\\w+)$`,'m'))[1]}));
 if(rows.some(r=>!vertices.includes(r.from)||!vertices.includes(r.to)))throw Error('Source parse mismatch');
 return {vertices,rows,source:'research/nima/agda/ActualSeedEndpointTable.agda',sha256:createHash('sha256').update(text).digest('hex')};
}
export const forward=label=>({label,direction:1});
export const reversePath=path=>path.slice().reverse().map(e=>({...e,direction:-e.direction}));
export function endpoints(seed,start,path){
 let current=start;if(!seed.vertices.includes(start))throw Error('Unknown source');
 for(const edge of path){
  const row=seed.rows.find(r=>r.label===edge.label);if(!row||![1,-1].includes(edge.direction))throw Error('Unknown occurrence or direction');
  const from=edge.direction===1?row.from:row.to,to=edge.direction===1?row.to:row.from;
  if(current!==from)throw Error('Noncomposable path');current=to;
 }
 return {from:start,to:current};
}
export function reducePath(path){
 const result=[];
 for(const edge of path){const last=result.at(-1);if(last?.label===edge.label&&last.direction===-edge.direction)result.pop();else result.push({...edge});}
 return result;
}
export function comparePaths(seed,start,left,right){
 const a=endpoints(seed,start,left),b=endpoints(seed,start,right);if(a.to!==b.to)throw Error('Comparison requires parallel paths');
 const loop=[...left,...reversePath(right)];
 return {from:start,to:a.to,left,right,loop,reducedLoop:reducePath(loop),scope:'Formal path comparison in the free graph realization, not a native reverse execution or a supplied 2-cell'};
}
export function directedPaths(seed,start,maxLength){
 if(!Number.isInteger(maxLength)||maxLength<0)throw Error('Nonnegative path bound required');
 const paths=[];
 function visit(vertex,word){paths.push({from:start,to:vertex,word});if(word.length===maxLength)return;for(const row of seed.rows)if(row.from===vertex)visit(row.to,[...word,forward(row.label)]);}
 visit(start,[]);return paths;
}
export const probe=(path,flips)=>path.reduce((state,edge)=>state^(flips[edge.label]??0),0);
export async function seedChannelStudy(){
 const seed=await loadSeed(),root='A',paths=directedPaths(seed,root,3);
 const rawSourceFibres=Object.fromEntries(seed.vertices.map(v=>[v,seed.rows.filter(r=>r.from===v)]));
 const rawTargetFibres=Object.fromEntries(seed.vertices.map(v=>[v,seed.rows.filter(r=>r.to===v)]));
 const directChannels=Object.fromEntries(seed.vertices.map(v=>[v,seed.rows.filter(r=>r.from===root&&r.to===v)]));
 const endpointFamilies=Object.fromEntries(seed.vertices.map(v=>[v,paths.filter(p=>p.to===v)]));
 const direct=[forward('AB')],via=[forward('AD'),forward('DB')],comparison=comparePaths(seed,root,via,direct);
 const triangleComparison=comparePaths(seed,root,[forward('AB'),forward('BC')],[{label:'CA',direction:-1}]);
 const countermodel=Object.fromEntries(seed.rows.map(r=>[r.label,r.label==='AB'?1:0]));
 const models=Array.from({length:2**seed.rows.length},(_,mask)=>Object.fromEntries(seed.rows.map((r,i)=>[r.label,(mask>>i)&1])));
 const forwardEquation=flips=>probe(via,flips)===probe(direct,flips);
 const triangleEquation=flips=>probe(triangleComparison.left,flips)===probe(triangleComparison.right,flips);
 const defect=probe(comparison.loop,countermodel);
 // A correction is calculable in this probe representation, but does NOT
 // produce the missing path equality in the free realization.
 const correction=probe(via,countermodel)^probe(direct,countermodel);
 return {seed,root,rawSourceFibres,rawTargetFibres,directChannels,endpointFamilies,pathBound:3,
  endpointUniqueness:{seed:new Set(seed.rows.map(r=>`${r.from}:${r.to}`)).size===seed.rows.length,pathTable:new Set(paths.map(r=>`${r.from}:${r.to}`)).size===paths.length},
  interpretation:'Four target-indexed path families after explicit free-path completion; not four primitive outgoing ports. Empty paths are identities, not new seed occurrences.',
  comparison,triangleComparison,countermodel,
  probeResults:{direct:probe(direct,countermodel),via:probe(via,countermodel),loopDefect:defect,correction,correctedVia:probe(via,countermodel)^correction,primitiveBA:probe([forward('BA')],countermodel),formalInverseAB:probe(reversePath(direct),countermodel)},
  assignmentCounts:{all:models.length,forwardEquation:models.filter(forwardEquation).length,triangleEquation:models.filter(triangleEquation).length,both:models.filter(f=>forwardEquation(f)&&triangleEquation(f)).length},
  disposition:{primitiveFourPorts:false,fourEndpointFamilies:true,strictForwardFaceForced:false,retainedNontrivialLoop:true,correctionIsNativeFiller:false,globalAssemblyLawDerived:false},
  scope:'Finite probe illustration of the existing SeedFaceObstruction, not a new proof-assistant theorem. Root A and the target-indexed path interpretation are explicit study choices. Binary transports and their corrections are diagnostic, not a physical or native assembly law.'};
}
