use serde_json::{json, Value};
use std::{collections::BTreeSet, fs, sync::Arc};
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

fn cut_support(label: &str) -> Vec<usize> {
    let sites = label.strip_prefix("g_").unwrap().chars()
        .map(|digit| digit.to_digit(10).unwrap() as usize - 1)
        .collect::<BTreeSet<_>>();
    (0..5).filter(|edge|
        sites.contains(edge) != sites.contains(&((edge + 1) % 5))
    ).collect()
}

fn denominator(label: &str) -> String {
    if label == "G" { return "5*t".to_owned(); }
    if let Some(edge) = label.strip_prefix("G_minus_e") {
        let index = edge.chars().next().unwrap().to_digit(10).unwrap() as usize - 1;
        return format!("5*t+2*y{}", index + 1);
    }
    let size = label.strip_prefix("g_").unwrap().len();
    let cuts = cut_support(label);
    assert_eq!(cuts.len(), 2);
    format!("{size}*t+y{}+y{}", cuts[0] + 1, cuts[1] + 1)
}

fn run() {
    let source: Value = serde_json::from_str(
        &fs::read_to_string("../results/five-cycle-ofpt-packet.json").unwrap()
    ).unwrap();
    let cycle = &source["five_cycle"];
    let common = cycle["common_prefactor"].as_array().unwrap().iter()
        .map(|entry| entry.as_str().unwrap().to_owned()).collect::<Vec<_>>();
    assert_eq!(common.len(), 6);
    let terms = cycle["terms"].as_array().unwrap();
    assert_eq!(terms.len(), 180);
    let candidates = terms.iter().flat_map(|term| term.as_array().unwrap().iter())
        .map(|entry| entry.as_str().unwrap().to_owned())
        .collect::<BTreeSet<_>>();
    assert_eq!(candidates.len(), 20);

    let order = Arc::new(vec![
        PolyVariable::Symbol(sym("t")),
        PolyVariable::Symbol(sym("y1")),
        PolyVariable::Symbol(sym("y2")),
        PolyVariable::Symbol(sym("y3")),
        PolyVariable::Symbol(sym("y4")),
        PolyVariable::Symbol(sym("y5")),
    ]);
    let polynomial = |text: &str| -> MultivariatePolynomial<Q, u16> {
        Atom::parse(text, "marici", Default::default()).unwrap()
            .expand().to_polynomial(&Q, Some(order.clone()))
    };
    let mut numerator = polynomial("0");
    for term in terms {
        let selected = term.as_array().unwrap().iter()
            .map(|entry| entry.as_str().unwrap()).collect::<BTreeSet<_>>();
        let complement_product = candidates.iter()
            .filter(|label| !selected.contains(label.as_str()))
            .fold(polynomial("1"), |product, label| product * &polynomial(&denominator(label)));
        numerator = &numerator + &complement_product;
    }
    let numerator_text = numerator.to_string();
    let denominator_labels = common.iter().cloned()
        .chain(candidates.iter().cloned()).collect::<Vec<_>>();
    let cancelled_carrier_factors = denominator_labels.iter()
        .filter(|label| numerator.try_div(&polynomial(&denominator(label))).is_some())
        .cloned().collect::<Vec<_>>();
    let maximum_total_degree = (0..numerator.nterms()).map(|term|
        numerator.exponents(term).iter().map(|entry| *entry as usize).sum::<usize>()
    ).max().unwrap_or(0);
    let full_denominator = denominator_labels.iter()
        .map(|label| format!("({})", denominator(label)))
        .collect::<Vec<_>>().join("*");
    let packet = json!({
        "schema": "marici.benincasa.five_site.asymmetric_canonical_sum.v1",
        "source_terms": 180,
        "common_denominators": common,
        "supplement_denominators": candidates,
        "common_prefactor_degree": 6,
        "supplement_lcm_degree": 20,
        "full_denominator_degree": 26,
        "combined_numerator_expected_degree": 16,
        "combined_numerator_total_degree": maximum_total_degree,
        "combined_numerator_term_count": numerator.nterms(),
        "combined_numerator_fnv1a64": fnv1a64(&numerator_text),
        "combined_numerator": numerator_text,
        "full_denominator_unexpanded": full_denominator,
        "denominator_labels": denominator_labels,
        "cancelled_carrier_factors": cancelled_carrier_factors,
        "identity": "Omega_C5 = combined_numerator / full_denominator",
        "normalization": "Entry 1250 source Eq.33 unit weights",
        "factorization_status": "deferred; exact carrier-factor divisibility is a separate specialization audit"
    });
    fs::write(
        "../results/five-site-asymmetric-canonical-sum.json",
        serde_json::to_string_pretty(&packet).unwrap() + "\n",
    ).unwrap();
    println!("numerator_chars={}", numerator_text.len());
}

fn main() {
    std::thread::Builder::new().stack_size(512 * 1024 * 1024)
        .spawn(run).unwrap().join().unwrap();
}
