use std::process::Command;

#[derive(Clone,Copy,Debug,Default)]struct C{r:f64,i:f64}
impl C{fn n(r:f64,i:f64)->Self{Self{r,i}}fn abs(self)->f64{(self.r*self.r+self.i*self.i).sqrt()}}
impl std::ops::Add for C{type Output=Self;fn add(self,x:Self)->Self{Self::n(self.r+x.r,self.i+x.i)}}
impl std::ops::Sub for C{type Output=Self;fn sub(self,x:Self)->Self{Self::n(self.r-x.r,self.i-x.i)}}
impl std::ops::Mul for C{type Output=Self;fn mul(self,x:Self)->Self{Self::n(self.r*x.r-self.i*x.i,self.r*x.i+self.i*x.r)}}
impl std::ops::Mul<f64> for C{type Output=Self;fn mul(self,x:f64)->Self{Self::n(self.r*x,self.i*x)}}

fn sector(path:&str,eta:f64,frequency:&str)->C{
 let out=Command::new(path).env("MARICI_ETA",eta.to_string()).output().expect("run sector checker");assert!(out.status.success());let text=String::from_utf8(out.stdout).unwrap();
 for line in text.lines().filter(|x|x.starts_with("LOWER|")){let p:Vec<&str>=line.split('|').collect();if p[2]=="0"&&p[3]==frequency{return C::n(p[4].parse().unwrap(),p[5].parse().unwrap())}}
 panic!("missing grade-zero row at frequency {frequency}")
}
fn raw(eta:f64,frequency:&str)->C{
 let paths=["research/benincasa/checkers/finite_time_bulk_bulk_lower_grades.exe","research/benincasa/checkers/finite_time_mixed_lower_grades.exe","research/benincasa/checkers/finite_time_boundary_boundary_grade.exe"];
 paths.iter().fold(C::default(),|z,path|z+sector(path,eta,frequency))
}
fn oscillatory(eta:f64,p:f64)->C{let x=2.*p*eta;raw(eta,"2,0,0")*C::n(x.cos(),x.sin())}
fn interpolate(fm:C,f0:C,fp:C,h:f64)->[C;3]{[f0,(fp-fm)*(1./(2.*h)),(fp+fm-f0*2.)*(1./(2.*h*h))]}

fn main(){
 let p=std::env::var("MARICI_P").ok().and_then(|x|x.parse().ok()).unwrap_or(1.1);let h=0.2;let a=interpolate(oscillatory(-h,p),oscillatory(0.,p),oscillatory(h,p),h);let b=interpolate(raw(-h,"0,0,0"),raw(0.,"0,0,0"),raw(h,"0,0,0"),h);
 let probe=0.31;let ap=a[0]+a[1]*probe+a[2]*(probe*probe);let bp=b[0]+b[1]*probe+b[2]*(probe*probe);let interpolation_defect=(oscillatory(probe,p)-ap).abs().max((raw(probe,"0,0,0")-bp).abs());assert!(interpolation_defect<1e-10);
 assert!(b.iter().all(|z|z.i.abs()<1e-10));
 let c_cos=2.*a[0].r;let c_eta_cos=2.*a[1].r;let c_eta2_cos=2.*a[2].r;let c_sin=2.*a[0].i;let c_eta_sin=2.*a[1].i;let c_eta2_sin=2.*a[2].i;let c_one=b[0].r;let c_eta2=b[2].r;
 let obs=[c_eta_cos+2.*p*c_sin,p*p*c_sin+c_eta2_sin,p*p*c_cos+c_eta2_cos,-2.*p*c_cos+c_eta_sin,-p*p*c_one+c_eta2];let maximum=obs.iter().fold(b[1].abs(),|m,x|m.max(x.abs()));assert!(maximum<1e-9,"grade-zero closure obstruction {maximum}");
 println!("{{");println!("  \"schema\": \"marici.finite_time_grade0_boundary_closure.v1\",");println!("  \"interpolation_defect\": {:.17e},",interpolation_defect);println!("  \"response_coordinates\": {{ \"ReA\": {:.17e}, \"ImA\": {:.17e}, \"B\": {:.17e} }},",c_sin,c_cos,c_one);println!("  \"annihilator_values\": [{:.17e}, {:.17e}, {:.17e}, {:.17e}, {:.17e}],",obs[0],obs[1],obs[2],obs[3],obs[4]);println!("  \"zero_mode_linear_coefficient\": {:.17e},",b[1].r);println!("  \"maximum_annihilator_defect\": {:.17e},",maximum);println!("  \"grade0_closes_on_quadratic_boundary_response\": true");println!("}}");
}
