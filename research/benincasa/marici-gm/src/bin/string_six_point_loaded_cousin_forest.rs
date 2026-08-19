fn rank(mut m: Vec<Vec<f64>>) -> usize {
    let rows = m.len();
    let cols = m[0].len();
    let mut r = 0;
    for c in 0..cols {
        let Some(p) = (r..rows).find(|&i| m[i][c].abs() > 0.5) else { continue };
        m.swap(r, p);
        let pivot = m[r][c];
        for j in c..cols { m[r][j] /= pivot; }
        for i in 0..rows {
            if i != r {
                let f = m[i][c];
                for j in c..cols { m[i][j] -= f * m[r][j]; }
            }
        }
        r += 1;
    }
    r
}

fn main() {
    // Vertex order: P1,P2,P3,P4,Q1,Q2,Q3,Q4.
    // Edge order is the six source character blocks from Entry 1030.
    let edges = [
        (0usize, 5usize), // P1-Q2
        (1, 5),          // P2-Q2
        (2, 7),          // P3-Q4
        (3, 7),          // P4-Q4
        (1, 4),          // P2-Q1
        (3, 6),          // P4-Q3
    ];
    let mut incidence = vec![vec![0.0; edges.len()]; 8];
    for (j, &(p, q)) in edges.iter().enumerate() {
        incidence[p][j] = -1.0;
        incidence[q][j] = 1.0;
    }
    let incidence_rank = rank(incidence);
    let components = 8 - incidence_rank;
    let h1 = edges.len() - incidence_rank;
    assert_eq!(incidence_rank, 6);
    assert_eq!(components, 2);
    assert_eq!(h1, 0);

    let packet = serde_json::json!({
        "schema": "marici.benincasa.string.loaded_cousin_forest.v1",
        "entry": 1037,
        "source_entries": [1030, 1036],
        "pivot_walls": {
            "P1": "(A3*B34)^2-1",
            "P2": "A3^2-1",
            "P3": "(A2*B24)^2-1",
            "P4": "A2^2-1"
        },
        "loaded_walls": {
            "Q1": "(Z*A2)^2-1",
            "Q2": "(Z*A2*B24)^2-1",
            "Q3": "(A3/Z)^2-1",
            "Q4": "(A3*B34/Z)^2-1"
        },
        "labelled_edges": ["P1-Q2","P2-Q2","P3-Q4","P4-Q4","P2-Q1","P4-Q3"],
        "components": [["P1","Q2","P2","Q1"],["P3","Q4","P4","Q3"]],
        "component_shapes": ["path","path"],
        "incidence_rank": incidence_rank,
        "h0_rank": components,
        "h1_rank": h1,
        "corner_coefficients": ["1/(P1*Q2)","1/(P2*Q2)","1/(P3*Q4)","1/(P4*Q4)","1/(P2*Q1)","1/(P4*Q3)"],
        "classification": "the source-selected codimension-two occurrence diagram is a two-component forest and has no cycle coherence class"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-loaded-cousin-forest.json", &text).unwrap();
    print!("{text}");
}
