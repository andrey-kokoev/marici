// Bounded, separate geometry-first and transport-first experiments.
// No particle-role assignments or native operation admission are made here.
import {selectPhaseAssembly,auditPhaseAssembly} from '../strominger/demos/particle-overlap-tetrahedron/phase-assembly-model.mjs';
import {phaseAdvanceWitness} from '../strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs';
const same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const key=p=>p.join(',');
const sorted=ps=>ps.map(key).sort();
const intersect=(a,b)=>a.filter(p=>b.some(q=>same(p,q)));
export const compose=(after,before)=>after.map(i=>before[i]);
export const inverse=p=>p.map((_,i)=>p.indexOf(i));
const identity=[0,1,2,3,4];
export function a4Cell(floor){
 if(floor.length!==5||floor.some(x=>!Number.isInteger(x)))throw Error('Five integer floor coordinates required');
 const q=-floor.reduce((s,x)=>s+x,0);if(q<1||q>4)throw Error('Empty full-dimensional chamber');
 const vertices=[];
 for(let mask=0;mask<32;mask++){
  const bits=Array.from({length:5},(_,i)=>(mask>>i)&1);
  if(bits.reduce((s,x)=>s+x,0)===q)vertices.push(bits.map((x,i)=>x+floor[i]));
 }
 const facets=[];
 for(let i=0;i<5;i++)for(const side of [0,1]){
  const vs=vertices.filter(v=>v[i]===floor[i]+side);
  if(vs.length>=4)facets.push({coordinate:i,side,vertices:vs});
 }
 return {floor:[...floor],q,vertices,facets};
}
export function closedAtTriangle(cells,triangle){
 if(!cells.length||triangle.length!==3||new Set(cells.map(c=>key(c.floor))).size!==cells.length)return false;
 if(cells.some(c=>!triangle.every(p=>c.vertices.some(q=>same(p,q)))))return false;
 const counts=new Map();
 for(const cell of cells)for(const face of cell.facets)if(triangle.every(p=>face.vertices.some(q=>same(p,q)))){
  const k=sorted(face.vertices).join('|');counts.set(k,(counts.get(k)??0)+1);
 }
 return counts.size>0&&[...counts.values()].every(n=>n===2);
}
export function geometryStudy(){
 const seed=a4Cell([0,0,-1,0,0]);
 const star=Array.from({length:4},(_,bits)=>a4Cell(seed.floor.map((x,i)=>x-(i<2?((bits>>i)&1):0))));
 const triangle=seed.vertices.filter(p=>p[0]===0&&p[1]===0);
 const completions=[];
 for(let bits=1;bits<16;bits++){
  const chosen=star.filter((_,i)=>bits&(1<<i));
  if(closedAtTriangle(chosen,triangle))completions.push(chosen.map(c=>c.floor));
 }
 const interfaces=[];
 for(let i=0;i<4;i++)for(let j=i+1;j<4;j++){
  const vertices=intersect(star[i].vertices,star[j].vertices);
  if(vertices.length>=4)interfaces.push({from:i,to:j,vertices});
 }
 // Mark the fifth coordinate: four base vertices, one apex, four apex edges.
 const base=seed.vertices.filter(v=>v[4]===0),apex=seed.vertices.find(v=>v[4]===1);
 const continuation=a4Cell(seed.floor.map((x,i)=>x-(i===4?1:0)));
 const complementFloor=k=>k.map(x=>-x-1);
 const dualSeed=a4Cell(complementFloor(seed.floor)),dualContinuation=a4Cell(complementFloor(continuation.floor));
 const dualityPass=[seed,continuation].every(c=>same(sorted(a4Cell(complementFloor(c.floor)).vertices),sorted(c.vertices.map(v=>v.map(x=>-x)))));
 const angles=star.map(c=>Math.acos((c.floor[0]===0?-1:1)*(c.floor[1]===0?-1:1)/4));
 return {status:'bounded-geometric-completion',triangle,star,interfaces,subsetCount:15,closedSubsets:completions,
  angleRadians:angles,angleSum:angles.reduce((s,x)=>s+x,0),
  markedInterface:{seed,continuation,sharedFacet:intersect(seed.vertices,continuation.vertices),apex,ports:base.map((endpoint,i)=>({id:`port-${i+1}`,apex,endpoint})),oppositeSection:continuation.vertices.filter(v=>v[4]===-1)},
  dual:{seed:dualSeed,continuation:dualContinuation,negationMatches:dualityPass},
  scope:'Unique ridge closure only inside the fixed four-cell A4 star. Four ports are marked apex-edge incidences, not derived particle transport. No global filling uniqueness or isotope assignment.'};
}
export function enumerateSimpleExitPaths(reference){
 const paths=[];
 function visit(chart,visited,edges){
  if(reference.charts[chart].species==='electron'){
   let permutation=[...identity],origin=0;
   for(const i of edges){const e=reference.edges[i];permutation=compose(e.permutation,permutation);origin+=e.phaseDelta;}
   paths.push({start:reference.root,end:chart,charts:[reference.root,...edges.map(i=>reference.edges[i].to)],edges,origin,permutation});return;
  }
  reference.edges.forEach((e,i)=>{if(e.from===chart&&!visited.has(e.to))visit(e.to,new Set([...visited,e.to]),[...edges,i]);});
 }
 visit(reference.root,new Set([reference.root]),[]);return paths;
}
export function transportStudy(){
 const r=selectPhaseAssembly('helium4');auditPhaseAssembly(r);
 const paths=enumerateSimpleExitPaths(r),pn=r.edges.find(e=>e.kind==='PN'),ne=r.edges.find(e=>e.kind==='NE');
 const nr=r.edges.find(e=>e.kind==='reader-phase-advance'&&r.charts[e.from].species==='neutron'&&r.charts[e.from].cell===r.charts[ne.from].cell);
 const ne2=r.edges.find(e=>e.kind==='NE'&&e.from===nr.to);
 if(nr.from!==ne.from||!ne2)throw Error('Cannot construct source-typed neutron/electron comparison square');
 const A=pn.permutation,C=ne.permutation,R=nr.permutation,D=compose(C,A);
 // Unique coefficient map completing X*C = C2*R. This is NOT an admitted event.
 const X=compose(ne2.permutation,compose(R,inverse(C)));
 let nativeReaderRejected=false;try{phaseAdvanceWitness(r.charts[ne.to],r.charts[ne2.to]);}catch{nativeReaderRejected=true;}
 const sameEndpointComparisons=[];
 for(let i=0;i<paths.length;i++)for(let j=i+1;j<paths.length;j++)if(paths[i].end===paths[j].end){
  const a=paths[i],b=paths[j];sameEndpointComparisons.push({fromPath:i,toPath:j,end:a.end,sameCoefficients:same(a.permutation,b.permutation),originDifference:b.origin-a.origin,
   coefficientComparison:compose(b.permutation,inverse(a.permutation)),nativeComparisonSupplied:false});
 }
 const cycleBack=r.edges.find(e=>e.from===nr.to&&e.to===nr.from&&e.kind==='reader-phase-advance');
 return {status:'coefficient-square-with-native-lift-gap',charts:r.charts,edges:r.edges,root:r.root,paths,sameEndpointComparisons,
  algebra:{A,C,R,D,D2:compose(D,D),DR:compose(D,R),RD:compose(R,D),commonFixedSlots:identity.filter(i=>[A,C,R].every(p=>p[i]===i))},
  electronSquare:{neutronSource:nr.from,neutronTarget:nr.to,electronSource:ne.to,electronTarget:ne2.to,edges:{NE: r.edges.indexOf(ne),reader:r.edges.indexOf(nr),nextNE:r.edges.indexOf(ne2)},candidateMap:X,
   left:compose(X,C),right:compose(ne2.permutation,R),phaseDelta:nr.phaseDelta,nativeReaderRejected,
   nativeDirectEdgeExists:r.edges.some(e=>e.from===ne.to&&e.to===ne2.to),
   coefficientInverseIsNotNativeReverse:true},
  readerRoundTrip:{start:nr.from,end:cycleBack.to,permutation:compose(cycleBack.permutation,R),originAdvance:nr.phaseDelta+cycleBack.phaseDelta},
  reverseElectronEdges:r.edges.filter(e=>r.charts[e.from].species==='electron').length,
  scope:'All chart-simple directed root-to-electron paths, not all walks. Coefficient comparisons retain separate histories and absolute origins. The derived electron map is not an admitted physical or native realization command. Five coefficient slots are not four transport ports.'};
}
