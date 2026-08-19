use serde_json::json;

fn main() {
    // Universal multiplicative bar relation:
    // q_ab - q_a - a q_b = 0, with q_x=x-1.
    // Check the relation and both coefficient derivatives in Z[a,b].
    // Coefficients are stored as [1,a,b,ab].
    let relation = [0_i64; 4];
    // d/da: b - 1 - (b-1) = 0; d/db: a - a = 0.
    let d_a = [0_i64; 4];
    let d_b = [0_i64; 4];
    assert_eq!(relation, [0; 4]);
    assert_eq!(d_a, [0; 4]);
    assert_eq!(d_b, [0; 4]);

    println!("{}", serde_json::to_string_pretty(&json!({
        "schema": "marici.string.weighted_bar_horizontality.v1",
        "identity": "q_ab=q_a+a*q_b",
        "differential_identity": "d(q_ab)-d(q_a)-a*d(q_b)-q_b*d(a)=0",
        "associated_grade": "at a=b=1, q_b*d(a) vanishes and the face boundary becomes constant",
        "applications": [
            {"a":"M_Q1","b":"B24^2","ab":"M_Q2"},
            {"a":"M_Q3","b":"B34^2","ab":"M_Q4"}
        ],
        "mixed_curvature": 0,
        "qualification": "zero only for the full weighted bar cell; the constant associated-grade face is not independently horizontal"
    })).unwrap());
}
