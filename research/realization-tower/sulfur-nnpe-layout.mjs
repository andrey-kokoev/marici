// Cube [-h,h]^3 cut by x=y, retaining y<=x: a triangular half-cube.
// Show only its three rectangular side surfaces; no caps or particle glyphs.
const h=.85;
export const nnpePlanes=[
 {name:'NP',role:'N',colour:0x168fff,normal:[1,0,0],corners:[[h,-h,-h],[h,h,-h],[h,h,h],[h,-h,h]]},
 {name:'PE',role:'P',colour:0xff3030,normal:[0,-1,0],corners:[[-h,-h,-h],[h,-h,-h],[h,-h,h],[-h,-h,h]]},
 {name:'EN',role:'E',colour:0xffffff,normal:[-Math.SQRT1_2,Math.SQRT1_2,0],corners:[[-h,-h,-h],[h,h,-h],[h,h,h],[-h,-h,h]]}
];
export function layoutNNPEComposition(model,collapsed=false){
 const source=collapsed?model.components:model.stars.map(s=>({id:s.id,stars:[s.id],boundary:s.ports.map(p=>p.id),inventory:s.inventory,history:{star:s.id}}));
 const lookup=new Map(model.stars.flatMap(s=>s.ports.map(p=>[p.id,p]))),columns=Math.min(4,Math.ceil(Math.sqrt(source.length))),rows=Math.ceil(source.length/columns);
 const groups=source.map((c,i)=>{
  const origin=[(i%columns-(columns-1)/2)*3.6,((rows-1)/2-Math.floor(i/columns))*3.6,0],counts={N:0,P:0,E:0};
  const planes=nnpePlanes.map(plane=>{const corners=plane.corners.map(p=>p.map((x,j)=>x+origin[j]));return {...plane,corners,origin:origin.map((x,j)=>x+plane.corners.reduce((s,p)=>s+p[j]/4,0))};});
  // Invisible interaction targets on the coloured surfaces retain port joining.
  const ports=c.boundary.map(id=>{
   const p=lookup.get(id),plane=planes.find(f=>f.role===p.role),index=counts[p.role]++,total=c.boundary.filter(k=>lookup.get(k).role===p.role).length;
   const u=total===1?.5:.15+.7*(index%4)/Math.min(3,total-1),v=total<=4?.5:.15+.7*Math.floor(index/4)/Math.max(1,Math.ceil(total/4)-1);
   const [a,b,,d]=plane.corners,point=a.map((x,j)=>x+u*(b[j]-x)+v*(d[j]-x));return {...p,point,used:model.usedPorts.includes(id)};
  });
  return {...c,origin,ports,planes};
 });
 const ports=groups.flatMap(g=>g.ports),positions=new Map(ports.map(p=>[p.id,p.point]));
 const joins=collapsed?[]:model.joins.map(([a,b])=>({a,b,points:[positions.get(a),positions.get(b)]}));
 const points=groups.flatMap(g=>g.planes.flatMap(p=>p.corners));
 const bounds=[0,1,2].map(i=>[Math.min(...points.map(p=>p[i]))-.3,Math.max(...points.map(p=>p[i]))+.3]);
 return {groups,ports,joins,envelope:bounds[0].flatMap(x=>bounds[1].flatMap(y=>bounds[2].map(z=>[x,y,z]))),audit:{representation:'diagonal-half-cube',operations:groups.length,planes:groups.length*3,intersectionVertices:0,colours:['blue','red','white'],centralGlyph:'none',cutPlane:'x=y',retainedHalf:'y<=x'}};
}
