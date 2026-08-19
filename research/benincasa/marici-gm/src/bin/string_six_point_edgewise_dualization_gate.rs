use serde_json::json;
use symbolica::prelude::*;

fn a(s: &str) -> Atom { Atom::parse(s, "marici", Default::default()).unwrap() }
fn clean(x: Atom) -> Atom { x.together().cancel().factor() }

fn closure(edge: &[Atom], transport: &[Atom]) -> Atom {
    let mut out = a("0");
    for j in 0..edge.len() {
        let suffix = ((j + 1)..edge.len())
            .map(|k| transport[k].clone())
            .fold(a("1"), |p, x| clean(p * x));
        out += suffix * edge[j].clone();
    }
    clean(out)
}

fn main() {
    let cycle = [0usize, 1, 4, 5, 3, 2];
    let mut records = Vec::new();

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
            let l = a(&(-16 * s * t).to_string());
            let dense = vec![a("0"), a("0"), a("0"), a("0"), l.clone(), -l.clone()];
            let vertex: Vec<Atom> = cycle.iter().map(|&i| dense[i].clone()).collect();
            let edge: Vec<Atom> = (0..6)
                .map(|k| clean(vertex[(k + 1) % 6].clone() - u[k].clone() * vertex[k].clone()))
                .collect();
            assert_eq!(closure(&edge, &u), a("0"));

            let dual_transport: Vec<Atom> = u.iter().cloned().map(|x| clean(a("1") / x)).collect();
            for exponent in [1_u32, 2] {
                let scaled: Vec<Atom> = edge.iter().cloned().zip(u.iter().cloned())
                    .map(|(d, x)| clean(-x.pow(exponent) * d)).collect();
                let obstruction = closure(&scaled, &dual_transport);
                assert_ne!(obstruction, a("0"));
                records.push(json!({
                    "s": s,
                    "t": t,
                    "unit_convention": if exponent == 1 { "-u_e" } else { "-u_e^2" },
                    "dual_closure_obstruction": obstruction.to_string(),
                    "is_dual_coboundary": false
                }));
            }
        }
    }

    let packet = json!({
        "schema": "marici.benincasa.string_six_point_edgewise_dualization_gate.v1",
        "cycle": cycle,
        "primal_transport": ["t*Z/A3","s/(Z*A2)","X","A3/(t*Z)","Z*A2/s","1/X"],
        "primitive_dense_support": [4,5],
        "primal_coboundary_closed": true,
        "tests": records,
        "conclusion": "Independent edgewise multiplication by the local dual Pochhammer unit is not a cochain map, whether the serialized transport is taken as monodromy or its square root.",
        "required_datum": "A source-derived global chain/cochain pairing with vertex as well as edge normalization."
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-edgewise-dualization-gate.json", &text).unwrap();
    print!("{text}");
}
