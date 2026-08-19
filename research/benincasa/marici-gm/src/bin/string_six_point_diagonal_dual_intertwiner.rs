use serde_json::json;
use symbolica::prelude::*;

fn a(s: &str) -> Atom { Atom::parse(s, "marici", Default::default()).unwrap() }
fn clean(x: Atom) -> Atom { x.together().cancel().factor() }

fn main() {
    let cycle = [0usize, 1, 4, 5, 3, 2];
    let mut sheets = Vec::new();

    for s in [-1_i32, 1] {
        for t in [-1_i32, 1] {
            let u = vec![
                clean(a(&t.to_string()) * a("Z") / a("A3")),
                clean(a(&s.to_string()) / (a("Z") * a("A2"))),
                a("X"),
                clean(a("A3") / (a(&t.to_string()) * a("Z"))),
                clean(a("Z") * a("A2") / a(&s.to_string())),
                a("1/X"),
            ];
            let mut g = vec![a("1")];
            for k in 0..5 {
                g.push(clean(g[k].clone() / u[k].clone().pow(2_u32)));
            }
            assert_eq!(clean(g[5].clone() / u[5].clone().pow(2_u32)), g[0]);
            let h: Vec<Atom> = (0..6).map(|k| g[(k + 1) % 6].clone()).collect();

            // Row k of D1 delta_u and delta_{u^-1} D0 has two entries.
            for k in 0..6 {
                assert_eq!(clean(-h[k].clone() * u[k].clone()), clean(-g[k].clone() / u[k].clone()));
                assert_eq!(h[k], g[(k + 1) % 6]);
            }

            let l = a(&(-16 * s * t).to_string());
            let dense = vec![a("0"), a("0"), a("0"), a("0"), l.clone(), -l];
            let vertex: Vec<Atom> = cycle.iter().map(|&i| dense[i].clone()).collect();
            let primal_edge: Vec<Atom> = (0..6).map(|k|
                clean(vertex[(k + 1) % 6].clone() - u[k].clone() * vertex[k].clone())
            ).collect();
            let mapped_vertex: Vec<Atom> = (0..6).map(|k| clean(g[k].clone() * vertex[k].clone())).collect();
            let mapped_edge: Vec<Atom> = (0..6).map(|k| clean(h[k].clone() * primal_edge[k].clone())).collect();
            let dual_edge: Vec<Atom> = (0..6).map(|k|
                clean(mapped_vertex[(k + 1) % 6].clone() - mapped_vertex[k].clone() / u[k].clone())
            ).collect();
            assert_eq!(mapped_edge, dual_edge);

            sheets.push(json!({
                "s":s,"t":t,
                "vertex_frame":g.iter().map(ToString::to_string).collect::<Vec<_>>(),
                "edge_frame":h.iter().map(ToString::to_string).collect::<Vec<_>>(),
                "mapped_primitive":mapped_vertex.iter().map(ToString::to_string).collect::<Vec<_>>(),
                "intertwiner_verified":true
            }));
        }
    }

    let packet = json!({
        "schema":"marici.benincasa.string_six_point_diagonal_dual_intertwiner.v1",
        "cycle":cycle,
        "identity":"D1*delta_u = delta_(u^-1)*D0",
        "recurrence":"g_(k+1)=g_k/u_k^2; h_k=g_(k+1)",
        "cyclic_consistency":"product(u_k)=1",
        "diagonal_solution_dimension":1,
        "normalization":"g_0=1 (global scalar remains)",
        "sheets":sheets,
        "conclusion":"The frozen transports canonically determine a diagonal primal-to-dual cellular intertwiner up to one global scalar, and it carries the minus primitive and its coboundary coherently.",
        "physical_pairing_identified":false
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-diagonal-dual-intertwiner.json",&text).unwrap();
    print!("{text}");
}
