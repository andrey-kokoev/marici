//! Factor the exact C4 node Hessian polynomials derived occurrence-by-occurrence.
use serde_json::{json, Value};
use std::{fs, path::PathBuf};
use symbolica::prelude::*;

fn atom(text: &str) -> Atom {
    Atom::parse(text, "marici", Default::default()).unwrap().expand()
}

fn strip_ansi(text: String) -> String {
    let mut out = String::new();
    let mut chars = text.chars().peekable();
    while let Some(c) = chars.next() {
        if c == '\u{1b}' && chars.peek() == Some(&'[') {
            chars.next();
            while let Some(x) = chars.next() {
                if ('@'..='~').contains(&x) { break; }
            }
        } else { out.push(c); }
    }
    out
}

fn main() {
    let root = PathBuf::from(env!("CARGO_MANIFEST_DIR")).join("..");
    let source = root.join("results/four-cycle-node-hessian-polynomials.json");
    let output = root.join("results/four-cycle-node-hessian-factors.json");
    let mut packet: Value = serde_json::from_str(&fs::read_to_string(source).unwrap()).unwrap();
    let class_count = {
        let classes = packet["classes"].as_array_mut().unwrap();
        for class in classes.iter_mut() {
            let expression = class["normalized_hessian"].as_str().unwrap();
            let factored = strip_ansi(format!("{}", atom(expression).factor()));
            class["factorization"] = json!(factored);
        }
        classes.len()
    };
    packet["schema"] = json!("marici.benincasa.four_cycle_node_hessian_factors.v1");
    packet["engine"] = json!("Symbolica 2.2.0 exact characteristic-zero factorization");
    fs::write(output, serde_json::to_string_pretty(&packet).unwrap() + "\n").unwrap();
    println!("{}", json!({"classes": class_count, "records": packet["records"]}));
}
