use symbolica::prelude::*;

fn a(s:&str)->Atom { Atom::parse(s,"marici",Default::default()).unwrap().expand() }
fn sign(p:&[usize])->i32 { let mut n=0; for i in 0..p.len(){for j in i+1..p.len(){if p[i]>p[j]{n+=1}}} if n%2==0{1}else{-1} }
fn perms(v:&mut[usize],i:usize,out:&mut Vec<Vec<usize>>){if i==v.len(){out.push(v.to_vec());return}for j in i..v.len(){v.swap(i,j);perms(v,i+1,out);v.swap(i,j)}}
fn det(m:&[Vec<Atom>])->Atom{let mut v=(0..m.len()).collect::<Vec<_>>();let mut ps=Vec::new();perms(&mut v,0,&mut ps);let mut d=a("0");for p in ps{let mut q=a("1");for(i,&j)in p.iter().enumerate(){q=(q*&m[i][j]).expand()}d=(d+a(&sign(&p).to_string())*q).expand()}d}
fn coefficients(p:&Atom,var:Symbol,name:&str)->Vec<Atom>{let mut d=p.clone().expand();let mut fact=1usize;let mut out=Vec::new();loop{out.push((d.clone()/a(&fact.to_string())).replace(a(name).to_pattern()).with(a("0").to_pattern()).expand());let next=d.derivative(var).expand();if next==a("0"){break}d=next;fact*=out.len();}while out.len()>1&&out.last()==Some(&a("0")){out.pop();}out}
fn resultant(l:&Atom,r:&Atom,var:Symbol,name:&str)->Atom{let lc=coefficients(l,var,name);let rc=coefficients(r,var,name);let(ld,rd)=(lc.len()-1,rc.len()-1);let n=ld+rd;let mut m=vec![vec![a("0");n];n];let lrev=lc.iter().rev().cloned().collect::<Vec<_>>();let rrev=rc.iter().rev().cloned().collect::<Vec<_>>();for i in 0..rd{for(j,c)in lrev.iter().enumerate(){m[i][i+j]=c.clone()}}for i in 0..ld{for(j,c)in rrev.iter().enumerate(){m[rd+i][i+j]=c.clone()}}det(&m).expand().factor()}

fn main(){
 let z=a("0");let o=a("1");
 // A=y12^2=E^2/4 on the translated normal E+2*y12=0.
 let m=vec![
  vec![z.clone(),o.clone(),o.clone(),o.clone(),o.clone()],
  vec![o.clone(),z.clone(),a("E^2/4"),a("B"),a("C")],
  vec![o.clone(),a("E^2/4"),z.clone(),a("p2"),a("p1")],
  vec![o.clone(),a("B"),a("p2"),z.clone(),a("p3")],
  vec![o.clone(),a("C"),a("p1"),a("p3"),z.clone()],
 ];
 let k=det(&m).factor();
 let kb=k.derivative(symbol!("marici::B")).expand().factor();
 let kc=k.derivative(symbol!("marici::C")).expand().factor();
 println!("K={k}");println!("K_B={kb}");println!("K_C={kc}");
 let r1=resultant(&k,&kb,symbol!("marici::B"),"B");
 let r2=resultant(&kc,&kb,symbol!("marici::B"),"B");
 let landau=resultant(&r1,&r2,symbol!("marici::C"),"C").factor();
 println!("relative_landau={landau}");

 // Correctly typed grade-two sector S={12,23}: one normal E+2(a+b)=0.
 let m_grade2=vec![
  vec![a("0"),a("1"),a("1"),a("1"),a("1")],
  vec![a("1"),a("0"),a("aa^2"),a("(-E/2-aa)^2"),a("C")],
  vec![a("1"),a("aa^2"),a("0"),a("p2"),a("p1")],
  vec![a("1"),a("(-E/2-aa)^2"),a("p2"),a("0"),a("p3")],
  vec![a("1"),a("C"),a("p1"),a("p3"),a("0")],
 ];
 let kg2=det(&m_grade2).expand().factor();
 let kg2_soft=kg2.replace(a("p2").to_pattern()).with(a("0").to_pattern()).replace(a("E").to_pattern()).with(a("0").to_pattern()).factor();
 assert_eq!(kg2_soft,a("-2*aa^2*(p1-p3)^2").factor());
 println!("grade2_soft_restriction={kg2_soft}");
 let kg2_triangle=kg2.replace(a("p1").to_pattern()).with(a("r^2").to_pattern()).replace(a("p2").to_pattern()).with(a("s^2").to_pattern()).replace(a("p3").to_pattern()).with(a("(r+s)^2").to_pattern()).replace(a("E").to_pattern()).with(a("2*s").to_pattern()).factor();
 assert_eq!(kg2_triangle,a("-2*s^2*(C+2*aa*r-aa^2-r^2)^2").factor());
 println!("grade2_triangle_contact_restriction={kg2_triangle}");
 let kg2c=kg2.derivative(symbol!("marici::C")).expand().factor();
 let kg2a=kg2.derivative(symbol!("marici::aa")).expand().factor();
 let g2r1=resultant(&kg2,&kg2c,symbol!("marici::C"),"C");
 let g2r2=resultant(&kg2a,&kg2c,symbol!("marici::C"),"C");
 let g2landau=resultant(&g2r1,&g2r2,symbol!("marici::aa"),"aa").factor();
 println!("grade2_relative_landau={g2landau}");
 let component_landau=a("2048*p2^2*(p2-L^2)^3*(-2*p2*p1-2*p2*p3-2*p1*p3+p2^2+p1^2+p3^2)^3").factor();
 println!("two_distance_component_landau={component_landau}");

}
