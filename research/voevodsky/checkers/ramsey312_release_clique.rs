// Certify by k-1 rectangles if possible; otherwise use exact graph and greedy-color bounds. A compatible loop alone permits a repeated-support clique.
fn tens(a: &[M], mut p: M, k: u32) -> Option<M> {
    if k == 0 {
        return Some(0);
    }
    while p.count_ones() >= k {
        let b = bit(p);
        p ^= b;
        if let Some(z) = tens(a, p & !a[b.trailing_zeros() as usize], k - 1) {
            return Some(b | z);
        }
    }
    None
}
fn fast(a: &[M], h: M, s: &[M], k: usize, cent: &[M], q: &mut Vec<usize>) -> bool {
    if s.is_empty() {
        return false;
    }
    let mut groups = vec![(h, 0); k - 1];
    for &x in s {
        let j = (0..cent.len())
            .min_by_key(|&i| (cent[i] ^ x).count_ones())
            .unwrap();
        groups[j].0 &= x;
        groups[j].1 |= x
    }
    if groups
        .iter()
        .all(|&(b, u)| u == 0 && b == h || b != 0 && has(a, h & !u, 10))
    {
        if s.contains(&0) {
            q.resize(k, s.iter().position(|x| *x == 0).unwrap());
            return true;
        }
        return false;
    }
    let mut g = vec![vec![0u64; (s.len() + 63) / 64]; s.len()];
    for (i, &x) in s.iter().enumerate() {
        let mut w = vec![];
        for (j, &y) in s[..=i].iter().enumerate() {
            if x & y != 0 {
                if w.iter().any(|t| t & y == 0) {
                    continue;
                }
                if let Some(t) = tens(a, h & !(x | y), 10) {
                    w.push(t);
                    continue;
                }
            }
            if i == j {
                q.resize(k, i);
                return true;
            }
            g[i][j / 64] |= 1 << (j % 64);
            g[j][i / 64] |= 1 << (i % 64)
        }
    }
    fn rec(g: &[Vec<M>], mut p: Vec<usize>, k: usize, q: &mut Vec<usize>) -> bool {
        if k == 0 {
            return true;
        }
        if p.len() < k {
            return false;
        }
        let mut order = vec![];
        let mut n = 0;
        while !p.is_empty() {
            let mut cl = vec![];
            n += 1;
            p.retain(|&i| {
                if cl
                    .iter()
                    .all(|&j: &usize| g[i][j / 64] >> (j % 64) & 1 == 0)
                {
                    cl.push(i);
                    false
                } else {
                    true
                }
            });
            order.extend(cl.into_iter().map(|i| (i, n)))
        }
        while let Some((i, n)) = order.pop() {
            if n < k {
                return false;
            }
            let next = order
                .iter()
                .filter_map(|&(j, _)| (g[i][j / 64] >> (j % 64) & 1 != 0).then_some(j))
                .collect();
            q.push(i);
            if rec(g, next, k - 1, q) {
                return true;
            }
            q.pop();
        }
        false
    }
    let mut p: Vec<_> = (0..s.len()).collect();
    p.sort_unstable_by_key(|&i| {
        std::cmp::Reverse(g[i].iter().map(|w| w.count_ones()).sum::<u32>())
    });
    rec(&g, p, k, q)
}
