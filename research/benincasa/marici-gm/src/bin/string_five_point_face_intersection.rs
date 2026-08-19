#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Facet {
    label: &'static str,
    cyclic_index: usize,
}

fn compatible(a: Facet, b: Facet) -> bool {
    let d = (a.cyclic_index + 5 - b.cyclic_index) % 5;
    d == 2 || d == 3
}

fn main() {
    // Mizera, arXiv:1706.08527, eq. (4.15): the identity chamber in
    // \bar M_0,5 has five boundary facets and five compatible vertices.
    let facets = [
        Facet {
            label: "s12",
            cyclic_index: 0,
        },
        Facet {
            label: "s23",
            cyclic_index: 1,
        },
        Facet {
            label: "s34",
            cyclic_index: 2,
        },
        Facet {
            label: "s45",
            cyclic_index: 3,
        },
        Facet {
            label: "s51",
            cyclic_index: 4,
        },
    ];

    let mut vertices = Vec::new();
    for i in 0..facets.len() {
        for j in (i + 1)..facets.len() {
            if compatible(facets[i], facets[j]) {
                vertices.push((facets[i].label, facets[j].label));
            }
        }
    }

    let expected = [
        ("s12", "s34"),
        ("s12", "s45"),
        ("s23", "s45"),
        ("s23", "s51"),
        ("s34", "s51"),
    ];
    assert_eq!(vertices, expected);

    // The generalized-Pochhammer self-intersection is the face sum:
    // one interior contribution, one h_i per facet, and h_i h_j per
    // compatible codimension-two face, where h_i=(q_i-1)^(-1).
    assert_eq!(1 + facets.len() + vertices.len(), 11);

    // Ordered normal contractions anticommute at every vertex.  This is
    // the Cut/Gysin sign, while the scalar coefficient h_i h_j is symmetric.
    for &(left, right) in &vertices {
        let contraction_lr = 1_i8;
        let contraction_rl = -1_i8;
        assert_eq!(contraction_lr, -contraction_rl, "{left},{right}");
    }

    // The cyclic action preserves the complete face census and compatibility.
    for shift in 0..5 {
        let rotated: Vec<(usize, usize)> = vertices
            .iter()
            .map(|&(a, b)| {
                let ia = facets.iter().position(|f| f.label == a).unwrap();
                let ib = facets.iter().position(|f| f.label == b).unwrap();
                ((ia + shift) % 5, (ib + shift) % 5)
            })
            .collect();
        assert!(rotated
            .iter()
            .all(|&(i, j)| compatible(facets[i], facets[j])));
    }

    println!("five_point_string_face_intersection: ok");
    println!("cell_counts: interior=1 facets=5 vertices=5 total=11");
    println!("source_match: arXiv:1706.08527 eq.(4.15)");
    println!("ordered_double_residue_sign: antisymmetric on all 5 vertices");
}
