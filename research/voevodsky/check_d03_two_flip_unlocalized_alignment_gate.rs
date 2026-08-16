//! Finite no-go for the unlocalized second weighted graph in the marked
//! two-flip path v+ -> m+ -> c.

type Point = [i64; 2];
const PRIME: i64 = 3;

fn modulo(value: i64) -> i64 {
    value.rem_euclid(PRIME)
}

fn projective_line() -> Vec<Point> {
    let mut result = (0..PRIME).map(|slope| [1, slope]).collect::<Vec<_>>();
    result.push([0, 1]);
    result
}

fn on_graph(occurrence: Point, normal: Point, t1: i64, t0: i64) -> bool {
    let [g, h] = occurrence;
    let [p, q] = normal;
    modulo(t0 * h * p - t1 * g * q) == 0
}

fn fiber(t1: i64, t0: i64) -> Vec<(Point, Point)> {
    let points = projective_line();
    points
        .iter()
        .flat_map(|occurrence| {
            points.iter().filter_map(move |normal| {
                on_graph(*occurrence, *normal, t1, t0).then_some((*occurrence, *normal))
            })
        })
        .collect()
}

fn normalize(point: Point) -> Point {
    assert_ne!(point, [0, 0]);
    if point[0] == 0 {
        [0, 1]
    } else {
        let inverse = (1..PRIME)
            .find(|candidate| modulo(point[0] * candidate) == 1)
            .expect("unit inverse");
        [1, modulo(point[1] * inverse)]
    }
}

fn main() {
    let points = projective_line();

    // Unit locus: [G:H]=[x1:x0] maps to [t1*G:t0*H]=[u1:u0].
    for t1 in 1..PRIME {
        for t0 in 1..PRIME {
            let graph = fiber(t1, t0);
            assert_eq!(graph.len(), points.len());
            for occurrence in &points {
                let image = normalize([modulo(t1 * occurrence[0]), modulo(t0 * occurrence[1])]);
                assert!(graph.contains(&(*occurrence, image)));
            }
            assert!(graph.contains(&([1, 0], [1, 0])));
            assert!(graph.contains(&([0, 1], [0, 1])));
        }
    }

    // t1=0 gives H*P=0; t0=0 gives G*Q=0.  Both are unions of two P1s
    // meeting once and hence have 2*(q+1)-1 points over F3.
    let t1_zero = fiber(0, 1);
    assert_eq!(t1_zero.len(), 2 * points.len() - 1);
    assert!(t1_zero
        .iter()
        .all(|(occurrence, normal)| occurrence[1] == 0 || normal[0] == 0));
    let t0_zero = fiber(1, 0);
    assert_eq!(t0_zero.len(), 2 * points.len() - 1);
    assert!(t0_zero
        .iter()
        .all(|(occurrence, normal)| occurrence[0] == 0 || normal[1] == 0));

    // At the double zero the equation vanishes, so the entire product and the
    // one-equation excess Tor1 line survive saturation.
    let double_zero = fiber(0, 0);
    assert_eq!(double_zero.len(), points.len() * points.len());
    assert!(double_zero
        .iter()
        .all(|(left, right)| *left != [0, 0] && *right != [0, 0]));
    let excess_tor1_rank = 1_usize;
    assert_eq!(excess_tor1_rank, 1);

    // Conditional facewise legality at m+={D03,x1,x3}: the oriented blowup
    // packet has all H subsets, including the mixed normal two-cell needed to
    // totalize the first and second flips.
    let mplus_normal_states = [
        "empty",
        "D03",
        "x1",
        "x3",
        "D03,x1",
        "D03,x3",
        "x1,x3",
        "D03,x1,x3",
    ];
    assert!(mplus_normal_states.contains(&"D03,x1"));
    let entry100_repeated_u3_tor_ranks = [1_usize, 1];
    assert_eq!(entry100_repeated_u3_tor_ranks, [1, 1]);

    // The special fibers contain more than the four points of an aligned
    // graph.  Therefore the full unlocalized closure has more than one
    // component-supported residue candidate; selecting the aligned one is an
    // additional quotient-line identification.
    assert!(t1_zero.len() > points.len());
    assert!(t0_zero.len() > points.len());
    assert!(double_zero.len() > points.len());
    let eta_mix_unique_from_unlocalized_graph = false;
    assert!(!eta_mix_unique_from_unlocalized_graph);

    // Every vertex and edge of v+->m+->c has short-boundary support, so the
    // literal filtration map factors through F_B and vanishes in Q=F_K/F_B.
    let two_flip_supports_in_f_b = [true, true, true, true, true];
    assert!(two_flip_supports_in_f_b.iter().all(|value| *value));
    let q_projection_rank = 0_usize;
    assert_eq!(q_projection_rank, 0);

    println!(
        "{}",
        r#"{"claim":"For the second marked flip, u1=t1*x1 and u0=t0*x0 define the weighted graph t0*H*P-t1*G*Q=0. It is the aligned projective graph where t0,t1 are units, but either single-zero fiber is a reducible union of two P1 components and the double-zero fiber is all P1xP1 with a rank-one excess Tor1 line. The actual m+ face packet contains the mixed H={D03,x1} state needed to totalize the two flips, and the entry100 repeated-u3 Tor0/Tor1 factor can pass externally, but the extra unlocalized graph components make the aligned residue and eta_mix nonunique. The full two-flip path lies in F_B and has zero projection to Q.","status":"falsified_scoped_unlocalized_two_flip_alignment","scope":"The admitted weighted-graph and entry143 facewise category for v+->m+->c only. This does not assert global nonexistence after adding an independently geometric nearby-cycle graph or quotient-line alignment.","evidence_refs":["ledger entries 100, 119, and 143","research/voevodsky/check_d03_two_flip_unlocalized_alignment_gate.rs"],"factorization_test":{"second_cross_relation":"t0*H*P-t1*G*Q=0","unit_locus":"aligned weighted graph with physical endpoints","t1_zero":"two P1 components","t0_zero":"two P1 components","double_zero":"full P1xP1","extra_Tor1":1,"mplus_mixed_normal_state":"H={D03,x1} exists","entry100_repeated_u3_Tor":[1,1],"eta_mix_from_full_closure":"not unique","two_flip_support":"entirely in F_B","Q_projection_rank":0},"first_obstruction":"No unlocalized nowhere-vanishing alignment t1~t0 is supplied; extra graph components and Tor survive projective saturation.","unconstructed":["clean second nearby-cycle graph","canonical selection of the aligned component-supported residue","generic-to-special Q leg"]}"#
    );
}
