import {packCellulation} from './cellulation-geometry.mjs';
const key=points=>points.map(p=>p.map(x=>Number(x.toFixed(8))).join(',')).sort().join('|');
export function buildOctahedralBridge(previous,id='oct:between-tetrahedra'){
 const [a,b]=previous.cells,shared=[...previous.repeat.origin];
 // Cyclic equator: the four red vertices of the two completed tetrahedra.
 const ring=[a.vertices[1],a.vertices[3],b.vertices[3],b.vertices[1]].map(p=>[...p]);
 const center=[0,1,2].map(i=>ring.reduce((sum,p)=>sum+p[i]/4,0)),opposite=center.map((x,i)=>2*x-shared[i]);
 const faces=ring.flatMap((p,i)=>{const next=ring[(i+1)%4];return [[shared,p,next],[opposite,next,p]];});
 const cell={id,kind:'octahedron',vertices:[shared,opposite,...ring],faces};
 const full=packCellulation([cell],'cellulation-step'),oldFaces=new Set(previous.faces.map(f=>key(f.vertices))),oldEdges=new Set(previous.edges.map(e=>key(e.vertices)));
 // Shared tetrahedral faces/edges are already drawn by the retained construction.
 const scaffold={...full,cellSize:previous.cellSize,faces:full.faces.filter(f=>!oldFaces.has(key(f.vertices))),edges:full.edges.filter(e=>!oldEdges.has(key(e.vertices)))};
 return {cell,shared,center,opposite,ring,scaffold,arrows:ring.map(from=>({from,to:[...opposite],colour:0xffffff}))};
}
export const octahedronTiming=Object.freeze({hold:600,edge:1000,fill:350,total:4950});
const clamp=x=>Math.max(0,Math.min(1,x));
export function octahedronAt(elapsed){
 const {hold,edge,fill,total}=octahedronTiming;
 const progress=[0,1,2,3].map(i=>clamp((elapsed-hold-i*edge)/edge)),fillProgress=clamp((elapsed-hold-4*edge)/fill);
 return {phase:elapsed<hold?'opposite-vertex':progress[3]<1?'growing-arrows':fillProgress<1?'closing-octahedron':'complete',progress,arrived:progress.filter(p=>p===1).length,fillProgress,active:elapsed<total};
}
