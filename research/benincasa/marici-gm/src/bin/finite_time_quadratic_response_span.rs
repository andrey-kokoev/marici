use symbolica::prelude::*;

fn atom(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default())
        .unwrap()
        .expand()
}

fn dot(left: &[Atom], right: &[Atom]) -> Atom {
    left.iter()
        .zip(right)
        .fold(atom("0"), |sum, (a, b)| (sum + a * b).expand())
}

fn main() {
    // Ordered late-time basis:
    // cos(theta), eta*cos(theta), eta^2*cos(theta),
    // sin(theta), eta*sin(theta), eta^2*sin(theta), 1, eta^2.
    let re_a = ["0", "-2*p", "0", "1", "0", "-p^2", "0", "0"];
    let im_a = ["1", "0", "-p^2", "0", "2*p", "0", "0", "0"];
    let b = ["0", "0", "0", "0", "0", "0", "1", "p^2"];
    let response: Vec<Vec<Atom>> = [re_a, im_a, b]
        .iter()
        .map(|row| row.iter().map(|x| atom(x)).collect())
        .collect();

    // Five source-independent annihilators of the response span.
    let annihilators = [
        ["0", "1", "0", "2*p", "0", "0", "0", "0"],
        ["0", "0", "0", "p^2", "0", "1", "0", "0"],
        ["p^2", "0", "1", "0", "0", "0", "0", "0"],
        ["-2*p", "0", "0", "0", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "-p^2", "1"],
    ];
    let annihilators: Vec<Vec<Atom>> = annihilators
        .iter()
        .map(|row| row.iter().map(|x| atom(x)).collect())
        .collect();

    for (i, functional) in annihilators.iter().enumerate() {
        for (j, direction) in response.iter().enumerate() {
            let value = dot(functional, direction);
            assert_eq!(value, atom("0"), "annihilator {i} fails on response {j}");
        }
    }

    // Eq. (19), after suppressing its common prefactor.  Here L denotes
    // J1-2*J0-4*J2-32*c3/(3*epsilon+2*delta)^2.  Its coefficient vector is
    // L times the ImA direction minus J0 times the B direction.
    let eq19: Vec<Atom> = [
        "L", "0", "-p^2*L", "0", "2*p*L", "0", "-J0", "-p^2*J0",
    ]
    .iter()
    .map(|x| atom(x))
    .collect();
    for (i, functional) in annihilators.iter().enumerate() {
        assert_eq!(
            dot(functional, &eq19),
            atom("0"),
            "Eq. (19) fails annihilator {i}"
        );
    }

    let packet = serde_json::json!({
        "schema": "marici.finite_time_quadratic_response_span.v1",
        "basis": [
            "cos(theta)", "eta*cos(theta)", "eta^2*cos(theta)",
            "sin(theta)", "eta*sin(theta)", "eta^2*sin(theta)",
            "1", "eta^2"
        ],
        "response_rank_generic": 3,
        "response_directions": {
            "ReA": re_a,
            "ImA": im_a,
            "B": b
        },
        "annihilator_rank_generic": 5,
        "annihilators": [
            "c_eta_cos + 2*p*c_sin",
            "p^2*c_sin + c_eta2_sin",
            "p^2*c_cos + c_eta2_cos",
            "-2*p*c_cos + c_eta_sin",
            "-p^2*c_nonosc + c_eta2_nonosc"
        ],
        "eq19_projection": {
            "ReA_coefficient": "0",
            "ImA_coefficient": "L",
            "B_coefficient": "-J0",
            "all_annihilators_zero": true
        },
        "verification": "all five annihilators kill all three response directions and Eq. (19) exactly"
    });
    println!("{}", serde_json::to_string_pretty(&packet).unwrap());
}
