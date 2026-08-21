use std::collections::BTreeMap;
use std::process::Command;

#[derive(Clone,Copy,Debug,Default)]struct C{r:f64,i:f64}
impl std::ops::AddAssign for C{fn add_assign(&mut self,x:Self){self.r+=x.r;self.i+=x.i}}
impl C{fn abs(self)->f64{(self.r*self.r+self.i*self.i).sqrt()}}

type Key=([i32;3],i32,[i32;3],i32);

fn triple(s:&str)->[i32;3]{let v:Vec<i32>=s.split(',').map(|x|x.parse().unwrap()).collect();[v[0],v[1],v[2]]}
fn collect(path:&str,expected:&str)->BTreeMap<Key,C>{
 let out=Command::new(path).output().expect("run route checker");assert!(out.status.success());let text=String::from_utf8(out.stdout).unwrap();let mut map=BTreeMap::new();
 for line in text.lines().filter(|x|x.starts_with("OBS|")){let p:Vec<&str>=line.split('|').collect();assert_eq!(p.len(),9);assert_eq!(p[1],expected);let key=(triple(p[2]),p[3].parse().unwrap(),triple(p[4]),p[5].parse().unwrap());let c=C{r:p[7].parse().unwrap(),i:p[8].parse().unwrap()};*map.entry(key).or_default()+=c;}
 map
}

fn main(){
 let bb=collect("research/benincasa/checkers/finite_time_bulk_bulk_lower_grades.exe","BB");
 let bs=collect("research/benincasa/checkers/finite_time_mixed_lower_grades.exe","BS");
 assert_eq!(bb.len(),bs.len());let mut maximum=0.0_f64;
 for(k,a)in&bb{let defect=*a;let mut combined=defect;combined+=*bs.get(k).expect("matching mixed primitive");maximum=maximum.max(combined.abs());}
 assert!(maximum<1e-12,"endpoint cancellation defect {maximum}");
 println!("{{");println!("  \"schema\": \"marici.finite_time_observation_endpoint_cancellation.v1\",");println!("  \"canonical_primitive_classes\": {},",bb.len());println!("  \"maximum_absolute_defect\": {:.17e},",maximum);println!("  \"bulk_bulk_plus_mixed_cancels\": true");println!("}}");
}
