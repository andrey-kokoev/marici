// Strand presentation of the retained reflection histories. Routes visit the
// history's successive copies through shared-edge contacts of each assembly.
// Shortest-path ties use cell ID order; inlet/outlet tails are display leads.
const key=p=>p.map(x=>x.toFixed(8)).join(',');
const dist2=(a,b)=>a.reduce((s,x,i)=>s+(x-b[i])**2,0);
const lerp=(a,b,t)=>a.map((x,i)=>x+t*(b[i]-x));
const normalize=a=>{const n=Math.hypot(...a);return a.map(x=>x/n);};
const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
export function buildReflectionBundle(certificate,step,project){
 const allCopies=new Map(certificate.stages[4].copies.map(c=>[c.id,c]));
 const cellOf=new Map(certificate.geometryGroups.flatMap(g=>g.copies.map(c=>[c,g.cell])));
 const cellVertices4=new Map(certificate.geometryGroups.map(g=>[g.cell,allCopies.get(g.copies[0]).vertices4]));
 const edgeByPair=new Map(certificate.contacts.map(c=>[[...c.cells].sort((a,b)=>a-b).join(','),c]));
 const stages=certificate.stages.slice(0,step+1).map(s=>new Set(s.copies.map(c=>c.id)));
 const activeCells=new Set([...stages[step]].map(c=>cellOf.get(c)));
 const extremes=[...activeCells].flatMap(id=>cellVertices4.get(id).slice(0,3).map(vertex4=>({id,vertex4,point:project(vertex4)})));
 const top=[...extremes].sort((a,b)=>b.point[1]-a.point[1]||a.id-b.id||key(a.point).localeCompare(key(b.point)))[0];
 const bottom=[...extremes].sort((a,b)=>a.point[1]-b.point[1]||a.id-b.id||key(a.point).localeCompare(key(b.point)))[0];
 function route(source,target,stage){
  const allowed=new Set([...stages[stage]].map(c=>cellOf.get(c))),queue=[[source]],seen=new Set([source]);
  for(let i=0;i<queue.length;i++){
   const path=queue[i],last=path.at(-1);if(last===target)return path;
   const next=certificate.contacts.filter(e=>e.cells.includes(last)).map(e=>e.cells.find(x=>x!==last)).filter(x=>allowed.has(x)).sort((a,b)=>a-b);
   for(const n of next)if(!seen.has(n)){seen.add(n);queue.push([...path,n]);}
  }
  throw Error(`No reflection contact route ${source} -> ${target} at stage ${stage}`);
 }
 function appendWalk(guide,walk,runs,stage){
  for(let i=1;i<walk.length;i++){
   const pair=[walk[i-1],walk[i]].sort((a,b)=>a-b),contact=edgeByPair.get(pair.join(','));
   if(!contact)throw Error('Missing geometric seam');
   // Enter and cross the actual shared edge, not a cell-centre graph link.
   guide.push(...contact.vertices);
   runs.push({from:walk[i-1],to:walk[i],stage,sharedEdge:contact.vertices,map:contact.map});
  }
 }
 const styles=[{label:'white',colors:[0xffffff]},{label:'blue-white',colors:[0x168fff,0xffffff]},{label:'red-white',colors:[0xff3030,0xffffff]},{label:'blue',colors:[0x168fff]}];
 const strands=certificate.stages[step].copies.map(copy=>{
  const number=Number(copy.id.slice(1)),bits=[0,1,2,3].map(i=>(number>>i)&1),pe=2*bits[0]+bits[1];
  const ancestry=stages.map(present=>{let c=copy;while(!present.has(c.id))c=allCopies.get(c.parent);return c.id;});
  const guide=[top.vertex4],runs=[];
  // A labelled native-edge circuit visits all five simplex vertices. These two
  // complementary cycles (and reverses) supply the four display colour styles;
  // every reflected copy uses its own transported, labelled vertices.
  const orders=[[0,1,2,3,4],[0,2,4,1,3],[0,4,3,2,1],[0,3,1,4,2]];
  function visit(id){
   const vertices=allCopies.get(id).vertices4,order=orders[pe];
   const start=order.findIndex(i=>JSON.stringify(vertices[i])===JSON.stringify(guide.at(-1)));
   if(start<0)throw Error('Contact vertex is not a vertex of the visited copy');
   for(let n=1;n<=5;n++)guide.push(vertices[order[(start+n)%5]]);
  }
  appendWalk(guide,route(top.id,cellOf.get(ancestry[0]),step),runs,step);visit(ancestry[0]);
  for(let j=1;j<=step;j++)if(ancestry[j]!==ancestry[j-1]){
   appendWalk(guide,route(cellOf.get(ancestry[j-1]),cellOf.get(ancestry[j]),j),runs,j);visit(ancestry[j]);
  }
  appendWalk(guide,route(cellOf.get(copy.id),bottom.id,step),runs,step);
  guide.push(bottom.vertex4);
  const nativeGuide4=guide.filter((p,i)=>i===0||JSON.stringify(p)!==JSON.stringify(guide[i-1]));
  const projected=nativeGuide4.map(project),clean=projected.filter((p,i)=>i===0||dist2(p,projected[i-1])>1e-18);
  const row=2*bits[0]+bits[2],column=2*bits[1]+bits[3],offset=[.065*(row-1.5),0,.065*(column-1.5)];
  return {id:'reflection:'+copy.id,copyId:copy.id,word:copy.word,bits,ancestry,...styles[pe],decisions:{white:bits[0],rotation1:bits[1],red:bits[2],rotation2:bits[3]},row,column,
   nativeGuide4,guide:clean,contactRuns:runs,incoming:top.point.map((x,i)=>x+offset[i]+(i===1?1.4:0)),outgoing:bottom.point.map((x,i)=>x+offset[i]-(i===1?1.4:0)),branches:[]};
 });
 // Each retained strand remains one mesh. Lane packing separates coincident
 // traversals without merging identities at shared contacts.
 const lanes=new Map();
 for(const s of strands)for(let i=1;i<s.guide.length;i++){
  const a=key(s.guide[i-1]),b=key(s.guide[i]),edge=[a,b].sort().join('|'),lane=s.id+':'+(a<b?'forward':'reverse');
  if(!lanes.has(edge))lanes.set(edge,new Set());lanes.get(edge).add(lane);
 }
 for(const s of strands){
  const points=[s.incoming,lerp(s.incoming,s.guide[0],.8)];
  for(let i=1;i<s.guide.length;i++){
   const a=s.guide[i-1],b=s.guide[i],ak=key(a),bk=key(b),edge=[ak,bk].sort().join('|'),ordered=[...lanes.get(edge)].sort(),index=ordered.indexOf(s.id+':'+(ak<bk?'forward':'reverse'));
   const width=Math.ceil(Math.sqrt(ordered.length)),u=index%width-(width-1)/2,v=Math.floor(index/width)-(Math.ceil(ordered.length/width)-1)/2;
   const direction=normalize(ak<bk?b.map((x,j)=>x-a[j]):a.map((x,j)=>x-b[j]));
   const side=normalize(cross(direction,Math.abs(direction[2])<.8?[0,0,1]:[0,1,0])),up=cross(direction,side);
   for(let n=0;n<=8;n++){
    const t=n/8,taper=Math.min(1,t*5,(1-t)*5);
    points.push(lerp(a,b,t).map((x,j)=>x+.057*taper*(u*side[j]+v*up[j])));
   }
  }
  points.push(lerp(s.outgoing,s.guide.at(-1),.8),s.outgoing);
  s.points=points.filter((p,i)=>i===0||dist2(p,points[i-1])>1e-18);
  s.incomingPoints=s.points.slice(0,2);s.outgoingPoints=s.points.slice(-2);
 }
 return {coordinateSpace:'world3',tubeRadius:.018,tubeSegmentsPerPoint:1.5,radialSegments:8,strands,stripeReferencePoints:[top.point,top.point.map((x,i)=>x+(i===1?1:0))],
  input:strands.map(s=>s.id),output:strands.map(s=>s.id),
  audit:{strands:strands.length,incomingBundles:1,outgoingBundles:1,endpointBijection:true,branchSegments:0,
   routeKind:'native simplex-edge circuits transported with copy labels; shortest shared-edge contact walks between copies',entryCell:top.id,exitCell:bottom.id}};
}
