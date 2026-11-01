import {buildShellFace} from './cellulation-shell.mjs';
import {buildCrossEdge} from './cellulation-cross-edge.mjs';
import {buildClosingWhiteClone} from './cellulation-white-clone.mjs';
import {buildBlueClone} from './cellulation-blue-clone.mjs';
import {redExtensionCount} from './cellulation-cycle.mjs';
import {buildWhiteRepeat,whiteRepeatCount} from './cellulation-white-repeat.mjs';
import {buildOctahedralBridge} from './cellulation-octahedron.mjs';
import {translateCellulationStep} from './cellulation-repeat.mjs';
import {packCellulation} from './cellulation-geometry.mjs';
// Only the requested construction step is defined; later growth is not inferred.
export const cellulationSteps=Object.freeze([{step:1,label:'Single unit tetrahedron'},{step:2,label:'Mark top vertex'},{step:3,label:'Grow red arrow'},{step:4,label:'Witness the vertex'},{step:5,label:'Close the adjacent faces'},{step:6,label:'Connect the red candidates'},{step:7,label:'Repeat from the witnessed white dot'},{step:8,label:'Complete the octahedron'},{step:9,label:'Continue the red-arrow line'},{step:10,label:'Continue five more times'},{step:11,label:'White arrow from the terminal red turn · XYZ (−45°, −45°, 90°)'},{step:12,label:'Close the first white tetrahedron'},{step:13,label:'Continue the white arrow · XYZ (−45°, 45°, 90°)'},{step:14,label:'Close the first white side face'},{step:15,label:'Close the second white side face'},{step:16,label:'Close the two white side faces'},{step:17,label:'Connect the candidates; fill three dots, two faces and the rectangle'},{step:18,label:'Repeat steps 12–17 five times · XYZ (−45°, 45°, 90°)'},{step:19,label:'Attach the blue assembly · 180° roll about its long axis'},{step:20,label:'Close the loop with a reflected white bar'},{step:21,label:'Build the full white coherence bar · 718 → 178'},{step:22,label:'Connect the remaining corners · white bar 110 → 770'},{step:23,label:'Fill face 000–808–880'},{step:24,label:'Fill face 000–088–808'},{step:25,label:'Fill face 000–880–088'},{step:26,label:'Complete the shell · face 808–088–880'}]);
export function buildCellulationStep(step=1,cellSize=1){
 if(!cellulationSteps.some(s=>s.step===step))throw Error('Undefined cellulation step');
 if(!Number.isFinite(cellSize)||cellSize<.5||cellSize>2)throw Error('Cell size must be 0.5..2');
 if(step>=23){
  const previous=buildCellulationStep(step-1,cellSize),shellFace=buildShellFace(previous,step-23);
  return {...packCellulation([...previous.cells,...shellFace.newCells],'cellulation-step'),step,cellSize,previous,shellFace};
 }
 if(step===21||step===22){
  const previous=buildCellulationStep(step-1,cellSize),crossEdge=buildCrossEdge(previous,step===22);
  return {...packCellulation([...previous.cells,...crossEdge.newCells],'cellulation-step'),step,cellSize,previous,crossEdge};
 }
 if(step===20){
  const previous=buildCellulationStep(19,cellSize),closingWhiteClone=buildClosingWhiteClone(previous);
  return {...packCellulation([...previous.cells,...closingWhiteClone.newCells],'cellulation-step'),step,cellSize,previous,closingWhiteClone};
 }
 if(step===19){
  const previous=buildCellulationStep(18,cellSize),blueClone=buildBlueClone(previous);
  return {...packCellulation([...previous.cells,...blueClone.newCells],'cellulation-step'),step,cellSize,previous,blueClone};
 }
 if(step===18){
  const previous=buildCellulationStep(17,cellSize),templates=[];let cursor=previous;
  while(cursor.step>=13){templates.unshift(cursor);cursor=cursor.previous;}
  // Translated Step 12 is exactly the completed boundary tetrahedron of Step 17.
  const whiteRepeats=Array.from({length:whiteRepeatCount},(_,i)=>buildWhiteRepeat(templates,i,cellSize));
  return {...packCellulation([...previous.cells,...whiteRepeats.flatMap(c=>c.stages.at(-1).cells)],'cellulation-step'),step,cellSize,previous,whiteRepeats};
 }
 if(step===17){
  const previous=buildCellulationStep(16,cellSize),frame=terminalLatticeFrame(previous),latticeVertices=[[0,1,-1],[0,2,-2],[-1,2,-1],[-1,1,-2]].map(frame),vertices=latticeVertices.map(p=>p.map(x=>x*cellSize/Math.SQRT2));
  const solidClosure={arrow:{from:vertices[2],to:vertices[3],colour:0xffffff},faces:[[vertices[2],vertices[3],vertices[1]],[vertices[2],vertices[3],vertices[0]]],filledVertices:[vertices[2],vertices[3],vertices[1]],latticeFaces:[[latticeVertices[2],latticeVertices[3],latticeVertices[1]],[latticeVertices[2],latticeVertices[3],latticeVertices[0]]],filledLatticeVertices:[latticeVertices[2],latticeVertices[3],latticeVertices[1]]};
  const latticeRectangle=[[-1,0,-1],[-1,1,0],[-1,2,-1],[-1,1,-2]].map(frame),rectangle=latticeRectangle.map(p=>p.map(x=>x*cellSize/Math.SQRT2));
  solidClosure.latticeRectangle=latticeRectangle;
  solidClosure.faces.push([rectangle[0],rectangle[1],rectangle[2]],[rectangle[0],rectangle[2],rectangle[3]]);
  const cell={id:tetrahedronId(latticeVertices),kind:'tetrahedron',vertices,faces:vertices.map((_,i)=>vertices.filter((_,j)=>i!==j))};
  return {...packCellulation([...previous.cells,cell],'cellulation-step'),step,cellSize,previous,solidClosure};
 }
 if(step===16){
  const previous=buildCellulationStep(15,cellSize),frame=terminalLatticeFrame(previous);
  const sequentialFaces=[[[0,1,-1],[-1,1,0],[-1,2,-1]],[[0,1,-1],[-1,1,-2],[-1,0,-1]]].map(offsets=>{
   const latticeFace=offsets.map(frame);
   const face=latticeFace.map(p=>p.map(x=>x*cellSize/Math.SQRT2));
   return {latticeFace,arrow:{from:face[1],to:face[2],colour:0xffffff},faces:[face]};
  });
  return {...packCellulation(previous.cells,'cellulation-step'),step,cellSize,previous,sequentialFaces};
 }
 if(step===15){
  const previous=buildCellulationStep(14,cellSize),latticeFace=[[0,1,-1],[0,2,-2],[-1,1,-2]].map(terminalLatticeFrame(previous)),face=latticeFace.map(p=>p.map(x=>x*cellSize/Math.SQRT2));
  const triangleClosure={latticeFace,face,arrows:[{from:face[1],to:face[2],colour:0xffffff},{from:face[2],to:face[0],colour:0xffffff}]};
  return {...packCellulation(previous.cells,'cellulation-step'),step,cellSize,previous,triangleClosure};
 }
 if(step===14){
  const previous=buildCellulationStep(13,cellSize),latticeFace=[[0,1,-1],[0,2,-2],[-1,2,-1]].map(terminalLatticeFrame(previous)),face=latticeFace.map(p=>p.map(x=>x*cellSize/Math.SQRT2));
  const triangleClosure={latticeFace,face,arrows:[{from:face[1],to:face[2],colour:0xffffff,euler:[180,-45,180],eulerOrder:'XYZ'},{from:face[2],to:face[0],colour:0xffffff}]};
  return {...packCellulation(previous.cells,'cellulation-step'),step,cellSize,previous,triangleClosure};
 }
 if(step===13){
  const previous=buildCellulationStep(12,cellSize),frame=terminalLatticeFrame(previous),fromLattice=frame([0,1,-1]),toLattice=frame([0,2,-2]);
  const directedArrow={from:fromLattice.map(x=>x*cellSize/Math.SQRT2),to:toLattice.map(x=>x*cellSize/Math.SQRT2),colour:0xffffff,euler:[-45,45,90],eulerOrder:'XYZ',fromLattice,toLattice};
  return {...packCellulation(previous.cells,'cellulation-step'),step,cellSize,previous,directedArrow};
 }
 if(step===12){
  const previous=buildCellulationStep(11,cellSize),frame=terminalLatticeFrame(previous),latticeFace=[[0,0,0],[0,1,-1],[-1,1,0]].map(frame),face=latticeFace.map(p=>p.map(x=>x*cellSize/Math.SQRT2));
  const lastLattice=frame([-1,0,-1]),last=lastLattice.map(x=>x*cellSize/Math.SQRT2),vertices=[...face,last];
  const finish={arrow:{from:face[1],to:last,colour:0xffffff},faces:[[face[0],face[1],last],[face[1],face[2],last]],latticeFaces:[[latticeFace[0],latticeFace[1],lastLattice],[latticeFace[1],latticeFace[2],lastLattice]],filledVertex:face[1]};
  const faceClosure={arrow:{from:face[1],to:face[2],colour:0xffffff},faces:[face],latticeFace,finish};
  const cell={id:tetrahedronId([...latticeFace,lastLattice]),kind:'tetrahedron',vertices,faces:vertices.map((_,i)=>vertices.filter((_,j)=>i!==j))};
  return {...packCellulation([...previous.cells,cell],'cellulation-step'),step,cellSize,previous,faceClosure};
 }
 if(step===11){
  const previous=buildCellulationStep(10,cellSize),frame=terminalLatticeFrame(previous),fromLattice=frame([0,0,0]),toLattice=frame([0,1,-1]);
  // XYZ (-45°, -45°, 90°) maps +X to (0, 1, -1)/sqrt(2).
  const directedArrow={from:fromLattice.map(x=>x*cellSize/Math.SQRT2),to:toLattice.map(x=>x*cellSize/Math.SQRT2),colour:0xffffff,euler:[-45,-45,90],eulerOrder:'XYZ',fromLattice,toLattice};
  return {...packCellulation(previous.cells,'cellulation-step'),step,cellSize,previous,directedArrow};
 }
 if(step===10){
  const previous=buildCellulationStep(9,cellSize),cycles=[];let last=previous.cycle.first.at(-1);
  for(let i=0;i<redExtensionCount;i++){
   const cycle=buildContinuation(last,cellSize,`extension:${i}:`);
   cycles.push({...packCellulation(cycle.closed.cells,'cellulation-step'),step,cellSize,cycle});last=cycle.first.at(-1);
  }
  return {...packCellulation([...previous.cells,...cycles.flatMap(c=>c.cells)],'cellulation-step'),step,cellSize,previous,extensions:cycles};
 }
 if(step===9){
  const previous=buildCellulationStep(8,cellSize),cycle=buildContinuation(previous.previous.repeat.stages.at(-1),cellSize,'cycle:');
  return {...packCellulation([...previous.cells,...cycle.closed.cells],'cellulation-step'),step,cellSize,previous,cycle};
 }
 if(step===8){
  const previous=buildCellulationStep(7,cellSize),bridge=buildOctahedralBridge(previous);
  return {...packCellulation([...previous.cells,bridge.cell],'cellulation-step'),step,cellSize,previous,bridge};
 }
 if(step===7){
  const previous=buildCellulationStep(6,cellSize),origin=[...previous.proposedVertex];
  const stages=[2,3,4,5,6].map(s=>translateCellulationStep(buildCellulationStep(s,cellSize),origin));
  return {...packCellulation([...previous.cells,...stages[0].cells],'cellulation-step'),step,cellSize,previous,repeat:{origin,stages}};
 }
 const vertices=[[0,0,0],[0,1,1],[1,0,1],[1,1,0]].map(p=>p.map(x=>x*cellSize/Math.SQRT2));
 const witness=step>=4?{stage:Math.min(step,5),proposedVertex:[...vertices[2]],returnPath:(step===4?[vertices[2],vertices[1],vertices[0]]:[vertices[0],vertices[3],vertices[2]]).map(p=>[...p]),faces:step>=5?[[vertices[0],vertices[2],vertices[1]],[vertices[0],vertices[3],vertices[2]]].map(f=>f.map(p=>[...p])):[]}:null;
 if(witness){
  witness.turnMarker={id:step===4?'turn-first':'turn-second',name:step===4?'first red dot':'second red dot',point:[...vertices[step===4?1:3]]};
  witness.priorTurnMarkers=step>=5?[{id:'turn-first',name:'first red dot',point:[...vertices[1]]}]:[];
 }
 const arrows=step>=3?[{from:[...vertices[0]],to:[...vertices[2]],colour:0xff3030}]:[];
 if(step>=5)for(const [from,to] of [[2,1],[1,0]])arrows.push({from:[...vertices[from]],to:[...vertices[to]],colour:0xffffff});
 const completion=step===6?{arrow:{from:[...vertices[1]],to:[...vertices[3]],colour:0xffffff},faces:[[vertices[0],vertices[1],vertices[3]],[vertices[1],vertices[2],vertices[3]]].map(f=>f.map(p=>[...p]))}:null;
 const cell={id:'t:0,0,0',kind:'tetrahedron',vertices,faces:vertices.map((_,i)=>vertices.filter((_,j)=>i!==j))};
 return {...packCellulation([cell],'cellulation-step'),step,cellSize,witness,completion,proposedVertex:step>=3?[...vertices[2]]:null,markedVertex:step>=2?[...vertices[0]]:null,arrows};
}
// All white construction coordinates are offsets from the actual last red turn.
export function terminalLatticeFrame(model){
 let red=model;while(red.step>10)red=red.previous;
 const turn=red.extensions.at(-1).cycle.first.at(-1).witness.turnMarker.point;
 const anchor=turn.map(x=>Math.round(x*Math.SQRT2/red.cellSize));
 return offset=>offset.map((x,i)=>x+anchor[i]);
}
function tetrahedronId(vertices){return `t:${[0,1,2].map(i=>Math.min(...vertices.map(p=>p[i]))).join(',')}`;}
function buildContinuation(last,cellSize,prefix){
 const origin=[...last.proposedVertex],first=[2,3,4,5,6].map(s=>translateCellulationStep(buildCellulationStep(s,cellSize),origin,`${prefix}first:`));
 const pair={...packCellulation([...last.cells,...first[0].cells],'cellulation-step'),cellSize,repeat:{origin}};
 const bridge=buildOctahedralBridge(pair,`${prefix}oct:between-tetrahedra`);
 // Retain the preceding tetrahedron in the outer assembly; draw only new cells here.
 const closed={...packCellulation([...first[0].cells,bridge.cell],'cellulation-step'),step:8,cellSize,previous:first.at(-1),bridge};
 return {origin,first,closed};
}
export const cellulationStepEnvelope=[-1,1.7].flatMap(x=>[-1,1.7].flatMap(y=>[-1,1.7].map(z=>[x,y,z])));
