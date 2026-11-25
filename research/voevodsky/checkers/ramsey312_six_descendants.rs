// Full K7 test and three-endpoint test on six-deletion descendants. Greedy independent color classes bound each clique-search prefix.
#[allow(dead_code)]
mod scan {
    include!("ramsey312_google_three_step.rs");
    fn witness(a: &[M], mut p: M, k: u32) -> Option<M> {
        if k == 0 {
            return Some(0);
        }
        while p.count_ones() >= k {
            let b = bit(p);
            p ^= b;
            if let Some(t) = witness(a, p & !a[b.trailing_zeros() as usize], k - 1) {
                return Some(t | b);
            }
        }
        None
    }
    fn edge(g: &[Vec<M>], i: usize, j: usize) -> bool {
        g[i][j / 64] >> (j % 64) & 1 == 1
    }
    fn clique(
        g: &[Vec<M>],
        mut p: Vec<usize>,
        k: usize,
        out: &mut Vec<usize>,
        emit: Option<(M, &[M])>,
    ) -> bool {
        if k == 0 {
            if let Some((d, s)) = emit {
                print!("K {d}");
                for &i in out.iter() {
                    print!(" {}", s[i])
                }
                println!();
                return false;
            }
            return true;
        }
        if p.len() < k {
            return false;
        }
        let mut order = vec![];
        let mut col = 0;
        while !p.is_empty() {
            col += 1;
            let mut cl = vec![];
            p.retain(|&i| {
                if cl.iter().all(|&j| !edge(g, i, j)) {
                    cl.push(i);
                    false
                } else {
                    true
                }
            });
            order.extend(cl.into_iter().map(|i| (i, col)))
        }
        while let Some((i, c)) = order.pop() {
            if c < k {
                return false;
            }
            let q = order
                .iter()
                .filter_map(|&(j, _)| edge(g, i, j).then_some(j))
                .collect();
            out.push(i);
            if clique(g, q, k - 1, out, emit) {
                return true;
            }
            out.pop();
        }
        false
    }
    pub fn go() {
        let args: Vec<_> = env::args().collect();
        let bs: Vec<_> = fs::read_to_string(&args[1])
            .unwrap()
            .bytes()
            .filter(|&x| x == 48 || x == 49)
            .collect();
        let a: Vec<M> = bs
            .chunks(52)
            .map(|r| {
                r.iter()
                    .enumerate()
                    .fold(0, |m, (i, &x)| m | (((x - 48) as M) << i))
            })
            .collect();
        let parse = |l: &str| {
            l.split_whitespace()
                .map(|v| v.parse::<M>().unwrap())
                .collect::<Vec<_>>()
        };
        let tm: Vec<_> = fs::read_to_string(&args[2])
            .unwrap()
            .lines()
            .map(parse)
            .collect();
        for l in fs::read_to_string(&args[3]).unwrap().lines() {
            let r = parse(l);
            let (d, s) = (r[0], &r[1..]);
            let h = ((1 << 52) - 1) ^ d;
            let n = s.len();
            let mut g: Vec<Vec<M>> = vec![vec![0; (n + 63) / 64]; n];
            let mut edges = 0;
            for i in 0..n {
                let mut ws = vec![];
                for j in 0..=i {
                    if s[i] & s[j] != 0 {
                        if ws.iter().any(|t| s[j] & t == 0) {
                            continue;
                        }
                        if let Some(t) = witness(&a, h & !(s[i] | s[j]), 10) {
                            ws.push(t);
                            continue;
                        }
                    }
                    assert_ne!(i, j, "loop: {d} {}", s[i]);
                    g[i][j / 64] |= 1 << (j % 64);
                    g[j][i / 64] |= 1 << (i % 64);
                    edges += 1
                }
            }
            if args.get(4).is_some_and(|x| x == "--edges") {
                for i in 0..n {
                    for (w, &word) in g[i].iter().enumerate() {
                        let mut mask = word;
                        while mask != 0 {
                            let j = 64 * w + mask.trailing_zeros() as usize;
                            if j < i {
                                println!("{j} {i}")
                            }
                            mask &= mask - 1;
                        }
                    }
                }
                continue;
            }
            let mut p: Vec<_> = (0..n).collect();
            p.sort_unstable_by_key(|&i| {
                std::cmp::Reverse(g[i].iter().map(|z| z.count_ones()).sum::<u32>())
            });
            let mut win = vec![];
            if args.get(4).is_some_and(|x| x == "--all") {
                clique(&g, p, 7, &mut win, Some((d, s)));
                continue;
            }
            let k7 = clique(&g, p.clone(), 7, &mut win, None);
            let mut attach = vec![];
            let mut base = 0;
            for t in &tm {
                if d & t[0] != t[0] {
                    continue;
                }
                let mut ids: Vec<_> = t[1..]
                    .iter()
                    .map(|x| s.binary_search(&(x & h)).unwrap())
                    .collect();
                ids.sort_unstable();
                ids.dedup();
                let common = p
                    .iter()
                    .copied()
                    .filter(|&i| ids.iter().all(|&j| edge(&g, i, j)))
                    .collect();
                if clique(&g, common, 3, &mut attach, None) {
                    base = t[0];
                    print!("A {d} {base}");
                    for z in &attach {
                        print!(" {}", s[*z])
                    }
                    for z in &t[1..] {
                        print!(" {}", z & h)
                    }
                    println!();
                    break;
                }
            }
            println!("S {d} {n} {edges} {base} {}", k7 as u8);
            if k7 {
                print!("K {d}");
                for i in win {
                    print!(" {}", s[i])
                }
                println!()
            }
        }
    }
}
fn main() {
    scan::go()
}
