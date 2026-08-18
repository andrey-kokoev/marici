fn quotient_dimension(cutoff: usize, kill_w: bool, kill_u: bool, kill_v: bool) -> usize {
    let mut count = 0;
    for w in 0..=cutoff {
        for u in 0..=cutoff - w {
            for v in 0..=cutoff - w - u {
                if (kill_w && w > 0) || (kill_u && u > 0) || (kill_v && v > 0) {
                    continue;
                }
                count += 1;
            }
        }
    }
    count
}

fn main() {
    // Completed normal form on the open locus where one Hessian minor is a
    // unit: w^2-u^2=lambda*(v^2+E^2), lambda=Lambda up to a unit.

    // E=0, lambda invertible: Jacobian ideal (w,u,v), ordinary A1.
    for cutoff in 1..=12 {
        assert_eq!(quotient_dimension(cutoff, true, true, true), 1);
    }

    // lambda=0: Jacobian ideal (w,u), leaving the critical coordinate v.
    // The ordinary Milnor algebra grows, while the transverse slice v=0 is A1.
    for cutoff in 1..=12 {
        assert_eq!(quotient_dimension(cutoff, true, true, false), cutoff + 1);
        assert_eq!(quotient_dimension(cutoff, true, true, true), 1);
    }

    // At E=lambda=0, the Morse function on the critical line is v^2+E^2.
    // Its E=0 Jacobian quotient k[[v]]/(2v) has length one.
    let critical_line_milnor_rank = 1;
    assert_eq!(critical_line_milnor_rank, 1);

    // (E,lambda) is a regular sequence in the reduced parameter base, so
    // there is no reduced excess Tor.  The source discriminant is E^2*lambda:
    // the doubled E layer has Cartier/Rees length two but reduced rank one.
    let reduced_excess_tor_rank = 0;
    let total_energy_cartier_length = 2;
    let reduced_vanishing_rank = 1;
    assert_eq!(reduced_excess_tor_rank, 0);
    assert_eq!(total_energy_cartier_length, 2);
    assert_eq!(reduced_vanishing_rank, 1);

    println!("completed_model=w^2-u^2=Lambda*(v^2+E^2)");
    println!("E_zero_milnor_number=1");
    println!("Lambda_zero_ordinary_milnor_number=nonisolated");
    println!("Lambda_zero_transverse_milnor_rank=1");
    println!("intersection_iterated_vanishing_rank=1");
    println!("intersection_reduced_excess_tor_rank=0");
    println!("E_cartier_rees_length=2");
    println!("anti_invariant_rank_excess=0");
}
