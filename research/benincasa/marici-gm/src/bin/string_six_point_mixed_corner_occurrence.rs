use std::collections::HashMap;

type Word3 = [usize; 3];
type Word6 = [usize; 6];

fn sigma_label(i: usize) -> usize {
    match i {
        2 => 3,
        3 => 4,
        4 => 2,
        _ => i,
    }
}

fn sigma3(w: Word3) -> Word3 {
    [sigma_label(w[0]), sigma_label(w[1]), sigma_label(w[2])]
}

fn sigma6(w: Word6) -> Word6 {
    [
        sigma_label(w[0]),
        sigma_label(w[1]),
        sigma_label(w[2]),
        sigma_label(w[3]),
        sigma_label(w[4]),
        sigma_label(w[5]),
    ]
}

fn permutation3(source: &[Word3], target: &[Word3]) -> Vec<usize> {
    let positions: HashMap<Word3, usize> = target
        .iter()
        .copied()
        .enumerate()
        .map(|(i, w)| (w, i))
        .collect();
    source.iter().map(|w| positions[&sigma3(*w)]).collect()
}

fn permutation6(source: &[Word6], target: &[Word6]) -> Vec<usize> {
    let positions: HashMap<Word6, usize> = target
        .iter()
        .copied()
        .enumerate()
        .map(|(i, w)| (w, i))
        .collect();
    source.iter().map(|w| positions[&sigma6(*w)]).collect()
}

fn compose(left: &[usize], right: &[usize]) -> Vec<usize> {
    right.iter().map(|i| left[*i]).collect()
}

fn main() {
    // C0=(s34,s345), C1=(s24,s245), C2=(s23,s235).
    // The ordering is source-fixed in each occurrence chart.
    let dense = [
        vec![[2, 3, 4], [2, 4, 3]],
        vec![[3, 2, 4], [3, 4, 2]],
        vec![[4, 2, 3], [4, 3, 2]],
    ];
    let sparse = [
        vec![[1, 5, 3, 4, 6, 2], [1, 5, 4, 3, 6, 2]],
        vec![[1, 5, 2, 4, 6, 3], [1, 5, 4, 2, 6, 3]],
        vec![[1, 5, 2, 3, 6, 4], [1, 5, 3, 2, 6, 4]],
    ];
    let third_normals = [[1, 2], [1, 3], [1, 4]];

    let dense_maps: Vec<Vec<usize>> = (0..3)
        .map(|i| permutation3(&dense[i], &dense[(i + 1) % 3]))
        .collect();
    let sparse_maps: Vec<Vec<usize>> = (0..3)
        .map(|i| permutation6(&sparse[i], &sparse[(i + 1) % 3]))
        .collect();

    assert_eq!(dense_maps, vec![vec![1, 0], vec![1, 0], vec![0, 1]]);
    assert_eq!(sparse_maps, vec![vec![1, 0], vec![1, 0], vec![0, 1]]);

    let dense_cycle = compose(&dense_maps[2], &compose(&dense_maps[1], &dense_maps[0]));
    let sparse_cycle = compose(&sparse_maps[2], &compose(&sparse_maps[1], &sparse_maps[0]));
    assert_eq!(dense_cycle, vec![0, 1]);
    assert_eq!(sparse_cycle, vec![0, 1]);

    let transported_normals: Vec<[usize; 2]> = third_normals
        .iter()
        .map(|normal| [sigma_label(normal[0]), sigma_label(normal[1])])
        .collect();
    assert_eq!(
        transported_normals,
        vec![third_normals[1], third_normals[2], third_normals[0]]
    );

    // A transition matrix has variance B x D. Conjugating its rank-one
    // exceptional block therefore uses the sparse permutation on rows and
    // the inverse dense permutation on columns. At the first two moves both
    // are J, so their orientation signs cancel; the third move is identity.
    let signed_steps: Vec<i32> = sparse_maps
        .iter()
        .zip(&dense_maps)
        .map(|(b, d)| {
            let sign = |p: &[usize]| if p == [1, 0] { -1 } else { 1 };
            sign(b) * sign(d)
        })
        .collect();
    assert_eq!(signed_steps, vec![1, 1, 1]);
    assert_eq!(signed_steps.iter().product::<i32>(), 1);

    // sigma acts by literal relabelling on U_12-1, U_13-1, U_14-1.
    // It neither inverts nor negates a conormal generator, so the first
    // associated grade has trivial normal-line character.
    let normal_line_steps = vec![1, 1, 1];
    let filtered_signed_steps: Vec<i32> = signed_steps
        .iter()
        .zip(&normal_line_steps)
        .map(|(basis, normal)| basis * normal)
        .collect();
    assert_eq!(filtered_signed_steps.iter().product::<i32>(), 1);

    println!(
        "{{\"schema\":\"marici.benincasa.string_six_point_mixed_corner_occurrence.v2\",\"corner_orbit\":[\"(s34,s345)\",\"(s24,s245)\",\"(s23,s235)\"],\"third_normal_orbit\":[\"s12\",\"s13\",\"s14\"],\"dense_permutations\":{:?},\"sparse_permutations\":{:?},\"signed_steps\":{:?},\"normal_line_steps\":{:?},\"filtered_signed_steps\":{:?},\"dense_cycle_identity\":true,\"sparse_cycle_identity\":true,\"signed_cyclic_composition\":1,\"filtered_signed_cyclic_composition\":1}}",
        dense_maps, sparse_maps, signed_steps, normal_line_steps, filtered_signed_steps
    );
}
