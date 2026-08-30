use serde_json::json;
use std::fs;
use symbolica::prelude::*;

fn a(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default())
        .unwrap()
        .expand()
}

fn main() {
    // X,Y,Z are site energies. U,V,W are squared norms of the three
    // contracted spatial resultants, with P_A+P_B+P_C=0.
    let x = a("X");
    let y = a("Y");
    let z = a("Z");
    let u = a("U");
    let v = a("V");
    let w = a("W");

    // Singleton wall equations:
    // X+y1+y2=Y+y2+y3=Z+y3+y1=0.
    let y1 = ((y.clone() - x.clone() - z.clone()) / a("2")).expand();
    let y2 = ((z.clone() - x.clone() - y.clone()) / a("2")).expand();
    let y3 = ((x.clone() - y.clone() - z.clone()) / a("2")).expand();

    // Foci 0, P_A, -P_C. Their 2x2 routing Gram matrix has entries
    // U, W, (U+W-V)/2.
    let h12 = ((u.clone() + w.clone() - v.clone()) / a("2")).expand();
    let det_h = (u.clone() * w.clone() - h12.clone() * h12.clone()).expand();
    let r1 = ((u.clone() + y1.clone() * y1.clone() - y2.clone() * y2.clone()) / a("2")).expand();
    let r2 = ((w.clone() + y1.clone() * y1.clone() - y3.clone() * y3.clone()) / a("2")).expand();
    let delta = (det_h.clone() * y1.clone() * y1.clone() - w.clone() * r1.clone() * r1.clone()
        + a("2") * h12.clone() * r1 * r2.clone()
        - u.clone() * r2.clone() * r2)
        .together()
        .factor();

    let homogeneous = delta
        .replace(a("U").to_pattern())
        .with(a("X^2").to_pattern())
        .replace(a("V").to_pattern())
        .with(a("Y^2").to_pattern())
        .replace(a("W").to_pattern())
        .with(a("Z^2").to_pattern())
        .expand()
        .factor();

    let total = a("X+Y+Z");
    let q = (-a("16") * a("X^2*Y^2") - a("8") * a("X*Y") * total.clone() * total.clone()
        + a("8") * (x.clone() + y.clone()) * total.clone() * total.clone() * total.clone()
        - a("5") * total.clone() * total.clone() * total.clone() * total)
        .expand()
        .factor();
    let q_on_signed_walls = [("X+Y-Z", "X+Y"), ("X-Y+Z", "Y-X"), ("X-Y-Z", "X-Y")]
        .into_iter()
        .map(|(wall, z_value)| {
            let value = q
                .replace(a("Z").to_pattern())
                .with(a(z_value).to_pattern())
                .expand()
                .factor();
            assert_ne!(value, a("0"));
            json!({"wall": wall, "Q_restriction": value.to_string(), "identically_zero": false})
        })
        .collect::<Vec<_>>();

    let packet = json!({
        "schema": "marici.benincasa.contracted_triangle.singleton_discriminant.v1",
        "wall_solution": {"y1": y1.to_string(), "y2": y2.to_string(), "y3": y3.to_string()},
        "routing_gram_determinant": det_h.factor().to_string(),
        "generic_height_discriminant": delta.to_string(),
        "homogeneous_specialization": homogeneous.to_string(),
        "source_Q": q.to_string(),
        "Q_on_signed_walls": q_on_signed_walls,
        "homogeneous_equals_Q": homogeneous == q,
        "homogeneous_is_zero": homogeneous == a("0"),
        "scope": "Generic triangle singleton-wall sphere-intersection discriminant; no physical-cycle activation claim."
    });
    fs::write(
        "../results/contracted-triangle-singleton-discriminant.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!("{}", serde_json::to_string_pretty(&packet).unwrap());
}
