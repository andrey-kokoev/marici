import carriers from './helium-carriers.json' with {type:'json'};
export function heliumCarriers(distance=0.67){
  if(!Number.isFinite(distance)||distance<=0)throw new RangeError('positive distance required');
  return carriers.items.map(item=>({...item,positions:item.indices.map(m=>m.map(v=>(2*v-1)*Math.sqrt(3)*distance))}));
}
// Exact fixture from research/realization-tower/results/helium-role-test-v1.json.
// Coordinates are FCC indices, NOT particle labels.
export function heliumCandidate(distance=0.67) {
  if(!Number.isFinite(distance)||distance<=0)throw new RangeError('positive distance required');
  const indices=[[0,0,0],[2,0,0],[1,1,0],[1,0,1],[1,-1,0],[1,0,-1]];
  const wedges=Array.from({length:4},(_,i)=>[0,1,2+i,2+(i+1)%4]);
  const edges=[];
  for(let i=0;i<4;i++){edges.push([0,2+i],[1,2+i],[2+i,2+(i+1)%4]);}
  return {indices,positions:indices.map(m=>m.map(v=>(2*v-1)*Math.sqrt(3)*distance)),wedges,edges,axis:[0,1]};
}
