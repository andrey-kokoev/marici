use serde_json::json;

fn gcd(mut a: i64, mut b: i64) -> i64 {
    a = a.abs(); b = b.abs();
    while b != 0 { let r = a % b; a = b; b = r; }
    a
}

fn main() {
    let chars = [
        [1,-1,-1,1], [1,-1,1,-1], [1,1,-1,-1], [1,1,1,1]
    ];
    let row_char = [0usize,0,1,2,3,3];
    let seeds = [[1,0,1,1,1,0],[0,1,1,1,0,1]];
    let component = [0usize,0,1,1,0,1];
    let mut augmentation = vec![vec![0_i64; 8]; 2];
    for seed in 0..2 {
        for g in 0..4 {
            for row in 0..6 {
                augmentation[component[row]][4*seed+g] +=
                    seeds[seed][row] * chars[row_char[row]][g];
            }
        }
    }
    assert_eq!(augmentation, vec![
        vec![2,0,0,2,1,-1,-1,1],
        vec![2,0,0,-2,3,1,1,-1],
    ]);
    let d1 = augmentation.iter().flatten().fold(0, |d,&x| gcd(d,x));
    let mut d2 = 0;
    for i in 0..8 { for j in i+1..8 {
        d2 = gcd(d2, augmentation[0][i]*augmentation[1][j]
            - augmentation[0][j]*augmentation[1][i]);
    }}
    assert_eq!((d1,d2/d1), (1,4));
    println!("{}", serde_json::to_string_pretty(&json!({
        "schema":"marici.string.loaded_cousin_integral_h0.v1",
        "occurrence_components":{"left":[0,1,4],"right":[2,3,5]},
        "augmentation_matrix":augmentation,
        "smith_invariants":[d1,d2/d1],
        "image_index":d2,
        "cokernel":"Z/4",
        "rational_h0_rank":2,
        "classification":"the native two-seed orbit reaches both Cousin components rationally but has index four in their integral augmentation lattice"
    })).unwrap());
}
