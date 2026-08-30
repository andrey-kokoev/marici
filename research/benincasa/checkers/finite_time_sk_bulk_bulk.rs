#[derive(Clone, Copy, Debug, Default)]
struct C { re: f64, im: f64 }
impl C {
    fn new(re:f64, im:f64)->Self{Self{re,im}}
    fn conj(self)->Self{Self::new(self.re,-self.im)}
    fn norm(self)->f64{(self.re*self.re+self.im*self.im).sqrt()}
}
impl std::ops::Add for C { type Output=Self; fn add(self,r:Self)->Self{Self::new(self.re+r.re,self.im+r.im)} }
impl std::ops::Sub for C { type Output=Self; fn sub(self,r:Self)->Self{Self::new(self.re-r.re,self.im-r.im)} }
impl std::ops::Mul for C { type Output=Self; fn mul(self,r:Self)->Self{Self::new(self.re*r.re-self.im*r.im,self.re*r.im+self.im*r.re)} }
impl std::ops::Mul<f64> for C { type Output=Self; fn mul(self,r:f64)->Self{Self::new(self.re*r,self.im*r)} }

fn phase(x:f64)->C{C::new(x.cos(),x.sin())}
fn gt(k:f64,a:f64,b:f64)->C{
    (C::new(1.0,k*a)*C::new(1.0,-k*b)*phase(-k*(a-b)))*(1.0/k.powi(3))
}
fn lt(k:f64,a:f64,b:f64)->C{gt(k,a,b).conj()}

fn gab(branch_a:i32,branch_b:i32,k:f64,a:f64,b:f64)->C{
    match (branch_a,branch_b) {
        (1,1) => if a>=b {gt(k,a,b)} else {lt(k,a,b)},
        (1,-1) => lt(k,a,b),
        (-1,1) => gt(k,a,b),
        (-1,-1) => if b>=a {gt(k,a,b)} else {lt(k,a,b)},
        _ => unreachable!(),
    }
}

fn external(branch:i32,p:f64,eta:f64,t:f64)->C{
    if branch==1 {gt(p,eta,t)} else {lt(p,eta,t)}
}

fn branch_integrand(a:i32,b:i32,p:f64,q:f64,k:f64,eta:f64,t1:f64,t2:f64)->C{
    let sign=(a*b) as f64;
    external(a,p,eta,t1)*external(b,p,eta,t2)*gab(a,b,q,t1,t2)*gab(a,b,k,t1,t2)
        *(sign/(t1*t1*t2*t2))
}

fn nested_integrand(p:f64,q:f64,k:f64,eta:f64,t1:f64,t2:f64)->C{
    let outer=gt(p,eta,t1)-lt(p,eta,t1);
    let inner=gt(p,eta,t2)*gt(q,t1,t2)*gt(k,t1,t2)
        -lt(p,eta,t2)*lt(q,t1,t2)*lt(k,t1,t2);
    outer*inner*(1.0/(t1*t1*t2*t2))
}

fn main(){
    let (p,q,k,eta)=(1.1,0.8,0.9,-0.15);
    let eta0=std::env::var("MARICI_ETA0").ok().and_then(|x|x.parse().ok()).unwrap_or(-5.0);
    let n=std::env::var("MARICI_TIME_GRID").ok().and_then(|x|x.parse().ok()).unwrap_or(800usize);
    let h=(eta-eta0)/(n as f64);
    let mut rectangular=C::default();
    let mut nested=C::default();
    for i in 0..n {
        let t1=eta0+(i as f64+0.5)*h;
        for j in 0..n {
            let t2=eta0+(j as f64+0.5)*h;
            for a in [1,-1] { for b in [1,-1] {
                rectangular=rectangular+branch_integrand(a,b,p,q,k,eta,t1,t2)*(h*h);
            }}
            if j<i { nested=nested+nested_integrand(p,q,k,eta,t1,t2)*(h*h); }
            if j==i { nested=nested+nested_integrand(p,q,k,eta,t1,t2)*(0.5*h*h); }
        }
    }
    // The rectangular four-branch sum is twice the ordered triangle.  The
    // common -1/2 perturbative prefactor then reproduces the source's minus
    // ordered integral.
    let defect=rectangular-nested*2.0;
    let scale=rectangular.norm().max((nested*2.0).norm()).max(1e-30);
    let relative=defect.norm()/scale;
    eprintln!("rectangular={:?} nested={:?} relative={}",rectangular,nested,relative);
    assert!(relative<1e-11,"relative contour-reduction defect={}",relative);
    println!("{{");
    println!("  \"schema\": \"marici.finite_time_sk_bulk_bulk.v1\",");
    println!("  \"grid\": {n},");
    println!("  \"rectangular_branch_sum_re\": {:.15e},",rectangular.re);
    println!("  \"twice_nested_triangle_re\": {:.15e},",2.0*nested.re);
    println!("  \"relative_defect\": {:.15e},",relative);
    println!("  \"contour_reduction_passes\": true");
    println!("}}");
}
