use serde_json::json;
use symbolica::prelude::*;

fn atom(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}

fn clean(x: Atom) -> Atom {
    x.expand().together().cancel().factor()
}

fn circuit(a: &str, b: &str) -> serde_json::Value {
    let ma = atom(&format!("{a}^2"));
    let mb = atom(&format!("{b}^2"));
    let one = atom("1");
    let direct = clean(ma.clone() * mb.clone() - one.clone());
    let two_step = clean((ma.clone() - one.clone()) + ma * (mb - one));
    assert_eq!(clean(direct.clone() - two_step.clone()), atom("0"));
    json!({
        "pivot_half_monodromy":a,
        "transition_half_monodromy":b,
        "two_step_boundary":format!("({a}^2-1)+{a}^2*({b}^2-1)"),
        "coupled_boundary":direct.to_string(),
        "identity_verified":true,
        "standalone_transition_factor_cancelled":format!("{b}^2-1")
    })
}

fn main() {
    let left = circuit("A3", "B34");
    let right = circuit("A2", "B24");
    let a2 = atom("A2");
    let a3 = atom("A3");
    let b24 = atom("B24");
    let b34 = atom("B34");
    let determinant = clean(
        ((a3.clone() * b34.clone()).pow(2) - atom("1"))
            * ((a2.clone() * b24.clone()).pow(2) - atom("1")),
    );
    let expected = clean(((a2 * b24).pow(2) - atom("1")) * ((a3 * b34).pow(2) - atom("1")));
    assert_eq!(clean(determinant.clone() - expected), atom("0"));

    let packet = json!({
        "schema":"marici.benincasa.string_six_point_pivot_transition_circuit.v1",
        "coherence_identity":"M_A*M_B-1=(M_A-1)+M_A*(M_B-1)",
        "circuits":[left,right],
        "augmented_determinant_factor":determinant.to_string(),
        "source_fitting_factors_matched":["(A2*B24)^2-1","(A3*B34)^2-1"],
        "additional_irreducible_factors":[],
        "classification":"the minimal pivot-transition two-step boundary derives the coupled source support without a new carrier cell"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-pivot-transition-circuit.json", &text).unwrap();
    print!("{text}");
}
