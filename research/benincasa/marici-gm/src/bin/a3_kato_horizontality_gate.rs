type Matrix3 = [[i64; 3]; 3];

fn apply(a: Matrix3, x: [i64; 3]) -> [i64; 3] {
    [
        a[0][0] * x[0] + a[0][1] * x[1] + a[0][2] * x[2],
        a[1][0] * x[0] + a[1][1] * x[1] + a[1][2] * x[2],
        a[2][0] * x[0] + a[2][1] * x[1] + a[2][2] * x[2],
    ]
}

fn cartan_norm(x: [i64; 3]) -> i64 {
    2 * (x[0] * x[0] + x[1] * x[1] + x[2] * x[2]) - 2 * (x[0] * x[1] + x[1] * x[2])
}

fn main() {
    let t: Matrix3 = [[0, 0, -1], [1, 0, -1], [0, 1, -1]];
    let minus_line = [1, 0, 1];
    assert_eq!(apply(t, minus_line), [-1, 0, -1]);
    assert_eq!(cartan_norm(minus_line), 4);

    // Every A1 vanishing cycle is an A3 root and has norm two.  Enumerate
    // the finite root set in the simple-root box and verify none spans the
    // rational (-1)-eigenline.
    let mut roots = Vec::new();
    for x in -1..=1 {
        for y in -1..=1 {
            for z in -1..=1 {
                let v = [x, y, z];
                if cartan_norm(v) == 2 {
                    roots.push(v);
                    assert_ne!(apply(t, v), [-v[0], -v[1], -v[2]]);
                }
            }
        }
    }
    assert_eq!(roots.len(), 12);

    let labelled_root = [1, 0, 0];
    let defect = {
        let tv = apply(t, labelled_root);
        [
            tv[0] + labelled_root[0],
            tv[1] + labelled_root[1],
            tv[2] + labelled_root[2],
        ]
    };
    assert_eq!(defect, [1, 1, 0]);

    println!("a3_root_count={}", roots.len());
    println!("minus_eigenline_generator=[1,0,1]");
    println!("minus_eigenline_norm=4");
    println!("a1_root_norm=2");
    println!("horizontal_a1_root_count=0");
    println!("labelled_root=[1,0,0]");
    println!("monodromy_defect=[1,1,0]");
    println!("strict_rank_two_quotient_local_system=false");
    println!("required_object=homotopy_coherent_mapping_cone");
}
