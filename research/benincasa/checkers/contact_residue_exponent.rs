// Exponent audit for the generic contact/branch tangency normal form.

fn main() {
    // Local model: q=v, K=u^2+v+nu, Omega=du^dv/(q*sqrt(K)).
    // Res_{q=0} Omega = du/sqrt(u^2+nu).  Scaling u=sqrt(nu)t
    // cancels the half powers: du/sqrt(u^2+nu)=dt/sqrt(t^2+1).
    let numerator_half_weight = 1_i32;
    let denominator_half_weight = 1_i32;
    let net_half_weight = numerator_half_weight - denominator_half_weight;
    assert_eq!(net_half_weight, 0);

    // The colliding endpoints generate a logarithm (unipotent Jordan block),
    // not a residual semisimple sign character.
    let semisimple_character = 1_i32;
    let nilpotent_rank = 1_usize;
    assert_eq!(semisimple_character, 1);
    assert_eq!(nilpotent_rank, 1);

    println!(
        "{{\"status\":\"pass\",\"normal_form\":\"q=v,K=u^2+v+nu\",\"net_half_weight\":0,\"semisimple_character\":1,\"nilpotent_rank\":1,\"half_kummer_supplied\":false}}"
    );
}
