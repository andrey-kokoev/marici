// Historical geometry-only diagnostic. Entry 2135 withdrew its cosmological
// interpretation because the all-deleted graph has component-resolved poles.
use symbolica::prelude::*;
fn a(s:&str)->Atom{Atom::parse(s,"marici",Default::default()).unwrap().expand()}
fn main(){
 let lambda=a("p1^2+p2^2+p3^2-2*p1*p2-2*p2*p3-2*p3*p1");
 let f=(a("(E^2-2*(p1+p2+p3))^2")+a("12")*lambda).expand().factor();
 println!("grade3_fermat_discriminant={f}");
 let hom=f
  .replace(a("E").to_pattern()).with(a("x+y+z").to_pattern())
  .replace(a("p1").to_pattern()).with(a("x^2").to_pattern())
  .replace(a("p2").to_pattern()).with(a("y^2").to_pattern())
  .replace(a("p3").to_pattern()).with(a("z^2").to_pattern()).expand().factor();
 let q=a("-16*(x*y)^2-8*x*y*(x+y+z)^2+8*(x+y)*(x+y+z)^3-5*(x+y+z)^4").factor();
 let fermat_param=f.clone()
  .replace(a("E").to_pattern()).with(a("-2*(r1+r2+r3)").to_pattern())
  .replace(a("p1").to_pattern()).with(a("r2^2+r3^2+r2*r3").to_pattern())
  .replace(a("p2").to_pattern()).with(a("r1^2+r3^2+r1*r3").to_pattern())
  .replace(a("p3").to_pattern()).with(a("r1^2+r2^2+r1*r2").to_pattern()).expand();
 assert_eq!(fermat_param,a("0"));
 println!("fermat_parameterization_check=0");
 println!("homogeneous_fermat={hom}");
 println!("published_Q={q}");
 println!("difference={}",(hom.clone()-q.clone()).expand().factor());
 println!("sum={}",(hom+q).expand().factor());
}
