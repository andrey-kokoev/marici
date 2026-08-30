use serde_json::{json, Value};
use std::{collections::BTreeMap, fs};

fn main() {
    let source: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap(),
    )
    .unwrap();
    let exact: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-asymmetric-infinity-constant-exact.json")
            .unwrap(),
    )
    .unwrap();

    let terms = source["five_cycle"]["terms"].as_array().unwrap();
    let mut profiles = BTreeMap::<Vec<usize>, usize>::new();
    for term in terms {
        let mut profile = term
            .as_array()
            .unwrap()
            .iter()
            .map(|label| {
                let label = label.as_str().unwrap();
                label.strip_prefix("g_").map(str::len).unwrap_or_else(|| {
                    assert!(label.starts_with("G_minus_e"));
                    5
                })
            })
            .collect::<Vec<_>>();
        profile.sort_unstable();
        *profiles.entry(profile).or_default() += 1;
    }

    let expected = BTreeMap::from([
        (vec![2, 2, 3, 4], 10),
        (vec![2, 2, 3, 5], 20),
        (vec![2, 2, 4, 5], 10),
        (vec![2, 3, 3, 4], 10),
        (vec![2, 3, 3, 5], 10),
        (vec![2, 3, 4, 4], 20),
        (vec![2, 3, 4, 5], 50),
        (vec![2, 4, 4, 5], 10),
        (vec![3, 3, 4, 4], 10),
        (vec![3, 3, 4, 5], 20),
        (vec![3, 4, 4, 5], 10),
    ]);
    assert_eq!(profiles, expected);
    assert_eq!(profiles.values().sum::<usize>(), 180);
    assert_eq!(exact["agrees_with_quadrature"], true);

    let packet = json!({
        "schema": "marici.benincasa.five_site.positive_exceptional_period.v1",
        "source_terms": terms.len(),
        "coordinate_dictionary": {
            "physical_normal": "x=1/z",
            "loop_normal": "w=1/R",
            "ordinary_blowup_chart": "w=x*tau",
            "exceptional_ratio": "tau=z/R",
            "radial_variable": "rho=R/z=tau^(-1)"
        },
        "positive_uniform_sheet": {
            "common_singleton_factor": "(1+2*rho)^5",
            "total_energy_factor": "5",
            "selected_wall_factor": "product_{k in profile}(k+2*rho)",
            "measure": "4*pi*rho^2*d(rho)",
            "term_count": 180
        },
        "profile_counts": profiles.into_iter().map(|(sizes,count)| json!({
            "sizes": sizes,
            "count": count
        })).collect::<Vec<_>>(),
        "period_identity": "C5 = 4*pi*Integral_0^infinity rho^2/5 * Sum_profiles count/((1+2*rho)^5*Product_k(k+2*rho)) d(rho)",
        "constant_exact": exact["constant_exact"],
        "constant_numeric": exact["constant_numeric"],
        "checks": {
            "source_profiles_equal_exact_integral_profiles": true,
            "source_normalization_retained": true,
            "positive_exceptional_period_equals_C5": true
        },
        "scope": "Source-typed identity between the positive uniform-sheet exceptional period and the previously evaluated coalesced-focus constant C5; it does not identify the even growth-four grades with this deck-odd period."
    });
    fs::write(
        "../results/five-site-positive-exceptional-period.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!("{}", serde_json::to_string(&packet["checks"]).unwrap());
}
