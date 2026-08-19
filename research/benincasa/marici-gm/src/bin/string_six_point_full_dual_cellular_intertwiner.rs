use serde_json::{json, Value};
use symbolica::prelude::*;

fn a(s: &str) -> Atom { Atom::parse(s, "marici", Default::default()).unwrap() }
fn clean(x: Atom) -> Atom { x.together().cancel().factor() }
fn read(path: &str) -> Value {
    serde_json::from_str(&std::fs::read_to_string(path).unwrap()).unwrap()
}
fn face(edge: &[Atom], u: &[Atom]) -> Atom {
    let mut out=a("0");
    for j in 0..6 {
        let suffix=((j+1)..6).map(|k|u[k].clone()).fold(a("1"),|p,x|clean(p*x));
        out += suffix*edge[j].clone();
    }
    clean(out)
}

fn main() {
    let prior=read("../string-six-point-pochhammer-cochain-closure.json");
    let u=vec![a("B34"),a("B24"),a("X"),a("1/B34"),a("1/B24"),a("1/X")];
    let dual_u:Vec<Atom>=u.iter().cloned().map(|x|clean(a("1")/x)).collect();
    let mut g=vec![a("1")];
    for k in 0..5 { g.push(clean(g[k].clone()/u[k].clone().pow(2_u32))); }
    assert_eq!(clean(g[5].clone()/u[5].clone().pow(2_u32)),g[0]);
    let h:Vec<Atom>=(0..6).map(|k|g[(k+1)%6].clone()).collect();
    let d:Vec<Atom>=prior["twisted_defects"].as_array().unwrap().iter().map(|x|a(x.as_str().unwrap())).collect();
    assert_eq!(face(&d,&u),a("0"));
    let mapped:Vec<Atom>=(0..6).map(|k|clean(h[k].clone()*d[k].clone())).collect();
    assert_eq!(face(&mapped,&dual_u),a("0"));

    // Coefficient comparison for arbitrary edge input:
    // w_dual,j h_j = g0 w_primal,j, hence D2=g0=1.
    for j in 0..6 {
        let wp=((j+1)..6).map(|k|u[k].clone()).fold(a("1"),|p,x|clean(p*x));
        let wd=((j+1)..6).map(|k|dual_u[k].clone()).fold(a("1"),|p,x|clean(p*x));
        assert_eq!(clean(wd*h[j].clone()),wp);
    }

    let packet=json!({
        "schema":"marici.benincasa.string_six_point_full_dual_cellular_intertwiner.v1",
        "transport":["B34","B24","X","B34^-1","B24^-1","X^-1"],
        "vertex_frame":g.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "edge_frame":h.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "face_frame":"1",
        "degree_zero_one_identity":"D1*delta0_u=delta0_(u^-1)*D0",
        "degree_one_two_identity":"D2*delta1_u=delta1_(u^-1)*D1",
        "entry_979_primal_face_boundary":"0",
        "entry_979_dual_face_boundary":face(&mapped,&dual_u).to_string(),
        "full_cellular_intertwiner_verified":true,
        "loaded_comparison_replaced":false,
        "conclusion":"The unique diagonal intertwiner extends through the native hexagon two-cell with D2=1 and transports Entry 979's complete exceptional coboundary to a dual coboundary."
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-full-dual-cellular-intertwiner.json",&text).unwrap();
    print!("{text}");
}
