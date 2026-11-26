// Same compressed footprint inequalities as ramsey_path_power_tensor_26.py, using 101-bit port masks.
use std::{
    env,
    fs::File,
    io::{BufWriter, Write},
};
type M = u128;
type Cs = Vec<(M, i32)>;
fn possible(cs: &Cs, q: i32, allowed: M, order: &[M]) -> bool {
    if (allowed.count_ones() as i32) < q {
        return false;
    }
    let mut s = 0;
    for &(f, c) in cs {
        if f.is_power_of_two() && q > c {
            s |= f
        }
    }
    if s & !allowed != 0 || s.count_ones() as i32 > q {
        return false;
    }
    for &b in order {
        if s.count_ones() as i32 == q {
            break;
        }
        s |= allowed & b
    }
    cs.iter().all(|&(f, c)| ((s & !f).count_ones() as i32) <= c)
}
fn cell(l: i32, k: i32) -> (String, i32, i32) {
    if l == 1 || k == 1 {
        return ("-".into(), -1, -1);
    }
    if l == 2 && k > 2 {
        return ("x".into(), -1, -1);
    }
    let n = (l - 1) * (k - 2);
    let full = (1u128 << (l + 1)) - 1;
    let mut order = vec![1u128];
    order.extend((1..l).rev().map(|i| 1u128 << i));
    order.push(1u128 << l);
    let mut footprints = vec![(0, 0)];
    for i in 0..l {
        footprints.push((1u128 << i, (n + l - 1 - i) / l))
    }
    let mut f = 1;
    for j in 1..l {
        f |= order[j as usize];
        let mut v = 0;
        while v * l - (if j == l - 1 { v } else { v.min(j) }) < n {
            v += 1
        }
        footprints.push((f, v))
    }
    let make = |root: i32| -> Cs {
        footprints
            .iter()
            .filter_map(|&(f, v)| {
                let c = k - 1 - v - i32::from(f & (1 << root) == 0);
                if c < ((full ^ f).count_ones() as i32) {
                    Some((f, c))
                } else {
                    None
                }
            })
            .collect()
    };
    let a = make(0);
    let b = make(l - 1);
    let mut first = l + 2;
    for (bad, good) in [(&a, &b), (&b, &a)] {
        for &(f, c) in bad {
            if c + 1 < first && possible(good, c + 1, full ^ f, &order) {
                first = c + 1
            }
        }
    }
    let repair = |cs: &Cs| {
        let (mut lo, mut hi) = (0, l + 2);
        while hi - lo > 1 {
            let mid = (lo + hi) / 2;
            if possible(cs, mid, full, &order) {
                lo = mid
            } else {
                hi = mid
            }
        }
        l + 1 - lo
    };
    (
        if first == l + 2 {
            "=".into()
        } else {
            first.to_string()
        },
        repair(&a),
        repair(&b),
    )
}
fn main() {
    let path = env::args().nth(1).unwrap();
    let mut w = BufWriter::new(File::create(path).unwrap());
    writeln!(w, "l,k,first_difference,repair_A,repair_C").unwrap();
    for l in 1..=100 {
        for k in 1..=100 {
            let (t, a, b) = cell(l, k);
            if a < 0 {
                writeln!(w, "{l},{k},{t},,").unwrap()
            } else {
                writeln!(w, "{l},{k},{t},{a},{b}").unwrap()
            }
        }
    }
}
