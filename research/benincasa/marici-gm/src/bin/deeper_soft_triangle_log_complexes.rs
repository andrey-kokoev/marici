use symbolica::prelude::*;

fn atom(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default())
        .unwrap()
        .expand()
}

fn set(expression: Atom, variable: &str, value: &str) -> Atom {
    expression
        .replace(atom(variable).to_pattern())
        .with(atom(value).to_pattern())
        .expand()
}

fn verify() {
    let k = atom(
        "E^4*P3^2-E^2*A*P1^2+E^2*A*P2^2-E^2*A*P3^2+E^2*B*P1^2-E^2*B*P2^2-E^2*B*P3^2-E^2*P1^2*P3^2-E^2*P2^2*P3^2+E^2*P3^4+A^2*P1^2-A*B*P1^2-A*B*P2^2+A*B*P3^2+A*P1^4-A*P1^2*P2^2-A*P1^2*P3^2+B^2*P2^2-B*P1^2*P2^2+B*P2^4-B*P2^2*P3^2+P1^2*P2^2*P3^2",
    );

    for r in ["1", "-1"] {
        for s in ["1", "-1"] {
            let one_scale = set(
                set(set(k.clone(), "P3", "0"), "P2", &format!("{s}*P1")),
                "E",
                &format!("{r}*P1"),
            );
            assert_eq!((one_scale - atom("P1^2*(A-B)^2")).expand(), atom("0"));
        }
    }

    let all_soft = set(set(set(set(k, "E", "0"), "P1", "0"), "P2", "0"), "P3", "0");
    assert_eq!(all_soft, atom("0"));

    // Reduced conductor Cech differential Q^2 -> Q, (x,y) |-> x-y.
    let d = [1_i32, -1_i32];
    let kernel_generator = [1_i32, 1_i32];
    assert_eq!(d[0] * kernel_generator[0] + d[1] * kernel_generator[1], 0);
    let cech_kernel_rank = 1;
    let cech_cokernel_rank = 0;

    println!("one_scale_identity=K=P1^2*(A-B)^2");
    println!("one_scale_log_factors=(a-b)*(a+b)");
    println!("one_scale_cech_differential=[1,-1]");
    println!("one_scale_anti_invariant_rank={cech_kernel_rank}");
    println!("one_scale_cech_cokernel_rank={cech_cokernel_rank}");
    println!("all_soft_restriction=0");
    println!("all_soft_first_object=projectivized_degree_six_normal_cone");
    println!("all_soft_finite_transverse_rank=undefined");
}

fn main() {
    std::thread::Builder::new()
        .name("deeper-soft-triangle-symbolica".into())
        .stack_size(64 * 1024 * 1024)
        .spawn(verify)
        .unwrap()
        .join()
        .unwrap();
}
