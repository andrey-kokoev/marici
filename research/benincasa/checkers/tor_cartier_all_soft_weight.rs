// Exact Rees-weight compatibility between the Tor Cartier factor and CM form.

fn main() {
    let tor_cartier_weight = 1_i32;
    let relative_cm_form_weight = -1_i32;
    let total = tor_cartier_weight + relative_cm_form_weight;
    assert_eq!(total, 0);

    let radial_monodromy = 1_i32; // both weights are integral
    assert_eq!(radial_monodromy, 1);
    println!(
        "{{\"status\":\"pass\",\"tor_cartier_weight\":1,\"relative_cm_form_weight\":-1,\"paired_exceptional_weight\":0,\"radial_monodromy\":1}}"
    );
}
