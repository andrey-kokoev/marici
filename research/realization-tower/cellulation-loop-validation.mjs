const distance=(a,b)=>Math.hypot(...a.map((x,i)=>x-b[i]));
export function validateCellulationLoop(model,arrows,anchors=[]){
 let loop=model;while(!loop.closingWhiteClone&&loop.previous)loop=loop.previous;
 if(!loop.closingWhiteClone)throw Error('Loop validation requires the completed closing step');
 const size=model.cellSize,tolerance=size*1e-6,lattice=p=>p.map(x=>Math.round(x*Math.SQRT2/size)),key=p=>lattice(p).join(','),edgeKey=(a,b)=>[key(a),key(b)].sort().join('|');
 const white=loop.closingWhiteClone,blue=loop.previous.blueClone,issues=[];
 const sides=[{name:'Red',from:blue.sourceStart,to:blue.sourceEnd,color:0xff3030},{name:'White A',from:white.sourceStart,to:white.sourceEnd,color:0xffffff},{name:'Blue',from:blue.arrows[0].from,to:blue.arrows.at(-1).to,color:blue.colour},{name:'White B',from:white.attachment,to:white.end,color:0xffffff}];
 const arrowMap=new Map();for(const arrow of arrows){const k=edgeKey(arrow.from,arrow.to);if(!arrowMap.has(k))arrowMap.set(k,[]);arrowMap.get(k).push(arrow);}
 const segments=[];
 for(const [sideIndex,side] of sides.entries()){
  const length=distance(side.from,side.to),count=Math.round(length/size);side.length=length/size;
  if(!count||Math.abs(length-count*size)>tolerance){issues.push({type:'length',message:`${side.name}: not an integer number of unit edges`,point:side.from});continue;}
  for(let i=0;i<count;i++){
   const from=side.from.map((x,j)=>x+(side.to[j]-x)*i/count),to=side.from.map((x,j)=>x+(side.to[j]-x)*(i+1)/count),found=arrowMap.get(edgeKey(from,to))??[];
   const priority=Math.max(...found.map(a=>a.order??0)),visible=found.filter(a=>(a.order??0)===priority);
   const forward=visible.filter(a=>distance(a.from,from)<tolerance&&distance(a.to,to)<tolerance),backward=visible.filter(a=>distance(a.from,to)<tolerance&&distance(a.to,from)<tolerance);
   let problem=null;
   if(!forward.length)problem=backward.length?'reversed-arrow':'missing-arrow';
   else if(!forward.some(a=>a.color===side.color))problem='arrow-color';
   else if(backward.length)problem='opposing-arrows';
   const segment={side:side.name,sideIndex,index:i,from,to,status:problem??'pass'};segments.push(segment);
   if(problem)issues.push({type:problem,from,to,point:from.map((x,j)=>(x+to[j])/2),message:`${side.name}: ${problem.replaceAll('-',' ')} (${key(from)}) → (${key(to)})`});
  }
 }
 const joins=sides.map((side,i)=>{
  const next=sides[(i+1)%sides.length],gap=distance(side.to,next.from),markers=anchors.filter(a=>distance(a.point,side.to)<tolerance),vertex=model.cells.some(c=>c.vertices.some(p=>distance(p,side.to)<tolerance));
  if(gap>tolerance)issues.push({type:'gap',point:side.to,from:side.to,to:next.from,message:`Join ${i+1}: gap ${gap/size} cell lengths`});
  if(!vertex||markers.length!==1)issues.push({type:'join-vertex',point:side.to,message:`Join ${i+1}: ${!vertex?'missing cell vertex':`${markers.length} dot IDs at the join`}`});
  const adjacent=segments.some(s=>s.status!=='pass'&&(distance(s.from,side.to)<tolerance||distance(s.to,side.to)<tolerance));
  return {id:`J${i+1}`,point:side.to,latticePoint:lattice(side.to),status:gap>tolerance||!vertex||markers.length!==1?'fail':adjacent?'warning':'pass',gap:gap/size,markerIds:markers.map(a=>a.id)};
 });
 const seen=new Set();let duplicateCells=0,invalidCells=0;
 for(const cell of model.cells){
  const vertices=cell.vertices.map(lattice),k=vertices.map(p=>p.join(',')).sort().join('|');
  const duplicate=seen.has(k);if(duplicate)duplicateCells++;seen.add(k);
  let valid=cell.vertices.every((p,i)=>p.every((x,j)=>Math.abs(x*Math.SQRT2/size-vertices[i][j])<1e-6)&&vertices[i].reduce((a,b)=>a+b,0)%2===0)&&new Set(vertices.map(p=>p.join(','))).size===vertices.length;
  if(cell.kind==='tetrahedron')valid&&=vertices.length===4&&vertices.every((p,i)=>vertices.slice(i+1).every(q=>Math.abs(distance(p,q)**2-2)<1e-6));
  else if(cell.kind==='octahedron'){
   const center=[0,1,2].map(i=>vertices.reduce((sum,p)=>sum+p[i],0)/vertices.length);
   valid&&=vertices.length===6&&center.every(Number.isInteger)&&Math.abs(center.reduce((a,b)=>a+b,0)%2)===1&&vertices.every(p=>p.reduce((sum,x,i)=>sum+Math.abs(x-center[i]),0)===1);
  }else valid=false;
  if(!valid)invalidCells++;
  if(duplicate||!valid)issues.push({type:duplicate?'duplicate-cell':'invalid-cell',point:cell.vertices[0],message:`${cell.id}: ${duplicate?'duplicate cell':'not a whole FCC tetrahedron/octahedron'}`});
 }
 const nonmanifoldFaces=model.faces.filter(f=>f.owners.length>2).length;
 if(nonmanifoldFaces)issues.push({type:'nonmanifold',message:`${nonmanifoldFaces} faces have more than two owners`,point:model.faces.find(f=>f.owners.length>2).vertices[0]});
 const lengthsMatch=sides.every(s=>Math.abs(s.length-sides[0].length)<1e-6);
 if(!lengthsMatch)issues.push({type:'length',message:'The four bars have different lengths',point:sides[0].from});
 const invalidArrows=arrows.filter(a=>Math.abs(distance(a.from,a.to)-size)>tolerance||[a.from,a.to].some(p=>p.some(x=>Math.abs(x*Math.SQRT2/size-Math.round(x*Math.SQRT2/size))>1e-6)||Math.abs(lattice(p).reduce((sum,x)=>sum+x,0)%2)!==0));
 for(const a of invalidArrows)issues.push({type:'invalid-arrow',from:a.from,to:a.to,point:a.from,message:'Rendered arrow is not a unit FCC edge'});
 const pathIssues=issues.filter(i=>['reversed-arrow','missing-arrow','arrow-color','opposing-arrows'].includes(i.type));
 const checks=[
  {name:'Four joins',status:joins.every(j=>j.gap<1e-6)?'pass':'fail',detail:joins.every(j=>j.gap<1e-6)?'No endpoint gaps':'Endpoint gaps detected'},
  {name:'Bar lengths',status:lengthsMatch?'pass':'fail',detail:sides.map(s=>`${s.name}: ${s.length.toFixed(3)}`).join(' · ')},
  {name:'Rendered arrow route',status:pathIssues.length?'fail':'pass',detail:`${segments.length} unit edges; ${pathIssues.length} direction/color issues`},
  {name:'Arrow geometry',status:invalidArrows.length?'fail':'pass',detail:`${arrows.length} rendered arrows; ${invalidArrows.length} non-unit/off-lattice`},
  {name:'Join dots',status:joins.every(j=>j.markerIds.length===1)?'pass':'fail',detail:'One existing dot ID per corner required'},
  {name:'FCC cells',status:duplicateCells||invalidCells||nonmanifoldFaces?'fail':'pass',detail:`${model.cells.length} cells; ${duplicateCells} duplicates; ${invalidCells} invalid; ${nonmanifoldFaces} nonmanifold faces`},
  {name:'N–N–P–E roles',status:'pending',detail:'Unassigned: colors and closure do not establish particle roles'},
 ];
 return {status:issues.length?'issues':'geometry-pass',checks,issues,joins,segments,sides,duplicateCells,invalidCells,roles:'unassigned',scope:'Route assumes red → white A → blue → white B. Counterflow may be intentional. Cell checks use model FCC cells; decorative surface overlap and face-role consistency still require visual review.'};
}
