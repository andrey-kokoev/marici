import {trial, orientedVolume} from './carrier.mjs';

export const occupantModes=['none','proton','neutron','electron','all'];
// Axial basis vectors are separated by 120 degrees. A +60-degree turn sends
// (q,r) to (q-r,q). This is an integer lattice automorphism, not a nearest-node fit.
function rotateAddress([q,r],steps) {
  for(let n=((steps%6)+6)%6;n>0;n--)[q,r]=[q-r,q];
  return [q,r];
}

export function latticeCarriers(space,mode='none',level=0) {
  if(!occupantModes.includes(mode))throw new RangeError('Unknown occupant selection');
  const empty={mode,level,points:{},bindings:{},edges:[],bodies:[],sharedFaces:[],
    construction:'Three cells of an adjacent-realization triangular lattice prism',
    incidenceSource:'carrier.mjs#trial',geometrySource:'vacuum-model.mjs lattice nodes'};
  if(mode==='none')return {...empty,status:'empty'};
  const turns=space.parameters.turn/60;
  if(Math.abs(turns-Math.round(turns))>1e-10)return {...empty,status:'blocked',
    obstruction:'Prism sewing requires a multiple-of-60° lattice rotation; no vertices are snapped or interpolated.'};
  const min=space.frames[0].level,max=space.frames.at(-1).level;
  if(!Number.isInteger(level)||level<min||level>max)throw new RangeError('Carrier level is outside the displayed lattice');
  const lower=level===max?level-1:level,upper=lower+1;
  const lowerFrame=space.frames.find(frame=>frame.level===lower),upperFrame=space.frames.find(frame=>frame.level===upper);
  // A single elementary triangle and its exact counterpart in the adjacent
  // frame form a prism. Its pulling triangulation has precisely the old
  // P/N/E vertex-incidence chain, without using the old tetrahedron coordinates.
  const triangle=[[0,0],[1,0],[1,1]];
  const addresses={};
  ['C0','M0','C1'].forEach((name,i)=>{addresses[name]={level:lower,axial:triangle[i]};});
  ['M1','C2','M2'].forEach((name,i)=>{addresses[name]={level:upper,axial:rotateAddress(triangle[i],-Math.round(turns))};});
  const allPoints={},allBindings={};
  for(const [name,address] of Object.entries(addresses)) {
    const index=space.patch.sites.findIndex(([q,r])=>q===address.axial[0]&&r===address.axial[1]);
    if(index<0)return {...empty,status:'blocked',obstruction:'Required elementary-triangle node is absent from this patch.'};
    const frame=address.level===lower?lowerFrame:upperFrame;
    allPoints[name]=frame.points[index];
    allBindings[name]={level:address.level,q:address.axial[0],r:address.axial[1],siteIndex:index};
  }
  for(const [a,b] of [['C0','M1'],['M0','C2'],['C1','M2']]) {
    if(Math.hypot(allPoints[a][0]-allPoints[b][0],allPoints[a][2]-allPoints[b][2])>1e-9)
      return {...empty,status:'blocked',obstruction:'Adjacent lattice frames do not sew the declared prism.'};
  }
  const bodies=trial.bodies.filter(body=>mode==='all'||body.id===mode),names=[...new Set(bodies.flatMap(body=>body.nodes))];
  const points=Object.fromEntries(names.map(name=>[name,allPoints[name]]));
  const bindings=Object.fromEntries(names.map(name=>[name,allBindings[name]]));
  const edges=[...new Map(bodies.flatMap(body=>body.nodes.flatMap((a,i)=>body.nodes.slice(i+1).map(b=>[a,b].sort()))).map(edge=>[edge.join('|'),edge])).values()];
  return {...empty,status:'constructed',points,bindings,edges,
    bodies:bodies.map(body=>({...body,volume:Math.abs(orientedVolume(body.nodes,points))})),
    sharedFaces:trial.sharedFaces.filter(face=>bodies.filter(body=>face.every(name=>body.nodes.includes(name))).length===2),
    realizationLevels:[lower,upper],expectedCellVolume:Math.sqrt(3)*space.parameters.spacing/12,
    regular:false,embedding:'Vertices are exact references to lattice nodes; cells partition an elementary triangular prism. No centering, scaling or nearest-node snapping.'};
}
