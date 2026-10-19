// A fresh parameter-line census using the previous independently checked field kernel.
#[allow(dead_code)] mod kernel {
 include!("count_hodge_minimal_axis_frobenius.rs");
 fn ordinary_b(f:&F,b:usize)->i64 {
  let mut nv=1+f.chi(f.sub(f.mul(f.mul(b,b),b),b));
  for x in 0..f.q {
   let p=f.wp(x);if f.chi(p)<0 {continue;}let y=f.root(p);
   let ys=if y==0{vec![0]}else{vec![y,f.neg(y)]};
   for y in ys {
    let x2=f.mul(x,x);let d=f.add(f.sub(x2,f.mul(4,x)),2);
    if d==0{nv+=1;continue;}
    let g=f.mul(f.add(y,f.mul(b,f.sub(x2,2))),f.inv(d));
    nv+=1+f.chi(f.sub(f.mul(f.mul(g,g),g),g));
   }
  }nv
 }
 fn torsor(f:&F)->Vec<(K,K)> {
  let nu=f.exp[1];let k=Quad{f,nu};let half=f.inv(2);let mut out=vec![];
  for z in 0..f.q {
   let rhs=f.add(f.add(f.mul(f.mul(z,z),z),f.mul(6,f.mul(z,z))),z);
   if f.chi(rhs)<0 {continue;}let y=f.root(rhs);let ys=if y==0{vec![0]}else{vec![y,f.neg(y)]};
   let s=f.add(z,3);let delta=f.sub(f.mul(s,s),8);
   for y in ys {
    if f.chi(delta)==-1 {
     let x=K(f.mul(s,half),f.mul(f.root(f.mul(delta,f.inv(nu))),half));
     let y=k.mul(K(y,0),k.inv(k.sub(K(1,0),k.mul(K(2,0),k.inv(k.mul(x,x))))));
     let y2=k.mul(y,y);let p=k.mul(k.mul(x,k.sub(x,K(1,0))),k.sub(x,K(2,0)));
     assert_eq!((y2.0,y2.1),(p.0,p.1));out.push((x,y));
    } else if delta==0 {
     let x=f.mul(s,half);let p=f.wp(x);
     if f.chi(p)==-1 {out.push((K(x,0),K(0,f.root(f.mul(p,f.inv(nu))))));}
    }
   }
  }out
 }
 fn twisted_b(f:&F,points:&[(K,K)],b:usize)->i64 {
  let k=Quad{f,nu:f.exp[1]};let mut count=0;
  for &(x,y) in points {
   let x2=k.mul(x,x);let d=k.add(k.sub(x2,k.mul(K(4,0),x)),K(2,0));
   if d.0==0&&d.1==0 {count+=2;continue;}
   let g=k.mul(k.add(y,k.mul(K(b,0),k.sub(x2,K(2,0)))),k.inv(d));assert_eq!(g.0,0);
   let a=k.sub(k.mul(k.mul(g,g),g),g);
   if a.0==0&&a.1==0 {count+=2;continue;}
   let r=k.pow(a,(f.q-1)/2);assert_eq!(r.1,0);let sign=f.mul(4,r.0);assert!(sign==1||sign==16);
   if sign==1 {count+=4;}
  }count
 }
 pub fn census(){
  let polys=vec![vec![3,1],vec![3,1,1],vec![3,1,0,1],vec![11,1,0,0,1]];
  println!("{{\"p\":17,\"lambda\":2,\"a\":4,\"rows\":[");let mut first=true;
  for (j,poly) in polys.iter().enumerate(){
   let f=F::new(poly);let(w,v,e,poles)=f.ordinary();let points=torsor(&f);assert_eq!(2*points.len() as i64,w);
   for b in [2,3,6,11,14,15] {
    let vb=ordinary_b(&f,b);let tb=twisted_b(&f,&points,b);
    if b==2 {assert_eq!(vb,v);assert_eq!(tb,twisted(&f).1);}
    println!("{}{{\"b\":{},\"n\":{},\"q\":{},\"modulus\":{:?},\"W\":{},\"V\":{},\"E\":{},\"rational_poles\":{},\"twisted_base\":{},\"rho_Frobenius_fixed_V\":{},\"full_primitive_generator_cycle_verified\":true}}",if first{""}else{","},b,j+1,f.q,poly,w,vb,e,poles,w,tb);first=false;
   }
  }println!("]}}");
 }
}
fn main(){kernel::census();}
