use std::collections::BTreeMap;

#[derive(Clone,Copy,Debug,Default)] struct C{r:f64,i:f64}
impl C{fn n(r:f64,i:f64)->Self{Self{r,i}}fn abs(self)->f64{(self.r*self.r+self.i*self.i).sqrt()}}
impl std::ops::Add for C{type Output=Self;fn add(self,x:Self)->Self{Self::n(self.r+x.r,self.i+x.i)}}
impl std::ops::Sub for C{type Output=Self;fn sub(self,x:Self)->Self{Self::n(self.r-x.r,self.i-x.i)}}
impl std::ops::Mul for C{type Output=Self;fn mul(self,x:Self)->Self{Self::n(self.r*x.r-self.i*x.i,self.r*x.i+self.i*x.r)}}
impl std::ops::Mul<f64> for C{type Output=Self;fn mul(self,x:f64)->Self{Self::n(self.r*x,self.i*x)}}
impl std::ops::Div for C{type Output=Self;fn div(self,x:Self)->Self{let d=x.r*x.r+x.i*x.i;Self::n((self.r*x.r+self.i*x.i)/d,(self.i*x.r-self.r*x.i)/d)}}

#[derive(Clone,Copy)] struct T{f1:[i32;3],f2:[i32;3],n1:i32,n2:i32,c:C}
fn af(a:[i32;3],b:[i32;3])->[i32;3]{[a[0]+b[0],a[1]+b[1],a[2]+b[2]]}
fn mul(a:&[T],b:&[T])->Vec<T>{let mut o=Vec::new();for x in a{for y in b{o.push(T{f1:af(x.f1,y.f1),f2:af(x.f2,y.f2),n1:x.n1+y.n1,n2:x.n2+y.n2,c:x.c*y.c})}}o}
fn external(which:usize,second:bool,sign:i32,m:f64,eta:f64)->Vec<T>{
 let phase=-(sign as f64)*m*eta;let base=C::n(phase.cos(),phase.sin())*C::n(1.,sign as f64*m*eta)*(1./m.powi(3));let mut f=[0;3];f[which]=sign;
 let (f1,f2,n1,n2)=if second{([0;3],f,0,1)}else{(f,[0;3],1,0)};
 let (z1,z2)=if second{(0,0)}else{(0,0)};
 vec![T{f1:if second{[0;3]}else{f},f2:if second{f}else{[0;3]},n1:z1,n2:z2,c:base},T{f1,f2,n1,n2,c:base*C::n(0.,-(sign as f64)*m)}]
}
fn internal(which:usize,gt:bool,m:f64)->Vec<T>{
 let s=if gt{-1}else{1};let mut f1=[0;3];let mut f2=[0;3];f1[which]=s;f2[which]=-s;let z=C::n(1./m.powi(3),0.);let l1=C::n(0.,-(s as f64)*m);let l2=C::n(0.,(s as f64)*m);
 vec![T{f1,f2,n1:0,n2:0,c:z},T{f1,f2,n1:1,n2:0,c:z*l1},T{f1,f2,n1:0,n2:1,c:z*l2},T{f1,f2,n1:1,n2:1,c:z*l1*l2}]
}
fn omega(f:[i32;3],p:f64,q:f64,k:f64)->f64{f[0]as f64*p+f[1]as f64*q+f[2]as f64*k}
fn falling(n:i32,r:usize)->f64{(0..r).map(|j|f64::from(n-j as i32)).product()}
fn pc(n:i32,r:usize,w:f64)->C{let s=if r%2==0{1.}else{-1.};C::n(s*falling(n,r),0.)/(0..=r).fold(C::n(1.,0.),|z,_|z*C::n(0.,w))}
fn add<K:Ord>(m:&mut BTreeMap<K,C>,key:K,value:C){let z=m.entry(key).or_default();*z=*z+value}

fn main(){
 let p=std::env::var("MARICI_P").ok().and_then(|x|x.parse().ok()).unwrap_or(1.1);let q=std::env::var("MARICI_Q").ok().and_then(|x|x.parse().ok()).unwrap_or(0.8);let k=std::env::var("MARICI_K").ok().and_then(|x|x.parse().ok()).unwrap_or(0.9);let eta=std::env::var("MARICI_ETA").ok().and_then(|x|x.parse().ok()).unwrap_or(-0.15);let weight=vec![T{f1:[0;3],f2:[0;3],n1:-2,n2:-2,c:C::n(1.,0.)}];let mut raw=Vec::new();
 for outer_gt in[true,false]{for inner_gt in[true,false]{let so=if outer_gt{1}else{-1};let si=if inner_gt{1}else{-1};let x=mul(&mul(&mul(&external(0,false,so,p,eta),&external(0,true,si,p,eta)),&internal(1,inner_gt,q)),&internal(2,inner_gt,k));let branch=(if outer_gt{1.}else{-1.})*(if inner_gt{1.}else{-1.});for mut t in mul(&weight,&x){t.c=t.c*branch;raw.push(t)}}}
 let mut lower:BTreeMap<([i32;3],i32),C>=BTreeMap::new();let mut upper_keys:BTreeMap<([i32;3],i32,[i32;3],i32,usize),C>=BTreeMap::new();let mut logarithms:BTreeMap<[i32;3],C>=BTreeMap::new();let max_r=8usize;
 for t in &raw{let w1=omega(t.f1,p,q,k);let w2=omega(t.f2,p,q,k);let fs=af(t.f1,t.f2);let ws=w1+w2;assert!(w1.abs()>1e-10&&w2.abs()>1e-10);
  for r2 in 0..=max_r{let a2=pc(t.n2,r2,w2);let n=t.n1+t.n2-r2 as i32;
   // Lower endpoint of the outer primitive of the inner upper term.
   if ws.abs()>1e-10{for r3 in 0..=max_r{let power=n-r3 as i32;if power<0{break}add(&mut lower,(fs,power),t.c*a2*pc(n,r3,ws)*(-1.));}}
   else if n == -1{add(&mut logarithms,fs,t.c*a2*(-1.))}else{let power=n+1;if power>=0{add(&mut lower,(fs,power),t.c*a2*(-1./f64::from(n+1)));}}
   // Product of the two lower primitives.
   for r1 in 0..=max_r{let power=t.n2-r2 as i32+t.n1-r1 as i32;if power<0{break}add(&mut lower,(fs,power),t.c*a2*pc(t.n1,r1,w1));}
   // Coefficient of -F2(eta0) F1(eta); this must cancel before F1 is evaluated.
   let power=t.n2-r2 as i32;if power>=0{add(&mut upper_keys,(t.f2,power,t.f1,t.n1,r2),t.c*a2*(-1.));}
  }
 }
 let spatial=(p*p+q*q+k*k).powi(2);for c in lower.values_mut(){*c=*c*(-spatial)}for c in upper_keys.values_mut(){*c=*c*(-spatial)}for c in logarithms.values_mut(){*c=*c*(-spatial)}
 lower.retain(|_,c|c.abs()>1e-10);upper_keys.retain(|_,c|c.abs()>1e-10);logarithms.retain(|_,c|c.abs()>1e-10);
 assert!(upper_keys.keys().all(|(_,power,_,_,_)|*power<2));
 assert!(logarithms.is_empty(),"logarithmic zero-frequency classes survive: {}",logarithms.len());
 for grade in[2,1,0]{let rows:Vec<_>=lower.iter().filter(|((_,n),_)|*n==grade).collect();println!("grade_{grade}_term_count={}",rows.len());for((f,_),c)in rows{println!("grade_{grade}_frequency_{f:?}=({:.15e},{:.15e})",c.r,c.i);println!("LOWER|BB|{grade}|{},{},{}|{:.17e}|{:.17e}",f[0],f[1],f[2],c.r,c.i)}}
 let g2:Vec<_>=lower.keys().filter(|(f,n)|*n==2&&f[1]==0&&f[2]==0&&matches!(f[0],-2|0|2)).collect();assert_eq!(g2.len(),3);
 let mut upper_support:BTreeMap<(i32,[i32;3]),usize>=BTreeMap::new();
 for((f2,power,_,_,_),_)in&upper_keys{*upper_support.entry((*power,*f2)).or_default()+=1;}
 println!("observation_endpoint_route_count={}",upper_keys.len());
 for((power,f),count)in upper_support{println!("observation_endpoint_grade_{power}_frequency_{f:?}_primitive_classes={count}");}
 for((fb,power,fo,n,r),c)in&upper_keys{println!("OBS|BB|{},{},{}|{}|{},{},{}|{}|{}|{:.17e}|{:.17e}",fb[0],fb[1],fb[2],power,fo[0],fo[1],fo[2],n,r,c.r,c.i);}
 println!("grade2_observation_endpoint_support_absent=true");println!("logarithmic_routes=0");println!("lower_endpoint_grades_derived_without_fitting=true");
}
