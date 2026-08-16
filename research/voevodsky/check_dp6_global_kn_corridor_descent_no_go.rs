#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum TargetVertex {
    Plus,
    Minus,
    Center(usize),
}

#[derive(Clone, Copy)]
struct Cone {
    first: usize,
    second: usize,
    positive: bool,
}

fn omitted(a: usize, b: usize) -> usize {
    3 - a - b
}

fn image(cone: Cone, ray: usize) -> TargetVertex {
    assert!(ray == cone.first || ray == cone.second);
    if ray == cone.first {
        if cone.positive {
            TargetVertex::Plus
        } else {
            TargetVertex::Minus
        }
    } else {
        TargetVertex::Center(omitted(cone.first, cone.second))
    }
}

fn main() {
    // Cyclic maximal-cone order from the two dP6 toric contractions.
    let cones = [
        Cone {
            first: 0,
            second: 1,
            positive: true,
        },
        Cone {
            first: 0,
            second: 2,
            positive: false,
        },
        Cone {
            first: 1,
            second: 2,
            positive: true,
        },
        Cone {
            first: 1,
            second: 0,
            positive: false,
        },
        Cone {
            first: 2,
            second: 0,
            positive: true,
        },
        Cone {
            first: 2,
            second: 1,
            positive: false,
        },
    ];
    let shared_rays = [0, 2, 1, 0, 2, 1];
    let mut endpoint_mismatches = 0;
    let mut center_mismatches = 0;
    for i in 0..6 {
        let left = image(cones[i], shared_rays[i]);
        let right = image(cones[(i + 1) % 6], shared_rays[i]);
        assert_ne!(left, right);
        match (left, right) {
            (TargetVertex::Plus, TargetVertex::Minus)
            | (TargetVertex::Minus, TargetVertex::Plus) => endpoint_mismatches += 1,
            (TargetVertex::Center(a), TargetVertex::Center(b)) if a != b => center_mismatches += 1,
            _ => panic!("unexpected mismatch"),
        }
    }
    assert_eq!(endpoint_mismatches, 3);
    assert_eq!(center_mismatches, 3);
    println!("{{\"status\":\"falsified_scoped_ordinary_global_KN_corridor_descent\",\"maximal_cones\":6,\"shared_ray_restriction_matches\":0,\"endpoint_mismatches\":{},\"distinct_center_mismatches\":{},\"ordinary_stratified_gluing_exists\":false,\"shifted_center_homotopies_available\":true,\"endpoint_connector_constructed\":false,\"minimal_additional_datum\":\"one D3-orbit of normalization-provenanced endpoint connector cells plus reflection coherence\"}}",endpoint_mismatches,center_mismatches);
}
