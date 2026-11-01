// Route-blind candidate generation. This module imports geometry only.
// Reference routes, their occupied-edge graph, and their selected exit ports
// are deliberately absent. Every surviving candidate is returned; no tie-break.
import {buildPESymmetricSector} from '../strominger/pe-symmetric-sector.mjs';
const key=p=>p.join(',');
const sub=(a,b)=>a.map((x,i)=>x-b[i]);
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const length2=v=>dot(v,v);
const require=(ok,message)=>{if(!ok)throw Error(message);};
const edgeKey=(a,b)=>[key(a),key(b)].sort().join('|');
const det3=g=>g[0][0]*(g[1][1]*g[2][2]-g[1][2]*g[2][1])-g[0][1]*(g[1][0]*g[2][2]-g[1][2]*g[2][0])+g[0][2]*(g[1][0]*g[2][1]-g[1][1]*g[2][0]);
function det4(rows){
 return rows[0].reduce((s,x,i)=>s+(i%2?-1:1)*x*det3(rows.slice(1).map(row=>row.filter((_,j)=>j!==i))),0);
}
export function buildRouteBlindGeometry(radius=1){
 const sector=buildPESymmetricSector(radius),vertices=new Map(),edges=new Map();
 const surfaceEdges=new Set();
 for(const face of sector.boundary)for(let i=0;i<3;i++)for(let j=i+1;j<3;j++)surfaceEdges.add(edgeKey(face.vertices[i],face.vertices[j]));
 for(const cell of sector.cells){
  for(const p of cell.vertices)vertices.set(key(p),p);
  for(let i=0;i<cell.vertices.length;i++)for(let j=i+1;j<cell.vertices.length;j++){
   const a=cell.vertices[i],b=cell.vertices[j];if(length2(sub(a,b))!==2)continue;
   const id=edgeKey(a,b);
   if(!edges.has(id))edges.set(id,{id,points:[a,b],surface:surfaceEdges.has(id),cells:[]});
   edges.get(id).cells.push({id:cell.id,role:cell.role});
  }
 }
 const adjacency=new Map([...vertices.keys()].map(id=>[id,[]]));
 for(const edge of edges.values())for(let i=0;i<2;i++)adjacency.get(key(edge.points[i])).push({point:edge.points[1-i],edge});
 return {radius,centre:sector.centre,vertices,edges,adjacency,audit:{cells:sector.cells.length,vertices:vertices.size,edges:edges.size,boundaryEdges:surfaceEdges.size}};
}
export function departureAngles(query,point){
 const axis=sub(query.head,query.tail),incoming=sub(query.planeWitness,query.tail),outgoing=sub(point,query.head);
 const transverse=v=>v.map((x,i)=>x-axis[i]*dot(v,axis)/length2(axis));
 const u=transverse(incoming),v=transverse(outgoing);
 return {axisCosine:dot(axis,outgoing)/Math.sqrt(length2(axis)*length2(outgoing)),
  transverseCosine:length2(u)*length2(v)>1e-20?dot(u,v)/Math.sqrt(length2(u)*length2(v)):null};
}
// Explicitly bounded calibration family: one signed polarity monomial per
// scalar angle, NOT a lookup table or arbitrary polynomial over strand IDs.
export function fitAngularCompletion(observations){
 const bits=['a','b','p','e'],model={};
 for(const sign of ['+','-']){
  const rows=observations.filter(r=>r.sign===sign);require(rows.length>0,'Missing angular training class');model[sign]={};
  for(const quantity of ['axisCosine','transverseCosine']){
   require(rows.every(r=>Number.isFinite(r[quantity])&&bits.every(b=>['+','-'].includes(r.polarities[b]))),'Invalid angular observation');
   const fits=[];
   for(let mask=0;mask<16;mask++){
    const selected=bits.filter((_,i)=>mask&(1<<i)),feature=r=>selected.reduce((p,b)=>p*(r.polarities[b]==='+'?1:-1),1);
    const coefficient=rows[0][quantity]/feature(rows[0]);
    if(rows.every(r=>Math.abs(r[quantity]-coefficient*feature(r))<1e-10))fits.push({bits:selected,coefficient});
   }
   require(fits.length===1,'Angular calibration is ambiguous or inconsistent');model[sign][quantity]=fits[0];
  }
 }
 return {bySign:model,family:'one polarity monomial per angular quantity; constants included',scope:'calibrated upper-carrier continuation only, not a layer-derived law'};
}
export function predictBlindDepartures(geometry,query,rule,angularModel=null){
 const allowed=['tail','head','previous','planeWitness','polarities','flowAxis'];
 require(Object.keys(query).every(k=>allowed.includes(k)),'Unexpected query field; future routes and ports are forbidden');
 const {tail,head,previous,planeWitness,polarities,flowAxis}=query;
 for(const p of [tail,head,previous,planeWitness])require(Array.isArray(p)&&p.length===4&&p.every(Number.isFinite)&&geometry.vertices.has(key(p)),'Query point outside native geometry');
 for(const p of [head,previous,planeWitness])require(geometry.edges.has(edgeKey(tail,p)),'Input frame must use actual native edges');
 for(const bit of ['a','b','p','e'])require(['+','-'].includes(polarities?.[bit]),'Missing incoming polarity');
 require(Array.isArray(flowAxis)&&flowAxis.length===4&&flowAxis.every(Number.isFinite)&&length2(flowAxis)>0,'Missing declared flow axis');
 const axis=sub(head,tail),oblique=sub(planeWitness,tail),arrival=sub(previous,tail),planeArea=length2(axis)*length2(oblique)-dot(axis,oblique)**2;
 require(planeArea>1e-10,'Incoming plane witness is collinear with the carrier');
 const selector=rule.selectorByA[polarities.a],sign=polarities[selector],desiredClass=rule.outputBySign[sign];
 require(['coplanar','skew'].includes(desiredClass),'Incomplete calibrated rule');
 const inputKind=Math.abs(dot(arrival,axis)/Math.sqrt(length2(arrival)*length2(axis))+1)<1e-10?'straight':'oblique';
 require(inputKind===rule.inputByAgreement[String(sign===polarities.b)],'Incoming state is incompatible with carrier frame');
 const height=dot(sub(head,geometry.centre),flowAxis),radial=sub(head,geometry.centre);
 const candidates=geometry.adjacency.get(key(head)).filter(c=>key(c.point)!==key(tail)).map(({point,edge})=>{
  const departure=sub(point,head),vs=[axis,oblique,departure],gram=vs.map(a=>vs.map(b=>dot(a,b))),determinant=det3(gram);
  const normalized=determinant/vs.reduce((s,v)=>s*length2(v),1),kind=Math.abs(normalized)<1e-10?'coplanar':'skew';
  return {point:[...point],edge:edge.id,kind,surface:edge.surface,...departureAngles(query,point),incidentRoles:[...new Set(edge.cells.map(c=>c.role))],
   heightDelta:dot(departure,flowAxis),radiusSquared:length2(sub(point,geometry.centre)),
   chirality:Math.sign(det4([flowAxis,radial,departure,[1,1,1,1]]))};
 });
 const plane=candidates.filter(c=>c.kind===desiredClass),nonascending=plane.filter(c=>c.heightDelta<=1e-10);
 const equatorial=plane.filter(c=>Math.abs(height)<1e-10&&Math.abs(c.heightDelta)<1e-10);
 const surface=equatorial.filter(c=>c.surface),interior=equatorial.filter(c=>!c.surface);
 const closest=equatorial.length?Math.min(...equatorial.map(c=>c.radiusSquared)):Infinity;
 const profiles={
  'plane only':plane,
  'plane + nonascending flow':nonascending,
  'plane + equatorial phase':equatorial,
  'plane + equatorial phase + surface':surface,
  'plane + equatorial phase + interior':interior,
  'plane + equatorial phase + nearest centre':equatorial.filter(c=>Math.abs(c.radiusSquared-closest)<1e-10),
  'plane + equatorial surface + positive chirality':surface.filter(c=>c.chirality>0),
  'plane + equatorial surface + negative chirality':surface.filter(c=>c.chirality<0)
 };
 let angularPrediction=null;
 if(angularModel){
  require(angularModel.bySign?.[sign],'Missing angular model class');
  angularPrediction=Object.fromEntries(['axisCosine','transverseCosine'].map(quantity=>{
   const term=angularModel.bySign[sign][quantity];
   require(term&&Number.isFinite(term.coefficient)&&Array.isArray(term.bits)&&term.bits.every(b=>['a','b','p','e'].includes(b)),'Invalid angular term');
   return [quantity,term.coefficient*term.bits.reduce((p,b)=>p*(polarities[b]==='+'?1:-1),1)];
  }));
  profiles['plane + fitted angular signature']=plane.filter(c=>Object.entries(angularPrediction).every(([q,value])=>Number.isFinite(c[q])&&Math.abs(c[q]-value)<1e-10));
 }
 return {selector,sign,desiredClass,height,inputKind,candidates,profiles,angularPrediction,
  assumptions:{base:'given carrier, incoming plane witness and polarity state; enumerate all native neighbors except immediate backtracking',
   diagnostics:'Flow, equatorial phase, surface/interior, radial preference and handedness are additional hypotheses, not consequences of the calibrated plane rule.',
   chiralityConvention:'sign det(flowAxis, head-centre, departure, (1,1,1,1)) in the declared native coordinate order'}};
}
