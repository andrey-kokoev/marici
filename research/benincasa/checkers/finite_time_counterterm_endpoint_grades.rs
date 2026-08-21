#[derive(Clone,Copy)]struct Operator{label:&'static str,scale_power:i32,field_power:i32,frequency:i32}
fn endpoint_grade(o:Operator)->i32{
    // For nonzero frequency, integration by parts preserves the maximal
    // Laurent power. All quadratic counterterm commutators have ±2p.
    assert_ne!(o.frequency,0);o.scale_power+o.field_power
}
fn main(){
    // c1: a^2 (zeta')^2; each differentiated mode is proportional to eta.
    // c2: a^2 p^2 zeta^2; an undifferentiated mode has maximal power one.
    // c3: p^4 zeta^2 with no conformal scale factor.
    let ops=[
        Operator{label:"c1",scale_power:-2,field_power:2,frequency:2},
        Operator{label:"c2",scale_power:-2,field_power:2,frequency:2},
        Operator{label:"c3",scale_power:0,field_power:2,frequency:2},
    ];
    let grades:Vec<_>=ops.iter().map(|&o|(o.label,endpoint_grade(o))).collect();
    assert_eq!(grades,vec![("c1",0),("c2",0),("c3",2)]);
    println!("{{");
    println!("  \"schema\": \"marici.finite_time_counterterm_endpoint_grades.v1\",");
    println!("  \"max_endpoint_grades\": {{\"c1\": 0, \"c2\": 0, \"c3\": 2}},");
    println!("  \"eta0_squared_zero_frequency_support\": false,");
    println!("  \"eta0_squared_oscillatory_support\": [\"c3:-2p\", \"c3:+2p\"],");
    println!("  \"labels_use_entry_1536_correction\": true");
    println!("}}");
}
