import {buildPESymmetricSector} from './pe-symmetric-sector.mjs';
import {buildNEdgeTubes} from './n-edge-tubes.mjs';
const signature=ids=>{const a=ids.join('|'),b=[...ids].reverse().join('|');return a<b?a:b;};
export function compareRouteTraces(reference,actual){
 const ref=new Set(reference.map(p=>signature(p.passIds))),now=new Set(actual.map(p=>signature(p.passIds)));
 if(ref.size!==reference.length||now.size!==actual.length)throw Error('Duplicate channel traces cannot be silently identified');
 return {unchanged:actual.filter(p=>ref.has(signature(p.passIds))).length,addedOrChanged:actual.filter(p=>!ref.has(signature(p.passIds))).length,removedOrChanged:reference.filter(p=>!now.has(signature(p.passIds))).length};
}
export function auditAmbientNeutralRouting(radius=3,extraShell=1){
 if(!Number.isInteger(radius)||radius<0||radius>3||![1,2].includes(extraShell))throw Error('Audit radius 0..3 and one or two ambient shells required');
 const structure=buildPESymmetricSector(radius),actual=buildNEdgeTubes(structure),ambient=buildPESymmetricSector(radius+extraShell);
 // Reference has the same carrier lattice and outer boundary, but no occupied
 // P/E cells. Its N routing is unchanged by construction; test that fact rather
 // than interpreting all available carrier paths as object-owned particles.
 const reference=buildNEdgeTubes({...ambient,cells:ambient.cells.filter(c=>c.role==='neutron')}),inside=new Set(actual.passes.map(p=>p.id)),restricted=[];let bothEndsExtend=0;
 for(const path of reference.paths){const indices=path.passIds.flatMap((id,i)=>inside.has(id)?[i]:[]);if(!indices.length)continue;const first=indices[0],last=indices.at(-1);if(indices.length!==last-first+1)throw Error('Reference route re-enters the observation window');restricted.push({passIds:path.passIds.slice(first,last+1)});if(first>0&&last<path.passIds.length-1)bothEndsExtend++;}
 const comparison=compareRouteTraces(restricted,actual.paths),covered=new Set(restricted.flatMap(p=>p.passIds));if(covered.size!==inside.size||[...inside].some(id=>!covered.has(id)))throw Error('Ambient comparison omitted local strands');
 const actualSignatures=new Set(actual.paths.map(p=>signature(p.passIds))),ambientMatchedPathIds=actual.paths.filter(p=>restricted.some(r=>signature(r.passIds)===signature(p.passIds))).map(p=>p.id);
 return {radius,extraShell,occupiedPECells:structure.cells.filter(c=>c.role!=='neutron').length,referenceOccupiedPECells:0,localChannels:actualSignatures.size,ambientWindowChannels:restricted.length,ambientMatchedChannels:comparison.unchanged,addedOrChangedChannels:comparison.addedOrChanged,removedOrChangedChannels:comparison.removedOrChanged,channelsExtendingAtBothEnds:bothEndsExtend,localPassesCompared:inside.size,closedPaths:actual.audit.closedPaths,peCouplingDefined:false,localizedNeutronCount:null,ambientMatchedPathIds,scope:'Matched-window comparison to a larger neutral carrier lattice with P/E occupancy absent. Current opposite-edge routing ignores P/E, so identity response is expected. No detected routing response is NOT a physical zero-neutron claim.'};
}
