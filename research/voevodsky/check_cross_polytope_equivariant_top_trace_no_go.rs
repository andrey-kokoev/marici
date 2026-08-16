use std::collections::{BTreeMap, BTreeSet};

type Signs = [i8; 3];

fn rotate(s: Signs) -> Signs {
    [s[2], s[0], s[1]]
}

fn reflect(s: Signs) -> Signs {
    [-s[0], -s[2], -s[1]]
}

fn all_signs() -> Vec<Signs> {
    (0_u8..8)
        .map(|mask| std::array::from_fn(|axis| if mask & (1 << axis) == 0 { 1 } else { -1 }))
        .collect()
}

fn product(s: Signs) -> i64 {
    s.iter().map(|value| i64::from(*value)).product()
}

fn orbit(seed: Signs) -> BTreeSet<Signs> {
    let mut result = BTreeSet::new();
    let mut present = seed;
    for _ in 0..3 {
        result.insert(present);
        result.insert(reflect(present));
        present = rotate(present);
    }
    result
}

fn gcd(mut a: i64, mut b: i64) -> i64 {
    a = a.abs();
    b = b.abs();
    while b != 0 {
        let r = a % b;
        a = b;
        b = r;
    }
    a
}

fn main() {
    let signs = all_signs();
    let orbit_two = orbit([1, 1, 1]);
    let orbit_six = orbit([-1, 1, 1]);
    assert_eq!(orbit_two.len(), 2);
    assert_eq!(orbit_six.len(), 6);
    assert!(orbit_two.is_disjoint(&orbit_six));
    assert_eq!(
        orbit_two
            .union(&orbit_six)
            .copied()
            .collect::<BTreeSet<_>>(),
        signs.iter().copied().collect()
    );

    // Geometric reflection reverses an oriented triangular face. The single
    // retained source orientation twist contributes a second minus, so the
    // loaded face basis is reflection-even while the loaded generic target
    // line is reflection-odd. Thus its coefficients are reflection-odd and
    // rotation-invariant, determined by a and b.
    let mut symbolic = BTreeMap::<Signs, (i64, i64)>::new();
    for s in &signs {
        let negative = s.iter().filter(|value| **value < 0).count();
        let coefficient = match negative {
            0 => (1, 0),
            3 => (-1, 0),
            1 => (0, 1),
            2 => (0, -1),
            _ => unreachable!(),
        };
        symbolic.insert(*s, coefficient);
    }
    for s in &signs {
        let coefficient = symbolic[s];
        assert_eq!(symbolic[&rotate(*s)], coefficient);
        assert_eq!(symbolic[&reflect(*s)], (-coefficient.0, -coefficient.1));
    }

    let pairing = signs.iter().fold((0_i64, 0_i64), |sum, s| {
        let coefficient = symbolic[s];
        (
            sum.0 + product(*s) * coefficient.0,
            sum.1 + product(*s) * coefficient.1,
        )
    });
    assert_eq!(pairing, (2, -6));
    assert_eq!(gcd(pairing.0, pairing.1), 2);
    assert!((-32_i64..=32).all(|a| (-32_i64..=32).all(|b| 2 * a - 6 * b != 1)));

    // One independently derived odd interior column with unit counit changes
    // the presentation [2,-6] to [2,-6,1], whose Smith factor is one.
    assert_eq!(gcd(gcd(2, -6), 1), 1);
    let repaired = (0_i64, 0_i64, 1_i64);
    assert_eq!(2 * repaired.0 - 6 * repaired.1 + repaired.2, 1);

    println!(
        "{{\"status\":\"falsified_scoped_ordinary_equivariant_octahedral_top_trace\",\"geometric_face_reflection_sign\":-1,\"source_orientation_twist_sign\":-1,\"loaded_face_reflection_sign\":1,\"loaded_target_reflection_sign\":-1,\"face_orbits\":[2,6],\"trace_parameters\":[\"a\",\"b\"],\"fundamental_pairing_row\":[2,-6],\"smith\":[2],\"obstruction_group\":\"Z/2\",\"primitive_top_value_one_solution\":\"EMPTY\",\"minimal_repair_row\":[2,-6,1],\"repaired_smith\":[1],\"odd_interior_excess_column_required\":true,\"odd_interior_column_geometrically_constructed\":false,\"global_correspondence_no_go\":false}}"
    );
}
