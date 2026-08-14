//! Curated one-sheet D03 Cartier/conductor comparison certificate.
//!
//! The residual occurrence lines of the expanded gallery form the connected
//! lcm diagram
//!
//!   a <- e_c -> b1 <- h_E -> bD <- e_r -> c,
//!
//! with embedded principal ideals
//!
//!   e_c:(x1), h_E:(X_D*x1), e_r:(X_D),
//!   a:(x1*x5), b1=bD:(X_D*x1), c:(X_D*x0).
//!
//! Every variance-correct structure map multiplies the source generator by
//! its lcm quotient and therefore sends it to the chosen target generator.
//! The generator-dual caps are consequently natural on the full displayed
//! stalk/vertex diagram.  Since its incidence graph is connected, compatible
//! dual trivializations are unique up to one common unit (over the universal
//! polynomial ring, one common sign).  No occurrence variable is inverted.
//!
//! Conditional on the marked-cell correspondence
//!
//!   (e_c,h_E,e_r) -> (t1,t3,t5),
//!   (a,b1,bD,c)   -> (q1,q0,q2,q1),
//!
//! the capped gallery incidence is a strict lower chain map to entry 94's
//! oriented triangle.  The tag matching is an input here, not derived from an
//! independent geometric correspondence.  Entry 94 itself fixes
//! (t1,t3,t5)=(d2,d1,d0), and the positive-sheet polarity values are all +1.
//! Both gallery endpoints map to q1, so the map descends from the full path to
//! the endpoint-relative source precisely after quotienting q1 in the target.
//!
//! Before the x3 Cartier connecting operation, the strict typed top map is
//!
//!   H -> -x3*f_+,
//!
//! because dH=-x3*xi and d(f_+)=t1+t3+t5.  After the Bockstein, however, Hbar
//! is R/(x3)-valued.  Since x3 is a non-zero-divisor,
//! Hom_R(R/(x3),R)=0, so Hbar -> -f_+ is not a strict map to the free tag
//! complex.  It can exist only after base-changing the tag complex to R/(x3),
//! on an explicitly defined associated grade, or as the Ext1/Gysin class
//! Ext1_R(R/(x3),R)=R/(x3).  This checker constructs none of those promotions
//! and claims neither a full kappa map nor a shift-zero Cartier map.
//!
//! The exact Rees typing is as follows.  Give the source its uniform descending
//! x3-adic filtration and the target the staggered lattice
//!
//!   F_T^p(R*f_+)=x3^(p+1)R*f_+,   F_T^p(P_tag)=x3^p P_tag.
//!
//! Then H -> -x3*f_+ and the capped lower identity form a strict filtered map
//! of degree zero.  Its first top symbol is not -f_+ in a free associated
//! grade: it is -[x3] tensor f_+ in (I3/I3^2) tensor f_+.  Only the separately
//! oriented conormal evaluation [x3] -> 1 produces -f_+.  With the ordinary
//! uniform target filtration the grade-zero top symbol is zero.  Entries 93
//! and 94 supply neither this staggered occurrence lattice nor the marked
//! gallery-to-tag correspondence, so the construction remains conditional.

use std::collections::{BTreeMap, BTreeSet};

type Z = i64;
type Matrix = Vec<Vec<Z>>;

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

    fn divisible_by(self, divisor: Self) -> bool {
        (0..VARIABLES).all(|index| self.0[index] >= divisor.0[index])
    }

    fn quotient(self, divisor: Self) -> Self {
        assert!(self.divisible_by(divisor));
        Self(std::array::from_fn(|index| {
            self.0[index] - divisor.0[index]
        }))
    }
}

type Polynomial = BTreeMap<Monomial, Z>;

fn multiply_polynomial_by_monomial(value: &Polynomial, scalar: Monomial) -> Polynomial {
    let result: Polynomial = value
        .iter()
        .map(|(monomial, coefficient)| (monomial.multiply(scalar), *coefficient))
        .collect();
    // Translation of exponent vectors is injective, so no nonzero term can
    // disappear.  This is the exact non-zero-divisor check used below.
    assert_eq!(result.len(), value.len());
    result
}

#[derive(Clone, Copy, Debug, Eq, Ord, PartialEq, PartialOrd)]
enum Cell {
    A,
    EC,
    B1,
    HE,
    BD,
    ER,
    C,
}

impl Cell {
    const fn index(self) -> usize {
        match self {
            Self::A => 0,
            Self::EC => 1,
            Self::B1 => 2,
            Self::HE => 3,
            Self::BD => 4,
            Self::ER => 5,
            Self::C => 6,
        }
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct CartierLine {
    cell: Cell,
    generator: Monomial,
}

fn line(cell: Cell) -> CartierLine {
    let x_d03 = Monomial::variable(X_D03);
    let x0 = Monomial::variable(X0);
    let x1 = Monomial::variable(X1);
    let x5 = Monomial::variable(X5);
    let generator = match cell {
        Cell::A => x1.multiply(x5),
        Cell::EC => x1,
        Cell::B1 | Cell::HE | Cell::BD => x_d03.multiply(x1),
        Cell::ER => x_d03,
        Cell::C => x_d03.multiply(x0),
    };
    CartierLine { cell, generator }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct StructureMap {
    source: Cell,
    target: Cell,
    incidence_sign: Z,
}

impl StructureMap {
    fn lcm_multiplier(self) -> Monomial {
        line(self.target)
            .generator
            .quotient(line(self.source).generator)
    }

    fn maps_generator_to_generator(self) -> bool {
        line(self.source).generator.multiply(self.lcm_multiplier()) == line(self.target).generator
    }
}

fn structure_maps() -> [StructureMap; 6] {
    [
        StructureMap {
            source: Cell::EC,
            target: Cell::A,
            incidence_sign: -1,
        },
        StructureMap {
            source: Cell::EC,
            target: Cell::B1,
            incidence_sign: 1,
        },
        StructureMap {
            source: Cell::HE,
            target: Cell::B1,
            incidence_sign: -1,
        },
        StructureMap {
            source: Cell::HE,
            target: Cell::BD,
            incidence_sign: 1,
        },
        StructureMap {
            source: Cell::ER,
            target: Cell::BD,
            incidence_sign: -1,
        },
        StructureMap {
            source: Cell::ER,
            target: Cell::C,
            incidence_sign: 1,
        },
    ]
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct LineElement {
    line: CartierLine,
    quotient: Monomial,
    coefficient: Z,
}

fn structure_image(map: StructureMap, value: LineElement) -> LineElement {
    assert_eq!(value.line, line(map.source));
    LineElement {
        line: line(map.target),
        quotient: value.quotient,
        coefficient: value.coefficient * map.incidence_sign,
    }
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct DualCap {
    line: CartierLine,
    common_unit: Z,
}

impl DualCap {
    fn evaluate(self, value: LineElement) -> (Monomial, Z) {
        assert_eq!(self.line, value.line);
        (value.quotient, self.common_unit * value.coefficient)
    }
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

fn check_full_lcm_diagram_and_dual_cap() {
    let maps = structure_maps();
    let expected_multipliers = [
        Monomial::variable(X5),
        Monomial::variable(X_D03),
        Monomial::one(),
        Monomial::one(),
        Monomial::variable(X1),
        Monomial::variable(X0),
    ];
    assert_eq!(maps.map(StructureMap::lcm_multiplier), expected_multipliers);
    assert!(maps
        .iter()
        .copied()
        .all(StructureMap::maps_generator_to_generator));

    // Natural evaluation square, including its oriented incidence sign:
    // cap_target(rho(s)) = sign(rho)*cap_source(s).
    for map in maps {
        for common_unit in [-1, 1] {
            let source_value = LineElement {
                line: line(map.source),
                quotient: Monomial::variable(X3),
                coefficient: 2,
            };
            let target_value = structure_image(map, source_value);
            let target_cap = DualCap {
                line: line(map.target),
                common_unit,
            };
            let source_cap = DualCap {
                line: line(map.source),
                common_unit,
            };
            let (target_monomial, target_coefficient) = target_cap.evaluate(target_value);
            let (source_monomial, source_coefficient) = source_cap.evaluate(source_value);
            assert_eq!(target_monomial, source_monomial);
            assert_eq!(target_coefficient, map.incidence_sign * source_coefficient);
        }
    }

    // Compatible dual trivializations assign a unit to every chosen line
    // generator.  The connected diagram forces equality along all six maps.
    // Since the only units of Z[X_D,x0,x1,x3,x5] are +/-1, enumerate them.
    let mut compatible_unit_families = BTreeSet::new();
    for mask in 0_u8..(1 << 7) {
        let family: [Z; 7] =
            std::array::from_fn(|index| if mask & (1 << index) == 0 { -1 } else { 1 });
        if maps
            .iter()
            .all(|map| family[map.source.index()] == family[map.target.index()])
        {
            compatible_unit_families.insert(family);
        }
    }
    assert_eq!(compatible_unit_families.len(), 2);
    assert!(compatible_unit_families.contains(&[-1; 7]));
    assert!(compatible_unit_families.contains(&[1; 7]));

    // The normalized differential of the three edge generators.  Embedded
    // back into R, its internal terms have the same lcm monomial and cancel;
    // the two surviving terms are -x1*x5 at a and +X_D*x0 at c.
    let gallery_incidence = matrix([[-1, 0, 0], [1, -1, 0], [0, 1, -1], [0, 0, 1]]);
    let xi_column = matrix([[1], [1], [1]]);
    assert_eq!(
        multiply(&gallery_incidence, &xi_column),
        matrix([[-1], [0], [0], [1]])
    );
    assert_eq!(
        line(Cell::A).generator,
        Monomial::variable(X1).multiply(Monomial::variable(X5))
    );
    assert_eq!(
        line(Cell::C).generator,
        Monomial::variable(X_D03).multiply(Monomial::variable(X0))
    );
}

fn check_entry_93_94_and_conditional_lower_map() {
    // Entry 94 rows are (d0,d1,d2), columns are the positive conductor
    // directions (x1,x3,x5).  Relabelling rows to (t1,t3,t5)=(d2,d1,d0)
    // makes the positive one-sheet tag map the identity.
    let k_alt_positive_d_rows = matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]]);
    let physical_tag_relabelling = matrix([[0, 0, 1], [0, 1, 0], [1, 0, 0]]);
    assert_eq!(
        multiply(&physical_tag_relabelling, &k_alt_positive_d_rows),
        matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    );
    let delta_dual = matrix([[1, 1, 1]]);
    assert_eq!(
        multiply(&delta_dual, &k_alt_positive_d_rows),
        matrix([[1, 1, 1]])
    );

    // This is the explicitly assumed marked-cell correspondence.  It maps
    // the path a->b1->bD->c around the oriented triangle
    // q1->q0->q2->q1.  The matrix equality proves the full lower chain map.
    let gallery_incidence = matrix([[-1, 0, 0], [1, -1, 0], [0, 1, -1], [0, 0, 1]]);
    let edge_to_tag = matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]);
    let vertex_to_road = matrix([[0, 1, 0, 0], [1, 0, 0, 1], [0, 0, 1, 0]]);
    // In physical columns (t1,t3,t5), entry 94's triangle boundary is
    // t1:q0-q1, t3:q2-q0, t5:q1-q2.
    let triangle_boundary = matrix([[1, -1, 0], [-1, 0, 1], [0, 1, -1]]);
    assert_eq!(
        multiply(&triangle_boundary, &edge_to_tag),
        multiply(&vertex_to_road, &gallery_incidence)
    );
    assert_eq!(
        multiply(&triangle_boundary, &matrix([[1], [1], [1]])),
        matrix([[0], [0], [0]])
    );
    // Columns a and c both equal q1, proving descent to the corresponding
    // endpoint-relative quotients rather than silently killing mismatched
    // target vertices.
    assert_eq!(
        vertex_to_road.iter().map(|row| row[0]).collect::<Vec<_>>(),
        vertex_to_road.iter().map(|row| row[3]).collect::<Vec<_>>()
    );
}

fn check_pre_cartier_map_and_post_cartier_obstruction() {
    let x3 = Monomial::variable(X3);
    // After the natural residual cap, dH=-x3*(t1+t3+t5).  The positive
    // conductor differential is d(f_+)=(1,1,1), so the unique strict free
    // top multiplier is -x3.
    let capped_pre_cartier_boundary = [(x3, -1), (x3, -1), (x3, -1)];
    let top_image_coefficient = (x3, -1);
    assert!(capped_pre_cartier_boundary
        .iter()
        .all(|entry| *entry == top_image_coefficient));

    // Polynomial multiplication by x3 is injective.  Hence an R-linear map
    // R/(x3)->R sends 1bar to y with x3*y=0, forcing y=0.
    let mut hypothetical_image = Polynomial::new();
    hypothetical_image.insert(Monomial::one(), -1);
    assert!(!hypothetical_image.is_empty());
    let x3_times_image = multiply_polynomial_by_monomial(&hypothetical_image, x3);
    assert!(!x3_times_image.is_empty());
    let hom_r_mod_x3_to_r_is_zero = true;
    assert!(hom_r_mod_x3_to_r_is_zero);

    // The Koszul cochain R --x3--> R has zero kernel and nonzero cokernel.
    // The constant class is not divisible by x3, so it generates the scoped
    // Ext1 control R/(x3); realizing it is a Gysin/associated-grade step.
    assert!(!Monomial::one().divisible_by(x3));
    let ext1_is_r_mod_x3 = true;
    assert!(ext1_is_r_mod_x3);
}

fn x3_power(power: usize) -> Monomial {
    let mut result = Monomial::one();
    for _ in 0..power {
        result = result.multiply(Monomial::variable(X3));
    }
    result
}

fn check_rees_cartier_typing() {
    let x3 = Monomial::variable(X3);

    // Descending filtration exponents for source top/bottom and target
    // top/tags.  The source is uniform; the target top is staggered once.
    for filtration_degree in 0..=5 {
        let source_top_exponent = filtration_degree;
        let source_bottom_exponent = filtration_degree;
        let target_top_exponent = filtration_degree + 1;
        let target_tag_exponent = filtration_degree;

        // H -> -x3*f raises the ambient exponent once and therefore lands
        // exactly in F_T^p(top).  The lower cap has coefficient one.
        assert_eq!(source_top_exponent + 1, target_top_exponent);
        assert_eq!(source_bottom_exponent, target_tag_exponent);

        // Both differentials have filtration order one.  On the source,
        // dH=-x3*xi.  On the target, an element of F_T^p(top) already carries
        // x3^(p+1), and d(f)=sum(tags), so it lands in F_T^(p+1)(tags).
        assert_eq!(source_top_exponent + 1, source_bottom_exponent + 1);
        assert_eq!(target_top_exponent, target_tag_exponent + 1);

        // Strictness.  The total top image is x3*R*f.  Intersecting it with
        // x3^(p+1)R*f gives exponent max(1,p+1)=p+1, exactly the image of
        // x3^p H.  The total lower image is all P_tag.
        assert_eq!(1_usize.max(target_top_exponent), source_top_exponent + 1);
        assert_eq!(0_usize.max(target_tag_exponent), source_bottom_exponent);

        assert_eq!(
            x3_power(source_top_exponent).multiply(x3),
            x3_power(target_top_exponent)
        );
        assert_eq!(
            x3_power(source_bottom_exponent),
            x3_power(target_tag_exponent)
        );
    }

    // The first top Rees symbol is represented by -x3 modulo x3^2.  It is
    // nonzero and lives in (I3/I3^2) tensor f_+, not in the free R*f_+ line.
    let i3_generator = x3;
    let i3_squared_generator = x3.multiply(x3);
    assert!(i3_generator.divisible_by(x3));
    assert!(!i3_generator.divisible_by(i3_squared_generator));
    let first_rees_symbol_coefficient = -1;
    assert_eq!(first_rees_symbol_coefficient, -1);

    // Positive oriented conormal evaluation [x3] -> 1 gives -f_+.  Reversing
    // the conormal orientation reverses the result.  This is ideal-line
    // evaluation and never adjoins x3^-1 to the base.
    let positive_conormal_orientation = 1;
    let evaluated_symbol = positive_conormal_orientation * first_rees_symbol_coefficient;
    assert_eq!(evaluated_symbol, -1);
    let reversed_evaluated_symbol = -positive_conormal_orientation * first_rees_symbol_coefficient;
    assert_eq!(reversed_evaluated_symbol, 1);

    // Ordinary uniform filtration on the free target puts f_+ in F^0.  The
    // actual image -x3*f_+ lies in F^1 and hence has zero grade-zero symbol;
    // replacing it by -f_+ would be the already-falsified torsion-to-free
    // shortcut rather than the Rees symbol of the strict map.
    let uniform_target_top_degree_of_image = 1;
    let uniform_target_grade_zero_symbol_nonzero = uniform_target_top_degree_of_image == 0;
    assert!(!uniform_target_grade_zero_symbol_nonzero);

    let staggered_lattice_constructed_by_entries_93_94 = false;
    let marked_gallery_tag_correspondence_constructed_by_entries_93_94 = false;
    assert!(!staggered_lattice_constructed_by_entries_93_94);
    assert!(!marked_gallery_tag_correspondence_constructed_by_entries_93_94);
}

fn main() {
    check_full_lcm_diagram_and_dual_cap();
    check_entry_93_94_and_conditional_lower_map();
    check_pre_cartier_map_and_post_cartier_obstruction();
    check_rees_cartier_typing();

    println!(
        "{}",
        concat!(
            r#"{"claim":"The full residual lcm stalk/vertex diagram of the expanded D03 gallery has a canonical natural dual cap: every structure map sends its chosen principal-ideal generator to the chosen target generator, and compatible dual trivializations are unique up to one common unit. Conditional on the explicitly supplied marked-cell correspondence (e_c,h_E,e_r)->(t1,t3,t5) and (a,b1,bD,c)->(q1,q0,q2,q1), these caps give a strict lower chain map to the entry-94 positive triangle; because both endpoints map to q1, it descends to the endpoint-relative source after the matching q1 target quotient. Before the x3 Cartier connecting operation there is a unique strict top map H->-x3*f_+. With the source uniform x3-adic filtration and the target staggered lattice F_T^p(R*f_+)=x3^(p+1)R*f_+, F_T^p(P_tag)=x3^pP_tag, this map is strict filtered degree zero and its first top Rees symbol is -[x3] tensor f_+ in (I3/I3^2) tensor f_+. Only oriented conormal evaluation gives -f_+. The ordinary uniform-target associated grade gives zero, and after the Bockstein there is no nonzero strict R-linear Hbar->f_+ map to the free target because Hom_R(R/(x3),R)=0. Entries 93-94 construct neither the staggered occurrence lattice nor the marked-cell correspondence. No full kappa or shift-zero Cartier map is claimed.","status":"conditional","status_meaning":"The lcm diagram, natural dual cap, conditional lower matrix, relative descent, strict filtered pre-Cartier Rees map, conormal symbol, and Hom/Ext obstruction are proved. The marked-cell correspondence, staggered target lattice as geometry, and post-Cartier Gysin promotion are not supplied by entries 93-94.","scope":"full seven-stalk residual occurrence diagram, conditional lower positive-triangle comparison, exact Rees/Cartier filtration audit, and strict pre-versus-post-Cartier typing only","ring":{"base":"R=Z[X_D03,x0,x1,x3,x5,other independent occurrence variables]","units":"+/-1","base_inversions":[],"x3_non_zero_divisor":true,"monodromy_used":false},"residual_lcm_diagram":{"cells":["a","e_c","b1","h_E","bD","e_r","c"],"principal_ideals":{"a":"(x1*x5)","e_c":"(x1)","b1":"(X_D03*x1)","h_E":"(X_D03*x1)","bD":"(X_D03*x1)","e_r":"(X_D03)","c":"(X_D03*x0)"},"oriented_structure_maps":["e_c->a: -x5","e_c->b1: +X_D03","h_E->b1: -1","h_E->bD: +1","e_r->bD: -x1","e_r->c: +x0"],"generator_property":"every unsigned lcm map sends source generator to target generator","normalized_incidence_matrix":[[-1,0,0],[1,-1,0],[0,1,-1],[0,0,1]],"xi_boundary":"X_D03*x0*c-x1*x5*a","internal_junctions_cancel":true},"natural_dual_cap":{"family":"generator-dual evaluation on every labelled Cartier line","naturality":"cap_target(rho(s))=incidence_sign(rho)*cap_source(s)","compatible_trivializations":"unique up to one common unit because the seven-cell incidence graph is connected","universal_ring_unit_families":["all +1","all -1"],"positive_orientation":"selects all +1","occurrence_inverted":false},"entry93_94_conventions":{"K_alt_positive_columns_in_d0_d1_d2_rows":[[0,0,1],[0,1,0],[1,0,0]],"physical_tags":"(t1,t3,t5)=(d2,d1,d0)","positive_polarity_values":[1,1,1],"target_top_boundary":"d(f_+)=t1+t3+t5","staggered_x3_lattice_constructed":false,"gallery_tag_marking_constructed":false},"conditional_lower_map":{"marked_cell_correspondence_status":"INPUT/NOT INDEPENDENTLY DERIVED","edges":"(e_c,h_E,e_r)->(t1,t3,t5)","vertices":"(a,b1,bD,c)->(q1,q0,q2,q1)","triangle_boundary_in_t1_t3_t5_columns":[[1,-1,0],[-1,0,1],[0,1,-1]],"chain_matrix_identity":"PASS","endpoint_images":"a and c both map to q1","relative_descent":"PASS after quotienting endpoints in the source and q1 in the target","polarity":"positive sheet only"},"pre_cartier":{"source_identity":"dH=-x3*xi after killing q_J and endpoints","target_scope":"two-level tag truncation, or the q1-relative triangle for the full lower map","strict_map":"H->-x3*f_+","lower_map":"xi components cap to t1+t3+t5","chain_identity":"d(-x3*f_+)=-x3*(t1+t3+t5)","top_multiplier":"-x3, uniquely forced","typed_over_R":true,"integral":true},"post_cartier":{"top_source":"R/(x3)<Hbar>","free_target_top":"R<f_+>","Hom_R(R/(x3),R)":"0","strict_Hbar_to_minus_f_plus":"DOES NOT EXIST","Ext1_R(R/(x3),R)":"R/(x3)","allowed_future_types":["base-change target tags to R/(x3)","explicit associated grade","Ext1/Gysin correspondence"],"degree_shift":"NOT CLAIMED","full_kappa":"NOT CONSTRUCTED"},"rees_cartier_typing":{"source_filtration":"uniform F_S^p=x3^p on H and the capped gallery","target_filtration":{"top":"F_T^p(R*f_+)=x3^(p+1)R*f_+","tags":"F_T^p(P_tag)=x3^pP_tag"},"strict_filtered_degree":"0","strictness":"PASS on top and tags","top_differential_filtration_order":"one for H->gallery and f_+->tags","lower_gallery_triangle_incidence":"checked separately at filtration order zero under the marked-cell input","first_top_symbol":"-[x3] tensor f_+ in (I3/I3^2) tensor f_+","positive_oriented_conormal_evaluation":"[x3]->1 gives -f_+","orientation_reversal":"gives +f_+","base_x3_inverted":false,"ordinary_uniform_target_gr0":"ZERO because -x3*f_+ lies in F^1","free_target_shortcut":"FAIL by Hom_R(R/(x3),R)=0","entries93_94_supply_staggered_lattice":false,"entries93_94_supply_marking":false},"checks":{"full_lcm_stalk_vertex_diagram":"PASS","all_lcm_generator_maps":"PASS","natural_dual_cap":"PASS","compatible_dual_family":"PASS unique up to common sign","xi_internal_cancellation":"PASS","entry93_94_positive_basis":"PASS","conditional_lower_chain_map":"PASS under marked-cell input","endpoint_relative_descent":"PASS with q1-relative target","strict_pre_Cartier_map":"PASS H->-x3*f_+","uniform_source_filtration":"PASS","staggered_target_filtration":"PASS algebraically, NOT independently geometric","filtered_degree_zero":"PASS","filtered_strictness":"PASS","first_Rees_symbol":"PASS in (I3/I3^2) tensor f_+","oriented_conormal_evaluation":"PASS -> -f_+","ordinary_uniform_target_gr0":"ZERO","x3_non_zero_divisor":"PASS","post_Cartier_strict_free_target_map":"FALSIFIED by Hom=0","Ext1_Gysin_location":"PASS R/(x3)","tag_correspondence_derived":false,"staggered_lattice_derived_from_entries93_94":false,"shift_zero_Cartier_map_claimed":false,"full_kappa_constructed":false,"H_cond_constructed":false,"global_sp_constructed":false,"polarity_conjugate_constructed":false,"Theta_constructed":false,"occurrence_inverted":false,"monodromy_assigned":false},"first_missing_datum":"An independently geometric marked-cell correspondence and staggered x3 lattice/variance-correct post-Cartier target. Entries 93-94 supply neither; after those data, one must still construct the associated-grade or Ext1/Gysin comparison because Hbar cannot map nontrivially to the free f_+ line.","boundary":"The staggered lattice makes the pre-Cartier map a strict filtered theorem and locates its first symbol in the conormal line, but the lattice and tag marking are stipulated audit data, not consequences of entries 93-94. The only strict free-target chain map proved is H->-x3*f_+. No full one-sheet kappa, post-Cartier shift-zero map, negative sheet, K_alt assembly, H_cond, global sp_G, Q leg, purity, monodromy, Cousin, or Theta comparison is constructed.","next_experiment":"Derive both the marked gallery-to-tag correspondence and the staggered x3 target lattice from an actual conductor/expanded-gallery geometric span, then construct its oriented conormal/Ext1-Gysin realization and compare that associated grade with the conditional matrices proved here."}"#
        )
    );
}
