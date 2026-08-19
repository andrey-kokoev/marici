use serde_json::json;
use std::fs;

fn main() {
    let exponent_derivative = "A_c d/dA_c KN = alpha'/(i*pi) log(f_c) KN";
    let frozen_packet = [
        "six constant word labels",
        "momentum/intersection kernel",
        "dense-to-block transition",
        "occurrence and residue orientations",
        "Cartier normal symbols",
    ];
    let absent_from_packet = [
        "period vector in the six-word frame",
        "reduction of logarithmic insertions",
        "ambient tangential connection matrix",
    ];

    let packet = json!({
        "schema": "marici.benincasa.string_six_point_connection_type_gate.v1",
        "monodromy_coordinate": "A_c=exp(i*pi*s_c)",
        "exponent_derivative": exponent_derivative,
        "frozen_packet_contains": frozen_packet,
        "frozen_packet_lacks": absent_from_packet,
        "serialized_derivative_is": "the trivial connection on constant word labels",
        "source_parameter_derivative_requires": "a logarithmic-insertion/unipotent enlargement or an independently reduced period connection",
        "rank_two_descent_authorized": false,
        "carrier_consequence": "none",
        "next_falsifier": "construct the logarithmic-insertion reduction and test covariant preservation of <r>"
    });

    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    fs::write("../string-six-point-connection-type-gate.json", &text).unwrap();
    print!("{text}");
}
