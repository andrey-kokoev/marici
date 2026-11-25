// With a maximal blue quadruple envelope, each further support must be red to some slot. At a proposed red-neighbor mask, maximize each slot by removing exactly the new neighbors it cannot share. For fixed colors this gives an exact feasibility check, by monotonicity.
#[allow(dead_code)]
mod run {
    include!("ramsey312_google_three_step.rs");
    use std::collections::HashMap;
    fn blue_ok(
        a: &[M],
        h: M,
        q: &[M; 4],
        ys: &[(M, u8)],
        patt: u64,
        cache: &mut HashMap<(M, u32), bool>,
    ) -> bool {
        let n = 4 + ys.len();
        let mut v = q.to_vec();
        let mut adj = vec![0usize; n];
        for (j, &(y, r)) in ys.iter().enumerate() {
            v.push(y);
            for i in 0..4 {
                if r >> i & 1 != 0 {
                    v[i] &= !y;
                    adj[i] |= 1 << (j + 4);
                    adj[j + 4] |= 1 << i
                }
            }
            for k in 0..j {
                if patt >> (j * (j - 1) / 2 + k) & 1 != 0 {
                    if y & ys[k].0 != 0 || r & ys[k].1 != 0 {
                        return false;
                    }
                    adj[k + 4] |= 1 << (j + 4);
                    adj[j + 4] |= 1 << (k + 4)
                }
            }
        }
        for i in 4..n {
            for j in 4..i {
                if adj[i] >> j & 1 != 0 && adj[i] & adj[j] != 0 {
                    return false;
                }
            }
        }
        for set in 1usize..1 << n {
            let mut union = 0;
            let mut rem = set;
            while rem != 0 {
                let i = rem.trailing_zeros() as usize;
                if adj[i] & set != 0 {
                    break;
                }
                union |= v[i];
                rem &= rem - 1
            }
            if rem != 0 {
                continue;
            }
            let key = (h & !union, 12 - set.count_ones());
            if *cache.entry(key).or_insert_with(|| has(a, key.0, key.1)) {
                return false;
            }
        }
        true
    }
    fn rec(
        a: &[M],
        h: M,
        q: &[M; 4],
        opts: &[(M, u8)],
        sel: &mut Vec<(M, u8)>,
        patt: u64,
        cache: &mut HashMap<(M, u32), bool>,
        nodes: &mut u64,
    ) -> bool {
        if sel.len() == 4 {
            return true;
        }
        let j = sel.len();
        for (i, &op) in opts.iter().enumerate() {
            sel.push(op);
            for red in 0u64..1 << j {
                let p = patt | (red << (j * j.saturating_sub(1) / 2));
                *nodes += 1;
                if blue_ok(a, h, q, sel, p, cache) && rec(a, h, q, &opts[i..], sel, p, cache, nodes)
                {
                    return true;
                }
            }
            sel.pop();
        }
        false
    }
    pub fn go() {
        let args: Vec<_> = env::args().collect();
        let b: Vec<_> = fs::read_to_string(&args[1])
            .unwrap()
            .bytes()
            .filter(|&x| x == 48 || x == 49)
            .collect();
        let mut a: Vec<M> = b
            .chunks(52)
            .map(|r| {
                r.iter()
                    .enumerate()
                    .fold(0, |m, (i, &x)| m | (((x - 48) as M) << i))
            })
            .collect();
        let d: Vec<M> = fs::read_to_string(&args[3])
            .unwrap()
            .split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect();
        let cs = fs::read_to_string(&args[2]).unwrap();
        let z: Vec<_> = cs
            .lines()
            .nth(d[0] as usize)
            .unwrap()
            .split_whitespace()
            .collect();
        let h = ((1 << 52) - 1) ^ z[2].parse::<M>().unwrap();
        for e in &z[5..] {
            let (i, j) = e.split_once(':').unwrap();
            let (i, j): (usize, usize) = (i.parse().unwrap(), j.parse().unwrap());
            a[i] ^= 1 << j;
            a[j] ^= 1 << i
        }
        let mut cache = HashMap::new();
        for (idx, l) in fs::read_to_string(&args[4]).unwrap().lines().enumerate() {
            let m: Vec<M> = l
                .split_whitespace()
                .skip(1)
                .map(|x| x.parse().unwrap())
                .collect();
            let q: [M; 4] = m[..4].try_into().unwrap();
            let lo = &m[4..];
            let forbidden = (0..52)
                .filter(|i| {
                    h >> i & 1 != 0
                        && (a[*i] & h).count_ones() as usize
                            + lo.iter().filter(|x| *x >> i & 1 != 0).count()
                            >= 11
                })
                .fold(0, |v, i| v | 1 << i);
            let mut opts = vec![];
            for &y in &d[1..] {
                if y & forbidden != 0 || y.count_ones() > 10 {
                    continue;
                }
                let rm = (0..4)
                    .filter(|&i| lo[i] & y == 0)
                    .fold(0u8, |v, i| v | 1 << i);
                let mut r = rm;
                while r != 0 {
                    if y.count_ones() + r.count_ones() <= 11
                        && blue_ok(&a, h, &q, &[(y, r)], 0, &mut cache)
                    {
                        opts.push((y, r))
                    }
                    r = (r - 1) & rm
                }
            }
            let mut sel = vec![];
            let mut nodes = 0;
            let found = rec(&a, h, &q, &opts, &mut sel, 0, &mut cache, &mut nodes);
            println!("{idx} {} {nodes} {found} {sel:?}", opts.len());
            if cache.len() > 1000000 {
                cache.clear()
            }
            if found {
                break;
            }
        }
    }
}
fn main() {
    run::go()
}
