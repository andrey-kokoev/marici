use serde_json::{json, Value};
use std::{fs, sync::Arc};
use symbolica::prelude::*;

fn sym(name: &str) -> Symbol {
    Symbol::parse(name, "marici").unwrap()
}

fn fnv1a64(text: &str) -> String {
    let mut hash = 0xcbf29ce484222325_u64;
    for byte in text.as_bytes() {
        hash ^= *byte as u64;
        hash = hash.wrapping_mul(0x100000001b3);
    }
    format!("{hash:016x}")
}

fn mod_power(mut base: i64, mut exponent: u16, prime: i64) -> i64 {
    let mut result = 1_i64;
    base = base.rem_euclid(prime);
    while exponent > 0 {
        if exponent & 1 == 1 { result = ((result as i128 * base as i128) % prime as i128) as i64; }
        base = ((base as i128 * base as i128) % prime as i128) as i64;
        exponent >>= 1;
    }
    result
}

fn square_root(value: i64, prime: i64) -> Option<i64> {
    let target = value.rem_euclid(prime);
    (0..prime).find(|root| (root * root).rem_euclid(prime) == target)
}

fn evaluate_base_polynomial(
    polynomial: &MultivariatePolynomial<Q,u16>,
    prime: i64,
    t: i64,
    u: [i64;3],
) -> i64 {
    let mut evaluation = 0_i64;
    for term_index in 0..polynomial.nterms() {
        let view = polynomial.to_monomial_view(term_index);
        let coefficient = view.coefficient.to_string().parse::<i128>().unwrap();
        let mut term = coefficient.rem_euclid(prime as i128) as i64;
        for (index,variable) in polynomial.get_vars_ref().iter().enumerate() {
            let value = if *variable == PolyVariable::Symbol(sym("t")) { t }
                else if *variable == PolyVariable::Symbol(sym("u1")) { u[0] }
                else if *variable == PolyVariable::Symbol(sym("u2")) { u[1] }
                else if *variable == PolyVariable::Symbol(sym("u3")) { u[2] }
                else { 0 };
            term = ((term as i128 * mod_power(value,view.exponents[index],prime) as i128)
                % prime as i128) as i64;
        }
        evaluation = (evaluation + term).rem_euclid(prime);
    }
    evaluation
}

fn evaluate_cover_sample(
    numerator: &MultivariatePolynomial<Q, u16>,
    coefficients: &[MultivariatePolynomial<Q,u16>;32],
    prime: i64,
    seed: i64,
) -> Value {
    for offset in 0..10_000_i64 {
        let u1 = (seed + 3 * offset + 2).rem_euclid(prime);
        let u2 = (2 * seed + 5 * offset + 3).rem_euclid(prime);
        let u3 = (3 * seed + 7 * offset + 5).rem_euclid(prime);
        let f1 = (2*u1*u1 + 2*u2*u2 + u3*u3 - 2*u1*u2 - 2*u2*u3).rem_euclid(prime);
        let values = [
            f1,
            (f1 - 2*u1 + 1).rem_euclid(prime),
            (f1 - 2*u2 + 2).rem_euclid(prime),
            (f1 - 2*u3 + 3).rem_euclid(prime),
            (f1 + 2*u1 + 2*u2 - 8*u3 + 29).rem_euclid(prime),
        ];
        let roots = values.iter().map(|value| square_root(*value, prime)).collect::<Option<Vec<_>>>();
        if let Some(roots) = roots {
            let t = (11 * seed + 13).rem_euclid(prime);
            let mut evaluation = 0_i64;
            for term_index in 0..numerator.nterms() {
                let view = numerator.to_monomial_view(term_index);
                let coefficient = view.coefficient.to_string().parse::<i128>().unwrap();
                let mut term = coefficient.rem_euclid(prime as i128) as i64;
                for (index,variable) in numerator.get_vars_ref().iter().enumerate() {
                    let value = if *variable == PolyVariable::Symbol(sym("t")) { t } else {
                        let edge = [sym("y1"),sym("y2"),sym("y3"),sym("y4"),sym("y5")]
                            .iter().position(|candidate| *variable == PolyVariable::Symbol(*candidate)).unwrap();
                        roots[edge]
                    };
                    term = ((term as i128 * mod_power(value, view.exponents[index], prime) as i128)
                        % prime as i128) as i64;
                }
                evaluation = (evaluation + term).rem_euclid(prime);
            }
            let mut reconstructed = 0_i64;
            for (mask,coefficient) in coefficients.iter().enumerate() {
                let mut term = evaluate_base_polynomial(coefficient,prime,t,[u1,u2,u3]);
                for edge in 0..5 {
                    if mask & (1 << edge) != 0 {
                        term = ((term as i128 * roots[edge] as i128) % prime as i128) as i64;
                    }
                }
                reconstructed = (reconstructed + term).rem_euclid(prime);
            }
            return json!({
                "prime": prime, "t": t, "u": [u1,u2,u3], "y": roots,
                "numerator_value": evaluation,
                "reconstructed_character_value": reconstructed,
                "passes": evaluation == reconstructed
            });
        }
    }
    panic!("no five-square cover point found");
}

fn run() {
    let profile = std::env::var("KINEMATIC_PROFILE").unwrap_or_else(|_| "A".to_owned());
    let prefix_depth = profile.strip_prefix("PREFIX_")
        .map(|raw| raw.parse::<usize>().expect("PREFIX depth must be an integer"));
    assert!(profile == "A" || profile == "B" || profile == "FORMAL" || profile == "FAMILY"
        || profile == "HOMOGENEOUS"
        || prefix_depth.is_some_and(|depth| depth <= 5));
    let source: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-site-asymmetric-canonical-sum.json").unwrap()
    ).unwrap();
    let numerator_text = source["combined_numerator"].as_str().unwrap();
    let input_fingerprint = fnv1a64(numerator_text);
    assert_eq!(source["combined_numerator_fnv1a64"].as_str(), Some(input_fingerprint.as_str()),
        "canonical numerator fingerprint mismatch; refusing stale or inconsistent input");
    let cover_order = Arc::new(vec![
        PolyVariable::Symbol(sym("t")),
        PolyVariable::Symbol(sym("y1")),
        PolyVariable::Symbol(sym("y2")),
        PolyVariable::Symbol(sym("y3")),
        PolyVariable::Symbol(sym("y4")),
        PolyVariable::Symbol(sym("y5")),
    ]);
    let numerator: MultivariatePolynomial<Q, u16> =
        Atom::parse(numerator_text, "marici", Default::default()).unwrap()
            .expand().to_polynomial(&Q, Some(cover_order));
    assert_eq!(numerator.nterms(), 13_304);
    let cover_t_index = numerator.get_vars_ref().iter()
        .position(|entry| *entry == PolyVariable::Symbol(sym("t"))).unwrap();
    let y_symbols = [sym("y1"),sym("y2"),sym("y3"),sym("y4"),sym("y5")];
    let cover_y_indices: [usize;5] = std::array::from_fn(|edge|
        numerator.get_vars_ref().iter().position(|entry|
            *entry == PolyVariable::Symbol(y_symbols[edge])
        ).unwrap()
    );

    let base_order = Arc::new(vec![
        PolyVariable::Symbol(sym("t")),
        PolyVariable::Symbol(sym("u1")),
        PolyVariable::Symbol(sym("u2")),
        PolyVariable::Symbol(sym("u3")),
        PolyVariable::Symbol(sym("s1")),
        PolyVariable::Symbol(sym("s2")),
        PolyVariable::Symbol(sym("s3")),
        PolyVariable::Symbol(sym("s4")),
        PolyVariable::Symbol(sym("s5")),
        PolyVariable::Symbol(sym("lam")),
        PolyVariable::Symbol(sym("rho")),
    ]);
    let base = |text: &str| -> MultivariatePolynomial<Q, u16> {
        Atom::parse(text, "marici", Default::default()).unwrap()
            .expand().to_polynomial(&Q, Some(base_order.clone()))
    };
    let f1 = base("2*u1^2+2*u2^2+u3^2-2*u1*u2-2*u2*u3");
    let f5_physical = if profile == "B" {
        &f1 + &base("2*u1+4*u2-12*u3+61")
    } else if profile == "FAMILY" {
        &f1 + &base("2*u1+(2+2*lam)*u2-(8+4*lam)*u3+29+26*lam+6*lam^2")
    } else {
        &f1 + &base("2*u1+2*u2-8*u3+29")
    };
    let physical = if profile == "HOMOGENEOUS" {[
        f1.clone(),
        &f1 + &base("-2*rho*u1+rho^2"),
        &f1 + &base("-2*rho*u2+2*rho^2"),
        &f1 + &base("-2*rho*u3+3*rho^2"),
        &f1 + &base("2*rho*u1+2*rho*u2-8*rho*u3+29*rho^2"),
    ]} else {[
        f1.clone(),
        &f1 + &base("-2*u1+1"),
        &f1 + &base("-2*u2+2"),
        &f1 + &base("-2*u3+3"),
        f5_physical,
    ]};
    let depth = if profile == "FORMAL" { 4 } else { prefix_depth.unwrap_or(5) };
    let f: [MultivariatePolynomial<Q,u16>;5] = std::array::from_fn(|edge| {
        if edge < depth { physical[edge].clone() } else { base(&format!("s{}",edge+1)) }
    });
    let zero = base("0");
    let base_t_index = zero.get_vars_ref().iter()
        .position(|entry| *entry == PolyVariable::Symbol(sym("t"))).unwrap();
    let mut coefficients = std::array::from_fn::<_, 32, _>(|_| zero.clone());
    for term_index in 0..numerator.nterms() {
        let view = numerator.to_monomial_view(term_index);
        let mut mask = 0_usize;
        let mut exponent = vec![0_u16; zero.nvars()];
        exponent[base_t_index] = view.exponents[cover_t_index];
        let mut contribution = zero.monomial(view.coefficient.clone(), exponent);
        for edge in 0..5 {
            let power = view.exponents[cover_y_indices[edge]] as usize;
            if power % 2 == 1 { mask |= 1 << edge; }
            contribution = contribution * &f[edge].pow(power / 2);
        }
        coefficients[mask] = &coefficients[mask] + &contribution;
    }
    let rows = coefficients.iter().enumerate().map(|(mask, coefficient)| {
        let text = coefficient.to_string();
        let coefficient_lam_index = coefficient.get_vars_ref().iter()
            .position(|entry| *entry == PolyVariable::Symbol(sym("lam")));
        let lambda_zero = coefficient_lam_index
            .map(|index| coefficient.replace(index, &Q.zero()))
            .unwrap_or_else(|| coefficient.clone());
        let total_degrees = (0..coefficient.nterms()).map(|term|
            coefficient.exponents(term).iter().map(|entry| *entry as usize).sum::<usize>()
        ).collect::<Vec<_>>();
        let minimum_total_degree = total_degrees.iter().min().copied().unwrap_or(0);
        let maximum_total_degree = total_degrees.iter().max().copied().unwrap_or(0);
        let variable_index = |name: &str| coefficient.get_vars_ref().iter()
            .position(|entry| *entry == PolyVariable::Symbol(sym(name)));
        let t_index = variable_index("t");
        let u_indices = [variable_index("u1"), variable_index("u2"), variable_index("u3")];
        let t_degrees = (0..coefficient.nterms()).map(|term|
            t_index.map(|index| coefficient.exponents(term)[index] as usize).unwrap_or(0)
        ).collect::<Vec<_>>();
        let maximum_loop_degree = (0..coefficient.nterms()).map(|term|
            u_indices.iter().flatten().map(|index| coefficient.exponents(term)[*index] as usize).sum::<usize>()
        ).max().unwrap_or(0);
        let character_weight = mask.count_ones() as usize;
        let grading_rule_passes = (0..coefficient.nterms()).all(|term| {
            let t_degree = t_index.map(|index| coefficient.exponents(term)[index] as usize).unwrap_or(0);
            let loop_degree = u_indices.iter().flatten()
                .map(|index| coefficient.exponents(term)[*index] as usize).sum::<usize>();
            t_degree % 2 == character_weight % 2
                && t_degree + loop_degree <= 16 - character_weight
        });
        json!({
            "mask": mask,
            "character_sites": (0..5).filter(|edge| mask & (1 << edge) != 0)
                .map(|edge| edge + 1).collect::<Vec<_>>(),
            "nonzero": !coefficient.is_zero(),
            "term_count": coefficient.nterms(),
            "maximum_total_degree": maximum_total_degree,
            "minimum_total_degree": minimum_total_degree,
            "character_weight": character_weight,
            "minimum_t_degree": t_degrees.iter().min().copied().unwrap_or(0),
            "maximum_t_degree": t_degrees.iter().max().copied().unwrap_or(0),
            "maximum_loop_degree": maximum_loop_degree,
            "grading_rule_passes": grading_rule_passes,
            "homogeneous_degree_rule_passes": profile != "HOMOGENEOUS"
                || (minimum_total_degree == 16 - character_weight
                    && maximum_total_degree == 16 - character_weight),
            "lambda_adic_order": if coefficient.is_zero() { None } else {
                Some(coefficient_lam_index.map(|index| coefficient.degree_bounds(index).0 as usize).unwrap_or(0))
            },
            "lambda_zero_term_count": lambda_zero.nterms(),
            "serialized_characters": text.len(),
            "exact_coefficient_if_short": if text.len() <= 1000 { Some(text) } else { None }
        })
    }).collect::<Vec<_>>();
    let nonzero = coefficients.iter().filter(|coefficient| !coefficient.is_zero()).count();
    let total_terms = coefficients.iter().map(|coefficient| coefficient.nterms()).sum::<usize>();
    let all_grading_rules_pass = rows.iter().all(|row| row["grading_rule_passes"] == true);
    let all_homogeneous_degree_rules_pass = rows.iter()
        .all(|row| row["homogeneous_degree_rule_passes"] == true);
    let evaluation_checks = if profile == "A" {
        [(1009_i64,1_i64),(1009,2),(1013,1),(1013,2)]
            .into_iter().map(|(prime,seed)| evaluate_cover_sample(&numerator,&coefficients,prime,seed))
            .collect::<Vec<_>>()
    } else { Vec::new() };
    let all_evaluations_pass = evaluation_checks.iter().all(|row| row["passes"] == true);
    let packet = json!({
        "schema": "marici.benincasa.five_site.asymmetric_kummer_character_reduction.v1",
        "kinematic_profile": profile,
        "physical_prefix_depth": depth,
        "cover_relations": (0..5).map(|edge| if edge < depth {
            format!("y{}^2=F{}",edge+1,edge+1)
        } else {
            format!("y{}^2=s{} (formal)",edge+1,edge+1)
        }).collect::<Vec<_>>(),
        "F1": "2u1^2+2u2^2+u3^2-2u1u2-2u2u3",
        "external_gram_determinant": 1,
        "homogenizing_scale": if profile == "HOMOGENEOUS" { Some("rho") } else { None },
        "input_numerator_terms": numerator.nterms(),
        "input_numerator_fnv1a64": input_fingerprint,
        "nonzero_character_coefficients": nonzero,
        "total_reduced_coefficient_terms": total_terms,
        "all_character_grading_rules_pass": all_grading_rules_pass,
        "all_homogeneous_degree_rules_pass": all_homogeneous_degree_rules_pass,
        "character_grading_rule": "For character weight w, every monomial has deg_t congruent to w mod 2 and deg_t+deg_u <= 16-w.",
        "characters": rows,
        "independent_finite_field_evaluations": evaluation_checks,
        "all_independent_evaluations_pass": all_evaluations_pass,
        "completed": profile != "A" || all_evaluations_pass,
        "identity": "N16 mod (y_i^2-F_i) = sum_{S subset {1,...,5}} C_S(t,u) y_S",
        "scope": "Exact quotient-ring reduction; no de Rham or master-basis reduction."
    });
    let output = if profile == "A" {
        "../results/five-site-asymmetric-kummer-character-reduction.json"
    } else if profile == "B" {
        "../results/five-site-asymmetric-kummer-character-reduction-profile-b.json"
    } else if profile == "FAMILY" {
        "../results/five-site-asymmetric-kummer-character-reduction-family.json"
    } else if profile == "FORMAL" {
        "../results/five-site-asymmetric-kummer-character-reduction-formal-fifth.json"
    } else if profile == "HOMOGENEOUS" {
        "../results/five-site-asymmetric-kummer-character-reduction-homogeneous.json"
    } else {
        Box::leak(format!("../results/five-site-asymmetric-kummer-character-reduction-prefix-{}.json",depth).into_boxed_str())
    };
    fs::write(
        output,
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    ).unwrap();
    println!("nonzero_characters={nonzero} total_reduced_terms={total_terms}");
}

fn main() {
    std::thread::Builder::new().stack_size(512 * 1024 * 1024)
        .spawn(run).unwrap().join().unwrap();
}
