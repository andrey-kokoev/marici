use std::collections::BTreeMap;
use std::env;
use std::fs::File;
use std::io::{self, Read};

const P: u32 = 32003;
type Row = BTreeMap<usize, u32>;

fn mul(a: u32, b: u32) -> u32 { ((a as u64 * b as u64) % P as u64) as u32 }
fn pow(mut a: u32, mut n: u32) -> u32 {
    let mut out = 1;
    while n > 0 { if n & 1 == 1 { out = mul(out, a); } a = mul(a, a); n >>= 1; }
    out
}
fn add_value(row: &mut Row, column: usize, value: u32) {
    let next = (row.get(&column).copied().unwrap_or(0) + value) % P;
    if next == 0 { row.remove(&column); } else { row.insert(column, next); }
}
fn insert(mut row: Row, pivots: &mut [Option<Row>]) -> bool {
    loop {
        let Some((&pivot, &coefficient)) = row.last_key_value() else { return false; };
        if let Some(existing) = &pivots[pivot] {
            let terms: Vec<(usize, u32)> = existing.iter().map(|(&c, &v)| (c, v)).collect();
            for (column, value) in terms {
                add_value(&mut row, column, (P - mul(coefficient, value)) % P);
            }
        } else {
            let inverse = pow(coefficient, P - 2);
            for value in row.values_mut() { *value = mul(*value, inverse); }
            pivots[pivot] = Some(row);
            return true;
        }
    }
}
fn u32_at(bytes: &[u8], cursor: &mut usize) -> u32 {
    let out = u32::from_le_bytes(bytes[*cursor..*cursor + 4].try_into().unwrap());
    *cursor += 4;
    out
}
fn row_at(bytes: &[u8], cursor: &mut usize) -> Row {
    let count = u32_at(bytes, cursor) as usize;
    let mut row = Row::new();
    for _ in 0..count {
        row.insert(u32_at(bytes, cursor) as usize, u32_at(bytes, cursor));
    }
    row
}
fn main() -> io::Result<()> {
    let path = env::args().nth(1).expect("usage: triangle_wall_dual_rank <packet>");
    let mut bytes = Vec::new();
    File::open(path)?.read_to_end(&mut bytes)?;
    let version = &bytes[..8];
    assert!(version == b"MRCIDR02" || version == b"MRCIDR03");
    let mut cursor = 8;
    assert_eq!(u32_at(&bytes, &mut cursor), P);
    let ambient = u32_at(&bytes, &mut cursor);
    let columns = u32_at(&bytes, &mut cursor) as usize;
    let rows = u32_at(&bytes, &mut cursor) as usize;
    let central_rank = u32_at(&bytes, &mut cursor) as usize;
    let mut dual_pivots: Vec<Option<Row>> = vec![None; 2 * columns];
    let mut triple_pivots: Vec<Option<Row>> = vec![None; 3 * columns];
    let mut central_pivots: Vec<Option<Row>> = vec![None; columns];
    let mut dual_rank = 0usize;
    let mut triple_rank = 0usize;
    let mut cumulative = Vec::new();
    let mut active_family = 0u32;
    for _ in 0..rows {
        let family = if version == b"MRCIDR03" { u32_at(&bytes, &mut cursor) } else { 0 };
        if family != active_family {
            cumulative.push((active_family, central_pivots.iter().flatten().count(), dual_rank, triple_rank));
            active_family = family;
        }
        let central = row_at(&bytes, &mut cursor);
        let derivative = row_at(&bytes, &mut cursor);
        let second = row_at(&bytes, &mut cursor);
        insert(central.clone(), &mut central_pivots);
        let mut first = central.clone();
        for (column, value) in derivative { add_value(&mut first, columns + column, value); }
        dual_rank += insert(first.clone(), &mut dual_pivots) as usize;
        dual_rank += insert(central.iter().map(|(&column, &value)| (columns + column, value)).collect(), &mut dual_pivots) as usize;

        let mut grade_zero = central.clone();
        for (&column, &value) in first.iter().filter(|(column, _)| **column >= columns) {
            add_value(&mut grade_zero, column, value);
        }
        for (column, value) in second { add_value(&mut grade_zero, 2 * columns + column, value); }
        let mut grade_one: Row = central.iter().map(|(&column, &value)| (columns + column, value)).collect();
        for (&column, &value) in first.iter().filter(|(column, _)| **column >= columns) {
            add_value(&mut grade_one, columns + column, value);
        }
        let grade_two: Row = central.into_iter().map(|(column, value)| (2 * columns + column, value)).collect();
        triple_rank += insert(grade_zero, &mut triple_pivots) as usize;
        triple_rank += insert(grade_one, &mut triple_pivots) as usize;
        triple_rank += insert(grade_two, &mut triple_pivots) as usize;
    }
    cumulative.push((active_family, central_pivots.iter().flatten().count(), dual_rank, triple_rank));
    let first_normal = dual_rank - 2 * central_rank;
    let second_normal = triple_rank - 3 * central_rank - 2 * first_normal;
    let family_json = cumulative.iter().map(|(family, central, dual, triple)| {
        let first = dual - 2 * central;
        let second = triple - 3 * central - 2 * first;
        format!("{{\"family_through\":{family},\"central_rank\":{central},\"first_normal_rank\":{first},\"second_normal_rank\":{second}}}")
    }).collect::<Vec<_>>().join(",");
    println!("{{\"schema\":\"marici.triangle-wall-jet-rank-rust.v3\",\"ambient_relation_degree\":{ambient},\"column_count\":{columns},\"raw_relation_row_count\":{rows},\"central_relation_rank\":{central_rank},\"dual_block_rank\":{dual_rank},\"first_normal_rank\":{first_normal},\"triple_block_rank\":{triple_rank},\"second_normal_rank\":{second_normal},\"family_filtration\":[{family_json}]}}");
    Ok(())
}
