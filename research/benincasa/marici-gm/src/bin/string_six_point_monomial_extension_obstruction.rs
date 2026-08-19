use serde_json::json;

fn column_counts(m: &[Vec<i32>]) -> Vec<usize> {
    (0..m[0].len())
        .map(|j| m.iter().filter(|row| row[j] != 0).count())
        .collect()
}

fn main() {
    // Support of Entry 967's fixed labelled loaded comparison.
    let mut loaded = vec![vec![0i32; 6]; 6];
    loaded[1][0] = 1;
    loaded[2][1] = -1;
    loaded[3][1] = 1;
    loaded[4][2] = 1;
    loaded[3][3] = 1;
    loaded[0][4] = -1;
    loaded[1][4] = 1;
    loaded[5][5] = 1;

    // Entry 974's permutation support.  Multiplication by nonzero diagonal
    // rational functions cannot change this support count.
    let p = [4usize, 1, 0, 5, 3, 2];
    let mut monomial = vec![vec![0i32; 6]; 6];
    for (i, &j) in p.iter().enumerate() {
        monomial[j][i] = 1;
    }

    let loaded_counts = column_counts(&loaded);
    let monomial_counts = column_counts(&monomial);
    assert_eq!(loaded_counts, vec![1, 2, 1, 1, 2, 1]);
    assert_eq!(monomial_counts, vec![1, 1, 1, 1, 1, 1]);
    let circuit_columns: Vec<_> = loaded_counts
        .iter()
        .enumerate()
        .filter_map(|(j, n)| (*n == 2).then_some(j))
        .collect();
    assert_eq!(circuit_columns, vec![1, 4]);

    let packet = json!({
        "schema":"marici.benincasa.string_six_point_monomial_extension_obstruction.v1",
        "loaded_support_matrix":loaded,
        "labelled_permutation_support_matrix":monomial,
        "loaded_column_support_counts":loaded_counts,
        "monomial_column_support_counts":monomial_counts,
        "two_term_circuit_columns":circuit_columns,
        "invariant_under_nonzero_diagonal_scaling":true,
        "invariant_under_row_and_column_permutation":"multiset of column support counts",
        "monomial_extension_possible_in_fixed_labelled_bases":false,
        "classification":"the exceptional-row factorization cannot extend as permutation times diagonal because two frozen source columns are two-term circuit boundaries",
        "required_next_datum":"a chain-level pivot-transition homotopy or source-derived nonmonomial target transformation"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-monomial-extension-obstruction.json", &text).unwrap();
    print!("{text}");
}
