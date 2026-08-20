use std::collections::{BTreeMap, BTreeSet};

#[derive(Clone, Copy, Debug)]
struct Edge {
    cut: &'static str,
    lower: &'static str,
    soft: &'static str,
    endpoint: &'static str,
}

fn main() {
    // Source order from equation (51), oriented as in Entry 1082.
    let edges = [
        Edge { cut: "G12", lower: "g23", soft: "y12=0", endpoint: "y31=X1" },
        Edge { cut: "G31", lower: "g23", soft: "y31=0", endpoint: "y12=X1" },
        Edge { cut: "G31", lower: "g12", soft: "y31=0", endpoint: "y23=X3" },
        Edge { cut: "G23", lower: "g12", soft: "y23=0", endpoint: "y31=X3" },
        Edge { cut: "G23", lower: "g31", soft: "y23=0", endpoint: "y12=X2" },
        Edge { cut: "G12", lower: "g31", soft: "y12=0", endpoint: "y23=X2" },
    ];

    let expected: BTreeSet<_> = [
        ("G12", "g23"), ("G12", "g31"),
        ("G23", "g31"), ("G23", "g12"),
        ("G31", "g12"), ("G31", "g23"),
    ].iter().copied().collect();
    let got: BTreeSet<_> = edges.iter().map(|e| (e.cut, e.lower)).collect();
    assert_eq!(got, expected);

    // Every total-energy specialization contains exactly one existing
    // coordinate-soft carrier equation; none is a generic Cut flag.
    assert!(edges.iter().all(|e| e.soft.ends_with("=0")));

    let mut multiplicity = BTreeMap::new();
    for edge in edges {
        *multiplicity.entry(edge.cut).or_insert(0usize) += 1;
        println!("{}|{}: {}, {}", edge.cut, edge.lower, edge.soft, edge.endpoint);
    }
    assert_eq!(multiplicity.values().copied().collect::<Vec<_>>(), vec![2, 2, 2]);
    println!("occurrence-forgetting multiplicities: {:?}", multiplicity);
}
