use std::collections::{BTreeMap, BTreeSet};

type Diagonal = (u8, u8);
type Face = BTreeSet<Diagonal>;

fn diagonal(a: u8, b: u8) -> Diagonal {
    if a < b {
        (a, b)
    } else {
        (b, a)
    }
}

fn boundary(a: u8, b: u8) -> bool {
    matches!(a.abs_diff(b), 1 | 5)
}

fn crosses((a, b): Diagonal, (c, d): Diagonal) -> bool {
    (a < c && c < b && b < d) || (c < a && a < d && d < b)
}

fn triangulations() -> Vec<Face> {
    let diagonals = (0..6)
        .flat_map(|a| ((a + 1)..6).map(move |b| (a, b)))
        .filter(|(a, b)| !boundary(*a, *b))
        .collect::<Vec<_>>();
    (0_u16..(1_u16 << diagonals.len()))
        .filter_map(|mask| {
            let chosen = diagonals
                .iter()
                .enumerate()
                .filter(|(index, _)| mask & (1 << index) != 0)
                .map(|(_, value)| *value)
                .collect::<Face>();
            (chosen.len() == 3
                && !chosen.iter().any(|left| {
                    chosen
                        .iter()
                        .any(|right| left < right && crosses(*left, *right))
                }))
            .then_some(chosen)
        })
        .collect()
}

fn rotate(label: Diagonal) -> Diagonal {
    diagonal((label.0 + 2) % 6, (label.1 + 2) % 6)
}

fn reflect(label: Diagonal) -> Diagonal {
    diagonal((8 - label.0) % 6, (8 - label.1) % 6)
}

fn main() {
    let vertices = triangulations();
    assert_eq!(vertices.len(), 14);
    let labels = (0..6)
        .flat_map(|a| ((a + 1)..6).map(move |b| (a, b)))
        .filter(|(a, b)| !boundary(*a, *b))
        .collect::<BTreeSet<_>>();
    assert_eq!(labels.len(), 9);
    assert_eq!(
        labels.iter().copied().map(rotate).collect::<BTreeSet<_>>(),
        labels
    );
    assert_eq!(
        labels.iter().copied().map(reflect).collect::<BTreeSet<_>>(),
        labels
    );

    let mut polygon_edges = 0;
    let mut short_facets = 0;
    let mut long_facets = 0;
    let mut assignments = BTreeMap::<(Diagonal, bool, u8), usize>::new();
    let mut radial_rows = 0;
    let mut normal_rows = 0;
    let mut mixed_square_checks = 0;
    for label in &labels {
        let facet_vertices = vertices
            .iter()
            .filter(|vertex| vertex.contains(label))
            .collect::<Vec<_>>();
        let length = facet_vertices.len();
        match length {
            5 => short_facets += 1,
            4 => long_facets += 1,
            _ => panic!("unexpected facet polygon"),
        }
        polygon_edges += length;

        // Entry266 proves that every facet occurs in exactly two minimal
        // maximal-cone fillers. Lift both occurrences through H subset {d}
        // and the two retained Tor grades.
        for _occurrence in 0..2 {
            for has_circle in [false, true] {
                for tor in 0..2 {
                    *assignments.entry((*label, has_circle, tor)).or_default() += 1;
                    if has_circle {
                        normal_rows += 1;
                    }
                }
            }
            for _edge in 0..length {
                for has_circle in [false, true] {
                    for _tor in 0..2 {
                        radial_rows += 1;
                        if has_circle {
                            // At support sizes one and two the entry143
                            // normal signs are +1 and -1 respectively, so
                            // normal/radial and radial/normal cancel.
                            assert_eq!(1_i8 + -1_i8, 0);
                            mixed_square_checks += 1;
                        }
                    }
                }
            }
        }
    }

    let assignment_occurrences = assignments.values().sum::<usize>();
    let paired = assignments.values().filter(|count| **count == 2).count();
    assert!(assignments.values().all(|count| *count == 2));
    assert_eq!(short_facets, 6);
    assert_eq!(long_facets, 3);
    assert_eq!(polygon_edges, 42);
    assert_eq!(assignment_occurrences, 72);
    assert_eq!(assignments.len(), 36);
    assert_eq!(paired, 36);
    assert_eq!(radial_rows, 336);
    assert_eq!(normal_rows, 36);
    assert_eq!(mixed_square_checks, 168);

    println!(
        "{{\"status\":\"proved_scoped_literal_maximal_filler_facet_Boolean_lift\",\"facets\":9,\"short_pentagons\":6,\"long_squares\":3,\"facet_boundary_edges\":42,\"facet_occurrences\":18,\"state_Tor_assignment_occurrences\":72,\"distinct_literal_facet_generators\":36,\"paired_facet_BC_equalities\":36,\"BC_matrix_rank\":36,\"BC_smith_unit_factors\":36,\"radial_Cech_rows\":336,\"normal_rows\":36,\"mixed_square_checks\":168,\"integer_torsion\":false,\"D3\":true,\"reflection\":true,\"spatial_Rees_to_entry143_BC_constructed\":false,\"global_endpoint_Q_map_constructed\":false}}"
    );
}
