// Exact ordinary and rho-twisted counts for V9/W1. No external crates.
// rho(p,w)=(p+k,i*w), i=4 in F17. Log cycles certify the fields.
struct F {q:usize, exp:Vec<usize>, log:Vec<usize>, sums:Vec<u16>}
impl F {
 fn new(poly:&[usize])->Self {
  let n=poly.len()-1;let q=17usize.pow(n as u32);let m=289;
  let mut sums=vec![0u16;m*m];
  for a in 0..m {for b in 0..m {sums[a*m+b]=((a%17+b%17)%17+17*((a/17+b/17)%17)) as u16;}}
  let mut f=F{q,exp:vec![0;q-1],log:vec![usize::MAX;q],sums};
  let mut red=[0;17];
  for t in 0..17 {for (j,&c) in poly[..n].iter().enumerate(){red[t]+=((17-t*c%17)%17)*17usize.pow(j as u32);}}
  let mut a=1;
  for j in 0..q-1 {assert!(a!=0&&f.log[a]==usize::MAX,"early generator repeat");f.exp[j]=a;f.log[a]=j;a=f.add((a*17)%q,red[a/(q/17)]);}
  assert_eq!(a,1);assert!(f.log[1..].iter().all(|&v|v!=usize::MAX));f
 }
 fn add(&self,mut a:usize,mut b:usize)->usize {let(mut v,mut p)=(0,1);while a!=0||b!=0 {v+=p*self.sums[(a%289)*289+b%289] as usize;a/=289;b/=289;p*=289;}v}
 fn neg(&self,a:usize)->usize {if a==0 {0}else{self.exp[(self.log[a]+(self.q-1)/2)%(self.q-1)]}}
 fn sub(&self,a:usize,b:usize)->usize {self.add(a,self.neg(b))}
 fn mul(&self,a:usize,b:usize)->usize {if a==0||b==0 {0}else{self.exp[(self.log[a]+self.log[b])%(self.q-1)]}}
 fn inv(&self,a:usize)->usize {assert_ne!(a,0);self.exp[(self.q-1-self.log[a])%(self.q-1)]}
 fn chi(&self,a:usize)->i64 {if a==0{0}else if self.log[a]%2==0{1}else{-1}}
 fn root(&self,a:usize)->usize {if a==0{0}else{assert_eq!(self.log[a]%2,0);self.exp[self.log[a]/2]}}
 fn wp(&self,x:usize)->usize {self.mul(self.mul(x,self.sub(x,1)),self.sub(x,2))}
 fn ordinary(&self)->(i64,i64,i64,i64) {
  // W infinity: g=2, g^3-g=6. Ei infinity contributes one.
  let(mut nw,mut nv,mut ne,mut poles)=(1,1+self.chi(6),1,0);
  for x in 0..self.q {
   ne+=1+self.chi(self.sub(self.mul(self.mul(x,x),x),x));
   let a=self.wp(x);if self.chi(a)<0 {continue;}let y=self.root(a);
   let ys=if y==0 {vec![0]}else{vec![y,self.neg(y)]};
   for y in ys {nw+=1;let x2=self.mul(x,x);let d=self.add(self.sub(x2,self.mul(4,x)),2);
    if d==0 {nv+=1;poles+=1;continue;}
    let g=self.mul(self.add(y,self.mul(2,self.sub(x2,2))),self.inv(d));
    nv+=1+self.chi(self.sub(self.mul(self.mul(g,g),g),g));
   }
  } (nw,nv,ne,poles)
 }
}
#[derive(Clone,Copy,Debug)]struct K(usize,usize);
struct Quad<'a>{f:&'a F,nu:usize}
impl<'a> Quad<'a> {
 fn add(&self,a:K,b:K)->K{K(self.f.add(a.0,b.0),self.f.add(a.1,b.1))}
 fn neg(&self,a:K)->K{K(self.f.neg(a.0),self.f.neg(a.1))}
 fn sub(&self,a:K,b:K)->K{self.add(a,self.neg(b))}
 fn mul(&self,a:K,b:K)->K {let f=self.f;K(f.add(f.mul(a.0,b.0),f.mul(self.nu,f.mul(a.1,b.1))),f.add(f.mul(a.0,b.1),f.mul(a.1,b.0)))}
 fn inv(&self,a:K)->K {let f=self.f;let d=f.inv(f.sub(f.mul(a.0,a.0),f.mul(self.nu,f.mul(a.1,a.1))));K(f.mul(a.0,d),f.neg(f.mul(a.1,d)))}
 fn pow(&self,mut a:K,mut n:usize)->K{let mut r=K(1,0);while n>0 {if n%2==1{r=self.mul(r,a);}a=self.mul(a,a);n/=2;}r}
 fn pair_lifts(&self,x:K,y:K)->i64 {
  let x2=self.mul(x,x);let d=self.add(self.sub(x2,self.mul(K(4,0),x)),K(2,0));
  if d.0==0&&d.1==0 {return 2;} // one normalized ramification point per base point
  let g=self.mul(self.add(y,self.mul(K(2,0),self.sub(x2,K(2,0)))),self.inv(d));
  assert_eq!(g.0,0,"g must be anti-invariant under q-Frobenius");
  let a=self.sub(self.mul(self.mul(g,g),g),g);
  if a.0==0&&a.1==0 {return 2;}
  let r=self.pow(a,(self.f.q-1)/2);assert_eq!(r.1,0);
  let sign=self.f.mul(4,r.0);assert!(sign==1||sign==16);
  if sign==1 {4}else{0}
 }
}
fn twisted(f:&F)->(i64,i64) {
 let nu=f.exp[1];assert_eq!(f.chi(nu),-1);let k=Quad{f,nu};let half=f.inv(2);
 let(mut base,mut count)=(0,0);
 // Z: Y^2=X^3+6X^2+X. Its O and (0,0) have split W-fibres.
 for z in 0..f.q {
  let rhs=f.add(f.add(f.mul(f.mul(z,z),z),f.mul(6,f.mul(z,z))),z);
  if f.chi(rhs)<0{continue;}let yy=f.root(rhs);let ys=if yy==0{vec![0]}else{vec![yy,f.neg(yy)]};
  let s=f.add(z,3);let delta=f.sub(f.mul(s,s),8);
  for yy in ys {
   if f.chi(delta)==-1 {
    let root=f.root(f.mul(delta,f.inv(nu)));let x=K(f.mul(s,half),f.mul(root,half));
    let x2=k.mul(x,x);let denom=k.sub(K(1,0),k.mul(K(2,0),k.inv(x2)));
    let y=k.mul(K(yy,0),k.inv(denom));
    // Check the inverse 2-isogeny equation in the quadratic field.
    let wpoly=k.mul(k.mul(x,k.sub(x,K(1,0))),k.sub(x,K(2,0)));
    let y2=k.mul(y,y);assert_eq!((y2.0,y2.1),(wpoly.0,wpoly.1));
    base+=2;count+=k.pair_lifts(x,y);
   } else if delta==0 {
    let x=f.mul(s,half);let a=f.wp(x);
    if f.chi(a)==-1 {
     let y=K(0,f.root(f.mul(a,f.inv(nu))));base+=2;count+=k.pair_lifts(K(x,0),y);
    }
   }
  }
 }(base,count)
}
fn main(){
 let polys=vec![vec![3,1],vec![3,1,1],vec![3,1,0,1],vec![11,1,0,0,1],vec![3,1,0,0,0,1]];
 println!("{{\"p\":17,\"i_mod_p\":4,\"rows\":[");
 for (j,poly) in polys.iter().enumerate(){let f=F::new(poly);let(nw,nv,ne,poles)=f.ordinary();
  let twist=if j<4 {let(b,t)=twisted(&f);assert_eq!(b,nw,"Lang torsor count");format!(",\"twisted_base\":{},\"rho_Frobenius_fixed_V\":{}",b,t)}else{String::new()};
  eprintln!("n={} q={} W={} V={} E={}",j+1,f.q,nw,nv,ne);
  println!("{}{{\"n\":{},\"q\":{},\"modulus\":{:?},\"W\":{},\"V\":{},\"E\":{},\"rational_poles\":{},\"full_primitive_generator_cycle_verified\":true{}}}",if j==0{""}else{","},j+1,f.q,poly,nw,nv,ne,poles,twist);
 } println!("]}}");
}
