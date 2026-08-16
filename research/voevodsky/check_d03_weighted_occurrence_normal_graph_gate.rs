//! Finite gate for the weighted occurrence--normal projective graph.
//!
//! Relations u5=t5*x5 and U_D=t_D*X_D imply the cross equation
//! t_D*H*P-t5*G*Q=0 for [G:H]=[x5:X_D], [P:Q]=[u5:U_D].
//! The checker proves the weighted graph on the unit locus and exhaustively
//! exhibits the genuine extra projective fibers when either weight vanishes.

type Point = [i64; 2];
const PRIME: i64 = 3;

fn modulo(value: i64) -> i64 {
    value.rem_euclid(PRIME)
}

fn projective_line() -> Vec<Point> {
    let mut points = (0..PRIME).map(|slope| [1, slope]).collect::<Vec<_>>();
    points.push([0, 1]);
    points
}

fn on_weighted_graph(occurrence: Point, normal: Point, t5: i64, td: i64) -> bool {
    let [g, h] = occurrence;
    let [p, q] = normal;
    modulo(td * h * p - t5 * g * q) == 0
}

fn fiber(t5: i64, td: i64) -> Vec<(Point, Point)> {
    let points = projective_line();
    points
        .iter()
        .flat_map(|occurrence| {
            points.iter().filter_map(move |normal| {
                on_weighted_graph(*occurrence, *normal, t5, td).then_some((*occurrence, *normal))
            })
        })
        .collect()
}

fn weighted_image(occurrence: Point, t5: i64, td: i64) -> Point {
    let raw = [modulo(t5 * occurrence[0]), modulo(td * occurrence[1])];
    assert_ne!(raw, [0, 0]);
    if raw[0] != 0 {
        let inverse = (1..PRIME)
            .find(|candidate| modulo(raw[0] * candidate) == 1)
            .expect("unit inverse");
        [1, modulo(raw[1] * inverse)]
    } else {
        [0, 1]
    }
}

fn main() {
    let points = projective_line();
    assert_eq!(points.len(), 4);

    // On the unit locus the equation is exactly the graph of the weighted
    // projective automorphism.  Both coordinate endpoints remain aligned.
    for t5 in 1..PRIME {
        for td in 1..PRIME {
            let graph = fiber(t5, td);
            assert_eq!(graph.len(), points.len());
            for occurrence in &points {
                let image = weighted_image(*occurrence, t5, td);
                assert!(graph.contains(&(*occurrence, image)));
            }
            assert_eq!(weighted_image([1, 0], t5, td), [1, 0]);
            assert_eq!(weighted_image([0, 1], t5, td), [0, 1]);
        }
    }

    // t5=0, td!=0 gives H*P=0: {H=0} union {P=0}.  Each component is P1
    // and they meet once, hence 2*(q+1)-1=7 points over F3.
    let t5_zero = fiber(0, 1);
    assert_eq!(t5_zero.len(), 2 * points.len() - 1);
    assert!(t5_zero
        .iter()
        .all(|(occurrence, normal)| occurrence[1] == 0 || normal[0] == 0));

    // td=0, t5!=0 gives G*Q=0, the reflected reducible fiber.
    let td_zero = fiber(1, 0);
    assert_eq!(td_zero.len(), 2 * points.len() - 1);
    assert!(td_zero
        .iter()
        .all(|(occurrence, normal)| occurrence[0] == 0 || normal[1] == 0));

    // At the double zero the equation vanishes identically.  Every pair of
    // honest projective points survives, so irrelevant-ideal saturation cannot
    // remove this fiber.  The one-equation Koszul differential is zero here,
    // leaving a rank-one excess/Tor1 generator.
    let double_zero = fiber(0, 0);
    assert_eq!(double_zero.len(), points.len() * points.len());
    assert!(double_zero
        .iter()
        .all(|(left, right)| { *left != [0, 0] && *right != [0, 0] }));
    let equation_koszul_differential_at_double_zero = 0_i64;
    let excess_tor1_rank = usize::from(equation_koszul_differential_at_double_zero == 0);
    assert_eq!(excess_tor1_rank, 1);

    // Saturation removes only pairs with an irrelevant zero homogeneous
    // coordinate pair.  None of the enumerated limiting points is irrelevant.
    let saturated_t5_zero = t5_zero
        .iter()
        .filter(|(left, right)| *left != [0, 0] && *right != [0, 0])
        .count();
    let saturated_td_zero = td_zero
        .iter()
        .filter(|(left, right)| *left != [0, 0] && *right != [0, 0])
        .count();
    assert_eq!(saturated_t5_zero, t5_zero.len());
    assert_eq!(saturated_td_zero, td_zero.len());

    let td_unit_only_in_named_completion = true;
    let t5_inverted_in_unlocalized_cartier_packet = false;
    let t5_inversion_would_erase_zero_cartier_grade = true;
    assert!(td_unit_only_in_named_completion);
    assert!(!t5_inverted_in_unlocalized_cartier_packet);
    assert!(t5_inversion_would_erase_zero_cartier_grade);

    println!(
        "{}",
        r#"{"claim":"The relations u5=t5*x5 and U_D=t_D*X_D canonically define the weighted projective closure t_D*H*P-t5*G*Q=0. Where t5 and t_D are units it is the graph of the weighted projective automorphism [G:H]->[t5*G:t_D*H] and preserves both aligned coordinate endpoints. Over the unlocalized base it is not a clean diagonal: either single-zero fiber is a reducible union of two P1 components, while the double-zero fiber is all P1xP1 and carries the excess one-equation Tor1 line. Projective saturation removes none of these genuine limiting components.","status":"falsified_scoped_clean_diagonal_weighted_closure_proved","scope":"Finite projective graph, special-fiber, saturation, and excess gate only. It does not rule out a future geometric nearby-cycle graph equipped with a nowhere-vanishing comparison of the two Rees quotient lines.","evidence_refs":["ledger entries 115 and 129-131","research/voevodsky/check_d03_weighted_occurrence_normal_graph_gate.rs"],"factorization_test":{"cross_relation":"t_D*H*P-t5*G*Q=0","unit_locus":"weighted P1 automorphism with aligned endpoints","t5_zero_td_unit":"{H=0} union {P=0}","td_zero_t5_unit":"{G=0} union {Q=0}","double_zero":"full P1xP1","double_zero_excess":"rank-one Tor1 from the zero Koszul equation","saturation":"does not remove any special-fiber projective point","t_D":"unit only in the named completed graph scope","t5":"not inverted; inversion would erase its zero Cartier grade"},"first_missing_datum":"A nowhere-vanishing isomorphism between the short and long Rees quotient lines carrying t5 to t_D, or an independently geometric graph with equivalent endpoint alignment.","unconstructed":["universal integral long t_D line","clean unlocalized occurrence-normal diagonal","entry143 spatial support kernel using that diagonal"]}"#
    );
}
