fn discriminant(bulk:f64,mixed:f64,surface:f64)->f64{mixed*mixed-4.*bulk*surface}
fn main(){
    // Symmetric sewing of two labelled three-point vertices. Signs and
    // vertex normalizations may be absorbed into V and W; the rank-one
    // binomial discriminant remains zero.
    let direct=(1.,2.,1.);
    let printed=(1.,4.,2.);
    let direct_disc=discriminant(direct.0,direct.1,direct.2);
    let printed_disc=discriminant(printed.0,printed.1,printed.2);
    assert_eq!(direct_disc,0.);
    assert_eq!(printed_disc,8.);
    // Independent vertex rescaling preserves vanishing of the discriminant.
    for (v,w) in [(2.,3.),(-1.5,0.7),(5.,-2.)]{
        assert!((discriminant(v*v,2.*v*w,w*w)).abs()<1e-14);
    }
    println!("{{");
    println!("  \"schema\": \"marici.three_point_kernel_sewing_discriminant.v1\",");
    println!("  \"direct_location_coefficients\": [1, 2, 1],");
    println!("  \"direct_discriminant\": {},",direct_disc);
    println!("  \"eq19_required_location_coefficients\": [1, 4, 2],");
    println!("  \"eq19_discriminant\": {},",printed_disc);
    println!("  \"eq19_is_rank_one_vertex_sewing\": false");
    println!("}}");
}
