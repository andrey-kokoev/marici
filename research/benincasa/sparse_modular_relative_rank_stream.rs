//! Sparse rank engine with a declared low/high column decomposition.
//!
//! Input: prime:u32, three low-column limits:u32, then records
//! `(kind:u8, length:u32, (column:u32, value:u32)^length)` for kinds 0..2.
//! Callers must order every high column above every low column.  A pivot below
//! the declared limit is therefore a relation in `R cap L`, not merely a
//! projection of a relation to `L`.

use std::collections::{BTreeMap, HashMap};
use std::convert::TryInto;
use std::io::{self, Read};

type Row = BTreeMap<u32, u32>;
type Pivots = HashMap<u32, Row>;

fn read_u32(bytes: &[u8], cursor: &mut usize) -> u32 {
    let end = *cursor + 4;
    assert!(end <= bytes.len(), "truncated u32 in relative rank stream");
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

fn add_pivot(mut row: Row, pivots: &mut Pivots, prime: u32) {
    loop {
        let Some((&pivot, &coefficient)) = row.last_key_value() else {
            return;
        };
        if let Some(pivot_row) = pivots.get(&pivot) {
            subtract_scaled(&mut row, pivot_row, coefficient, prime);
            continue;
        }
        let inverse = mod_pow(coefficient as u64, (prime - 2) as u64, prime as u64);
        if inverse != 1 {
            for value in row.values_mut() {
                *value = (*value as u64 * inverse as u64 % prime as u64) as u32;
            }
        }
        assert_eq!(row.get(&pivot), Some(&1));
        pivots.insert(pivot, row);
        return;
    }
}

fn main() {
    let mut bytes = Vec::new();
    io::stdin().read_to_end(&mut bytes).unwrap();
    let mut cursor = 0;
    let prime = read_u32(&bytes, &mut cursor);
    let low_limits = [
        read_u32(&bytes, &mut cursor),
        read_u32(&bytes, &mut cursor),
        read_u32(&bytes, &mut cursor),
    ];
    let mut pivots: Vec<Pivots> = (0..3).map(|_| HashMap::new()).collect();
    let mut row_counts = [0_u64; 3];
    while cursor < bytes.len() {
        let kind = bytes[cursor] as usize;
        cursor += 1;
        assert!(kind < 3);
        let length = read_u32(&bytes, &mut cursor) as usize;
        let mut row = Row::new();
        for _ in 0..length {
            let column = read_u32(&bytes, &mut cursor);
            let value = read_u32(&bytes, &mut cursor) % prime;
            if value != 0 {
                row.insert(column, value);
            }
        }
        row_counts[kind] += 1;
        add_pivot(row, &mut pivots[kind], prime);
    }
    let ranks = [pivots[0].len(), pivots[1].len(), pivots[2].len()];
    let low_ranks = [
        pivots[0].keys().filter(|&&pivot| pivot < low_limits[0]).count(),
        pivots[1].keys().filter(|&&pivot| pivot < low_limits[1]).count(),
        pivots[2].keys().filter(|&&pivot| pivot < low_limits[2]).count(),
    ];
    println!(
        "{{\"schema\":\"marici.benincasa.sparse-modular-relative-rank-stream.v1\",\"prime\":{},\"row_counts\":[{},{},{}],\"ranks\":[{},{},{}],\"low_limits\":[{},{},{}],\"low_intersection_ranks\":[{},{},{}]}}",
        prime,
        row_counts[0], row_counts[1], row_counts[2],
        ranks[0], ranks[1], ranks[2],
        low_limits[0], low_limits[1], low_limits[2],
        low_ranks[0], low_ranks[1], low_ranks[2],
    );
}
