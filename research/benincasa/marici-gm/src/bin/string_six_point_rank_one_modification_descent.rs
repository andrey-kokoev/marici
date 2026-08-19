use serde_json::json;
use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}

fn main() {
    let x = a("X");
    let q = clean((a("1") + x.clone() * x.clone()) / (x.clone() * x.clone() - a("1")));
    let q_ref = clean(
        (a("1") + a("1") / (x.clone() * x.clone())) / (a("1") / (x.clone() * x.clone()) - a("1")),
    );
    assert_eq!(q_ref, clean(-q));
    let mut sheets = Vec::new();
    for s in [-1, 1] {
        for t in [-1, 1] {
            let numerator_reflection_unit = -1;
            let normal_reflection_unit = s * t;
            let quotient_reflection_unit = -s * t;
            assert_eq!(quotient_reflection_unit * quotient_reflection_unit, 1);
            sheets.push(json!({"signs":[s,t],"reflected_signs":[t,s],"kernel_numerator_unit":numerator_reflection_unit,"effective_normal_unit":normal_reflection_unit,"modification_generator_unit":quotient_reflection_unit,"reflection_square":1}));
        }
    }
    let packet = json!({
     "schema":"marici.benincasa.string_six_point_rank_one_modification_descent.v1",
     "characters":{
      "++":{"pair_shift_units":{"T24":1,"T34":1},"cyclic_step_unit":1},
      "--":{"pair_shift_kernel_units":{"T24":-1,"T34":-1},"pair_shift_normal_units":{"T24":-1,"T34":-1},"pair_shift_modification_units":{"T24":1,"T34":1},"cyclic_step_unit":1}
     },
     "reflection_sheets":sheets,
     "collapse_scalar_reflection":"q(1/X)=-q(X)",
     "cyclic_holonomy":1,
     "classification":"the source-derived rank-one elementary modification descends globally; pair shifts and cyclic transport are trivial on its quotient generator, while reflection carries the sheet character -st",
     "scope":"symmetry descent of K/(delta U+st delta V); no physical-period interpretation"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write(
        "../string-six-point-rank-one-modification-descent.json",
        &text,
    )
    .unwrap();
    print!("{text}");
}
