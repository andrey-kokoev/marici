// Independent structural description of the existing same-orientation sector.
// Weights are weak compositions of 6 into four corner coordinates, not charges.
export const cellStructuralTypes=Object.freeze([
 {profile:'6,0,0,0',layer:0,stratum:'vertex',count:4,rule:'source'},
 {profile:'5,1,0,0',layer:1,stratum:'edge',count:12,rule:'target'},
 {profile:'4,2,0,0',layer:2,stratum:'edge',count:12,rule:'source'},
 {profile:'4,1,1,0',layer:2,stratum:'face',count:12,rule:'opposite'},
 {profile:'3,3,0,0',layer:3,stratum:'edge',count:6,rule:'midpoint-pair'},
 {profile:'3,2,1,0',layer:3,stratum:'face',count:24,rule:'nearest-other'},
 {profile:'3,1,1,1',layer:3,stratum:'interior',count:4,rule:'source'},
 {profile:'2,2,1,1',layer:4,stratum:'interior',count:6,rule:'P > N > E'},
 {profile:'2,2,2,0',layer:5,stratum:'face',count:4,rule:'opposite'},
].map(Object.freeze));
const roles=['proton','neutron','electron'],priority={proton:2,neutron:1,electron:0};
export function classifyCellStructure(weights,cornerRoles){
 if(!Array.isArray(weights)||weights.length!==4||Array.from(weights).some(x=>!Number.isInteger(x)||x<0)||weights.reduce((s,x)=>s+x,0)!==6)throw Error('Four nonnegative integer weights summing to 6 required');
 if(!Array.isArray(cornerRoles)||cornerRoles.length!==4||Array.from(cornerRoles).some(r=>!roles.includes(r)))throw Error('Four corner roles required');
 const profile=[...weights].sort((a,b)=>b-a).join(','),type=cellStructuralTypes.find(t=>t.profile===profile);
 if(!type)throw Error('Unclassified weight profile');
 const at=n=>weights.flatMap((w,i)=>w===n?[cornerRoles[i]]:[]);
 let role;
 switch(profile){
  case '6,0,0,0':role=at(6)[0];break;
  case '5,1,0,0':role=at(1)[0];break;
  case '4,2,0,0':role=at(4)[0];break;
  case '4,1,1,0':case '2,2,2,0':role=at(0)[0];break;
  case '3,2,1,0':role=at(2)[0];break;
  case '3,1,1,1':role=at(3)[0];break;
  case '2,2,1,1':role=at(2).reduce((a,b)=>priority[a]>=priority[b]?a:b);break;
  case '3,3,0,0':{
   const pair=at(3).sort().join('|');
   role={'electron|proton':'neutron','neutron|neutron':'electron','neutron|proton':'electron','electron|neutron':'proton'}[pair];
   if(!role)throw Error(`Midpoint rule is not defined for ${pair}`);break;
  }
 }
 return {...type,role};
}
export function compositionAddresses(){
 const out=[];for(let a=0;a<=6;a++)for(let b=0;b<=6-a;b++)for(let c=0;c<=6-a-b;c++)out.push([a,b,c,6-a-b-c]);return out;
}
