// Independent rebuild of the actual capped triple relation, with no use of the prior maximal triples, shrink decisions, or template joins. Group supports by one maximal extension ONLY as an exact blue-pair prefilter. Blue edges tested by explicit core ten-set bitsets; blue triples tested directly against the independent nines.
#[allow(dead_code)]
mod scan {
    include!("ramsey312_google_three_step.rs");
    use std::collections::HashMap;
    fn comp(x: &[M], y: &[M]) -> bool {
        x.iter().zip(y).all(|(a, b)| a & b == 0)
    }
    pub fn run() {
        let args: Vec<_> = env::args().collect();
        let bs: Vec<_> = fs::read_to_string(&args[1])
            .unwrap()
            .bytes()
            .filter(|&x| x == 48 || x == 49)
            .collect();
        let mut a: Vec<M> = bs
            .chunks(52)
            .map(|r| {
                r.iter()
                    .enumerate()
                    .fold(0, |m, (i, &x)| m | (((x - 48) as M) << i))
            })
            .collect();
        let r: Vec<M> = fs::read_to_string(&args[3])
            .unwrap()
            .split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect();
        let k = r[0] as usize;
        let s = &r[1..];
        let text = fs::read_to_string(&args[2]).unwrap();
        let z: Vec<_> = text.lines().nth(k).unwrap().split_whitespace().collect();
        let h = ((1 << 52) - 1) ^ z[2].parse::<M>().unwrap();
        for e in &z[5..] {
            let (i, j) = e.split_once(':').unwrap();
            let (i, j): (usize, usize) = (i.parse().unwrap(), j.parse().unwrap());
            a[i] ^= 1 << j;
            a[j] ^= 1 << i
        }
        let mut tens = vec![];
        sets(&a, h, 10, 0, &mut tens);
        let chunks = (tens.len() + 63) / 64;
        let mut mask = vec![vec![0u64; chunks]; 52];
        for (j, &t) in tens.iter().enumerate() {
            let mut p = t;
            while p != 0 {
                let b = bit(p);
                p ^= b;
                mask[b.trailing_zeros() as usize][j / 64] |= 1 << (j % 64)
            }
        }
        let get = |mut x: M| {
            let mut v = vec![!0; chunks];
            if tens.len() % 64 != 0 {
                v[chunks - 1] = (1 << (tens.len() % 64)) - 1
            }
            while x != 0 {
                let b = bit(x);
                x ^= b;
                for (v, m) in v.iter_mut().zip(&mask[b.trailing_zeros() as usize]) {
                    *v &= !m
                }
            }
            v
        };
        let mut groups: HashMap<M, Vec<usize>> = HashMap::new();
        let mut miss = vec![];
        for (i, &x) in s.iter().enumerate() {
            if x.count_ones() > 9 {
                miss.push(vec![]);
                continue;
            }
            miss.push(get(x));
            let mut p = h & !x;
            let mut q = x;
            while p != 0 {
                let b = bit(p);
                p ^= b;
                if a[b.trailing_zeros() as usize] & q == 0 {
                    q |= b
                }
            }
            groups.entry(q).or_default().push(i)
        }
        let gs: Vec<_> = groups.into_iter().map(|(x, is)| (get(x), is)).collect();
        let mut g = vec![vec![]; s.len()];
        for (i, (u, us)) in gs.iter().enumerate() {
            for (j, (v, vs)) in gs[..=i].iter().enumerate() {
                if !comp(u, v) {
                    continue;
                }
                let yy: Vec<_> = vs.iter().copied().filter(|&y| comp(u, &miss[y])).collect();
                for &x in us {
                    if !comp(v, &miss[x]) {
                        continue;
                    }
                    for &y in &yy {
                        if i == j && x < y {
                            continue;
                        }
                        if comp(&miss[x], &miss[y]) {
                            g[x.max(y)].push(x.min(y) as u32)
                        }
                    }
                }
            }
        }
        for l in &mut g {
            l.sort_unstable();
        }
        let bytes = fs::read(&args[4]).unwrap();
        let mut expected: HashSet<[u32; 3]> = bytes
            .chunks_exact(12)
            .map(|z| {
                std::array::from_fn(|i| u32::from_le_bytes(z[4 * i..4 * i + 4].try_into().unwrap()))
            })
            .collect();
        let mut ct = 0;
        let mut memo = HashMap::new();
        for (i, v) in g.iter().enumerate() {
            for &j in v {
                for &k in &g[j as usize] {
                    if [s[i], s[j as usize], s[k as usize]]
                        .iter()
                        .filter(|x| x.count_ones() == 9)
                        .count()
                        > 1
                        || v.binary_search(&k).is_err()
                    {
                        continue;
                    }
                    let p = h & !(s[i] | s[j as usize] | s[k as usize]);
                    if !*memo.entry(p).or_insert_with(|| has(&a, p, 9)) {
                        ct += 1;
                        assert!(expected.remove(&[k, j, i as u32]));
                    }
                }
            }
        }
        assert!(expected.is_empty());
        println!(
            "case={k} checked_supports={} blue_pairs={} verified_triples={ct}",
            s.len(),
            g.iter().map(Vec::len).sum::<usize>()
        )
    }
}
fn main() {
    scan::run()
}
