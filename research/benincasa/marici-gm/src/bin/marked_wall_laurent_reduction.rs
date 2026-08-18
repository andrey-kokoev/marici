use symbolica::prelude::*;
use symbolica::solve::SolveError;

fn atom(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap().expand()
}

fn reduce_wall_one(f: Atom, direction: Symbol) -> Vec<Atom> {
    let a = atom("a");
    let l = atom("a+(v-u)/2-1");
    let k = atom("(a^4-h*a^2*b^2+y^2*b^4+ga*a^2+gb*b^2+hh)")
        .replace(atom("b").to_pattern()).with(atom("u-1").to_pattern())
        .replace(atom("y").to_pattern()).with(atom("(u+v)/2-1").to_pattern())
        .replace(atom("h").to_pattern()).with(atom("1+((u+v)/2-1)^2-((u-v)/2)^2").to_pattern())
        .replace(atom("ga").to_pattern()).with(atom("(1-u^2)*(1-((u+v)/2-1)^2-((u-v)/2)^2)-2*u^2*((u-v)/2)^2").to_pattern())
        .replace(atom("gb").to_pattern()).with(atom("(((u+v)/2-1)^2-u^2)*(((u+v)/2-1)^2-1-((u-v)/2)^2)-2*u^2*((u-v)/2)^2").to_pattern())
        .replace(atom("hh").to_pattern()).with(atom("((u-v)/2)^2*((u^2-((u+v)/2-1)^2)*(u^2-1)+u^2*((u-v)/2)^2)").to_pattern())
        .expand();
    let s_poly = atom("s0+s1*a+s2*a^2+s3*a^3+s4*a^4+s5*a^5+s6*a^6");
    let lhs = ((f.derivative(direction) * k.clone() - f.clone() * k.derivative(direction) / atom("2")
        - atom("c0") * k.clone() / l.clone() - atom("c1") * k.clone()) * l.clone() * l.clone()).expand();
    let rhs = ((s_poly.derivative(symbol!("marici::a")) * l.clone() - s_poly.clone()) * k.clone()
        - s_poly * l * k.derivative(symbol!("marici::a")) / atom("2")).expand();
    let identity = (lhs - rhs).expand();
    let equations: Vec<Atom> = (0..=10)
        .map(|n| identity.replace(a.to_pattern()).with(atom(&n.to_string()).to_pattern()).expand())
        .collect();
    let vars: Vec<InlineVar> = vec![
        symbol!("marici::s0").into(), symbol!("marici::s1").into(), symbol!("marici::s2").into(),
        symbol!("marici::s3").into(), symbol!("marici::s4").into(), symbol!("marici::s5").into(),
        symbol!("marici::s6").into(), symbol!("marici::c0").into(), symbol!("marici::c1").into(),
    ];
    let raw = match AtomView::solve_linear_system::<u8, _, InlineVar>(&equations, &vars) {
        Ok(solution) => solution,
        Err(SolveError::Underdetermined { partial_solution, .. }) => partial_solution,
        Err(error) => panic!("wall reduction failed: {error:?}"),
    };
    let free_zero = atom("0");
    let sol_atoms: Vec<Atom> = raw.iter().map(|q| {
        atom(&q.to_string())
            .replace(atom("s3").to_pattern()).with(free_zero.to_pattern())
            .together().cancel().factor()
    }).collect();
    for coefficient in &sol_atoms[7..9] {
        let text = coefficient.to_string();
        assert!(!text.contains("marici::a"));
        assert!(!text.contains("marici::s"));
    }
    sol_atoms
}

fn reduce_wall_two(f: Atom, direction: Symbol) -> Vec<Atom> {
    let b = atom("b");
    let l = atom("b+1-u");
    let k = atom("(a^4-h*a^2*b^2+y^2*b^4+ga*a^2+gb*b^2+hh)")
        .replace(atom("a").to_pattern()).with(atom("1+(u-v)/2").to_pattern())
        .replace(atom("y").to_pattern()).with(atom("(u+v)/2-1").to_pattern())
        .replace(atom("h").to_pattern()).with(atom("1+((u+v)/2-1)^2-((u-v)/2)^2").to_pattern())
        .replace(atom("ga").to_pattern()).with(atom("(1-u^2)*(1-((u+v)/2-1)^2-((u-v)/2)^2)-2*u^2*((u-v)/2)^2").to_pattern())
        .replace(atom("gb").to_pattern()).with(atom("(((u+v)/2-1)^2-u^2)*(((u+v)/2-1)^2-1-((u-v)/2)^2)-2*u^2*((u-v)/2)^2").to_pattern())
        .replace(atom("hh").to_pattern()).with(atom("((u-v)/2)^2*((u^2-((u+v)/2-1)^2)*(u^2-1)+u^2*((u-v)/2)^2)").to_pattern())
        .expand();
    let s_poly = atom("s0+s1*b+s2*b^2+s3*b^3+s4*b^4+s5*b^5+s6*b^6");
    let lhs = ((f.derivative(direction) * k.clone() - f.clone() * k.derivative(direction) / atom("2")
        - atom("c0") * k.clone() / l.clone() - atom("c1") * k.clone()) * l.clone() * l.clone()).expand();
    let rhs = ((s_poly.derivative(symbol!("marici::b")) * l.clone() - s_poly.clone()) * k.clone()
        - s_poly * l * k.derivative(symbol!("marici::b")) / atom("2")).expand();
    let identity = (lhs - rhs).expand();
    let equations: Vec<Atom> = (0..=10)
        .map(|n| identity.replace(b.to_pattern()).with(atom(&n.to_string()).to_pattern()).expand())
        .collect();
    let vars: Vec<InlineVar> = vec![
        symbol!("marici::s0").into(), symbol!("marici::s1").into(), symbol!("marici::s2").into(),
        symbol!("marici::s3").into(), symbol!("marici::s4").into(), symbol!("marici::s5").into(),
        symbol!("marici::s6").into(), symbol!("marici::c0").into(), symbol!("marici::c1").into(),
    ];
    let raw = match AtomView::solve_linear_system::<u8, _, InlineVar>(&equations, &vars) {
        Ok(solution) => solution,
        Err(SolveError::Underdetermined { partial_solution, .. }) => partial_solution,
        Err(error) => panic!("second wall reduction failed: {error:?}"),
    };
    let sol_atoms: Vec<Atom> = raw.iter().map(|q| {
        atom(&q.to_string())
            .replace(atom("s3").to_pattern()).with(atom("0").to_pattern())
            .together().cancel().factor()
    }).collect();
    for coefficient in &sol_atoms[7..9] {
        let text = coefficient.to_string();
        assert!(!text.contains("marici::b"));
        assert!(!text.contains("marici::s"));
    }
    sol_atoms
}

fn run() {
    let mut blocks = Vec::new();
    for direction in [symbol!("marici::u"), symbol!("marici::v")] {
        let top1 = reduce_wall_one(atom("1/(a+(v-u)/2-1)"), direction);
        let wall1 = reduce_wall_one(atom("1"), direction);
        let top2 = reduce_wall_two(atom("1/(b+1-u)"), direction);
        let wall2 = reduce_wall_two(atom("1"), direction);
        assert_eq!(top1[7], top2[7]);
        blocks.push(vec![
            top1[7].clone(), top1[8].clone(), wall1[8].clone(),
            top2[8].clone(), wall2[8].clone(),
        ]);
    }
    let u = symbol!("marici::u");
    let v = symbol!("marici::v");
    for diagonal in [0, 2, 4] {
        assert_eq!(
            (blocks[1][diagonal].derivative(u) - blocks[0][diagonal].derivative(v))
                .together().cancel(),
            atom("0")
        );
    }
    for (beta, gamma) in [(1, 2), (3, 4)] {
        let curvature = blocks[1][beta].derivative(u) - blocks[0][beta].derivative(v)
            + blocks[0][beta].clone() * blocks[1][0].clone()
            + blocks[0][gamma].clone() * blocks[1][beta].clone()
            - blocks[1][beta].clone() * blocks[0][0].clone()
            - blocks[1][gamma].clone() * blocks[0][beta].clone();
        assert_eq!(curvature.together().cancel(), atom("0"));
    }
    for (name, block) in [("u", &blocks[0]), ("v", &blocks[1])] {
        println!("{name}: alpha={} beta1={} gamma1={} beta2={} gamma2={}",
            block[0], block[1], block[2], block[3], block[4]);
    }
    println!("same_sheet_top_horizontal=true");
    println!("A3_flat=true");
}

fn main() {
    std::thread::Builder::new()
        .name("marked-wall-laurent-symbolica".into())
        .stack_size(256 * 1024 * 1024)
        .spawn(run)
        .unwrap()
        .join()
        .unwrap();
}
