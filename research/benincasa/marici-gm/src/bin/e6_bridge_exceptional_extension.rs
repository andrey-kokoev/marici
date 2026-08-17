#[derive(Clone, Copy)]
struct Point {
    chart: &'static str,
    name: &'static str,
    a: i64,
    b: i64,
}

fn main() {
    // The frozen marked-extension column is e6/[8(x+y)].  Under the
    // radial blowup, x+y is the exceptional parameter times the listed
    // strict transform in each standard chart.
    let chart_factors = [("E", "u*(r+s)"), ("x", "u*(1+s)"), ("y", "u*(1+s)")];
    assert_eq!(chart_factors.len(), 3);

    // Four base points of A/B.  Choose the x-chart when x != 0 and the
    // y-chart otherwise.  The pair (a,b) records the affine coordinates;
    // the strict factor is 1+b in both chosen charts.
    let base_points = [
        Point {
            chart: "x",
            name: "[0:1:0]",
            a: 0,
            b: 0,
        },
        Point {
            chart: "y",
            name: "[0:0:1]",
            a: 0,
            b: 0,
        },
        Point {
            chart: "x",
            name: "[2:1:0]",
            a: 2,
            b: 0,
        },
        Point {
            chart: "y",
            name: "[2:0:1]",
            a: 2,
            b: 0,
        },
    ];
    for p in base_points {
        assert!(matches!(p.chart, "x" | "y"));
        assert_eq!(1 + p.b, 1, "unexpected x+y pole at {}", p.name);
        let _ = p.a;
    }

    // In the E-chart the four finite conductor--energy tangencies have
    // r+s = 3/2, 3/2, 1/2, 1/2.  Clear the common denominator two.
    let tangencies_twice = [(1, 2), (2, 1), (3, -2), (-2, 3)];
    let strict_sums: Vec<i64> = tangencies_twice
        .iter()
        .map(|(two_r, two_s)| two_r + two_s)
        .collect();
    assert_eq!(strict_sums, vec![3, 3, 1, 1]);
    assert!(strict_sums.iter().all(|v| *v != 0));

    println!("{{");
    println!("  \"schema\": \"marici.benincasa.e6_bridge_exceptional_extension.v1\",");
    println!("  \"frozen_bridge\": \"g111_top -> e6/(8*(x+y))\",");
    println!("  \"invariant_line\": \"<e6>\",");
    println!("  \"chart_denominators\": {{\"E\":\"8*u*(r+s)\",\"x\":\"8*u*(1+s)\",\"y\":\"8*u*(1+s)\"}},");
    println!("  \"required_cartier_support\": [\"radial exceptional divisor u=0\",\"strict transform of x+y=0\"],");
    println!("  \"modulus_base_point_strict_factors\": [1,1,1,1],");
    println!("  \"twice_tangency_strict_factors\": [3,3,1,1],");
    println!("  \"new_pole_at_entry_370_centers\": false,");
    println!("  \"bridge_line_lost_at_entry_370_centers\": false,");
    println!("  \"new_carrier_datum\": false,");
    println!("  \"scope\": \"e6 line and its marked top-column bridge only; not the full rank-twelve connection\"");
    println!("}}");
}
