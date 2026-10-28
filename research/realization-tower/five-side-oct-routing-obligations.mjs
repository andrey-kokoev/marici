import {buildPESymmetricSector} from '../strominger/pe-symmetric-sector.mjs';
const key=vs=>vs.map(String).sort().join('|');
const sorted=xs=>[...xs].sort((a,b)=>a.id.localeCompare(b.id));
const centre=vs=>[0,1,2,3].map(i=>vs.reduce((s,p)=>s+p[i]/vs.length,0));
const axisOf=face=>{const axes=[0,1,2,3].filter(i=>face.every(p=>p[i]===face[0][i]));if(axes.length!==1)throw Error('Not a native triangular face');return axes[0];};

// Obligation-site enumeration only. Deliberately imports no routing candidate,
// modulo-four phase assignment, endpoint matching, or renderer.
export function buildFiveSideOctRoutingObligations(sector=buildPESymmetricSector(2)){
 const cells=sorted(sector.cells),faces=sorted(sector.faces),ports=[],portAt=new Map(),edges=new Map(),oppositeFaceSites=[];
 for(const c of cells)for(const f of c.faces){
  const face=key(f),port={id:`${c.id}@${face}`,cell:c.id,role:c.role,face,axis:axisOf(f)};
  ports.push(port);portAt.set(`${c.id}@${face}`,port);
 }
 for(const f of faces)for(let i=0;i<3;i++)for(let j=i+1;j<3;j++){
  const id=key([f.vertices[i],f.vertices[j]]);
  if(!edges.has(id))edges.set(id,{id,vertices:[f.vertices[i],f.vertices[j]].sort((a,b)=>String(a).localeCompare(String(b))),faces:[],cells:[]});
  const e=edges.get(id);e.faces.push(f.id);e.cells.push(...f.owners);
 }
 for(const e of edges.values()){e.faces=[...new Set(e.faces)].sort();e.cells=[...new Set(e.cells)].sort();}
 for(const c of cells.filter(c=>c.role==='neutron'))for(let axis=0;axis<4;axis++){
  const fs=c.faces.filter(f=>axisOf(f)===axis).sort((a,b)=>a[0][axis]-b[0][axis]);
  if(fs.length!==2)throw Error('Missing opposite N faces');
  oppositeFaceSites.push({id:`${c.id}/opposition:${axis}`,cell:c.id,axis,ports:fs.map(f=>portAt.get(`${c.id}@${key(f)}`).id),status:'geometric-opposition-only',channelWitness:null});
 }
 const interfaces=faces.filter(f=>f.owners.length===2).map(f=>({id:f.id,ports:[...f.owners].sort().map(c=>portAt.get(`${c}@${f.id}`).id),requirement:'shared-interface-compatibility',witness:null}));
 const boundaries=faces.filter(f=>f.owners.length===1).map(f=>({id:f.id,port:portAt.get(`${f.owners[0]}@${f.id}`).id,requirement:'admitted-boundary',continuation:null,witness:null}));
 if(faces.some(f=>![1,2].includes(f.owners.length)))throw Error('Nonmanifold carrier');
 const adjacency=new Map(cells.map(c=>[c.id,new Set()]));
 for(const f of faces)if(f.owners.length===2){adjacency.get(f.owners[0]).add(f.owners[1]);adjacency.get(f.owners[1]).add(f.owners[0]);}
 const readings=[],axes=[[1,1,-1,-1],[1,-1,1,-1],[1,-1,-1,1]];
 for(let axisIndex=0;axisIndex<3;axisIndex++)for(const sign of [-1,1]){
  const axis=axes[axisIndex],height=c=>sign*axis.reduce((s,x,i)=>s+x*(centre(c.vertices)[i]-sector.centre[i]),0)/2;
  const top=Math.max(...cells.map(height)),layers=new Map();
  for(const c of cells){const layer=Math.round(2*(top-height(c)))+1;if(!layers.has(layer))layers.set(layer,[]);layers.get(layer).push(c);}
  const layer=n=>layers.get(n)??[],l2=new Set(layer(2).map(c=>c.id)),l3=new Set(layer(3).map(c=>c.id));
  const contexts=layer(3).map(c=>{
   const references=layer(2).filter(r=>adjacency.get(c.id).has(r.id));
   if(references.length!==2||new Set(references.map(r=>r.role)).size!==2)throw Error('Layer-3 signed-context incidence differs from source specification');
   return {channelOccurrence:c.id,P:references.find(r=>r.role==='proton').id,E:references.find(r=>r.role==='electron').id,signBinding:null};
  });
  const comparisons=[],outer=[];
  for(const c of layer(4)){
   const inputs=[...adjacency.get(c.id)].filter(id=>l3.has(id)).sort();
   if(inputs.length===1){outer.push({cell:c.id,input:inputs[0]});continue;}
   if(inputs.length!==2)throw Error('Unexpected entry comparison incidence');
   const shared=[...adjacency.get(inputs[0])].filter(id=>l2.has(id)&&adjacency.get(inputs[1]).has(id));
   if(shared.length!==1)throw Error('Comparison has no unique shared entry reference');
   const operands=inputs.map(id=>contexts.find(c=>c.channelOccurrence===id));
   const compare=c.role==='proton'?'P':'E',reference=compare==='P'?'E':'P';
   if(operands[0][reference]!==shared[0]||operands[1][reference]!==shared[0]||operands[0][compare]===operands[1][compare])throw Error('Invalid shared-reference operands');
   comparisons.push({id:`reading:${axisIndex}:${sign}/comparison:${c.id}`,cell:c.id,kind:`compare-${compare}-at-shared-${reference}`,inputs,operands,sharedReference:shared[0],source:'sulfur-spec#Layer-4 recombination locations',status:'required-prefix-incidence; comparison-map-unbound',comparisonWitness:null,outputPairing:null});
  }
  if(layer(1).length!==1||layer(2).length!==4||contexts.length!==4||comparisons.length!==4||outer.length!==8)throw Error('Entry prefix does not match specified incidence');
  readings.push({id:`reading:${axisIndex}:${sign}`,axis,sign,incomingN:layer(1)[0].id,scope:'alternative reading of one retained carrier; not another independent input bundle',layerProfile:[...layers].sort((a,b)=>a[0]-b[0]).map(([layer,cs])=>({layer,P:cs.filter(c=>c.role==='proton').length,N:cs.filter(c=>c.role==='neutron').length,E:cs.filter(c=>c.role==='electron').length})),contexts,comparisons,outer});
 }
 return {schema:'five-side-oct.routing-obligation-sites.v1',status:'unresolved-obligations-not-a-routing',constructionAdmitted:false,edgeUnits:sector.edgeUnits,
  inventory:{cells:cells.length,P:cells.filter(c=>c.role==='proton').length,N:cells.filter(c=>c.role==='neutron').length,E:cells.filter(c=>c.role==='electron').length,faceOccurrences:ports.length,nativeFaces:faces.length,nativeEdges:edges.size,sharedInterfaces:interfaces.length,boundaryOccurrences:boundaries.length,oppositeFaceSites:oppositeFaceSites.length},
  cellIds:cells.map(c=>c.id),chargedFibreSites:{P:cells.filter(c=>c.role==='proton').map(c=>c.id),E:cells.filter(c=>c.role==='electron').map(c=>c.id)},ports:sorted(ports),interfaces,boundaries,edges:sorted(edges.values()),oppositeFaceSites:sorted(oppositeFaceSites),readings,
  unresolved:{wholeDepthComparisonComplex:'not instantiated: a licensed whole-depth binding is required',signedPortBinding:'not supplied by geometric axis labels',boundaryLaw:'not supplied by radius-one periodic closure',nativeRealization:'no paths assigned',groupCount:'not selected',interpretationOf320:'320 P face ports and 320 E face ports are geometric counts, not by themselves a signed-payload identification'},
  selectedEndpointMatches:[],selectedGroups:[],selectedRoutes:[]};
}
