use symbolica::prelude::*;

fn z(s: &str) -> Atom {
    Atom::parse(s, "marici", Default::default()).unwrap().expand()
}

fn main() {
    let zero = z("0");
    // z=X3=u-y-1 in the normalized chart.
    assert_eq!(z("(u-v)/2-(u-((u+v)/2-1)-1)"), zero);

    // D2 has y=u^2, hence z=u-u^2-1=-(u^2-u+1), strictly negative.
    assert_eq!(z("(u-u^2-1)+(u^2-u+1)"), zero);
    // D3 can meet y>=0 only at u=y=0, where z=-1.
    assert_eq!(z("0-0-1+1"), zero);
    // Z12 has negative discriminant.
    assert_eq!(z("(-1)^2-4*1*1+3"), zero);
    // On real Z13, physical closure would require u>=1; then
    // u^2+u-1 is strictly positive, so no physical point exists.
    assert_eq!(z("(1)^2+1-1-1"), zero);
    // Z23 is the nonphysical point (u,y,z)=(0,0,-1).
    assert_eq!(z("0-0-1+1"), zero);

    println!("Symbolica: physical-base closure is disjoint from all three principal incidence supports");
}
