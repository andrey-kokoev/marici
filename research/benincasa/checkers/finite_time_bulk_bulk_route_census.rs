use std::collections::BTreeMap;

#[derive(Clone, Copy, Debug, Default)]
struct C { r:f64, i:f64 }
impl C { fn n(r:f64,i:f64)->Self{Self{r,i}} fn abs(self)->f64{(self.r*self.r+self.i*self.i).sqrt()} }
impl std::ops::Add for C { type Output=Self; fn add(self,x:Self)->Self{Self::n(self.r+x.r,self.i+x.i)} }
impl std::ops::Sub for C { type Output=Self; fn sub(self,x:Self)->Self{Self::n(self.r-x.r,self.i-x.i)} }
impl std::ops::Mul for C { type Output=Self; fn mul(self,x:Self)->Self{Self::n(self.r*x.r-self.i*x.i,self.r*x.i+self.i*x.r)} }
impl std::ops::Mul<f64> for C { type Output=Self; fn mul(self,x:f64)->Self{Self::n(self.r*x,self.i*x)} }
impl std::ops::Div<C> for C { type Output=Self; fn div(self,x:Self)->Self{let d=x.r*x.r+x.i*x.i;Self::n((self.r*x.r+self.i*x.i)/d,(self.i*x.r-self.r*x.i)/d)} }

#[derive(Clone,Copy)]
struct T { f1:[i32;3], f2:[i32;3], n1:i32, n2:i32, c:C }
fn af(a:[i32;3],b:[i32;3])->[i32;3]{[a[0]+b[0],a[1]+b[1],a[2]+b[2]]}
fn mul(a:&[T],b:&[T])->Vec<T>{let mut o=Vec::new();for x in a{for y in b{o.push(T{f1:af(x.f1,y.f1),f2:af(x.f2,y.f2),n1:x.n1+y.n1,n2:x.n2+y.n2,c:x.c*y.c})}}o}
fn external_t(which:usize, sign:i32, m:f64, eta:f64)->Vec<T>{
    let phase=if sign==1{-m*eta}else{m*eta};
    let base=C::n(phase.cos(),phase.sin())*C::n(1.,sign as f64*m*eta)*(1./m.powi(3));
    let mut f=[0;3];f[which]=sign;
    vec![T{f1:f,f2:[0;3],n1:0,n2:0,c:base},T{f1:f,f2:[0;3],n1:1,n2:0,c:base*C::n(0.,-(sign as f64)*m)}]
}
fn external_t2(sign:i32,m:f64,eta:f64)->Vec<T>{external_t(0,sign,m,eta).into_iter().map(|x|T{f1:[0;3],f2:x.f1,n1:0,n2:x.n1,c:x.c}).collect()}
fn internal(which:usize, gt:bool, m:f64)->Vec<T>{
    let s=if gt{-1}else{1}; let mut f1=[0;3];let mut f2=[0;3];f1[which]=s;f2[which]=-s;
    let l1=C::n(0.,-(s as f64)*m);let l2=C::n(0.,(s as f64)*m);let z=C::n(1./m.powi(3),0.);
    vec![T{f1,f2,n1:0,n2:0,c:z},T{f1,f2,n1:1,n2:0,c:z*l1},T{f1,f2,n1:0,n2:1,c:z*l2},T{f1,f2,n1:1,n2:1,c:z*l1*l2}]
}
fn add(map:&mut BTreeMap<([i32;3],i32),C>,k:([i32;3],i32),v:C){let x=map.entry(k).or_default();*x=*x+v}
fn omega(f:[i32;3],p:f64,q:f64,k:f64)->f64{f[0]as f64*p+f[1]as f64*q+f[2]as f64*k}

fn main(){
    let p=std::env::var("MARICI_P").ok().and_then(|x|x.parse().ok()).unwrap_or(1.1);
    let q=std::env::var("MARICI_Q").ok().and_then(|x|x.parse().ok()).unwrap_or(0.8);
    let k=std::env::var("MARICI_K").ok().and_then(|x|x.parse().ok()).unwrap_or(0.9);
    let eta=std::env::var("MARICI_ETA").ok().and_then(|x|x.parse().ok()).unwrap_or(-0.15);
    let weight=vec![T{f1:[0;3],f2:[0;3],n1:-2,n2:-2,c:C::n(1.,0.)}];
    let mut raw=Vec::new();
    for outer_gt in [true,false] { for inner_gt in [true,false] {
        let outer_sign=if outer_gt{1}else{-1};
        let inner_sign=if inner_gt{1}else{-1};
        let product=mul(&mul(&mul(&external_t(0,outer_sign,p,eta),&external_t2(inner_sign,p,eta)),&internal(1,inner_gt,q)),&internal(2,inner_gt,k));
        let expansion_sign=(if outer_gt{1.}else{-1.})*(if inner_gt{1.}else{-1.});
        for mut t in mul(&weight,&product){t.c=t.c*expansion_sign;raw.push(t)}
    }
    }
    // Census the only inner-lower route that can contribute eta0^2 while
    // leaving the outer primitive evaluated at the fixed observation time:
    // zero inner frequency and n2=1.
    let mut outer:BTreeMap<([i32;3],i32),C>=BTreeMap::new();
    let mut count=0usize;
    for t in &raw {if t.f2==[0;3] && t.n2==1 {count+=1;add(&mut outer,(t.f1,t.n1),t.c*(-0.5));}}
    outer.retain(|_,c|c.abs()>1e-11);
    let negative_outer=outer.iter().filter(|((_,n),_)|*n<0).count();
    println!("raw_terms={}",raw.len());
    println!("inner_lower_grade2_terms={count}");
    println!("combined_outer_monomials={}",outer.len());
    println!("negative_outer_powers={negative_outer}");
    for((f,n),c)in&outer{println!("outer f={:?} n={} c=({:.12e},{:.12e})",f,n,c.r,c.i)}

    // At total grade two both time powers must be maximal, n1=n2=1.
    // Route U: inner upper endpoint followed by outer lower endpoint.
    // Route LL: inner lower endpoint followed by outer lower endpoint.
    let mut grade:BTreeMap<([i32;3],i32),C>=BTreeMap::new();
    for t in &raw {
        let f=af(t.f1,t.f2);let w1=omega(t.f1,p,q,k);let w2=omega(t.f2,p,q,k);let ws=omega(f,p,q,k);
        assert!(w1.abs()>1e-10&&w2.abs()>1e-10);
        let sum_power=t.n1+t.n2;
        let upper_then_lower=if ws.abs()>1e-10 {
            if sum_power==2 {(t.c/C::n(0.,w2)/C::n(0.,ws))*(-1.)}else{C::default()}
        } else {
            // For zero combined frequency the outer primitive is polynomial.
            // Grade two requires an outer t^1 term.  It comes either from the
            // leading inner primitive when n1+n2=1 or from its first
            // subleading term when n1+n2=2.
            let inner=if sum_power==1 {C::n(1.,0.)/C::n(0.,w2)}
                else if sum_power==2 {(C::n(1.,0.)/C::n(0.,w2))*(-(t.n2 as f64))/C::n(0.,w2)}
                else {C::default()};
            inner*(-0.5)*t.c
        };
        let lower_lower=if sum_power==2{t.c/C::n(0.,w2)/C::n(0.,w1)}else{C::default()};
        add(&mut grade,(f,2),upper_then_lower+lower_lower);
    }
    // The source's ordered bulk--bulk term carries an overall minus sign.
    let spatial=(p*p+q*q+k*k).powi(2);
    for c in grade.values_mut(){*c=*c*(-spatial)}
    grade.retain(|_,c|c.abs()>1e-11);
    assert!(grade.keys().all(|(f,n)|*n==2&&f[1]==0&&f[2]==0&&matches!(f[0],-2|0|2)));
    for((f,n),c)in&grade{println!("bulk_bulk_grade{n}_frequency_{:?}=({:.15e},{:.15e})",f,c.r,c.i)}
    let minus=grade.get(&([-2,0,0],2)).unwrap();let plus=grade.get(&([2,0,0],2)).unwrap();
    assert!((*minus-C::n(plus.r,-plus.i)).abs()<1e-11);
    assert!(grade.get(&([0,0,0],2)).unwrap().i.abs()<1e-11);
    let shape=C::n((-2.*p*eta).cos(),(-2.*p*eta).sin())*C::n(1.-p*p*eta*eta,2.*p*eta)*0.5;
    let amplitude=(*plus/shape)*p;let j1=(p*p+q*q+k*k).powi(2)/(p.powi(4)*q*k*(q+k-p));assert!((amplitude-C::n(j1,0.)).abs()<1e-10);
    println!("bulk_bulk_internal_frequency_support_cancelled=true");
    println!("bulk_bulk_grade2_reality=true");
    println!("direct_oscillatory_basis=J1");
}
