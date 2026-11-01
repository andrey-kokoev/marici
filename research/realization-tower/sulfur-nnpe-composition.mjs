// A graded cyclic-composition experiment, not an inferred nuclear assembly.
// NNPE = one N centre with N/P/E attachment labels. Each generator is assigned
// inventory (N:1,P:1); joining ports retains that inventory, not port counts.
export const nnpeDual={N:'N',P:'E',E:'P'};
export const nnpeStars=Array.from({length:16},(_,i)=>({id:`S${i+1}`,centre:'N',inventory:{N:1,P:1},ports:['N','P','E'].map(role=>({id:`S${i+1}:${role}`,starId:`S${i+1}`,role}))}));
export function buildNNPEComposition(joins=[]){
 const ports=new Map(nnpeStars.flatMap(s=>s.ports.map(p=>[p.id,p]))),used=new Set(),accepted=[],rejected=[];
 let components=nnpeStars.map(s=>({id:s.id,stars:[s.id],boundary:s.ports.map(p=>p.id),inventory:{...s.inventory},history:{star:s.id}}));
 for(const pair of joins){
  const [a,b]=Array.isArray(pair)?pair:[],pa=ports.get(a),pb=ports.get(b);
  let reason=!pa||!pb?'Unknown attachment port.':a===b?'Choose two different ports.':used.has(a)||used.has(b)?'A port is already joined.':nnpeDual[pa.role]!==pb.role?`${pa.role} joins ${nnpeDual[pa.role]}.`:null;
  const left=components.find(c=>c.boundary.includes(a)),right=components.find(c=>c.boundary.includes(b));
  if(!reason&&left===right)reason='That join would create a loop.';
  if(reason){rejected.push({pair,reason});continue;}
  const i=left.boundary.indexOf(a),j=right.boundary.indexOf(b);
  const composite={id:left.id,stars:[...left.stars,...right.stars],
   boundary:[...left.boundary.slice(0,i),...right.boundary.slice(j+1),...right.boundary.slice(0,j),...left.boundary.slice(i+1)],
   inventory:{N:left.inventory.N+right.inventory.N,P:left.inventory.P+right.inventory.P},
   history:{join:[a,b],left:left.history,right:right.history}};
  components=components.filter(c=>c!==left&&c!==right);components.push(composite);
  used.add(a);used.add(b);accepted.push([a,b]);
 }
 components.sort((a,b)=>Math.min(...a.stars.map(s=>Number(s.slice(1))))-Math.min(...b.stars.map(s=>Number(s.slice(1)))));
 const inventory=components.reduce((sum,c)=>({N:sum.N+c.inventory.N,P:sum.P+c.inventory.P}),{N:0,P:0});
 return {stars:nnpeStars,components,joins:accepted,rejected,usedPorts:[...used],inventory,
  audit:{generators:16,joins:accepted.length,components:components.length,boundaryPorts:48-2*accepted.length,inventory,target:{N:16,P:16},acyclic:true,historyRetained:true,counting:'additive generator grading; ports are attachment labels'}};
}
