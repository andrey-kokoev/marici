//! Streaming sparse row reduction over a prime field.
//!
//! Binary protocol (little endian): prime:u32, followed by records
//! `(kind:u8, length:u32, (column:u32, value:u32)^length)`.
//! Kinds 0,1,2 feed independent special/dual/triple relation modules.
//! Kinds 3,4,5 are reduced against the completed kind-2 module and measure
//! the ranks of three declared source images.

use std::collections::{BTreeMap, HashMap};
use std::convert::TryInto;
use std::io::{self, Read};

type Row = BTreeMap<u32, u32>;
type Pivots = HashMap<u32, Row>;

fn read_u32(bytes: &[u8], cursor: &mut usize) -> u32 {
    let end = *cursor + 4;
    assert!(end <= bytes.len(), "truncated u32 in rank stream");
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
    assert_eq!(row.get(&pivot), Some(&1));
    pivots.insert(pivot, row);
}

fn main() {
    let mut bytes = Vec::new();
    io::stdin().read_to_end(&mut bytes).unwrap();
    let mut cursor = 0;
    let prime = read_u32(&bytes, &mut cursor);
    assert!(prime > 2);

    let mut relation_pivots: Vec<Pivots> = (0..3).map(|_| HashMap::new()).collect();
    let mut image_pivots: Vec<Pivots> = (0..3).map(|_| HashMap::new()).collect();
    let mut relation_rows = [0_u64; 3];
    let mut image_rows = [0_u64; 3];

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
            add_pivot(row, &mut relation_pivots[kind], prime);
        } else {
            let image = kind - 3;
            assert!(image < 3, "unknown rank-stream record kind");
            image_rows[image] += 1;
            let reduced = reduce_row(row, &relation_pivots[2], prime);
            add_pivot(reduced, &mut image_pivots[image], prime);
        }
    }

    println!(
        "{{\"schema\":\"marici.benincasa.sparse-modular-rank-stream.v1\",\"prime\":{},\"relation_rows\":[{},{},{}],\"relation_ranks\":[{},{},{}],\"image_rows\":[{},{},{}],\"image_ranks\":[{},{},{}]}}",
        prime,
        relation_rows[0], relation_rows[1], relation_rows[2],
        relation_pivots[0].len(), relation_pivots[1].len(), relation_pivots[2].len(),
        image_rows[0], image_rows[1], image_rows[2],
        image_pivots[0].len(), image_pivots[1].len(), image_pivots[2].len(),
    );
}
