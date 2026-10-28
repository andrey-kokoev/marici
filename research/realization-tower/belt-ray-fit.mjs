const sub=(a,b)=>a.map((v,i)=>v-b[i]),dot=(a,b)=>a.reduce((s,v,i)=>s+v*b[i],0),cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]],unit=a=>a.map(v=>v/Math.hypot(...a));
export function rotateBeltPoint(p,origin,axis,angle){const d=sub(p,origin),c=Math.cos(angle),s=Math.sin(angle),k=cross(axis,d);return origin.map((v,i)=>v+c*d[i]+s*k[i]+(1-c)*dot(axis,d)*axis[i]);}
// The intended enclosure is the intersection of the two inward triangular
// cones after their tips, truncated at the finite ray endpoints.
export function fitBeltInsideRays(surface,rays,origin,axis){
 const planes=[];
 for(const copy of ['original','clone']){
  const rs=rays.filter(r=>r.copy===copy).map(r=>r.points);if(rs.length!==3)return {status:'missing-rays'};
  // Tip is one native edge length from each start; rays have length five.
  const tips=rs.map(r=>r[0].map((v,i)=>v+(r[1][i]-v)/5)),tip=tips[0].map((_,i)=>tips.reduce((s,p)=>s+p[i]/3,0));
  for(let i=0;i<3;i++){let n=unit(cross(sub(rs[i][1],tip),sub(rs[(i+1)%3][1],tip)));if(dot(n,sub(origin,tip))<0)n=n.map(v=>-v);planes.push({point:tip,normal:n});}
  const end=rs[0][1];let n=axis.map(v=>v*(copy==='original'?1:-1));planes.push({point:end,normal:n});
 }
 const inradius=Math.min(...surface.faces.map(f=>{const [a,b,c]=f.indices.map(i=>surface.vertices[i]),n=unit(cross(sub(b,a),sub(c,a)));return Math.abs(dot(n,sub(origin,a)));}));
 const enclosureClearance=Math.min(...planes.map(f=>dot(f.normal,sub(origin,f.point))));
 const rotationObstruction=enclosureClearance<inradius-1e-9?{kind:'inscribed-ball-exceeds-cone-clearance',beltInradius:inradius,enclosureClearance,deficit:inradius-enclosureClearance,scope:'Every rotation about the belt centre retains its inscribed ball; a cone plane cuts that ball.'}:null;
 const clearance=angle=>Math.min(...surface.vertices.flatMap(p=>{const q=rotateBeltPoint(p,origin,axis,angle);return planes.map(f=>dot(f.normal,sub(q,f.point)));}));
 let best={angle:0,clearance:clearance(0)};
 for(let degrees=1;degrees<360;degrees++){const angle=degrees*Math.PI/180,c=clearance(angle);if(c>best.clearance+1e-12)best={angle,clearance:c};}
 return {status:rotationObstruction?'rotation-obstructed':best.clearance>=-1e-9?'fits':'no-axial-fit',rotationObstruction,...best,degrees:best.angle*180/Math.PI,initialClearance:clearance(0),planes,scope:'All boundary vertices inside both finite triangular ray cones; axial rigid rotations only.'};
}
