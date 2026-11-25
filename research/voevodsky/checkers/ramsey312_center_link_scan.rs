// Enumerate maximal centered common-link domains of compatible exterior support pairs. Reduce each by inclusion domination before building the compatibility graph.
#[allow(dead_code)]
mod scan {
    include!("ramsey312_google_three_step.rs");
    use std::collections::HashMap;
    fn fit(a: &[M], h: M, x: M, y: M) -> bool {
        x & y == 0 || !has(a, h & !(x | y), 10)
    }
    pub fn go() {
        let args: Vec<_> = env::args().collect();
        let b: Vec<_> = fs::read_to_string(&args[1])
            .unwrap()
            .bytes()
            .filter(|&x| x == 48 || x == 49)
            .collect();
        let a: Vec<M> = b
            .chunks(52)
            .map(|r| {
                r.iter()
                    .enumerate()
                    .fold(0, |m, (i, &x)| m | (((x - 48) as M) << i))
            })
            .collect();
        for line in fs::read_to_string(&args[2]).unwrap().lines() {
            let r: Vec<M> = line
                .split_whitespace()
                .map(|x| x.parse().unwrap())
                .collect();
            let d = r[0];
            let h = ((1 << 52) - 1) ^ d;
            for tri in [[37, 39, 41], [1, 49, 51]] {
                if tri.iter().any(|v| d & (1 << v) == 0) {
                    continue;
                }
                let c = tri.iter().fold(h, |x, &v| x & a[v]);
                assert!(c != 0);
                let (inside, out): (Vec<_>, Vec<_>) =
                    r[1..].iter().copied().partition(|x| x & c == c);
                let mut l = vec![];
                for &x in &out {
                    let mut v = vec![0u64; (inside.len() + 63) / 64];
                    for (i, &y) in inside.iter().enumerate() {
                        if fit(&a, h, x, y) {
                            v[i / 64] |= 1 << (i % 64)
                        }
                    }
                    l.push(v)
                }
                let mut ds = HashMap::new();
                let mut pairs = 0;
                for (i, &x) in out.iter().enumerate() {
                    if args.get(3).map_or(false, |v| v == "--single") {
                        pairs += 1;
                        ds.entry(l[i].clone()).or_insert((x, 0));
                        continue;
                    }
                    for (j, &y) in out[..i].iter().enumerate() {
                        if !fit(&a, h, x, y) {
                            continue;
                        }
                        pairs += 1;
                        let v: Vec<M> = l[i].iter().zip(&l[j]).map(|(a, b)| a & b).collect();
                        ds.entry(v).or_insert((x, y));
                    }
                }
                let n = ds.len();
                let mut ds: Vec<_> = ds.into_iter().collect();
                ds.sort_unstable_by_key(|(v, _)| {
                    (
                        std::cmp::Reverse(v.iter().map(|x| x.count_ones()).sum::<u32>()),
                        v.clone(),
                    )
                });
                let mut max: Vec<Vec<M>> = vec![];
                for (v, (x, y)) in ds {
                    if max
                        .iter()
                        .any(|w| v.iter().zip(w).all(|(p, q)| p & !q == 0))
                    {
                        continue;
                    }
                    let mut s: Vec<_> = inside
                        .iter()
                        .enumerate()
                        .filter_map(|(i, &z)| {
                            if v[i / 64] >> (i % 64) & 1 != 0 {
                                Some(z)
                            } else {
                                None
                            }
                        })
                        .collect();
                    s.sort_unstable_by_key(|x| std::cmp::Reverse(x.count_ones()));
                    let mut f = vec![];
                    for x in s {
                        if !f.iter().any(|&y| x & y == x) {
                            f.push(x)
                        }
                    }
                    print!("L {d} {x} {y} {}", f.len());
                    for x in &f {
                        print!(" {x}")
                    }
                    print!(" ;");
                    for (i, &x) in f.iter().enumerate() {
                        for (j, &y) in f[..i].iter().enumerate() {
                            if fit(&a, h, x, y) {
                                print!(" {j}:{i}")
                            }
                        }
                    }
                    println!();
                    max.push(v)
                }
                println!("S {d} {c} {pairs} {n} {}", max.len());
            }
        }
    }
}
fn main() {
    scan::go()
}
