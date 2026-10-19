// General denominator coefficient a, reusing the checked generic field kernel.
#[allow(dead_code)] mod kernel {
 include!("count_hodge_minimal_axis_second_prime.rs");
 fn ordinary_a(f:&F,a:usize,b:usize)->(i64,i64,i64,i64){
  let(mut w,mut v,mut e,mut poles)=(1,1+f.chi(f.sub(f.mul(f.mul(b,b),b),b)),1,0);
  for x in 0..f.q {
   e+=1+f.chi(f.sub(f.mul(f.mul(x,x),x),x));let p=f.wp(x);if f.chi(p)<0{continue;}
   let y=f.root(p);let ys=if y==0{vec![0]}else{vec![y,f.neg(y)]};
   for y in ys{w+=1;let xx=f.mul(x,x);let d=f.add(f.sub(xx,f.mul(a,x)),2);
    if d==0{v+=1;poles+=1;continue;}
    let g=f.mul(f.add(y,f.mul(b,f.sub(xx,2))),f.inv(d));v+=1+f.chi(f.sub(f.mul(f.mul(g,g),g),g));
   }
  }(w,v,e,poles)
 }
 impl<'a> Quad<'a>{
  fn lifts_a(&self,x:K,y:K,a:usize,b:usize,i:usize)->i64{
   let xx=self.mul(x,x);let d=self.add(self.sub(xx,self.mul(K(a,0),x)),K(2,0));if d.0==0&&d.1==0{return 2;}
   let g=self.mul(self.add(y,self.mul(K(b,0),self.sub(xx,K(2,0)))),self.inv(d));assert_eq!(g.0,0);
   let z=self.sub(self.mul(self.mul(g,g),g),g);if z.0==0&&z.1==0{return 2;}
   let r=self.pow(z,(self.f.q-1)/2);assert_eq!(r.1,0);let sign=self.f.mul(i,r.0);assert!(sign==1||sign==self.f.p-1);if sign==1{4}else{0}
  }
 }
 fn twisted_a(f:&F,a:usize,b:usize,i:usize)->(i64,i64){
  let nu=f.exp[1];let k=Quad{f,nu};let half=f.inv(2);let(mut base,mut count)=(0,0);
  for z in 0..f.q{
   let rhs=f.add(f.add(f.mul(f.mul(z,z),z),f.mul(6,f.mul(z,z))),z);if f.chi(rhs)<0{continue;}
   let y=f.root(rhs);let ys=if y==0{vec![0]}else{vec![y,f.neg(y)]};let s=f.add(z,3);let delta=f.sub(f.mul(s,s),8);
   for y in ys{
    if f.chi(delta)==-1{
     let x=K(f.mul(s,half),f.mul(f.root(f.mul(delta,f.inv(nu))),half));let xx=k.mul(x,x);
     let y=k.mul(K(y,0),k.inv(k.sub(K(1,0),k.mul(K(2,0),k.inv(xx)))));
     let yy=k.mul(y,y);let p=k.mul(k.mul(x,k.sub(x,K(1,0))),k.sub(x,K(2,0)));assert_eq!((yy.0,yy.1),(p.0,p.1));
     base+=2;count+=k.lifts_a(x,y,a,b,i);
    }else if delta==0{
     let x=f.mul(s,half);let p=f.wp(x);if f.chi(p)==-1{let y=K(0,f.root(f.mul(p,f.inv(nu))));base+=2;count+=k.lifts_a(K(x,0),y,a,b,i);}
    }
   }
  }(base,count)
 }
 pub fn run(){
  let polys=vec![vec![2,1],vec![2,1,1],vec![6,1,0,1],vec![2,1,1,0,1],vec![2,4,0,0,0,1]];
  println!("{{\"p\":13,\"lambda\":2,\"b\":2,\"i_mod_p\":5,\"rows\":[");let mut first=true;
  for(j,poly)in polys.iter().enumerate(){
   let f=F::new(13,poly);assert_eq!(ordinary_a(&f,4,3),f.ordinary(3));
   if j<4{assert_eq!(twisted_a(&f,4,3,5),twisted(&f,3,5));}
   for a in [0,2,6,7,8,10,11,12]{
    let(w,v,e,poles)=ordinary_a(&f,a,2);
    let t=if j<4{let(base,fixed)=twisted_a(&f,a,2,5);assert_eq!(base,w);
     format!(",\"twisted_base\":{},\"rho_Frobenius_fixed_V\":{}",base,fixed)
    }else{String::new()};
    println!("{}{{\"a\":{},\"n\":{},\"q\":{},\"modulus\":{:?},\"W\":{},\"V\":{},\"E\":{},\"rational_poles\":{},\"full_primitive_generator_cycle_verified\":true{}}}",if first{""}else{","},a,j+1,f.q,poly,w,v,e,poles,t);first=false;
   }
  }println!("]}}");
 }
}
fn main(){kernel::run();}
