// Blind two-deletion search from a 49-core. Precompute all centered maximal independent sets once per retained-center stratum; projection contains every possible maximal facet after any exterior deletions.
#[allow(dead_code)]
mod scan {
    include!("ramsey312_google_three_step.rs");
    fn facets(a: &[M], x: M, mut p: M, mut e: M, out: &mut Vec<M>) {
        if p | e == 0 {
            out.push(x);
            return;
        }
        let u = (p | e).trailing_zeros() as usize;
        let mut cand = p & (a[u] | (1 << u));
        while cand != 0 {
            let b = bit(cand);
            cand ^= b;
            let al = !(a[b.trailing_zeros() as usize] | b);
            facets(a, x | b, p & al, e & al, out);
            p ^= b;
            e |= b
        }
    }
    pub fn go() {
        let argv: Vec<_> = env::args().collect();
        let b: Vec<_> = fs::read_to_string(&argv[1])
            .unwrap()
            .bytes()
            .filter(|&x| x == 48 || x == 49)
            .collect();
        let a: Vec<M> = b
            .chunks(52)
            .map(|r| {
                r.iter()
                    .enumerate()
                    .fold(0, |m, (j, &x)| m | (((x - 48) as M) << j))
            })
            .collect();
        let f = (1 << 52) - 1;
        for tri in [[37, 39, 41], [1, 49, 51]] {
            let h = tri.iter().fold(f, |m, i| m & !(1 << i));
            let center = tri.iter().fold(h, |m, &i| m & a[i]);
            let mut pre = std::collections::HashMap::new();
            let mut elev = vec![];
            sets(&a, h, 11, 0, &mut elev);
            for i in 0..52 {
                for j in 0..i {
                    let d = (1 << i) | (1 << j);
                    if d & h != d {
                        continue;
                    }
                    let c = center & !d;
                    let raw = pre.entry(c).or_insert_with(|| {
                        let mut p = h & !center;
                        for v in 0..52 {
                            if c >> v & 1 != 0 {
                                p &= !a[v]
                            }
                        }
                        let mut raw = vec![];
                        facets(&a, c, p, 0, &mut raw);
                        raw
                    });
                    let mut projected: Vec<M> = raw.iter().map(|x| x & !d).collect();
                    projected.sort_unstable();
                    projected.dedup();
                    let mut s = vec![];
                    for &x in &projected {
                        if !projected.iter().any(|&y| x != y && x & y == x)
                            && !elev.iter().any(|t| t & (x | d) == 0)
                        {
                            s.push(x)
                        }
                    }
                    print!("{} {d} {}", f ^ h, s.len());
                    for x in &s {
                        print!(" {x}")
                    }
                    print!(" ;");
                    for (i, &x) in s.iter().enumerate() {
                        for (j, &y) in s[..i].iter().enumerate() {
                            if !has(&a, h & !(d | x | y), 10) {
                                print!(" {j}:{i}")
                            }
                        }
                    }
                    println!()
                }
            }
            eprintln!(
                "triple={tri:?} complete-center facets={}",
                pre[&center].len()
            );
        }
    }
}
fn main() {
    scan::go()
}
