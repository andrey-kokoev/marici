// Layer-first construction around an upright seed in an oppositely oriented
// regular tetrahedral envelope. Signed structural coordinates sum to one.
// One item is a regular tetrahedron or a four-tetrahedron octahedral assembly.
const units=Array.from({length:4},(_,i)=>Array.from({length:4},(_,j)=>Number(i===j)));
export const primitives={regular:{vertices:units},splitOctahedron:{vertices:[[1,0,1,0],[0,1,0,1],[1,1,0,0],[1,0,0,1]]}};
function compositions(total,min=0){
 const result=[];
 for(let a=min;a<=total;a++)for(let b=min;b<=total-a;b++)for(let c=min;c<=total-a-b;c++){
  const d=total-a-b-c;if(d>=min)result.push([a,b,c,d]);
 }
 return result;
}
export function assembleComponents(n=7){
 if(n!==7)throw RangeError('This construction has four prescribed layers at resolution 7');
 const components=[],groups=[],items=[],layers=[];
 function emitItem(layer,kind,origin,inverted=false){
  // Orient the entire coherent assembly around the upright unit simplex.
  // No boundary cells are removed, relocated, or replaced by extra caps.
  if(kind==='octahedron')origin=origin.map(x=>1-x);
  else {origin=origin.map(x=>2-x);inverted=!inverted;}
  const id=`layer${layer}-item${layers[layer].items.length+1}`;
  const item={id,layer,kind,origin:[...origin],inverted,children:[]};
  const parent=kind==='octahedron'?groups.length:null;
  function instance(primitive,transform){
   const index=components.length;
   components.push({id:index,itemId:id,layer,primitive,parent,origin:[...origin],transform,
    addresses:primitives[primitive].vertices.map(p=>origin.map((x,i)=>x+(transform.kind==='inversion'?-p[i]:p[transform.permutation[i]])))});
   item.children.push(index);
  }
  if(kind==='tetrahedron')instance('regular',inverted?{kind:'inversion'}:{kind:'permutation',permutation:[0,1,2,3]});
  else {
   for(const permutation of [[0,1,2,3],[3,0,1,2],[2,3,0,1],[1,2,3,0]])instance('splitOctahedron',{kind:'permutation',permutation});
   groups.push({id:parent,itemId:id,kind,children:[...item.children],origin:[...origin]});
  }
  items.push(item);layers[layer].items.push(item);
 }
 for(let layer=0;layer<4;layer++){
  layers.push({id:`layer${layer}`,items:[]});
  if(layer===0)emitItem(layer,'tetrahedron',[2,2,2,2],true);
  if(layer===1)for(const origin of compositions(5,1))emitItem(layer,'octahedron',origin);
  if(layer===2){
   for(const origin of compositions(6,1))emitItem(layer,'tetrahedron',origin);
   for(const origin of compositions(8,1).filter(a=>Math.min(...a)===1))emitItem(layer,'tetrahedron',origin,true);
  }
  if(layer===3){
   for(const origin of compositions(6).filter(a=>Math.min(...a)===0))emitItem(layer,'tetrahedron',origin);
   for(const origin of compositions(5).filter(a=>Math.min(...a)===0))emitItem(layer,'octahedron',origin);
  }
 }
 const expected=[1,4,44,126];
 if(layers.some((l,i)=>l.items.length!==expected[i]))throw Error('Invalid construction layer counts');
 return {primitives,components,groups,items,layers};
}
