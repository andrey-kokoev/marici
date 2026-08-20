use symbolica::prelude::*;

fn a(s:&str)->Atom { Atom::parse(s,"marici",Default::default()).unwrap().expand() }
fn coeff(mut f:Atom,n:usize)->Atom {
    let t=symbol!("marici::T");
    for _ in 0..n { f=f.derivative(t).expand(); }
    let fact=(1..=n).product::<usize>().max(1);
    (f/a(&fact.to_string())).replace(a("T").to_pattern()).with(a("0").to_pattern()).expand()
}
fn main(){
    let g=a("28*s*A+8*A*B+17*s^2-12*A^2-8*s*A*B+4*s*A^2-39*s-26*A-12*B+39-2*s^2*A-4*s^2*B-s^3+8*A^3");
    let h=a("52*s+32*A+8*B-16*s*A-8*s*B-74-10*s^2+8*A^2");
    let sub=a("(3-s-T)/2");
    let gt=g.replace(a("A").to_pattern()).with(sub.to_pattern()).expand();
    let ht=h.replace(a("A").to_pattern()).with(sub.to_pattern()).expand();
    let g3=coeff(gt.clone(),3); let h2=coeff(ht.clone(),2);
    let residue=(h2.clone()/a("32")+a("3")*g3.clone()/a("16")).expand();
    assert_eq!(residue,a("-1/8"));
    println!("{{\"schema\":\"marici.benincasa.rank12_u2v0_e6_first_rees_residue.v2\",\"K3_T3\":\"{}\",\"K12_T2\":\"{}\",\"plus_sheet_Tminus1_residue\":\"{}\",\"minus_sheet_Tminus1_residue\":\"1/8\",\"anti_invariant_class\":\"(-1/8)*(e_plus-e_minus)\",\"bulk_class_zero\":false,\"moving_conductor_support\":\"s*(B-1)=0\",\"conclusion\":\"e6 is exact at leading grade but has a nonzero anti-invariant first-Rees node residue\"}}",g3,h2,residue);
}
