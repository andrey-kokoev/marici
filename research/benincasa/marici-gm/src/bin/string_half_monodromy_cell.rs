use std::{f64::consts::PI, fs};

#[derive(Clone, Copy)]
struct Complex { re: f64, im: f64 }

impl Complex {
    fn exp_i(theta: f64) -> Self { Self { re: theta.cos(), im: theta.sin() } }
    fn add(self, q: Self) -> Self { Self { re: self.re + q.re, im: self.im + q.im } }
    fn sub(self, q: Self) -> Self { Self { re: self.re - q.re, im: self.im - q.im } }
    fn mul(self, q: Self) -> Self { Self { re: self.re*q.re-self.im*q.im, im: self.re*q.im+self.im*q.re } }
    fn div(self, q: Self) -> Self { let d=q.re*q.re+q.im*q.im; Self { re:(self.re*q.re+self.im*q.im)/d, im:(self.im*q.re-self.re*q.im)/d } }
    fn scale(self, x: f64) -> Self { Self { re:self.re*x, im:self.im*x } }
    fn abs(self) -> f64 { self.re.hypot(self.im) }
}

fn main() {
    let (s,t)=(0.37_f64,0.61_f64);
    let one=Complex{re:1.0,im:0.0};
    let (ms,mt)=(Complex::exp_i(2.0*PI*s),Complex::exp_i(2.0*PI*t));
    let adjacent=Complex::exp_i(PI*s).div(ms.sub(one));
    let sine=Complex{re:0.0,im:-0.5/(PI*s).sin()};
    let adjacent_error=adjacent.sub(sine).abs();

    // Mizera's four source deformations, Eqs. (self-int-4)–(self-int-4d).
    let inv_s=one.div(ms.sub(one)); let inv_t=one.div(mt.sub(one));
    let f1=inv_s.scale(-1.0).add(one.scale(-1.0)).add(inv_t.scale(-1.0));
    let f2=ms.mul(inv_s).scale(-1.0).add(one).add(mt.mul(inv_t).scale(-1.0));
    let f3=inv_s.scale(-1.0).add(mt.mul(inv_t).scale(-1.0));
    let f4=ms.mul(inv_s).scale(-1.0).add(inv_t.scale(-1.0));
    let target=Complex{re:0.0,im:0.5*((PI*s).tan().recip()+(PI*t).tan().recip())};
    let deformation_error=[f1,f2,f3,f4].into_iter().map(|z|z.sub(target).abs()).fold(0.0,f64::max);
    let tolerance=2.0e-15;
    assert!(adjacent_error<tolerance && deformation_error<tolerance);
    let json=format!(concat!(
        "{{\n  \"s\": {:.17}, \"t\": {:.17},\n",
        "  \"half_monodromy\": {{\"re\": {:.17}, \"im\": {:.17}}},\n",
        "  \"sine_form\": {{\"re\": {:.17}, \"im\": {:.17}}},\n",
        "  \"adjacent_error\": {:.17e},\n",
        "  \"maximum_deformation_error\": {:.17e},\n",
        "  \"tolerance\": {:.1e},\n  \"passed\": true\n}}\n"),
        s,t,adjacent.re,adjacent.im,sine.re,sine.im,adjacent_error,deformation_error,tolerance);
    fs::write("../string-half-monodromy-cell.json",&json).expect("write packet");
    print!("{json}");
}
