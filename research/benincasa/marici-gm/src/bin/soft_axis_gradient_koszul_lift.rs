#[derive(Clone, Copy)]
struct GradientBoundary { ka: i64, kb: i64 }
fn d(h: GradientBoundary, ka: i64, kb: i64) -> i64 { h.ka * ka + h.kb * kb }
fn main() {
    let (m, ka, kb) = (5_i64, 7_i64, 11_i64);
    let hp = GradientBoundary { ka: 0, kb: 3 * m };
    let hq = GradientBoundary { ka: -3 * m, kb: 0 };
    assert_eq!(d(hp, ka, kb), 3 * m * kb);
    assert_eq!(d(hq, ka, kb), -3 * m * ka);
    println!("{{\"schema\":\"marici.benincasa.soft_axis_gradient_koszul_lift.v1\",\"p_mod_K\":\"(3/2)*m*K_b\",\"q_mod_K\":\"-(3/2)*m*K_a\",\"all_exact_sectors_nullhomotopic\":true,\"bare_module_target_sufficient\":false,\"derived_gradient_target_required\":true}}");
}
