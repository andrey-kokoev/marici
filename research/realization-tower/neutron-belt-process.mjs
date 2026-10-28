import geometry from '../voevodsky/results/four_six_center_cones.json' with {type:'json'};
import flux from '../voevodsky/results/mode_flux_charge.json' with {type:'json'};
import {seed} from './normal-ray-model.mjs';
const rational=s=>{const [a,b='1']=s.split('/');return Number(a)/Number(b);};
// Isometric coordinate adapter only: old physical XYZ -> viewer sum-one chart.
export function beltViewerPoint([x,y,z]){
 x+=3/7;y+=Math.sqrt(3)/7;z+=Math.sqrt(6)/14;
 const q3=z/(2*Math.sqrt(6)/7),q2=(y-q3*Math.sqrt(3)/7)/(3*Math.sqrt(3)/7),q1=(x-(q2+q3)*3/7)/(6/7);
 return [1-q1-q2-q3,q1,q2,q3];
}
const physical=Object.fromEntries(Object.entries(geometry.belt_scaled_coordinates).map(([id,p])=>{const [x,y,z]=p.map(rational);return [id,[Math.sqrt(3)*x,y,z]];}));
const points=Object.fromEntries(Object.entries(physical).map(([id,p])=>[id,beltViewerPoint(p)]));
export const neutronBeltEnvelope=Object.entries(points).filter(([id])=>id!=='O').map(([,p])=>p);
const centroid=ps=>ps[0].map((_,i)=>ps.reduce((s,p)=>s+p[i]/ps.length,0));
export function neutronBeltProcess(k,step){
 if(k!==7||step!==0)throw Error('Invalid neutron belt inspection state');
 const retainedBodies=geometry.belt_tetrahedra.map((names,i)=>{
  const sign=flux.belt_face_signs[i],sector=flux.sector_pairs.findIndex(pair=>pair.includes(i))+1;
  const vertices=names.map(n=>points[n]);
  return {id:`belt:${i}`,kind:'tetrahedron',vertices,faces:vertices.map((_,j)=>vertices.filter((_,n)=>j!==n)),components:[],role:null,layer:0,color:sign>0?0x42bfb3:0xb785e8,opacity:.35,
   internalSector:{face:i,sector,circulation:sign,vertices:names,scope:'Circulation sign, not a P/E cell assignment.'}};
 });
 const interfaceGuides=geometry.belt_faces.flatMap((face,i)=>{
  const cycle=flux.belt_face_signs[i]>0?face:[...face].reverse(),center=centroid(face.map(n=>points[n]));
  const inset=cycle.map(n=>points[n].map((x,j)=>center[j]+.65*(x-center[j])));
  return inset.map((p,j)=>({points:[p,inset[(j+1)%3]],color:flux.belt_face_signs[i]>0?0x42bfb3:0xb785e8}));
 });
 return {k:7,step,end:seed,assignments:[],firstRay:null,rays:[],faceNeighbors:[],faceVertexComparisons:[],neutronNeighbors:[],surfaceNeutronNeighbors:[],closureRounds:[],nextClosure:[],diamonds:[],conflicts:[],
 retainedBodies,emptyBodies:[],conflictBodies:[],presentationLabels:retainedBodies.map(b=>({cell:b.id,text:`${b.internalSector.sector}${b.internalSector.circulation>0?'+':'−'}`,color:b.color,point:centroid(b.vertices)})),interfaceGuides,
 presentationAudit:{geometryOnly:true,particleAssignments:false},
 neutronBeltAudit:{pieces:6,sectors:flux.sector_pairs,signs:flux.belt_face_signs,excludedCaps:geometry.missing_cap_tetrahedra,centerLink:geometry.topology.belt_center_link.rational_betti,transfers:flux.new_intrinsic_operator_support,flux:flux.results.paired_opposite_branch_belt,source:'research/voevodsky/results/four_six_center_cones.json',branchSource:'research/voevodsky/results/mode_flux_charge.json'},
 summary:'Six-cone annular carrier; three opposite-circulation pairs. Inspection only, not attached to a parent N.',history:[],canAdvance:false};
}
