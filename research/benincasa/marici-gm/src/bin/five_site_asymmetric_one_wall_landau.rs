use serde_json::json;
use std::fs;

const P: [[i64; 3]; 5] = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 2, 3],
    [-2, -3, -4],
];

fn region(start: usize, size: usize) -> Vec<usize> {
    (0..size).map(|offset| (start + offset) % 5).collect()
}

fn resultant(indices: &[usize]) -> [i64; 3] {
    let mut sum = [0_i64; 3];
    for &index in indices {
        for coordinate in 0..3 {
            sum[coordinate] += P[index][coordinate];
        }
    }
    sum
}

fn norm_squared(vector: [i64; 3]) -> i64 {
    vector.iter().map(|entry| entry * entry).sum()
}

fn main() {
    let total = resultant(&[0, 1, 2, 3, 4]);
    assert_eq!(total, [0, 0, 0]);

    let mut proper_walls = Vec::new();
    for size in 1..=4 {
        for start in 0..5 {
            let indices = region(start, size);
            let momentum = resultant(&indices);
            let momentum_squared = norm_squared(momentum);
            let left_cut = (start + 4) % 5;
            let right_cut = (start + size - 1) % 5;
            proper_walls.push(json!({
                "label": format!("E_A({})", indices.iter().map(|i| (i + 1).to_string()).collect::<Vec<_>>().join(",")),
                "start_site": start + 1,
                "region_size": size,
                "sites": indices.iter().map(|i| i + 1).collect::<Vec<_>>(),
                "boundary_edges": [left_cut + 1, right_cut + 1],
                "P_A": momentum,
                "P_A_squared": momentum_squared,
                "signed_threshold_polynomial": format!("{}*t^2-{}", size * size, momentum_squared),
                "physical_sheet_root": format!("-sqrt({})/{}", momentum_squared, size)
            }));
        }
    }
    assert_eq!(proper_walls.len(), 20);

    let one_cut_walls = (0..5)
        .map(|edge| json!({
            "label": format!("E_total_minus_edge_{}", edge + 1),
            "threshold_polynomial": "t",
            "source_reason": "At the soft endpoint y_e=0, 5t+2y_e=0 reduces to t=0."
        }))
        .collect::<Vec<_>>();

    let packet = json!({
        "schema": "marici.benincasa.five_site.asymmetric_one_wall_landau.v1",
        "source_slice": "Entry 1257 asymmetric momentum-conserving rank-three physical slice",
        "spatial_resultants": P,
        "site_energies": "X_1=...=X_5=t",
        "wall_census": {
            "proper_connected_region_walls": 20,
            "total_energy_walls": 1,
            "one_cut_total_walls": 5,
            "total": 26
        },
        "proper_connected_region_walls": proper_walls,
        "total_energy_wall": {
            "label": "E_total",
            "threshold_polynomial": "t",
            "source_reason": "E_total=5t."
        },
        "one_cut_total_walls": one_cut_walls,
        "landau_geometry": "For E_A=|A|t+y_left+y_right, stationary collinear two-focus configurations give y_left+y_right=+-|P_A| after complex continuation.",
        "classification": "source-derived individual-wall endpoint support over the existing labelled partial-energy and soft carrier",
        "scope": "all 26 individual labelled walls; no simultaneous multi-wall conclusion",
        "new_carrier_datum": false
    });

    fs::write(
        "../results/five-site-asymmetric-one-wall-landau.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!("wrote five-site-asymmetric-one-wall-landau.json");
}
