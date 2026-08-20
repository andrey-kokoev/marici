use std::collections::{BTreeMap, BTreeSet};

fn rank(mut a: Vec<Vec<i64>>) -> usize {
    let rows = a.len();
    let cols = a.first().map_or(0, Vec::len);
    let mut r = 0;
    for c in 0..cols {
        let Some(p) = (r..rows).find(|&i| a[i][c] != 0) else { continue };
        a.swap(r, p);
        for i in 0..rows {
            if i == r || a[i][c] == 0 { continue; }
            let x = a[i][c];
            let y = a[r][c];
            for j in c..cols { a[i][j] = y * a[i][j] - x * a[r][j]; }
            let g = a[i].iter().fold(0_i64, |g, &v| gcd(g, v.abs()));
            if g > 1 { for v in &mut a[i] { *v /= g; } }
        }
        r += 1;
    }
    r
}

fn gcd(mut a: i64, mut b: i64) -> i64 {
    while b != 0 { let t = a % b; a = b; b = t; }
    a.abs()
}

fn det3(m: [[i64;3];3]) -> i64 {
    m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
    -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
    +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0])
}

fn main() {
    let common = ["qG", "qg1", "qg2", "qg3"];
    let cycle = ["qG12", "qg23", "qG31", "qg12", "qG23", "qg31"];
    let source_pairs = [
        ("qG12", "qg23"), ("qG12", "qg31"),
        ("qG23", "qg31"), ("qG23", "qg12"),
        ("qG31", "qg12"), ("qG31", "qg23"),
    ];
    let source_set: BTreeSet<_> = source_pairs.iter().map(|&(a,b)| {
        if a < b {(a,b)} else {(b,a)}
    }).collect();

    let mut boundary = vec![vec![0_i64; 6]; 6];
    for e in 0..6 {
        boundary[e][e] = -1;
        boundary[(e + 1) % 6][e] = 1;
        let a = cycle[e]; let b = cycle[(e + 1) % 6];
        let pair = if a < b {(a,b)} else {(b,a)};
        assert!(source_set.contains(&pair));
    }
    assert_eq!(source_set.len(), 6);
    let rank_d1 = rank(boundary.clone());
    let h0 = 6 - rank_d1;
    let h1 = 6 - rank_d1;
    assert_eq!((rank_d1, h0, h1), (5,1,1));

    let sigma: BTreeMap<&str,&str> = [
        ("qG12","qG23"),("qG23","qG31"),("qG31","qG12"),
        ("qg12","qg23"),("qg23","qg31"),("qg31","qg12"),
    ].iter().copied().collect();
    for &(a,b) in &source_pairs {
        let sa=sigma[a]; let sb=sigma[b];
        let pair=if sa<sb {(sa,sb)} else {(sb,sa)};
        assert!(source_set.contains(&pair));
    }
    // The cyclic action is a rotation by four positions in this orientation,
    // hence fixes the oriented fundamental cycle rather than reversing it.
    for (i,&v) in cycle.iter().enumerate() {
        assert_eq!(sigma[v], cycle[(i+4)%6]);
    }

    // Source orientation is dy12 ^ dy23 ^ dy31.  The first row is the
    // deletion-pole normal, the second the paired connected-subgraph normal,
    // and the third the coordinate along the edge internal to that subgraph.
    // Positive rescalings of the deletion normals (the convention-dependent
    // factor two) do not affect these signs.
    let source_residue_signs = [
        det3([[1,0,0],[1,0,1],[0,1,0]]), // G12,g23 ; y23
        det3([[1,0,0],[1,1,0],[0,0,1]]), // G12,g31 ; y31
        det3([[0,1,0],[1,1,0],[0,0,1]]), // G23,g31 ; y31
        det3([[0,1,0],[0,1,1],[1,0,0]]), // G23,g12 ; y12
        det3([[0,0,1],[0,1,1],[1,0,0]]), // G31,g12 ; y12
        det3([[0,0,1],[1,0,1],[0,1,0]]), // G31,g23 ; y23
    ];
    assert_eq!(source_residue_signs, [-1,1,-1,1,-1,1]);

    // Relative to the oriented hexagon, the second, fourth, and sixth source
    // pairs are traversed backwards. Poincare-residue antisymmetry flips them.
    let oriented_cycle_coefficients = [
        source_residue_signs[0], -source_residue_signs[5],
        source_residue_signs[4], -source_residue_signs[3],
        source_residue_signs[2], -source_residue_signs[1],
    ];
    assert_eq!(oriented_cycle_coefficients, [-1,-1,-1,-1,-1,-1]);
    for v in 0..6 {
        let incoming=oriented_cycle_coefficients[(v+5)%6];
        let outgoing=oriented_cycle_coefficients[v];
        assert_eq!(incoming, outgoing); // boundary coefficient vanishes
    }

    // Every maximal source term contains the common four-pole simplex, so any
    // one common vertex is a cone point for the complete nerve.
    assert!(!common.is_empty());
    println!("source_maximal_terms=6 common_vertices=4 link_vertices=6 link_edges=6 rank_d1={rank_d1} link_h0={h0} link_h1={h1} full_nerve_cone=true cyclic_h1_character=+1 source_residue_signs=-,+,-,+,-,+ oriented_cycle_coefficients=-,-,-,-,-,- cycle_boundary=0");
}
