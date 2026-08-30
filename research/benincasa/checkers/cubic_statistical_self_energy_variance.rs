#[derive(Clone, Copy, Debug, PartialEq, Eq)]
struct Linear4 {
    x: i64,
    y: i64,
}

impl Linear4 {
    fn zero() -> Self {
        Self { x: 0, y: 0 }
    }
}

fn main() {
    // Ordering: (++,+-,-+,--).  At t1>t2 the vacuum contour propagator is
    // (G^>,G^<,G^>,G^<)=(x,y,x,y).
    let vacuum = [
        Linear4 { x: 1, y: 0 },
        Linear4 { x: 0, y: 1 },
        Linear4 { x: 1, y: 0 },
        Linear4 { x: 0, y: 1 },
    ];
    let vertex_metric = [1, -1, -1, 1];

    // For a cubic self-energy, Sigma^{ab} is proportional to
    // (a b)(G^{ab})^2.  Linearizing along the common statistical tangent
    // delta G=(1,1,1,1) gives 2(a b)G^{ab}.
    let mut image = [Linear4::zero(); 4];
    for i in 0..4 {
        image[i] = Linear4 {
            x: 2 * vertex_metric[i] * vacuum[i].x,
            y: 2 * vertex_metric[i] * vacuum[i].y,
        };
    }

    let expected = [
        Linear4 { x: 2, y: 0 },
        Linear4 { x: 0, y: -2 },
        Linear4 { x: -2, y: 0 },
        Linear4 { x: 0, y: 2 },
    ];
    assert_eq!(image, expected);

    // It is not a common-contour propagator tangent: component 0 differs
    // from component 2 and component 1 differs from component 3.
    let remains_common = image.iter().all(|entry| *entry == image[0]);
    assert!(!remains_common);

    // It is odd under flipping the first contour occurrence, as required
    // for the covariant self-energy variance.
    assert_eq!(image[2].x, -image[0].x);
    assert_eq!(image[3].y, -image[1].y);

    println!(
        "{{\"schema\":\"marici.benincasa.cubic_statistical_self_energy_variance.v1\",\"component_order\":[\"++\",\"+-\",\"-+\",\"--\"],\"linearized_image\":[\"2x\",\"-2y\",\"-2x\",\"2y\"],\"remains_common_contour\":false,\"first_occurrence_character\":\"odd\",\"status\":\"verified\"}}"
    );
}

