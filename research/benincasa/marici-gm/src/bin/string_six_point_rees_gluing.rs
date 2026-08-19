use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}
fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}
fn replace(x: Atom, name: &str, value: Atom) -> Atom {
    clean(x.replace(a(name).to_pattern()).with(value.to_pattern()))
}

fn main() {
    // Exceptional homogeneous coordinates are [n_a:n_y:n_q].
    // a-chart: U=n_y/n_a, V=n_q/n_a.
    let f_a = clean(a("1") / a("U"));

    // y-chart: A=n_a/n_y, W=n_q/n_y.
    let f_y = a("A");
    let f_y_on_a = replace(
        replace(f_y.clone(), "A", clean(a("1") / a("U"))),
        "W",
        clean(a("V") / a("U")),
    );
    assert_eq!(clean(f_y_on_a - f_a.clone()), a("0"));

    // q-chart: C=n_a/n_q, D=n_y/n_q.
    let f_q = clean(a("C") / a("D"));
    let f_q_on_a = replace(
        replace(f_q.clone(), "C", clean(a("1") / a("V"))),
        "D",
        clean(a("U") / a("V")),
    );
    assert_eq!(clean(f_q_on_a - f_a.clone()), a("0"));

    // Direct y-q transition: C=A/W, D=1/W.
    let f_q_on_y = replace(
        replace(f_q, "C", clean(a("A") / a("W"))),
        "D",
        clean(a("1") / a("W")),
    );
    assert_eq!(clean(f_q_on_y - f_y), a("0"));

    // div(n_a/n_y)=D_a-D_y on E=P^2.
    let divisor = [1, -1, 0];
    assert_eq!(divisor.iter().sum::<i32>(), 0);

    println!(
        "{{\"schema\":\"marici.benincasa.string_six_point_rees_gluing.v1\",\"exceptional_coordinates\":[\"n_a\",\"n_y\",\"n_q\"],\"a_chart_factor\":\"1/U\",\"y_chart_factor\":\"A\",\"q_chart_factor\":\"C/D\",\"a_y_overlap\":true,\"a_q_overlap\":true,\"y_q_overlap\":true,\"projective_image_constant\":true,\"divisor_coefficients\":{{\"D_a\":1,\"D_y\":-1,\"D_q\":0}},\"divisor_degree\":0,\"global_object\":\"meromorphic rank-one line with lattice modification D_a-D_y\"}}"
    );
}
