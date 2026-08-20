use serde_json::json;
use std::fs;
use symbolica::prelude::*;

fn a(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default()).unwrap().expand()
}

fn det(m: &[Vec<Atom>]) -> Atom {
    if m.len() == 1 { return m[0][0].clone(); }
    let mut out = a("0");
    for j in 0..m.len() {
        let minor: Vec<Vec<Atom>> = m[1..].iter()
            .map(|row| row.iter().enumerate().filter(|(k, _)| *k != j)
                 .map(|(_, x)| x.clone()).collect()).collect();
        let term = m[0][j].clone() * det(&minor);
        if j % 2 == 0 { out += term; } else { out -= term; }
    }
    out.expand()
}

fn adj(m: &[Vec<Atom>]) -> Vec<Vec<Atom>> {
    let n = m.len();
    let mut out = vec![vec![a("0"); n]; n];
    for i in 0..n {
        for j in 0..n {
            let minor: Vec<Vec<Atom>> = m.iter().enumerate().filter(|(r, _)| *r != j)
                .map(|(_, row)| row.iter().enumerate().filter(|(c, _)| *c != i)
                     .map(|(_, x)| x.clone()).collect()).collect();
            let cofactor = det(&minor);
            out[i][j] = if (i + j) % 2 == 0 { cofactor } else { -cofactor };
        }
    }
    out
}

fn quad(m: &[Vec<Atom>], x: &[Atom], y: &[Atom]) -> Atom {
    let mut out = a("0");
    for i in 0..x.len() {
        for j in 0..y.len() { out += x[i].clone()*m[i][j].clone()*y[j].clone(); }
    }
    out.expand()
}

fn main() {
    let g = vec![
        vec![a("g11"),a("g12"),a("g13"),a("g14")],
        vec![a("g12"),a("g22"),a("g23"),a("g24")],
        vec![a("g13"),a("g23"),a("g33"),a("g34")],
        vec![a("g14"),a("g24"),a("g34"),a("g44")],
    ];
    let determinant = det(&g);
    let adjugate = adj(&g);
    let delta = (1..=4).map(|i| a(&format!("D{i}"))).collect::<Vec<_>>();
    let mass = (1..=4).map(|i| a(&format!("S{i}"))).collect::<Vec<_>>();
    let rho = a("rho");
    let half = a("1/2");
    let v = (0..4).map(|i| half.clone()*(delta[i].clone()/rho.clone().pow(2)-mass[i].clone()))
        .collect::<Vec<_>>();
    let source = (rho.clone().pow(4) *
        (determinant.clone()*a("Y1^2")/rho.clone().pow(2)-quad(&adjugate,&v,&v)))
        .together().cancel().expand();
    let k0 = -a("1/4")*quad(&adjugate,&delta,&delta);
    let k2 = determinant.clone()*a("Y1^2") + a("1/2")*quad(&adjugate,&delta,&mass);
    let k4 = -a("1/4")*quad(&adjugate,&mass,&mass);
    let expected = (k0.clone()+rho.clone().pow(2)*k2.clone()+rho.clone().pow(4)*k4.clone()).expand();
    assert_eq!((source-expected).expand(),a("0"));
    // Regard z=rho^2 as the radial coordinate.  The collision of its two
    // branch roots is intrinsic coefficient support, with discriminant
    // K2^2-4*K0*K4.  Verify the completed-square normal form exactly.
    let z = a("z");
    let radial_discriminant =
        (k2.clone().pow(2)-a("4")*k0.clone()*k4.clone()).expand();
    let completed_square =
        (a("4")*k4.clone()*(k4.clone()*z.clone().pow(2)+k2.clone()*z+k0.clone())
         -(a("2")*k4.clone()*a("z")+k2.clone()).pow(2)
         +radial_discriminant.clone()).expand();
    assert_eq!(completed_square,a("0"));
    let packet=json!({
        "schema":"marici.benincasa.five_site_radial_cm_rees.v1",
        "engine":"Symbolica 2.2 exact characteristic-zero identity",
        "source":"rho^4*(det(G)*Y1^2/rho^2-v^T adj(G) v), v=(Delta/rho^2-S)/2",
        "K0":"-(1/4) Delta^T adj(G) Delta",
        "K2":"det(G) Y1^2+(1/2) Delta^T adj(G) S",
        "K4":"-(1/4) S^T adj(G) S",
        "radial_coordinate":"z=rho^2",
        "radial_collision_discriminant":"K2^2-4*K0*K4",
        "radial_collision_expanded":"(det(G)Y1^2+(1/2)Delta^T adj(G)S)^2-(1/4)(Delta^T adj(G)Delta)(S^T adj(G)S)",
        "completed_square_identity":"4*K4*(K4*z^2+K2*z+K0)=(2*K4*z+K2)^2-(K2^2-4*K0*K4)",
        "generic_collision_type":"A1 coefficient degeneration in the z-line",
        "nonzero_radial_orders":[0,2,4],
        "first_ordinary_normal_grade":0,
        "first_nontrivial_branch_grade":2,
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-radial-cm-rees.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
