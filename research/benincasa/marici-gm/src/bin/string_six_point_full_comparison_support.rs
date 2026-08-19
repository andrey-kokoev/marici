use serde_json::json;

fn main(){
    let branch_valuation=12;
    let dense_valuation=18;
    let dense_factors=[
      ("x2",2),("x3",2),("x4",2),("y23",2),("y24",2),("y34",2),
      ("y23*y24*y34",1),("x2*x3*y23",1),("x2*x4*y24",1),
      ("x3*x4*y34",1),("x2*x3*x4*y23*y24*y34",2)
    ];
    assert_eq!(dense_factors.iter().map(|(_,v)|v).sum::<i32>(),dense_valuation);
    assert_eq!(dense_valuation-branch_valuation,6);
    let packet=json!({
      "schema":"marici.benincasa.string_six_point_full_comparison_support.v1",
      "branch_fitting_total_valuation":branch_valuation,
      "full_dense_kernel_total_valuation":dense_valuation,
      "additional_full_comparison_valuation":6,
      "dense_factors":dense_factors.iter().map(|(f,v)|json!({"channel_monomial":f,"valuation":v,"factor_type":"M-M^-1"})).collect::<Vec<_>>(),
      "all_additional_support_is_existing_source_channel_sine_support":true,
      "branch_minor_determines_full_comparison_determinant":false,
      "new_carrier_divisor":false,
      "source_certificate":"string-six-point-dense-momentum-kernel.json"
    });
    let text=serde_json::to_string_pretty(&packet).unwrap()+"\n";
    std::fs::write("../string-six-point-full-comparison-support.json",&text).unwrap();print!("{text}");
}
