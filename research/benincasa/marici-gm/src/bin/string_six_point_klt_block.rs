use std::{f64::consts::PI,fs};

#[derive(Clone,Copy)]struct C{re:f64,im:f64}
impl C{fn exp_i(x:f64)->Self{Self{re:x.cos(),im:x.sin()}}fn add(self,q:Self)->Self{Self{re:self.re+q.re,im:self.im+q.im}}fn sub(self,q:Self)->Self{Self{re:self.re-q.re,im:self.im-q.im}}fn mul(self,q:Self)->Self{Self{re:self.re*q.re-self.im*q.im,im:self.re*q.im+self.im*q.re}}fn div(self,q:Self)->Self{let d=q.re*q.re+q.im*q.im;Self{re:(self.re*q.re+self.im*q.im)/d,im:(self.im*q.re-self.re*q.im)/d}}fn scale(self,x:f64)->Self{Self{re:self.re*x,im:self.im*x}}fn abs(self)->f64{self.re.hypot(self.im)}}
fn csc(s:f64)->C{let m=C::exp_i(2.0*PI*s);C{re:0.0,im:2.0}.mul(C::exp_i(PI*s).div(m.sub(C{re:1.0,im:0.0})))}
fn cot(s:f64)->C{let m=C::exp_i(2.0*PI*s);C{re:0.0,im:2.0}.mul(C{re:1.0,im:0.0}.div(m.sub(C{re:1.0,im:0.0})).add(C{re:0.5,im:0.0}))}
fn mm(a:[[C;2];2],b:[[C;2];2])->[[C;2];2]{let z=C{re:0.0,im:0.0};let mut o=[[z;2];2];for i in 0..2{for j in 0..2{for k in 0..2{o[i][j]=o[i][j].add(a[i][k].mul(b[k][j]));}}}o}
fn inv(a:[[C;2];2])->[[C;2];2]{let det=a[0][0].mul(a[1][1]).sub(a[0][1].mul(a[1][0]));[[a[1][1].div(det),a[0][1].scale(-1.0).div(det)],[a[1][0].scale(-1.0).div(det),a[0][0].div(det)]]}
fn main(){
 let(s12,x,y,z)=(0.23_f64,0.37_f64,0.29_f64,-0.17_f64);let q=x+y+z;
 let a=csc(s12).mul(csc(x)).mul(csc(q));
 let b=csc(s12).mul(csc(q)).mul(cot(x).add(cot(y))).scale(-1.0);
 let c=csc(s12).mul(csc(q)).mul(cot(x).add(cot(z))).scale(-1.0);
 let block=[[a,b],[c,a]];let reconstructed=inv(block);
 let sp=|u:f64|(PI*u).sin();
 let published=[[
   C{re:-sp(s12)*sp(y)*sp(z),im:0.0},C{re:-sp(s12)*sp(z)*sp(x+y),im:0.0}],
   [C{re:-sp(s12)*sp(y)*sp(x+z),im:0.0},C{re:-sp(s12)*sp(y)*sp(z),im:0.0}]];
 let mut inverse_error=0.0_f64;for i in 0..2{for j in 0..2{inverse_error=inverse_error.max(reconstructed[i][j].sub(published[i][j]).abs());}}
 let identity=mm(block,published);let mut identity_error=0.0_f64;for i in 0..2{for j in 0..2{let e=if i==j{1.0}else{0.0};identity_error=identity_error.max(identity[i][j].sub(C{re:e,im:0.0}).abs());}}
 let det=block[0][0].mul(block[1][1]).sub(block[0][1].mul(block[1][0]));
 let expected_det=-1.0/(sp(s12).powi(2)*sp(x)*sp(y)*sp(z)*sp(q));
 let determinant_error=det.sub(C{re:expected_det,im:0.0}).abs();
 let trig_identity=sp(y)*sp(z)-sp(x+y)*sp(x+z)+sp(x)*sp(q);
 let tolerance=8.0e-15;assert!(inverse_error<tolerance&&identity_error<tolerance&&determinant_error<tolerance&&trig_identity.abs()<tolerance);
 let json=format!(concat!(
  "{{\n  \"source_block\": \"Mizera Eq. (six-point first 2x2 block)\",\n",
  "  \"s345_relation\": \"s345=s34+s35+s45\",\n",
  "  \"inverse_error\": {:.17e},\n  \"identity_error\": {:.17e},\n",
  "  \"determinant\": {{\"re\": {:.17}, \"im\": {:.17}}},\n",
  "  \"expected_determinant\": {:.17},\n  \"determinant_error\": {:.17e},\n",
  "  \"trigonometric_factorization_error\": {:.17e},\n",
  "  \"determinant_letters\": [\"s12\",\"s34\",\"s35\",\"s45\",\"s345\"],\n",
  "  \"new_mixed_divisor\": false,\n  \"tolerance\": {:.1e},\n  \"passed\": true\n}}\n"),
  inverse_error,identity_error,det.re,det.im,expected_det,determinant_error,trig_identity.abs(),tolerance);
 fs::write("../string-six-point-klt-block.json",&json).expect("write packet");print!("{json}");
}
