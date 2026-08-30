use serde_json::{json, Value};
use std::{collections::BTreeMap, f64::consts::PI, fs};

fn gauss_legendre(n: usize) -> Vec<(f64, f64)> {
    let mut rows = Vec::with_capacity(n);
    for i in 0..n {
        let mut x = (PI * (i as f64 + 0.75) / (n as f64 + 0.5)).cos();
        for _ in 0..40 {
            let mut p0 = 1.0;
            let mut p1 = x;
            for k in 2..=n {
                let p2 = ((2*k-1) as f64*x*p1-(k-1) as f64*p0)/k as f64;
                p0=p1; p1=p2;
            }
            let derivative=n as f64*(x*p1-p0)/(x*x-1.0);
            let delta=p1/derivative;
            x-=delta;
            if delta.abs()<1e-15 {break;}
        }
        let mut p0=1.0; let mut p1=x;
        for k in 2..=n {
            let p2=((2*k-1) as f64*x*p1-(k-1) as f64*p0)/k as f64;
            p0=p1; p1=p2;
        }
        let derivative=n as f64*(x*p1-p0)/(x*x-1.0);
        rows.push((x,2.0/((1.0-x*x)*derivative*derivative)));
    }
    rows
}

fn evaluate_profiles(profiles:&BTreeMap<Vec<usize>,usize>,cycle_size:usize,n:usize)->f64 {
    gauss_legendre(n).into_iter().map(|(node,weight)| {
        let x=(node+1.0)/2.0;
        let r=x/(1.0-x);
        let jacobian=0.5/(1.0-x).powi(2);
        let term_sum=profiles.iter().map(|(profile,count)| {
            let selected=profile.iter().map(|size| *size as f64+2.0*r).product::<f64>();
            *count as f64/selected
        }).sum::<f64>();
        weight*jacobian*4.0*PI*r*r*term_sum/
            (cycle_size as f64*(1.0+2.0*r).powi(cycle_size as i32))
    }).sum::<f64>()
}

fn main() {
    let source: Value=serde_json::from_str(
        &fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()
    ).unwrap();
    let terms=source["five_cycle"]["terms"].as_array().unwrap();
    let mut profiles=BTreeMap::<Vec<usize>,usize>::new();
    for term in terms {
        let mut profile=term.as_array().unwrap().iter().map(|label| {
            let label=label.as_str().unwrap();
            label.strip_prefix("g_").map(str::len).unwrap_or_else(|| {
                assert!(label.starts_with("G_minus_e"));
                5
            })
        }).collect::<Vec<_>>();
        profile.sort_unstable();
        *profiles.entry(profile).or_default()+=1;
    }
    assert_eq!(profiles.values().sum::<usize>(),180);

    let orders=[64_usize,128,256,512];
    let estimates=orders.into_iter().map(|n|json!({"order":n,"value":evaluate_profiles(&profiles,5,n)})).collect::<Vec<_>>();
    let packet=json!({
        "schema":"marici.benincasa.five_site.asymmetric.infinity_constant.v1",
        "identity":"lim_{z->infinity} z^7 Pi(z) = 4*pi integral_0^infinity r^2 Omega_infinity(r) dr",
        "profile_counts":profiles.into_iter().map(|(profile,count)|json!({"sizes":profile,"count":count})).collect::<Vec<_>>(),
        "estimates":estimates,
        "status":"deterministic one-dimensional quadrature of the exact coalesced-focus integrand"
    });
    fs::write("../results/five-site-asymmetric-infinity-constant.json",
        serde_json::to_string_pretty(&packet).unwrap()+"\n").unwrap();

    let source6:Value=serde_json::from_str(
        &fs::read_to_string("../results/six-cycle-ofpt-packet.json").unwrap()
    ).unwrap();
    let mut profiles6=BTreeMap::<Vec<usize>,usize>::new();
    for term in source6["six_cycle"]["terms"].as_array().unwrap() {
        let mut profile=term.as_array().unwrap().iter().map(|label|{
            let label=label.as_str().unwrap();
            label.strip_prefix("g_").map(str::len).unwrap_or(6)
        }).collect::<Vec<_>>();
        profile.sort_unstable();
        *profiles6.entry(profile).or_default()+=1;
    }
    let estimates6=orders.into_iter().map(|n|json!({"order":n,"value":evaluate_profiles(&profiles6,6,n)})).collect::<Vec<_>>();
    let packet6=json!({
        "schema":"marici.benincasa.six_site.asymmetric.infinity_constant.v1",
        "profile_counts":profiles6.into_iter().map(|(profile,count)|json!({"sizes":profile,"count":count})).collect::<Vec<_>>(),
        "estimates":estimates6,
        "status":"independent deterministic quadrature of the source-derived six-cycle radial integral"
    });
    fs::write("../results/six-site-asymmetric-infinity-constant.json",serde_json::to_string_pretty(&packet6).unwrap()+"\n").unwrap();
    println!("{}",serde_json::to_string(&packet["estimates"]).unwrap());
}
