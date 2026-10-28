import {worldPoint} from './normal-ray-model.mjs';
// Trial contract: disjoint adjacent PE pairs on each ring; complementary
// endpoint matching on each cable. Geometric proximity selects among free ports.
export function routeEpPairs(structures,square,bodies,internalLinks){
 const byId=new Map(bodies.map(b=>[b.id,b])),ports=new Map(structures.map(s=>[s.id,[0,2,4].map(i=>({id:`${s.id}:pair:${i/2}`,nodes:s.nodeIds.slice(i,i+2),structure:s.id}))]));
 const squarePorts=[{id:'square:EP',nodes:[square[0],square[1]],structure:'square'},{id:'square:PE',nodes:[square[3],square[2]],structure:'square'}];
 const role=id=>byId.get(id).role,dist=(a,b)=>{const p=worldPoint(byId.get(a).point),q=worldPoint(byId.get(b).point);return p.reduce((s,x,i)=>s+(x-q[i])**2,0);};
 const matches=(a,b)=>a.nodes.map(from=>({from,to:b.nodes.find(to=>role(from)!==role(to))}));
 const cost=(a,b)=>matches(a,b).reduce((s,e)=>s+dist(e.from,e.to),0);
 const cables=[],links=[],degree=new Map(bodies.map(b=>[b.id,0]));
 for(const e of internalLinks){degree.set(e.from,degree.get(e.from)+1);degree.set(e.to,degree.get(e.to)+1);}
 function connect(a,b,interfaceId){
  const edges=matches(a,b);if(edges.some(e=>!e.to||degree.get(e.from)>=4||degree.get(e.to)>=4))throw Error('EP route exceeds port capacity');
  const id=`ep-cable:${cables.length}`;
  cables.push({id,interfaceId,fromPair:a.id,toPair:b.id,fromStructure:a.structure,toStructure:b.structure,cost:cost(a,b),endpoints:edges});
  for(const e of edges){links.push({...e,kind:'ep-coupling',cable:id});degree.set(e.from,degree.get(e.from)+1);degree.set(e.to,degree.get(e.to)+1);}
 }
 // Complete 3-by-2 module contacts; each pair is used at most once on this side.
 for(const [outerLayer,innerLayer] of [[1,2],[5,4]]){
  const outer=structures.filter(s=>s.layer===outerLayer),inner=structures.filter(s=>s.layer===innerLayer),used=new Set();
  const contacts=outer.flatMap(a=>inner.map(b=>({a,b,min:Math.min(...ports.get(a.id).flatMap(p=>ports.get(b.id).map(q=>cost(p,q))))}))).sort((a,b)=>a.min-b.min||a.a.id.localeCompare(b.a.id)||a.b.id.localeCompare(b.b.id));
  for(const {a,b} of contacts){const candidates=ports.get(a.id).flatMap(p=>ports.get(b.id).map(q=>({p,q,cost:cost(p,q)}))).filter(({p,q})=>!used.has(p.id)&&!used.has(q.id)).sort((a,b)=>a.cost-b.cost||a.p.id.localeCompare(b.p.id)||a.q.id.localeCompare(b.q.id));const {p,q}=candidates[0];connect(p,q,`${outerLayer}-${innerLayer}`);used.add(p.id);used.add(q.id);}
 }
 // Each inner module reaches one square pair. Each square pair receives one
 // cable from either side; its endpoints then have exactly four total links.
 for(const layer of [2,4]){
  const inner=structures.filter(s=>s.layer===layer),assignments=[[0,1],[1,0]].map(order=>{
   const chosen=inner.map((s,i)=>ports.get(s.id).map(p=>({p,q:squarePorts[order[i]],cost:cost(p,squarePorts[order[i]])})).sort((a,b)=>a.cost-b.cost||a.p.id.localeCompare(b.p.id))[0]);
   return {chosen,cost:chosen.reduce((s,c)=>s+c.cost,0)};
  }).sort((a,b)=>a.cost-b.cost);
  for(const {p,q} of assignments[0].chosen)connect(p,q,`${layer}-3`);
 }
 const all=[...internalLinks,...links],neighbors=new Map(bodies.map(b=>[b.id,[]]));for(const e of all){neighbors.get(e.from).push(e.to);neighbors.get(e.to).push(e.from);}
 function reachable(start,blocked=new Set()) {const seen=new Set(),queue=[start];while(queue.length){const id=queue.pop();if(seen.has(id)||blocked.has(id))continue;seen.add(id);queue.push(...neighbors.get(id).filter(n=>!seen.has(n)&&!blocked.has(n)));}return seen;}
 const first=structures.find(s=>s.layer===1).nodeIds[0],last=structures.filter(s=>s.layer===5).flatMap(s=>s.nodeIds),withoutSquare=reachable(first,new Set(square));
 return {links,audit:{hypothesis:'Directional EP-pair coupling',contract:'Nearest available disjoint ring pairs; complementary E↔P matching; no parent or interlayer face identification inferred',selection:'Deterministic greedy outer contacts and minimum-cost square-pair assignment; not a global optimum',cables,pairCableCount:cables.length,addedLinks:links.length,maxDegree:Math.max(...degree.values()),connectedNodes:reachable(first).size,totalNodes:bodies.length,centralSquareRequired:last.every(id=>!withoutSquare.has(id)),scope:'Static routing connectivity, not simulated dynamics or a physical circuit law'}};
}
