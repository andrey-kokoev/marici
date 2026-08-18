#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Valuation {
    k: i64,
    q2: i64,
    q3: i64,
    q23: i64,
}

impl Valuation {
    fn residue(self, weights: [i64; 4]) -> i64 {
        self.k * weights[0]
            + self.q2 * weights[1]
            + self.q3 * weights[2]
            + self.q23 * weights[3]
    }
}

fn main() {
    // Frozen factor order: K, q_g2, q_g3, q_g23 after taking q_g1 residue.
    let weights = [5_i64, 19, 23, 29];

    // At generic infinity K=s^-4 Kbar, q2 and q3 scale as s^-1,
    // while q23=X2+X3-X1 is constant on q_g1=0.
    let d_plus = Valuation { k: -4, q2: -1, q3: -1, q23: 0 };
    let d_minus = d_plus;

    // Blowing up the node t=+1 gives ord_E(Kbar)=2 and ord_E(s)=1.
    // The q2 numerator vanishes once there, cancelling its s^-1 pole;
    // q3 remains an s^-1 pole.  At t=-1 the roles are exchanged.
    let e_plus = Valuation { k: -2, q2: 0, q3: -1, q23: 0 };
    let e_minus = Valuation { k: -2, q2: -1, q3: 0, q23: 0 };

    assert_eq!(d_plus.residue(weights), -62);
    assert_eq!(d_minus.residue(weights), -62);
    assert_eq!(e_plus.residue(weights), -33);
    assert_eq!(e_minus.residue(weights), -29);
    assert!(
        [d_plus, d_minus, e_plus, e_minus]
            .into_iter()
            .all(|valuation| valuation.residue(weights) != 0)
    );

    println!("factor_order=K,q_g2,q_g3,q_g23");
    println!("weights=5,19,23,29");
    println!("valuation_D_plus=-4,-1,-1,0 residue=-62");
    println!("valuation_D_minus=-4,-1,-1,0 residue=-62");
    println!("valuation_E_plus=-2,0,-1,0 residue=-33");
    println!("valuation_E_minus=-2,-1,0,0 residue=-29");
    println!("q_g23_on_q_g1=X2+X3-X1_CONSTANT");
    println!("trivial_boundary_coefficient_system=FALSE_GENERICALLY");
    println!("four_plus_one_packet=ASSOCIATED_GRADE_ONLY");
}
