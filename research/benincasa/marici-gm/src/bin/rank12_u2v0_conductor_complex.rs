// Generic normalization/conductor descent for Entry 1100.
// Basis of normalization sheets: (e_plus,e_minus); conductor basis: c.
// Poincare-residue orientation fixes d=(1,-1).  Deck swaps the sheets and
// acts by -1 on c, making d equivariant.

fn main() {
    let d = [1_i64, -1];
    let tau_n = [[0_i64, 1], [1, 0]];
    let tau_c = -1_i64;

    // Equivariance d*tau_N=tau_C*d.
    let d_tau = [
        d[0] * tau_n[0][0] + d[1] * tau_n[1][0],
        d[0] * tau_n[0][1] + d[1] * tau_n[1][1],
    ];
    assert_eq!(d_tau, [tau_c * d[0], tau_c * d[1]]);

    let invariant = [1_i64, 1];
    let anti_invariant = [1_i64, -1];
    let image = |v: [i64; 2]| d[0] * v[0] + d[1] * v[1];
    assert_eq!(image(invariant), 0);
    assert_eq!(image(anti_invariant), 2);

    // Over characteristic zero, multiplication by two is invertible.
    let normalization_rank = 2;
    let conductor_rank = 1;
    let differential_rank = 1;
    let kernel_rank = normalization_rank - differential_rank;
    let cokernel_rank = conductor_rank - differential_rank;
    let anti_invariant_homology_rank = 0;

    println!("normalization_basis=(e_plus,e_minus)");
    println!("conductor_basis=c");
    println!("difference_map=[1,-1]");
    println!("deck_on_normalization=[[0,1],[1,0]]");
    println!("deck_on_conductor=-1");
    println!("equivariant=true");
    println!("invariant_kernel_generator=(1,1)");
    println!("anti_invariant_map=2");
    println!("kernel_rank={kernel_rank}");
    println!("cokernel_rank={cokernel_rank}");
    println!("anti_invariant_homology_rank={anti_invariant_homology_rank}");
    println!("valid_locus=s*(B-1)!=0");
}
