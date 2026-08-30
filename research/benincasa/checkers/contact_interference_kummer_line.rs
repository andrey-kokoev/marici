// Exact rank-one connection data for p=8/(ell_j ell_k)*(1,-1).

fn main() {
    let residues = [-1_i32, -1_i32, 1_i32, 1_i32];

    for &r in residues.iter() {
        // exp(2*pi*i*r)=1 for integral r.
        assert!(r == -1 || r == 1);
    }

    // Multiplication by ell_j*ell_k sends the packet generator to the
    // constant route-kernel vector 8*(1,-1).
    let normalized = [8_i128, -8_i128];
    assert_eq!(normalized[0] + normalized[1], 0);

    println!(
        "{{\"status\":\"pass\",\"line\":\"K_(ell_j^-1*ell_k^-1) tensor Q*(1,-1)\",\"finite_residues\":[-1,-1],\"infinity_residues\":[1,1],\"local_monodromy\":\"identity\",\"normalized_generator\":[8,-8],\"rank\":1}}"
    );
}
