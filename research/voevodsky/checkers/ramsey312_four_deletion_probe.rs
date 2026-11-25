// Input: witness matrix and a file of four vertex labels per line. Failed nearest-anchor tests emit full support list for exact follow-up.
#[allow(dead_code)]
mod search {
    include!("ramsey312_google_three_step.rs");
    fn ten(a: &[M], mut p: M, k: u32) -> Option<M> {
        if k == 0 {
            return Some(0);
        }
        while p.count_ones() >= k {
            let b = bit(p);
            p ^= b;
            if let Some(t) = ten(a, p & !a[b.trailing_zeros() as usize], k - 1) {
                return Some(b | t);
            }
        }
        None
    }
    include!("ramsey312_six_search.rs");
    pub fn run() {
        let args: Vec<_> = env::args().collect();
        let data: Vec<_> = fs::read_to_string(&args[1])
            .unwrap()
            .bytes()
            .filter(|b| *b == 48 || *b == 49)
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
        let export = args.get(3).is_some_and(|arg| arg == "--supports");
        let sweep = args.get(3).is_some_and(|arg| arg == "--sweep");
        let mut prefix = 0;
        let mut subset = vec![];
        for line in fs::read_to_string(&args[2]).unwrap().lines() {
            let d: Vec<usize> = line
                .split_whitespace()
                .map(|x| x.parse().unwrap())
                .collect();
            let h = d.iter().fold(f, |m, i| m & !(1 << i));
            assert!(d.len() >= 4 && h.count_ones() as usize + d.len() == 52);
            let low = (0..52)
                .filter(|&i| h >> i & 1 != 0 && (a[i] & h).count_ones() < 11)
                .fold(0, |m, i| m | 1 << i);
            let pre = d[..3].iter().fold(0, |m, i| m | 1 << i);
            if prefix != pre {
                prefix = pre;
                subset.clear();
                subset.extend(elev.iter().copied().filter(|x| x & pre == 0));
            }
            let mut req: Vec<_> = subset
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
            let anchors: Vec<_> = d.iter().map(|&i| a[i] & h).collect();
            assert!(anchors.iter().all(|x| s.contains(x)));
            if export {
                s.sort_unstable();
                print!("{}", f ^ h);
                for x in &s {
                    print!(" {x}")
                }
                println!();
                continue;
            }
            let mut sig = vec![(h, 0); d.len()];
            for x in &s {
                let j = (0..d.len())
                    .min_by_key(|&j| (anchors[j] ^ x).count_ones())
                    .unwrap();
                sig[j].0 &= x;
                sig[j].1 |= x
            }
            let cert = sig
                .iter()
                .map(|&(m, u)| {
                    if m == 0 {
                        None
                    } else {
                        Some((bit(m), ten(&a, h & !u, 10)?))
                    }
                })
                .collect::<Option<Vec<_>>>();
            if sweep {
                assert_eq!(d.len(), 5);
                let (tag, c) = if let Some(cl) = &cert {
                    (
                        "near",
                        cl.iter().flat_map(|&(b, t)| [b, t]).collect::<Vec<_>>(),
                    )
                } else {
                    fallback(&a, h, &s, &anchors)
                };
                print!("{} {} {}", f ^ h, s.len(), tag);
                for x in c {
                    print!(" {x}")
                }
                println!();
                continue;
            }
            print!("{} {}", line, s.len());
            if let Some(c) = cert {
                assert!(s
                    .iter()
                    .all(|x| c.iter().any(|(b, t)| x & b != 0 && x & t == 0)));
                print!(" OK");
                for (b, t) in c {
                    print!(" {b} {t}")
                }
            } else {
                print!(" RAW");
                for x in s {
                    print!(" {x}")
                }
            }
            println!()
        }
    }
}
fn main() {
    search::run()
}
