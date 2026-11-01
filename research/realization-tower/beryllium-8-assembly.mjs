const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const sub=(a,b)=>a.map((x,i)=>x-b[i]);
const unit=v=>{const length=Math.hypot(...v);return v.map(x=>x/length);};
// Isometric embedding of the sum-constant 4D carrier into three dimensions.
// Only the rendering lanes leave the exact native edges; they taper back to
// their native endpoints. Route identity and connectivity are never changed.
export function buildBeryllium8Assembly(columns,reference){
 if(columns.length!==8||new Set(columns.map(s=>s.id)).size!==8||columns.some(s=>!s.id.startsWith('be8:wire:')))throw Error('Expected eight retained Be-8 routes');
 const centre=reference.envelope[0].map((_,i)=>reference.envelope.reduce((n,p)=>n+p[i],0)/reference.envelope.length);
 const basis=[[.5,-.5,.5,-.5],reference.axis,[.5,-.5,-.5,.5]],project=p=>basis.map(v=>dot(sub(p,centre),v));
 const sleeve=reference.sleeve?{...reference.sleeve,point:project(reference.sleeve.point)}:null;
 const vertices=reference.envelope.map(project);if(sleeve)vertices.push(sleeve.point);
 const isCentre=p=>sleeve&&Math.hypot(...sub(p,sleeve.point))<1e-9,edges=new Map();
 for(const s of columns)for(let i=0;i<s.edgeIds.length;i++){
  const id=s.edgeIds[i];if(!edges.has(id))edges.set(id,{id,guide:[project(s.guide[i]),project(s.guide[i+1])],...(sleeve?{sleeveLink:[s.guide[i],s.guide[i+1]].some(p=>isCentre(project(p)))}:{}),strandIds:[]});
  edges.get(id).strandIds.push(s.id);
 }
 for(const edge of edges.values())edge.strandIds.sort();
 const strands=columns.map(s=>{
  const guide=s.guide.map(project),arrows=[],runs=[];
  // Separate the four passages INSIDE the sleeve, rather than merging their
  // rendered conductors at a single point. Each keeps its own quadrant.
  const displayGuide=guide.map((p,i)=>{
   if(!isCentre(p))return p;
   const incoming=unit(sub(guide[i-1],p)),outgoing=unit(sub(guide[i+1],p));
   return p.map((x,j)=>x+.04*(incoming[j]+outgoing[j]));
  });
  for(let i=0;i<s.edgeIds.length;i++){
   const a=displayGuide[i],b=displayGuide[i+1],edge=edges.get(s.edgeIds[i]),mid=a.map((x,j)=>(x+b[j])/2),radial=unit(mid);
   const offset=edge.sleeveLink?0:.08*(edge.strandIds.indexOf(s.id)-(edge.strandIds.length-1)/2);
   const points=Array.from({length:17},(_,k)=>{
    const t=k/16,taper=k===0||k===16?0:Math.sin(Math.PI*t);
    return a.map((x,j)=>x+t*(b[j]-x)+offset*taper*radial[j]);
   });
   runs.push({edgeId:edge.id,points});
   if(s.polarityDirection||s.routeDirection)arrows.push({edgeId:edge.id,segment:i,point:points[8],kind:s.polarityDirection?'polarity':'route',direction:unit(sub(b,a)).map(x=>x*(s.polarityDirection||s.routeDirection))});
  }
  return {id:s.id,inputSlot:s.inputSlot,outputSlot:s.outputSlot,colours:[...s.colours],guide,displayGuide,runs,points:runs.flatMap((r,i)=>i?r.points.slice(1):r.points),arrows};
 });
 return {vertices,edges:[...edges.values()],strands,...(sleeve?{sleeve}:{}),inputPole:project(reference.envelope[1]),outputPole:project(reference.envelope[0]),
  audit:{vertices:vertices.length,edges:edges.size,strands:strands.length,polarityArrows:strands.reduce((n,s)=>n+s.arrows.filter(a=>a.kind==='polarity').length,0),routeArrows:strands.reduce((n,s)=>n+s.arrows.filter(a=>a.kind==='route').length,0),displayLaneOffset:.04,...(sleeve?{shellVertices:reference.envelope.length,centralSleeves:1,sleeveStrands:sleeve.strandIds.length,incomingPairs:sleeve.incomingPairs.length,outgoingPairs:sleeve.outgoingPairs.length}:{})}};
}
