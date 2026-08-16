use std::collections::{HashMap, HashSet, VecDeque};

#[derive(Clone, Copy, Debug, Eq, Hash, PartialEq)]
enum Object {
    EndpointCone,
    WallH1Twist,
    MarkedH2,
    AbsoluteH2,
    AlgebraicKernel,
    AbsoluteH3,
    EllipticBoundaryH1Twist,
}

#[derive(Clone, Copy)]
struct Arrow {
    name: &'static str,
    source: Object,
    target: Object,
}

fn path(source: Object, target: Object, arrows: &[Arrow]) -> Option<Vec<&'static str>> {
    let mut seen = HashSet::from([source]);
    let mut queue = VecDeque::from([source]);
    let mut parent: HashMap<Object, (Object, &'static str)> = HashMap::new();
    while let Some(node) = queue.pop_front() {
        if node == target {
            let mut cursor = target;
            let mut result = Vec::new();
            while cursor != source {
                let (previous, arrow) = parent[&cursor];
                result.push(arrow);
                cursor = previous;
            }
            result.reverse();
            return Some(result);
        }
        for arrow in arrows.iter().filter(|arrow| arrow.source == node) {
            if seen.insert(arrow.target) {
                parent.insert(arrow.target, (node, arrow.name));
                queue.push_back(arrow.target);
            }
        }
    }
    None
}

fn main() {
    // Frozen nonzero canonical arrows. The localization sequence is
    // H^2(S) -> H^2(U) -> H^1(W)(-1) -> H^3(S).
    let frozen = [
        Arrow {
            name: "endpoint realization",
            source: Object::EndpointCone,
            target: Object::WallH1Twist,
        },
        Arrow {
            name: "restriction j*",
            source: Object::AbsoluteH2,
            target: Object::MarkedH2,
        },
        Arrow {
            name: "wall residue",
            source: Object::MarkedH2,
            target: Object::WallH1Twist,
        },
        Arrow {
            name: "wall Gysin",
            source: Object::WallH1Twist,
            target: Object::AbsoluteH3,
        },
        Arrow {
            name: "algebraic-kernel inclusion",
            source: Object::AlgebraicKernel,
            target: Object::AbsoluteH2,
        },
        Arrow {
            name: "infinity residue",
            source: Object::AbsoluteH2,
            target: Object::EllipticBoundaryH1Twist,
        },
    ];

    let endpoint_to_wall = path(Object::EndpointCone, Object::WallH1Twist, &frozen);
    let endpoint_to_h3 = path(Object::EndpointCone, Object::AbsoluteH3, &frozen);
    let endpoint_to_h2 = path(Object::EndpointCone, Object::AbsoluteH2, &frozen);
    let endpoint_to_kernel = path(Object::EndpointCone, Object::AlgebraicKernel, &frozen);
    let kernel_to_wall = path(Object::AlgebraicKernel, Object::WallH1Twist, &frozen);

    assert_eq!(endpoint_to_wall, Some(vec!["endpoint realization"]));
    assert_eq!(
        endpoint_to_h3,
        Some(vec!["endpoint realization", "wall Gysin"])
    );
    assert!(endpoint_to_h2.is_none());
    assert!(endpoint_to_kernel.is_none());
    assert_eq!(
        kernel_to_wall,
        Some(vec![
            "algebraic-kernel inclusion",
            "restriction j*",
            "wall residue"
        ])
    );

    println!(
        r#"{{
  "schema": "marici.endpoint-to-algebraic-kernel-type-gate.v1",
  "frozen_nonzero_arrows": [
    "EndpointCone->H1(W)(-1)",
    "A_--->H2(S)",
    "H2(S)->H2(U)",
    "H2(U)->H1(W)(-1)",
    "H1(W)(-1)->H3(S)",
    "H2(S)->H1(D_infinity)(-1)"
  ],
  "endpoint_to_wall": true,
  "endpoint_to_absolute_H3": true,
  "endpoint_to_absolute_H2": false,
  "endpoint_to_A_--": false,
  "A_--_to_wall": true,
  "e6_ancestry_is_morphism": false,
  "zero_infinity_image_is_lift": false,
  "required_extra_datum": [
    "localization splitting or contracting homotopy",
    "source-derived physical relative-realization correspondence"
  ],
  "canonical_embedding_claim": "falsified_in_frozen_calculus",
  "endpoint_extension_home": "marked relative coefficient data",
  "Q_home_updated": "not endpoint-to-A_-- morphism; physical relative-chain/discriminant extension or apparent alphabet remains",
  "new_carrier_incidence": false
}}"#
    );
}
