use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}

fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}

fn main() {
    let zero = a("0");
    let one = a("1");
    let s: [[i32; 6]; 6] = [
        [0, 0, 0, 0, -1, 0],
        [1, 0, 0, 0, 1, 0],
        [0, -1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
    ];
    let monodromy = ["M1", "M2a", "M2b", "M3", "M4a", "M4b"];
    let q: Vec<Atom> = monodromy
        .iter()
        .map(|m| a(m) - one.clone())
        .collect();

    // C = S diag(M_i-1), in the occurrence order of Entries 967 and 969.
    let c: Vec<Vec<Atom>> = (0..6)
        .map(|i| {
            (0..6)
                .map(|j| a(&s[i][j].to_string()) * q[j].clone())
                .collect()
        })
        .collect();

    // Primal regularization divides each source path by its own boundary defect.
    let primal: Vec<Vec<Atom>> = (0..6)
        .map(|i| {
            (0..6)
                .map(|j| clean(c[i][j].clone() / q[j].clone()))
                .collect()
        })
        .collect();
    assert!((0..6).all(|i| (0..6).all(|j|
        primal[i][j] == a(&s[i][j].to_string())
    )));

    // In the dual local system 1/(M_i^{-1}-1)=-M_i/(M_i-1).
    let dual: Vec<Vec<Atom>> = (0..6)
        .map(|i| {
            (0..6)
                .map(|j| clean(c[i][j].clone() * (-a(monodromy[j])) / q[j].clone()))
                .collect()
        })
        .collect();
    assert!((0..6).all(|i| (0..6).all(|j| {
        let expected = a(&s[i][j].to_string()) * (-a(monodromy[j]));
        clean(dual[i][j].clone() - expected) == zero
    })));

    let packet = serde_json::json!({
        "schema": "marici.benincasa.string.loaded_pochhammer_cancellation.v1",
        "entry": 1032,
        "source_entries": [949, 1010, 1028, 1030, 1031],
        "occurrence_monodromies": monodromy,
        "boundary_factors": monodromy.iter().map(|m| format!("{m}-1")).collect::<Vec<_>>(),
        "incidence_skeleton": s,
        "incidence_determinant_absolute": 1,
        "primal_regularized_boundary": "S",
        "dual_regularized_boundary": "S*diag(-M_i)",
        "primal_laurent_unimodular": true,
        "dual_laurent_unimodular": true,
        "remaining_scope": "first occurrencewise loaded-boundary grade; no global twisted period pairing or intersection normalization constructed"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-loaded-pochhammer-cancellation.json", &text).unwrap();
    print!("{text}");
}
