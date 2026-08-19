use serde_json::json;

fn rank(mut a: Vec<Vec<i64>>) -> usize {
    let rows = a.len();
    let cols = a[0].len();
    let mut r = 0;
    for c in 0..cols {
        let Some(p) = (r..rows).find(|&i| a[i][c] != 0) else { continue };
        a.swap(r, p);
        for i in 0..rows {
            if i == r || a[i][c] == 0 { continue; }
            let x = a[i][c];
            let y = a[r][c];
            for j in c..cols { a[i][j] = y * a[i][j] - x * a[r][j]; }
        }
        r += 1;
    }
    r
}

fn main() {
    // Vertices: P1,P2,P3,P4,Q1,Q2,Q3,Q4. Columns are oriented edges.
    let edges = [(0,5),(1,5),(2,7),(3,7),(1,4),(3,6),(4,5),(6,7)];
    let mut d1 = vec![vec![0_i64; edges.len()]; 8];
    for (j, &(from, to)) in edges.iter().enumerate() {
        d1[from][j] = -1;
        d1[to][j] = 1;
    }
    // F24 = e4 + e6 - e1; F34 = e5 + e7 - e3.
    let mut d2 = vec![vec![0_i64; 2]; edges.len()];
    for (edge, value) in [(4,1),(6,1),(1,-1)] { d2[edge][0] = value; }
    for (edge, value) in [(5,1),(7,1),(3,-1)] { d2[edge][1] = value; }

    let composite: Vec<Vec<i64>> = (0..8).map(|i|
        (0..2).map(|k| (0..8).map(|j| d1[i][j] * d2[j][k]).sum()).collect()
    ).collect();
    assert!(composite.iter().flatten().all(|&x| x == 0));
    let r1 = rank(d1);
    let r2 = rank(d2);
    let (h0, h1, h2) = (8-r1, 8-r1-r2, 2-r2);
    assert_eq!((r1,r2,h0,h1,h2), (6,2,2,0,0));

    println!("{}", serde_json::to_string_pretty(&json!({
        "schema": "marici.string.loaded_cousin_bar_cells.v1",
        "source_entries": [967, 1030, 1037],
        "vertices": ["P1","P2","P3","P4","Q1","Q2","Q3","Q4"],
        "transition_edges": ["Q1->Q2 via B24^2", "Q3->Q4 via B34^2"],
        "bar_cells": {
            "F24": "e4+e6-e1",
            "F34": "e5+e7-e3"
        },
        "chain_condition": true,
        "ranks": {"d1": r1, "d2": r2},
        "homology": {"h0": h0, "h1": h1, "h2": h2},
        "classification": "the two source bar cells fill the only cycles in the source-selected loaded Cousin nerve"
    })).unwrap());
}
