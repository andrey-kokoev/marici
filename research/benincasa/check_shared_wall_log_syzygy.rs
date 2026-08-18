//! Degree census for vector fields logarithmic along K and the three shared walls.
use std::collections::BTreeMap;

const P: i64 = 2_305_843_009_213_693_951;
type Mon = (usize, usize);
type Poly = BTreeMap<Mon, i64>;

fn add(a: i64, b: i64) -> i64 { ((a as i128 + b as i128).rem_euclid(P as i128)) as i64 }
fn mul(a: i64, b: i64) -> i64 { ((a as i128 * b as i128).rem_euclid(P as i128)) as i64 }
fn pow(mut a: i64, mut n: i64) -> i64 { let mut r=1; while n>0 { if n&1==1 {r=mul(r,a)} a=mul(a,a); n>>=1; } r }
fn inv(a: i64) -> i64 { pow(a, P-2) }
fn put(q: &mut Poly, m: Mon, c: i64) { let z=add(*q.get(&m).unwrap_or(&0),c); if z==0 {q.remove(&m);} else {q.insert(m,z);} }
fn pmul(a:&Poly,b:&Poly)->Poly { let mut q=Poly::new(); for (&(i,j),&x) in a {for (&(k,l),&y) in b {put(&mut q,(i+k,j+l),mul(x,y));}} q }
fn deriv(a:&Poly, axis:usize)->Poly { let mut q=Poly::new(); for (&(i,j),&x) in a {let e=if axis==0{i}else{j}; if e>0 {let m=if axis==0{(i-1,j)}else{(i,j-1)}; put(&mut q,m,mul(x,e as i64));}} q }
fn mons(d:isize)->Vec<Mon>{if d<0{return vec![]} let d=d as usize; (0..=d).flat_map(|i|(0..=d-i).map(move|j|(i,j))).collect()}
fn poly(ts:&[(usize,usize,i64)])->Poly{let mut q=Poly::new();for &(i,j,c) in ts{put(&mut q,(i,j),c.rem_euclid(P));}q}

fn rank(mut a:Vec<Vec<i64>>, n:usize)->usize{
 let mut r=0;
 for c in 0..n {let Some(piv)=(r..a.len()).find(|&i|a[i][c]!=0) else{continue};a.swap(r,piv);let z=inv(a[r][c]);for j in c..n{a[r][j]=mul(a[r][j],z)}for i in 0..a.len(){if i!=r&&a[i][c]!=0{let z=a[i][c];for j in c..n{a[i][j]=add(a[i][j],-mul(z,a[r][j]));}}}r+=1;if r==a.len(){break}}
 r
}

fn add_block(rows:&mut BTreeMap<(usize,Mon),Vec<i64>>, eq:usize, col:usize, factor:&Poly, shift:Mon, scale:i64, ncols:usize){
 for (&(i,j),&c) in factor {let row=rows.entry((eq,(i+shift.0,j+shift.1))).or_insert_with(||vec![0;ncols]);row[col]=add(row[col],mul(scale,c));}
}

fn system(d:usize, force_wall_product:bool, k:&Poly, walls:&[Poly], wall_product:&Poly)->(Vec<Vec<i64>>,usize,Vec<Mon>,Vec<Mon>){
 let vp=if force_wall_product{mons(d as isize-3)}else{mons(d as isize)};
 let vn=mons(d as isize-1);
 let np=vp.len();let nn=vn.len();let ncols=2*np+(1+walls.len())*nn;
 let ka=deriv(k,0);let kb=deriv(k,1);
 let mut rows:BTreeMap<(usize,Mon),Vec<i64>>=BTreeMap::new();
 for (u,&m) in vp.iter().enumerate(){
   let base=if force_wall_product{pmul(wall_product,&poly(&[(m.0,m.1,1)]))}else{poly(&[(m.0,m.1,1)])};
   for (&s,&c) in &base {add_block(&mut rows,0,u,&ka,s,c,ncols);add_block(&mut rows,0,np+u,&kb,s,c,ncols);
     for (i,q) in walls.iter().enumerate(){let qa=deriv(q,0);let qb=deriv(q,1);add_block(&mut rows,1+i,u,&qa,s,c,ncols);add_block(&mut rows,1+i,np+u,&qb,s,c,ncols);}
   }
 }
 for (u,&m) in vn.iter().enumerate(){add_block(&mut rows,0,2*np+u,k,m,-1,ncols);for i in 0..walls.len(){add_block(&mut rows,1+i,2*np+(i+1)*nn+u,&walls[i],m,-1,ncols);}}
 let matrix:Vec<Vec<i64>>=rows.into_values().filter(|r|r.iter().any(|&x|x!=0)).collect();
 (matrix,ncols,vp,vn)
}
fn nullity(d:usize, force_wall_product:bool, k:&Poly, walls:&[Poly], wall_product:&Poly)->usize{
 let (matrix,ncols,_,_)=system(d,force_wall_product,k,walls,wall_product);ncols-rank(matrix,ncols)
}

fn nullity_k_quotient_divisible_by(d:usize,k:&Poly,walls:&[Poly],factor:&Poly,factor_degree:usize)->usize{
 let vp=mons(d as isize);let vn=mons(d as isize-1);let nk=mons(d as isize-1-factor_degree as isize);
 let np=vp.len();let nn=vn.len();let ncols=2*np+nk.len()+walls.len()*nn;
 let ka=deriv(k,0);let kb=deriv(k,1);let kw=pmul(k,factor);
 let mut rows:BTreeMap<(usize,Mon),Vec<i64>>=BTreeMap::new();
 for (u,&m) in vp.iter().enumerate(){
   add_block(&mut rows,0,u,&ka,m,1,ncols);add_block(&mut rows,0,np+u,&kb,m,1,ncols);
   for (i,q) in walls.iter().enumerate(){let qa=deriv(q,0);let qb=deriv(q,1);add_block(&mut rows,1+i,u,&qa,m,1,ncols);add_block(&mut rows,1+i,np+u,&qb,m,1,ncols);}
 }
 for (u,&m) in nk.iter().enumerate(){add_block(&mut rows,0,2*np+u,&kw,m,-1,ncols);}
 for (i,q) in walls.iter().enumerate(){for (u,&m) in vn.iter().enumerate(){add_block(&mut rows,1+i,2*np+nk.len()+i*nn+u,q,m,-1,ncols);}}
 let matrix:Vec<Vec<i64>>=rows.into_values().filter(|r|r.iter().any(|&x|x!=0)).collect();
 ncols-rank(matrix,ncols)
}

fn dimension_k_quotient_vanishes_on_corner(d:usize,k:&Poly,walls:&[Poly],selected:usize)->usize{
 let vp=mons(d as isize);let vn=mons(d as isize-1);let nq=mons(d as isize-2);let nk=mons(d as isize-5);
 let np=vp.len();let nn=vn.len();let ncols=2*np+nq.len()+nk.len()+walls.len()*nn;
 let ka=deriv(k,0);let kb=deriv(k,1);let kq=pmul(k,&walls[selected]);let k2=pmul(k,k);
 let mut rows:BTreeMap<(usize,Mon),Vec<i64>>=BTreeMap::new();
 for (u,&m) in vp.iter().enumerate(){add_block(&mut rows,0,u,&ka,m,1,ncols);add_block(&mut rows,0,np+u,&kb,m,1,ncols);
  for (i,q) in walls.iter().enumerate(){let qa=deriv(q,0);let qb=deriv(q,1);add_block(&mut rows,1+i,u,&qa,m,1,ncols);add_block(&mut rows,1+i,np+u,&qb,m,1,ncols);}}
 for (u,&m) in nq.iter().enumerate(){add_block(&mut rows,0,2*np+u,&kq,m,-1,ncols);}
 for (u,&m) in nk.iter().enumerate(){add_block(&mut rows,0,2*np+nq.len()+u,&k2,m,-1,ncols);}
 for (i,q) in walls.iter().enumerate(){for (u,&m) in vn.iter().enumerate(){add_block(&mut rows,1+i,2*np+nq.len()+nk.len()+i*nn+u,q,m,-1,ncols);}}
 let matrix:Vec<Vec<i64>>=rows.into_values().filter(|r|r.iter().any(|&x|x!=0)).collect();
 let representation_kernel=mons(d as isize-6).len();
 ncols-rank(matrix,ncols)-representation_kernel
}

fn dimension_k_quotient_vanishes_on_all_corners(d:usize,k:&Poly,walls:&[Poly])->usize{
 let vp=mons(d as isize);let vn=mons(d as isize-1);let mu=mons(d as isize-2);let nu=mons(d as isize-5);
 let np=vp.len();let nn=vn.len();let block=mu.len()+nu.len();
 let ncols=2*np+nn+walls.len()*nn+walls.len()*block;
 let ka=deriv(k,0);let kb=deriv(k,1);let one=poly(&[(0,0,1)]);
 let mut rows:BTreeMap<(usize,Mon),Vec<i64>>=BTreeMap::new();
 for (u,&m) in vp.iter().enumerate(){add_block(&mut rows,0,u,&ka,m,1,ncols);add_block(&mut rows,0,np+u,&kb,m,1,ncols);
  for (i,q) in walls.iter().enumerate(){let qa=deriv(q,0);let qb=deriv(q,1);add_block(&mut rows,1+i,u,&qa,m,1,ncols);add_block(&mut rows,1+i,np+u,&qb,m,1,ncols);}}
 let n0_offset=2*np;let lambda_offset=n0_offset+nn;let corner_offset=lambda_offset+walls.len()*nn;
 for (u,&m) in vn.iter().enumerate(){add_block(&mut rows,0,n0_offset+u,k,m,-1,ncols);
  for i in 0..walls.len(){add_block(&mut rows,1+walls.len()+i,n0_offset+u,&one,m,1,ncols);}}
 for (i,q) in walls.iter().enumerate(){for (u,&m) in vn.iter().enumerate(){add_block(&mut rows,1+i,lambda_offset+i*nn+u,q,m,-1,ncols);}
  for (u,&m) in mu.iter().enumerate(){add_block(&mut rows,1+walls.len()+i,corner_offset+i*block+u,q,m,-1,ncols);}
  for (u,&m) in nu.iter().enumerate(){add_block(&mut rows,1+walls.len()+i,corner_offset+i*block+mu.len()+u,k,m,-1,ncols);}}
 let matrix:Vec<Vec<i64>>=rows.into_values().filter(|r|r.iter().any(|&x|x!=0)).collect();
 let representation_kernel=walls.len()*mons(d as isize-6).len();
 ncols-rank(matrix,ncols)-representation_kernel
}

fn fiber_census(x:i64,y:i64,z:i64)->String{
 let e=x+y+z;let (x2,y2,z2,e2)=(x*x,y*y,z*z,e*e);
 let k=poly(&[
  (4,0,x2),(2,2,-(x2+y2-z2)),(0,4,y2),(2,0,x2*(x2-y2-z2)+e2*(y2-x2-z2)),
  (0,2,y2*(y2-x2-z2)+e2*(x2-y2-z2)),(0,0,z2*e2*e2+e2*z2*(z2-x2-y2)+z2*x2*y2)]);
 let shared=vec![poly(&[(0,1,1),(0,0,-y-z)]),poly(&[(1,0,1),(0,0,-x-z)]),poly(&[(1,0,1),(0,1,1),(0,0,z)])];
 let mut five=shared.clone();five.push(poly(&[(0,1,1),(0,0,-x)]));five.push(poly(&[(1,0,1),(0,0,-y)]));
 let product=|ws:&[Poly]|ws.iter().fold(poly(&[(0,0,1)]),|a,b|pmul(&a,b));let q3=product(&shared);let q5=product(&five);
 let census=|ws:&[Poly],q:&Poly,maxd:usize|{(0..=maxd).map(|d|{let f=nullity(d,false,&k,ws,q);let z=nullity(d,true,&k,ws,q);(d,f,z,f-z)}).collect::<Vec<_>>()};
 let rows3=census(&shared,&q3,7);let rows5=census(&five,&q5,10);
 let corner= five.iter().map(|q|nullity_k_quotient_divisible_by(7,&k,&five,q,1)).collect::<Vec<_>>();
 let corner_mod_k=five.iter().enumerate().map(|(i,_)|dimension_k_quotient_vanishes_on_corner(7,&k,&five,i)).collect::<Vec<_>>();
 let all_corner=nullity_k_quotient_divisible_by(7,&k,&five,&q5,5);
 let all_corner_mod_k=dimension_k_quotient_vanishes_on_all_corners(7,&k,&five);
 let show=|rows:&[(usize,usize,usize,usize)]|rows.iter().map(|(d,f,q,a)|format!("{{\"degree\":{},\"full\":{},\"wall_product_divisible\":{},\"wall_active\":{}}}",d,f,q,a)).collect::<Vec<_>>().join(",");
 format!("{{\"fiber\":[{},{},{}],\"shared_three_rows\":[{}],\"complete_five_rows\":[{}],\"degree7_k_quotient_wall_divisible_nullities\":{:?},\"degree7_k_quotient_corner_vanishing_dimensions\":{:?},\"degree7_k_quotient_all_walls_divisible_nullity\":{},\"degree7_k_quotient_all_corner_vanishing_dimension\":{}}}",x,y,z,show(&rows3),show(&rows5),corner,corner_mod_k,all_corner,all_corner_mod_k)
}
fn main(){
 let a=fiber_census(2,3,4);let b=fiber_census(3,5,7);
 println!("{{\"schema\":\"marici.shared_wall_log_syzygy_census.v4\",\"prime\":{},\"samples\":[{},{}],\"stable_complete_five_minimal_degree\":7,\"stable_complete_five_minimal_rank\":3}}",P,a,b);
}
