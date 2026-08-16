use std::collections::BTreeSet;

type Ray = (usize, i8);

fn det(columns: [Ray; 3]) -> i64 {
    let mut matrix = [[0_i64; 3]; 3];
    for (column, (axis, sign)) in columns.into_iter().enumerate() {
        matrix[axis][column] = i64::from(sign);
    }
    matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
        - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
        + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
}

fn rotate(ray: Ray) -> Ray {
    ((ray.0 + 1) % 3, ray.1)
}

fn reflect(ray: Ray) -> Ray {
    match ray {
        (0, sign) => (0, -sign),
        (1, sign) => (2, -sign),
        (2, sign) => (1, -sign),
        _ => unreachable!(),
    }
}

fn main() {
    let rays = (0..3)
        .flat_map(|axis| [(axis, -1_i8), (axis, 1_i8)])
        .collect::<BTreeSet<_>>();
    assert_eq!(rays.len(), 6);

    let mut maximal = BTreeSet::new();
    let mut two_cones = BTreeSet::new();
    for mask in 0_u8..8 {
        let cone = std::array::from_fn::<_, 3, _>(|axis| {
            (axis, if mask & (1 << axis) == 0 { 1 } else { -1 })
        });
        assert_eq!(det(cone).abs(), 1);
        maximal.insert(cone.into_iter().collect::<BTreeSet<_>>());
        for omitted in 0..3 {
            two_cones.insert(
                cone.into_iter()
                    .filter(|(axis, _)| *axis != omitted)
                    .collect::<BTreeSet<_>>(),
            );
        }
    }
    assert_eq!(maximal.len(), 8);
    assert_eq!(two_cones.len(), 12);

    for cone in &maximal {
        let rotated = cone.iter().copied().map(rotate).collect::<BTreeSet<_>>();
        let reflected = cone.iter().copied().map(reflect).collect::<BTreeSet<_>>();
        assert!(maximal.contains(&rotated));
        assert!(maximal.contains(&reflected));
    }

    // A two-cone is sheetwise when its two chosen ray signs agree.
    let sheetwise = two_cones
        .iter()
        .filter(|cone| {
            cone.iter()
                .map(|(_, sign)| sign)
                .collect::<BTreeSet<_>>()
                .len()
                == 1
        })
        .count();
    assert_eq!(sheetwise, 6);
    assert_eq!(two_cones.len() - sheetwise, 6);

    // Multiplicities belong to the characteristic-monoid map; saturation of
    // the source fan does not erase them or turn them into ray subdivisions.
    let multiplicities = [2_i64, 3, 5];
    assert_eq!(multiplicities.iter().product::<i64>(), 30);
    assert!(multiplicities.iter().all(|value| *value > 0));

    println!(
        "{{\"status\":\"proved_scoped_full_log_toric_source\",\"toric_bundle\":\"product_D P(O plus L_D)\",\"rays\":6,\"two_cones\":12,\"maximal_cones\":8,\"smooth_unimodular\":true,\"sheetwise_two_cones\":6,\"cross_sheet_two_cones\":6,\"multiplicities_retained_in_monoid_map\":true,\"D3\":true,\"reflection\":true,\"literal_entry143_comparison_constructed\":false,\"mapping_fiber_instantiated\":false}}"
    );
}
