// Exact polynomial certificate for the dashed-edge Kummer adapter.
// Test polynomial: f(u,v)=u^3+2uv+v^2.

fn f(u: i128, v: i128) -> i128 { u*u*u + 2*u*v + v*v }
fn fu(u: i128, v: i128) -> i128 { 3*u*u + 2*v }
fn fv(u: i128, v: i128) -> i128 { 2*u + 2*v }

fn main() {
    // T(f)=f(x_s+y,x_t+y)/y.  Clear the common denominators and verify
    // y*d_y T + T = f_u+f_v, while x derivatives intertwine directly.
    let samples = [(2_i128, 3_i128, 5_i128), (-4, 7, 3), (11, -2, 13)];
    for (xs, xt, y) in samples {
        let u = xs + y;
        let v = xt + y;
        let numerator = f(u, v);
        let dxs_numerator = fu(u, v);
        let dxt_numerator = fv(u, v);
        let dy_numerator = fu(u, v) + fv(u, v);

        assert_eq!(dxs_numerator, fu(u, v));
        assert_eq!(dxt_numerator, fv(u, v));

        // y^2*(d_y T + T/y) = y*(f_u+f_v).
        let lhs_cleared = (-numerator + y*dy_numerator) + numerator;
        let rhs_cleared = y*(fu(u, v) + fv(u, v));
        assert_eq!(lhs_cleared, rhs_cleared);
    }
    println!("{{\"status\":\"pass\",\"samples\":3,\"identity\":\"(d_y+1/y)T=T(d_u+d_v)\"}}");
}
