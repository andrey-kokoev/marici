// Generic odd-prime field kernel; two fresh split-prime controls, no crates.
struct F {p:usize,m:usize,q:usize,exp:Vec<usize>,log:Vec<usize>,sums:Vec<u16>}
impl F {
 fn new(p:usize,poly:&[usize])->Self {
  let n=poly.len()-1;let q=p.pow(n as u32);let m=p*p;
  let mut sums=vec![0u16;m*m];
  for a in 0..m {for b in 0..m{sums[a*m+b]=((a%p+b%p)%p+p*((a/p+b/p)%p)) as u16;}}
  let mut f=F{p,m,q,exp:vec![0;q-1],log:vec![usize::MAX;q],sums};let mut red=vec![0;p];
  for t in 0..p {for(j,&c)in poly[..n].iter().enumerate(){red[t]+=(p-t*c%p)%p*p.pow(j as u32);}}
  let mut a=1;
  for j in 0..q-1 {assert!(a!=0&&f.log[a]==usize::MAX);f.exp[j]=a;f.log[a]=j;a=f.add(a*p%q,red[a/(q/p)]);}
  assert_eq!(a,1);assert!(f.log[1..].iter().all(|&v|v!=usize::MAX));f
 }
 fn add(&self,mut a:usize,mut b:usize)->usize{let(mut v,mut t)=(0,1);while a!=0||b!=0{v+=t*self.sums[(a%self.m)*self.m+b%self.m] as usize;a/=self.m;b/=self.m;t*=self.m;}v}
 fn neg(&self,a:usize)->usize{if a==0{0}else{self.exp[(self.log[a]+(self.q-1)/2)%(self.q-1)]}}
 fn sub(&self,a:usize,b:usize)->usize{self.add(a,self.neg(b))}
 fn mul(&self,a:usize,b:usize)->usize{if a==0||b==0{0}else{self.exp[(self.log[a]+self.log[b])%(self.q-1)]}}
 fn inv(&self,a:usize)->usize{assert_ne!(a,0);self.exp[(self.q-1-self.log[a])%(self.q-1)]}
 fn chi(&self,a:usize)->i64{if a==0{0}else if self.log[a]%2==0{1}else{-1}}
 fn root(&self,a:usize)->usize{if a==0{0}else{assert_eq!(self.log[a]%2,0);self.exp[self.log[a]/2]}}
 fn wp(&self,x:usize)->usize{self.mul(self.mul(x,self.sub(x,1)),self.sub(x,2))}
 fn ordinary(&self,b:usize)->(i64,i64,i64,i64){
  let(mut w,mut v,mut e,mut poles)=(1,1+self.chi(self.sub(self.mul(self.mul(b,b),b),b)),1,0);
  for x in 0..self.q {
   e+=1+self.chi(self.sub(self.mul(self.mul(x,x),x),x));let a=self.wp(x);if self.chi(a)<0{continue;}
   let y=self.root(a);let ys=if y==0{vec![0]}else{vec![y,self.neg(y)]};
   for y in ys{w+=1;let x2=self.mul(x,x);let d=self.add(self.sub(x2,self.mul(4,x)),2);
    if d==0{v+=1;poles+=1;continue;}
    let g=self.mul(self.add(y,self.mul(b,self.sub(x2,2))),self.inv(d));v+=1+self.chi(self.sub(self.mul(self.mul(g,g),g),g));
   }
  }(w,v,e,poles)
 }
}
#[derive(Clone,Copy)]struct K(usize,usize);
struct Quad<'a>{f:&'a F,nu:usize}
impl<'a> Quad<'a>{
 fn add(&self,a:K,b:K)->K{K(self.f.add(a.0,b.0),self.f.add(a.1,b.1))}
 fn neg(&self,a:K)->K{K(self.f.neg(a.0),self.f.neg(a.1))}
 fn sub(&self,a:K,b:K)->K{self.add(a,self.neg(b))}
 fn mul(&self,a:K,b:K)->K{let f=self.f;K(f.add(f.mul(a.0,b.0),f.mul(self.nu,f.mul(a.1,b.1))),f.add(f.mul(a.0,b.1),f.mul(a.1,b.0)))}
 fn inv(&self,a:K)->K{let f=self.f;let d=f.inv(f.sub(f.mul(a.0,a.0),f.mul(self.nu,f.mul(a.1,a.1))));K(f.mul(a.0,d),f.neg(f.mul(a.1,d)))}
 fn pow(&self,mut a:K,mut n:usize)->K{let mut v=K(1,0);while n>0{if n%2==1{v=self.mul(v,a);}a=self.mul(a,a);n/=2;}v}
 fn lifts(&self,x:K,y:K,b:usize,i:usize)->i64{
  let x2=self.mul(x,x);let d=self.add(self.sub(x2,self.mul(K(4,0),x)),K(2,0));if d.0==0&&d.1==0{return 2;}
  let g=self.mul(self.add(y,self.mul(K(b,0),self.sub(x2,K(2,0)))),self.inv(d));assert_eq!(g.0,0);
  let a=self.sub(self.mul(self.mul(g,g),g),g);if a.0==0&&a.1==0{return 2;}
  let r=self.pow(a,(self.f.q-1)/2);assert_eq!(r.1,0);let sign=self.f.mul(i,r.0);assert!(sign==1||sign==self.f.p-1);if sign==1{4}else{0}
 }
}
fn twisted(f:&F,b:usize,i:usize)->(i64,i64){
 let nu=f.exp[1];assert_eq!(f.chi(nu),-1);let k=Quad{f,nu};let half=f.inv(2);let(mut base,mut count)=(0,0);
 for z in 0..f.q{
  let rhs=f.add(f.add(f.mul(f.mul(z,z),z),f.mul(6,f.mul(z,z))),z);if f.chi(rhs)<0{continue;}
  let y=f.root(rhs);let ys=if y==0{vec![0]}else{vec![y,f.neg(y)]};let s=f.add(z,3);let delta=f.sub(f.mul(s,s),8);
  for y in ys{
   if f.chi(delta)==-1{
    let x=K(f.mul(s,half),f.mul(f.root(f.mul(delta,f.inv(nu))),half));let xx=k.mul(x,x);
    let y=k.mul(K(y,0),k.inv(k.sub(K(1,0),k.mul(K(2,0),k.inv(xx)))));
    let yy=k.mul(y,y);let a=k.mul(k.mul(x,k.sub(x,K(1,0))),k.sub(x,K(2,0)));assert_eq!((yy.0,yy.1),(a.0,a.1));
    base+=2;count+=k.lifts(x,y,b,i);
   }else if delta==0{
    let x=f.mul(s,half);let a=f.wp(x);if f.chi(a)==-1{let y=K(0,f.root(f.mul(a,f.inv(nu))));base+=2;count+=k.lifts(K(x,0),y,b,i);}
   }
  }
 }(base,count)
}
fn main(){
 let cases=vec![(13,3,5,vec![vec![2,1],vec![2,1,1],vec![6,1,0,1],vec![2,1,1,0,1],vec![2,4,0,0,0,1]]),
 (29,6,12,vec![vec![2,1],vec![3,1,1],vec![11,1,0,1],vec![19,1,0,0,1],vec![8,1,0,0,0,1]])];
 println!("{{\"cases\":[");
 for(c,(p,b,i,polys))in cases.iter().enumerate(){
  assert_eq!(i*i%p,p-1);println!("{}{{\"p\":{},\"b\":{},\"i_mod_p\":{},\"rows\":[",if c==0{""}else{","},p,b,i);
  for(j,poly)in polys.iter().enumerate(){
   let f=F::new(*p,poly);let(w,v,e,poles)=f.ordinary(*b);
   let t=if j<4{let(base,fixed)=twisted(&f,*b,*i);assert_eq!(base,w);format!(",\"twisted_base\":{},\"rho_Frobenius_fixed_V\":{}",base,fixed)}else{String::new()};
   println!("{}{{\"n\":{},\"q\":{},\"modulus\":{:?},\"W\":{},\"V\":{},\"E\":{},\"rational_poles\":{},\"full_primitive_generator_cycle_verified\":true{}}}",if j==0{""}else{","},j+1,f.q,poly,w,v,e,poles,t);
   eprintln!("p={} b={} n={} W={} V={}",p,b,j+1,w,v);
  }println!("]}}");
 }println!("]}}");
}
