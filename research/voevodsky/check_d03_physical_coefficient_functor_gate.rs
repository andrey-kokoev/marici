//! Ablation table for standard coefficient functors on the reduced cap.

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
enum Image {
    Zero,
    ResidueLine,
    LocalizedLine,
    CompletionQuotientShifted,
    LocalCohomologyShifted,
}

#[derive(Clone, Copy, Debug)]
struct FunctorTest {
    name: &'static str,
    branch_image: Image,
    center_image: Image,
}

fn main() {
    // R is x-adically separated, x is a regular parameter, and
    // D_x=RHom_R(R[x^-1],R) has H^1 = Rhat/R.  Multiplication by x is an
    // automorphism on Rhat/R.  These are the resulting standard functor
    // images, up to the common recorded shifts.
    let tests = [
        FunctorTest {
            name: "i_star_derived_tensor_R_mod_x",
            branch_image: Image::Zero,
            center_image: Image::ResidueLine,
        },
        FunctorTest {
            name: "i_shriek_RHom_R_mod_x",
            branch_image: Image::Zero,
            center_image: Image::ResidueLine,
        },
        FunctorTest {
            name: "j_star_localize_x",
            branch_image: Image::CompletionQuotientShifted,
            center_image: Image::LocalizedLine,
        },
        FunctorTest {
            name: "R_Gamma_x",
            branch_image: Image::Zero,
            center_image: Image::LocalCohomologyShifted,
        },
    ];

    for test in tests {
        assert_ne!(
            test.branch_image, test.center_image,
            "{} cannot carry the reduced cap to an identity",
            test.name
        );
    }

    println!(
        "{{\"claim\":\"No standard closed/open restriction or local-cohomology operation inverts the reduced Entry-176 localization-dual cap\",\"status\":\"standard_functors_fail\",\"tested\":[\"i_star\",\"i_shriek\",\"j_star\",\"R_Gamma_x\"],\"remaining\":\"an independently defined framed residue/relative-boundary functor or an independently justified Verdier quotient\"}}"
    );
}
