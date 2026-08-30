use serde_json::json;
use symbolica::prelude::*;

fn a(s:&str)->Atom{Atom::parse(s,"marici",Default::default()).unwrap()}

fn main(){
    let f=[
        a("2*u1^2+2*u2^2+u3^2-2*u1*u2-2*u2*u3"),
        a("2*u1^2+2*u2^2+u3^2-2*u1*u2-2*u2*u3-2*u1+1"),
        a("2*u1^2+2*u2^2+u3^2-2*u1*u2-2*u2*u3-2*u2+2"),
        a("2*u1^2+2*u2^2+u3^2-2*u1*u2-2*u2*u3-2*u3+3"),
        a("2*u1^2+2*u2^2+u3^2-2*u1*u2-2*u2*u3+2*u1+2*u2-8*u3+29"),
    ];
    // The four differences f_i-f_1 determine the only possible affine lift
    // of f_i(u')=f_{i+1}(u), with indices read cyclically.
    let up=[a("-u1+u2"),a("-u1+u3"),a("-2*u1-u2+4*u3-25/2")];
    let substitute=|source:&Atom|{
        source.clone()
            .replace(a("u1").to_pattern()).with(a("U1").to_pattern())
            .replace(a("u2").to_pattern()).with(a("U2").to_pattern())
            .replace(a("u3").to_pattern()).with(a("U3").to_pattern())
            .replace(a("U1").to_pattern()).with(up[0].to_pattern())
            .replace(a("U2").to_pattern()).with(up[1].to_pattern())
            .replace(a("U3").to_pattern()).with(up[2].to_pattern()).expand()
    };
    let residuals=(0..5).map(|i|(substitute(&f[i])-&f[(i+1)%5]).expand()).collect::<Vec<_>>();
    assert!(residuals.iter().any(|r|*r!=a("0")));
    let packet=json!({
        "schema":"marici.benincasa.five_site.asymmetric.cyclic_specialization.v1",
        "required_permutation":"f_i(u') = f_{i+1}(u)",
        "unique_affine_candidate":up.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "residuals":residuals.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "cyclic_affine_lift_exists":false,
        "reason":"the affine differences determine the candidate uniquely, and its common quadratic residual is nonzero"
    });
    std::fs::write("../results/five-site-asymmetric-cyclic-specialization.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
