use serde_json::json;
use std::fs;

fn main() {
    // At e=1/2, d_a log B(a,e)=psi(a)-psi(a+e).
    // The two digamma terms have disjoint infinite pole progressions.
    let count = 16;
    let integer_poles: Vec<String> = (0..count).map(|n| format!("-{n}")).collect();
    let half_integer_poles: Vec<String> =
        (0..count).map(|n| format!("-{n}-1/2")).collect();

    assert!(integer_poles.iter().all(|p| !half_integer_poles.contains(p)));
    let packet = json!({
        "schema": "marici.benincasa.string_beta_parameter_connection_gate.v1",
        "boundary_period": "B(a,e)=Gamma(a)Gamma(e)/Gamma(a+e)",
        "logarithmic_derivative": "d_a log B=psi(a)-psi(a+e)",
        "generic_slice": "e=1/2",
        "integer_pole_progression": integer_poles,
        "half_integer_pole_progression": half_integer_poles,
        "progressions_disjoint": true,
        "progressions_infinite": true,
        "rational_function_has_finitely_many_poles": true,
        "rank_one_rational_connection_possible": false,
        "required_enlargement": "digamma/logarithmic parameter extension"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    fs::write("../string-beta-parameter-connection-gate.json", &text).unwrap();
    print!("{text}");
}
