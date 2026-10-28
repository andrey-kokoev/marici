import {buildFoldedFibration,foldedFibrationEnvelope} from './fibration-folded-process.mjs';
import {seed} from './normal-ray-model.mjs';
import {innerLayerHexReflection} from './inner-layer-hex-reflection.mjs';
import {geometricCellLayer} from './cell-fibration-cut.mjs';
import {quartetCellCoherence} from './quartet-cell-coherence.mjs';
export const cellFibrationStages=Object.freeze([
 'Seed the four vertex cells with their original corner colours.',
 'Layer 1: grow three whole tetrahedra from each vertex cell, in their target corner colours.',
 'Layer 2: extend edge branches in their source corner colours; fill between each pair on a face in the opposite corner colour.',
 'Complete layer 1: fill each corner’s adjoining octahedron in its vertex colour.',
 'Inner layer-2 hexagons: copy opposite colours; E or P becomes N.',
 'Surface triangles, including edge positions: read the adjacent layer-2 triangle. P → E, E → P, N → N.',
 'Central cells: complete two N and two non-N cells. Add only N or P.',
 'Fill remaining layer-3 cells with N.',
 'Copy each central quartet to the opposite face.',
 'Copy opposite-face colours into paired interior cells.',
 'Copy further interior cells from matching layer addresses.',
 'Two simplex moves: for each source with one 6 and three 4s, increment every pair of non-source coordinates once and copy the source colour to each destination.',
 'Four-neighbour filler coherence: NEPN → P for unfilled 4466 permutations; preserve two N and introduce no filler E.',
 'Cross the surface/filler boundary: advance the unique coordinate 1 to 2 in each 1666 permutation; copy P/N and convert E to P.',
 'Complete the central 5555 tetrahedron: NPPN → P; preserve two N and introduce no filler E.'
]);
const key=vs=>vs.map(v=>v.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|');
const center=vs=>vs[0].map((_,i)=>vs.reduce((s,v)=>s+v[i]/vs.length,0));
const body=(g,role,layer)=>({id:g.id,kind:g.kind,vertices:g.vertices,faces:g.faces,primitiveIds:g.primitiveIds,components:[],role,layer});
export function buildCellFibration(){
 const model=buildFoldedFibration(),byShape=new Map(model.geometry.map(g=>[key(g.vertices),g]));
 const corners=foldedFibrationEnvelope.map((point,i)=>{
  const matches=model.geometry.filter(g=>g.vertices.some(v=>key([v])===key([point])));
  if(matches.length!==1||matches[0].kind!=='tetrahedron')throw Error('Unique corner tetrahedron required');
  return {vertex:i+1,point,cell:matches[0].id,role:matches[0].role,geometry:matches[0]};
 });
 const translated=(source,targets)=>{
  const delta=source.point.map((x,i)=>targets.reduce((s,c)=>s+(c.point[i]-x)/7,0));
  const g=byShape.get(key(source.geometry.vertices.map(v=>v.map((x,i)=>x+delta[i]))));
  if(!g||g.kind!=='tetrahedron')throw Error('Native tetrahedron required');return g;
 };
 const attachments=(child,parents)=>parents.map(parent=>{
  const shared=child.vertices.filter(v=>parent.vertices.some(w=>key([v])===key([w])));
  if(shared.length!==1)throw Error('Single vertex attachment required');
  return {parent:parent.id,point:shared[0]};
 });
 const seeds=corners.map(c=>body(c.geometry,c.role,0)),growth=[],edgeGrowth=[],faceGrowth=[];
 for(const source of corners)for(const target of corners.filter(c=>c!==source)){
  const child=translated(source,[target]),attachment=attachments(child,[source.geometry])[0].point;
  const first={source:source.vertex,target:target.vertex,parent:source.cell,attachment,body:body(child,target.role,1)};growth.push(first);
  const next=translated(source,[target,target]);
  edgeGrowth.push({source:source.vertex,target:target.vertex,parent:child.id,attachment:attachments(next,[child])[0].point,body:body(next,source.role,2)});
 }
 for(const source of corners){
  const others=corners.filter(c=>c!==source);
  for(let i=0;i<others.length;i++)for(let j=i+1;j<others.length;j++){
   const a=others[i],b=others[j],opposite=others.find(c=>c!==a&&c!==b),child=translated(source,[a,b]);
   const parents=[a,b].map(t=>edgeGrowth.find(g=>g.source===source.vertex&&g.target===t.vertex).body);
   faceGrowth.push({source:source.vertex,face:[source.vertex,a.vertex,b.vertex].sort(),opposite:opposite.vertex,attachments:attachments(child,parents),kind:'face',body:body(child,opposite.role,2)});
  }
 }
 const complementaryGrowth=corners.map(source=>{
  const seedFaces=new Set(source.geometry.faces.map(key));
  const octs=model.geometry.filter(g=>g.kind==='octahedron'&&g.faces.some(f=>seedFaces.has(key(f))));
  if(octs.length!==1)throw Error('Unique adjoining octahedron required');
  const oct=octs[0];
  return {source:source.vertex,kind:'complementary',complementaryLayer:1,parent:source.cell,sharedFace:oct.faces.find(f=>seedFaces.has(key(f))),body:body(oct,source.role,3)};
 });
 const previous=[...seeds,...[...growth,...edgeGrowth,...faceGrowth,...complementaryGrowth].map(g=>g.body)];
 if(previous.length!==44||new Set(previous.map(g=>g.id)).size!==44)throw Error('Layer-1/2 additions collide');
 const reflection=innerLayerHexReflection(model.geometry,previous,corners);
 const hexReflectionGrowth=reflection.agreed.map(({cell,...g})=>({...g,kind:'inner-hex-reflection',complementaryLayer:2,body:{...body(cell,g.role,4),reflection:g.hexWitnesses[0]}}));
 if(new Set([...previous,...hexReflectionGrowth.map(g=>g.body)].map(g=>g.id)).size!==56)throw Error('Twelve distinct layer-2 octahedra required');
 const occupied=new Set([...previous,...hexReflectionGrowth.map(g=>g.body)].map(g=>g.id)),faceMiddleGrowth=[];
 const swap={proton:'electron',electron:'proton',neutron:'neutron'};
 const carrierFaces=corners.map(opposite=>{
  const cs=corners.filter(c=>c!==opposite);
  const axis=cs[0].point.findIndex((x,i)=>cs.every(c=>c.point[i]===x)&&opposite.point[i]!==x);
  return {face:cs.map(c=>c.vertex),axis,plane:cs[0].point[axis]};
 });
 for(const source of corners){
  const parents=previous.filter(g=>g.kind==='tetrahedron'&&geometricCellLayer(g,source.vertex)===2);
  for(const child of model.geometry.filter(g=>g.kind==='octahedron'&&!occupied.has(g.id)&&geometricCellLayer(g,source.vertex)===3)){
   const witnesses=[];
   for(const {face,axis,plane} of carrierFaces){
    const onFace=f=>f.every(v=>v[axis]===plane),surfaceFace=child.faces.find(onFace);
    if(!surfaceFace)continue;
    const matches=parents.flatMap(parent=>parent.faces.filter(onFace).map(sourceFace=>({parent,sourceFace,sharedEdge:surfaceFace.filter(v=>sourceFace.some(w=>key([v])===key([w])))}))).filter(w=>w.sharedEdge.length===2);
    if(matches.length!==1)throw Error('Unique adjacent layer-2 triangle required on each exposed face');
    const {parent,sourceFace,sharedEdge}=matches[0];
    witnesses.push({face,parent:parent.id,sourceRole:parent.role,sourceFace,surfaceFace,sharedEdge});
   }
   if(!witnesses.length)continue;
   if(new Set(witnesses.map(w=>w.parent)).size!==1)throw Error('Exposed faces must read the same layer-2 cell');
   const first=witnesses[0],faces=witnesses.map(w=>w.face),role=swap[first.sourceRole];
   const edgeSource={cell:first.parent,role:first.sourceRole,assignedRole:role,face:first.face,faces,source:source.vertex};
   faceMiddleGrowth.push({...first,kind:'face-middle',position:witnesses.length===1?'face-middle':'edge-adjacent',source:source.vertex,faces,witnesses,body:{...body(child,role,5),edgeSource}});
  }
 }
 if(faceMiddleGrowth.length!==24||new Set([...occupied,...faceMiddleGrowth.map(g=>g.body.id)]).size!==80)throw Error('Twenty-four distinct surface octahedra required');
 const beforeCentres=[...previous,...hexReflectionGrowth.map(g=>g.body),...faceMiddleGrowth.map(g=>g.body)],centreIds=new Set(beforeCentres.map(g=>g.id)),centralQuartetGrowth=[];
 for(const source of corners){
  const others=corners.filter(c=>c!==source),axis=source.point.findIndex((x,i)=>others.every(c=>c.point[i]!==x));
  const candidates=model.geometry.filter(g=>{
   if(g.kind!=='tetrahedron'||centreIds.has(g.id)||geometricCellLayer(g,source.vertex)!==3)return false;
   const transverse=center(g.vertices).filter((_,i)=>i!==axis);
   return transverse.every(x=>x===transverse[0]);
  });
  if(candidates.length!==1)throw Error('Unique central layer-3 tetrahedron required');
  const child=candidates[0],faces=new Set(child.faces.map(key));
  const neighbors=beforeCentres.flatMap(g=>{const sharedFace=g.faces.find(f=>faces.has(key(f)));return sharedFace?[{cell:g.id,role:g.role,sharedFace}]:[];});
  const result=quartetCellCoherence(neighbors.map(n=>n.role)),coherence={...result,neighbors};
  centralQuartetGrowth.push({kind:'central-quartet',source:source.vertex,...coherence,body:{...body(child,result.role,6),coherence}});
 }
 if(new Set([...centreIds,...centralQuartetGrowth.map(g=>g.body.id)]).size!==84)throw Error('Four distinct central cells required');
 const beforeFillIds=new Set([...centreIds,...centralQuartetGrowth.map(g=>g.body.id)]);
 const layer3Fill=model.geometry.filter(g=>!beforeFillIds.has(g.id)).flatMap(g=>{
  const sources=corners.filter(c=>geometricCellLayer(g,c.vertex)===3).map(c=>c.vertex);
  return sources.length?[{kind:'layer-3-fill',sources,body:body(g,'neutron',7)}]:[];
 });
 if(layer3Fill.length!==42||new Set([...beforeFillIds,...layer3Fill.map(g=>g.body.id)]).size!==126)throw Error('Forty-two distinct layer-3 gaps required');
 const beforeCopies=[...beforeCentres,...centralQuartetGrowth.map(g=>g.body),...layer3Fill.map(g=>g.body)],copySources=new Map(beforeCopies.map(g=>[g.id,g])),oppositeQuartetGrowth=[];
 for(const quartet of centralQuartetGrowth){
  const source=corners.find(c=>c.vertex===quartet.source),others=corners.filter(c=>c!==source),face=others.map(c=>c.vertex);
  const axis=source.point.findIndex((x,i)=>others.every(c=>c.point[i]!==x)),plane=others[0].point[axis];
  const distance=plane-Math.max(...quartet.body.vertices.map(v=>v[axis]));
  const delta=source.point.map((_,i)=>i===axis?distance:-distance/3);
  const members=[quartet.body,...quartet.neighbors.map(n=>copySources.get(n.cell))];
  for(const original of members){
   const child=byShape.get(key(original.vertices.map(v=>v.map((x,i)=>x+delta[i]))));
   if(!child||child.kind!==original.kind||copySources.has(child.id)||!child.faces.some(f=>f.every(v=>v[axis]===plane)))throw Error('Empty translated cell on the opposite face required');
   const translation={cell:original.id,source:source.vertex,face,delta};
   oppositeQuartetGrowth.push({kind:'opposite-quartet',source:source.vertex,face,parent:original.id,delta,body:{...body(child,original.role,8),translation}});
  }
 }
 if(oppositeQuartetGrowth.length!==16||new Set([...copySources.keys(),...oppositeQuartetGrowth.map(g=>g.body.id)]).size!==142)throw Error('Sixteen distinct translated cells required');
 const beforePairs=new Map([...beforeCopies,...oppositeQuartetGrowth.map(g=>g.body)].map(g=>[g.id,g]));
 const byLayers=new Map(model.geometry.map(g=>[[1,2,3,4].map(v=>geometricCellLayer(g,v)).join(''),g]));
 if(byLayers.size!==model.geometry.length)throw Error('Unique layer addresses required');
 const pairPlans=[['6444',['5554','4554']],['4644',['5545','5445']],['4464',['5455','5445']],['4446',['4555','4554']]],pairTargets=new Map();
 for(const [from,targets] of pairPlans){
  const source=beforePairs.get(byLayers.get(from)?.id);
  if(!source?.role)throw Error('Assigned opposite-face source required');
  for(const address of targets){
   const child=byLayers.get(address);
   if(!child||beforePairs.has(child.id))throw Error('Empty interior copy target required');
   if(!pairTargets.has(child.id))pairTargets.set(child.id,{child,layers:[...address].map(Number),parents:[]});
   pairTargets.get(child.id).parents.push({cell:source.id,role:source.role,layers:[...from].map(Number)});
  }
 }
 const interiorPairGrowth=[...pairTargets.values()].map(({child,layers,parents})=>{
  if(new Set(parents.map(p=>p.role)).size!==1)throw Error('Shared interior copy sources disagree');
  const role=parents[0].role;
  return {kind:'interior-pair',layers,parents,body:{...body(child,role,9),interiorCopy:{layers,sources:parents}}};
 });
 if(interiorPairGrowth.length!==6||new Set([...beforePairs.keys(),...interiorPairGrowth.map(g=>g.body.id)]).size!==148)throw Error('Six distinct interior copies required');
 const furtherInteriorGrowth=[];
 for(const [target,source,roleOverride] of [['4455','2466',null],['5454','6462',null],['4545','2646',null],['5544','6642',null]]){
  const child=byLayers.get(target),parent=beforePairs.get(byLayers.get(source)?.id);
  if(!child||beforePairs.has(child.id)||!parent?.role)throw Error('Unassigned further interior target or source required');
  furtherInteriorGrowth.push({kind:'interior-pair',layers:[...target].map(Number),parents:[{cell:parent.id,role:parent.role,layers:[...source].map(Number)}],body:{...body(child,roleOverride??parent.role,10),interiorCopy:{layers:[...target].map(Number),sources:[{cell:parent.id,role:parent.role,layers:[...source].map(Number)}],rule:roleOverride?'P exception':undefined}}});
 }
 const placedBeforeMoves=new Map([...beforePairs.values(),...interiorPairGrowth.map(g=>g.body),...furtherInteriorGrowth.map(g=>g.body)].map(b=>[b.id,b]));
 const pairedDirectionGrowth=[1,2,3,4].flatMap(vertex=>[1,2,3,4].filter(v=>v!==vertex).map(partner=>{
  const sourceLayers=[1,2,3,4].map(v=>v===vertex?6:4);
  const directions=[1,2,3,4].filter(v=>v!==vertex&&v!==partner);
  const layers=sourceLayers.map((value,i)=>value+(directions.includes(i+1)?1:0));
  const parent=placedBeforeMoves.get(byLayers.get(sourceLayers.join(''))?.id),child=byLayers.get(layers.join(''));
  if(!parent?.role||!child||placedBeforeMoves.has(child.id))throw Error('Assigned source and empty two-direction target required');
  const source={cell:parent.id,role:parent.role,layers:sourceLayers};
  return {kind:'interior-pair',vertex,partner,directions,layers,parents:[source],body:{...body(child,parent.role,11),interiorCopy:{layers,sources:[source],directions,fixedVertices:[vertex,partner],rule:'Increment each of the two chosen non-source coordinates once; copy source colour (destination only).'}}};
 }));
 const placedBeforeCoherence=new Map([...placedBeforeMoves,...pairedDirectionGrowth.map(g=>[g.body.id,g.body])]);
 const fillerCoherenceGrowth=model.geometry.flatMap(child=>{
  const layers=[1,2,3,4].map(v=>geometricCellLayer(child,v));
  if(child.kind!=='tetrahedron'||placedBeforeCoherence.has(child.id)||[...layers].sort().join('')!=='4466')return [];
  const neighbors=layers.map((_,axis)=>{
   const address=[...layers];address[axis]--;
   const neighbor=placedBeforeCoherence.get(byLayers.get(address.join(''))?.id);
   if(!neighbor)throw Error('Assigned four-neighbour coherence witness required');
   if(!child.faces.some(f=>neighbor.faces.some(g=>key(f)===key(g))))throw Error('Coherence witness must share a facet');
   return {vertex:axis+1,cell:neighbor.id,role:neighbor.role,layers:address};
  });
  const word=neighbors.map(n=>({neutron:'N',electron:'E',proton:'P'})[n.role]).join('');
  if(word!=='NEPN')throw Error(`Unexpected filler coherence word: ${word}`);
  const coherence={word,pattern:'NEPN → P',role:'proton',neighbors,rule:'Preserve exactly two N; no new E in filler.'};
  return [{kind:'filler-coherence',layers,...coherence,body:{...body(child,'proton',12),coherence}}];
 });
 const placedBeforeBoundary=new Map([...placedBeforeCoherence,...fillerCoherenceGrowth.map(g=>[g.body.id,g.body])]);
 const boundaryGrowth=[1,2,3,4].map(vertex=>{
  const sourceLayers=[1,2,3,4].map(v=>v===vertex?1:6),layers=sourceLayers.map((n,i)=>i===vertex-1?n+1:n);
  const parent=placedBeforeBoundary.get(byLayers.get(sourceLayers.join(''))?.id),child=byLayers.get(layers.join(''));
  if(!parent?.role||!child||placedBeforeBoundary.has(child.id))throw Error('Assigned boundary source and empty filler target required');
  if(!child.faces.some(f=>parent.faces.some(g=>key(f)===key(g))))throw Error('Boundary crossing must share a facet');
  const role=parent.role==='electron'?'proton':parent.role,source={cell:parent.id,role:parent.role,layers:sourceLayers};
  return {kind:'interior-pair',vertex,layers,parents:[source],body:{...body(child,role,13),interiorCopy:{layers,sources:[source],rule:'Surface → filler: P → P, N → N, E → P.',boundaryCrossing:true}}};
 });
 const placedBeforeCentre=new Map([...placedBeforeBoundary,...boundaryGrowth.map(g=>[g.body.id,g.body])]);
 const centralCell=byLayers.get('5555');
 if(!centralCell||centralCell.kind!=='tetrahedron'||placedBeforeCentre.has(centralCell.id))throw Error('Empty central tetrahedron required');
 const centralNeighbors=[1,2,3,4].map(vertex=>{
  const layers=[5,5,5,5];layers[vertex-1]--;
  const neighbor=placedBeforeCentre.get(byLayers.get(layers.join(''))?.id);
  if(!neighbor||!centralCell.faces.some(f=>neighbor.faces.some(g=>key(f)===key(g))))throw Error('Assigned central face-neighbour required');
  return {vertex,cell:neighbor.id,role:neighbor.role,layers};
 });
 const centralWord=centralNeighbors.map(n=>({neutron:'N',proton:'P',electron:'E'})[n.role]).join('');
 if(centralWord!=='NPPN')throw Error(`Unexpected central coherence word: ${centralWord}`);
 const centralCoherence={word:centralWord,pattern:'NPPN → P',role:'proton',neighbors:centralNeighbors,rule:'Preserve exactly two N; no new E in filler.'};
 const centralGrowth=[{kind:'filler-coherence',layers:[5,5,5,5],...centralCoherence,body:{...body(centralCell,'proton',14),coherence:centralCoherence}}];
 return {geometry:model.geometry,corners:corners.map(({geometry,...c})=>c),seeds,growth,edgeGrowth,faceGrowth,complementaryGrowth,hexReflectionGrowth,faceMiddleGrowth,centralQuartetGrowth,layer3Fill,oppositeQuartetGrowth,interiorPairGrowth,furtherInteriorGrowth,pairedDirectionGrowth,fillerCoherenceGrowth,boundaryGrowth,centralGrowth,hexReflectionConflicts:[],envelope:foldedFibrationEnvelope};
}
const construction=buildCellFibration();
export function cellFibrationProcess(k,step){
 if(!Number.isInteger(k)||k<1||k>7||!Number.isInteger(step)||step<0||step>=cellFibrationStages.length)throw Error('Invalid cell fibration step');
 const growth=[...(step>=1?construction.growth:[]),...(step>=2?[...construction.edgeGrowth,...construction.faceGrowth]:[]),...(step>=3?construction.complementaryGrowth:[]),...(step>=4?construction.hexReflectionGrowth:[]),...(step>=5?construction.faceMiddleGrowth:[]),...(step>=6?construction.centralQuartetGrowth:[]),...(step>=7?construction.layer3Fill:[]),...(step>=8?construction.oppositeQuartetGrowth:[]),...(step>=9?construction.interiorPairGrowth:[]),...(step>=10?construction.furtherInteriorGrowth:[]),...(step>=11?construction.pairedDirectionGrowth:[]),...(step>=12?construction.fillerCoherenceGrowth:[]),...(step>=13?construction.boundaryGrowth:[]),...(step>=14?construction.centralGrowth:[])];
 const retainedBodies=[...construction.seeds,...growth.map(g=>g.body)];
 const zero=()=>({proton:0,neutron:0,electron:0,total:0}),counts={surface:zero(),filler:zero(),total:zero()};
 const planes=[0,1,2,3].map(axis=>foldedFibrationEnvelope.map(p=>p[axis]).find(value=>foldedFibrationEnvelope.filter(p=>p[axis]===value).length===3));
 for(const b of retainedBodies){
  const surface=b.faces.some(f=>planes.some((value,axis)=>f.every(p=>p[axis]===value))),row=counts[surface?'surface':'filler'];
  row[b.role]++;row.total++;counts.total[b.role]++;counts.total.total++;
 }
 const placed=new Set(retainedBodies.map(g=>g.id));
 const emptyBodies=construction.geometry.filter(g=>!placed.has(g.id)).map(g=>({...g,role:null,layer:null,unfilled:true}));
 return {k:7,step,end:seed,assignments:[],retainedBodies,emptyBodies,conflictBodies:[],
  presentationLabels:retainedBodies.map(b=>({cell:b.id,role:b.role,point:center(b.vertices)})),
  presentationAudit:{nativeGeometry:true,nativeParticleRealization:false,wholeCellColour:true},
  cellFibrationAudit:{layer:step,unresolvedOctahedra:[],complementaryLayer:step>=3?Math.min(2,step-2):0,corners:construction.corners,growth:growth.map(({body,...g})=>({...g,child:body.id,role:body.role,layer:body.layer})),counts,bodyCount:retainedBodies.length,vertexAttachment:true,faceSubdivision:false,envelope:construction.envelope},
  interfaceGuides:[],firstRay:null,rays:[],faceNeighbors:[],faceVertexComparisons:[],neutronNeighbors:[],surfaceNeutronNeighbors:[],closureRounds:[],nextClosure:[],diamonds:[],conflicts:[],
  summary:`${cellFibrationStages[step]} ${retainedBodies.length} whole cells.`,
  history:cellFibrationStages.slice(0,step+1).map((rule,index)=>({layer:index,rule})),canAdvance:step<cellFibrationStages.length-1};
}
