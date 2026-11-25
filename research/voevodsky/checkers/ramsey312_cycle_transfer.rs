// Transfer cyclic templates to held-out cores. Pin endpoints to the two deleted originals outside the triple, then enlarge projected masks. Require every circular edge, not just a packing score.
#[allow(dead_code)]
mod run {
    include!("ramsey312_google_three_step.rs");
    fn fit(a: &[M], h: M, x: M, y: M) -> bool {
        x != y && (x & y == 0 || !has(a, h & !(x | y), 10))
    }
    fn rec(a: &[M], h: M, ls: &[Vec<M>], out: &mut Vec<M>) -> bool {
        let n = ls.len();
        let i = out.len();
        if i == n {
            return true;
        }
        for &x in &ls[i] {
            if out
                .iter()
                .enumerate()
                .all(|(j, &y)| x != y && ((i - j < n / 3 || i - j > n - n / 3) || fit(a, h, x, y)))
            {
                out.push(x);
                if rec(a, h, ls, out) {
                    return true;
                }
                out.pop();
            }
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
                    .fold(0, |m, (i, &v)| m | (((v - 48) as M) << i))
            })
            .collect();
        let f = (1 << 52) - 1;
        let parse = |l: &str| {
            l.split_whitespace()
                .map(|v| v.parse::<M>().unwrap())
                .collect::<Vec<_>>()
        };
        let cycles: Vec<_> = fs::read_to_string(&args[2])
            .unwrap()
            .lines()
            .map(parse)
            .collect();
        let (mut cores, mut hits) = (0, 0);
        for l in fs::read_to_string(&args[3]).unwrap().lines() {
            let r = parse(l);
            let d = r[0];
            let h = f ^ d;
            cores += 1;
            'templates: for t in &cycles {
                let tri = t[..3].iter().fold(0, |m, i| m | 1 << i);
                if d & tri != tri {
                    continue;
                }
                let e = d ^ tri;
                let u = a[e.trailing_zeros() as usize] & h;
                let v = a[(e & (e - 1)).trailing_zeros() as usize] & h;
                assert!(fit(&a, h, u, v));
                let free = args.get(4).map_or(false, |arg| arg == "--free");
                let mut ls = vec![];
                for p in &t[3..] {
                    let p = p & h;
                    let mut opts: Vec<_> = r[1..]
                        .iter()
                        .copied()
                        .filter(|&x| x & p == p && (free || (fit(&a, h, x, u) && fit(&a, h, x, v))))
                        .collect();
                    opts.sort_unstable_by_key(|x| std::cmp::Reverse(x.count_ones()));
                    if opts.is_empty() {
                        break;
                    }
                    ls.push(opts)
                }
                if ls.len() != t.len() - 3 {
                    continue;
                }
                if free {
                    let mut end = vec![];
                    let center = t[..3].iter().fold(h, |m, i| m & a[*i as usize]);
                    for &x in &r[1..] {
                        if x & center == center {
                            continue;
                        }
                        let mut mm = vec![];
                        for opts in &ls {
                            let allowed: Vec<_> = opts
                                .iter()
                                .filter(|&&s| fit(&a, h, x, s))
                                .copied()
                                .collect();
                            if allowed.is_empty() {
                                break;
                            }
                            mm.push(allowed)
                        }
                        if mm.len() == ls.len() {
                            end.push((x, mm))
                        }
                    }
                    for (i, (u, ul)) in end.iter().enumerate() {
                        for (v, vl) in &end[..i] {
                            if !fit(&a, h, *u, *v) {
                                continue;
                            }
                            let ll: Vec<Vec<_>> = ul
                                .iter()
                                .zip(vl)
                                .map(|(l, r)| l.iter().filter(|s| r.contains(s)).copied().collect())
                                .collect();
                            if ll.iter().any(|l| l.is_empty()) {
                                continue;
                            }
                            let mut c = vec![];
                            if rec(&a, h, &ll, &mut c) {
                                print!("{d} {tri} {u} {v}");
                                for x in c {
                                    print!(" {x}")
                                }
                                println!();
                                hits += 1;
                                break 'templates;
                            }
                        }
                    }
                    continue;
                }
                let mut c = vec![];
                if rec(&a, h, &ls, &mut c) {
                    print!("{d} {tri} {u} {v}");
                    for x in c {
                        print!(" {x}")
                    }
                    println!();
                    hits += 1;
                    break;
                }
            }
        }
        eprintln!("cores={cores} hits={hits}")
    }
}
fn main() {
    run::go()
}
