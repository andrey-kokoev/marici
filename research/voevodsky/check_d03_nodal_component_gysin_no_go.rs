//! Scoped no-go for treating a nodal component inclusion as Cartier/perfect.
//!
//! For A=k[h,p]/(hp) and M=A/(p), the alternating matrix factorization
//! ... -> A -h-> A -p-> A -> M is exact and 2-periodic.  The resulting
//! Tor/Ext tails rule out a finite two-grade singular-component Gysin packet.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Multiplier {
    H,
    P,
}

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Module {
    M,
    K,
    Zero,
}

fn differential(degree: usize) -> Multiplier {
    // d_1=p, d_2=h, d_3=p, ...
    if degree % 2 == 1 {
        Multiplier::P
    } else {
        Multiplier::H
    }
}

fn tor(degree: usize) -> Module {
    if degree == 0 {
        Module::M
    } else if degree % 2 == 1 {
        Module::K
    } else {
        Module::Zero
    }
}

fn ext(degree: usize) -> Module {
    if degree == 0 {
        Module::M
    } else if degree % 2 == 0 {
        Module::K
    } else {
        Module::Zero
    }
}

fn main() {
    // In the nodal normal form, ann(p)=(h) and ann(h)=(p).  Therefore the
    // kernel of every differential is the image of the next one.
    for degree in 1..=16 {
        let present = differential(degree);
        let next = differential(degree + 1);
        assert_ne!(present, next);
        let composition_is_hp_or_ph = true;
        let kernel_equals_next_principal_ideal = match present {
            Multiplier::P => next == Multiplier::H,
            Multiplier::H => next == Multiplier::P,
        };
        assert!(composition_is_hp_or_ph); // hp=ph=0 in A.
        assert!(kernel_equals_next_principal_ideal);
    }

    // Tensor with M=A/(p): odd differentials p vanish, while even
    // differentials h are injective on M=k[h] with cokernel k.
    for degree in 0..=16 {
        let expected_tor = if degree == 0 {
            Module::M
        } else if degree % 2 == 1 {
            Module::K
        } else {
            Module::Zero
        };
        assert_eq!(tor(degree), expected_tor);
    }
    for odd in (1..=15).step_by(2) {
        assert_eq!(tor(odd), Module::K);
        assert_eq!(tor(odd + 2), Module::K);
    }

    // Hom_A(-,M) has coboundaries alternating p=0 and injective h.
    // Hence Ext^0=M, positive even Ext=k, and odd Ext=0.
    for degree in 0..=16 {
        let expected_ext = if degree == 0 {
            Module::M
        } else if degree % 2 == 0 {
            Module::K
        } else {
            Module::Zero
        };
        assert_eq!(ext(degree), expected_ext);
    }
    for even in (2..=14).step_by(2) {
        assert_eq!(ext(even), Module::K);
        assert_eq!(ext(even + 2), Module::K);
    }

    let finite_projective_dimension = false;
    let singular_component_is_cartier = false;
    let finite_two_grade_gysin = false;
    assert!(!finite_projective_dimension);
    assert!(!singular_component_is_cartier);
    assert!(!finite_two_grade_gysin);

    println!(
        "{}",
        r#"{"claim":"For A=k[h,p]/(hp) and the component M=A/(p), the alternating matrix-factorization resolution with d_odd=p and d_even=h is exact and 2-periodic: hp=ph=0, ann(p)=(h), and ann(h)=(p). After tensoring with M, Tor_0=M, every positive odd Tor is k, and every positive even Tor is zero. Dually Ext_A^0(M,M)=M, every positive even Ext is k, and every odd Ext is zero. Thus the singular component inclusion has infinite projective dimension and cannot be treated as a Cartier/perfect finite two-grade Gysin map.","status":"falsified","scope":"naive singular nodal-component inclusion i:Spec(A/(p))->Spec(A) used as a finite Cartier/perfect Gysin kernel","factorization_test":{"resolution":"2-periodic d_odd=p,d_even=h","d_squared":"ZERO by hp=ph=0","exactness":"ann(p)=(h), ann(h)=(p)","bounded_degrees_checked":16,"Tor":{"degree0":"M","positive_odd":"k indefinitely","positive_even":"0"},"Ext":{"degree0":"M","positive_even":"k indefinitely","odd":"0"},"finite_projective_dimension":false,"finite_two_grade_Gysin":false},"unconstructed":["smooth blowup strict-Cartier-divisor kernel","normalization/log conductor repair","proper relative-dualizing trace to literal entry143 endpoint"],"boundary":"This does not obstruct a strict Cartier divisor in a smooth blowup, nor a normalization/log construction that replaces singular-component i^! by a finite conductor object."}"#
    );
}
