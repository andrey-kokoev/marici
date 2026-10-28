// Experimental coordinatewise law for three equal-width real fibers.
// This is a declared orthonormal reference metric, not a native field metric.
// All three modes remain stored at the destination; no scalar merging occurs.
export const fiberJunctionLaw=Object.freeze({id:'retained-common-contrast-v1',status:'trial',metric:'sum of squared real reference coordinates',contrastTurnDegrees:120});
function checkVectors(vectors,count){
 if(vectors.length!==count||!Array.isArray(vectors[0])||vectors[0].length===0||vectors.some(v=>!Array.isArray(v)||v.length!==vectors[0].length||v.some(x=>!Number.isFinite(x))))throw Error('Expected equal nonempty finite real fibers');
}
export function splitFiberJunction(inputs){
 checkVectors(inputs,3);const [a,b,c]=inputs;
 return {common:a.map((v,i)=>(v+b[i]+c[i])/Math.sqrt(3)),contrasts:[a.map((v,i)=>(v-b[i])/Math.sqrt(2)),a.map((v,i)=>(v+b[i]-2*c[i])/Math.sqrt(6))]};
}
export function joinFiberJunction(state){
 const {common:s,contrasts:[u,v]}=state;checkVectors([s,u,v],3);
 return [s.map((x,i)=>x/Math.sqrt(3)+u[i]/Math.sqrt(2)+v[i]/Math.sqrt(6)),s.map((x,i)=>x/Math.sqrt(3)-u[i]/Math.sqrt(2)+v[i]/Math.sqrt(6)),s.map((x,i)=>x/Math.sqrt(3)-2*v[i]/Math.sqrt(6))];
}
export function advanceFiberJunction(state,turn=2*Math.PI/3){
 const {common,contrasts:[u,v]}=state;checkVectors([common,u,v],3);if(!Number.isFinite(turn))throw Error('Expected finite turn');
 const c=Math.cos(turn),s=Math.sin(turn);
 return {common:[...common],contrasts:[u.map((x,i)=>c*x-s*v[i]),u.map((x,i)=>s*x+c*v[i])]};
}
export function fiberJunctionNorm(state){return [state.common,...state.contrasts].flat().reduce((s,x)=>s+x*x,0);}
