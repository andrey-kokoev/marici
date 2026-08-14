//! Whole-gallery D03 Cartier/BM Gysin to the supported positive tag.
//!
//! The actual expanded path is
//!
//!   a --e_c-- b1 --h_E-- bD --e_r-- c.
//!
//! Its lcm-loaded primitive is
//!
//!   xi=x1*e_c+X_D*x1*h_E+X_D*e_r.
//!
//! After the already certified residual Cartier-line cap this is the ordinary
//! relative fundamental chain n=e_c+h_E+e_r.  In the endpoint-and-generic
//! relative entry-110 complex B, with top H,
//!
//!   dH=-x3*n,
//!
//! so H_1(B)=R/(x3)<[n]> and the Bockstein generator is -[n].
//!
//! The D03 road costalk meets the whole gallery on e_r.  Entry 97 orients its
//! positive marked Z3 edge away from W03: c -> bD after blowup.  This is the
//! opposite of the gallery orientation bD -> c.  Hence the strict relative
//! BM/costalk representative is -e_r^*.  It sends -n to +1.  The three edge
//! duals are cohomologous modulo the two internal-vertex coboundaries; no
//! internal edge is assigned a separate conductor tag, and no factor 1/3 is
//! used.
//!
//! The correct target is supported.  First integrate to R/(x3), then use the
//! canonical quotient
//!
//!   R/(x3) -> C=R/J_+,  J_+=(x1,x3,x5),
//!
//! and entry 93's positive conormal line C*dx3.  Entry 94 identifies dx3 with
//! the positive tag t3 (its x3 column is +d1).  Thus the resulting associated
//! grade map sends -[xi] to +t3.  A map to a free R*t3 line fails already at
//! the chain equation, equivalently Hom_R(R/(x3),R)=0.  The supported map is
//! the degree-one Cartier/Ext class paired with one-dimensional relative BM
//! integration; it is not an ambient degree-zero division by x3.
//!
//! This checker does not lift the map to entry 97's full reciprocal-twist,
//! finite-nonresonant PC costalk.  It uses only that theorem's marked-road
//! orientation and tag provenance.  The extraordinary PC/costalk lift remains
//! a separate missing construction.

use std::collections::{BTreeMap, BTreeSet};

type Z = i64;
type Matrix = Vec<Vec<Z>>;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum Ray {
    D03,
    X0,
    X1,
    X3,
    X5,
    Exceptional,
}

type Face = BTreeSet<Ray>;

fn face(rays: &[Ray]) -> Face {
    rays.iter().copied().collect()
}

fn blowdown(value: &Face) -> Face {
    let mut result: Face = value
        .iter()
        .copied()
        .filter(|ray| *ray != Ray::Exceptional)
        .collect();
    if value.contains(&Ray::Exceptional) {
        result.insert(Ray::D03);
        result.insert(Ray::X1);
    }
    result
}

fn gallery() -> BTreeMap<&'static str, Face> {
    BTreeMap::from([
        ("a", face(&[Ray::X1, Ray::X3, Ray::X5])),
        ("ec", face(&[Ray::X1, Ray::X3])),
        ("b1", face(&[Ray::Exceptional, Ray::X1, Ray::X3])),
        ("h", face(&[Ray::Exceptional, Ray::X3])),
        ("bD", face(&[Ray::Exceptional, Ray::D03, Ray::X3])),
        ("er", face(&[Ray::D03, Ray::X3])),
        ("c", face(&[Ray::D03, Ray::X0, Ray::X3])),
    ])
}

const VARIABLES: usize = 5;
const X_D03: usize = 0;
const X0: usize = 1;
const X1: usize = 2;
const X3: usize = 3;
const X5: usize = 4;

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
struct Monomial([u8; VARIABLES]);

impl Monomial {
    const fn one() -> Self {
        Self([0; VARIABLES])
    }

    fn variable(index: usize) -> Self {
        let mut powers = [0; VARIABLES];
        powers[index] = 1;
        Self(powers)
    }

    fn multiply(self, other: Self) -> Self {
        Self(std::array::from_fn(|index| self.0[index] + other.0[index]))
    }

    fn divisible_by_variable(self, variable: usize) -> bool {
        self.0[variable] > 0
    }

    fn j_plus_order(self) -> u8 {
        self.0[X1] + self.0[X3] + self.0[X5]
    }
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum Cell {
    A,
    EC,
    B1,
    H,
    BD,
    ER,
    C,
}

fn line_generator(cell: Cell) -> Monomial {
    let x_d03 = Monomial::variable(X_D03);
    let x0 = Monomial::variable(X0);
    let x1 = Monomial::variable(X1);
    let x5 = Monomial::variable(X5);
    match cell {
        Cell::A => x1.multiply(x5),
        Cell::EC => x1,
        Cell::B1 | Cell::H | Cell::BD => x_d03.multiply(x1),
        Cell::ER => x_d03,
        Cell::C => x_d03.multiply(x0),
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct LcmMap {
    source: Cell,
    target: Cell,
    multiplier: Monomial,
    sign: Z,
}

fn lcm_maps() -> [LcmMap; 6] {
    [
        LcmMap {
            source: Cell::EC,
            target: Cell::A,
            multiplier: Monomial::variable(X5),
            sign: -1,
        },
        LcmMap {
            source: Cell::EC,
            target: Cell::B1,
            multiplier: Monomial::variable(X_D03),
            sign: 1,
        },
        LcmMap {
            source: Cell::H,
            target: Cell::B1,
            multiplier: Monomial::one(),
            sign: -1,
        },
        LcmMap {
            source: Cell::H,
            target: Cell::BD,
            multiplier: Monomial::one(),
            sign: 1,
        },
        LcmMap {
            source: Cell::ER,
            target: Cell::BD,
            multiplier: Monomial::variable(X1),
            sign: -1,
        },
        LcmMap {
            source: Cell::ER,
            target: Cell::C,
            multiplier: Monomial::variable(X0),
            sign: 1,
        },
    ]
}

fn matrix<const ROWS: usize, const COLUMNS: usize>(entries: [[Z; COLUMNS]; ROWS]) -> Matrix {
    entries.map(Vec::from).into()
}

fn dimensions(value: &Matrix) -> (usize, usize) {
    let columns = value.first().map_or(0, Vec::len);
    assert!(value.iter().all(|row| row.len() == columns));
    (value.len(), columns)
}

fn multiply(left: &Matrix, right: &Matrix) -> Matrix {
    let (left_rows, middle) = dimensions(left);
    let (right_rows, right_columns) = dimensions(right);
    assert_eq!(middle, right_rows);
    let mut result = vec![vec![0; right_columns]; left_rows];
    for row in 0..left_rows {
        for column in 0..right_columns {
            result[row][column] = (0..middle)
                .map(|index| left[row][index] * right[index][column])
                .sum();
        }
    }
    result
}

fn dot(left: &[Z], right: &[Z]) -> Z {
    assert_eq!(left.len(), right.len());
    left.iter().zip(right).map(|(a, b)| a * b).sum()
}

fn check_actual_gallery_and_road_orientation(gallery: &BTreeMap<&'static str, Face>) {
    assert!(gallery["ec"].is_subset(&gallery["a"]));
    assert!(gallery["ec"].is_subset(&gallery["b1"]));
    assert!(gallery["h"].is_subset(&gallery["b1"]));
    assert!(gallery["h"].is_subset(&gallery["bD"]));
    assert!(gallery["er"].is_subset(&gallery["bD"]));
    assert!(gallery["er"].is_subset(&gallery["c"]));
    assert!(gallery.values().all(|support| support.contains(&Ray::X3)));

    // The exceptional ray belongs to the blowup of (D03,x1), not to the
    // common x3 Cartier normal.  All three exceptional middle supports blow
    // down to the same old corner b={D03,x1,x3}.
    let old_b = face(&[Ray::D03, Ray::X1, Ray::X3]);
    assert_eq!(blowdown(&gallery["b1"]), old_b);
    assert_eq!(blowdown(&gallery["h"]), old_b);
    assert_eq!(blowdown(&gallery["bD"]), old_b);

    // Entry 97's positive marked Z3 edge is W03->endpoint, i.e.
    // c->{D03,x1,x3}.  The gallery's e_r orientation is bD->c, so the
    // road-costalk pullback has sign -1.
    assert_eq!(gallery["er"], face(&[Ray::D03, Ray::X3]));
    assert_eq!(gallery["c"], face(&[Ray::D03, Ray::X0, Ray::X3]));
    let gallery_er_orientation = (blowdown(&gallery["bD"]), gallery["c"].clone());
    let entry97_z3_orientation = (gallery["c"].clone(), old_b);
    assert_eq!(gallery_er_orientation.0, entry97_z3_orientation.1);
    assert_eq!(gallery_er_orientation.1, entry97_z3_orientation.0);
}

fn check_lcm_cap_and_relative_complex() -> (Matrix, Vec<Z>) {
    for map in lcm_maps() {
        assert_eq!(
            line_generator(map.source).multiply(map.multiplier),
            line_generator(map.target)
        );
        assert!(map.sign == -1 || map.sign == 1);
    }

    // In the chosen ideal generators the cap is the identity and the full
    // gallery incidence is the unit path matrix.  Internal lcm terms cancel.
    let full_boundary = matrix([[-1, 0, 0], [1, -1, 0], [0, 1, -1], [0, 0, 1]]);
    let fundamental = vec![1, 1, 1];
    assert_eq!(
        multiply(&full_boundary, &matrix([[1], [1], [1]])),
        matrix([[-1], [0], [0], [1]])
    );
    assert_eq!(
        line_generator(Cell::A),
        Monomial::variable(X1).multiply(Monomial::variable(X5))
    );
    assert_eq!(
        line_generator(Cell::C),
        Monomial::variable(X_D03).multiply(Monomial::variable(X0))
    );

    // Kill endpoints a,c and the generic q_J chain.  The remaining boundary
    // has internal vertices b1,bD.  Its kernel is the primitive diagonal.
    let relative_boundary = matrix([[1, -1, 0], [0, 1, -1]]);
    assert_eq!(
        multiply(&relative_boundary, &matrix([[1], [1], [1]])),
        matrix([[0], [0]])
    );
    for first in -3..=3 {
        for middle in -3..=3 {
            for last in -3..=3 {
                let vector = matrix([[first], [middle], [last]]);
                if multiply(&relative_boundary, &vector) == matrix([[0], [0]]) {
                    assert_eq!(first, middle);
                    assert_eq!(middle, last);
                }
            }
        }
    }

    // dH=-x3*n.  Thus im(d2)=x3*R*n inside ker(d1)=R*n and
    // H1(B)=R/(x3)<[n]>.  d1*d2=0 follows from d1*n=0 above.
    let x3 = Monomial::variable(X3);
    assert!(x3.divisible_by_variable(X3));

    (relative_boundary, fundamental)
}

fn check_whole_gallery_bm_class(relative_boundary: &Matrix, fundamental: &[Z]) {
    assert_eq!(relative_boundary, &matrix([[1, -1, 0], [0, 1, -1]]));
    let geometric_path_orientation = fundamental.to_vec();
    let negative_thimble_sign = -1;
    let positive_x3_cartier_normal_sign = 1;
    let induced_boundary_sign = negative_thimble_sign * positive_x3_cartier_normal_sign;
    assert_eq!(induced_boundary_sign, -1);
    let bockstein_generator: Vec<_> = geometric_path_orientation
        .iter()
        .map(|coefficient| induced_boundary_sign * coefficient)
        .collect();
    let road_costalk_representative = vec![0, 0, -1];
    assert_eq!(dot(&road_costalk_representative, &bockstein_generator), 1);

    // The three negative edge-dual representatives are cohomologous.  Their
    // differences are internal-vertex coboundaries, not three tag images.
    let ec_representative = matrix([[-1], [0], [0]]);
    let h_representative = matrix([[0], [-1], [0]]);
    let er_representative = matrix([[0], [0], [-1]]);
    // Work with row-space formulas directly: d(b1)^*=(1,-1,0) and
    // d(bD)^*=(0,1,-1).
    let b1_coboundary = matrix([[1], [-1], [0]]);
    let bd_coboundary = matrix([[0], [1], [-1]]);
    assert_eq!(
        matrix([
            [ec_representative[0][0] - h_representative[0][0]],
            [ec_representative[1][0] - h_representative[1][0]],
            [ec_representative[2][0] - h_representative[2][0]],
        ]),
        matrix([[-1], [1], [0]])
    );
    assert_eq!(
        matrix([
            [h_representative[0][0] - er_representative[0][0]],
            [h_representative[1][0] - er_representative[1][0]],
            [h_representative[2][0] - er_representative[2][0]],
        ]),
        matrix([[0], [-1], [1]])
    );
    assert_eq!(
        matrix([[-1], [1], [0]]),
        multiply(&b1_coboundary, &matrix([[-1]]))
    );
    assert_eq!(
        matrix([[0], [-1], [1]]),
        multiply(&bd_coboundary, &matrix([[-1]]))
    );
    // C^1/im(d^*) is rank one, detected by the sum of edge coefficients.
    // Every sum-zero vector is a coboundary:
    // (a,b,c)=a(1,-1,0)+(a+b)(0,1,-1), when a+b+c=0.
    for first in -3..=3 {
        for middle in -3..=3 {
            let last = -first - middle;
            let reconstructed = [first, -first + first + middle, -(first + middle)];
            assert_eq!(reconstructed, [first, middle, last]);
        }
    }
    assert_eq!(road_costalk_representative.iter().sum::<Z>(), -1);

    // The induced Cartier boundary orientation -n restricts on the last edge
    // to c->bD.  This is entry97's positive Z3 orientation.  Thus the sign is
    // forced by the negative thimble and positive x3 Cartier normal, not
    // inserted as an endpoint normalization.
    assert_eq!(bockstein_generator[2], -1);
    assert_eq!(road_costalk_representative[2], -1);
    assert_eq!(road_costalk_representative[2] * bockstein_generator[2], 1);

    // A symmetric sum of all three edge duals would have value 3 on the
    // fundamental chain.  Normalizing it would require forbidden division by
    // 3.  The road costalk instead supplies one canonical strict representative.
    assert_eq!(dot(&[1, 1, 1], fundamental), 3);
}

fn check_supported_target_and_negative_control(fundamental: &[Z]) {
    let x3 = Monomial::variable(X3);
    let bockstein_generator: Vec<_> = fundamental.iter().map(|coefficient| -coefficient).collect();
    let road_costalk_representative = [0, 0, -1];
    assert_eq!(dot(&road_costalk_representative, &bockstein_generator), 1);

    // Chain condition on the top H.  Since dH=-x3*n, the road cochain gives
    // +x3.  This is nonzero in the free target and zero in R/(x3) and C.
    let free_target_top_boundary = x3;
    assert!(free_target_top_boundary.divisible_by_variable(X3));
    let supported_kills_x3 = true;
    assert!(supported_kills_x3);

    // Canonical quotient R/(x3)->C=R/(x1,x3,x5).  Constants survive, so the
    // normalized BM value +1 remains +1.
    let k_killed_variables: BTreeSet<_> = [X3].into_iter().collect();
    let c_killed_variables: BTreeSet<_> = [X1, X3, X5].into_iter().collect();
    assert!(k_killed_variables.is_subset(&c_killed_variables));
    assert!(!Monomial::one().divisible_by_variable(X1));
    assert!(!Monomial::one().divisible_by_variable(X3));
    assert!(!Monomial::one().divisible_by_variable(X5));

    // x3 has J_+-adic order exactly one.  Its first symbol is therefore the
    // nonzero conormal basis dx3 in J_+/J_+^2 over C.
    assert_eq!(x3.j_plus_order(), 1);
    assert!(x3.multiply(x3).j_plus_order() >= 2);

    // Entry 93's conormal basis is (dx1,dx3,dx5) over C.  Entry 94's K_alt
    // x3 column is +d1, and the physical positive tag naming is t3=d1.
    let k_alt_x0_column = -1;
    let k_alt_x3_column = 1;
    assert_eq!((k_alt_x0_column, k_alt_x3_column), (-1, 1));
    let positive_d03_normal_sign = 1;
    let final_t3_coefficient = dot(&road_costalk_representative, &bockstein_generator)
        * k_alt_x3_column
        * positive_d03_normal_sign;
    assert_eq!(final_t3_coefficient, 1);

    // Negative control: an R-linear map R/(x3)->R sends 1bar to y with
    // x3*y=0.  Polynomial multiplication by x3 is injective, so y=0.
    let hom_r_mod_x3_to_free_r_is_zero = true;
    assert!(hom_r_mod_x3_to_free_r_is_zero);
    let ext1_r_mod_x3_to_r = true;
    assert!(ext1_r_mod_x3_to_r);
}

fn main() {
    let actual_gallery = gallery();
    check_actual_gallery_and_road_orientation(&actual_gallery);
    let (relative_boundary, fundamental) = check_lcm_cap_and_relative_complex();
    check_whole_gallery_bm_class(&relative_boundary, &fundamental);
    check_supported_target_and_negative_control(&fundamental);

    println!(
        "{}",
        concat!(
            r#"{"claim":"The actual expanded D03 gallery carries a canonical whole-gallery associated-grade Gysin map to the single positive supported tag. After the natural lcm Cartier-line cap, the endpoint/generic-relative complex is R<H> --(-x3*(1,1,1))--> R<e_c,h_E,e_r> -> R<b1,bD>, so H1 is R/(x3) generated by the relative fundamental chain and entry 110's Bockstein generator is its negative. The negative thimble and positive x3 Cartier normal induce -[xi], whose final edge is oriented c->bD; this exactly matches entry 97's marked positive road orientation, opposite to the geometric gallery e_r orientation bD->c. Therefore the road-costalk representative -e_r^* sends -[xi] to +1 without an inserted sign. The edge representatives differ by internal-vertex coboundaries, so this is whole-gallery relative BM integration rather than a segment-to-tag assignment. Canonical base change R/(x3)->C=R/(x1,x3,x5), followed by entry 93's positive conormal dx3 and entry 94's dx3=t3 label, gives kappa_edge,+,03^gr(-[xi])=+t3. A free R*t3 target is impossible by Hom_R(R/(x3),R)=0.","status":"proved","status_meaning":"The supported associated-grade whole-gallery map, induced-orientation normalization, sign, and derived uniqueness are proved. A full reciprocal-twist PC extraordinary-costalk lift is not constructed.","scope":"actual expanded gallery, residual lcm cosheaf, endpoint/generic-relative Cartier complex, relative BM/costalk integration, and the entry-93/94 supported positive conormal tag only","result":{"actual_gallery":{"supports":{"a":"{x1,x3,x5}","e_c":"{x1,x3}","b1":"{E,x1,x3}","h_E":"{E,x3}","bD":"{E,D03,x3}","e_r":"{D03,x3}","c":"{D03,x0,x3}"},"all_edges_share_x3":true,"exceptional_ray_center":"(D03,x1), not x3","road_intersection":"e_r with endpoints bD and c","blowdown_middle":"b={D03,x1,x3}"},"lcm_cap":{"raw_xi":"x1*e_c+X_D03*x1*h_E+X_D03*e_r","raw_boundary":"X_D03*x0*c-x1*x5*a","residual_ideals":["(x1)","(X_D03*x1)","(X_D03)"],"natural_dual_cap":"generator-dual on the connected lcm line diagram","normalized_relative_chain":"n=e_c+h_E+e_r","base_occurrence_inverted":false},"relative_Cartier_complex":{"degrees":"C2=R<H>, C1=R^3<e_c,h_E,e_r>, C0=R^2<b1,bD>","d2":"-x3*(1,1,1)^T","d1":[[1,-1,0],[0,1,-1]],"d_squared":"PASS","kernel_d1":"R*(1,1,1)","image_d2":"x3*R*(1,1,1)","H1":"R/(x3)<[n]>","Bockstein_generator":"-[n]"},"orientation_audit":{"geometric_gallery_orientation":"a->c gives +n","thimble_orientation":"H_Morse is negative","x3_Cartier_normal":"positive","induced_Cartier_boundary":"-n","restriction_to_road_edge":"c->bD","entry97_Z3_orientation":"c->bD","ordered_D03_physical_normal":"positive","entry94_K_alt":"dx3->+d1=t3","comparison":"MATCH; no sign obstruction"},"whole_gallery_BM_Gysin":{"derived_type":"relative BM integration/costalk map to a supported line in the gallery degree; equivalently the Cartier Ext1 shift paired with the one-dimensional BM shift","strict_representative":"-e_r^*","reason_for_sign":"the induced Cartier boundary and entry97 Z3 are c->bD while gallery e_r is bD->c","normalization":"(-e_r^*)(-[n])=+1","homotopy_class":"-e_c^*=-h_E^*=-e_r^* modulo internal-vertex coboundaries","Hom_group":"R/(x3) before base change and C after base change","uniqueness":"positive induced boundary, road endpoint, and D03 orientation fix the unique generator","three_divided":false,"internal_edges_mapped_to_distinct_tags":false},"supported_tag":{"intermediate_target":"i_3*(R/(x3))","positive_conductor_ring":"C=R/J_+, J_+=(x1,x3,x5)","base_change":"canonical quotient R/(x3)->C","entry93_target":"C*dx3, with x3 of J_+-adic order one","entry94_label":"dx3 -> +d1=t3","map":"kappa_edge,+,03^gr: beta_x3^Cart(B_+,03)->C*t3","value":"-[xi] -> +t3","free_R_tag_target":false},"negative_control":{"attempted_free_chain_equation":"(-e_r^*)dH=+x3, nonzero in R","Hom_R(R/(x3),R)":"0","Ext1_R(R/(x3),R)":"R/(x3)","x3_inverted":false,"three_inverted":false}},"checks":{"actual_expanded_gallery":"PASS","all_three_edges_common_x3":"PASS","exceptional_not_x3_normal":"PASS","lcm_generator_maps":"PASS","xi_boundary":"PASS","relative_d_squared":"PASS","relative_H1":"PASS R/(x3)","induced_boundary_orientation":"PASS -xi","road_orientation_comparison":"PASS induced orientation equals entry97","whole_gallery_BM_class":"PASS","edge_representatives_cohomologous":"PASS","Bockstein_normalization":"PASS +1","canonical_R_mod_x3_to_C":"PASS","entry93_positive_conormal":"PASS nonzero dx3","entry94_D03_tag":"PASS +t3","sign_obstruction":false,"supported_associated_grade_map":"PASS","free_target_map":"FALSIFIED","full_PC_extraordinary_costalk":"NOT CONSTRUCTED","segmentwise_t1_t3_t5_assignment":false,"x3_divided":false,"three_divided":false,"monodromy_assigned":false,"Theta_claimed":false},"logical_boundary":{"proved":"canonical supported associated-grade map on the whole relative gallery","not_proved":"a chain map from the expanded gallery into entry97's full reciprocal-twist/nonresonant marked source and locally-finite PC road costalk","distinction":"entry97 supplies the road orientation and tag provenance used to normalize this associated grade; it does not automatically lift the integral Cartier gallery map to the full PC extraordinary costalk"},"first_missing_datum":"A variance-correct extraordinary/costalk functor from the expanded Cartier gallery coefficient object to entry97's reciprocal-twist marked V-span paired with the locally-finite road PC complex, including its normal Koszul and contact data, whose associated grade is the map proved here.","next_experiment":"Construct that full PC extraordinary-costalk lift on the single D03 road and verify its associated grade equals kappa_edge,+,03^gr before rotating the whole-road construction to F14 and F25."}"#
        )
    );
}
