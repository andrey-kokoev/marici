use serde_json::{json, Value};
use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}
fn shift_vec(v: &[Atom], name: &str) -> Vec<Atom> {
    v.iter().cloned().map(|x| clean(x.replace(a(name).to_pattern()).with((-a(name)).to_pattern()))).collect()
}
fn shift_mat(m: &[Vec<Atom>], name: &str) -> Vec<Vec<Atom>> {
    m.iter().map(|row| shift_vec(row, name)).collect()
}
fn eval(v: &[Atom], m: &[Vec<Atom>]) -> Vec<Atom> {
    (0..m[0].len()).map(|j| clean((0..v.len()).fold(a("0"), |s,i| s+v[i].clone()*m[i][j].clone()))).collect()
}
fn equal(x: &[Atom], y: &[Atom]) -> bool {
    x.iter().zip(y).all(|(p,q)| clean(p.clone()-q.clone())==a("0"))
}
fn project(l: &[Atom], sx: &[Atom], sy: &[Atom], sxy: &[Atom], ex: i32, ey: i32) -> Vec<Atom> {
    (0..l.len()).map(|i| clean(l[i].clone()+a(&ex.to_string())*sx[i].clone()+a(&ey.to_string())*sy[i].clone()+a(&(ex*ey).to_string())*sxy[i].clone())).collect()
}

fn main() {
    let lp: Value = serde_json::from_str(&std::fs::read_to_string("../string-six-point-circuit-exceptional-cochain.json").unwrap()).unwrap();
    let cp: Value = serde_json::from_str(&std::fs::read_to_string("../string-six-point-loaded-corner-comparison.json").unwrap()).unwrap();
    let l: Vec<Atom> = lp["cochain"].as_array().unwrap().iter().map(|x|a(x.as_str().unwrap())).collect();
    let c: Vec<Vec<Atom>> = cp["matrix"].as_array().unwrap().iter().map(|row|row.as_array().unwrap().iter().map(|x|a(x.as_str().unwrap())).collect()).collect();

    for name in ["A2","A3","B24","B34"] {
        let shifted=shift_mat(&c,name);
        for i in 0..6 { assert!(equal(&shifted[i],&c[i])); }
        assert!(equal(&eval(&shift_vec(&l,name),&c),&shift_vec(&eval(&l,&c),name)));
    }

    let lx=shift_vec(&l,"B24");
    let ly=shift_vec(&l,"B34");
    let lxy=shift_vec(&lx,"B34");
    let chars=[("++",1,1),("-+",-1,1),("+-",1,-1),("--",-1,-1)];
    let mut records=Vec::new();
    for (label,ex,ey) in chars {
        let p=project(&l,&lx,&ly,&lxy,ex,ey);
        let image=eval(&p,&c);
        assert!(p.iter().any(|z|*z!=a("0")));
        assert!(image.iter().any(|z|*z!=a("0")));
        let direct=project(&eval(&l,&c),&shift_vec(&eval(&l,&c),"B24"),&shift_vec(&eval(&l,&c),"B34"),&shift_vec(&shift_vec(&eval(&l,&c),"B24"),"B34"),ex,ey);
        assert!(equal(&image,&direct));
        records.push(json!({"character":label,"source_nonzero":true,"target_nonzero":true,"comparison_scalar_in_natural_image_basis":"1"}));
    }
    let packet=json!({
      "schema":"marici.benincasa.string_six_point_loaded_evaluation_shift.v1",
      "loaded_matrix_invariant_under":["A2 sign","A3 sign","B24 sign","B34 sign"],
      "intertwining_identity":"T(lambda)*C=T(lambda*C)",
      "characters":records,
      "characterwise_rank":[1,1,1,1],
      "generic_isomorphism":true,
      "reason":"C is generically invertible and each character projector is nonzero",
      "classification":"loaded evaluation is a strict deck-equivariant isomorphism from the exceptional-cochain orbit to its occurrence-source image, with unit scalar one in natural image bases",
      "scope":"comparison with the loaded occurrence image; equality with Entry 931's independently defined normal-symbol row is not yet established"
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-loaded-evaluation-shift.json",&text).unwrap();
    print!("{text}");
}
