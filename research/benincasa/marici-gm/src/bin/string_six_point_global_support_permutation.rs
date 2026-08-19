use serde_json::json;

fn main() {
    let corner = ["123456", "124356", "142356", "132456", "134256", "143256"];
    let dense = ["123456", "124356", "132456", "134256", "142356", "143256"];

    // Entry 971 fixes the singleton images.  Entry 973 fixes both repeated
    // blocks to the swap J in their source-labelled orders.
    let occurrence_to_dense = [4usize, 1, 0, 5, 3, 2];
    let expected_blocks = [
        (vec![0usize], vec![4usize]),
        (vec![1usize, 2], vec![1usize, 0]),
        (vec![3usize], vec![5usize]),
        (vec![4usize, 5], vec![3usize, 2]),
    ];

    let mut seen = [false; 6];
    for &j in &occurrence_to_dense {
        assert!(j < 6 && !seen[j]);
        seen[j] = true;
    }
    assert!(seen.iter().all(|x| *x));

    for (src, target) in &expected_blocks {
        let image: Vec<_> = src.iter().map(|i| occurrence_to_dense[*i]).collect();
        assert_eq!(&image, target);
    }

    let mut matrix = vec![vec![0i32; 6]; 6];
    for (i, &j) in occurrence_to_dense.iter().enumerate() {
        matrix[j][i] = 1;
    }
    for row in &matrix {
        assert_eq!(row.iter().sum::<i32>(), 1);
    }
    for col in 0..6 {
        assert_eq!(matrix.iter().map(|row| row[col]).sum::<i32>(), 1);
    }

    // The permutation is the five-cycle (0 4 3 5 2), with 1 fixed.
    let cycle = [0usize, 4, 3, 5, 2];
    for k in 0..cycle.len() {
        assert_eq!(occurrence_to_dense[cycle[k]], cycle[(k + 1) % cycle.len()]);
    }
    assert_eq!(occurrence_to_dense[1], 1);
    let determinant = 1i32;

    let packet = json!({
        "schema":"marici.benincasa.string_six_point_global_support_permutation.v1",
        "corner_occurrence_order":corner,
        "dense_six_word_order":dense,
        "occurrence_to_dense_indices":occurrence_to_dense,
        "occurrence_to_dense_labels":occurrence_to_dense.iter().map(|j| dense[*j]).collect::<Vec<_>>(),
        "matrix_dense_rows_corner_columns":matrix,
        "block_images":[
            {"factor":"(ZA2)^2-1","corner":[0],"dense":[4]},
            {"factor":"(ZA2B24)^2-1","corner":[1,2],"dense":[1,0]},
            {"factor":"(A3/Z)^2-1","corner":[3],"dense":[5]},
            {"factor":"(A3B34/Z)^2-1","corner":[4,5],"dense":[3,2]}
        ],
        "cycle_decomposition":[[0,4,3,5,2],[1]],
        "determinant":determinant,
        "classification":"the four source-labelled localized maps assemble uniquely into one orientation-preserving six-occurrence support permutation",
        "scope":"support and labelled ordering only; equality with the complete rational transition remains unproved"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-global-support-permutation.json", &text).unwrap();
    print!("{text}");
}
