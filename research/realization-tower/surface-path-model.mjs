// A surface walk, not the previous inward normal-ray construction.
// Work on the outer face opposite V2: structural coordinate q1=2.
import {cells,seed,apex} from './normal-ray-model.mjs';
const key=p=>p.join(','),mean=ps=>ps[0].map((_,i)=>ps.reduce((s,p)=>s+p[i]/ps.length,0));
const shared=(a,b)=>a.filter(p=>b.some(q=>key(p)===key(q)));
export const surfaceCells=cells.map(c=>({...c,face:c.vertices.filter(p=>p[1]===2)})).filter(c=>c.face.length===3);
const byId=new Map(surfaceCells.map(c=>[c.id,c]));
const neighbors=new Map(surfaceCells.map(a=>[a.id,surfaceCells.filter(b=>b.id!==a.id&&shared(a.face,b.face).length===2).map(b=>b.id).sort((a,b)=>a-b)]));
// The first move must select a distinct primitive sharing ONLY the surface edge.
const first=neighbors.get(seed.id).filter(id=>shared(seed.vertices,byId.get(id).vertices).length===2);
if(first.length!==1)throw Error('Expected one edge-only first surface continuation');
// Fix a reproducible longest-distance direction within this finite surface.
// This is a display-path selection, not a law selecting an isotope.
const paths=new Map([[seed.id,[seed.id]],[first[0],[seed.id,first[0]]]]),queue=[first[0]];
for(let i=0;i<queue.length;i++)for(const next of neighbors.get(queue[i]))if(!paths.has(next)){paths.set(next,[...paths.get(queue[i]),next]);queue.push(next);}
const longest=[...paths.values()].sort((a,b)=>b.length-a.length||a.at(-1)-b.at(-1))[0];
if(longest.length<8)throw Error('Surface walk too short for seven steps');
export const surfacePath=longest;
export function surfaceProbe(k){
 if(!Number.isInteger(k)||k<1||k>7)throw Error('k must be 1..7');
 const traversed=surfacePath.slice(0,k+1),end=byId.get(traversed.at(-1)),start=byId.get(seed.id);
 const linePoints=[[...apex],mean(start.face)],crossings=[];
 for(let i=1;i<traversed.length;i++){
  const edge=shared(byId.get(traversed[i-1]).face,byId.get(traversed[i]).face);
  crossings.push(edge);linePoints.push(mean(edge),mean(byId.get(traversed[i]).face));
 }
 return {k,point:mean(end.face),polygons:[end.face],traversed,atStop:[end.id],linePoints,crossings,end,surfaceFace:'opposite V2',plane:{coordinate:1,value:2}};
}
export function surfaceProcedure(k,step){
 if(![1,2].includes(step))throw Error('Only two procedural steps are defined');
 const probe=surfaceProbe(k),end={...probe.end,outsideEnvelope:false};
 return {k,step,end,probe,assignments:step===1?[]:[
  {id:'entry',kind:'cell-role',cell:seed.id,role:'proton',boundary:'entry',point:mean(seed.vertices)},
  {id:'exit',kind:'cell-role',cell:end.id,role:k%2?'electron':'proton',boundary:'exit',point:mean(end.vertices)},
 ]};
}
