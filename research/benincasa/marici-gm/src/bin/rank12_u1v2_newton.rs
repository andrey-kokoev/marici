use symbolica::prelude::*;

fn a(s:&str)->Atom{Atom::parse(s,"marici",Default::default()).unwrap().expand()}
fn pulled(e:&Atom)->Atom{let mut o=e.clone();for v in ["p","q","A","B"]{o=o.replace(a(v).to_pattern()).with(a(&format!("rho*{v}h")).to_pattern()).expand();}o}
fn coeff(e:&Atom,n:usize)->Atom{let rho=symbol!("marici::rho");let mut d=pulled(e);for _ in 0..n{d=d.derivative(rho).expand();}let f=(1..=n).product::<usize>().max(1);(d/a(&f.to_string())).replace(a("rho").to_pattern()).with(a("0").to_pattern()).expand()}
fn val(e:&Atom)->(usize,Atom){for n in 0..=12{let c=coeff(e,n);if c!=a("0"){return(n,c)}}panic!("valuation bound")}

fn main(){
 let u=a("1+p");let v=a("2+q");let aa=a("1/2+A");let bb=a("B");
 let x=a("1");let y=((&u+&v-a("2"))/a("2")).expand();let z=((&u-&v)/a("2")).expand();let c=(-u.clone()).expand();
 let h=(&x*&x+&y*&y-&z*&z).expand();
 let ga=((&x*&x-&c*&c)*(&x*&x-&y*&y-&z*&z)-a("2")*&c*&c*&z*&z).expand();
 let gb=((&y*&y-&c*&c)*(&y*&y-&x*&x-&z*&z)-a("2")*&c*&c*&z*&z).expand();
 let hh=(&z*&z*((&c*&c-&y*&y)*(&c*&c-&x*&x)+&c*&c*&z*&z)).expand();
 let k=(&aa*&aa*&aa*&aa-&h*&aa*&aa*&bb*&bb+&y*&y*&bb*&bb*&bb*&bb+&ga*&aa*&aa+&gb*&bb*&bb+&hh).expand();
 let k1a=(-a("2")*&c*(a("1")-&y*&y+&z*&z)).expand();let k1b=(-a("2")*&c*(&y*&y-a("1")+&z*&z)).expand();
 let k1h=(a("2")*&c*&z*&z*(a("2")*&c*&c-a("1")-&y*&y+&z*&z)).expand();let k1=(&k1a*&aa*&aa+&k1b*&bb*&bb+&k1h).expand();
 let l1=(&bb+a("1")-&u).expand();let l2=(&aa+(&v-a("2")-&u)/a("2")).expand();
 let(vk,ik)=val(&k);let(vk1,ik1)=val(&k1);let(vl1,il1)=val(&l1);let(vl2,il2)=val(&l2);
 println!("center=(u,v,a,b)=(1,2,1/2,0)");println!("joint_ideal=(p,q,A,B)");
 println!("nu_K={vk}");println!("K_initial={}",ik.factor());println!("nu_K1={vk1}");println!("K1_initial={}",ik1.factor());
 println!("nu_L1={vl1}");println!("L1_initial={il1}");println!("nu_L2={vl2}");println!("L2_initial={il2}");
 for n in vk..=6{println!("K_radial_{n}={}",coeff(&k,n));}for n in vk1..=5{println!("K1_radial_{n}={}",coeff(&k1,n));}
 let k3_plane=coeff(&k,3).replace(a("Ah").to_pattern()).with(a("(ph+qh)/2").to_pattern()).expand().factor();
 println!("K3_on_double_plane={k3_plane}");
 let form_orders=[-1_i32,0,0,2,1,0,2,1,0,1,1,3];println!("relative_form_orders={form_orders:?}");
}
