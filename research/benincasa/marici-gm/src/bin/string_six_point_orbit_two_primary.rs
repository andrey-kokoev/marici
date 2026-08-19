use serde_json::json;

fn rank_mod(mut a: Vec<Vec<i64>>, p: i64) -> usize {
    let rows = a.len();
    let cols = a[0].len();
    let mut rank = 0;
    for col in 0..cols {
        let Some(pivot) = (rank..rows).find(|&r| a[r][col].rem_euclid(p) != 0) else { continue };
        a.swap(rank, pivot);
        let x = a[rank][col].rem_euclid(p);
        let inv = (1..p).find(|y| (x * y).rem_euclid(p) == 1).unwrap();
        for j in col..cols { a[rank][j] = (a[rank][j] * inv).rem_euclid(p); }
        for i in 0..rows {
            if i == rank { continue; }
            let c = a[i][col].rem_euclid(p);
            for j in col..cols {
                a[i][j] = (a[i][j] - c * a[rank][j]).rem_euclid(p);
            }
        }
        rank += 1;
        if rank == rows { break; }
    }
    rank
}

fn main() {
    // Rows have character multiplicities (2,1,1,2).  The two columns seeds
    // model the two X sheets after localization at the nonunit Fitting
    // factors.  Each seed is translated through all four group elements.
    let chars = [
        [1, -1, -1, 1], // --
        [1, -1,  1,-1], // -+
        [1,  1, -1,-1], // +-
        [1,  1,  1, 1], // ++
    ];
    let row_char = [0usize, 0, 1, 2, 3, 3];
    let seeds = [
        [1, 0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 1],
    ];
    let mut matrix = vec![vec![0i64; 8]; 6];
    for seed in 0..2 {
        for g in 0..4 {
            for row in 0..6 {
                matrix[row][4 * seed + g] = seeds[seed][row] * chars[row_char[row]][g];
            }
        }
    }
    let rational_rank = rank_mod(matrix.clone(), 101);
    let mod_two_rank = rank_mod(matrix.clone(), 2);
    assert_eq!(rational_rank, 6);
    assert_eq!(mod_two_rank, 2);
    let even_invariant_factor_lower_bound = rational_rank - mod_two_rank;
    assert_eq!(even_invariant_factor_lower_bound, 4);

    let packet = json!({
        "schema":"marici.benincasa.string_six_point_orbit_two_primary.v1",
        "shift_group":"(Z/2)^2",
        "source_seed_count":2,
        "orbit_columns_per_seed":4,
        "character_multiplicities":[2,1,1,2],
        "generic_rank":rational_rank,
        "mod_two_rank":mod_two_rank,
        "even_invariant_factor_lower_bound":even_invariant_factor_lower_bound,
        "index_divisibility_lower_bound":16,
        "reason":"all four translates of each seed coincide modulo 2",
        "scope":"orbit lattice after localization away from the nonunit kinematic Fitting factors",
        "exact_smith_form":"not determined"
    });
    let text = serde_json::to_string_pretty(&packet).unwrap() + "\n";
    std::fs::write("../string-six-point-orbit-two-primary.json", &text).unwrap();
    print!("{text}");
}
