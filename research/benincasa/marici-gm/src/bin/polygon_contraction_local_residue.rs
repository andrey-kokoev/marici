use serde_json::json;
use std::fs;

fn main(){
    // On y_(n,1)=0 use q=q_{n,1}, s=q_1 and t=q_n=q-s.
    // The orientation is ds wedge dq. Near s=0 it is
    // (ds/s) wedge dq/(q-s), so Res_s=+dq/q.
    let residue_s=1_i32;

    // Near t=0, ds=dq-dt and therefore
    // ds wedge dq = -dt wedge dq. Hence Res_t=-dq/q.
    let jacobian_ds_dq_to_dt_dq=-1_i32;
    let residue_t=jacobian_ds_dq_to_dt_dq;
    assert_eq!(residue_s,1);
    assert_eq!(residue_t,-1);
    assert_eq!(residue_s+residue_t,0);
    assert_eq!(residue_s-residue_t,2);

    let packet=json!({
        "schema":"marici.benincasa.polygon_contraction_local_residue.v1",
        "coordinates":{
            "merged_wall":"q=q_{n,1}",
            "first_occurrence":"s=q_1",
            "second_occurrence":"t=q_n=q-s",
            "orientation":"ds wedge dq"
        },
        "form":"ds wedge dq / (s*(q-s))",
        "endpoint_residues":{
            "s_zero":"+dq/q",
            "t_zero":"-dq/q"
        },
        "combinations":{
            "unoriented_sum":0,
            "oriented_difference":2,
            "one_sided_residue":1
        },
        "conclusion":{
            "one_sided_target_map":true,
            "exchange_symmetric_integral_unit_map":false,
            "occurrence_oriented_map_has_factor_two":true,
            "required_extra_datum":"choose one occurrence or supply an independently normalized trace/counit allowing division by two"
        },
        "scope":"Local logarithmic Poincare-residue calculation on the contracted-edge divisor; it does not choose the physical contraction counit."
    });
    fs::write("../results/polygon-contraction-local-residue.json",serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet["conclusion"]).unwrap());
}
