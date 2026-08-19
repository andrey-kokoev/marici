use std::collections::BTreeMap;
use std::env;
use std::fs::File;
use std::io::{self, Read, Write};

const P: u32 = 32003;
type Row = BTreeMap<usize, u32>;
type Provenance = BTreeMap<usize, u32>;

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
fn insert_tracked(
    mut row: Row,
    mut provenance: Provenance,
    pivots: &mut [Option<(Row, Provenance)>],
) -> Option<(usize, Provenance)> {
    loop {
        let Some((&pivot, &coefficient)) = row.last_key_value() else { return None; };
        if let Some((existing, existing_provenance)) = &pivots[pivot] {
            let terms: Vec<(usize, u32)> = existing.iter().map(|(&c, &v)| (c, v)).collect();
            let provenance_terms: Vec<(usize, u32)> = existing_provenance.iter().map(|(&c, &v)| (c, v)).collect();
            for (column, value) in terms {
                add_value(&mut row, column, (P - mul(coefficient, value)) % P);
            }
            for (source, value) in provenance_terms {
                add_value(&mut provenance, source, (P - mul(coefficient, value)) % P);
            }
        } else {
            let inverse = pow(coefficient, P - 2);
            for value in row.values_mut() { *value = mul(*value, inverse); }
            for value in provenance.values_mut() { *value = mul(*value, inverse); }
            let result = provenance.clone();
            pivots[pivot] = Some((row, provenance));
            return Some((pivot, result));
        }
    }
}
fn shifted(row: &Row, offset: usize) -> Row {
    row.iter().map(|(&column, &value)| (offset + column, value)).collect()
}
fn reduce(mut row: Row, pivots: &[Option<Row>]) -> Row {
    loop {
        let Some(pivot) = row.keys().rev().find(|&&column| pivots[column].is_some()).copied() else { return row; };
        let coefficient = row[&pivot];
        let existing = pivots[pivot].as_ref().unwrap();
        let terms: Vec<(usize, u32)> = existing.iter().map(|(&c, &v)| (c, v)).collect();
        for (column, value) in terms {
            add_value(&mut row, column, (P - mul(coefficient, value)) % P);
        }
    }
}
fn reduce_tracked(
    mut row: Row,
    pivots: &[Option<(Row, Provenance)>],
) -> (Row, Provenance) {
    let mut provenance = Provenance::new();
    loop {
        let Some(pivot) = row.keys().rev().find(|&&column| pivots[column].is_some()).copied() else { return (row, provenance); };
        let coefficient = row[&pivot];
        let (existing, existing_provenance) = pivots[pivot].as_ref().unwrap();
        let terms: Vec<(usize, u32)> = existing.iter().map(|(&c, &v)| (c, v)).collect();
        let provenance_terms: Vec<(usize, u32)> = existing_provenance.iter().map(|(&c, &v)| (c, v)).collect();
        for (column, value) in terms {
            add_value(&mut row, column, (P - mul(coefficient, value)) % P);
        }
        for (source, value) in provenance_terms {
            add_value(&mut provenance, source, (P - mul(coefficient, value)) % P);
        }
    }
}
fn reduce_pair(
    mut base: Row,
    mut tangent: Row,
    pivots: &mut [Option<(Row, Row)>],
) -> Option<Row> {
    loop {
        let Some((&pivot, &coefficient)) = base.last_key_value() else { return Some(tangent); };
        if let Some((existing_base, existing_tangent)) = &pivots[pivot] {
            let base_terms: Vec<(usize, u32)> = existing_base.iter().map(|(&c, &v)| (c, v)).collect();
            let tangent_terms: Vec<(usize, u32)> = existing_tangent.iter().map(|(&c, &v)| (c, v)).collect();
            for (column, value) in base_terms {
                add_value(&mut base, column, (P - mul(coefficient, value)) % P);
            }
            for (column, value) in tangent_terms {
                add_value(&mut tangent, column, (P - mul(coefficient, value)) % P);
            }
        } else {
            let inverse = pow(coefficient, P - 2);
            for value in base.values_mut() { *value = mul(*value, inverse); }
            for value in tangent.values_mut() { *value = mul(*value, inverse); }
            pivots[pivot] = Some((base, tangent));
            return None;
        }
    }
}
fn reduce_pair_fixed(
    mut base: Row,
    mut image: Row,
    pivots: &[Option<(Row, Row)>],
) -> (Row, Row) {
    loop {
        let Some(pivot) = base.keys().rev().find(|&&column| pivots[column].is_some()).copied() else {
            return (base, image);
        };
        let coefficient = base[&pivot];
        let (existing_base, existing_image) = pivots[pivot].as_ref().unwrap();
        for (&column, &value) in existing_base { add_value(&mut base, column, (P - mul(coefficient, value)) % P); }
        for (&column, &value) in existing_image { add_value(&mut image, column, (P - mul(coefficient, value)) % P); }
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
    let arguments: Vec<String> = env::args().collect();
    let path = arguments.get(1).expect("usage: triangle_wall_dual_rank <packet> [mode]");
    let second_argument = arguments.get(2).cloned();
    let mixed_length3_only = second_argument.as_deref() == Some("--mixed-length3-only");
    let mixed_lower_only = second_argument.as_deref() == Some("--mixed-lower-only");
    let write_basis_path = if second_argument.as_deref() == Some("--write-quadratic-basis") {
        Some(arguments.get(3).expect("--write-quadratic-basis requires a path").clone())
    } else if second_argument.as_deref() == Some("--probe-basis-and-write") {
        Some(arguments.get(5).expect("--probe-basis-and-write requires an output path").clone())
    } else { None };
    let transition_probe = if second_argument.as_deref() == Some("--probe-basis")
        || second_argument.as_deref() == Some("--probe-basis-and-write") {
        Some((
            arguments.get(3).expect("--probe-basis requires a path").clone(),
            arguments.get(4).expect("--probe-basis requires old column count").parse::<usize>().unwrap(),
        ))
    } else { None };
    let connection_sidecar = if second_argument.as_deref() == Some("--transport-connection") {
        Some((
            arguments.get(3).expect("--transport-connection requires a sidecar path").clone(),
            arguments.get(4).expect("--transport-connection requires an output path").clone(),
        ))
    } else { None };
    let probe_file = if second_argument.as_deref() == Some("--probe-file") {
        Some(arguments.get(3).expect("--probe-file requires a path").clone())
    } else { None };
    let probe = second_argument.filter(|argument| {
        !mixed_length3_only && !mixed_lower_only
            && argument != "--write-quadratic-basis" && argument != "--probe-basis"
            && argument != "--probe-basis-and-write" && argument != "--probe-file"
            && argument != "--transport-connection"
    }).map(|argument| {
        argument.split(',').filter(|term| !term.is_empty()).map(|term| {
            let (column, value) = term.split_once(':').expect("probe term must be column:value");
            (column.parse::<usize>().unwrap(), value.parse::<u32>().unwrap() % P)
        }).collect::<Row>()
    });
    let mut bytes = Vec::new();
    File::open(path)?.read_to_end(&mut bytes)?;
    let version = &bytes[..8];
    assert!(version == b"MRCIDR02" || version == b"MRCIDR03" || version == b"MRCIDR04");
    let mut cursor = 8;
    assert_eq!(u32_at(&bytes, &mut cursor), P);
    let ambient = u32_at(&bytes, &mut cursor);
    let columns = u32_at(&bytes, &mut cursor) as usize;
    let rows = u32_at(&bytes, &mut cursor) as usize;
    let _declared_central_rank = u32_at(&bytes, &mut cursor) as usize;
    let mut dual_pivots: Vec<Option<Row>> = vec![None; 2 * columns];
    let mut triple_pivots: Vec<Option<Row>> = vec![None; 3 * columns];
    let mut central_pivots: Vec<Option<Row>> = vec![None; columns];
    let mut dual_rank = 0usize;
    let mut triple_rank = 0usize;
    let mut cumulative = Vec::new();
    let mut records = Vec::with_capacity(rows);
    let mut tangent_records = Vec::with_capacity(rows);
    let mut central_generators = Vec::new();
    let mut active_family = 0u32;
    for _ in 0..rows {
        let family = if version == b"MRCIDR03" || version == b"MRCIDR04" { u32_at(&bytes, &mut cursor) } else { 0 };
        if family != active_family {
            cumulative.push((active_family, central_pivots.iter().flatten().count(), dual_rank, triple_rank));
            active_family = family;
        }
        let central = row_at(&bytes, &mut cursor);
        let derivative = row_at(&bytes, &mut cursor);
        let second = row_at(&bytes, &mut cursor);
        if version == b"MRCIDR04" {
            tangent_records.push((
                row_at(&bytes, &mut cursor),
                row_at(&bytes, &mut cursor),
                row_at(&bytes, &mut cursor),
            ));
        }
        let row_index = records.len();
        records.push((family, central.clone(), derivative.clone(), second.clone()));
        if insert(central.clone(), &mut central_pivots) { central_generators.push(row_index); }
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

    let connection_records = if let Some((sidecar_path, _)) = &connection_sidecar {
        let mut sidecar = Vec::new();
        File::open(sidecar_path)?.read_to_end(&mut sidecar)?;
        assert_eq!(&sidecar[..8], b"MRCICON1");
        let mut sidecar_cursor = 8;
        assert_eq!(u32_at(&sidecar, &mut sidecar_cursor), P);
        assert_eq!(u32_at(&sidecar, &mut sidecar_cursor), ambient);
        assert_eq!(u32_at(&sidecar, &mut sidecar_cursor) as usize, rows);
        let target_columns = u32_at(&sidecar, &mut sidecar_cursor) as usize;
        let mut images = Vec::with_capacity(rows);
        for _ in 0..rows {
            images.push((row_at(&sidecar, &mut sidecar_cursor), row_at(&sidecar, &mut sidecar_cursor)));
        }
        Some((target_columns, images))
    } else { None };
    let central_rank = central_pivots.iter().flatten().count();
    let first_normal = dual_rank - 2 * central_rank;
    let second_normal = triple_rank - 3 * central_rank - 2 * first_normal;
    assert_eq!(central_generators.len(), central_rank);

    let tangent_json = if version == b"MRCIDR04" {
        let mut mixed_results = Vec::new();
        let base_ranks = [central_rank, dual_rank, triple_rank];
        let lengths: Vec<usize> = if mixed_length3_only {
            vec![3]
        } else if mixed_lower_only {
            vec![1, 2]
        } else {
            (1..=3).collect()
        };
        for lambda_length in lengths {
            let width = lambda_length * columns;
            let mut pair_pivots: Vec<Option<(Row, Row)>> = vec![None; width];
            let mut defect_candidates = Vec::new();
            for (index, (_, central, derivative, second)) in records.iter().enumerate() {
                let normal = [central, derivative, second];
                let tangent = [&tangent_records[index].0, &tangent_records[index].1, &tangent_records[index].2];
                for lambda_shift in 0..lambda_length {
                    let mut base_row = Row::new();
                    let mut tangent_row = Row::new();
                    for order in 0..(lambda_length - lambda_shift) {
                        let block = lambda_shift + order;
                        for (&column, &value) in normal[order] {
                            add_value(&mut base_row, block * columns + column, value);
                        }
                        for (&column, &value) in tangent[order] {
                            add_value(&mut tangent_row, block * columns + column, value);
                        }
                    }
                    if let Some(candidate) = reduce_pair(base_row, tangent_row, &mut pair_pivots) {
                        if !candidate.is_empty() {
                            defect_candidates.push(candidate);
                        }
                    }
                }
            }
            let pair_rank = pair_pivots.iter().flatten().count();
            assert_eq!(pair_rank, base_ranks[lambda_length - 1]);
            let base_pivots: Vec<Option<Row>> = pair_pivots.iter().map(|entry| {
                entry.as_ref().map(|(base, _)| base.clone())
            }).collect();
            let mut defect_pivots: Vec<Option<Row>> = vec![None; width];
            let mut excess = 0usize;
            for candidate in defect_candidates {
                let residual = reduce(candidate, &base_pivots);
                if insert(residual, &mut defect_pivots) {
                    excess += 1;
                }
            }
            mixed_results.push((lambda_length, 2 * pair_rank + excess, excess));
        }
        let levels = mixed_results.iter().map(|(length, rank, excess)| {
            format!("{{\"normal_length\":{length},\"relation_rank\":{rank},\"flatness_excess\":{excess}}}")
        }).collect::<Vec<_>>().join(",");
        format!("{{\"levels\":[{levels}]}}")
    } else { "null".to_string() };

    // Build the length-two module in a source-tracked basis.  The first two
    // stages are the two shifts of a selected M0 basis.  Any later pivot is a
    // genuine first-normal lift, with coefficients in U + Lambda U retained.
    let mut tracked_dual: Vec<Option<(Row, Provenance)>> = vec![None; 2 * columns];
    for &index in &central_generators {
        let central = &records[index].1;
        insert_tracked(shifted(central, columns), [(rows + index, 1)].into(), &mut tracked_dual);
    }
    for &index in &central_generators {
        let (_, central, derivative, _) = &records[index];
        let mut first = central.clone();
        for (&column, &value) in derivative { add_value(&mut first, columns + column, value); }
        insert_tracked(first, [(index, 1)].into(), &mut tracked_dual);
    }
    let mut first_lifts = Vec::new();
    for (index, (_, central, derivative, _)) in records.iter().enumerate() {
        let mut first = central.clone();
        for (&column, &value) in derivative { add_value(&mut first, columns + column, value); }
        if let Some((_, provenance)) = insert_tracked(first, [(index, 1)].into(), &mut tracked_dual) {
            first_lifts.push(provenance);
        }
    }
    assert_eq!(first_lifts.len(), first_normal);

    let lift_to_length_three = |provenance: &Provenance| {
        let mut out = Row::new();
        for (&source, &coefficient) in provenance {
            if source < rows {
                let (_, central, derivative, second) = &records[source];
                for (&column, &value) in central { add_value(&mut out, column, mul(coefficient, value)); }
                for (&column, &value) in derivative { add_value(&mut out, columns + column, mul(coefficient, value)); }
                for (&column, &value) in second { add_value(&mut out, 2 * columns + column, mul(coefficient, value)); }
            } else {
                let (_, central, derivative, _) = &records[source - rows];
                for (&column, &value) in central { add_value(&mut out, columns + column, mul(coefficient, value)); }
                for (&column, &value) in derivative { add_value(&mut out, 2 * columns + column, mul(coefficient, value)); }
            }
        }
        out
    };

    // Seed precisely the valuation-zero and valuation-one length-three
    // lifts.  The remaining grade-zero pivots are the valuation-two grade.
    let mut filtered_triple: Vec<Option<Row>> = vec![None; 3 * columns];
    for &index in &central_generators {
        insert(shifted(&records[index].1, 2 * columns), &mut filtered_triple);
    }
    for (_, central, derivative, _) in &records {
        let mut grade_one = shifted(central, columns);
        for (&column, &value) in derivative { add_value(&mut grade_one, 2 * columns + column, value); }
        insert(grade_one, &mut filtered_triple);
    }
    for &index in &central_generators {
        insert(lift_to_length_three(&[(index, 1)].into()), &mut filtered_triple);
    }
    for provenance in &first_lifts {
        insert(lift_to_length_three(provenance), &mut filtered_triple);
    }
    let baseline_rank = filtered_triple.iter().flatten().count();
    assert_eq!(baseline_rank, 3 * central_rank + 2 * first_normal);
    let mut quadratic_witnesses = Vec::new();
    let mut quadratic_basis: Vec<Option<(Row, Provenance)>> = vec![None; 3 * columns];
    for (index, (_, central, derivative, second)) in records.iter().enumerate() {
        let mut grade_zero = central.clone();
        for (&column, &value) in derivative { add_value(&mut grade_zero, columns + column, value); }
        for (&column, &value) in second { add_value(&mut grade_zero, 2 * columns + column, value); }
        let residual = reduce(grade_zero, &filtered_triple);
        let witness_index = quadratic_witnesses.len();
        if let Some((pivot, _)) = insert_tracked(residual, [(witness_index, 1)].into(), &mut quadratic_basis) {
            let normalized = quadratic_basis[pivot].as_ref().unwrap().0.clone();
            quadratic_witnesses.push((index, records[index].0, pivot, normalized));
        }
    }

    if let (Some((target_columns, connection_images)), Some((_, output_path))) = (&connection_records, &connection_sidecar) {
        let shifted_connection = |row: &Row, shift: usize| -> Row {
            row.iter().filter_map(|(&column, &value)| {
                let block = column / target_columns;
                let within = column % target_columns;
                (block + shift < 3).then_some(((block + shift) * target_columns + within, value))
            }).collect()
        };
        let connection_lift = |provenance: &Provenance, tangent: usize| -> Row {
            let mut out = Row::new();
            for (&source, &coefficient) in provenance {
                let (t1, t2) = &connection_images[source % rows];
                let image = if tangent == 0 { t1 } else { t2 };
                let shifted_image = shifted_connection(image, source / rows);
                for (column, value) in shifted_image { add_value(&mut out, column, mul(coefficient, value)); }
            }
            out
        };
        let mut outputs = vec![Vec::<Row>::new(), Vec::<Row>::new()];
        for tangent in 0..2 {
            let mut paired_baseline: Vec<Option<(Row, Row)>> = vec![None; 3 * columns];
            for &index in &central_generators {
                let base_row = shifted(&records[index].1, 2 * columns);
                let image_row = shifted_connection(if tangent == 0 { &connection_images[index].0 } else { &connection_images[index].1 }, 2);
                reduce_pair(base_row, image_row, &mut paired_baseline);
            }
            for (index, (_, central, derivative, _)) in records.iter().enumerate() {
                let mut base_row = shifted(central, columns);
                for (&column, &value) in derivative { add_value(&mut base_row, 2 * columns + column, value); }
                let image_row = shifted_connection(if tangent == 0 { &connection_images[index].0 } else { &connection_images[index].1 }, 1);
                reduce_pair(base_row, image_row, &mut paired_baseline);
            }
            for &index in &central_generators {
                let provenance: Provenance = [(index, 1)].into();
                reduce_pair(lift_to_length_three(&provenance), connection_lift(&provenance, tangent), &mut paired_baseline);
            }
            for provenance in &first_lifts {
                reduce_pair(lift_to_length_three(provenance), connection_lift(provenance, tangent), &mut paired_baseline);
            }
            let mut paired_quadratic: Vec<Option<(Row, Row)>> = vec![None; 3 * columns];
            for (index, (_, central, derivative, second)) in records.iter().enumerate() {
                let mut base_row = central.clone();
                for (&column, &value) in derivative { add_value(&mut base_row, columns + column, value); }
                for (&column, &value) in second { add_value(&mut base_row, 2 * columns + column, value); }
                let image_row = if tangent == 0 { connection_images[index].0.clone() } else { connection_images[index].1.clone() };
                let (base_residual, image_residual) = reduce_pair_fixed(base_row, image_row, &paired_baseline);
                if base_residual.is_empty() { continue; }
                let pivot = *base_residual.keys().next_back().unwrap();
                if paired_quadratic[pivot].is_none() {
                    let inverse = pow(base_residual[&pivot], P - 2);
                    let normalized_base: Row = base_residual.into_iter().map(|(column, value)| (column, mul(value, inverse))).collect();
                    let normalized_image: Row = image_residual.into_iter().map(|(column, value)| (column, mul(value, inverse))).collect();
                    paired_quadratic[pivot] = Some((normalized_base, normalized_image.clone()));
                    outputs[tangent].push(normalized_image);
                } else {
                    let (reduced_base, reduced_image) = reduce_pair_fixed(base_residual, image_residual, &paired_quadratic);
                    if !reduced_base.is_empty() {
                        let pivot = *reduced_base.keys().next_back().unwrap();
                        let inverse = pow(reduced_base[&pivot], P - 2);
                        let normalized_base: Row = reduced_base.into_iter().map(|(column, value)| (column, mul(value, inverse))).collect();
                        let normalized_image: Row = reduced_image.into_iter().map(|(column, value)| (column, mul(value, inverse))).collect();
                        paired_quadratic[pivot] = Some((normalized_base, normalized_image.clone()));
                        outputs[tangent].push(normalized_image);
                    }
                }
            }
        }
        let mut output = File::create(output_path)?;
        for tangent in 0..2 {
            assert_eq!(outputs[tangent].len(), second_normal);
            for row in &outputs[tangent] {
                writeln!(output, "{}", row.iter().map(|(column, value)| format!("{column}:{value}")).collect::<Vec<_>>().join(","))?;
            }
        }
    }
    assert_eq!(quadratic_witnesses.len(), second_normal);
    if let Some(path) = write_basis_path {
        let mut output = File::create(path)?;
        for entry in quadratic_basis.iter().flatten() {
            let line = entry.0.iter().map(|(column, value)| format!("{column}:{value}"))
                .collect::<Vec<_>>().join(",");
            writeln!(output, "{line}")?;
        }
    }
    let transition_json = if let Some((path, old_columns)) = transition_probe {
        let text = std::fs::read_to_string(path)?;
        let mut coordinate_pivots: Vec<Option<Row>> = vec![None; second_normal];
        let mut probe_count = 0usize;
        let mut remainder_count = 0usize;
        let mut coordinate_rows = Vec::new();
        for line in text.lines().filter(|line| !line.trim().is_empty()) {
            probe_count += 1;
            let embedded = line.split(',').map(|term| {
                let (old_column, value) = term.split_once(':').unwrap();
                let old_column = old_column.parse::<usize>().unwrap();
                let block = old_column / old_columns;
                let within = old_column % old_columns;
                (block * columns + within, value.parse::<u32>().unwrap() % P)
            }).collect::<Row>();
            let baseline_residual = reduce(embedded, &filtered_triple);
            let (remainder, coefficients) = reduce_tracked(baseline_residual, &quadratic_basis);
            if !remainder.is_empty() { remainder_count += 1; }
            let coordinate_row: Row = coefficients.into_iter().map(|(index, value)| (index, (P - value) % P)).collect();
            coordinate_rows.push(coordinate_row.clone());
            insert(coordinate_row, &mut coordinate_pivots);
        }
        let rank = coordinate_pivots.iter().flatten().count();
        let image_pivots = coordinate_pivots.iter().enumerate()
            .filter_map(|(index, row)| row.as_ref().map(|_| index))
            .collect::<Vec<_>>();
        let quotient_columns = (0..second_normal)
            .filter(|index| coordinate_pivots[*index].is_none())
            .collect::<Vec<_>>();
        let image_pivots_json = image_pivots.iter().map(usize::to_string).collect::<Vec<_>>().join(",");
        let quotient_columns_json = quotient_columns.iter().map(usize::to_string).collect::<Vec<_>>().join(",");
        let coordinates_json = coordinate_rows.iter().map(|row| {
            let entries = row.iter().map(|(index, value)| format!("[{index},{value}]")).collect::<Vec<_>>().join(",");
            format!("[{entries}]")
        }).collect::<Vec<_>>().join(",");
        format!("{{\"probe_count\":{probe_count},\"target_dimension\":{second_normal},\"transition_rank\":{rank},\"kernel_dimension\":{},\"cokernel_dimension\":{},\"nonzero_remainders\":{remainder_count},\"image_pivot_columns\":[{image_pivots_json}],\"quotient_coordinate_columns\":[{quotient_columns_json}],\"coordinate_rows\":[{coordinates_json}]}}", probe_count - rank, second_normal - rank)
    } else { "null".to_string() };
    let probe_json = if let Some(probe) = probe {
        let baseline_residual = reduce(probe, &filtered_triple);
        let (remainder, coefficients) = reduce_tracked(baseline_residual, &quadratic_basis);
        let coordinates = coefficients.iter().map(|(index, value)| {
            format!("[{index},{}]", (P - value) % P)
        }).collect::<Vec<_>>().join(",");
        format!("{{\"remainder_terms\":{},\"coordinates\":[{coordinates}]}}", remainder.len())
    } else { "null".to_string() };
    let probe_file_json = if let Some(path) = probe_file {
        let text = std::fs::read_to_string(path)?;
        let mut results = Vec::new();
        for line in text.lines().filter(|line| !line.trim().is_empty()) {
            let probe = line.split(',').filter(|term| !term.is_empty()).map(|term| {
                let (column, value) = term.split_once(':').expect("probe term must be column:value");
                (column.parse::<usize>().unwrap(), value.parse::<u32>().unwrap() % P)
            }).collect::<Row>();
            let baseline_residual = reduce(probe, &filtered_triple);
            let (remainder, coefficients) = reduce_tracked(baseline_residual, &quadratic_basis);
            let coordinates = coefficients.iter().map(|(index, value)| {
                format!("[{index},{}]", (P - value) % P)
            }).collect::<Vec<_>>().join(",");
            results.push(format!("{{\"remainder_terms\":{},\"coordinates\":[{coordinates}]}}", remainder.len()));
        }
        format!("[{}]", results.join(","))
    } else { "null".to_string() };
    let family_json = cumulative.iter().map(|(family, central, dual, triple)| {
        let first = dual - 2 * central;
        let second = triple - 3 * central - 2 * first;
        format!("{{\"family_through\":{family},\"central_rank\":{central},\"first_normal_rank\":{first},\"second_normal_rank\":{second}}}")
    }).collect::<Vec<_>>().join(",");
    let witness_json = quadratic_witnesses.iter().map(|(row, family, pivot, residual)| {
        let residual_json = if *family == 6 {
            residual.iter().map(|(column, value)| format!("[{column},{value}]")).collect::<Vec<_>>().join(",")
        } else { String::new() };
        format!("{{\"row_index\":{row},\"family\":{family},\"pivot_column\":{pivot},\"residual\":[{residual_json}]}}")
    }).collect::<Vec<_>>().join(",");
    println!("{{\"schema\":\"marici.triangle-wall-jet-rank-rust.v6\",\"ambient_relation_degree\":{ambient},\"column_count\":{columns},\"raw_relation_row_count\":{rows},\"central_relation_rank\":{central_rank},\"dual_block_rank\":{dual_rank},\"first_normal_rank\":{first_normal},\"triple_block_rank\":{triple_rank},\"second_normal_rank\":{second_normal},\"tangential_jet\":{tangent_json},\"family_filtration\":[{family_json}],\"tracked_first_lift_count\":{},\"filtered_baseline_rank\":{baseline_rank},\"quadratic_witnesses\":[{witness_json}],\"probe\":{probe_json},\"probe_file\":{probe_file_json},\"basis_transition\":{transition_json}}}", first_lifts.len());
    Ok(())
}
