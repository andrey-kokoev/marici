use std::process::Command;

fn run(path:&str,p:f64,q:f64,k:f64)->f64{
 let out=Command::new(path).env("MARICI_P",p.to_string()).env("MARICI_Q",q.to_string()).env("MARICI_K",k.to_string()).output().expect("run closure checker");assert!(out.status.success(),"closure checker failed at ({p},{q},{k})");let text=String::from_utf8(out.stdout).unwrap();
 let marker="\"maximum_annihilator_defect\":";let tail=text.split(marker).nth(1).expect("maximum defect field");tail.split(',').next().unwrap().trim().parse().unwrap()
}
fn main(){
 let points:[(f64,f64,f64);5]=[(1.1,0.8,0.9),(1.4,0.65,1.05),(0.95,1.2,0.72),(1.7,0.91,1.22),(0.78,0.56,1.11)];let mut maximum=0.0_f64;
 for(p,q,k)in points{assert!((q+k-p).abs()>0.1);let d1=run("research/benincasa/checkers/finite_time_grade1_boundary_closure.exe",p,q,k);let d0=run("research/benincasa/checkers/finite_time_grade0_boundary_closure.exe",p,q,k);maximum=maximum.max(d1).max(d0);println!("point=({p},{q},{k}) grade1={d1:.17e} grade0={d0:.17e}");}
 assert!(maximum<1e-8);println!("maximum_sweep_defect={maximum:.17e}");println!("kinematic_points=5");println!("both_omitted_grades_close=true");
}
