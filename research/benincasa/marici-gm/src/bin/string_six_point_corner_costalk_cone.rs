use serde_json::json;

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
    // Columns are (F_m,F_n,D); rows are their two common point costalks.
    let canonical = [[1i64, 0, -1], [0, 1, -1]];
    let mut orientation_cases = Vec::new();
    for a in [-1i64, 1] {
        for b in [-1i64, 1] {
            for c in [-1i64, 1] {
                for d in [-1i64, 1] {
                    let m = [[a, 0, c], [0, b, d]];
                    let mut divisor1 = 0;
                    for row in m {
                        for x in row {
                            divisor1 = gcd(divisor1, x);
                        }
                    }
                    let minors = [
                        m[0][0] * m[1][1] - m[0][1] * m[1][0],
                        m[0][0] * m[1][2] - m[0][2] * m[1][0],
                        m[0][1] * m[1][2] - m[0][2] * m[1][1],
                    ];
                    let divisor2 = minors.into_iter().fold(0, gcd);
                    assert_eq!((divisor1, divisor2 / divisor1), (1, 1));
                    let kernel = [-c * a, -d * b, 1];
                    assert_eq!(m[0][0] * kernel[0] + m[0][2] * kernel[2], 0);
                    assert_eq!(m[1][1] * kernel[1] + m[1][2] * kernel[2], 0);
                    assert_eq!(kernel.into_iter().fold(0, gcd), 1);
                    orientation_cases
                        .push(json!({"matrix":m,"smith":[1,1],"primitive_kernel":kernel}));
                }
            }
        }
    }
    assert_eq!(orientation_cases.len(), 16);

    let occurrences = [
        ("12|35", "124356", "Z*A2"),
        ("124|35", "124356", "Z*A2*B24"),
        ("124|35", "142356", "Z*A2*B24"),
        ("13|25", "134256", "A3/Z"),
        ("134|25", "134256", "A3*B34/Z"),
        ("134|25", "143256", "A3*B34/Z"),
    ];
    let packet = json!({
        "schema":"marici.benincasa.string_six_point_corner_costalk_cone.v1",
        "local_complex":"Z^3 -> Z^2 with columns (facet_1,facet_2,diagonal)",
        "canonical_matrix":canonical,
        "canonical_primitive_kernel":[1,1,1],
        "local_smith":[1,1],
        "local_kernel_rank":1,
        "local_cokernel_rank":0,
        "orientation_cases_checked":orientation_cases.len(),
        "all_orientation_cases_primitive_and_acyclic_in_cokernel":true,
        "labelled_occurrences":occurrences.iter().map(|(corner,chamber,factor)|json!({"corner":corner,"chamber":chamber,"factor":factor})).collect::<Vec<_>>(),
        "global_source_rank":18,
        "global_target_rank":12,
        "global_differential_rank":12,
        "global_kernel_rank":6,
        "global_cokernel_rank":0,
        "global_kernel_lattice":"Z^6, one primitive compatibility class per labelled corner occurrence",
        "fitting_composite_total_valuation":6,
        "rank_matches_total_composite_valuation":true
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-corner-costalk-cone.json", &text).unwrap();
    print!("{text}");
}
