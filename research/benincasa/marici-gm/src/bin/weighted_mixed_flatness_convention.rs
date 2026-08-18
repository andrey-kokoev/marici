use symbolica::prelude::*;

fn atom(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default())
        .unwrap()
        .expand()
}

fn main() {
    // Entry 793's exceptional tangential matrix and the complete normal
    // residue after the valuation-derived shear (0,0,4,2).  The lower-left
    // block is the principal vertical column before endpoint residues.
    let at = [
        ["0", "0", "0", "0"],
        ["0", "2*t/(t^2-1)", "0", "0"],
        ["0", "0", "0", "0"],
        ["0", "0", "0", "0"],
    ];
    let re = [
        ["-3/2", "0", "0", "0"],
        ["0", "4", "0", "0"],
        ["0", "-1/(2*(t^2-1))", "7/2", "0"],
        ["0", "3/(2*(t^2-1))", "0", "5/2"],
    ];

    let at = at.map(|row| row.map(atom));
    let re = re.map(|row| row.map(atom));
    let zero = atom("0");

    // The reconstructed source matrices obey dF=A F, hence dA-A^2=0.
    // At residue order the mixed equation is
    //   d_t R_e - A_t R_e + R_e A_t = 0.
    let mut theta = vec![vec![zero.clone(); 4]; 4];
    let mut wrong_sign = vec![vec![zero.clone(); 4]; 4];
    for i in 0..4 {
        for j in 0..4 {
            let derivative = re[i][j].derivative(symbol!("marici::t")).expand();
            let left = (0..4)
                .map(|k| (&at[i][k] * &re[k][j]).expand())
                .fold(zero.clone(), |sum, value| (sum + value).expand());
            let right = (0..4)
                .map(|k| (&re[i][k] * &at[k][j]).expand())
                .fold(zero.clone(), |sum, value| (sum + value).expand());
            theta[i][j] = (derivative.clone() - &left + &right).expand();
            wrong_sign[i][j] = (derivative + left - right).expand();
            assert_eq!(theta[i][j], zero);
        }
    }

    assert_eq!(wrong_sign[2][1], atom("2*t/(t^2-1)^2"));
    assert_eq!(wrong_sign[3][1], atom("-6*t/(t^2-1)^2"));

    println!("connection_convention=dF=A*F");
    println!("curvature_convention=dA-A_wedge_A=0");
    println!("mixed_residue_theta_rank=0");
    println!("principal_column_is_horizontal_chain_map=true");
    println!("homotopy_required=false");
    println!("opposite_sign_defect=(0,2*t/(t^2-1)^2,0,-6*t/(t^2-1)^2)");
}
