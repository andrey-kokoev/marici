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

fn run() {
    for (direction_name, direction) in [("u", symbol!("marici::u")), ("v", symbol!("marici::v"))] {
        for (form_name, form) in [("top1", atom("1/(a+(v-u)/2-1)")), ("wall1", atom("1"))] {
            let sol = reduce_wall_one(form, direction);
            println!("{direction_name}:{form_name}: c0={} c1={}", sol[7], sol[8]);
        }
    }
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
