fn close(a:f64,b:f64){assert!((a-b).abs()<2e-9,"{} != {}",a,b)}
fn main(){
    // One-sided exponential mollifier rho_e(x)=exp(-x/e)/e, x>=0.
    // Midpoint quadrature verifies the two ordered chambers before the
    // coincidence limit. Scaling removes epsilon, so set epsilon=1.
    let n=200_000usize;let xmax=24.0;let h=xmax/n as f64;
    let mut mass=0.;let mut lower=0.;let mut upper=0.;
    for i in 0..n{let x=(i as f64+0.5)*h;let rho=(-x).exp();mass+=rho*h;
        // Exact inner masses avoid an O(n^2) census.
        lower+=rho*(1.-(-x).exp())*h;
        upper+=rho*(-x).exp()*h;
    }
    close(mass,1.);close(lower,0.5);close(upper,0.5);close(lower+upper,mass*mass);

    // Printed H0=-delta*S0/2 with formal endpoint mass two.
    let endpoint_mass:f64=2.;let local_coefficient:f64=-0.5;
    let one=local_coefficient*endpoint_mass;
    let two_before_perturbative=local_coefficient.powi(2)*endpoint_mass.powi(2)*(lower+upper);
    let two_after_perturbative=-0.5*two_before_perturbative;
    close(one,-1.);close(two_after_perturbative,-0.5);
    println!("{{");
    println!("  \"schema\": \"marici.regulated_endpoint_occurrence_limit.v1\",");
    println!("  \"mollifier_mass\": {:.15},",mass);
    println!("  \"ordered_chambers\": [{:.15}, {:.15}],",lower,upper);
    println!("  \"ordered_sum\": {:.15},",lower+upper);
    println!("  \"one_boundary_effective_weight\": {:.1},",one);
    println!("  \"two_boundary_perturbative_weight\": {:.1},",two_after_perturbative);
    println!("  \"factorized_coincidence_limit\": true,");
    println!("  \"eq19_factor_two_generated\": false");
    println!("}}");
}
