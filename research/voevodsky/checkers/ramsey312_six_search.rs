// Exact fallback after nearest-anchor cover fails. Shared-ten pruning constructs the compatibility graph without testing every pair by DFS. Clone each support 6 times only if looped (clique search below instead permits repetitions on loops).
fn fallback(a: &[M], h: M, s: &[M], anchors: &[M]) -> (&'static str, Vec<M>) {
    let mut sig: Vec<_> = anchors
        .iter()
        .map(|&x| (x, x, ten(a, h & !x, 10).unwrap_or(0)))
        .collect();
    let mut ordered = s.to_vec();
    ordered.sort_unstable_by_key(|x| {
        (
            std::cmp::Reverse(anchors.iter().map(|z| (x ^ z).count_ones()).min().unwrap()),
            *x,
        )
    });
    let mut good = true;
    for x in ordered {
        let mut ord = [0, 1, 2, 3, 4];
        ord.sort_unstable_by_key(|&j| (x ^ anchors[j]).count_ones());
        let mut done = false;
        for j in ord {
            let (b, u, t) = sig[j];
            if b & x == 0 {
                continue;
            }
            let un = u | x;
            let nt = if t != 0 && t & x == 0 {
                Some(t)
            } else {
                ten(a, h & !un, 10)
            };
            if let Some(n) = nt {
                sig[j] = (b & x, un, n);
                done = true;
                break;
            }
        }
        if !done {
            good = false;
            break;
        }
    }
    if good {
        return (
            "greedy",
            sig.iter().flat_map(|&(b, _, t)| [bit(b), t]).collect(),
        );
    }
    let n = s.len();
    let mut g = vec![vec![]; n];
    for i in 0..n {
        let mut witnesses = vec![];
        for j in 0..=i {
            if s[i] & s[j] != 0 {
                if witnesses.iter().any(|t| s[j] & t == 0) {
                    continue;
                }
                if let Some(t) = ten(a, h & !(s[i] | s[j]), 10) {
                    witnesses.push(t);
                    continue;
                }
            }
            g[i].push(j);
            if j != i {
                g[j].push(i)
            }
        }
    }
    for e in &mut g {
        e.sort_unstable()
    }
    fn rec(g: &[Vec<usize>], cand: &[usize], chosen: &mut Vec<usize>) -> bool {
        if chosen.len() == 6 {
            return true;
        }
        for (k, &i) in cand.iter().enumerate() {
            chosen.push(i);
            let tail: Vec<_> = cand[k..]
                .iter()
                .copied()
                .filter(|v| g[i].binary_search(v).is_ok())
                .collect();
            if rec(g, &tail, chosen) {
                return true;
            }
            chosen.pop();
        }
        false
    }
    let mut c = vec![];
    if rec(&g, &(0..n).collect::<Vec<_>>(), &mut c) {
        ("K6", c.iter().map(|&i| s[i]).collect())
    } else {
        ("noK6", vec![])
    }
}
