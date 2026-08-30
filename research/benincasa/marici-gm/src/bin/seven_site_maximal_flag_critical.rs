use serde_json::json;
use std::fs;
use symbolica::prelude::*;

fn a(source: &str) -> Atom {
    Atom::parse(source, "marici", Default::default())
        .unwrap()
        .expand()
}

fn replace(expression: Atom, variable: &Atom, value: &Atom) -> Atom {
    expression
        .replace(variable.to_pattern())
        .with(value.to_pattern())
}

fn main() {
    let k = a("k");
    let z = a("z");
    let x = a("x");
    let f = a("-12+82*k-122*k*z+64*k*z^2+24*z+112*k^2-175*k^2*z+64*k^2*z^2-12*z^2");
    let g = a("-6-67*k+58*k*z+6*z-118*k^2+76*k^2*z-56*k^3+40*k^3*z");
    let h = a("-12-278*k+98*k*z+24*k*x+12*z-452*k^2+89*k^2*z+28*k^2*x-168*k^3+128*k^3*z");
    let hx = h.derivative(symbol!("marici::x")).factor();
    let gram = a("k*(6+7*k)");
    assert_eq!(hx.clone(), a("4*k*(6+7*k)").expand().factor());
    assert_eq!(
        (hx.clone() / gram.clone()).together().cancel().expand(),
        a("4")
    );

    // The first two equations are independent of the sole free loop square x.
    // Solve the linear second equation for z to classify the ordinary
    // (noncritical) complete-intersection support.
    let g_z = g.derivative(symbol!("marici::z")).factor();
    let g_constant = replace(g.clone(), &z, &a("0")).factor();
    let z_solution = (-g_constant / g_z.clone()).together().cancel().expand();
    let base_resultant = (replace(f.clone(), &z, &z_solution) * g_z.clone() * g_z.clone())
        .together()
        .cancel()
        .expand()
        .factor();
    let x_solution = replace(
        (-replace(h.clone(), &x, &a("0")) / hx.clone())
            .together()
            .cancel()
            .expand(),
        &z,
        &z_solution,
    )
    .together()
    .cancel()
    .expand();

    let f0 = replace(f.clone(), &k, &a("0")).factor();
    let g0 = replace(g.clone(), &k, &a("0")).factor();
    let h0 = replace(h.clone(), &k, &a("0")).factor();
    let hx0 = replace(hx.clone(), &k, &a("0")).expand();
    assert_eq!(f0.clone().expand(), a("-12*(z-1)^2").expand());
    assert_eq!(g0.clone().expand(), a("6*(z-1)").expand());
    assert_eq!(h0.clone().expand(), a("12*(z-1)").expand());
    assert_eq!(hx0, a("0"));

    let k_second = a("-6/7");
    let f_second = replace(f.clone(), &k, &k_second).factor();
    let g_second = replace(g.clone(), &k, &k_second).factor();
    let h_second = replace(h.clone(), &k, &k_second).factor();
    let hx_second = replace(hx.clone(), &k, &k_second).expand();
    assert_eq!(hx_second, a("0"));
    assert_eq!(f_second.clone().expand(), a("-972/49*z^2").expand());
    assert_eq!(g_second.clone().expand(), a("-4482/343*z").expand());
    assert_eq!(h_second.clone().expand(), a("-29916/343*z").expand());

    // On the vertical line k=0,z=1, the selected sixfold source residue
    // leaves only the universal prefactor. For t=1 and y7=r its singleton
    // factors are listed below and are generically nonzero.
    let r = a("r");
    let singleton_factors = vec![
        (r.clone() - a("5/2")).expand(),
        a("-5"),
        a("-3"),
        a("-1"),
        a("1"),
        a("3"),
        (r.clone() + a("5/2")).expand(),
    ];
    let singleton_product = singleton_factors
        .iter()
        .fold(a("7"), |product, factor| product * factor.clone())
        .expand()
        .factor();
    assert_ne!(singleton_product, a("0"));

    let packet = json!({
        "schema":"marici.seven_site_maximal_flag_critical.v2",
        "pulled_cover":{"F":f.to_string(),"G":g.to_string(),"H":h.to_string()},
        "sole_free_loop_square":"x=y7^2",
        "critical_ideal":{"generators":["F","G","H","partial_x H"],"partial_x_H":hx.to_string(),"Gram_factor":gram.to_string(),"saturation":"unit ideal after inverting k*(6+7*k)"},
        "generic_conclusion":"no generic critical locus and therefore no horizontal Landau divisor",
        "ordinary_noncritical_intersection":{"z_solution":z_solution.to_string(),"base_resultant":base_resultant.to_string(),"x_solution":x_solution.to_string(),"classification":"transverse in x wherever the routing Gram is invertible"},
        "Gram_fibers":{
            "k=0":{"F":f0.to_string(),"G":g0.to_string(),"H":h0.to_string(),"critical_scheme":"(z-1) with x free","support":"reduced affine line","Cartier_length":1},
            "6+7k=0":{"k":"-6/7","F":f_second.to_string(),"G":g_second.to_string(),"H":h_second.to_string(),"critical_scheme":"(z) with x free","support":"reduced affine line contained in the inherited all-soft locus t=0","Cartier_length":1,"source_visibility":false,"source_multiplier_reason":"the wall solution makes t=y1=...=y6=0, so the frozen universal and singleton source factors vanish"}
        },
        "vertical_source_residue":{"t":1,"free_signed_loop_energy":"r=y7","singleton_factors":singleton_factors.iter().map(ToString::to_string).collect::<Vec<_>>(),"common_prefactor_product":singleton_product.to_string(),"generic_nonzero":true,"excluded_soft_points":["r=5/2","r=-5/2"]},
        "physical_activation":"no generic vanishing cycle exists for Bunch-Davies pairing; the vertical Gram line is source-visible but not a horizontal pinch",
        "classification":"one source-visible reduced Gram-supported vertical line at k=0 plus one reduced inherited all-soft line at 6+7k=0; no horizontal physical divisor and no Cartier excess"
    });
    fs::write(
        "../results/seven-site-maximal-flag-critical.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    )
    .unwrap();
    println!(
        "{}",
        json!({"dH_dx":hx.to_string(),"generic_critical":"empty after Gram saturation","Gram_fiber_k0":"reduced line z=1","Gram_fiber_second":{"F":f_second.to_string(),"G":g_second.to_string(),"H":h_second.to_string()}})
    );
}
