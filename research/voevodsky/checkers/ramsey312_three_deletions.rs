// Three deletion audit; stdout: deleted triple, #supports, then three (common bit, missed ten-set) pairs, or FAIL.
#[allow(dead_code)]
mod search {
    include!("ramsey312_google_three_step.rs");
    fn witness(a: &[M], mut p: M, k: u32) -> Option<M> {
        if k == 0 {
            return Some(0);
        }
        while p.count_ones() >= k {
            let b = bit(p);
            p ^= b;
            if let Some(t) = witness(a, p & !a[b.trailing_zeros() as usize], k - 1) {
                return Some(b | t);
            }
        }
        None
    }
    fn cert(a: &[M], h: M, cl: &[M]) -> Option<(M, M)> {
        if cl.is_empty() {
            return None;
        }
        let inter = cl.iter().fold(h, |v, x| v & x);
        if inter == 0 {
            return None;
        }
        let un = cl.iter().fold(0, |v, x| v | x);
        Some((bit(inter), witness(a, h & !un, 10)?))
    }
    fn by_bits(a: &[M], h: M, s: &[M]) -> Option<[(M, M); 3]> {
        for i in 0..52 {
            let (l, r): (Vec<_>, Vec<_>) = s.iter().copied().partition(|x| x >> i & 1 != 0);
            if l.is_empty() || r.is_empty() {
                continue;
            }
            for (one, two) in [(&l, &r), (&r, &l)] {
                if let Some(c) = cert(a, h, one) {
                    for j in 0..52 {
                        let (l, r): (Vec<_>, Vec<_>) =
                            two.iter().copied().partition(|x| x >> j & 1 != 0);
                        if let (Some(d), Some(e)) = (cert(a, h, &l), cert(a, h, &r)) {
                            return Some([c, d, e]);
                        }
                    }
                }
            }
        }
        None
    }
    pub fn audit() {
        let args: Vec<_> = env::args().collect();
        let data: Vec<_> = fs::read_to_string(&args[1])
            .unwrap()
            .bytes()
            .filter(|x| *x == 48 || *x == 49)
            .collect();
        assert_eq!(data.len(), 2704);
        let a: Vec<M> = data
            .chunks(52)
            .map(|r| {
                r.iter()
                    .enumerate()
                    .fold(0, |m, (i, &x)| m | (((x - 48) as M) << i))
            })
            .collect();
        let f = (1 << 52) - 1;
        let mut elev = vec![];
        sets(&a, f, 11, 0, &mut elev);
        let start: usize = args[2].parse().unwrap();
        let end: usize = args[3].parse().unwrap();
        for u in start..end {
            for v in 0..u {
                for w in 0..v {
                    let h = f ^ (1 << u) ^ (1 << v) ^ (1 << w);
                    let low = (0..52)
                        .filter(|&i| h >> i & 1 != 0 && (a[i] & h).count_ones() < 11)
                        .fold(0, |m, i| m | 1 << i);
                    let mut req: Vec<_> = elev
                        .iter()
                        .filter(|&&x| x & !h == 0)
                        .map(|x| x & low)
                        .collect();
                    req.sort_unstable();
                    req.dedup();
                    req.sort_unstable_by_key(|x| x.count_ones());
                    let mut mins = vec![];
                    for x in req {
                        if !mins.iter().any(|y| x & y == *y) {
                            mins.push(x)
                        }
                    }
                    let mut s = vec![];
                    supports(&a, low, 0, &mins, &mut s);
                    let anchors = [a[u] & h, a[v] & h, a[w] & h];
                    assert!(anchors.iter().all(|x| s.contains(x)));
                    let mut c = [vec![], vec![], vec![]];
                    for &x in &s {
                        let j = (0..3)
                            .min_by_key(|&j| (anchors[j] ^ x).count_ones())
                            .unwrap();
                        c[j].push(x)
                    }
                    let probed = c
                        .iter()
                        .map(|v| cert(&a, h, v))
                        .collect::<Option<Vec<_>>>()
                        .or_else(|| by_bits(&a, h, &s).map(|z| z.to_vec()));
                    print!("{u},{v},{w},{}", s.len());
                    if let Some(classes) = probed {
                        assert!(s
                            .iter()
                            .all(|s| classes.iter().any(|(b, t)| s & b != 0 && s & t == 0)));
                        for (b, t) in classes {
                            print!(",{b},{t}")
                        }
                    } else {
                        print!(",FAIL")
                    }
                    println!();
                }
            }
        }
    }
}
fn main() {
    search::audit()
}
