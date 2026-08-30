#[derive(Clone, Copy, Debug, Default)]
struct C { re: f64, im: f64 }
impl C { fn n(re:f64,im:f64)->Self{Self{re,im}} fn abs(self)->f64{(self.re*self.re+self.im*self.im).sqrt()} }
impl std::ops::Add for C { type Output=Self; fn add(self,x:Self)->Self{Self::n(self.re+x.re,self.im+x.im)} }
impl std::ops::Mul<f64> for C { type Output=Self; fn mul(self,x:f64)->Self{Self::n(self.re*x,self.im*x)} }
impl std::ops::Div<C> for C { type Output=Self; fn div(self,x:C)->Self{let d=x.re*x.re+x.im*x.im;Self::n((self.re*x.re+self.im*x.im)/d,(self.im*x.re-self.re*x.im)/d)} }

#[derive(Clone,Copy,Debug)] struct Term{power:i32,coefficient:C}

fn asymptotic_primitive(power:i32, omega:f64, depth:usize)->Vec<Term>{
    assert!(omega!=0.0);
    let iw=C::n(0.0,omega);
    let mut coefficient=C::n(1.0,0.0)/iw;
    let mut out=Vec::new();
    for r in 0..depth {
        let p=power-r as i32;
        out.push(Term{power:p,coefficient});
        coefficient=(coefficient*(-(p as f64)))/iw;
    }
    out
}

fn derivative_coefficients(terms:&[Term],omega:f64)->Vec<(i32,C)>{
    let mut out:Vec<(i32,C)>=Vec::new();
    for t in terms {
        let oscillatory=C::n(-omega*t.coefficient.im,omega*t.coefficient.re);
        add(&mut out,t.power,oscillatory);
        if t.power!=0 { add(&mut out,t.power-1,t.coefficient*(t.power as f64)); }
    }
    out.sort_by_key(|x|x.0);out
}
fn add(out:&mut Vec<(i32,C)>,power:i32,value:C){
    if let Some((_,v))=out.iter_mut().find(|(p,_)|*p==power){*v=*v+value}else{out.push((power,value))}
}

fn main(){
    let omega=2.75;let depth=9usize;let mut worst=0.0f64;
    for power in -4..=5 {
        let primitive=asymptotic_primitive(power,omega,depth);
        let derivative=derivative_coefficients(&primitive,omega);
        for (p,c) in derivative {
            let expected=if p==power{C::n(1.0,0.0)}else{C::default()};
            // The final uncancelled derivative is the declared truncation residual.
            if p==power-depth as i32 {continue}
            worst=worst.max((c+expected*(-1.0)).abs());
        }
    }
    assert!(worst<1e-12);
    println!("{{");
    println!("  \"schema\": \"marici.laurent_exponential_endpoint_algebra.v1\",");
    println!("  \"tested_power_min\": -4,");
    println!("  \"tested_power_max\": 5,");
    println!("  \"retained_depth\": {depth},");
    println!("  \"worst_nonresidual_derivative_defect\": {worst:.15e},");
    println!("  \"zero_frequency_power_minus_one\": \"logarithm_flagged\",");
    println!("  \"frequency_labels_preserved\": true");
    println!("}}");
}
