// Shared tetrahedral–octahedral lattice face convention. It depends on native
// triangle orientation, not a growth-rule assignment to its owning cell.
export function nativeFaceRole(vertices){
 const sum=vertices[0].reduce((s,_,i)=>s+Math.max(...vertices.map(v=>v[i])),0);
 if(sum!==2&&sum!==3)throw Error('Expected a native unit triangle in sum(q)=1');
 return sum===2?'proton':'electron';
}
