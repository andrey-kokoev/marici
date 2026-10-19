// Complete regular F37 denominator chart. Shared orbits and exact character identities.
#[allow(dead_code)] mod kernel {
 include!("count_hodge_minimal_axis_second_prime.rs");
 const ASES:[usize;34]=[0,1,2,4,5,6,7,8,9,10,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36];
 fn ordinary_a(f:&F,a:usize)->(i64,i64,i64,i64){
  let(mut w,mut v,mut e,mut poles)=(1,1+f.chi(6),1,0);
  for x in 0..f.q {
   e+=1+f.chi(f.sub(f.mul(f.mul(x,x),x),x));let p=f.wp(x);if f.chi(p)<0{continue;}
   let y=f.root(p);let ys=if y==0{vec![0]}else{vec![y,f.neg(y)]};
   for y in ys{w+=1;let xx=f.mul(x,x);let d=f.add(f.sub(xx,f.mul(a,x)),2);
    if d==0{v+=1;poles+=1;continue;}
    let g=f.mul(f.add(y,f.mul(2,f.sub(xx,2))),f.inv(d));v+=1+f.chi(f.sub(f.mul(f.mul(g,g),g),g));
   }
  }(w,v,e,poles)
 }
 fn ordinary_all(f:&F,n:usize)->(i64,Vec<i64>,i64,Vec<i64>,[usize;6]){
  assert_eq!(f.chi(f.neg(1)),1);let(mut w,mut e)=(1,1);let mut vs=vec![1+f.chi(6);34];let mut poles=vec![0;34];
  let mut seen=vec![false;f.q];let mut sizes=[0usize;6];let mut covered=0;
  for x in 0..f.q {
   if seen[x]{continue;}let(mut t,mut len)=(x,0);
   loop{assert!(!seen[t]);seen[t]=true;len+=1;covered+=1;t=if t==0{0}else{f.exp[f.log[t]*37%(f.q-1)]};if t==x{break;}assert!(len<n);}
   assert_eq!(n%len,0);sizes[len]+=1;let weight=len as i64;
   e+=weight*(1+f.chi(f.sub(f.mul(f.mul(x,x),x),x)));let p=f.wp(x);if f.chi(p)<0{continue;}
   let y=f.root(p);let ys=[y,f.neg(y)];let count=if y==0{1}else{2};let xx=f.mul(x,x);let negx=f.neg(x);let z=f.sub(xx,2);let nn=f.add(z,z);
   for &y in &ys[..count]{w+=weight;let u=f.add(y,nn);let cu=f.chi(u);let negu=f.neg(u);let mut d=f.add(xx,2);let mut j=0;
    for a in 0..37{
     if j<34&&ASES[j]==a{
      if d==0{vs[j]+=weight;poles[j]+=weight;}else{let chi=cu*f.chi(d)*f.chi(f.add(d,u))*f.chi(f.add(d,negu));vs[j]+=weight*(1+chi);}
      j+=1;
     }d=f.add(d,negx);
    }assert_eq!(j,34);
   }
  }assert_eq!(covered,f.q);assert_eq!((1..=5).map(|j|j*sizes[j]).sum::<usize>(),f.q);(w,vs,e,poles,sizes)
 }
 impl<'a> Quad<'a>{
  fn lifts_fast(&self,x:K,y:K,a:usize,sign0:i64,audit:bool)->i64{
   let xx=self.mul(x,x);let d=self.add(self.sub(xx,self.mul(K(a,0),x)),K(2,0));if d.0==0&&d.1==0{return 2;}
   let g=self.mul(self.add(y,self.mul(K(2,0),self.sub(xx,K(2,0)))),self.inv(d));assert_eq!(g.0,0);
   let c=self.f.mul(g.1,self.f.sub(self.f.mul(self.nu,self.f.mul(g.1,g.1)),1));
   if c==0{assert_eq!(g.1,0);return 2;}
   let sign=sign0*self.f.chi(c);
   if audit{let h=self.sub(self.mul(self.mul(g,g),g),g);let r=self.pow(h,(self.f.q-1)/2);assert_eq!(r.1,0);let old=self.f.mul(6,r.0);assert_eq!(sign,if old==1{1}else{assert_eq!(old,36);-1});}
   if sign==1{4}else{assert_eq!(sign,-1);0}
  }
 }
 fn twisted_all(f:&F,audit:bool)->(i64,Vec<i64>){
  let nu=f.exp[1];let k=Quad{f,nu};let half=f.inv(2);let(mut base,mut counts)=(0,vec![0;34]);
  let root_i=f.exp[f.log[nu]*((f.q-1)/4)%(f.q-1)];let s0=f.mul(6,root_i);let sign0=if s0==1{1}else{assert_eq!(s0,36);-1};
  for z in 0..f.q{
   let rhs=f.add(f.add(f.mul(f.mul(z,z),z),f.mul(6,f.mul(z,z))),z);if f.chi(rhs)<0{continue;}
   let y=f.root(rhs);let ys=if y==0{vec![0]}else{vec![y,f.neg(y)]};let s=f.add(z,3);let delta=f.sub(f.mul(s,s),8);
   for y in ys{
    let point=if f.chi(delta)==-1{
     let x=K(f.mul(s,half),f.mul(f.root(f.mul(delta,f.inv(nu))),half));let xx=k.mul(x,x);
     let y=k.mul(K(y,0),k.inv(k.sub(K(1,0),k.mul(K(2,0),k.inv(xx)))));
     assert_eq!((k.mul(y,y).0,k.mul(y,y).1),{let p=k.mul(k.mul(x,k.sub(x,K(1,0))),k.sub(x,K(2,0)));(p.0,p.1)});Some((x,y))
    }else if delta==0{let x=f.mul(s,half);let p=f.wp(x);if f.chi(p)==-1{Some((K(x,0),K(0,f.root(f.mul(p,f.inv(nu))))))}else{None}}else{None};
    if let Some((x,y))=point{base+=2;for(j,&a)in ASES.iter().enumerate(){counts[j]+=k.lifts_fast(x,y,a,sign0,audit);}}
   }
  }(base,counts)
 }
 pub fn run(){
  let polys=vec![vec![2,1],vec![5,1,1],vec![13,1,0,1],vec![2,1,0,0,1],vec![5,1,0,0,0,1]];
  println!("{{\"p\":37,\"lambda\":2,\"b\":2,\"i_mod_p\":6,\"rows\":[");let mut first=true;
  for(n0,poly)in polys.iter().enumerate(){let n=n0+1;let f=F::new(37,poly);let(w,vs,e,poles,sizes)=ordinary_all(&f,n);
   let tw=if n<5{let(base,counts)=twisted_all(&f,n<=2);assert_eq!(base,w);let j=ASES.iter().position(|&a|a==4).unwrap();assert_eq!(ordinary_a(&f,4),f.ordinary(2));assert_eq!((base,counts[j]),twisted(&f,2,6));Some((base,counts))}else{None};
   for(j,&a)in ASES.iter().enumerate(){if n<5{assert_eq!((w,vs[j],e,poles[j]),ordinary_a(&f,a));}
    let ts=if let Some((base,ref counts))=tw{format!(",\"twisted_base\":{},\"rho_Frobenius_fixed_V\":{},\"twist_power_crosscheck\":{}",base,counts[j],n<=2)}else{String::new()};
    println!("{}{{\"a\":{},\"n\":{},\"q\":{},\"modulus\":{:?},\"W\":{},\"V\":{},\"E\":{},\"rational_poles\":{},\"Frobenius_x_orbit_counts_by_length\":{:?},\"direct_ordinary_crosscheck\":{},\"full_primitive_generator_cycle_verified\":true{}}}",if first{""}else{","},a,n,f.q,poly,w,vs[j],e,poles[j],sizes,n<5,ts);first=false;
   }
  }println!("]}}");
 }
}
fn main(){kernel::run();}
