type Matrix = Vec<Vec<i64>>;

fn rank(mut a: Matrix) -> usize {
    let rows = a.len();
    let cols = a.first().map_or(0, Vec::len);
    let mut r = 0;
    for c in 0..cols {
        let Some(pivot) = (r..rows).find(|&i| a[i][c] != 0) else { continue };
        a.swap(r, pivot);
        let p = a[r][c];
        for i in r + 1..rows {
            if a[i][c] == 0 { continue; }
            let q = a[i][c];
            for j in c..cols { a[i][j] = p * a[i][j] - q * a[r][j]; }
        }
        r += 1;
    }
    r
}

fn multiply(a: &Matrix, b: &Matrix) -> Matrix {
    let mut out = vec![vec![0; b[0].len()]; a.len()];
    for i in 0..a.len() {
        for k in 0..b.len() {
            for j in 0..b[0].len() { out[i][j] += a[i][k] * b[k][j]; }
        }
    }
    out
}

fn main() {
    // Ordered marked basis: Omega111, Omega101, Omega110, e1,...,e9.
    let mut j_star = vec![vec![0; 9]; 12];
    for i in 0..9 { j_star[3 + i][i] = 1; }

    // Residue bases are (top_from_Wi, primitive_Wi).  From da^db orientation:
    // Res_W1 Omega111=-da/(L2 sqrt K), Res_W1 Omega101=-da/sqrt K;
    // Res_W2 Omega111=+db/(L1 sqrt K), Res_W2 Omega110=+db/sqrt K.
    let mut res_w1 = vec![vec![0; 12]; 2];
    res_w1[0][0] = -1; res_w1[1][1] = -1;
    let mut res_w2 = vec![vec![0; 12]; 2];
    res_w2[0][0] = 1; res_w2[1][2] = 1;
    let stacked = [res_w1.clone(), res_w2.clone()].concat();

    // The same-sheet top differential adds the two oriented iterated residues.
    let res_top = vec![vec![1, 0, 1, 0]];
    assert_eq!(multiply(&res_top, &stacked), vec![vec![0; 12]]);
    assert_eq!(rank(stacked.clone()), 3);
    assert_eq!(rank(res_top.clone()), 1);
    assert_eq!(4 - rank(res_top.clone()), rank(stacked.clone()));

    // Source-normalized H1(W) basis is the three columns induced by
    // Omega111, Omega101, Omega110.
    let mut res_w = vec![vec![0; 12]; 3];
    for i in 0..3 { res_w[i][i] = 1; }
    assert_eq!(rank(j_star.clone()), 9);
    assert_eq!(rank(res_w.clone()), 3);
    assert_eq!(multiply(&res_w, &j_star), vec![vec![0; 9]; 3]);
    assert_eq!(rank(j_star.clone()) + rank(res_w.clone()), 12);

    println!("basis12=[Omega111,Omega101,Omega110,e1,...,e9]");
    println!("j_star=bottom_identity_12x9");
    println!("Res_W1(Omega111,Omega101)=[-top1,-wall1]");
    println!("Res_W2(Omega111,Omega110)=[+top2,+wall2]");
    println!("Res_top=[1,0,1,0]");
    println!("rank_j_star=9");
    println!("rank_Res_W=3");
    println!("Res_W*j_star=0");
    println!("image_stacked_residues=kernel_Res_top=true");
}
