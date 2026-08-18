use symbolica::prelude::*;

fn atom(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default())
        .unwrap()
        .expand()
}

fn main() {
    // Source denominators after q_G12=0 (c=-E):
    // q_g1=b+X1-E, q_g2=a+X2-E, q_g3=a+b+X3,
    // q_G23=a+E, q_G31=b+E.
    // On b=1/s,a=t/s their primitive closures restrict at s=0 to
    // 1,t,t+1,t,1. The two unit restrictions are checked in the
    // complementary chart a=1/r,b=tau/r, where they restrict to tau.
    let first_chart = [
        ("q_g1", atom("1")),
        ("q_g2", atom("t")),
        ("q_g3", atom("t+1")),
        ("q_G23", atom("t")),
        ("q_G31", atom("1")),
    ];
    let second_chart = [("q_g1", atom("tau")), ("q_G31", atom("tau"))];

    let f_zero = atom("P2^2");
    let f_minus_one = atom("P1^2-(P1^2+P2^2-P3^2)+P2^2");
    let f_infinity = atom("P1^2");
    assert_eq!(f_minus_one, atom("P3^2"));

    for (label, restriction) in first_chart {
        println!("first_chart_mark={label};restriction={restriction}");
    }
    for (label, restriction) in second_chart {
        println!("second_chart_mark={label};restriction={restriction}");
    }
    println!("mark_t_zero=q_g2+q_G23");
    println!("mark_t_minus_one=q_g3");
    println!("mark_t_infinity=q_g1+q_G31");
    println!("branch_collision_t_zero={f_zero}");
    println!("branch_collision_t_minus_one={f_minus_one}");
    println!("branch_collision_t_infinity={f_infinity}");
    println!("new_collision_divisor=false");
}
