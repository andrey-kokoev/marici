import {cells} from './normal-ray-model.mjs';
const key=p=>p.join(',');
const shared=(a,b)=>a.filter(p=>b.some(q=>key(p)===key(q)));

// Surface rule: two face-sharing PE/EP diamonds meet at a vertex. Each
// one- or two-triangle arc between them around that vertex is an N gap.
// This is distinct from the interior two-filled-face closure rule.
export function surfaceDiamondGaps(k,assignments,planes){
 const roles=new Map(assignments.map(a=>[a.cell,a.role])),witnesses=[],pending=new Map(),seen=new Set();
 const uniquePlanes=[...new Map(planes.map(p=>[`${p.coordinate}:${p.value}`,p])).values()];
 for(const {coordinate,value} of uniquePlanes){
  const faces=cells.filter(c=>c.vertices.every(p=>p[0]<=-5+k)).map(c=>({cell:c.id,vertices:c.vertices.filter(p=>p[coordinate]===value)})).filter(f=>f.vertices.length===3);
  const charged=faces.filter(f=>['electron','proton'].includes(roles.get(f.cell))),diamonds=[];
  for(let i=0;i<charged.length;i++)for(let j=i+1;j<charged.length;j++){
   const a=charged[i],b=charged[j];
   if(roles.get(a.cell)===roles.get(b.cell)||shared(a.vertices,b.vertices).length!==2||shared(cells[a.cell].vertices,cells[b.cell].vertices).length!==3)continue;
   diamonds.push({faces:[a,b],vertices:[...new Map([...a.vertices,...b.vertices].map(p=>[key(p),p])).values()]});
  }
  for(let i=0;i<diamonds.length;i++)for(let j=i+1;j<diamonds.length;j++){
   const a=diamonds[i],b=diamonds[j];
   if(a.faces.some(f=>b.faces.some(g=>f.cell===g.cell)))continue;
   const intersection=shared(a.vertices,b.vertices);if(intersection.length!==1)continue;
   const vertex=intersection[0],touches=f=>f.vertices.some(p=>key(p)===key(vertex)),star=faces.filter(touches);
   for(const start of a.faces.filter(touches))for(const end of b.faces.filter(touches)){
    function walk(path){
     const last=path.at(-1);
     if(last.cell===end.cell){
      if(path.length<3||path.length>4)return;
      const ids=path.map(f=>f.cell),signature=`${coordinate}:${value}:`+[ids.join(','),[...ids].reverse().join(',')].sort()[0];
      if(seen.has(signature))return;seen.add(signature);
      const gap=ids.slice(1,-1),fillCells=gap.filter(id=>!roles.has(id));if(!fillCells.length)return;
      const witness={coordinate,value,vertex,diamonds:[a.faces.map(f=>f.cell),b.faces.map(f=>f.cell)],path:ids,gap,fillCells};
      const witnessIndex=witnesses.length;witnesses.push(witness);
      for(const cell of fillCells){if(!pending.has(cell))pending.set(cell,{cell,witnesses:[]});pending.get(cell).witnesses.push(witnessIndex);}
      return;
     }
     if(path.length>=4)return;
     for(const next of star){
      if(path.some(f=>f.cell===next.cell)||shared(last.vertices,next.vertices).length!==2)continue;
      if(next.cell!==end.cell&&roles.has(next.cell)&&roles.get(next.cell)!=='neutron')continue;
      walk([...path,next]);
     }
    }
    walk([start]);
   }
  }
 }
 return {cells:[...pending.values()].sort((a,b)=>a.cell-b.cell),witnesses};
}
