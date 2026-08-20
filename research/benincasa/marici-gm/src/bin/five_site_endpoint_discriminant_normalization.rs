use serde_json::json;
use std::fs;

fn rank(mut a: Vec<Vec<i64>>) -> usize {
    let rows = a.len();
    let cols = a.first().map_or(0, |r| r.len());
    let mut r = 0;
    for c in 0..cols {
        let Some(p) = (r..rows).find(|&i| a[i][c] != 0) else { continue };
        a.swap(r, p);
        let pivot = a[r][c];
        for i in 0..rows {
            if i == r || a[i][c] == 0 { continue; }
            let q = a[i][c];
            for j in c..cols { a[i][j] = pivot*a[i][j]-q*a[r][j]; }
            let g = a[i].iter().fold(0_i64, |g, x| gcd(g, x.abs()));
            if g > 1 { for x in &mut a[i] { *x /= g; } }
        }
        r += 1;
        if r == rows { break; }
    }
    r
}

fn gcd(mut a: i64, mut b: i64) -> i64 {
    while b != 0 { let t = a % b; a = b; b = t; }
    a.abs()
}

fn main() {
    // R=Q[k,d]/(d^2-k^2) embeds in its normalization
    // N=Q[k] plus Q[k] by f(k,d) -> (f(k,k),f(k,-k)).
    // At cutoff D, use component bases (k^0,...,k^D) on both sheets.
    let mut census = Vec::new();
    for d in [2_usize, 4, 8, 16, 32] {
        let ncols = 2*(d+1);
        let mut generators = Vec::new();
        for degree in 0..=d {
            let mut v = vec![0_i64; ncols];
            v[degree] = 1;
            v[d+1+degree] = 1;
            generators.push(v); // k^degree -> diagonal
        }
        for degree in 1..=d {
            let mut v = vec![0_i64; ncols];
            v[degree] = 1;
            v[d+1+degree] = -1;
            generators.push(v); // d*k^(degree-1) -> anti-diagonal
        }
        let image_rank = rank(generators);
        assert_eq!(image_rank, 2*d+1);
        assert_eq!(ncols-image_rank, 1);
        census.push(json!({"cutoff":d,"normalization_rank":ncols,
                           "source_image_rank":image_rank,"cokernel_rank":1}));
    }
    let packet = json!({
        "schema":"marici.benincasa.five_site.endpoint_discriminant_normalization.v1",
        "endpoint_cover":"R=Q[K2,delta]/(delta^2-K2^2)",
        "normalization":"N=Q[K2] direct_sum Q[K2]",
        "normalization_map":"f(K2,delta) -> (f(K2,K2),f(K2,-K2))",
        "conductor":"K2*N",
        "normalization_cokernel":"N/R = Q supported at K2=0",
        "deck_action_on_cokernel":-1,
        "canonical_generator_type":"anti-diagonal sheet difference; no affine sign choice",
        "finite_and_infinity_endpoint_models":"identical after K0<->K4 and z<->w",
        "cutoff_census":census,
        "physical_chain_map_derived":false,
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-endpoint-discriminant-normalization.json",
              serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
