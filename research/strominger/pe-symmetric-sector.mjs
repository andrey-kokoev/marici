// Independent sector probe. No ESD7 generator, corner assignments or particle-count target.
// Native lattice: integer q with sum(q)=1. All cells are whole unit tetrahedra/octahedra.
import {nativeFaceRole} from '../realization-tower/native-face-role.mjs';
export const neutralCentre=Object.freeze([.5,.5,.5,-.5]);
export const dualPoint=q=>q.map((v,i)=>2*neutralCentre[i]-v);
const key=vs=>vs.map(p=>p.join(',')).sort().join('|');
const choose=(xs,n)=>n===0?[[]]:xs.flatMap((x,i)=>choose(xs.slice(i+1),n-1).map(t=>[x,...t]));
const distance2=(a,b)=>a.reduce((s,x,i)=>s+(x-b[i])**2,0);
function integerBases(lower,upper,sum){const out=[];for(let a=lower[0];a<=upper[0];a++)for(let b=lower[1];b<=upper[1];b++)for(let c=lower[2];c<=upper[2];c++){const d=sum-a-b-c;if(d>=lower[3]&&d<=upper[3])out.push([a,b,c,d]);}return out;}
export function buildPESymmetricSector(radius){
 if(!Number.isInteger(radius)||radius<0||radius>6)throw Error('Radius must be an integer in 0..6');
 const halfWidth=radius+.5,lower=neutralCentre.map(x=>x-halfWidth),upper=neutralCentre.map(x=>x+halfWidth),axes=[0,1,2,3],cells=[];
 for(const [role,sum,lo,hi]of [['proton',2,lower.map(x=>x+1),upper],['electron',0,lower,upper.map(x=>x-1)],['neutron',3,lower.map(x=>x+1),upper]])for(const base of integerBases(lo,hi,sum)){
  const vertices=role==='neutron'?choose(axes,2).map(pair=>base.map((x,i)=>x-(pair.includes(i)?1:0))):axes.map(a=>base.map((x,i)=>x+(i===a?(role==='proton'?-1:1):0)));
  const faces=choose(vertices,3).filter(f=>choose(f,2).every(([a,b])=>distance2(a,b)===2));
  cells.push({id:`${role}:${base.join(',')}`,role,kind:role==='neutron'?'octahedron':'tetrahedron',vertices,faces});
 }
 const faceMap=new Map(),byGeometry=new Map(cells.map(c=>[key(c.vertices),c]));
 for(const c of cells)for(const vertices of c.faces){const id=key(vertices);if(!faceMap.has(id))faceMap.set(id,{id,vertices,role:nativeFaceRole(vertices),owners:[]});faceMap.get(id).owners.push(c.id);}
 const faces=[...faceMap.values()],boundary=faces.filter(f=>f.owners.length===1),exposed=new Set(boundary.flatMap(f=>f.owners)),opposite={proton:'electron',electron:'proton',neutron:'neutron'};
 const dualPairs=cells.map(c=>{const d=byGeometry.get(key(c.vertices.map(dualPoint)));if(!d||d.role!==opposite[c.role])throw Error('Sector is not closed under native P/E duality');return [c.id,d.id];});
 const counts=xs=>Object.fromEntries(['proton','neutron','electron'].map(r=>[r,xs.filter(x=>x.role===r).length]));
 const edgeStrips=[];
 // Each octahedral edge meets an upper-coordinate face and a lower-coordinate
 // face. Keep the two incident strips distinct; do not identify their cells.
 for(const a of axes)for(const b of axes)if(a!==b){
  const upperStrip=boundary.filter(f=>f.vertices.every(p=>p[a]===upper[a]&&p[b]<=lower[b]+1));
  const lowerStrip=boundary.filter(f=>f.vertices.every(p=>p[b]===lower[b]&&p[a]>=upper[a]-1));
  edgeStrips.push({upperAxis:a,lowerAxis:b,upper:counts(upperStrip),lower:counts(lowerStrip),combined:counts([...upperStrip,...lowerStrip])});
 }
 return {radius,edgeUnits:2*radius+1,centre:[...neutralCentre],lower,upper,cells,faces,boundary,dualPairs,edgeStrips,audit:{wholeCells:counts(cells),surfaceCells:counts(cells.filter(c=>exposed.has(c.id))),surfaceFaces:counts(boundary),cells:cells.length,boundaryTriangles:boundary.length,nonmanifoldFaces:faces.filter(f=>f.owners.length>2).length,scope:'P/E-symmetric octahedral sector of the native lattice. Not a Pb-208 identification or a belt attachment.'}};
}
