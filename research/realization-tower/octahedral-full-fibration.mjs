import {buildPESymmetricSector} from '../strominger/pe-symmetric-sector.mjs';
const mod4=x=>((x%4)+4)%4;
const phase=q=>q.slice(0,3).map(x=>mod4(x-q[3])).join(',');
const base=c=>[0,1,2,3].map(i=>c.role==='proton'?Math.max(...c.vertices.map(v=>v[i])):Math.min(...c.vertices.map(v=>v[i])));
const key=q=>q.join(',');

// UNVALIDATED EDGE-FIVE MATCHING CANDIDATE, not a completed full fibration.
// The source inventory is geometric; the boundary choices below are not
// selected by global coherence. See five-side-oct-routing-obligations-v1.md.
// Lift Sulfur's coordinate-axis P -> N -> E correspondence without quotienting
// away any of the larger carrier's P/E cells. Native matches take precedence;
// remaining equal-phase lifts are paired in stable coordinate order. Boundary
// transports use the SAME 1-4e_i period lattice as the Sulfur reference.
export function buildOctahedralFullFibration(radius){
 if(![1,2].includes(radius))throw Error('Full fibration currently supports edge units 3 and 5');
 const sector=buildPESymmetricSector(radius),sources=sector.cells.filter(c=>c.role==='proton').sort((a,b)=>a.id.localeCompare(b.id)),targets=sector.cells.filter(c=>c.role==='electron').sort((a,b)=>a.id.localeCompare(b.id));
 const targetAt=new Map(targets.map(c=>[key(base(c)),c])),wires=[];
 for(let axis=0;axis<4;axis++){
  const pending=[],used=new Set();
  const connect=(source,target,expected)=>{
   if(used.has(target.id))throw Error('Target slot reused');used.add(target.id);
   const transport=base(target).map((x,i)=>x-expected[i]);
   if(transport.reduce((a,b)=>a+b,0)!==0||transport.some(x=>mod4(x)!==mod4(transport[3])))throw Error('Not a Sulfur period transport');
   wires.push({id:`oct${sector.edgeUnits}:${source.id}/slot:${axis}`,source:source.id,target:target.id,axis,slot:[axis>>1,axis&1],transport});
  };
  for(const source of sources){const expected=base(source).map((x,i)=>x-1+2*Number(i===axis)),native=targetAt.get(key(expected));if(native)connect(source,native,expected);else pending.push({source,expected});}
  for(const {source,expected} of pending){const target=targets.find(c=>!used.has(c.id)&&phase(base(c))===phase(expected));if(!target)throw Error('Missing target lift for source slot');connect(source,target,expected);}
  if(used.size!==targets.length)throw Error('Incomplete target fibration');
 }
 const fibres=(cells,side)=>cells.map(c=>({id:c.id,cell:c.id,slots:[0,1,2,3].map(axis=>{const matches=wires.filter(w=>w[side]===c.id&&w.axis===axis);if(matches.length!==1)throw Error('Fibre slot is not bijective');return matches[0].id;})}));
 return {sector,wires,sourceFibers:fibres(sources,'source'),targetFibers:fibres(targets,'target'),counts:{sourceFibers:sources.length,targetFibers:targets.length,slotWires:wires.length,geometricNCells:sector.cells.filter(c=>c.role==='neutron').length},scope:'Full retained P/E fibres with four coordinate-axis slots each; no signed-polarity interpretation is inferred from the slot colours.'};
}
