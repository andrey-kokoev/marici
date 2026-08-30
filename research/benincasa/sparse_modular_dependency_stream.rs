//! Sparse quotient-rank engine retaining dependencies among ordered test rows.

use std::collections::{BTreeMap, HashMap};
use std::convert::TryInto;
use std::io::{self, Read};

type Row = BTreeMap<u32, u32>;

#[derive(Clone)]
struct Tagged {
    row: Row,
    provenance: Row,
}

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
        if exponent & 1 == 1 { result = result * base % modulus; }
        base = base * base % modulus;
        exponent >>= 1;
    }
    result as u32
}

fn subtract_scaled(row: &mut Row, pivot: &Row, scale: u32, prime: u32) {
    let modulus = prime as u64;
    for (&column, &value) in pivot {
        let old = row.get(&column).copied().unwrap_or(0) as u64;
        let decrement = scale as u64 * value as u64 % modulus;
        let next = (old + modulus - decrement) % modulus;
        if next == 0 { row.remove(&column); } else { row.insert(column, next as u32); }
    }
}

fn reduce_plain(mut row: Row, pivots: &HashMap<u32, Row>, prime: u32) -> Row {
    loop {
        let Some((&pivot, &coefficient)) = row.last_key_value() else { return row; };
        let Some(pivot_row) = pivots.get(&pivot) else { return row; };
        subtract_scaled(&mut row, pivot_row, coefficient, prime);
    }
}

fn add_plain(row: Row, pivots: &mut HashMap<u32, Row>, prime: u32) {
    let mut row = reduce_plain(row, pivots, prime);
    let Some((&pivot, &coefficient)) = row.last_key_value() else { return; };
    let inverse = mod_pow(coefficient as u64, (prime - 2) as u64, prime as u64);
    for value in row.values_mut() {
        *value = (*value as u64 * inverse as u64 % prime as u64) as u32;
    }
    pivots.insert(pivot, row);
}

fn reduce_tagged(mut item: Tagged, pivots: &HashMap<u32, Tagged>, prime: u32) -> Tagged {
    loop {
        let Some((&pivot, &coefficient)) = item.row.last_key_value() else { return item; };
        let Some(pivot_item) = pivots.get(&pivot) else { return item; };
        subtract_scaled(&mut item.row, &pivot_item.row, coefficient, prime);
        subtract_scaled(&mut item.provenance, &pivot_item.provenance, coefficient, prime);
    }
}

fn json_row(row: &Row) -> String {
    let entries: Vec<String> = row.iter().map(|(i, v)| format!("[{},{}]", i, v)).collect();
    format!("[{}]", entries.join(","))
}

fn main() {
    let mut bytes = Vec::new();
    io::stdin().read_to_end(&mut bytes).unwrap();
    let mut cursor = 0;
    let prime = read_u32(&bytes, &mut cursor);
    let mut relations: HashMap<u32, Row> = HashMap::new();
    let mut tests: HashMap<u32, Tagged> = HashMap::new();
    let mut dependencies: Vec<Row> = Vec::new();
    let mut relation_rows = 0_u64;
    let mut test_rows = 0_u32;
    while cursor < bytes.len() {
        let kind = bytes[cursor];
        cursor += 1;
        let length = read_u32(&bytes, &mut cursor) as usize;
        let mut row = Row::new();
        for _ in 0..length {
            let column = read_u32(&bytes, &mut cursor);
            let value = read_u32(&bytes, &mut cursor) % prime;
            if value != 0 { row.insert(column, value); }
        }
        match kind {
            0 => {
                relation_rows += 1;
                add_plain(row, &mut relations, prime);
            }
            4 => {
                let mut provenance = Row::new();
                provenance.insert(test_rows, 1);
                test_rows += 1;
                let row = reduce_plain(row, &relations, prime);
                let mut item = reduce_tagged(Tagged { row, provenance }, &tests, prime);
                if item.row.is_empty() {
                    dependencies.push(item.provenance);
                } else {
                    let (&pivot, &coefficient) = item.row.last_key_value().unwrap();
                    let inverse = mod_pow(coefficient as u64, (prime - 2) as u64, prime as u64);
                    for value in item.row.values_mut() {
                        *value = (*value as u64 * inverse as u64 % prime as u64) as u32;
                    }
                    for value in item.provenance.values_mut() {
                        *value = (*value as u64 * inverse as u64 % prime as u64) as u32;
                    }
                    tests.insert(pivot, item);
                }
            }
            _ => panic!("unsupported row kind {}", kind),
        }
    }
    let deps: Vec<String> = dependencies.iter().map(json_row).collect();
    println!(
        "{{\"schema\":\"marici.benincasa.sparse-modular-dependency-stream.v1\",\"prime\":{},\"relation_rows\":{},\"relation_rank\":{},\"test_rows\":{},\"test_rank\":{},\"dependencies\":[{}]}}",
        prime, relation_rows, relations.len(), test_rows, tests.len(), deps.join(",")
    );
}
