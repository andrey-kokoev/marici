use serde_json::{json, Value};
use symbolica::prelude::*;

fn a(s: &str) -> Atom { Atom::parse(s, "marici", Default::default()).unwrap() }
fn clean(x: Atom) -> Atom { x.together().cancel().factor() }
fn shift(v: &[Atom], name: &str) -> Vec<Atom> {
    v.iter().cloned().map(|x| clean(x.replace(a(name).to_pattern()).with((-a(name)).to_pattern()))).collect()
}
fn minus_project(v: &[Atom]) -> Vec<Atom> {
    let x = shift(v, "B24");
    let y = shift(v, "B34");
    let xy = shift(&x, "B34");
    (0..v.len()).map(|i| clean(v[i].clone()-x[i].clone()-y[i].clone()+xy[i].clone())).collect()
}
fn restrict_sheet(x: Atom, s: i32, t: i32) -> Atom {
    let b24 = clean(a(&s.to_string()) / (a("Z") * a("A2")));
    let b34 = clean(a(&t.to_string()) * a("Z") / a("A3"));
    clean(x.replace(a("B24").to_pattern()).with(b24.to_pattern())
        .replace(a("B34").to_pattern()).with(b34.to_pattern()))
}

fn main() {
    let prior: Value = serde_json::from_str(&std::fs::read_to_string("../string-six-point-circuit-exceptional-cochain.json").unwrap()).unwrap();
    let lambda: Vec<Atom> = prior["cochain"].as_array().unwrap().iter().map(|x| a(x.as_str().unwrap())).collect();
    let lm = minus_project(&lambda);
    let cycle = [0usize,1,4,5,3,2];
    let transport = [a("B34"),a("B24"),a("X"),a("1/B34"),a("1/B24"),a("1/X")];
    let defects: Vec<Atom> = (0..6).map(|k| clean(lm[cycle[(k+1)%6]].clone()-transport[k].clone()*lm[cycle[k]].clone())).collect();
    let sheets: Vec<Value> = [-1,1].into_iter().flat_map(|s| [-1,1].into_iter().map(move |t|(s,t))).map(|(s,t)| {
        let restricted_primitive: Vec<Atom> = lm.iter().cloned().map(|x|restrict_sheet(x,s,t)).collect();
        let restricted: Vec<Atom> = defects.iter().cloned().map(|x|restrict_sheet(x,s,t)).collect();
        let nonzero: Vec<usize> = restricted.iter().enumerate().filter_map(|(i,x)|(*x!=a("0")).then_some(i)).collect();
        assert_eq!(nonzero, vec![1,2,3]);
        let tr: Vec<Atom> = transport.iter().cloned().map(|x|restrict_sheet(x,s,t)).collect();
        let mut boundary=a("0");
        for j in 0..6 {
            let suffix=((j+1)..6).map(|k|tr[k].clone()).fold(a("1"),|p,u|clean(p*u));
            boundary += suffix*restricted[j].clone();
        }
        let boundary=clean(boundary);
        assert_eq!(boundary,a("0"));
        let primitive_support: Vec<usize> = restricted_primitive.iter().enumerate().filter_map(|(i,x)|(*x!=a("0")).then_some(i)).collect();
        assert_eq!(primitive_support,vec![4,5]);
        json!({"s":s,"t":t,"restricted_primitive":restricted_primitive.iter().map(ToString::to_string).collect::<Vec<_>>(),"primitive_nonzero_indices":primitive_support,"restricted_defects":restricted.iter().map(ToString::to_string).collect::<Vec<_>>(),"nonzero_indices":nonzero,"transported_boundary":boundary.to_string(),"edge_class_in_image_of_delta":true})
    }).collect();
    let packet=json!({
        "schema":"marici.benincasa.string_six_point_minus_recombination_edge_restriction.v1",
        "projector":"1-T24-T34+T24*T34 (unnormalized)",
        "cycle":cycle,
        "recombination_substitution":{"B24":"s/(Z*A2)","B34":"t*Z/A3","s_squared":1,"t_squared":1},
        "projected_cochain":lm.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "projected_twisted_defects":defects.iter().map(ToString::to_string).collect::<Vec<_>>(),
        "sheet_restrictions":sheets,
        "classification":"on every signed recombination sheet the -- edge class is a closed three-edge arc, not the two-edge star of the unique incident chamber vertex",
        "local_vertex_cousin_image_matches":false,
        "twisted_cellular_cohomology_class":"zero: the displayed restricted primitive maps exactly to the three-edge arc",
        "scope":"restriction of Entry 979's -- character edge cochain to Entry 999's recombination locus; no physical-cycle interpretation"
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-minus-recombination-edge-restriction.json",&text).unwrap();
    print!("{text}");
}
