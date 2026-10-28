import {buildPESymmetricSector,neutralCentre} from './pe-symmetric-sector.mjs';
// Scalar test amplitudes, NOT particle counts, charges, or a derived N field.
export function interiorNPairing(radius=3){
 const s=buildPESymmetricSector(radius),surface=new Set(s.boundary.flatMap(f=>f.owners)),cells=s.cells.filter(c=>c.role==='neutron'&&!surface.has(c.id)),ids=new Set(cells.map(c=>c.id)),dual=new Map(s.dualPairs),seen=new Set(),pairs=[],fixed=[];
 for(const c of [...cells].sort((a,b)=>a.id.localeCompare(b.id))){if(seen.has(c.id))continue;const other=dual.get(c.id);if(!ids.has(other))throw Error('Interior N sector not inversion closed');seen.add(c.id);seen.add(other);if(other===c.id)fixed.push(c.id);else pairs.push([c.id,other]);}
 return {radius,cells,pairs,fixed,scope:'Geometric inversion pairing of interior octahedra. Pair order is a bookkeeping convention, not a physical sign assignment.'};
}
export function decomposeInteriorN(pairing,values){
 for(const c of pairing.cells)if(!Number.isFinite(values[c.id]))throw Error(`Missing finite amplitude for ${c.id}`);
 const pairs=pairing.pairs.map(([a,b])=>({ids:[a,b],common:(values[a]+values[b])/2,contrast:(values[a]-values[b])/2})),fixed=pairing.fixed.map(id=>({id,value:values[id]})),sum=xs=>xs.reduce((a,b)=>a+b,0),pairedNet=2*sum(pairs.map(p=>p.common)),centralNet=sum(fixed.map(p=>p.value));
 return {pairs,fixed,pairedNet,centralNet,total:pairedNet+centralNet,contrastNet:0,originalNorm2:sum(pairing.cells.map(c=>values[c.id]**2)),transformedNorm2:2*sum(pairs.map(p=>p.common**2+p.contrast**2))+sum(fixed.map(p=>p.value**2)),scope:'Invertible mean/contrast coordinates. Cancellation of pair net requires zero common component; no cell or contrast mode is removed.'};
}
export function reconstructInteriorN(decomposition){return Object.fromEntries([...decomposition.pairs.flatMap(p=>[[p.ids[0],p.common+p.contrast],[p.ids[1],p.common-p.contrast]]),...decomposition.fixed.map(p=>[p.id,p.value])]);}
export function probeInteriorNCancellation(radius=3){
 const pairing=interiorNPairing(radius),uniform=Object.fromEntries(pairing.cells.map(c=>[c.id,1])),opposed=Object.fromEntries(pairing.pairs.flatMap(([a,b])=>[[a,1],[b,-1]]));for(const id of pairing.fixed)opposed[id]=1;
 // Linear amplitude along the declared +N/-N port axis (02 versus 13).
 const nAxis=[1,-1,1,-1],axial=Object.fromEntries(pairing.cells.map(c=>[c.id,c.vertices.reduce((sum,p)=>sum+p.reduce((v,x,i)=>v+(x-neutralCentre[i])*nAxis[i],0),0)/c.vertices.length]));
 const report=values=>{const d=decomposeInteriorN(pairing,values);return {pairedNet:d.pairedNet,centralNet:d.centralNet,total:d.total,norm2:d.originalNorm2,activePairs:d.pairs.filter(p=>p.contrast!==0).length,nonzeroCommonPairs:d.pairs.filter(p=>p.common!==0).length};};
 return {radius,interiorNCells:pairing.cells.length,inversionPairs:pairing.pairs.length,fixedCells:pairing.fixed,scalarCommonModes:pairing.pairs.length+pairing.fixed.length,scalarContrastModes:pairing.pairs.length,uniform:report(uniform),opposedWithCentralOne:report(opposed),axialOdd:report(axial),scope:'Trial scalar amplitudes only. Uniform occupancy does not cancel. Opposed amplitudes are imposed test data, not derived N dynamics or a reduction in particle count.'};
}
