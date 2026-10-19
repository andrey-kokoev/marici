// A cell-local reflection complex, not a space-filling Euclidean tetrahedral lattice.
export const exitColors=[0xf6b75a,0x66cfff,0xf19ad0];
export const carrierModes=['none','proton','neutron','electron','all'];
const sub=(a,b)=>a.map((x,i)=>x-b[i]);
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
export const centroid=points=>points.reduce((s,p)=>s.map((x,i)=>x+p[i]/points.length),[0,0,0]);
export function reflectAcrossFace(point,facePoints) {
  const [a,b,c]=facePoints,n=cross(sub(b,a),sub(c,a)),n2=dot(n,n);
  if(n2<1e-15)throw new RangeError('Degenerate continuation face');
  const k=2*dot(sub(point,a),n)/n2;
  return point.map((x,i)=>x-k*n[i]);
}
export function cellVolume(points) {
  const [a,b,c,d]=points;return Math.abs(dot(sub(b,a),cross(sub(c,a),sub(d,a))))/6;
}
// Separating-axis test: touching faces/edges are not interior overlap.
export function interiorsOverlap(a,b,tolerance=1e-9) {
  const faces=[[0,1,2],[0,3,1],[0,2,3],[1,3,2]],edgeIds=[[0,1],[0,2],[0,3],[1,2],[1,3],[2,3]];
  const axes=[];
  for(const p of [a,b])for(const [i,j,k] of faces)axes.push(cross(sub(p[j],p[i]),sub(p[k],p[i])));
  for(const [i,j] of edgeIds)for(const [k,l] of edgeIds)axes.push(cross(sub(a[j],a[i]),sub(b[l],b[k])));
  for(const axis of axes) {
    const length=Math.hypot(...axis);if(length<1e-12)continue;
    const normal=axis.map(x=>x/length),pa=a.map(p=>dot(p,normal)),pb=b.map(p=>dot(p,normal));
    if(Math.min(Math.max(...pa),Math.max(...pb))-Math.max(Math.min(...pa),Math.min(...pb))<=tolerance)return false;
  }
  return true;
}
export function makeFaceComplex() {
  const raw=[[0,0,0],[1,0,0],[.5,Math.sqrt(3)/2,0],[.5,Math.sqrt(3)/6,Math.sqrt(2/3)]],center=centroid(raw);
  const nodes=new Map(raw.map((p,i)=>['v'+i,p.map((x,j)=>x-center[j])]));
  const cells=new Map();
  const root={id:'root',path:[],parent:null,vertices:['v0','v1','v2','v3'],incoming:['v0','v1','v2']};
  cells.set('root',root);
  const key=path=>path.length?path.map(i=>'R'+(i+1)).join('/'):'root';
  function getCell(path=[]) {
    if(!Array.isArray(path)||path.length>18||path.some(i=>!Number.isInteger(i)||i<0||i>2))throw new RangeError('A face address is a word of at most 18 exits R1/R2/R3');
    const id=key(path);if(cells.has(id))return cells.get(id);
    const parent=getCell(path.slice(0,-1)),exit=path.at(-1),omitted=parent.incoming[exit];
    const face=parent.vertices.filter(id=>id!==omitted),apex='node:'+id;
    nodes.set(apex,reflectAcrossFace(nodes.get(omitted),face.map(id=>nodes.get(id))));
    const cell={id,path:[...path],parent:parent.id,vertices:[...face,apex],incoming:[...face],exitFromParent:exit};
    cells.set(id,cell);return cell;
  }
  function describe(cell) {
    const points=cell.vertices.map(id=>nodes.get(id));
    return {...cell,points:Object.fromEntries(cell.vertices.map(id=>[id,nodes.get(id)])),center:centroid(points),volume:cellVolume(points)};
  }
  function exits(path=[]) {
    const cell=getCell(path);
    return cell.incoming.map((omitted,index)=>{
      const face=cell.vertices.filter(id=>id!==omitted),child=getCell([...path,index]);
      return {index,name:'R'+(index+1),face,omitted,childId:child.id,path:child.path,
        center:centroid(face.map(id=>nodes.get(id))),target:centroid(child.vertices.map(id=>nodes.get(id))),color:exitColors[index]};
    });
  }
  function carriers(mode='none',anchor=[]) {
    if(!carrierModes.includes(mode))throw new RangeError('Unknown carrier selection');
    const p=getCell(anchor),n=getCell([...anchor,0]),e=getCell([...anchor,0,0]);
    const names={C0:p.vertices[0],M0:p.vertices[1],C1:p.vertices[2],M1:p.vertices[3],C2:n.vertices[3],M2:e.vertices[3]};
    const definitions=[
      {id:'proton',symbol:'P',signature:'CMC[M]',names:['C0','M0','C1','M1'],cell:p,color:0x6baec8},
      {id:'neutron',symbol:'N',signature:'MCM[C]',names:['M0','C1','M1','C2'],cell:n,color:0xd7ae77},
      {id:'electron',symbol:'E',signature:'MCC[M]',names:['M1','C1','C2','M2'],cell:e,color:0xf19ad0},
    ];
    const bodies=definitions.filter(body=>mode==='all'||mode===body.id).map(({cell,...body})=>({...body,cellId:cell.id,vertices:body.names.map(name=>names[name])}));
    const used=[...new Set(bodies.flatMap(body=>body.names))];
    return {mode,anchor:[...anchor],bodies,bindings:Object.fromEntries(used.map(name=>[name,names[name]])),
      points:Object.fromEntries(used.map(name=>[name,nodes.get(names[name])])),
      scope:'Carrier incidence labels on generated cells; no physical particle or C/M transition law is inferred.'};
  }
  return {nodes,cells,getCell,describe,exits,carriers};
}
