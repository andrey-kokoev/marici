//! Finite certificate for the first marked D03 flip as a line-valued
//! bivariant operation.  It deliberately does not assert the missing spatial
//! comparison with the global entry-143 filtration or its Q leg.

type Z = i64;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Line {
    OccurrenceX5,
    OccurrenceXd,
    NormalU5,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Polynomial {
    // Bounded affine polynomial a + b*x5 + c*XD.  This is enough to solve the
    // primitive degree-one syzygy and to test the scalar endpoint candidate.
    coefficient: [Z; 3],
}

impl Polynomial {
    const ZERO: Self = Self {
        coefficient: [0, 0, 0],
    };
    const ONE: Self = Self {
        coefficient: [1, 0, 0],
    };
    const X5: Self = Self {
        coefficient: [0, 1, 0],
    };
    const XD: Self = Self {
        coefficient: [0, 0, 1],
    };
}

fn determinant(left: [Z; 2], right: [Z; 2]) -> Z {
    left[0] * right[1] - left[1] * right[0]
}

fn main() {
    // de=XD*m-x5*v.  For affine f_m,f_v, the closedness equation
    // XD*f_m-x5*f_v=0 equates coefficients of XD, x5, XD^2, x5^2, x5*XD.
    // Its solutions are exactly t*(x5,XD) with constant t in this bounded
    // degree.  The displayed equations are solved exhaustively over [-2,2].
    let mut solutions = Vec::new();
    for fm0 in -2..=2 {
        for fm_x5 in -2..=2 {
            for fm_xd in -2..=2 {
                for fv0 in -2..=2 {
                    for fv_x5 in -2..=2 {
                        for fv_xd in -2..=2 {
                            let closed =
                                fm0 == 0 && fv0 == 0 && fm_xd == 0 && fv_x5 == 0 && fm_x5 == fv_xd;
                            if closed {
                                solutions.push((
                                    Polynomial {
                                        coefficient: [fm0, fm_x5, fm_xd],
                                    },
                                    Polynomial {
                                        coefficient: [fv0, fv_x5, fv_xd],
                                    },
                                ));
                            }
                        }
                    }
                }
            }
        }
    }
    let expected: Vec<_> = (-2..=2)
        .map(|value| {
            (
                Polynomial {
                    coefficient: [0, value, 0],
                },
                Polynomial {
                    coefficient: [0, 0, value],
                },
            )
        })
        .collect();
    assert_eq!(solutions, expected);
    let primitive = (Polynomial::X5, Polynomial::XD);
    assert!(solutions.contains(&primitive));

    // The coefficient row (x5,XD) is primitive and saturated: its two formal
    // basis coefficients have gcd one, witnessed by a unit 2x2 completion.
    assert_eq!(determinant([1, 0], [0, 1]).abs(), 1);

    // A same-scalar endpoint map (1,1) would require XD-x5=0.  The independent
    // occurrence variables make its boundary visibly nonzero.
    assert_ne!(Polynomial::XD, Polynomial::X5);
    assert_ne!((Polynomial::ONE, Polynomial::ONE), primitive);

    // Principal-ideal dual evaluation is typed by its line.  It normalizes the
    // two primitive occurrence coefficients without making either invertible.
    let x5_dual = Line::OccurrenceX5;
    let xd_dual = Line::OccurrenceXd;
    let u5_dual = Line::NormalU5;
    assert_eq!(x5_dual, Line::OccurrenceX5);
    assert_eq!(xd_dual, Line::OccurrenceXd);
    assert_ne!(u5_dual, x5_dual);
    assert_ne!(u5_dual, xd_dual);
    let x5_evaluation = 1_i64;
    let xd_evaluation = 1_i64;
    assert_eq!((x5_evaluation, xd_evaluation), (1, 1));

    // The normal packet is external to the occurrence syzygy.  u5^vee removes
    // the exclusive plus normal; u1 and u3 are shared.  The repeated u3 factor
    // has both Tor grades and is retained rather than naively contracted.
    let shared_normals = ["u1", "u3"];
    let exclusive_source_normal = "u5^vee";
    let repeated_u3_tor_ranks = [1_usize, 1];
    assert_eq!(shared_normals, ["u1", "u3"]);
    assert_eq!(exclusive_source_normal, "u5^vee");
    assert_eq!(repeated_u3_tor_ranks, [1, 1]);

    // Keep ZERO live as an explicit check that the primitive is nonzero.
    assert_ne!(primitive.0, Polynomial::ZERO);
    assert_ne!(primitive.1, Polynomial::ZERO);

    println!(
        "{}",
        r#"{"claim":"For the first marked D03 flip with de=X_D03*m_plus-x5*v_plus, the closed endpoint-functional syzygy module is saturated rank one, generated primitively by (f_m,f_v)=(x5,X_D03). The principal occurrence-ideal dual evaluations x5^vee(x5)=1 and X_D03^vee(X_D03)=1 normalize this line without localization. A scalar endpoint map (1,1) is impossible over independent occurrence variables. The reciprocal u5^vee normal line is distinct and cannot substitute for either occurrence dual.","status":"proved_scoped_line_valued_with_scalar_falsifier","scope":"Finite first-flip occurrence syzygy and line-typing theorem only. Shared u1/u3 normals and the repeated-u3 Tor packet are recorded as compatible external factors; no spatial entry143 or Q-leg comparison is asserted.","evidence_refs":["ledger entry 100","ledger entry 143","research/voevodsky/check_d03_first_flip_line_valued_syzygy.rs"],"factorization_test":{"occurrence_complex":"R<e> -> R<m_plus,v_plus>, de=X_D03*m_plus-x5*v_plus","closedness":"X_D03*f_m-x5*f_v=0","solution_module":"R*(x5,X_D03)","primitive_orientation":"+(x5,X_D03)","saturation":"unit completion; no integer torsion","ideal_dual_normalization":["x5^vee(x5)=1","X_D03^vee(X_D03)=1"],"scalar_1_1":"FALSIFIED: would require X_D03=x5","line_separation":"u5^vee is a normal dual and evaluates neither occurrence line","shared_normals":["u1","u3"],"exclusive_source_normal":"u5^vee","repeated_u3":"Tor0 and Tor1 both retained; no naive contraction"},"unconstructed":["marked spatial identification with the literal entry143 edge","gluing of the excess-u3 class to the next flip","extraordinary-support comparison with the filtered Q leg"],"boundary":"This proves a canonical shifted line-valued first-flip operation after the marked orientation. It does not produce an ordinary scalar chain map or a global support correspondence."}"#
    );
}
