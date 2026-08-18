//! Type the two local resonant blocks over S=Q[z], R=S/(z^2).
//!
//! The even relation cell is Tor_1^S(R,R)=R.  The odd matrix
//! factorization has cokernel R/(z).  Their Cartier lengths are 2 and 1.

fn rank(matrix: &[Vec<i64>]) -> usize {
    let mut a: Vec<Vec<f64>> = matrix.iter().map(|r| r.iter().map(|&x| x as f64).collect()).collect();
    let rows = a.len();
    let cols = a.first().map_or(0, Vec::len);
    let mut pivot = 0;
    for col in 0..cols {
        let Some(row) = (pivot..rows).find(|&r| a[r][col].abs() > 1e-9) else { continue };
        a.swap(pivot, row);
        let d = a[pivot][col];
        for j in col..cols { a[pivot][j] /= d; }
        for i in 0..rows {
            if i != pivot {
                let q = a[i][col];
                for j in col..cols { a[i][j] -= q * a[pivot][j]; }
            }
        }
        pivot += 1;
    }
    pivot
}

fn main() {
    // Multiplication by z^2 becomes zero after tensoring the Koszul
    // resolution [S --z^2--> S] with R.
    let even_base_changed_differential = vec![vec![0, 0], vec![0, 0]];
    let even_tor_dimension = 2 - rank(&even_base_changed_differential);
    assert_eq!(even_tor_dimension, 2);

    // Multiplication by z on R, basis (1,z), sends 1->z and z->0.
    let odd_differential = vec![vec![0, 0], vec![1, 0]];
    let odd_cokernel_dimension = 2 - rank(&odd_differential);
    assert_eq!(odd_cokernel_dimension, 1);

    // The odd complementary map -z/6 has the same rank; compositions
    // recover z^2 over S and vanish only after passage to R.
    assert_eq!(rank(&odd_differential), 1);
    assert_eq!(even_tor_dimension + odd_cokernel_dimension, 3);

    println!(
        "{{\"ambient_ring\":\"S=Q[z]\",\"carrier_ring\":\"R=S/(z^2)\",\"even_object\":\"Tor_1^S(R,R)=I/I^2 congruent R\",\"even_cartier_length\":{},\"odd_object\":\"coker(z:R->R)=R/(z)\",\"odd_cartier_length\":{},\"total_local_length\":3,\"reduced_rank\":2,\"singularity_category_alone_sufficient\":false,\"global_quartic_tail_transport\":\"NOT_YET_COMPUTED\"}}",
        even_tor_dimension, odd_cokernel_dimension
    );
}
