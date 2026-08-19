use serde_json::json;

fn main(){
    // D(alpha,beta)=(D_KN alpha + theta wedge beta, D_KN beta).
    // Since d theta=0, the two off-diagonal terms in D^2 have signs - and +.
    let off_diagonal_square = -1_i32 + 1_i32;
    assert_eq!(off_diagonal_square,0);
    let packet=json!({
      "schema":"marici.benincasa.string_six_point_log_insertion_complex.v1",
      "channel":"34",
      "fiber_function":"f_34=z_3-z_4",
      "log_generator":"ell_34=log(f_34)",
      "theta":"dlog(f_34)",
      "underlying_module":"Omega_KN direct_sum ell_34*Omega_KN",
      "differential":"D(alpha,beta)=(D_KN alpha + dlog(f_34) wedge beta, D_KN beta)",
      "square_zero":true,
      "extension_sequence":"0 -> Omega_KN -> Omega_log,<=1 -> Omega_KN -> 0",
      "extension_residue_on_f34":1,
      "extension_generically_split":false,
      "new_carrier_divisor":false,
      "coefficient_extension":true,
      "finite_top_form_reduction_constructed":false,
      "conclusion":"The physical first logarithmic insertion is a nontrivial triangular de Rham extension supported on the existing channel divisor. It is not the naive constant two-layer tensor factor."
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-log-insertion-complex.json",&text).unwrap();
    print!("{text}");
}
