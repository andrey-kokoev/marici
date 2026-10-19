// Three equivalent discrete realization generators. No face-navigation state.
export const realizationBasis=[[1,0,0],[.5,Math.sqrt(3)/2,0],[.5,Math.sqrt(3)/6,Math.sqrt(2/3)]];
// Underlying empty space: one unsubdivided closed 3-simplex, not an edgewise lattice.
export function makeSimplexSpace(origin=[0,0,0]) {
  const corners=[[0,0,0],...realizationBasis];
  const center=corners.reduce((s,p)=>s.map((x,i)=>x+p[i]/4),[0,0,0]);
  const vertices=corners.map(p=>p.map((x,i)=>origin[i]+6*(x-center[i])));
  return {vertices,edges:[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]],
    faces:[[0,2,1],[0,1,3],[0,3,2],[1,2,3]],cells:[[0,1,2,3]]};
}
export const carrierModes=['none','proton','neutron','electron','all'];
const add=(a,b)=>a.map((x,i)=>x+b[i]),sub=(a,b)=>a.map((x,i)=>x-b[i]);
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
const unit=a=>a.map(x=>x/Math.hypot(...a));
export const addressKey=a=>a.join(',');
export function worldPoint(address) {return realizationBasis.reduce((sum,b,i)=>sum.map((x,j)=>x+address[i]*b[j]),[0,0,0]);}
export function frameAt(address,assignment='MMC') {
  if(!Array.isArray(address)||address.length!==3||address.some(x=>!Number.isInteger(x)))throw RangeError('Realization address must have three integer coordinates');
  if(!['MMC','CCM'].includes(assignment))throw RangeError('Reference assignment must be MMC or CCM');
  const grade=address.reduce((s,x)=>s+x,0),angle=grade*Math.PI/3;
  const normal=unit(realizationBasis.reduce(add,[0,0,0]));
  const raw=[sub(realizationBasis[1],realizationBasis[2]),sub(realizationBasis[2],realizationBasis[0]),sub(realizationBasis[0],realizationBasis[1])];
  const roles=grade%2===0?assignment:(assignment==='MMC'?'CCM':'MMC');
  const axes=raw.map((a,i)=>({id:i,role:roles[i],direction:a.map((x,j)=>x*Math.cos(angle)+cross(normal,a)[j]*Math.sin(angle)+normal[j]*dot(normal,a)*(1-Math.cos(angle)))}));
  return {address:[...address],origin:worldPoint(address),grade,angleDegrees:grade*60,roles,axes,normal};
}
export function makeRealizationSpace({address=[0,0,0],extent=2,assignment='MMC',carrier='none'}={}) {
  const frame=frameAt(address,assignment);
  if(!Number.isInteger(extent)||extent<1||extent>4)throw RangeError('Lattice extent must be 1..4');
  if(!carrierModes.includes(carrier))throw RangeError('Unknown carrier selection');
  const nodes=[],lookup=new Map();
  for(let i=-extent;i<=extent;i++)for(let j=-extent;j<=extent;j++)for(let k=-extent;k<=extent;k++) {
    const a=add(address,[i,j,k]),node={id:addressKey(a),address:a,point:worldPoint(a)};lookup.set(node.id,nodes.length);nodes.push(node);
  }
  const edges=[],deltas=[[1,0,0],[0,1,0],[0,0,1],[1,-1,0],[0,1,-1],[-1,0,1]];
  for(const node of nodes)for(const delta of deltas){const other=lookup.get(addressKey(add(node.address,delta)));if(other!==undefined)edges.push([lookup.get(node.id),other]);}
  const offsets={C0:[0,0,0],M0:[1,0,0],C1:[0,1,0],M1:[0,0,1],C2:[1,1,0],M2:[0,1,1]};
  const definitions=[
    {id:'proton',symbol:'P',signature:'CMC[M]',names:['C0','M0','C1','M1'],color:0x6baec8},
    {id:'neutron',symbol:'N',signature:'MCM[C]',names:['M0','C1','M1','C2'],color:0xd7ae77},
    {id:'electron',symbol:'E',signature:'MCC[M]',names:['M1','C1','C2','M2'],color:0xf19ad0},
  ];
  const bodies=definitions.filter(body=>carrier==='all'||carrier===body.id),used=[...new Set(bodies.flatMap(body=>body.names))];
  const bindings=Object.fromEntries(used.map(name=>[name,addressKey(add(address,offsets[name]))]));
  const points=Object.fromEntries(used.map(name=>[name,nodes[lookup.get(bindings[name])].point]));
  return {space:makeSimplexSpace(frame.origin),basis:realizationBasis,frame,nodes,edges,carriers:{mode:carrier,bodies,bindings,points},
    scope:'Three discrete realization axes with 60-degree signed M/C frame increments; carrier incidence bound to lattice nodes, not a derived physical particle law.'};
}
