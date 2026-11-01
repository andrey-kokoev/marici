import {Vector3,Quaternion,Euler,MathUtils} from 'three';
// A direction alone leaves roll undefined: choose the shortest rotation from +X.
export function gridEdgeEuler(from,to){
 const direction=new Vector3(...to).sub(new Vector3(...from));
 if(direction.lengthSq()<1e-14)throw Error('An edge needs distinct endpoints');
 const q=new Quaternion().setFromUnitVectors(new Vector3(1,0,0),direction.normalize());
 const e=new Euler().setFromQuaternion(q,'XYZ');
 return [e.x,e.y,e.z].map(MathUtils.radToDeg);
}
const angle=x=>`${Number(x.toFixed(1))}°`;
export function cellulationGridLabels(anchor,edges){
 const result=[{key:`dot:${anchor.id}`,kind:'dot',point:anchor.point,text:`FCC (${anchor.latticePoint.join(', ')})`}];
 for(const [i,edge] of edges.entries()){
  const other=edge.vertices.find(p=>p.some((v,j)=>Math.abs(v-anchor.point[j])>1e-7));
  const euler=gridEdgeEuler(anchor.point,other);
  result.push({key:`edge:${i}`,kind:'edge',from:anchor.point,to:other,point:anchor.point.map((v,j)=>(v+other[j])/2),euler,text:`XYZ (${euler.map(angle).join(', ')})`});
 }
 return result;
}
