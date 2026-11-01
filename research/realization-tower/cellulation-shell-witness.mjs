import {analyzeDotCompatibility} from '../strominger/cellulation-dot-compatibility.mjs';
import {blueClonePoint,blueCloneVector} from './cellulation-blue-clone.mjs';

// A deterministic replay of the existing Step 3–6 tetrahedron and Step 8
// octahedron protocols. These are construction witnesses, not physical proofs.
export function buildShellWitnessPlan(model,initial,{octahedronOrder=[0,1,2,3],requireSourceRoles=false}={}){
 if(typeof requireSourceRoles!=='boolean')throw Error('requireSourceRoles must be boolean');
 if(octahedronOrder.length!==4||new Set(octahedronOrder).size!==4||octahedronOrder.some(i=>!Number.isInteger(i)||i<0||i>3))throw Error('Expected a permutation of four octahedral arrivals');
 const size=model.cellSize,key=p=>p.map(x=>Math.round(x*Math.SQRT2/size)).join(','),faceKey=f=>f.map(key).sort().join('|');
 const arrowKey=a=>`${key(a.from)}>${key(a.to)}:${a.colour??a.color}`;
 let loop=model.previous;while(!loop.closingWhiteClone)loop=loop.previous;
 const blue=loop.previous.blueClone;let seed=blue.source,oct=blue.source;
 while(seed.step!==6)seed=seed.previous;while(oct.step!==8)oct=oct.previous;
 const family=model.shellFace.seedFaces.find(s=>Math.abs(s.normal.reduce((sum,x,i)=>sum+x*model.shellFace.normal[i],0))>1-1e-7);
 const isBlue=family.id.startsWith('blue'),transform=p=>isBlue?blueClonePoint(blue,p):p;
 const vector=p=>isBlue?blueCloneVector(blue,p):p,charged=isBlue?blue.colour:seed.arrows[0].colour;
 const dotClaims=[],events=[],arrows=[],dots=[],faces=[],cells=[],scaffoldEdges=[],blockers=[],knownArrows=new Map(),knownDots=new Map(),knownFaces=new Map(),knownCells=new Map();let clock=0;
 const seedDependency='retained-step',knownEdges=new Set(),edgeKey=(a,b)=>[key(a),key(b)].sort().join('|');
 for(const c of initial.cells)for(const f of c.faces)for(let i=0;i<3;i++)knownEdges.add(edgeKey(f[i],f[(i+1)%3]));
 for(const a of initial.arrows)knownArrows.set(arrowKey(a),{...a,id:`retained-arrow:${arrowKey(a)}`,event:seedDependency});
 for(const a of initial.anchors)if(a.solid)knownDots.set(key(a.point),{...a,event:seedDependency,solid:true});
 for(const c of initial.cells){knownCells.set(faceKey(c.vertices),seedDependency);for(const f of c.faces)knownFaces.set(faceKey(f),{event:seedDependency,retained:true});}
 const boundary=new Map(model.shellFace.boundaryReadings.map(r=>[faceKey(r.vertices),r]));
 function emit(type,cell,requires,duration,details={}){
  const event={id:`${model.step}:action:${events.length}`,index:events.length,type,cell,requires:[...new Set(requires)],start:clock,end:clock+duration,...details};events.push(event);clock=event.end;return event;
 }
 function fit(template,target){
  const source=template.map(transform),targetKeys=new Set(target.map(key));
  for(const p of target){const shift=p.map((x,i)=>x-source[0][i]);if(source.every(q=>targetKeys.has(key(q.map((x,i)=>x+shift[i])))))return q=>transform(q).map((x,i)=>x+shift[i]);}
  return null;
 }
 function claim(point,colour,normal,event,role,kind='proposal',center=null){
  const old=knownDots.get(key(point));dotClaims.push({point:key(point),cell:event.cell,event:event.id,role,kind,colour,normal:normal?[...normal]:null,center:center?[...center]:null,observedColour:old?.colour??null,retained:old?.event===seedDependency,at:kind==='requirement'||event.type.startsWith('propose-')?event.start:event.end});
 }
 function propose(point,colour,normal,event,role,center){
  claim(point,colour,normal,event,role,'proposal',center);
  const k=key(point);if(knownDots.has(k))return knownDots.get(k);
  const d={id:`shell:${k}`,name:'candidate',point,colour,normal,appearAt:event.type.startsWith('propose-')?event.start:event.end,fillStart:Infinity,fillEnd:Infinity,event:event.id,solid:false};knownDots.set(k,d);dots.push(d);return d;
 }
 function draw(arrow,cell,dependency,duration=1600){
  const k=arrowKey(arrow),old=knownArrows.get(k);knownEdges.add(edgeKey(arrow.from,arrow.to));
  if(old)return emit('reuse-arrow',cell,[dependency,old.event],0,{arrow:old.id,from:arrow.from,to:arrow.to,colour:arrow.colour});
  const reverse=knownArrows.get(arrowKey({...arrow,from:arrow.to,to:arrow.from}));
  const e=emit('draw-arrow',cell,[dependency],duration,{from:arrow.from,to:arrow.to,colour:arrow.colour,oppositeRetained:reverse?.id??null});
  const a={...arrow,id:`shell-arrow:${k}`,start:e.start,end:e.end,event:e.id,oppositeRetained:reverse?.id??null};arrows.push(a);knownArrows.set(k,a);e.arrow=a.id;return e;
 }
 function solidify(points,cell,dependency){
  const e=emit('witness-dots',cell,[dependency,...points.map(p=>knownDots.get(key(p)).event)],350,{points:points.map(key)});
  for(const point of points){const d=knownDots.get(key(point));if(!d.solid){d.fillStart=e.start;d.fillEnd=e.end;d.event=e.id;d.solid=true;}}
  return e;
 }
 function fill(triangles,cell,dependencies){
  const e=emit('fill-faces',cell,dependencies,650,{faces:triangles.map(faceKey),retainedFaces:[]});
  for(const vertices of triangles){const k=faceKey(vertices),old=knownFaces.get(k);if(old){e.requires.push(old.event);e.retainedFaces.push(k);continue;}
   const reading=boundary.get(k),f={id:k,vertices,colour:reading?.colour??0xffffff,source:reading?.source??'neutral-internal-scaffold',boundary:!!reading,start:e.start,end:e.end,event:e.id};faces.push(f);knownFaces.set(k,f);
  }
  e.requires=[...new Set(e.requires)];return e;
 }
 function commit(cell,lastWitness){
  const faceProofs=cell.faces.map(f=>({face:faceKey(f),event:knownFaces.get(faceKey(f)).event}));
  const e=emit('commit-cell',cell.id,[lastWitness,...faceProofs.map(f=>f.event)],0,{faceProofs});knownCells.set(faceKey(cell.vertices),e.id);cells.push({cell,end:e.end,event:e.id});
 }
 function roleMismatch(requirements){
  if(!requireSourceRoles)return null;
  for(const {point,colour,role} of requirements){const old=knownDots.get(key(point));if(old&&old.colour!==colour)return {reason:old.colour==null?'unknown-dot-colour':'shared-dot-role-mismatch',point:key(point),role,requiredColour:colour,observedColour:old.colour??null};}
  return null;
 }
 function tetra(cell,map){
  const A=map(seed.markedVertex),C=map(seed.proposedVertex),B=map(seed.witness.priorTurnMarkers[0].point),D=map(seed.witness.turnMarker.point);
  const anchor=knownDots.get(key(A));if(!anchor?.solid)return {reason:'missing-solid-source',point:key(A)};
  const mismatch=roleMismatch([{point:A,colour:0xffffff,role:'A:white-source'},{point:C,colour:0xffffff,role:'C:white-destination'},{point:B,colour:charged,role:'B:first-turn'},{point:D,colour:charged,role:'D:second-turn'}]);if(mismatch)return mismatch;
  const center=[0,1,2].map(i=>cell.vertices.reduce((sum,p)=>sum+p[i],0)/4),normal=p=>{const v=p.map((x,i)=>x-center[i]),length=Math.hypot(...v);return v.map(x=>x/length);};
  let e=emit('propose-target',cell.id,[anchor.event],900,{point:key(C)});claim(A,0xffffff,null,e,'A:white-source','requirement');propose(C,0xffffff,normal(C),e,'C:white-destination',center);
  e=draw({from:A,to:C,colour:charged},cell.id,e.id);const main=e;
  e=draw({from:C,to:B,colour:0xffffff},cell.id,e.id);propose(B,charged,normal(B),e,'B:first-turn',center);
  e=draw({from:B,to:A,colour:0xffffff},cell.id,e.id);
  const first=emit('first-return-witness',cell.id,[main.id,e.id],0,{path:[C,B,A].map(key)});
  e=draw({from:A,to:D,colour:0xffffff},cell.id,first.id);propose(D,charged,normal(D),e,'D:second-turn',center);
  e=draw({from:D,to:C,colour:0xffffff},cell.id,e.id);
  const second=emit('second-return-witness',cell.id,[first.id,e.id],0,{path:[A,D,C].map(key)});
  e=solidify([C],cell.id,second.id);
  e=fill([[A,C,B],[A,D,C]],cell.id,[first.id,second.id,e.id]);
  e=draw({from:B,to:D,colour:0xffffff},cell.id,e.id);
  const connected=emit('connect-candidates-witness',cell.id,[e.id,second.id],0,{points:[B,D].map(key)});
  e=solidify([B,D],cell.id,connected.id);e=fill([[A,B,D],[B,C,D]],cell.id,[connected.id,e.id]);commit(cell,e.id);return null;
 }
 function octahedron(cell,map){
  const bridge=oct.bridge,parents=oct.previous.cells.map(c=>faceKey(c.vertices.map(map))),missing=parents.filter(k=>!knownCells.has(k));
  if(missing.length)return {reason:'missing-completed-support-tetrahedra',parents:missing};
  const ring=bridge.ring.map(map),shared=map(bridge.shared),opposite=map(bridge.opposite),missingDots=[shared,...ring].filter(p=>!knownDots.get(key(p))?.solid);
  if(missingDots.length)return {reason:'missing-solid-octahedral-support',points:missingDots.map(key)};
  const mismatch=roleMismatch([{point:shared,colour:0xffffff,role:'octahedron:white-shared'},...ring.map(point=>({point,colour:charged,role:'octahedron:charged-ring'})),{point:opposite,colour:0xffffff,role:'octahedron:white-opposite'}]);if(mismatch)return mismatch;
  const n=vector(bridge.opposite.map((x,i)=>x-bridge.center[i])),length=Math.hypot(...n);
  let e=emit('propose-opposite',cell.id,[...parents.map(k=>knownCells.get(k)),...[shared,...ring].map(p=>knownDots.get(key(p)).event)],600,{point:key(opposite)});claim(shared,0xffffff,null,e,'octahedron:white-shared','requirement');for(const p of ring)claim(p,charged,null,e,'octahedron:charged-ring','requirement');propose(opposite,0xffffff,n.map(x=>x/length),e,'octahedron:white-opposite',map(bridge.center));
  const arrived=[];for(const i of octahedronOrder){const from=ring[i];e=draw({from,to:opposite,colour:0xffffff},cell.id,e.id,1000);arrived.push(e.id);}
  const closure=emit('four-arrival-witness',cell.id,arrived,0,{point:key(opposite)});
  for(const face of cell.faces)for(let i=0;i<3;i++){const a=face[i],b=face[(i+1)%3],k=edgeKey(a,b);if(!knownEdges.has(k)){knownEdges.add(k);scaffoldEdges.push({cell:cell.id,vertices:[a,b],end:closure.end,event:closure.id,role:'octahedron-equatorial-scaffold'});}}
  e=solidify([opposite],cell.id,closure.id);e=fill(cell.faces,cell.id,[closure.id,e.id]);commit(cell,e.id);return null;
 }
 const targetKeys=model.shellFace.newCells.map(c=>faceKey(c.vertices));
 if(new Set(targetKeys).size!==targetKeys.length||targetKeys.some(k=>knownCells.has(k)))throw Error('Duplicate or retained cell in construction targets');
 const pending=model.shellFace.newCells.map(cell=>({cell,map:fit(cell.kind==='tetrahedron'?seed.cells[0].vertices:oct.bridge.cell.vertices,cell.vertices)}));
 while(pending.length){
  let progressed=false;const failures=[];
  for(let i=0;i<pending.length;i++){
   const {cell,map}=pending[i],failure=!map?{reason:'no-source-template-isometry'}:cell.kind==='tetrahedron'?tetra(cell,map):octahedron(cell,map);
   if(failure){failures.push({cell:cell.id,...failure});continue;}
   pending.splice(i,1);progressed=true;break;
  }
  if(!progressed){blockers.push(...failures);break;}
 }
 const compatibility=analyzeDotCompatibility(dotClaims);
 compatibility.blockedRoleRequirements=blockers.filter(b=>b.reason==='shared-dot-role-mismatch'||b.reason==='unknown-dot-colour');
 if(compatibility.blockedRoleRequirements.length)compatibility.status='unresolved';
 const plan={rolePolicy:requireSourceRoles?'strict-role-preserving':'legacy-first-writer',dotClaims,compatibility,cellSize:size,retainedDotKeys:initial.anchors.filter(a=>a.solid).map(a=>key(a.point)),events,arrows,dots,faces,cells,scaffoldEdges,blockers,duration:clock,complete:blockers.length===0,retainedCells:initial.cells.length,sourceProtocols:['cellulation steps 3–6','cellulation step 8'],scope:'Directed construction witnesses; existing dot/face colors retained. Not a physical coherence certificate.'};
 validateShellWitnessPlan(plan);return plan;
}

export function validateShellWitnessPlan(plan){
 const done=new Map([['retained-step',0]]);let previousEnd=0;
 for(const e of plan.events){
  if(e.start!==previousEnd)throw Error('Non-sequential construction schedule');previousEnd=e.end;
  if(e.start<0||e.end<e.start||!Number.isFinite(e.end))throw Error(`Invalid action interval: ${e.id}`);
  for(const dep of e.requires)if(!done.has(dep)||done.get(dep)>e.start)throw Error(`Unmet prerequisite ${dep} for ${e.id}`);
  done.set(e.id,e.end);
 }
 const groups=new Map();for(const e of plan.events){if(!groups.has(e.cell))groups.set(e.cell,[]);groups.get(e.cell).push(e);}
 const key=p=>p.map(x=>Math.round(x*Math.SQRT2/plan.cellSize)).join(','),solid=new Set(plan.retainedDotKeys);
 for(const es of groups.values()){
  const tetra=es[0].type==='propose-target',expected=tetra?['propose-target','arrow','arrow','arrow','first-return-witness','arrow','arrow','second-return-witness','witness-dots','fill-faces','arrow','connect-candidates-witness','witness-dots','fill-faces','commit-cell']:['propose-opposite','arrow','arrow','arrow','arrow','four-arrival-witness','witness-dots','fill-faces','commit-cell'];
  if(es.length!==expected.length||es.some((e,i)=>(['draw-arrow','reuse-arrow'].includes(e.type)?'arrow':e.type)!==expected[i]))throw Error('Incomplete local witness protocol');
  for(let i=1;i<es.length;i++)if(!es[i].requires.includes(es[i-1].id))throw Error(`Missing immediate witness prerequisite: ${es[i].id}`);
  const require=(event,dependencies)=>{if(dependencies.some(d=>!event.requires.includes(d.id)))throw Error('Missing local closure witness');};
  if(tetra){require(es[4],[es[1],es[3]]);require(es[7],[es[4],es[6]]);require(es[9],[es[4],es[7],es[8]]);require(es[11],[es[10],es[7]]);require(es[13],[es[11],es[12]]);}
  else require(es[5],es.slice(1,5));
  const cell=plan.cells.find(c=>c.cell.id===es[0].cell)?.cell;if(!cell)throw Error('Missing cell commitment');
  const vertices=new Set(cell.vertices.map(key));
  for(const e of es.filter(e=>['draw-arrow','reuse-arrow'].includes(e.type))){
   if(!vertices.has(key(e.from))||!vertices.has(key(e.to))||Math.abs(Math.hypot(...e.from.map((x,i)=>x-e.to[i]))-plan.cellSize)>1e-7)throw Error('Arrow is not a unit edge of its witnessed cell');
  }
  const same=(a,b)=>key(a)===key(b);
  if(tetra){
   const [main,r1,r2,s1,s2,last]=[1,2,3,5,6,10].map(i=>es[i]);
   if(!solid.has(key(main.from)))throw Error('Tetrahedron source is not witnessed');
   if(!same(main.to,r1.from)||!same(r1.to,r2.from)||!same(r2.to,main.from)||!same(s1.from,main.from)||!same(s1.to,s2.from)||!same(s2.to,main.to)||!same(last.from,r1.to)||!same(last.to,s1.to))throw Error('Broken tetrahedral return paths');
   for(const p of cell.vertices)solid.add(key(p));
  }else{
   const arrivals=es.slice(1,5);if(new Set(arrivals.map(e=>key(e.from))).size!==4||arrivals.some(e=>!solid.has(key(e.from))||!same(e.to,arrivals[0].to)))throw Error('Broken octahedral arrival witness');
   solid.add(key(arrivals[0].to));
  }
  const commit=es.at(-1);if(commit.faceProofs.length!==cell.faces.length||commit.faceProofs.some(f=>!commit.requires.includes(f.event)))throw Error('Cell committed without all face witnesses');
 }
 for(const edge of plan.scaffoldEdges){
  const event=plan.events.find(e=>e.id===edge.event),cell=plan.cells.find(c=>c.cell.id===edge.cell)?.cell;
  if(event?.type!=='four-arrival-witness'||cell?.kind!=='octahedron'||edge.end!==event.end||plan.scaffoldEdges.filter(e=>e.cell===edge.cell).length>2)throw Error('Unwitnessed octahedral scaffold');
  if(Math.abs(Math.hypot(...edge.vertices[0].map((x,i)=>x-edge.vertices[1][i]))-plan.cellSize)>1e-7)throw Error('Non-unit scaffold edge');
 }
 for(const records of [plan.arrows,plan.faces,plan.cells])for(const r of records)if(done.get(r.event)!==r.end)throw Error(`Uncertified construction record ${r.id??r.cell?.id}`);
 for(const d of plan.dots)if(!Number.isFinite(d.fillEnd)||done.get(d.event)!==d.fillEnd)throw Error(`Unwitnessed dot ${d.id}`);
 return true;
}

export function shellWitnessFrame(plan,elapsed){
 const t=Math.max(0,elapsed),progress=(start,end)=>t>=end?1:t<=start?0:(t-start)/(end-start),current=plan.events.find(e=>t<e.end);
 return {phase:current?current.type:plan.complete?'complete':'blocked',action:current?.index??plan.events.length,cell:current?.cell??null,totalActions:plan.events.length,duration:plan.duration,blockers:plan.blockers,
  arrowProgress:plan.arrows.map(a=>progress(a.start,a.end)),faceProgress:plan.faces.map(f=>progress(f.start,f.end)),dotStates:plan.dots.map(d=>({visible:t>=d.appearAt,fill:progress(d.fillStart,d.fillEnd)})),completedCells:plan.cells.filter(c=>t>=c.end).map(c=>c.cell)};
}
