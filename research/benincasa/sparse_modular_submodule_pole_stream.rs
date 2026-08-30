//! Three-grade source lattice and normal-pole audit.
//!
//! Kinds 0..2 are relations, 3..5 are source images, and each following
//! block of three kinds is one test family reduced modulo both.

use std::collections::{BTreeMap, HashMap};
use std::convert::TryInto;
use std::io::{self, Read};

type Row = BTreeMap<u32, u32>;
type Pivots = HashMap<u32, Row>;

fn read_u32(bytes: &[u8], cursor: &mut usize) -> u32 {
    let end = *cursor + 4;
    assert!(end <= bytes.len());
    let value = u32::from_le_bytes(bytes[*cursor..end].try_into().unwrap());
    *cursor = end;
    value
}
fn mod_pow(mut base: u64, mut exponent: u64, modulus: u64) -> u32 {
    let mut result = 1_u64;
    while exponent > 0 { if exponent & 1 == 1 { result = result * base % modulus; } base = base * base % modulus; exponent >>= 1; }
    result as u32
}
fn subtract_scaled(row: &mut Row, pivot_row: &Row, scale: u32, prime: u32) {
    let modulus = prime as u64;
    for (&column, &value) in pivot_row {
        let old = row.get(&column).copied().unwrap_or(0) as u64;
        let next = (old + modulus - scale as u64 * value as u64 % modulus) % modulus;
        if next == 0 { row.remove(&column); } else { row.insert(column, next as u32); }
    }
}
fn reduce_row(mut row: Row, pivots: &Pivots, prime: u32) -> Row {
    loop {
        let Some((&pivot, &coefficient)) = row.last_key_value() else { return row; };
        let Some(pivot_row) = pivots.get(&pivot) else { return row; };
        subtract_scaled(&mut row, pivot_row, coefficient, prime);
    }
}
fn add_pivot(row: Row, pivots: &mut Pivots, prime: u32) -> bool {
    let mut row = reduce_row(row, pivots, prime);
    let Some((&pivot, &coefficient)) = row.last_key_value() else { return false; };
    let inverse = mod_pow(coefficient as u64, (prime - 2) as u64, prime as u64);
    for value in row.values_mut() { *value = (*value as u64 * inverse as u64 % prime as u64) as u32; }
    pivots.insert(pivot, row);
    true
}

fn main() {
    let mut bytes = Vec::new(); io::stdin().read_to_end(&mut bytes).unwrap();
    let mut cursor = 0; let prime = read_u32(&bytes, &mut cursor);
    let mut relations: Vec<Pivots> = (0..3).map(|_| HashMap::new()).collect();
    let mut images: Vec<Pivots> = (0..3).map(|_| HashMap::new()).collect();
    let mut tests: Vec<Vec<Pivots>> = (0..3).map(|_| (0..3).map(|_| HashMap::new()).collect()).collect();
    let mut rows = vec![[0_u64; 3]; 5];
    while cursor < bytes.len() {
        let kind = bytes[cursor] as usize; cursor += 1;
        let length = read_u32(&bytes, &mut cursor) as usize;
        let mut row = Row::new();
        for _ in 0..length {
            let column = read_u32(&bytes, &mut cursor);
            let value = read_u32(&bytes, &mut cursor) % prime;
            if value != 0 { row.insert(column, value); }
        }
        let class = kind / 3; let grade = kind % 3;
        assert!(class < 5); rows[class][grade] += 1;
        if class == 0 { add_pivot(row, &mut relations[grade], prime); }
        else {
            let reduced = reduce_row(row, &relations[grade], prime);
            if class == 1 { add_pivot(reduced, &mut images[grade], prime); }
            else {
                let reduced = reduce_row(reduced, &images[grade], prime);
                add_pivot(reduced, &mut tests[class - 2][grade], prime);
            }
        }
    }
    println!("{{\"schema\":\"marici.benincasa.sparse-modular-submodule-pole-stream.v1\",\"prime\":{},\"relation_ranks\":[{},{},{}],\"source_image_ranks\":[{},{},{}],\"test_extension_ranks\":[[{},{},{}],[{},{},{}],[{},{},{}]]}}",
        prime,
        relations[0].len(),relations[1].len(),relations[2].len(),
        images[0].len(),images[1].len(),images[2].len(),
        tests[0][0].len(),tests[0][1].len(),tests[0][2].len(),
        tests[1][0].len(),tests[1][1].len(),tests[1][2].len(),
        tests[2][0].len(),tests[2][1].len(),tests[2][2].len());
}
