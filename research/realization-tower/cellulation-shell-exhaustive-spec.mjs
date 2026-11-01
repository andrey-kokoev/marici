import {buildShellFace} from './cellulation-shell.mjs';
import {packCellulation} from './cellulation-geometry.mjs';
import {buildShellWitnessPlan} from './cellulation-shell-witness.mjs';
import {advanceShellWitnessState} from './cellulation-shell-confluence.mjs';
const faceKey=ps=>ps.map(p=>p.join(',')).sort().join('|');
const gcd=(a,b)=>b?gcd(b,a%b):Math.abs(a);
function primitive(v){const g=v.reduce((a,b)=>gcd(a,b),0);if(!g)throw Error('Zero witness normal');return v.map(x=>x/g);}
const phase=t=>['draw-arrow','reuse-arrow'].includes(t)?'arrow':t;

export function freezeShellEventSpecification(base,initial){
 const size=base.cellSize,lattice=p=>p.map(x=>Math.round(x*Math.SQRT2/size)),point=p=>lattice(p).join(','),programs=[],allCells=new Map(base.cells.map(c=>[c.id,c])),plans=[],boundary=new Map();
 for(let index=0;index<4;index++){
  const shellFace=buildShellFace(base,index),model={...packCellulation([...base.cells,...shellFace.newCells],'cellulation-step'),cellSize:size,step:23,previous:base,shellFace},plan=buildShellWitnessPlan(model,initial);
  if(!plan.complete)throw Error('Cannot freeze an unsupported source protocol');
  plans.push({index,model,plan});for(const c of shellFace.newCells)allCells.set(c.id,c);
  for(const r of shellFace.boundaryReadings){const k=faceKey(r.vertices.map(lattice)),old=boundary.get(k);if(old&&old.colour!==r.colour)throw Error('Conflicting source boundary colors');boundary.set(k,r);}
 }
 const cells=[...allCells.values()].map(c=>({id:c.id,kind:c.kind,vertices:c.vertices.map(point),faces:c.faces.map(f=>faceKey(f.map(lattice)))})),tetrahedra=cells.filter(c=>c.kind==='tetrahedron');
 for(const {index,model,plan} of plans){
  for(const cell of model.shellFace.newCells){
   const es=plan.events.filter(e=>e.cell===cell.id),id=`face:${index}/${cell.id}`,vertices=cell.vertices.map(lattice),normal=p=>primitive(lattice(p).map((x,i)=>x*vertices.length-vertices.reduce((sum,q)=>sum+q[i],0)));
   const opId=i=>`${id}/action:${i}`,ops=es.map((e,i)=>({id:opId(i),phase:phase(e.type),requires:i?[opId(i-1)]:[],requiresDots:[],requiresSolid:[],requiresCells:[],requiresFaces:[],effects:[]}));
   const propose=(i,p,colour)=>ops[i].effects.push({type:'propose',key:point(p),colour,normal:normal(p)});
   const solidify=(i,points)=>{ops[i].requiresDots=points.map(point);ops[i].effects.push(...points.map(p=>({type:'solidify',key:point(p)})));};
   for(const [i,e] of es.entries())if(phase(e.type)==='arrow'){
    ops[i].requiresDots=[point(e.from)];ops[i].effects.push({type:'arrow',key:`${point(e.from)}>${point(e.to)}:${e.colour}`});
   }
   if(cell.kind==='tetrahedron'){
    const A=es[1].from,C=es[1].to,B=es[2].to,D=es[5].to,colour=es[1].colour;
    ops[0].requiresSolid=[point(A)];propose(0,C,0xffffff);propose(2,B,colour);propose(5,D,colour);
    ops[4].requires=[opId(1),opId(3)];ops[7].requires=[opId(4),opId(6)];
    solidify(8,[C]);ops[9].requires=[opId(4),opId(7),opId(8)];
    ops[11].requires=[opId(7),opId(10)];solidify(12,[B,D]);ops[13].requires=[opId(11),opId(12)];
   }else{
    const ring=es.slice(1,5).map(e=>e.from),opposite=es[1].to,center=[0,1,2].map(i=>cell.vertices.reduce((sum,p)=>sum+p[i],0)/6),shared=center.map((x,i)=>2*x-opposite[i]);
    const supportFaces=[[shared,ring[0],ring[1]],[shared,ring[2],ring[3]]].map(f=>faceKey(f.map(lattice)));
    ops[0].requiresCells=supportFaces.map(k=>{const parents=tetrahedra.filter(c=>c.faces.includes(k));if(parents.length!==1)throw Error('Ambiguous octahedron support');return parents[0].id;});
    ops[0].requiresSolid=[shared,...ring].map(point);propose(0,opposite,0xffffff);
    // Arrival order was a display schedule, not a dependency. All four can
    // proceed independently once the supported opposite candidate exists.
    for(let i=1;i<=4;i++)ops[i].requires=[opId(0)];
    ops[5].requires=[1,2,3,4].map(opId);solidify(6,[opposite]);ops[7].requires=[opId(5),opId(6)];
   }
   for(const [i,e] of es.entries())if(e.type==='fill-faces')for(const key of e.faces){const reading=boundary.get(key);ops[i].effects.push({type:'face',key,colour:reading?.colour??0xffffff,source:reading?.source??'neutral-internal-scaffold'});}
   const commit=ops.at(-1);commit.requiresFaces=cell.faces.map(f=>faceKey(f.map(lattice)));commit.requiresSolid=cell.vertices.map(point);commit.effects.push({type:'commit'});
   programs.push({id,cell:cell.id,face:index,kind:cell.kind,primaryColour:cell.kind==='tetrahedron'?es[1].colour:0xffffff,operations:ops});
  }
 }
 const dotNormal=a=>{const nonzero=a.normal.filter(x=>Math.abs(x)>1e-8),min=Math.min(...nonzero.map(Math.abs)),v=a.normal.map(x=>Math.round(x/min));if(a.normal.some((x,i)=>Math.abs(x/min-v[i])>1e-7))throw Error('Initial normal has no admitted exact direction representation');return primitive(v);};
 const spec={schema:'cellulation-event-state-v1',sourceStep:22,cellSize:size,policy:{arrowIdentity:'directed endpoints plus color; set union; reverse is distinct',dotSelection:'retained boundary fixed; otherwise first proposal wins; all competing claims retained',cellSelection:'first enabled face program claims a shared cell; competing programs cannot both construct it',faceSelection:'retained faces fixed; otherwise global seed-plane boundary reading; neutral internal faces',abstraction:'Discrete semantic completion events; continuous interpolation and holds do not admit witnesses',normalEncoding:'Primitive integer direction, normalized only for display',interleavings:'All enabled operations across all cells/faces; tetrahedral source ordering fixed; four octahedral arrivals independent',partialOrderReduction:'none'},initial:{dots:initial.anchors.filter(a=>a.solid).map(a=>({key:point(a.point),id:a.id,colour:a.colour,normal:dotNormal(a),solid:true})),arrows:[...new Set(initial.arrows.map(a=>`${point(a.from)}>${point(a.to)}:${a.colour??a.color}`))].sort(),faces:[...new Set(base.faces.map(f=>faceKey(f.vertices.map(lattice))))].map(key=>({key,colour:null,source:'retained-boundary'})),cells:initial.cells.map(c=>c.id)},cells,targets:[...new Set(programs.map(p=>p.cell))],programs};
 validateShellEventSpecification(spec);return spec;
}
export function validateShellEventSpecification(spec){
 for(const p of spec.programs){
  if(!['tetrahedron','octahedron'].includes(p.kind))throw Error('Unknown source cell kind');
  const ops=p.operations,tetra=p.kind==='tetrahedron',expected=tetra?['propose-target','arrow','arrow','arrow','first-return-witness','arrow','arrow','second-return-witness','witness-dots','fill-faces','arrow','connect-candidates-witness','witness-dots','fill-faces','commit-cell']:['propose-opposite','arrow','arrow','arrow','arrow','four-arrival-witness','witness-dots','fill-faces','commit-cell'];
  if(ops.length!==expected.length||ops.some((o,i)=>o.phase!==expected[i]))throw Error('Source protocol phase mismatch');
  const need=(i,indices)=>{if(indices.some(j=>!ops[i].requires.includes(ops[j].id)))throw Error('Dropped source witness prerequisite');};
  if(tetra){for(let i=1;i<ops.length;i++)need(i,[i-1]);need(4,[1,3]);need(7,[4,6]);need(9,[4,7,8]);need(11,[7,10]);need(13,[11,12]);if(ops[0].requiresSolid.length!==1)throw Error('Missing tetrahedral source');}
  else{for(let i=1;i<=4;i++){need(i,[0]);if(ops[i].requires.length!==1)throw Error('Artificial octahedral arrival ordering');}need(5,[1,2,3,4]);need(6,[5]);need(7,[5,6]);need(8,[7]);if(ops[0].requiresCells.length!==2||ops[0].requiresSolid.length!==5)throw Error('Missing octahedral supports');}
  const c=spec.cells.find(c=>c.id===p.cell),commit=ops.at(-1);if(c.faces.some(f=>!commit.requiresFaces.includes(f))||c.vertices.some(v=>!commit.requiresSolid.includes(v)))throw Error('Incomplete cell commitment prerequisites');
  const parse=k=>k.split(',').map(Number),sameSet=(a,b)=>JSON.stringify([...a].sort())===JSON.stringify([...b].sort()),face=ps=>ps.sort().join('|');
  const dependencies=tetra?[[],[0],[1],[2],[1,3],[4],[5],[4,6],[7],[4,7,8],[9],[7,10],[11],[11,12],[13]]:[[],[0],[0],[0],[0],[1,2,3,4],[5],[5,6],[7]];
  const effects=tetra?[['propose'],['arrow'],['arrow','propose'],['arrow'],[],['arrow','propose'],['arrow'],[],['solidify'],['face','face'],['arrow'],[],['solidify','solidify'],['face','face'],['commit']]:[['propose'],['arrow'],['arrow'],['arrow'],['arrow'],[],['solidify'],Array(8).fill('face'),['commit']];
  for(const [i,o] of ops.entries()){
   if(!sameSet(o.requires,dependencies[i].map(j=>ops[j].id)))throw Error('Artificial or missing operation dependency');
   if(!sameSet(o.effects.map(e=>e.type),effects[i]))throw Error('Unexpected protocol effects');
   if((tetra||i!==0)&&o.requiresCells.length)throw Error('Artificial cell scheduling gate');
   if(i!==0&&i!==ops.length-1&&o.requiresSolid.length)throw Error('Artificial dot scheduling gate');
   if(i!==ops.length-1&&o.requiresFaces.length)throw Error('Artificial face scheduling gate');
   if(!['arrow','witness-dots'].includes(o.phase)&&o.requiresDots.length)throw Error('Artificial candidate scheduling gate');
  }
  if(!sameSet(commit.requiresFaces,c.faces)||!sameSet(commit.requiresSolid,c.vertices))throw Error('Artificial commitment gate');
  const arrow=i=>{const effects=ops[i].effects.filter(e=>e.type==='arrow');if(effects.length!==1)throw Error('Missing directed arrow');const [ends,colour]=effects[0].key.split(':'),[from,to]=ends.split('>');return {from,to,colour:Number(colour)};};
  for(const [i,o] of ops.entries())if(o.phase==='arrow'){
   const a=arrow(i),v=parse(a.from),w=parse(a.to);if(!c.vertices.includes(a.from)||!c.vertices.includes(a.to)||v.reduce((sum,x,j)=>sum+(x-w[j])**2,0)!==2||!sameSet(o.requiresDots,[a.from]))throw Error('Invalid directed cell edge');
   if(a.colour!==(tetra&&i===1?p.primaryColour:0xffffff))throw Error('Wrong protocol arrow color');
  }
  const proposal=(i,key,colour)=>{const e=ops[i].effects.find(e=>e.type==='propose');if(!e||e.key!==key||e.colour!==colour)throw Error('Wrong candidate proposal');const vertices=c.vertices.map(parse),normal=primitive(parse(key).map((x,j)=>x*vertices.length-vertices.reduce((s,v)=>s+v[j],0)));if(JSON.stringify(normal)!==JSON.stringify(e.normal))throw Error('Wrong candidate normal');};
  const fills=(i,keys)=>{if(!sameSet(ops[i].effects.filter(e=>e.type==='face').map(e=>e.key),keys))throw Error('Wrong witnessed faces');};
  const solids=(i,keys)=>{if(!sameSet(ops[i].effects.filter(e=>e.type==='solidify').map(e=>e.key),keys)||!sameSet(ops[i].requiresDots,keys))throw Error('Wrong dot witnesses');};
  if(tetra){
   const main=arrow(1),r1=arrow(2),r2=arrow(3),s1=arrow(5),s2=arrow(6),last=arrow(10),A=main.from,C=main.to,B=r1.to,D=s1.to;
   if(r1.from!==C||r2.from!==B||r2.to!==A||s1.from!==A||s2.from!==D||s2.to!==C||last.from!==B||last.to!==D||!ops[0].requiresSolid.includes(A))throw Error('Broken source return paths');
   proposal(0,C,0xffffff);proposal(2,B,p.primaryColour);proposal(5,D,p.primaryColour);solids(8,[C]);solids(12,[B,D]);fills(9,[face([A,C,B]),face([A,D,C])]);fills(13,[face([A,B,D]),face([B,C,D])]);
  }else{
   const arrivals=[1,2,3,4].map(arrow),target=arrivals[0].to,ring=arrivals.map(a=>a.from),shared=c.vertices.find(k=>k!==target&&!ring.includes(k));
   if(new Set(ring).size!==4||arrivals.some(a=>a.to!==target)||!sameSet(ops[0].requiresSolid,[shared,...ring]))throw Error('Broken four-arrival witness');
   const supports=[face([shared,ring[0],ring[1]]),face([shared,ring[2],ring[3]])];
   if(supports.some(k=>!ops[0].requiresCells.some(id=>spec.cells.find(c=>c.id===id)?.faces.includes(k))))throw Error('Incorrect support tetrahedra');
   proposal(0,target,0xffffff);solids(6,[target]);fills(7,c.faces);
  }
 }
 return true;
}
export function shellGuideTrace(base,initial,{faceOrder=[0,1,2,3],swapFirstFaceCells=false}={}){
 let model=base,state=initial;const trace=[],cellOrders=[];
 for(const index of faceOrder){
  let shellFace=buildShellFace(model,index),next={...packCellulation([...model.cells,...shellFace.newCells],'cellulation-step'),step:model.step+1,cellSize:model.cellSize,previous:model,shellFace};
  if(swapFirstFaceCells&&index===0){const p=buildShellWitnessPlan(next,state),order=p.cells.map(c=>c.cell);[order[1],order[2]]=[order[2],order[1]];next={...next,shellFace:{...shellFace,newCells:order}};}
  const plan=buildShellWitnessPlan(next,state);if(!plan.complete)throw Error('Blocked guide');
  for(const c of plan.cells){const events=plan.events.filter(e=>e.cell===c.cell.id);trace.push(...events.map((_,i)=>`face:${index}/${c.cell.id}/action:${i}`));}
  cellOrders.push(plan.cells.map(c=>c.cell.id));state=advanceShellWitnessState(state,plan);model=next;
 }
 return {trace,cellOrders,finalState:state};
}
