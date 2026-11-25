// Core-only classifier, insert call immediately after support generation, before pair joins.
fn side_probes(
    a: &[M],
    h: M,
    s: &[M],
    u: usize,
    v: usize,
) -> (
    Vec<bool>,
    Vec<bool>,
    Vec<bool>,
    Vec<bool>,
    [M; 4],
    Vec<(M, M)>,
) {
    let mut masks = s.to_vec();
    masks.sort_unstable();
    let mut anchors = (0, 0);
    let mut max = 0;
    for (i, &x) in masks.iter().enumerate() {
        for &y in &masks[..i] {
            let d = (x ^ y).count_ones();
            if d > max {
                anchors = (y, x);
                max = d
            }
        }
    }
    let classify = |p: M, q: M| {
        s.iter()
            .map(|&x| (x ^ p).count_ones() > (x ^ q).count_ones())
            .collect::<Vec<_>>()
    };
    let orig = classify(a[u] & h, a[v] & h);
    let dia = classify(anchors.0, anchors.1);
    // An even simpler rule: find a single core vertex membership bit certifying both sides. No compatibility queries.
    fn witness(a: &[M], p: M, k: u32) -> Option<M> {
        if k == 0 {
            return Some(0);
        }
        let mut q = p;
        while q.count_ones() >= k {
            let b = bit(q);
            q ^= b;
            if let Some(rest) = witness(a, q & !a[b.trailing_zeros() as usize], k - 1) {
                return Some(b | rest);
            }
        }
        None
    }
    let certify = |side: &[bool]| {
        let mut w = vec![];
        for z in [false, true] {
            let mut intersection = h;
            let mut union = 0;
            let mut count = 0;
            for (&x, &c) in s.iter().zip(side) {
                if c == z {
                    count += 1;
                    intersection &= x;
                    union |= x
                }
            }
            if count == 0 || intersection == 0 {
                return vec![];
            }
            if let Some(t) = witness(a, h & !union, 10) {
                w.push((bit(intersection), t))
            } else {
                return vec![];
            }
        }
        w
    };
    let wd = certify(&dia);
    let mut wb = vec![];
    let mut one = vec![];
    for i in 0..52 {
        if h >> i & 1 == 0 {
            continue;
        }
        let b: Vec<_> = s.iter().map(|x| x >> i & 1 != 0).collect();
        wb = certify(&b);
        if !wb.is_empty() {
            one = b;
            break;
        }
    }
    (
        orig,
        dia,
        one,
        vec![!wd.is_empty()],
        [
            anchors.0,
            anchors.1,
            wd.first().map_or(0, |p| p.1),
            wd.get(1).map_or(0, |p| p.1),
        ],
        wb,
    )
}
