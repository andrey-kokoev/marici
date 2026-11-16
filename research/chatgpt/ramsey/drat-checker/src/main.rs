//! Small text-DIMACS/text-DRAT frontend to the independent dratify checker.
use std::{env, fs::File, io::{BufRead, BufReader}, time::Instant};
use dratify::{Checker, Lit};

fn literal(value: i64) -> Lit {
    assert!(value != 0 && value.unsigned_abs() <= u32::MAX as u64 / 2);
    ((value.unsigned_abs() as u32 - 1) * 2) + u32::from(value < 0)
}

fn main() {
    let args: Vec<_> = env::args().collect();
    assert_eq!(args.len(), 3, "usage: ramsey-drat-checker formula.cnf proof.drat");
    let started = Instant::now();
    let mut header = None;
    let mut clauses = Vec::new();
    let mut pending = Vec::new();
    for line in BufReader::new(File::open(&args[1]).unwrap()).lines() {
        let line = line.unwrap();
        let text = line.trim();
        if text.is_empty() || text.starts_with('c') { continue; }
        if text.starts_with('p') {
            let words: Vec<_> = text.split_whitespace().collect();
            assert!(header.is_none() && words.len() == 4 && words[1] == "cnf");
            header = Some((words[2].parse::<u32>().unwrap(), words[3].parse::<usize>().unwrap()));
            continue;
        }
        let (vars, _) = header.expect("missing DIMACS header");
        for token in text.split_whitespace() {
            let value = token.parse::<i64>().unwrap();
            if value == 0 { clauses.push(std::mem::take(&mut pending)); }
            else {
                assert!(value.unsigned_abs() <= vars as u64);
                pending.push(literal(value));
            }
        }
    }
    let (vars, count) = header.expect("missing DIMACS header");
    assert!(pending.is_empty() && clauses.len() == count);
    let mut checker = Checker::new(vars, &clauses, true, true);
    let mut steps = 0u64;
    let mut derived_empty = false;
    for (index, line) in BufReader::new(File::open(&args[2]).unwrap()).lines().enumerate() {
        let line = line.unwrap();
        let text = line.trim();
        if text.is_empty() || text.starts_with('c') { continue; }
        let mut words: Vec<_> = text.split_whitespace().collect();
        let deletion = words[0] == "d";
        if deletion { words.remove(0); }
        assert_eq!(words.pop(), Some("0"), "unterminated proof clause at {}", index + 1);
        let clause: Vec<Lit> = words.iter().map(|w| literal(w.parse::<i64>().unwrap())).collect();
        assert!(checker.check_step(deletion, &clause), "invalid DRAT step at line {}", index + 1);
        steps += 1;
        if !deletion && clause.is_empty() { derived_empty = true; }
    }
    assert!(derived_empty, "proof did not derive the empty clause");
    println!("VERIFIED UNSAT: {} input clauses, {} checked proof steps; dratify 0.1.11; {:.3}s", count, steps, started.elapsed().as_secs_f64());
}
