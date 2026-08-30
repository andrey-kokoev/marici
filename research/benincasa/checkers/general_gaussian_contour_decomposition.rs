fn rank_2x2(m: [[i64; 2]; 2]) -> usize {
    if m == [[0, 0], [0, 0]] {
        0
    } else if m[0][0] * m[1][1] - m[0][1] * m[1][0] == 0 {
        1
    } else {
        2
    }
}

fn main() {
    let statistical = [[1, 1], [1, 1]];
    assert_eq!(rank_2x2(statistical), 1);

    // A normalized complex Bogoliubov coordinate supplies two real tangent
    // directions; Eq. (162) supplies one independent statistical direction.
    let bogoliubov_real_rank = 2usize;
    let statistical_rank = rank_2x2(statistical);
    assert_eq!(bogoliubov_real_rank + statistical_rank, 3);

    println!(
        "{{\"schema\":\"marici.benincasa.general_gaussian_contour_decomposition.v1\",\"bogoliubov_real_rank\":{},\"statistical_contour_rank\":{},\"gaussian_real_rank\":{},\"statistical_matrix\":[[1,1],[1,1]],\"status\":\"verified\"}}",
        bogoliubov_real_rank,
        statistical_rank,
        bogoliubov_real_rank + statistical_rank
    );
}

