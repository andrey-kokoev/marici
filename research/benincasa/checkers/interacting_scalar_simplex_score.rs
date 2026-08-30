// Exact finite-field rank certificate for the external-energy score tower of
// the six labelled simplex routes in arXiv:2408.16386, eq. (4.15).

const P: i64 = 1_000_000_007;

fn add(a: i64, b: i64) -> i64 { (a + b).rem_euclid(P) }
fn mul(a: i64, b: i64) -> i64 { ((a as i128 * b as i128) % P as i128) as i64 }
fn pow(mut a: i64, mut n: i64) -> i64 {
    let mut r = 1i64;
    while n > 0 {
        if n & 1 == 1 { r = mul(r, a); }
        a = mul(a, a);
        n >>= 1;
    }
    r
}
fn inv(a: i64) -> i64 { pow(a.rem_euclid(P), P - 2) }

#[derive(Clone, Copy)]
struct Linear {
    value: i64,
    grad: [i64; 3],
    ygrad: [i64; 3],
}

fn route_jet(a: Linear, b: Linear) -> [i64; 10] {
    let ia = inv(a.value);
    let ib = inv(b.value);
    let f = mul(ia, ib);
    let mut out = [0i64; 10];
    out[0] = f;
    let mut ell = [0i64; 3];
    for i in 0..3 {
        ell[i] = add(mul(a.grad[i], ia), mul(b.grad[i], ib));
        out[1 + i] = -mul(f, ell[i]);
    }
    let pairs = [(0,0),(0,1),(0,2),(1,1),(1,2),(2,2)];
    for (k, (i,j)) in pairs.iter().enumerate() {
        let aa = mul(mul(a.grad[*i], a.grad[*j]), mul(ia, ia));
        let bb = mul(mul(b.grad[*i], b.grad[*j]), mul(ib, ib));
        out[4 + k] = mul(f, add(add(mul(ell[*i], ell[*j]), aa), bb));
    }
    out
}

fn route_normal(a: Linear, b: Linear, direction: [i64; 3]) -> i64 {
    let ia = inv(a.value);
    let ib = inv(b.value);
    let f = mul(ia, ib);
    let da = (0..3).fold(0, |s, i| add(s, mul(a.ygrad[i], direction[i])));
    let db = (0..3).fold(0, |s, i| add(s, mul(b.ygrad[i], direction[i])));
    -mul(f, add(mul(da, ia), mul(db, ib)))
}

fn rank(mut m: Vec<Vec<i64>>) -> usize {
    let rows = m.len();
    let cols = m[0].len();
    let mut r = 0usize;
    for c in 0..cols {
        let Some(pivot) = (r..rows).find(|&i| m[i][c] != 0) else { continue };
        m.swap(r, pivot);
        let s = inv(m[r][c]);
        for j in c..cols { m[r][j] = mul(m[r][j], s); }
        for i in 0..rows {
            if i == r || m[i][c] == 0 { continue; }
            let t = m[i][c];
            for j in c..cols { m[i][j] = add(m[i][j], -mul(t, m[r][j])); }
        }
        r += 1;
        if r == rows { break; }
    }
    r
}

fn main() {
    // Generic exact point X=(2,3,5), (y12,y23,y31)=(7,11,13).
    // q_Gij = E+yij and q_gij = Xi+Xj + the two cut-edge weights.
    let g12 = Linear { value: 10 + 7, grad: [1,1,1], ygrad: [1,0,0] };
    let g23 = Linear { value: 10 + 11, grad: [1,1,1], ygrad: [0,1,0] };
    let g31 = Linear { value: 10 + 13, grad: [1,1,1], ygrad: [0,0,1] };
    let s23 = Linear { value: 3 + 5 + 7 + 13, grad: [0,1,1], ygrad: [1,0,1] };
    let s31 = Linear { value: 5 + 2 + 7 + 11, grad: [1,0,1], ygrad: [1,1,0] };
    let s12 = Linear { value: 2 + 3 + 11 + 13, grad: [1,1,0], ygrad: [0,1,1] };

    // Source order from eq. (4.15).
    let routes = [
        route_jet(g12, s23),
        route_jet(g12, s31),
        route_jet(g23, s31),
        route_jet(g23, s12),
        route_jet(g31, s12),
        route_jet(g31, s23),
    ];
    let matrix = |nrows: usize| -> Vec<Vec<i64>> {
        (0..nrows).map(|i| routes.iter().map(|r| r[i].rem_euclid(P)).collect()).collect()
    };
    let r0 = rank(matrix(1));
    let r1 = rank(matrix(4));
    let r2 = rank(matrix(10));
    let first_minor_rank = rank(matrix(6));
    assert_eq!((r0, r1, r2), (1, 4, 6));
    assert_eq!(first_minor_rank, 6);

    // On a=b, routes 2 and 3 coincide under every X derivative.  The normal
    // edge direction d/da-d/db separates them.
    let ab = 7;
    let dg12 = Linear { value: 10 + ab, grad: [1,1,1], ygrad: [1,0,0] };
    let dg23 = Linear { value: 10 + ab, grad: [1,1,1], ygrad: [0,1,0] };
    let dg31 = Linear { value: 10 + 13, grad: [1,1,1], ygrad: [0,0,1] };
    let ds23 = Linear { value: 3 + 5 + ab + 13, grad: [0,1,1], ygrad: [1,0,1] };
    let ds31 = Linear { value: 5 + 2 + ab + ab, grad: [1,0,1], ygrad: [1,1,0] };
    let ds12 = Linear { value: 2 + 3 + ab + 13, grad: [1,1,0], ygrad: [0,1,1] };
    let diagonal_pairs = [(dg12,ds23),(dg12,ds31),(dg23,ds31),(dg23,ds12),(dg31,ds12),(dg31,ds23)];
    let diagonal_routes = diagonal_pairs.map(|(x,y)| route_jet(x,y));
    let mut diagonal_matrix = (0..10).map(|i| diagonal_routes.iter().map(|r| r[i].rem_euclid(P)).collect::<Vec<_>>()).collect::<Vec<_>>();
    let diagonal_rank = rank(diagonal_matrix.clone());
    let normal_row = diagonal_pairs.map(|(x,y)| route_normal(x,y,[1,-1,0]).rem_euclid(P)).to_vec();
    diagonal_matrix.push(normal_row);
    let recovered_rank = rank(diagonal_matrix);
    assert_eq!((diagonal_rank,recovered_rank),(5,6));

    println!("{{\"status\":\"pass\",\"source\":\"arXiv:2408.16386 eq. (4.15)\",\"routes\":6,\"score_ranks\":{{\"order0\":1,\"through_order1\":4,\"through_order2\":6}},\"certifying_rows\":[\"1\",\"dX1\",\"dX2\",\"dX3\",\"dX1dX1\",\"dX1dX2\"],\"first_score_blind_rank\":2,\"second_score_blind_rank\":0,\"a_equals_b\":{{\"external_score_rank\":5,\"kernel\":\"route2-route3\",\"with_edge_normal_score_rank\":6}},\"classification\":\"generic scalar route packet is contextually faithful through second external-energy score; edge coincidence requires its normal loop-edge port\"}}");
}
