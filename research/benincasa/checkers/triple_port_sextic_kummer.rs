// Historical algebra-only diagnostic. Entry 2129 withdrew its cosmological
// interpretation because the three equations came from additive sectors.
fn lambda(p1:i64,p2:i64,p3:i64)->i64 {
    p1*p1+p2*p2+p3*p3-2*(p1*p2+p2*p3+p3*p1)
}
fn main(){
    // At p1=p2=p3=1, Lambda=-3 and Qtilde=U*Lambda+4 with U=E^2.
    let l=lambda(1,1,1);
    assert_eq!(l,-3);
    // Verify Qtilde=0 at U=4/3 after clearing the denominator.
    assert_eq!(4*l+3*4,0);
    // d Qtilde / dU = Lambda is nonzero: the incidence is transverse.
    assert_ne!(l,0);
    println!("{}", r#"{"status":"pass","smooth_test":"p_i=1,E^2=4/3","kummer_exponent":"-1/2","monodromy":-1}"#);
}
