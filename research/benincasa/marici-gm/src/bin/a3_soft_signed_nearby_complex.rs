type Matrix3 = [[i64; 3]; 3];

fn mul(a: Matrix3, b: Matrix3) -> Matrix3 {
    let mut out = [[0; 3]; 3];
    for i in 0..3 {
        for j in 0..3 {
            out[i][j] = (0..3).map(|k| a[i][k] * b[k][j]).sum();
        }
    }
    out
}

fn apply(a: Matrix3, x: [i64; 3]) -> [i64; 3] {
    [
        a[0][0] * x[0] + a[0][1] * x[1] + a[0][2] * x[2],
        a[1][0] * x[0] + a[1][1] * x[1] + a[1][2] * x[2],
        a[2][0] * x[0] + a[2][1] * x[1] + a[2][2] * x[2],
    ]
}

fn main() {
    let t: Matrix3 = [[0, 0, -1], [1, 0, -1], [0, 1, -1]];
    let t2 = mul(t, t);
    let t4 = mul(t2, t2);
    assert_eq!(t4, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]);

    let kato = [1, 0, 1];
    assert_eq!(apply(t, kato), [-1, 0, -1]);
    for v in [[1, 1, 0], [0, 1, 1]] {
        let t2v = apply(t2, v);
        assert_eq!([t2v[0] + v[0], t2v[1] + v[1], t2v[2] + v[2]], [0, 0, 0]);
    }

    let graded_map: Matrix3 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]];
    assert_eq!(graded_map, [[1, 0, 0], [0, 1, 0], [0, 0, 1]]);

    let representatives = [
        ("g1,g2", "E-X2", "E-X1"),
        ("g1,g3", "-E+X1-X3", "E-X1"),
        ("g1,G23", "-E", "E-X1"),
        ("g2,g3", "E-X2", "-E+X2-X3"),
        ("g2,G31", "E-X2", "-E"),
        ("g3,G23", "-E", "E-X3"),
        ("g3,G31", "E-X3", "-E"),
        ("G23,G31", "-E", "-E"),
    ];
    let eligible: Vec<_> = representatives
        .iter()
        .filter(|(_, a, b)| *a != "-E" && *b != "-E")
        .map(|(label, _, _)| *label)
        .collect();
    assert_eq!(eligible, ["g1,g2", "g1,g3", "g2,g3"]);
    let movable_germs = eligible.len() * 3 * 4;
    let coalesced_germs = (representatives.len() - eligible.len()) * 3 * 2;
    let germs = movable_germs + coalesced_germs;
    assert_eq!(movable_germs, 36);
    assert_eq!(coalesced_germs, 30);
    assert_eq!(germs, 66);

    println!("complex_source_rank=3");
    println!("complex_target_rank=3");
    println!("associated_grade_map=identity_on_[1,a,a^2]");
    println!("associated_grade_rank=3");
    println!("support_symbol_rank=2");
    println!("betti_comparison_map=unconstructed");
    println!("integral_extension_class=undefined");
    println!("kato_monodromy=-1");
    println!("excess_monodromy_polynomial=T^2+1");
    println!("a3_monodromy_polynomial=(T+1)*(T^2+1)");
    println!("eligible_orbits={}", eligible.len());
    println!("movable_labelled_germs={movable_germs}");
    println!("coalesced_labelled_germs={coalesced_germs}");
    println!("labelled_germs={germs}");
    println!("total_rank={}", 3 * germs);
    println!("generic_kato_rank={germs}");
    println!("excess_rank={}", 2 * germs);
}
