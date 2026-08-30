use symbolica::prelude::*;

fn atom(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default())
        .unwrap()
        .expand()
}

type Matrix2 = [[Atom; 2]; 2];

fn multiply(left: &Matrix2, right: &Matrix2) -> Matrix2 {
    std::array::from_fn(|i| {
        std::array::from_fn(|j| {
            (left[i][0].clone() * right[0][j].clone()
                + left[i][1].clone() * right[1][j].clone())
            .expand()
        })
    })
}

fn metric_sandwich(matrix: &Matrix2) -> Matrix2 {
    let signs = [1, -1];
    std::array::from_fn(|i| {
        std::array::from_fn(|j| {
            (atom(&signs[i].to_string()) * matrix[i][j].clone()
                * atom(&signs[j].to_string()))
            .expand()
        })
    })
}

fn ctp_defect(matrix: &Matrix2) -> Atom {
    (matrix[0][0].clone() + matrix[1][1].clone()
        - matrix[0][1].clone()
        - matrix[1][0].clone())
    .replace(atom("d").to_pattern())
    .with(atom("b+c-a").to_pattern())
    .expand()
}

fn impose_ctp(expression: Atom) -> Atom {
    expression
        .replace(atom("d").to_pattern())
        .with(atom("b+c-a").to_pattern())
        .expand()
}

fn impose_three_ctp(expression: Atom) -> Atom {
    expression
        .replace(atom("d").to_pattern())
        .with(atom("b+c-a").to_pattern())
        .replace(atom("h").to_pattern())
        .with(atom("f+g-e").to_pattern())
        .replace(atom("l").to_pattern())
        .with(atom("j+k-i").to_pattern())
        .expand()
}

fn to_three_keldysh(expression: Atom) -> Atom {
    let replacements = [
        ("a", "FL+(RL+AL)/2"),
        ("b", "FL-(RL-AL)/2"),
        ("c", "FL+(RL-AL)/2"),
        ("d", "FL-(RL+AL)/2"),
        ("e", "FM+(RM+AM)/2"),
        ("f", "FM-(RM-AM)/2"),
        ("g", "FM+(RM-AM)/2"),
        ("h", "FM-(RM+AM)/2"),
        ("i", "FR+(RR+AR)/2"),
        ("j", "FR-(RR-AR)/2"),
        ("k", "FR+(RR-AR)/2"),
        ("l", "FR-(RR+AR)/2"),
    ];
    let mut out = expression;
    for (from, to) in replacements {
        out = out
            .replace(atom(from).to_pattern())
            .with(atom(to).to_pattern());
    }
    out.expand().factor()
}

fn main() {
    let g: Matrix2 = [[atom("a"), atom("b")], [atom("c"), atom("d")]];
    let sigma: Matrix2 = [
        [atom("2*a"), atom("-2*b")],
        [atom("-2*c"), atom("2*d")],
    ];

    let ordinary = multiply(&multiply(&g, &sigma), &g);
    let metric = multiply(&multiply(&g, &metric_sandwich(&sigma)), &g);

    let ordinary_defect = ctp_defect(&ordinary);
    let metric_defect = ctp_defect(&metric);
    assert_eq!(ordinary_defect, atom("0"));
    assert_ne!(metric_defect, atom("0"));

    let components: Vec<String> = ordinary
        .iter()
        .flat_map(|row| row.iter())
        .map(|entry| impose_ctp(entry.clone()).to_string())
        .collect();
    let statistical = impose_ctp(
        (ordinary[0][1].clone() + ordinary[1][0].clone()) * atom("1/2"),
    );
    let spectral = impose_ctp(ordinary[1][0].clone() - ordinary[0][1].clone());
    let retarded = impose_ctp(ordinary[0][0].clone() - ordinary[0][1].clone());
    let common = atom("-3*a*b-3*a*c+b*c+3*a^2+b^2+c^2");
    assert_eq!(
        (statistical.clone() - atom("(b+c)") * common.clone()).expand(),
        atom("0")
    );
    assert_eq!(
        (spectral.clone() - atom("2*(c-b)") * common).expand(),
        atom("0")
    );
    assert_eq!((retarded.clone() - atom("2*(a-b)^3")).expand(), atom("0"));

    println!("ordinary_ctp_defect={ordinary_defect}");
    println!("metric_ctp_defect={metric_defect}");
    println!("ordinary_components={components:?}");
    println!("keldysh_statistical={}", statistical.factor());
    println!("keldysh_spectral={}", spectral.factor());
    println!("keldysh_retarded={}", retarded.factor());
    println!("occupation_ratio_preserved=true");

    // First convolution audit: keep the left leg, self-energy kernel, and
    // right leg independently labelled.  Each separately obeys the CTP
    // identity, but no time-ordering incidence relations are imposed yet.
    let left: Matrix2 = [[atom("a"), atom("b")], [atom("c"), atom("d")]];
    let middle_sigma: Matrix2 = [
        [atom("2*e"), atom("-2*f")],
        [atom("-2*g"), atom("2*h")],
    ];
    let right: Matrix2 = [[atom("i"), atom("j")], [atom("k"), atom("l")]];
    let independent = multiply(&multiply(&left, &middle_sigma), &right);
    let independent_defect = impose_three_ctp(
        independent[0][0].clone() + independent[1][1].clone()
            - independent[0][1].clone()
            - independent[1][0].clone(),
    )
    .factor();
    assert_eq!(independent_defect, atom("0"));
    let independent_statistical = impose_three_ctp(
        (independent[0][1].clone() + independent[1][0].clone()) * atom("1/2"),
    )
    .factor();
    let independent_spectral = impose_three_ctp(
        independent[1][0].clone() - independent[0][1].clone(),
    )
    .factor();
    let independent_retarded = impose_three_ctp(
        independent[0][0].clone() - independent[0][1].clone(),
    )
    .factor();
    let independent_advanced = impose_three_ctp(
        independent[0][0].clone() - independent[1][0].clone(),
    )
    .factor();
    let ra_statistical = to_three_keldysh(independent_statistical.clone());
    let ra_retarded = to_three_keldysh(independent_retarded.clone());
    let ra_advanced = to_three_keldysh(independent_advanced.clone());
    assert_eq!(
        (ra_statistical.clone()
            - atom("2*(FL*AM*AR+RL*FM*AR+RL*RM*FR)"))
        .expand(),
        atom("0")
    );
    assert_eq!(
        (ra_retarded.clone() - atom("2*RL*RM*RR")).expand(),
        atom("0")
    );
    assert_eq!(
        (ra_advanced.clone() - atom("2*AL*AM*AR")).expand(),
        atom("0")
    );
    println!("independent_three_kernel_ctp_defect={independent_defect}");
    println!("independent_ctp_relations_sufficient=true");
    println!("independent_keldysh_statistical={independent_statistical}");
    println!("independent_keldysh_spectral={independent_spectral}");
    println!("independent_keldysh_retarded={independent_retarded}");
    println!("independent_keldysh_advanced={independent_advanced}");
    println!(
        "independent_ra_statistical={}",
        ra_statistical
    );
    println!(
        "independent_ra_retarded={}",
        ra_retarded
    );
    println!(
        "independent_ra_advanced={}",
        ra_advanced
    );
}
