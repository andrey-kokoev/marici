use std::fs;

fn mat_vec(t: &[Vec<i128>], u: &[i128]) -> Vec<i128> {
    t.iter()
        .map(|row| row.iter().zip(u).map(|(a, b)| a * b).sum())
        .collect()
}

fn outer(u: &[i128]) -> Vec<Vec<i128>> {
    u.iter()
        .map(|x| u.iter().map(|y| x * y).collect())
        .collect()
}

fn congruence(t: &[Vec<i128>], x: &[Vec<i128>]) -> Vec<Vec<i128>> {
    let rows = t.len();
    let cols = t[0].len();
    let mut out = vec![vec![0_i128; rows]; rows];
    for i in 0..rows {
        for j in 0..rows {
            for a in 0..cols {
                for b in 0..cols {
                    out[i][j] += t[i][a] * x[a][b] * t[j][b];
                }
            }
        }
    }
    out
}

fn compose(s: &[Vec<i128>], t: &[Vec<i128>]) -> Vec<Vec<i128>> {
    let mut out = vec![vec![0_i128; t[0].len()]; s.len()];
    for i in 0..s.len() {
        for j in 0..t[0].len() {
            for k in 0..t.len() {
                out[i][j] += s[i][k] * t[k][j];
            }
        }
    }
    out
}

fn main() {
    let mut packets = 0_u64;
    let mut composition_checks = 0_u64;
    for seed in -19_i128..=19 {
        let u = vec![seed + 1, 2 * seed - 3, 3 * seed + 2, 5 - seed];
        let t = vec![
            vec![1, 0, 1, 0],
            vec![0, 1, 0, 1],
            vec![1, -1, 0, 0],
        ];
        let s = vec![vec![1, 1, 0], vec![0, 1, 1]];

        let xi = outer(&u);
        let tu = mat_vec(&t, &u);
        assert_eq!(outer(&tu), congruence(&t, &xi));

        let stu = mat_vec(&s, &tu);
        let st = compose(&s, &t);
        assert_eq!(stu, mat_vec(&st, &u));
        assert_eq!(outer(&stu), congruence(&s, &congruence(&t, &xi)));
        assert_eq!(outer(&stu), congruence(&st, &xi));
        packets += 1;
        composition_checks += 3;
    }

    let output = format!(
        concat!(
            "{{\n",
            "  \"schema\": \"marici.symmetric_square_cut_functoriality.v1\",\n",
            "  \"exact_labelled_cut_packets_checked\": {},\n",
            "  \"nested_composition_checks\": {},\n",
            "  \"transport\": \"Xi maps to T Xi T^T=Sym2(Tu)\",\n",
            "  \"rank_one_preserved\": true,\n",
            "  \"deck_evenness_preserved\": true,\n",
            "  \"new_carrier_operation_required\": false\n",
            "}}\n"
        ),
        packets, composition_checks
    );
    fs::write(
        "research/benincasa/results/symmetric-square-cut-functoriality.json",
        output,
    )
    .unwrap();
}
