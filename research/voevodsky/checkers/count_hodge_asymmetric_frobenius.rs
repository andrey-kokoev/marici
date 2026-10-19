// Exact F_(7^n) enumeration of C9 and C17, including normalized pole fibres.
// No external crates. Generator cycles certify every nonzero field element.
use std::time::Instant;
struct Field { q:usize, m:usize, sums:Vec<u16>, exp:Vec<usize>, log:Vec<usize> }
impl Field {
 fn new(poly:&[usize])->Self {
  let n=poly.len()-1; let q=7usize.pow(n as u32); let m=7usize.pow(((n+1)/2) as u32);
  let mut sums=vec![0u16;m*m];
  for a in 0..m { for b in 0..m { let (mut x,mut y,mut v,mut place)=(a,b,0,1);
   for _ in 0..((n+1)/2) {v+=((x%7+y%7)%7)*place;x/=7;y/=7;place*=7;} sums[a*m+b]=v as u16;
  }}
  let mut f=Field{q,m,sums,exp:vec![0;q-1],log:vec![usize::MAX;q]};
  let mut reduction=[0usize;7];
  for t in 0..7 {let mut place=1;for &a in &poly[..n] {reduction[t]+=((7-t*a%7)%7)*place;place*=7;}}
  let mut v=1;
  for i in 0..q-1 {assert!(v!=0 && f.log[v]==usize::MAX,"generator cycle repeated early");f.exp[i]=v;f.log[v]=i;
   let top=v/(q/7);v=f.add((v*7)%q,reduction[top]);
  }
  assert_eq!(v,1); assert!(f.log[1..].iter().all(|&v|v!=usize::MAX)); f
 }
 #[inline] fn add(&self,a:usize,b:usize)->usize {self.sums[(a%self.m)*self.m+b%self.m] as usize+self.m*(self.sums[(a/self.m)*self.m+b/self.m] as usize)}
 #[inline] fn neg(&self,a:usize)->usize {if a==0 {0} else {self.exp[(self.log[a]+(self.q-1)/2)%(self.q-1)]}}
 #[inline] fn sub(&self,a:usize,b:usize)->usize {self.add(a,self.neg(b))}
 #[inline] fn mul(&self,a:usize,b:usize)->usize {if a==0||b==0 {0} else {let v=self.log[a]+self.log[b];self.exp[if v>=self.q-1 {v-(self.q-1)} else {v}]}}
 #[inline] fn inv(&self,a:usize)->usize {assert_ne!(a,0);self.exp[if self.log[a]==0 {0} else {self.q-1-self.log[a]}]}
 #[inline] fn chi(&self,a:usize)->i64 {if a==0 {0} else if self.log[a]%2==0 {1} else {-1}}
 #[inline] fn root(&self,a:usize)->usize {if a==0 {0} else {assert_eq!(self.log[a]%2,0);self.exp[self.log[a]/2]}}
 fn fibre_pair(&self,a:usize,b:usize,y:usize)->i64 {if y==0 {1+self.chi(a)} else {2+self.chi(self.add(a,b))+self.chi(self.sub(a,b))}}
 fn counts(&self)->(i64,i64) {
  let mut c9=4i64; // O and u=0, two normalized split points each.
  for u in 1..self.q {
   let u2=self.mul(u,u);let f=self.mul(u,self.add(self.sub(u2,u),1));
   if self.chi(f)<0 {continue;} let y=self.root(f);let inv=self.inv(u);
   let x2=self.add(self.add(u,6),inv);let x4=self.mul(x2,x2);let a=self.sub(self.mul(x4,x4),2);
   let b=self.mul(y,self.sub(1,self.mul(inv,inv))); c9+=self.fibre_pair(a,b,y);
  }
  let mut c17=8i64; // All four rational kernel points, two split points each.
  for x in 2..self.q {
   let f=self.add(self.mul(self.mul(x,x),x),x);
   if self.chi(f)<0 {continue;} let y=self.root(f);let invx=self.inv(x);
   let u=self.sub(self.add(x,invx),2);assert_ne!(u,0);let invu=self.inv(u);
   let x2=self.add(self.add(u,6),invu);let x4=self.mul(x2,x2);let a=self.sub(self.mul(x4,x4),2);
   let b=self.mul(self.mul(y,self.sub(1,self.mul(invx,invx))),self.sub(1,self.mul(invu,invu)));
   c17+=self.fibre_pair(a,b,y);
  }
  assert_eq!(c9%2,0);assert_eq!(c17%4,0); (c9,c17)
 }
}
fn main(){
 let polynomials:Vec<Vec<usize>>=vec![vec![4,1],vec![3,6,1],vec![4,0,6,1],vec![3,4,5,0,1],vec![4,1,0,0,0,1],vec![3,6,4,5,1,0,1],vec![4,6,0,0,0,0,0,1],vec![3,2,6,4,0,0,0,0,1]];
 let args:Vec<String>=std::env::args().collect();let max:usize=args.get(1).map(|s|s.parse().unwrap()).unwrap_or(8);assert!((1..=8).contains(&max));
 println!("{{\"p\":7,\"rows\":[");
 for (i,poly) in polynomials[..max].iter().enumerate(){let start=Instant::now();let f=Field::new(poly);let(c9,c17)=f.counts();let trace=c9-c17;
  eprintln!("n={} q={} trace={} elapsed={:?}",i+1,f.q,trace,start.elapsed());
  println!("{}{{\"n\":{},\"q\":{},\"modulus\":{:?},\"C9\":{},\"C17\":{},\"primitive_trace\":{},\"full_primitive_generator_cycle_verified\":true}}",if i==0 {""} else {","},i+1,f.q,poly,c9,c17,trace);
 } println!("]}}");
}
