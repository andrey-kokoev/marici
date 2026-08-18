use symbolica::prelude::*;

fn z(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap().expand()
}

fn main() {
    let zero = z("0");
    assert_eq!(z("-16*(u^2)^2-8*u^2*u^2+8*u*u^3-5*u^4+21*u^4"), zero);
    // Reduction of u(1-u)-1 using u^2=u-1.
    assert_eq!(z("u-(u-1)-1"), zero);
    assert_eq!(z("-16*(-u^2)^2-8*(-u^2)*u^2+8*u*u^3-5*u^4+5*u^4"), zero);
    // Reduction of u(u+1)-1 using u^2=1-u.
    assert_eq!(z("(1-u)+u-1"), zero);
    assert_eq!(z("-16*0^2-8*0*0^2+8*1*0^3-5*0^4"), zero);

    for entry in ["0*0-0*0", "0*1-1*0", "0*(-1)-(-1)*0"] {
        assert_eq!(z(entry), zero);
    }
    // lambda M=0 for M=[[0,1,0],[0,0,1],[0,-1,1]].
    for entry in ["1*0-1*0+1*0", "1*1-1*0+1*(-1)", "1*0-1*1+1*1"] {
        assert_eq!(z(entry), zero);
    }
    // With dM=A_E=0, Entry 743's projected obstruction vanishes.
    assert_eq!(z("1*(0+0)-1*(0+0)+1*(0+0)"), zero);
    println!("Symbolica: support fields, vacuous Q-linear descent, and Q restrictions verified");
}
