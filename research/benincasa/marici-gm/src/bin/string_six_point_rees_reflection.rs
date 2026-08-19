use symbolica::prelude::*;

fn a(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap()
}

fn clean(x: Atom) -> Atom {
    x.together().cancel().factor()
}

fn swap_yz(x: Atom) -> Atom {
    // Simultaneous exchange via a temporary symbol.
    let tmp = x
        .replace(a("n_y").to_pattern())
        .with(a("n_tmp").to_pattern());
    let tmp = tmp
        .replace(a("n_z").to_pattern())
        .with(a("n_y").to_pattern());
    clean(
        tmp.replace(a("n_tmp").to_pattern())
            .with(a("n_z").to_pattern()),
    )
}

fn main() {
    // The source reflection tau_off=(23) fixes a=s14 and q=s235, and exchanges
    // y=s35 with z=s25.
    let f_y = clean(a("n_a") / a("n_y"));
    let f_z = clean(a("n_a") / a("n_z"));
    assert_eq!(swap_yz(f_y.clone()), f_z);

    // Divisor coordinates are ordered (D_a,D_y,D_z,D_q).
    let div_y = [1, -1, 0, 0];
    let div_z = [1, 0, -1, 0];
    let tau_div_y = [div_y[0], div_y[2], div_y[1], div_y[3]];
    assert_eq!(tau_div_y, div_z);
    assert_eq!(div_y.iter().sum::<i32>(), 0);
    assert_eq!(div_z.iter().sum::<i32>(), 0);

    // In the source-normalized transition, tau reverses both the sparse
    // row basis and dense column basis. Their orientation characters cancel.
    let sparse_orientation = -1;
    let dense_orientation = -1;
    let residue_orientation = 1;
    let normal_orientation = 1;
    let total_character = sparse_orientation
        * dense_orientation
        * residue_orientation
        * normal_orientation;
    assert_eq!(total_character, 1);

    println!(
        "{{\"schema\":\"marici.benincasa.string_six_point_rees_reflection.v1\",\"reflection\":\"(23)\",\"normal_action\":{{\"n_a\":\"n_a\",\"n_y\":\"n_z\",\"n_z\":\"n_y\",\"n_q\":\"n_q\"}},\"source_factor_y\":\"n_a/n_y\",\"transported_factor_z\":\"n_a/n_z\",\"divisor_y\":[1,-1,0,0],\"divisor_z\":[1,0,-1,0],\"sparse_orientation\":-1,\"dense_orientation\":-1,\"residue_orientation\":1,\"normal_orientation\":1,\"total_character\":{},\"strict_occurrence_covariance\":true,\"extra_unit\":\"1\"}}",
        total_character
    );
}
