use std::{env, fs, path::PathBuf};

fn main() {
    let source = PathBuf::from(env::var("CARGO_MANIFEST_DIR").unwrap())
        .join("../../check_two_open_pair_ward_naturality.rs");
    println!("cargo:rerun-if-changed={}", source.display());
    let text = fs::read_to_string(source).unwrap();
    // include! cannot import inner documentation comments into this module.
    // No executable source line is modified; the original main stays unused.
    let included = text.lines().map(|line| {
        line.strip_prefix("//!").map_or_else(|| line.to_owned(), |tail| format!("//{tail}"))
    }).collect::<Vec<_>>().join("\n") + "\n";
    fs::write(PathBuf::from(env::var("OUT_DIR").unwrap()).join("native_source.rs"), included).unwrap();
}
