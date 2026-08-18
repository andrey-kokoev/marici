use std::collections::{BTreeMap, HashMap};

const P: i64 = 2_305_843_009_213_693_951;
type Mon = (u8, usize, usize);
type Poly = BTreeMap<Mon, i64>;
type Row = (usize, u8, usize, usize);
type Column = BTreeMap<usize, i64>;

fn add_mod(x: i64, y: i64) -> i64 {
    ((x as i128 + y as i128).rem_euclid(P as i128)) as i64
}
fn mul_mod(x: i64, y: i64) -> i64 {
    ((x as i128 * y as i128).rem_euclid(P as i128)) as i64
}
fn pow_mod(mut x: i64, mut n: i64) -> i64 {
    let mut out = 1;
    while n > 0 {
        if n & 1 == 1 { out = mul_mod(out, x); }
        x = mul_mod(x, x);
        n >>= 1;
    }
    out
}
fn inv(x: i64) -> i64 { pow_mod(x, P - 2) }
fn mon(u: u8, a: usize, b: usize, c: i64) -> Poly {
    BTreeMap::from([((u, a, b), c.rem_euclid(P))])
}
fn scale(x: &Poly, c: i64) -> Poly {
    x.iter().filter_map(|(&m, &v)| {
        let z = mul_mod(v, c);
        (z != 0).then_some((m, z))
    }).collect()
}
fn add(xs: &[Poly]) -> Poly {
    let mut out = Poly::new();
    for x in xs {
        for (&m, &v) in x {
            let z = add_mod(*out.get(&m).unwrap_or(&0), v);
            if z == 0 { out.remove(&m); } else { out.insert(m, z); }
        }
    }
    out
}
fn mul(x: &Poly, y: &Poly) -> Poly {
    let mut out = Poly::new();
    for (&(u1, a1, b1), &c1) in x {
        for (&(u2, a2, b2), &c2) in y {
            if u1 + u2 >= 2 { continue; }
            let m = (u1 + u2, a1 + a2, b1 + b2);
            let z = add_mod(*out.get(&m).unwrap_or(&0), mul_mod(c1, c2));
            if z == 0 { out.remove(&m); } else { out.insert(m, z); }
        }
    }
    out
}
fn power(x: &Poly, n: usize) -> Poly {
    let mut out = mon(0, 0, 0, 1);
    for _ in 0..n { out = mul(&out, x); }
    out
}
fn derivative(x: &Poly, coordinate: usize) -> Poly {
    let mut out = Poly::new();
    for (&(u, a, b), &c) in x {
        let degrees = [u as usize, a, b];
        if degrees[coordinate] == 0 { continue; }
        let mut target = degrees;
        target[coordinate] -= 1;
        out.insert(
            (target[0] as u8, target[1], target[2]),
            mul_mod(c, degrees[coordinate] as i64),
        );
    }
    out
}

fn rank(columns: Vec<Column>) -> usize {
    let mut basis: BTreeMap<usize, Column> = BTreeMap::new();
    for mut vector in columns {
        while let Some((&pivot, &value)) = vector.first_key_value() {
            if let Some(base) = basis.get(&pivot) {
                for (&row, &entry) in base {
                    let z = add_mod(*vector.get(&row).unwrap_or(&0), P - mul_mod(value, entry));
                    if z == 0 { vector.remove(&row); } else { vector.insert(row, z); }
                }
            } else {
                let inverse = inv(value);
                for entry in vector.values_mut() { *entry = mul_mod(*entry, inverse); }
                basis.insert(pivot, vector);
                break;
            }
        }
    }
    basis.len()
}

fn component_rows(cutoff: usize) -> Vec<Row> {
    let mut rows = Vec::new();
    for (component, frame_character) in [(0, -1), (1, 1), (2, 1)] {
        for ud in 0..=1 {
            for total in 0..=cutoff {
                for ad in 0..=total {
                    let coefficient_character = if ad % 2 == 0 { 1 } else { -1 };
                    if coefficient_character * frame_character == 1 {
                        rows.push((component, ud, ad, total - ad));
                    }
                }
            }
        }
    }
    rows
}

fn emit(parts: &[Poly; 3], cutoff: usize, position: &HashMap<Row, usize>, columns: &mut Vec<Column>) {
    let nonempty = parts.iter().any(|part| !part.is_empty());
    if !nonempty { return; }
    // Whole-column admission: inspect every component before plus projection.
    if parts.iter().flat_map(|part| part.keys()).any(|&(ud, ad, bd)| ud >= 2 || ad + bd > cutoff) {
        return;
    }
    let mut column = Column::new();
    for (component, part) in parts.iter().enumerate() {
        for (&(ud, ad, bd), &coefficient) in part {
            if let Some(&row) = position.get(&(component, ud, ad, bd)) {
                let z = add_mod(*column.get(&row).unwrap_or(&0), coefficient);
                if z == 0 { column.remove(&row); } else { column.insert(row, z); }
            }
        }
    }
    if !column.is_empty() { columns.push(column); }
}

fn census(cutoff: usize) -> (usize, usize, usize) {
    let one = mon(0, 0, 0, 1);
    let u = mon(1, 0, 0, 1);
    let a = mon(0, 1, 0, 1);
    let b = mon(0, 0, 1, 1);
    let l1 = add(&[b.clone(), one, scale(&u, P - 1)]);
    let l2_minus = add(&[a.clone(), scale(&u, P - inv(2))]);
    let l2_plus = add(&[a.clone(), scale(&u, inv(2))]);
    let euler = [scale(&a, inv(4)), Poly::new(), scale(&u, inv(2))];

    let rows = component_rows(cutoff);
    let position: HashMap<_, _> = rows.iter().enumerate().map(|(i, &row)| (row, i)).collect();
    let mut columns = Vec::new();

    for (sa, sb) in [(1usize, 1usize), (1, 0), (0, 1), (0, 0)] {
        let (ea, eb) = (2 - sa, 2 - sb);
        for l2 in [&l2_minus, &l2_plus] {
            let base = mul(&power(&l1, ea), &power(l2, eb));
            for total in 0..=cutoff {
                for ad in 0..=total {
                    let f = mon(0, ad, total - ad, 1);
                    let m = mul(&f, &base);

                    let mut cp = scale(&mul(&derivative(&f, 2), &base), P - 1);
                    if sa != 0 {
                        cp = add(&[cp, scale(&mul(&mul(&f, &power(&l1, ea - 1)), &power(l2, eb)), sa as i64)]);
                    }
                    let hp = [Poly::new(), scale(&m, mul_mod(3, inv(2))), Poly::new()];
                    let pparts = std::array::from_fn(|i| add(&[hp[i].clone(), mul(&cp, &euler[i])]));
                    emit(&pparts, cutoff, &position, &mut columns);

                    let mut cq = mul(&derivative(&f, 1), &base);
                    if sb != 0 {
                        cq = add(&[cq, scale(&mul(&mul(&f, &power(&l1, ea)), &power(l2, eb - 1)), P - sb as i64)]);
                    }
                    let hq = [scale(&m, P - mul_mod(3, inv(2))), Poly::new(), Poly::new()];
                    let qparts = std::array::from_fn(|i| add(&[hq[i].clone(), mul(&cq, &euler[i])]));
                    emit(&qparts, cutoff, &position, &mut columns);
                }
            }
        }
    }

    for total in 0..=cutoff {
        for ad in 0..=total {
            let p = mon(0, ad, total - ad, 1);
            let parts = std::array::from_fn(|i| mul(&p, &euler[i]));
            emit(&parts, cutoff, &position, &mut columns);
        }
    }

    let full_dimension = rows.len() - rank(columns.clone());
    let zero_rows: Vec<_> = rows.iter().copied().filter(|row| row.1 == 0).collect();
    let zero_position: HashMap<_, _> = zero_rows.iter().enumerate().map(|(i, &row)| (row, i)).collect();
    let zero_columns = columns.into_iter().filter_map(|column| {
        let restricted: Column = column.into_iter().filter_map(|(row, value)| {
            (rows[row].1 == 0).then(|| (zero_position[&rows[row]], value))
        }).collect();
        (!restricted.is_empty()).then_some(restricted)
    }).collect();
    let special_dimension = zero_rows.len() - rank(zero_columns);
    let torsion_dimension = 2 * special_dimension - full_dimension;
    (full_dimension, special_dimension, torsion_dimension)
}

fn main() {
    let expected = [(12, (105, 68, 31)), (16, (155, 106, 57)), (20, (213, 152, 91)), (24, (279, 206, 133))];
    for (cutoff, wanted) in expected {
        let result = census(cutoff);
        assert_eq!(result, wanted);
        println!("D={cutoff}: dim_Q={} dim_Q_mod_u={} t={}", result.0, result.1, result.2);
    }
    println!("{{\"schema\":\"marici.benincasa.q_d_census.v1\",\"closed_form\":\"t_D=(D/2)^2-D/2+1\"}}");
}
