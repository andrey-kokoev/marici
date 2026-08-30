use serde_json::json;
use std::fs;

fn main() {
    // The full labelled q_i Gram matrix is the symmetric C8 circulant with
    // first row (2,3/2,1/2,k,l,k,1/2,3/2).  Its real Fourier eigenvalues are
    // lambda_m = 2 + 3 cos(pi m/4) + cos(pi m/2)
    //            + 2 k cos(3 pi m/4) + l (-1)^m.
    // Only lambda_3 and lambda_4 are needed below.

    // Family A: 2k-3=0.  Then lambda_3=2-l and lambda_4=l-3,
    // whose sum is -1.  They cannot both be nonnegative.
    let family_a_sum = -1i64;
    assert!(family_a_sum < 0);

    // Family B: 7+6k-8l=0.  Positivity of the already frozen cumulative
    // four-route principal Gram requires
    //   -k(6+7k)/4 >= 0, hence -6/7 <= k <= 0.
    // On the divisor, 8 sqrt(2) lambda_3 equals
    //   f(k) = (9-6k)sqrt(2) + 8(2k-3).
    // Its slope is 16-6sqrt(2)>0, so on k<=0 it is bounded above by
    // f(0)=9sqrt(2)-24<0.  Both signs are proved by squaring positive
    // quantities: 16^2> (6sqrt2)^2 and 24^2>(9sqrt2)^2.
    let slope_square_gap = 16i64.pow(2) - 2 * 6i64.pow(2);
    let endpoint_square_gap = 24i64.pow(2) - 2 * 9i64.pow(2);
    assert!(slope_square_gap > 0);
    assert!(endpoint_square_gap > 0);

    let packet = json!({
        "schema":"marici.eight_site_linear_divisor_euclidean_gate.v1",
        "full_routing_gram":{
            "type":"symmetric C8 circulant",
            "first_row":["2","3/2","1/2","k","l","k","1/2","3/2"],
            "physical_requirement":"positive semidefinite on the real Euclidean Cayley-Menger routing chain",
            "eigenvalues_used":{
                "lambda_3":"2+(2*k-3)/sqrt(2)-l",
                "lambda_4":"l-2*k"
            },
            "cumulative_four_route_determinant":"-1/4*k*(6+7*k)"
        },
        "family_2k_minus_3":{
            "orbit_count":21,
            "specialization":{"lambda_3":"2-l","lambda_4":"l-3","sum":"-1"},
            "psd_contradiction":"lambda_3 and lambda_4 cannot both be nonnegative",
            "real_euclidean_routing_support":"empty"
        },
        "family_7_plus_6k_minus_8l":{
            "orbit_count":15,
            "specialization":"l=(7+6*k)/8",
            "necessary_cumulative_gram_interval":"-6/7 <= k <= 0",
            "scaled_lambda_3":"8*sqrt(2)*lambda_3=(9-6*k)*sqrt(2)+8*(2*k-3)",
            "monotonicity_certificate":{"slope":"16-6*sqrt(2)>0","squared_gap":slope_square_gap},
            "endpoint_certificate":{"at_k_0":"9*sqrt(2)-24<0","squared_gap":endpoint_square_gap},
            "conclusion":"lambda_3<0 throughout the necessary cumulative-Gram interval",
            "real_euclidean_routing_support":"empty"
        },
        "source_continuation_consequence":"a Leray continuation retaining the real Euclidean Cayley-Menger routing chain cannot activate either displayed linear family",
        "ordinary_support_result":"Entry 1910 remains valid after narrowing to ordinary pullback",
        "companion_discriminants":"not decided by this Euclidean linear-factor checker",
        "new_carrier_structure":false,
        "classification":"the two universal linear C8 coefficient divisors are coefficient support outside the real Euclidean physical routing cone",
        "scope":"necessary real Euclidean routing test; complex routing continuation and the 36 companion coefficient discriminants remain open"
    });
    fs::write(
        "../results/eight-site-linear-divisor-euclidean-gate.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"linear_families":2,"orbits":36,"real_euclidean_support":0,"companion_discriminants":"open"})
    );
}
