use std::{f64::consts::PI, fs};

#[derive(Clone, Copy)]
struct Complex { re: f64, im: f64 }
impl Complex {
    fn exp_i(x:f64)->Self{Self{re:x.cos(),im:x.sin()}}
    fn add(self,q:Self)->Self{Self{re:self.re+q.re,im:self.im+q.im}}
    fn sub(self,q:Self)->Self{Self{re:self.re-q.re,im:self.im-q.im}}
    fn mul(self,q:Self)->Self{Self{re:self.re*q.re-self.im*q.im,im:self.re*q.im+self.im*q.re}}
    fn div(self,q:Self)->Self{let d=q.re*q.re+q.im*q.im;Self{re:(self.re*q.re+self.im*q.im)/d,im:(self.im*q.re-self.re*q.im)/d}}
    fn scale(self,x:f64)->Self{Self{re:self.re*x,im:self.im*x}}
    fn abs(self)->f64{self.re.hypot(self.im)}
}

fn pochhammer_csc(s:f64)->Complex {
    let mon=Complex::exp_i(2.0*PI*s);
    let half=Complex::exp_i(PI*s).div(mon.sub(Complex{re:1.0,im:0.0}));
    Complex{re:0.0,im:2.0}.mul(half)
}

fn pochhammer_cot(s:f64)->Complex {
    let mon=Complex::exp_i(2.0*PI*s);
    let endpoint=Complex{re:1.0,im:0.0}.div(mon.sub(Complex{re:1.0,im:0.0}));
    Complex{re:0.0,im:2.0}.mul(endpoint.add(Complex{re:0.5,im:0.0}))
}

fn main(){
    let (s12,s23,s24,s35,s45)=(9.0/20.0,1.0/2.0,-17.0/40.0,61.0/40.0,93.0/40.0);
    let (c12,c23,c35,c45)=(pochhammer_csc(s12),pochhammer_cot(s23),pochhammer_csc(s35),pochhammer_csc(s45));
    let t12=pochhammer_cot(s12);
    let m1=c45.mul(t12.add(c23)).scale(-1.0);
    let m2=c12.mul(c35).scale(-1.0);
    let k1=(PI*s23).sin()*(PI*s45).sin();
    let k2=(PI*s24).sin()*(PI*s35).sin();
    let assembled=[m1.scale(k1),m2.scale(k2)];
    let expected=[
        -((PI*(s12+s23)).sin()/(PI*s12).sin()),
        -((PI*s24).sin()/(PI*s12).sin()),
    ];
    let errors=[assembled[0].sub(Complex{re:expected[0],im:0.0}).abs(),assembled[1].sub(Complex{re:expected[1],im:0.0}).abs()];
    let local_errors=[
        c12.sub(Complex{re:(PI*s12).sin().recip(),im:0.0}).abs(),
        t12.sub(Complex{re:(PI*s12).tan().recip(),im:0.0}).abs(),
    ];
    let tolerance=2.0e-15;
    assert!(errors.into_iter().chain(local_errors).all(|e|e<tolerance));
    let json=format!(concat!(
        "{{\n  \"source_row\": [{{\"re\": {:.17}, \"im\": {:.17}}}, {{\"re\": {:.17}, \"im\": {:.17}}}],\n",
        "  \"diagonal_vertex_kernel\": [{:.17}, {:.17}],\n",
        "  \"assembled_circuit\": [{{\"re\": {:.17}, \"im\": {:.17}}}, {{\"re\": {:.17}, \"im\": {:.17}}}],\n",
        "  \"expected_circuit\": [{:.17}, {:.17}],\n",
        "  \"assembly_errors\": [{:.17e}, {:.17e}],\n",
        "  \"local_cell_errors\": [{:.17e}, {:.17e}],\n",
        "  \"tolerance\": {:.1e},\n  \"passed\": true\n}}\n"),
        m1.re,m1.im,m2.re,m2.im,k1,k2,assembled[0].re,assembled[0].im,
        assembled[1].re,assembled[1].im,expected[0],expected[1],errors[0],errors[1],
        local_errors[0],local_errors[1],tolerance);
    fs::write("../string-five-point-twisted-boundary.json",&json).expect("write packet");
    print!("{json}");
}
