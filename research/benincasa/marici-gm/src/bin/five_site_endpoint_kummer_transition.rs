use serde_json::json;
use std::fs;

fn main() {
    let packet = json!({
        "schema":"marici.benincasa.five_site.endpoint_kummer_transition.v1",
        "finite_period_frame":"p0=2*pi*i/sqrt(K4)",
        "infinity_period_frame":"pinf=2*pi*i/sqrt(K0)",
        "transition":"p0=sqrt(K0/K4)*pinf",
        "transition_square":"K0/K4",
        "kummer_divisor":"[K0=0]-[K4=0] modulo 2",
        "inertia_K0":-1,
        "inertia_K4":-1,
        "combined_loop_inertia":1,
        "orientation_dependence":"a common sign rescales both frames and does not change the Kummer line",
        "physical_chain_activation":"not determined",
        "new_carrier_datum":false
    });
    fs::write("../results/five-site-endpoint-kummer-transition.json",
              serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet).unwrap());
}
