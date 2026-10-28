import {makeFourByFourFiller,fillerEndpointReadout} from '../strominger/four-by-four-filler-model.mjs';
const filler=makeFourByFourFiller();
export const neutralExtensionSize=2*56+filler.residualBasis.length;
const packet=()=>Array.from({length:5},()=>[0,0]);
export const zeroNeutralValues=()=>Array.from({length:neutralExtensionSize},packet);
export function validateNeutralValues(values){
 if(!Array.isArray(values)||values.length!==neutralExtensionSize||Array.from(values).some(p=>!Array.isArray(p)||p.length!==5||Array.from(p).some(z=>!Array.isArray(z)||z.length!==2||!Number.isFinite(z[0])||!Number.isFinite(z[1]))))throw Error('126 complete five-complex-coefficient neutral packets required');
 return values;
}
export function restoreNeutralValues(values){try{return validateNeutralValues(values).map(p=>p.map(z=>[...z]));}catch{return zeroNeutralValues();}}
export function buildNeutralExtension(geometry){
 const sites=geometry.filter(g=>g.kind==='octahedron');
 if(sites.length!==56||new Set(sites.map(g=>g.id)).size!==56||sites.some(g=>g.polarityRoles.positive!=='neutron'||g.polarityRoles.negative!=='neutron'))throw Error('56 distinct neutral octahedral sites required');
 const center=g=>g.vertices[0].map((_,i)=>g.vertices.reduce((s,v)=>s+v[i]/g.vertices.length,0));
 const modes=['positive','negative'].flatMap((sheet,s)=>sites.map((g,i)=>({id:`N:${sheet}:${g.id}`,kind:'site-channel',sheet,site:g.id,point:center(g),embedding:[{coordinate:s*56+i,weight:1}]})));
 for(const [i,b] of filler.residualBasis.entries())modes.push({id:`N:residual:${i}`,kind:'residual-channel',basisKind:b.kind,embedding:b.vector.flatMap((weight,j)=>weight?[{coordinate:112+j,weight}]:[])});
 return {modes,ambientCoordinates:128,counts:{positiveSites:56,negativeSites:56,residual:14,total:modes.length},complexCoefficientCount:5*modes.length,
  physicalCellsAdded:0,derivedFromNativeReplay:false,physicalNeutronsEstablished:false,
  assumption:'Explicit direct-sum extension: two independent site-channel banks plus the free boundary kernel. The native sheet-link constraint is not imposed on these added channels; independence and residual freedoms are stipulated by this new model, not derived from native replay. Channel dimensions are not particle occupation numbers.'};
}
export function liftNeutralValues(extension,values){
 validateNeutralValues(values);const ambient=Array.from({length:extension.ambientCoordinates},packet);
 for(const [i,m] of extension.modes.entries())for(const {coordinate,weight} of m.embedding)for(let c=0;c<5;c++)for(let part=0;part<2;part++)ambient[coordinate][c][part]+=weight*values[i][c][part];
 return ambient;
}
export function inspectNeutralValues(extension,values){
 const ambient=liftNeutralValues(extension,values),boundary={P:packet(),E:packet()};
 for(let c=0;c<5;c++)for(let part=0;part<2;part++){
  const b=fillerEndpointReadout(ambient.slice(112).map(p=>p[c][part]));boundary.P[c][part]=b.P;boundary.E[c][part]=b.E;
 }
 return {boundaryDelta:boundary,activeChannels:values.filter(p=>p.some(z=>z.some(x=>x!==0))).length};
}
