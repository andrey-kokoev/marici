import {probePECoupledNRouting} from './pe-coupled-n-routing.mjs';
// Four three-element port orbits under the distinguished face's C3 stabilizer.
export function enumerateThreefoldPortMatchings(){
 const rotate=i=>3*Math.floor(i/3)+(i+1)%3,m=Array(12).fill(-1);let total=0,threefold=0,fixedCompanion=0;
 function visit(){const a=m.indexOf(-1);if(a<0){total++;if(!m.every((b,i)=>m[rotate(i)]===rotate(b)))return;threefold++;if([0,1,2].every(i=>m[6+i]===9+i))fixedCompanion++;return;}for(let b=a+1;b<12;b++)if(m[b]<0){m[a]=b;m[b]=a;visit();m[a]=-1;m[b]=-1;}}
 visit();return {totalReversibleMatchings:total,threefoldMatchings:threefold,withCompanionStrandsFixed:fixedCompanion,nontrivialWithCompanionFixed:fixedCompanion-1};
}
export function falsifyRoutingUniqueness(){
 const policies=['cyclic','reverse','vacancy-reversed','occupied-reversed','occupied-only','vacancy-only','both-triplets','equator-reversed'],results=policies.map(routingPolicy=>probePECoupledNRouting(3,2,{routingPolicy}).audit);
 let rejectedControl;try{probePECoupledNRouting(3,2,{routingPolicy:'both-triplets-odd'});throw Error('Invalid control unexpectedly admitted');}catch(e){if(!e.message.includes('broke P/E geometric duality'))throw e;rejectedControl=e.message;}
 return {conjecture:'Nontrivial reversible, C3-symmetric, geometrically P/E-dual occupancy-driven N port routing forces 126 open response pairs at edge 7.',verdict:'falsified',matchings:enumerateThreefoldPortMatchings(),results,rejectedControl,scope:'Counterexamples preserve checked geometric P/E duality. They need not satisfy additional unasserted face-only coupling or fixed-geometry charge-conjugation laws. Viewer reference policy remains cyclic.'};
}
