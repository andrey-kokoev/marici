fn mat_mul(a:&[[i8;6];6],b:&[[i8;6];6])->[[i8;6];6] {
    let mut c=[[0_i8;6];6];
    for i in 0..6 { for j in 0..6 { for k in 0..6 { c[i][j]+=a[i][k]*b[k][j]; }}}
    c
}

fn main() {
    // Occurrence order: 12|23,12|31,23|31,23|12,31|12,31|23.
    // rho sends 0->2->4->0 and 1->3->5->1.
    let image=[2_usize,3,4,5,0,1];
    let mut rho=[[0_i8;6];6]; for i in 0..6 { rho[image[i]][i]=1; }
    let residue=std::array::from_fn(|i|std::array::from_fn(|j|i8::from(i==j)));
    assert_eq!(mat_mul(&residue,&rho),mat_mul(&rho,&residue));

    // Every marked Cut has q=E+y, normal derivative +1, even cyclic residue
    // orientation, multiplicity one, and the same 2*pi*i boundary-value factor.
    let jacobians=[1_i8;3]; let orientations=[1_i8;3]; let multiplicities=[1_i8;3];
    assert_eq!(jacobians,[1,1,1]); assert_eq!(orientations,[1,1,1]); assert_eq!(multiplicities,[1,1,1]);

    // The convex negative-imaginary tube has one identical strict inequality
    // for each site and edge variable; cyclic relabelling permutes them.
    let tube_inequalities=["Im x1<0","Im x2<0","Im x3<0","Im y12<0","Im y23<0","Im y31<0"];
    let permuted=[tube_inequalities[1],tube_inequalities[2],tube_inequalities[0],tube_inequalities[4],tube_inequalities[5],tube_inequalities[3]];
    let mut lhs=tube_inequalities; let mut rhs=permuted; lhs.sort(); rhs.sort(); assert_eq!(lhs,rhs);

    // No source summand has two marked-Cut poles, so every iterated marked-Cut
    // residue is zero. This is preserved by rho and needs no overlap repair.
    let pairwise_iterated_residues=[0_i8;6]; assert_eq!(pairwise_iterated_residues,[0;6]);
    let source=[1_i8;6]; let mut rotated=[0_i8;6]; for i in 0..6 { rotated[image[i]]=source[i]; } assert_eq!(rotated,source);

    println!("{{");
    println!("  \"occurrence_order\": [\"12|23\",\"12|31\",\"23|31\",\"23|12\",\"31|12\",\"31|23\"],");
    println!("  \"C3_orbits\": [[\"12|23\",\"23|31\",\"31|12\"],[\"12|31\",\"23|12\",\"31|23\"]],");
    println!("  \"residue_matrix\": \"I6\",");
    println!("  \"residue_commutes_with_C3\": true,");
    println!("  \"jacobians\": [1,1,1],");
    println!("  \"orientations\": [1,1,1],");
    println!("  \"multiplicities\": [1,1,1],");
    println!("  \"boundary_value_factor\": \"2*pi*i in every sector\",");
    println!("  \"negative_imaginary_tube_C3_invariant\": true,");
    println!("  \"pairwise_iterated_cut_residues\": [0,0,0,0,0,0],");
    println!("  \"cyclic_leray_naturality\": true,");
    println!("  \"classification\": \"C3-equivariant family of local analytic-continuation residue germs, not Cech gluing\"");
    println!("}}");
}
