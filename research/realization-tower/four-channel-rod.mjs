// View-only hypothesis: four marked channels, not particle assignments or routes.
import {apex,worldPoint} from './normal-ray-model.mjs';
import {radialConstraints} from './radial-constraints.mjs';
export function fourChannelRod(k,anchor='center'){
 if(!Number.isInteger(k)||k<1||k>7)throw Error('Use k=1..7');
 if(!['center','electron'].includes(anchor))throw Error('Unknown anchor');
 const vertices=[apex,...[1,2,3].map(j=>apex.map((x,i)=>x+(i===0?k:i===j?-k:0)))].map(p=>[...p]);
 const center=apex.map((_,i)=>vertices.reduce((s,p)=>s+p[i]/4,0));
 const reference=worldPoint(anchor==='center'?center:vertices[0]);
 const local=p=>worldPoint(p).map((x,i)=>x-reference[i]);
 const radial=radialConstraints(k,[]);
 return {k,anchor,center,vertices,reference,centerPoint:local(center),vertexPoints:vertices.map(local),centralCell:radial.centralCell,centerCandidates:radial.centerCandidates,
  channels:vertices.map((target,i)=>({id:`fiber-${i+1}`,vertex:i+1,marked:i===0,from:[...center],to:target,points:[local(center),local(target)],status:'schematic-not-a-lattice-path'})),
  centerStatus:k===1?'shared-seed-cell':radial.centralCell===null?'multiple-center-pieces':'unique-center-cell',
  assignments:[],scope:'Proposed four-channel P/E relation. Neither transport maps nor N reconciliation are derived.'};
}
