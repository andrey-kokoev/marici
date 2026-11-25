// Capacitated transversal of supports by core vertices b. At most 11-deg_H(b) newcomers can contain b in any joint completion. Solve restricted small hitting set exactly (heuristic work cap only skips this shortcut).
fn degree_certificate(a: &[M], h: M, s: &[M], budget: u32) -> Option<M> {
    let mut pool = h;
    let cost: Vec<_> = a
        .iter()
        .map(|v| 11u32.saturating_sub((v & h).count_ones()))
        .collect();
    for i in 0..52 {
        if cost[i] == 0 || cost[i] > budget {
            pool &= !(1 << i)
        }
    }
    let mut rows: Vec<_> = s.iter().map(|x| x & pool).collect();
    rows.sort_unstable();
    rows.dedup();
    if rows.first() == Some(&0) {
        return None;
    }
    rows.sort_unstable_by_key(|x| x.count_ones());
    let mut mins = vec![];
    for x in rows {
        if !mins.iter().any(|p| x & p == *p) {
            mins.push(x)
        }
    }
    fn rec(p: M, c: u32, m: &[M], w: &[u32], fuel: &mut usize) -> Option<M> {
        if *fuel == 0 {
            return None;
        }
        *fuel -= 1;
        let mut pool = 0;
        let mut best = 53;
        for &r in m {
            if r & p != 0 {
                continue;
            }
            let len = r.count_ones();
            if len < best {
                pool = r;
                best = len
            }
            if best == 1 {
                break;
            }
        }
        if best == 53 {
            return Some(p);
        }
        while pool != 0 {
            let b = bit(pool);
            pool ^= b;
            let v = w[b.trailing_zeros() as usize];
            if v <= c {
                if let Some(p) = rec(p | b, c - v, m, w, fuel) {
                    return Some(p);
                }
            }
        }
        None
    }
    rec(0, budget, &mins, &cost, &mut 10000)
}
