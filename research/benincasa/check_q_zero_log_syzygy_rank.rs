//! Rank gate for the complete five-wall logarithmic syzygy module on Q=0.
use std::collections::BTreeMap;

const P: i64 = 2_305_843_009_213_693_951;
type Mon = (usize, usize);
type Poly = BTreeMap<Mon, i64>;

fn add(a:i64,b:i64)->i64 { ((a as i128+b as i128).rem_euclid(P as i128)) as i64 }
fn mul(a:i64,b:i64)->i64 { ((a as i128*b as i128).rem_euclid(P as i128)) as i64 }
fn neg(a:i64)->i64 { if a==0 {0} else {P-a} }
fn pow(mut a:i64,mut n:i64)->i64 { let mut r=1; while n>0 {if n&1==1{r=mul(r,a)} a=mul(a,a);n>>=1;} r }
fn inv(a:i64)->i64 {pow(a,P-2)}
fn div(a:i64,b:i64)->i64 {mul(a,inv(b))}
fn put(q:&mut Poly,m:Mon,c:i64){let z=add(*q.get(&m).unwrap_or(&0),c);if z==0{q.remove(&m);}else{q.insert(m,z);}}
fn poly(ts:&[(usize,usize,i64)])->Poly{let mut q=Poly::new();for &(i,j,c) in ts{put(&mut q,(i,j),c.rem_euclid(P));}q}
fn deriv(a:&Poly,axis:usize)->Poly{let mut q=Poly::new();for (&(i,j),&c) in a{let e=if axis==0{i}else{j};if e>0{put(&mut q,if axis==0{(i-1,j)}else{(i,j-1)},mul(c,e as i64));}}q}
fn mons(d:isize)->Vec<Mon>{if d<0{return vec![]}let d=d as usize;(0..=d).flat_map(|i|(0..=d-i).map(move|j|(i,j))).collect()}
fn add_block(rows:&mut BTreeMap<(usize,Mon),Vec<i64>>,eq:usize,col:usize,f:&Poly,s:Mon,scale:i64,n:usize){for(&(i,j),&c)in f{let r=rows.entry((eq,(i+s.0,j+s.1))).or_insert_with(||vec![0;n]);r[col]=add(r[col],mul(scale,c));}}
fn rank(mut a:Vec<Vec<i64>>,n:usize)->usize{let mut r=0;for c in 0..n{let Some(k)=(r..a.len()).find(|&i|a[i][c]!=0)else{continue};a.swap(r,k);let z=inv(a[r][c]);for j in c..n{a[r][j]=mul(a[r][j],z)}for i in 0..a.len(){if i!=r&&a[i][c]!=0{let z=a[i][c];for j in c..n{a[i][j]=add(a[i][j],neg(mul(z,a[r][j])));}}}r+=1;if r==a.len(){break}}r}

fn k_poly(x:i64,y:i64,z:i64,e:i64)->Poly{
 let (x2,y2,z2,e2)=(mul(x,x),mul(y,y),mul(z,z),mul(e,e));
 let h=add(add(x2,y2),neg(z2));
 let ca=add(mul(x2,add(add(x2,neg(y2)),neg(z2))),mul(e2,add(add(y2,neg(x2)),neg(z2))));
 let cb=add(mul(y2,add(add(y2,neg(x2)),neg(z2))),mul(e2,add(add(x2,neg(y2)),neg(z2))));
 let c0=add(add(mul(z2,mul(e2,e2)),mul(mul(e2,z2),add(add(z2,neg(x2)),neg(y2)))),mul(z2,mul(x2,y2)));
 poly(&[(4,0,x2),(2,2,neg(h)),(0,4,y2),(2,0,ca),(0,2,cb),(0,0,c0)])
}
fn nullity(x:i64,y:i64,z:i64,e:i64,d:usize)->usize{
 let k=k_poly(x,y,z,e);let walls=vec![
  poly(&[(0,1,1),(0,0,neg(add(y,z)))]),
  poly(&[(1,0,1),(0,0,neg(add(x,z)))]),
  poly(&[(1,0,1),(0,1,1),(0,0,z)]),
  poly(&[(0,1,1),(0,0,neg(x))]),
  poly(&[(1,0,1),(0,0,neg(y))])];
 let vp=mons(d as isize);let vn=mons(d as isize-1);let np=vp.len();let nn=vn.len();let n=2*np+6*nn;
 let (ka,kb)=(deriv(&k,0),deriv(&k,1));let mut rows:BTreeMap<(usize,Mon),Vec<i64>>=BTreeMap::new();
 for(u,&m)in vp.iter().enumerate(){add_block(&mut rows,0,u,&ka,m,1,n);add_block(&mut rows,0,np+u,&kb,m,1,n);for(i,q)in walls.iter().enumerate(){add_block(&mut rows,1+i,u,&deriv(q,0),m,1,n);add_block(&mut rows,1+i,np+u,&deriv(q,1),m,1,n);}}
 for(u,&m)in vn.iter().enumerate(){add_block(&mut rows,0,2*np+u,&k,m,neg(1),n);for(i,q)in walls.iter().enumerate(){add_block(&mut rows,1+i,2*np+(i+1)*nn+u,q,m,neg(1),n);}}
 n-rank(rows.into_values().filter(|r|r.iter().any(|&c|c!=0)).collect(),n)
}
fn quartic(x:i64,y:i64,e:i64)->i64{
 let s=add(x,y);let p=mul(x,y);let e2=mul(e,e);let e3=mul(e2,e);let e4=mul(e2,e2);
 add(add(neg(mul(16,mul(p,p))),neg(mul(8,mul(p,e2)))),add(mul(8,mul(s,e3)),neg(mul(5,e4))))
}
fn main(){
 let mut rows=Vec::new();let mut constructions=Vec::new();
 for &(e,t) in &[(2,3),(3,2)] {
  let e2=mul(e,e);let s=div(add(div(mul(t,t),e),e),2);let pr=add(neg(div(e2,4)),div(mul(e,t),2));
  let disc=add(mul(s,s),neg(mul(4,pr)));assert_eq!(pow(disc,(P-1)/2),1);
  let root=pow(disc,(P+1)/4);constructions.push(format!("{{\"E\":{},\"t\":{},\"s\":{},\"p\":{}}}",e,t,s,pr));
  for (branch,r) in [root,neg(root)].iter().enumerate(){
   let x=div(add(s,*r),2);let y=div(add(s,neg(*r)),2);let z=add(e,neg(s));
   assert_eq!(mul(x,y),pr);assert_eq!(quartic(x,y,e),0);
   let qrank=nullity(x,y,z,e,7);
   let left=nullity(x,y,add(z,neg(1)),add(e,neg(1)),7);
   let right=nullity(x,y,add(z,1),add(e,1),7);
   rows.push(format!("{{\"family\":[{},{}],\"branch\":{},\"x\":{},\"y\":{},\"z\":{},\"E\":{},\"Q\":0,\"degree7_nullity\":{},\"neighbor_nullities\":[{},{}]}}",e,t,branch,x,y,z,e,qrank,left,right));
  }
 }
 println!("{{\"schema\":\"marici.q-zero-log-syzygy-rank.v1\",\"prime\":{},\"constructions\":[{}],\"samples\":[{}]}}",P,constructions.join(","),rows.join(","));
}
