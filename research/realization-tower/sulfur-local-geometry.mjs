// Geometry tests and observed local replay; no paths are created or rerouted.
const sub=(a,b)=>a.map((x,i)=>x-b[i]);
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const cos=(a,b)=>dot(a,b)/Math.sqrt(dot(a,a)*dot(b,b));
const key=p=>p.join(',');
const require=(ok,message)=>{if(!ok)throw Error(message);};
const det3=g=>g[0][0]*(g[1][1]*g[2][2]-g[1][2]*g[2][1])-g[0][1]*(g[1][0]*g[2][2]-g[1][2]*g[2][0])+g[0][2]*(g[1][0]*g[2][1]-g[1][1]*g[2][0]);
export function analyzeNativePortFrame(motif){
 const axis=sub(motif.head,motif.tail),incoming=motif.inputs.map(p=>({...p,arm:sub(p.point,motif.tail)}));
 const inputs=incoming.map(p=>({...p,cosineToAxis:cos(p.arm,axis),kind:Math.abs(cos(p.arm,axis)+1)<1e-10?'straight':'oblique'}));
 require(inputs.filter(p=>p.kind==='straight').length===1&&inputs.filter(p=>p.kind==='oblique').length===1,'Frame needs one straight and one oblique arrival');
 const oblique=inputs.find(p=>p.kind==='oblique').arm;
 const transverse=v=>v.map((x,i)=>x-axis[i]*dot(v,axis)/dot(axis,axis));
 const outputs=motif.outputs.map(p=>{
  const arm=sub(p.point,motif.head),vectors=[axis,oblique,arm],gram=vectors.map(a=>vectors.map(b=>dot(a,b)));
  const gramDeterminant=det3(gram),normalizedDeterminant=gramDeterminant/vectors.reduce((s,v)=>s*dot(v,v),1);
  const transverseCosine=cos(transverse(oblique),transverse(arm));
  return {...p,kind:Math.abs(normalizedDeterminant)<1e-10?'coplanar':'skew',gramDeterminant,normalizedDeterminant,transverseCosine,
   planeAngleDegrees:Math.acos(Math.max(-1,Math.min(1,Math.abs(transverseCosine))))*180/Math.PI};
 });
 require(outputs.filter(p=>p.kind==='coplanar').length===1&&outputs.filter(p=>p.kind==='skew').length===1,'Frame needs one planar and one skew departure');
 return {axis,inputs,outputs,planeDefinition:'span of oriented carrier and its oblique incoming arm'};
}
export function learnGeometricLocalRule(motifs){
 const selectorByA={},inputByAgreement={},outputBySign={};
 const observe=(table,key,value)=>{require(table[key]===undefined||table[key]===value,'No consistent geometric local rule');table[key]=value;};
 for(const motif of motifs){
  const frame=analyzeNativePortFrame(motif);observe(selectorByA,motif.context.a,motif.selector);
  for(const row of motif.rows){
   const sign=row.polarities[motif.selector];
   observe(inputByAgreement,String(sign===row.polarities.b),frame.inputs.find(p=>p.edge===row.incomingEdge).kind);
   observe(outputBySign,sign,frame.outputs.find(p=>p.edge===row.outgoingEdge).kind);
  }
 }
 require(selectorByA['+']&&selectorByA['-']&&inputByAgreement.true&&inputByAgreement.false&&outputBySign['+']&&outputBySign['-'],'Incomplete training classes');
 return {selectorByA,inputByAgreement,outputBySign,scope:'observed upper mixing motifs; ports classified by Euclidean geometry, not coordinate ordering'};
}
export function replayGeometricLocalPacket(motif,packet,rule,direction='forward'){
 require(['forward','reverse'].includes(direction),'Unknown direction');
 for(const [bit,value] of Object.entries(motif.context))require(packet.polarities?.[bit]===value,'Wrong carrier context');
 const frame=analyzeNativePortFrame(motif),selector=rule.selectorByA[packet.polarities.a],sign=packet.polarities[selector];
 require(sign==='+'||sign==='-','Missing selector state');
 const inputKind=rule.inputByAgreement[String(sign===packet.polarities.b)],outputKind=rule.outputBySign[sign];
 const input=frame.inputs.find(p=>p.kind===inputKind),output=frame.outputs.find(p=>p.kind===outputKind);
 require(input&&output,'Incomplete geometric switch rule');
 require(packet.port===(direction==='forward'?input.edge:output.edge),'Packet does not arrive on its geometrically selected port');
 return {...structuredClone(packet),port:direction==='forward'?output.edge:input.edge};
}
function endGeometry(origin,other,ports){
 const arms=[sub(other,origin),...ports.map(p=>sub(p,origin))],squaredLengths=arms.map(a=>dot(a,a));
 const cosines=arms.flatMap((a,i)=>arms.slice(i+1).map(b=>cos(a,b))).sort((a,b)=>a-b);
 // Necessary for a non-stretching fold of a filled planar 120-degree star
 // with these equal-length arms: none of its pairwise endpoint distances
 // can exceed the original planar chord. This is NOT a graph-hinge test.
 const maxChordExpansion=arms.reduce((max,a,i)=>Math.max(max,...arms.slice(i+1).map((b,j)=>{
  const planarSquared=dot(a,a)+dot(b,b)+Math.sqrt(dot(a,a)*dot(b,b));
  return dot(sub(a,b),sub(a,b))/planarSquared;
 })),1);
 return {squaredLengths,cosines,hexAngles:cosines.every(c=>Math.abs(c+.5)<1e-10),equalLengths:squaredLengths.every(x=>Math.abs(x-squaredLengths[0])<1e-10),maxChordExpansion};
}
export function scanSharedCarriers(reference){
 // Every contiguous INTERNAL run of every existing complete route, including
 // the opposite orientation. Endpoints must have one observed arm outside.
 const groups=new Map();let windows=0;
 for(const strand of reference.strands)for(let start=1;start<strand.guide.length-2;start++)for(let end=start+1;end<strand.guide.length-1;end++){
  const original=strand.guide.slice(start,end+1),forward=original.map(key).join('|'),backward=[...original].reverse().map(key).join('|'),reverse=backward<forward;
  const path=reverse?[...original].reverse():original,id=reverse?backward:forward;
  if(!groups.has(id))groups.set(id,{path,occurrences:[]});
  groups.get(id).occurrences.push({strandId:strand.id,start,end,reversed:reverse,
   previous:strand.guide[reverse?end+1:start-1],next:strand.guide[reverse?start-1:end+1]});windows++;
 }
 const summaries=[];
 const points=ps=>[...new Map(ps.map(p=>[key(p),p])).values()];
 function examine(group,occurrences,scope){
  const inputs=points(occurrences.map(r=>r.previous)),outputs=points(occurrences.map(r=>r.next));
  if(inputs.length!==2||outputs.length!==2)return;
  const path=group.path,tail=path[0],head=path.at(-1),chord=sub(head,tail);if(dot(chord,chord)<1e-12)return;
  const local={tail:endGeometry(tail,path[1],inputs),head:endGeometry(head,path.at(-2),outputs)};
  const coarse={tail:endGeometry(tail,head,inputs),head:endGeometry(head,tail,outputs)};
  summaries.push({scope,length:path.length-1,path,occurrences,inputs,outputs,local,coarse,
   tangentStarMatch:local.tail.hexAngles&&local.head.hexAngles,
   chordAngleMatch:coarse.tail.hexAngles&&coarse.head.hexAngles,
   equalScaleChordMatch:coarse.tail.hexAngles&&coarse.head.hexAngles&&coarse.tail.equalLengths&&coarse.head.equalLengths});
 }
 let sharedGroups=0;
 for(const group of groups.values()){
  if(new Set(group.occurrences.map(r=>r.strandId)).size<2)continue;sharedGroups++;
  examine(group,group.occurrences,'all recorded traffic');
  if(group.occurrences.length>2)for(let i=0;i<group.occurrences.length;i++)for(let j=i+1;j<group.occurrences.length;j++){
   if(group.occurrences[i].strandId===group.occurrences[j].strandId)continue;
   examine(group,[group.occurrences[i],group.occurrences[j]],'two-strand subtraffic; other identities not removed');
  }
 }
 return {scope:'exhaustive contiguous internal runs of the current sixteen reference routes; not arbitrary native paths or general branched regions',windows,distinctRuns:groups.size,sharedGroups,
  candidates:summaries,counts:{candidates:summaries.length,maxCarrierEdges:Math.max(0,...summaries.map(c=>c.length)),tangentStarMatches:summaries.filter(c=>c.tangentStarMatch).length,chordAngleMatches:summaries.filter(c=>c.chordAngleMatch).length,equalScaleChordMatches:summaries.filter(c=>c.equalScaleChordMatch).length}};
}
export function testSingleEdgeSheetFolds(motifs){
 return motifs.map(m=>{
  const tail=endGeometry(m.tail,m.head,m.inputs.map(p=>p.point)),head=endGeometry(m.head,m.tail,m.outputs.map(p=>p.point));
  return {motif:m.number,tail,head,necessaryNonExpansionSatisfied:tail.maxChordExpansion<=1+1e-10&&head.maxChordExpansion<=1+1e-10,
   assumption:'filled planar source chart containing local straight chords; unit arms mapped to equal-length native arms; no stretching'};
 });
}
