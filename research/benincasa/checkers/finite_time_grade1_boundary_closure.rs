use std::process::Command;

#[derive(Clone,Copy,Debug,Default)]struct C{r:f64,i:f64}
impl C{fn n(r:f64,i:f64)->Self{Self{r,i}}fn abs(self)->f64{(self.r*self.r+self.i*self.i).sqrt()}}
impl std::ops::Add for C{type Output=Self;fn add(self,x:Self)->Self{Self::n(self.r+x.r,self.i+x.i)}}
impl std::ops::Sub for C{type Output=Self;fn sub(self,x:Self)->Self{Self::n(self.r-x.r,self.i-x.i)}}
impl std::ops::Mul for C{type Output=Self;fn mul(self,x:Self)->Self{Self::n(self.r*x.r-self.i*x.i,self.r*x.i+self.i*x.r)}}
impl std::ops::Mul<f64> for C{type Output=Self;fn mul(self,x:f64)->Self{Self::n(self.r*x,self.i*x)}}

fn sector(path:&str,eta:f64)->C{
 let out=Command::new(path).env("MARICI_ETA",eta.to_string()).output().expect("run sector checker");assert!(out.status.success());let text=String::from_utf8(out.stdout).unwrap();
 for line in text.lines().filter(|x|x.starts_with("LOWER|")){let p:Vec<&str>=line.split('|').collect();if p[2]=="1"&&p[3]=="2,0,0"{return C::n(p[4].parse().unwrap(),p[5].parse().unwrap())}}
 panic!("missing grade-one positive-frequency row")
}
fn coefficient(eta:f64,p:f64)->C{
 let paths=["research/benincasa/checkers/finite_time_bulk_bulk_lower_grades.exe","research/benincasa/checkers/finite_time_mixed_lower_grades.exe","research/benincasa/checkers/finite_time_boundary_boundary_grade.exe"];
 let raw=paths.iter().fold(C::default(),|z,path|z+sector(path,eta));let x=2.*p*eta;raw*C::n(x.cos(),x.sin())
}
fn main(){
 let p=std::env::var("MARICI_P").ok().and_then(|x|x.parse().ok()).unwrap_or(1.1);let h=0.2;let fm=coefficient(-h,p);let f0=coefficient(0.,p);let fp=coefficient(h,p);let a0=f0;let a1=(fp-fm)*(1./(2.*h));let a2=(fp+fm-f0*2.)*(1./(2.*h*h));
 let probe=0.31;let reconstructed=a0+a1*probe+a2*(probe*probe);let interpolation_defect=(coefficient(probe,p)-reconstructed).abs();assert!(interpolation_defect<1e-11);
 // A(eta)e^{-i theta}+conjugate = 2 Re(A) cos(theta)+2 Im(A) sin(theta).
 let c_cos=2.*a0.r;let c_eta_cos=2.*a1.r;let c_eta2_cos=2.*a2.r;let c_sin=2.*a0.i;let c_eta_sin=2.*a1.i;let c_eta2_sin=2.*a2.i;
 let obs=[c_eta_cos+2.*p*c_sin,p*p*c_sin+c_eta2_sin,p*p*c_cos+c_eta2_cos,-2.*p*c_cos+c_eta_sin,0.0_f64];let maximum=obs.iter().fold(0.0_f64,|m,x|m.max(x.abs()));assert!(maximum<1e-10,"grade-one closure obstruction {maximum}");
 println!("{{");println!("  \"schema\": \"marici.finite_time_grade1_boundary_closure.v1\",");println!("  \"interpolation_defect\": {:.17e},",interpolation_defect);println!("  \"response_coordinates\": {{ \"ReA\": {:.17e}, \"ImA\": {:.17e}, \"B\": 0 }},",c_sin,c_cos);println!("  \"annihilator_values\": [{:.17e}, {:.17e}, {:.17e}, {:.17e}, 0],",obs[0],obs[1],obs[2],obs[3]);println!("  \"maximum_annihilator_defect\": {:.17e},",maximum);println!("  \"grade1_closes_on_quadratic_boundary_response\": true");println!("}}");
}
