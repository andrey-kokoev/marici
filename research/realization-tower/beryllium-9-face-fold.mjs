const add=(a,b)=>a.map((x,i)=>x+b[i]),sub=(a,b)=>a.map((x,i)=>x-b[i]),scale=(v,s)=>v.map(x=>x*s);
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
const unit=v=>scale(v,1/Math.hypot(...v));
const counts=n=>{const k=Math.floor((n.lattice[0]-2)/3);return [(k-n.lattice[1])/2,(k+n.lattice[1])/2];};
export function foldBeryllium9Faces(nodes,edges,foldLower){
 // The eight rows of WHITE-edge midpoints span a triangular carrier of side
 // seven. Its three midlines pass through the actual conductor midpoints.
 const red=[-Math.sqrt(3)/2,-1.5,0],blue=[Math.sqrt(3)/4,-1.5,.75],top=[0,-.5,0];
 const at=(r,b)=>add(top,add(scale(red,r),scale(blue,b)));
 const left=foldLower(at(3.5,0)),right=foldLower(at(0,3.5)),bottom=foldLower(at(3.5,3.5));
 let normal=unit(cross(sub(right,left),sub(bottom,left)));
 if(dot(sub(top,left),normal)<0)normal=scale(normal,-1);
 const makeHinge=(origin,tip)=>{
  const axis=unit(sub(bottom,origin));
  const rotate=(point,sign)=>{const v=sub(point,origin);return add(origin,add(scale(v,.5),add(scale(cross(axis,v),sign*Math.sqrt(3)/2),scale(axis,.5*dot(axis,v)))));};
  const sign=dot(sub(rotate(tip,1),tip),normal)>0?1:-1;
  return {origin,axis,angle:sign*60,rotate:p=>rotate(p,sign)};
 };
 const redTip=foldLower(at(7,0)),blueTip=foldLower(at(0,7));
 const redHinge=makeHinge(left,redTip),blueHinge=makeHinge(right,blueTip);
 const owner=n=>{const [r,b]=counts(n);return r>3.5&&b>3.5?'junction':r>3.5?'red':b>3.5?'blue':'central';};
 const source=new Map(nodes.map(n=>[n.id,n])),mapped=new Map(nodes.map(n=>{
  const side=owner(n),point=side==='red'?redHinge.rotate(n.point):side==='blue'?blueHinge.rotate(n.point):[...n.point];
  return [n.id,{...n,point}];
 }));
 // The final branching row protrudes beyond the triangular WHITE-row carrier.
 // Its shared middle output is still ONE retained node, not two torn tips.
 // Close its two unit-length terminal conductors at their sphere intersection.
 const closures=[];
 for(const n of nodes.filter(n=>owner(n)==='junction')){
  const incoming=edges.filter(e=>e.to===n.id);if(incoming.length!==2)throw Error('Expected two terminal conductors');
  const [a,b]=incoming.map(e=>mapped.get(e.from).point),delta=sub(b,a),distance=Math.hypot(...delta);
  if(distance>2+1e-10||distance<1e-10)throw Error('Terminal conductors cannot close at unit length');
  const axis=unit(delta),mid=scale(add(a,b),.5),preferred=scale(add(redHinge.rotate(n.point),blueHinge.rotate(n.point)),.5);
  let radial=sub(preferred,mid);radial=sub(radial,scale(axis,dot(radial,axis)));
  if(Math.hypot(...radial)<1e-10)radial=sub(normal,scale(axis,dot(normal,axis)));
  const point=add(mid,scale(unit(radial),Math.sqrt(Math.max(0,1-distance*distance/4))));
  mapped.get(n.id).point=point;closures.push({id:n.id,parents:incoming.map(e=>e.from),point});
 }
 const foldedEdges=edges.map(e=>{
  const a=source.get(e.from),b=source.get(e.to),sa=owner(a),sb=owner(b),start=mapped.get(e.from).point,end=mapped.get(e.to).point;
  if(sa==='junction'||sb==='junction')return {...e,points:[start,end]};
  if(sa===sb){const rotate=sa==='red'?redHinge.rotate:sa==='blue'?blueHinge.rotate:p=>p;return {...e,points:e.points.map(rotate)};}
  const hinge=sa==='red'||sb==='red'?redHinge:blueHinge;
  const midpoint=e.points.length===3?e.points[1]:scale(add(a.point,b.point),.5);
  const relative=sub(midpoint,hinge.origin);
  if(Math.hypot(...cross(relative,hinge.axis))>1e-8)throw Error('Conductor midpoint is not on its side hinge');
  return {...e,points:[start,midpoint,end]};
 });
 const faces=[{id:'upper',points:[top,left,right]},{id:'central',points:[left,right,bottom]},
  {id:'red-side',points:[left,redHinge.rotate(redTip),bottom]},{id:'blue-side',points:[right,bottom,blueHinge.rotate(blueTip)]}];
 return {nodes:[...mapped.values()],edges:foldedEdges,faces,audit:{triangularFaces:4,sideFoldAngle:60,commonSideNormal:normal,
  sideHinges:[redHinge,blueHinge].map(({origin,axis,angle})=>({origin,axis,angle})),terminalClosures:closures}};
}
