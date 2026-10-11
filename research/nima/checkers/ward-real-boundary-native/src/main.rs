#[allow(dead_code)]
mod native {
    include!(concat!(env!("OUT_DIR"), "/native_source.rs"));

    fn fnv(bytes: &[u8]) -> String {
        let value = bytes.iter().fold(0xcbf29ce484222325u64, |h, b| {
            (h ^ u64::from(*b)).wrapping_mul(0x100000001b3)
        });
        format!("{value:016x}")
    }

    fn at_integer_point(polynomial: &Polynomial, a: Int) -> Polynomial {
        let mut value = 0;
        for (monomial, coefficient) in &polynomial.0 {
            let mut term = *coefficient;
            for (index, exponent) in monomial.0.iter().enumerate() {
                assert!(*exponent >= 0, "No Laurent input admitted to the tree test");
                let variable = if index == VAR_A { a }
                    else if index == VAR_D { 12 } else { index as Int + 2 };
                term *= variable.pow(*exponent as u32);
            }
            value += term;
        }
        Polynomial::constant(value)
    }

    fn point_gram(first: Vector, second: Vector, a: Int) -> GramSpace {
        let mut gram = GramSpace::new(first, second);
        for row in &mut gram.pairings {
            for entry in row { *entry = at_integer_point(entry, a); }
        }
        gram
    }

    fn constant_value(polynomial: &Polynomial) -> Int {
        assert!(polynomial.0.keys().all(|m| *m == Monomial::ONE));
        *polynomial.0.get(&Monomial::ONE).unwrap_or(&0)
    }

    pub fn boundary_probe_main() {
        let started_ns = std::time::SystemTime::now().duration_since(std::time::UNIX_EPOCH).unwrap().as_nanos();
        let output = std::path::Path::new(env!("CARGO_MANIFEST_DIR"))
            .join("../../results/ward-real-boundary-native.json");
        if output.exists() { std::fs::remove_file(&output).unwrap(); }
        assert_eq!((VERTICES, BASE_PRIMITIVES, TEST_VECTORS), (5, 7, 4));
        let words = patterns();
        let masks = spanning_tree_masks();
        assert_eq!((words.len(), masks.len()), (243, 12));
        let mut rows = Vec::new();
        let mut generic_nonzero = 0;
        let mut a_zero_only_nonzero = 0;
        for tree in masks {
            let open: Vec<_> = (0..6).filter(|slot| tree & (1 << slot) == 0).collect();
            assert_eq!(open.len(), 2);
            let closures = [open[0], open[1]];
            let first = edge_momentum(open[0]);
            let second = edge_momentum(open[1]);
            let actions = tree_actions(tree);
            assert!(actions.iter().all(|a| matches!(a, EdgeAction::Metric | EdgeAction::Open)));
            let tests = std::array::from_fn(test_vector);
            let mut terminals = Vec::new();
            terminals.extend(open_terminals(open[0], tests[0], tests[1]));
            terminals.extend(open_terminals(open[1], tests[2], tests[3]));

            // Rank-free envelope of the real collinear, transverse boundary.
            // Retain all polarization-polarization coordinates and all words.
            // Only pairings forced zero by this physical restriction are killed.
            let mut boundary = GramSpace::new(first, second);
            for i in 0..PRIMITIVES {
                for j in 0..PRIMITIVES {
                    if i < 4 || j < 4 { boundary.pairings[i][j] = Polynomial::default(); }
                }
            }
            for (word_index, word) in words.iter().enumerate() {
                let value = evaluate_sector(*word, actions, false, 1, &terminals, &boundary);
                assert_eq!(value, Polynomial::default(), "tree {tree}, word {word_index}: {word:?}");
            }
            let value = four_open_value(tree, closures, tests, &boundary, &words);
            assert_eq!(value, Polynomial::default(), "summed boundary tree {tree}");

            let generic = point_gram(first, second, 1);
            let generic_value = constant_value(&four_open_value(tree, closures, tests, &generic, &words));
            if generic_value != 0 { generic_nonzero += 1; }
            // This point does NOT impose physical reality/cross-transversality.
            let a_zero_only = point_gram(first, second, 0);
            let a_zero_value = constant_value(&four_open_value(tree, closures, tests, &a_zero_only, &words));
            if a_zero_value != 0 { a_zero_only_nonzero += 1; }
            rows.push(format!("{{\"mask\":{tree},\"open_slots\":[{},{}],\"zero_sectors\":243,\"boundary_value\":0,\"generic_value\":\"{generic_value}\",\"a_zero_only_value\":\"{a_zero_value}\"}}", open[0], open[1]));
        }
        assert!(generic_nonzero > 0, "Nonvacuity control failed");
        let native_source = include_str!(concat!(env!("OUT_DIR"), "/native_source.rs"));
        let result = format!(concat!(
            "{{\"schema\":\"marici.nima.ward-real-boundary-native.v1\",\"status\":\"pass\",",
            "\"tree_count\":12,\"tested_sectors\":2916,\"boundary_nonzero_sectors\":0,\"started_ns\":\"{}\",", 
            "\"generic_nonzero_trees\":{},\"a_zero_only_nonzero_trees\":{},\"trees\":[{}],",
            "\"compiled_fnv1a64\":{{\"native_included\":\"{}\",\"main.rs\":\"{}\",\"build.rs\":\"{}\",\"Cargo.toml\":\"{}\"}}}}\n"
        ), started_ns, generic_nonzero, a_zero_only_nonzero, rows.join(","),
            fnv(native_source.as_bytes()), fnv(include_bytes!("main.rs")),
            fnv(include_bytes!("../build.rs")), fnv(include_bytes!("../Cargo.toml")));
        std::fs::create_dir_all(output.parent().unwrap()).unwrap();
        std::fs::write(output, &result).unwrap();
        println!("{result}");
    }
}

fn main() { native::boundary_probe_main(); }
