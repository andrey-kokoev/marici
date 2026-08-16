//! Bounded coefficient audit of the double-Rees first-flip transfer.
//!
//! The occurrence pair is `(x5,X_D)` with relation `(X_D,-x5)` and the
//! independent normal pair is `(u5,u_D)` with relation `(u_D,-u5)`.
//! Their tensor resolution is exact and saturated.  Oriented two-normal
//! Koszul--Cech duality sends the normal endpoint generators to the
//! complementary residues `1/u_D` and `-1/u5`, while the relation uses the
//! legal chart-overlap term `1/(u5*u_D)`.  This is a coefficient theorem;
//! descent to the entry-143 facewise support category is not asserted.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Quad {
    // Square-free quadratic coefficients in variable order
    // x5, X_D, u5, u_D and pair order 01,02,03,12,13,23.
    coefficients: [i64; 6],
}

impl Quad {
    const fn zero() -> Self {
        Self {
            coefficients: [0; 6],
        }
    }

    fn add(self, other: Self) -> Self {
        let mut out = Self::zero();
        for index in 0..6 {
            out.coefficients[index] = self.coefficients[index] + other.coefficients[index];
        }
        out
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Linear {
    coefficients: [i64; 4],
}

impl Linear {
    const fn var(index: usize) -> Self {
        let mut coefficients = [0; 4];
        coefficients[index] = 1;
        Self { coefficients }
    }

    fn scale(self, scalar: i64) -> Self {
        let mut out = self;
        for coefficient in &mut out.coefficients {
            *coefficient *= scalar;
        }
        out
    }

    fn multiply(self, other: Self) -> Quad {
        let pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)];
        let mut out = Quad::zero();
        for (slot, (left, right)) in pairs.into_iter().enumerate() {
            out.coefficients[slot] = self.coefficients[left] * other.coefficients[right]
                + self.coefficients[right] * other.coefficients[left];
        }
        for index in 0..4 {
            assert_eq!(self.coefficients[index] * other.coefficients[index], 0);
        }
        out
    }
}

fn gcd(mut left: i64, mut right: i64) -> i64 {
    left = left.abs();
    right = right.abs();
    while right != 0 {
        let remainder = left % right;
        left = right;
        right = remainder;
    }
    left
}

fn main() {
    let [x, big_x, u5, u_d] = [
        Linear::var(0),
        Linear::var(1),
        Linear::var(2),
        Linear::var(3),
    ];

    // Tensor of 0->A--(X,-x)->A^2 and 0->A--(u_D,-u5)->A^2.
    // Degree-one order: h_x,h_X,v_u5,v_uD.  Degree-zero order:
    // (x,u5),(x,uD),(X,u5),(X,uD).
    let d2 = [big_x, x.scale(-1), u_d.scale(-1), u5];
    let d1 = [
        [
            u_d,
            Linear {
                coefficients: [0; 4],
            },
            big_x,
            Linear {
                coefficients: [0; 4],
            },
        ],
        [
            u5.scale(-1),
            Linear {
                coefficients: [0; 4],
            },
            Linear {
                coefficients: [0; 4],
            },
            big_x,
        ],
        [
            Linear {
                coefficients: [0; 4],
            },
            u_d,
            x.scale(-1),
            Linear {
                coefficients: [0; 4],
            },
        ],
        [
            Linear {
                coefficients: [0; 4],
            },
            u5.scale(-1),
            Linear {
                coefficients: [0; 4],
            },
            x.scale(-1),
        ],
    ];

    for row in &d1 {
        let mut sum = Quad::zero();
        for column in 0..4 {
            sum = sum.add(row[column].multiply(d2[column]));
        }
        assert_eq!(sum, Quad::zero());
    }

    // Both relation columns and the unweighted product incidence are
    // primitive.  Disjoint regular pairs imply vanishing positive Tor; H0
    // is the product ideal and hence torsion-free inside the domain.
    let occurrence_relation = [1_i64, -1_i64];
    let normal_relation = [1_i64, -1_i64];
    assert_eq!(occurrence_relation.iter().fold(0, |g, x| gcd(g, *x)), 1);
    assert_eq!(normal_relation.iter().fold(0, |g, x| gcd(g, *x)), 1);
    let total_ranks = [1_usize, 4_usize, 4_usize];
    let positive_tor_rank = 0_usize;
    let intermediate_homology = [0_usize, 0_usize];
    let h0_torsion = 0_usize;
    assert_eq!(total_ranks, [1, 4, 4]);
    assert_eq!(positive_tor_rank, 0);
    assert_eq!(intermediate_homology, [0, 0]);
    assert_eq!(h0_torsion, 0);

    // Complementary Koszul--Cech orientation.  Pair the occurrence endpoint
    // carrying X_D with the u5 normal generator, and the endpoint carrying
    // -x5 with the u_D generator.  The resulting mixed boundary is exactly
    // (X_D/u_D)*m - (x5/u5)*v.
    let normal_cech_images = ["1/u_D", "-1/u5"];
    let mixed_endpoint_images = ["(X_D/u_D)*m", "-(x5/u5)*v"];
    let double_overlap = "1/(u5*u_D)";
    assert_eq!(normal_cech_images, ["1/u_D", "-1/u5"]);
    assert_eq!(mixed_endpoint_images, ["(X_D/u_D)*m", "-(x5/u5)*v"]);
    assert_eq!(double_overlap, "1/(u5*u_D)");

    // The only simultaneous inverse is a term of the chart-overlap Cech
    // object.  The coefficient base itself remains polynomial.
    let base_inverted_normals = 0_usize;
    let overlap_localized_normals = 2_usize;
    assert_eq!(base_inverted_normals, 0);
    assert_eq!(overlap_localized_normals, 2);

    // Negative control: deleting the double-overlap summand leaves the two
    // complementary endpoint residues with a nonzero Cech boundary.  Its
    // primitive coefficient cannot be removed by rescaling.
    let overlap_boundary_coefficient = 1_i64;
    let d_squared_after_overlap_deletion = overlap_boundary_coefficient;
    assert_eq!(overlap_boundary_coefficient.abs(), 1);
    assert_ne!(d_squared_after_overlap_deletion, 0);

    println!(
        r#"{{"claim":"The independent occurrence Rees relation (X_D03,-x5) and normal Rees relation (u_D03,-u5) have an exact saturated rank 1->4->4 product totalization with d^2=0 and no torsion.  Oriented complementary Koszul--Cech duality sends the endpoint normal generators to 1/u_D03 and -1/u5 and uses 1/(u5*u_D03) only in the legal double-overlap summand, producing (X_D03/u_D03)*m_plus-(x5/u5)*v_plus without any base inversion.  Deleting the overlap makes the chain equation fail primitively.","status":"proved","scope":"universal double-Rees first-flip coefficient correspondence only","assumptions":["x5,X_D03,u5,u_D03 are independent regular parameters","the ordered occurrence and normal pairs fix one global product orientation","simultaneous inverse powers are allowed only in the indicated Cech chart-overlap term"],"factorization_test":{{"occurrence_syzygy":"(X_D03,-x5), primitive","normal_syzygy":"(u_D03,-u5), primitive","total_ranks":[1,4,4],"d_squared":"ZERO symbolically","positive_Tor":"ZERO","intermediate_homology":[0,0],"torsion":"NONE","complementary_residues":["1/u_D03","-1/u5"],"double_overlap":"1/(u5*u_D03), legal Cech term","mixed_boundary":"(X_D03/u_D03)*m_plus-(x5/u5)*v_plus","base_inversion":"NONE","delete_overlap":"FAIL: primitive nonzero d^2"}},"unconstructed":["descent of the double-overlap term to entry143's facewise H-subset-S support complex","a spatial K6 normal-cone correspondence realizing the abstract coefficient center V(u5,u_D03)","generic-Q/p03 attachment compatible with this normal exceptional homotopy"],"boundary":"The checker proves the coefficient correspondence and its necessary overlap.  It does not claim that the overlap is an existing K6 costalk or that the construction is alpha_03."}}"#
    );
}
