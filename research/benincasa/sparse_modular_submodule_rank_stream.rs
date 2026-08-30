//! Sparse ranks of three relation modules and three declared submodules.
//!
//! Kinds 0..2 add relation rows.  After those rows are complete, kinds 3..5
//! are reduced against the corresponding relation module and span the image
//! of a declared source lattice.

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
    while exponent > 0 {
        if exponent & 1 == 1 {
            result = result * base % modulus;
        }
        base = base * base % modulus;
        exponent >>= 1;
    }
    result as u32
}

fn subtract_scaled(row: &mut Row, pivot_row: &Row, scale: u32, prime: u32) {
    let modulus = prime as u64;
    for (&column, &value) in pivot_row {
        let old = row.get(&column).copied().unwrap_or(0) as u64;
        let decrement = scale as u64 * value as u64 % modulus;
        let next = (old + modulus - decrement) % modulus;
        if next == 0 {
            row.remove(&column);
        } else {
            row.insert(column, next as u32);
        }
    }
}

fn reduce_row(mut row: Row, pivots: &Pivots, prime: u32) -> Row {
    loop {
        let Some((&pivot, &coefficient)) = row.last_key_value() else {
            return row;
        };
        let Some(pivot_row) = pivots.get(&pivot) else {
            return row;
        };
        subtract_scaled(&mut row, pivot_row, coefficient, prime);
    }
}

fn add_pivot(row: Row, pivots: &mut Pivots, prime: u32) {
    let mut row = reduce_row(row, pivots, prime);
    let Some((&pivot, &coefficient)) = row.last_key_value() else {
        return;
    };
    let inverse = mod_pow(coefficient as u64, (prime - 2) as u64, prime as u64);
    if inverse != 1 {
        for value in row.values_mut() {
            *value = (*value as u64 * inverse as u64 % prime as u64) as u32;
        }
    }
    pivots.insert(pivot, row);
}

fn main() {
    let mut bytes = Vec::new();
    io::stdin().read_to_end(&mut bytes).unwrap();
    let mut cursor = 0;
    let prime = read_u32(&bytes, &mut cursor);
    let mut relations: Vec<Pivots> = (0..3).map(|_| HashMap::new()).collect();
    let mut images: Vec<Pivots> = (0..3).map(|_| HashMap::new()).collect();
    let mut relation_rows = [0_u64; 3];
    let mut source_rows = [0_u64; 3];
    while cursor < bytes.len() {
        let kind = bytes[cursor] as usize;
        cursor += 1;
        let length = read_u32(&bytes, &mut cursor) as usize;
        let mut row = Row::new();
        for _ in 0..length {
            let column = read_u32(&bytes, &mut cursor);
            let value = read_u32(&bytes, &mut cursor) % prime;
            if value != 0 {
                row.insert(column, value);
            }
        }
        if kind < 3 {
            relation_rows[kind] += 1;
            add_pivot(row, &mut relations[kind], prime);
        } else {
            let index = kind - 3;
            assert!(index < 3);
            source_rows[index] += 1;
            let reduced = reduce_row(row, &relations[index], prime);
            add_pivot(reduced, &mut images[index], prime);
        }
    }
    println!(
        "{{\"schema\":\"marici.benincasa.sparse-modular-submodule-rank-stream.v1\",\"prime\":{},\"relation_rows\":[{},{},{}],\"relation_ranks\":[{},{},{}],\"source_rows\":[{},{},{}],\"source_image_ranks\":[{},{},{}]}}",
        prime,
        relation_rows[0], relation_rows[1], relation_rows[2],
        relations[0].len(), relations[1].len(), relations[2].len(),
        source_rows[0], source_rows[1], source_rows[2],
        images[0].len(), images[1].len(), images[2].len(),
    );
}
