// Allow arbitrary recoloring among the nine restored originals with all their 43-core neighborhoods fixed. For every valid 52-vertex mutation test an unrestricted 53rd support.
#[allow(dead_code)]
mod scan {
    include!("ramsey312_google_three_step.rs");
    use std::collections::HashMap;
    pub fn go() {
        let args: Vec<_> = env::args().collect();
        let bs: Vec<_> = fs::read_to_string(&args[1])
            .unwrap()
            .bytes()
            .filter(|&x| x == 48 || x == 49)
            .collect();
        assert_eq!(bs.len(), 2704);
        let a: Vec<M> = bs
            .chunks(52)
            .map(|r| {
                r.iter()
                    .enumerate()
                    .fold(0, |m, (i, &x)| m | (((x - 48) as M) << i))
            })
            .collect();
        let mut cache = HashMap::new();
        let f = (1 << 52) - 1;
        for l in fs::read_to_string(&args[2]).unwrap().lines() {
            let d: M = l.parse().unwrap();
            let h = f ^ d;
            let vs: Vec<_> = (0..52).filter(|&i| d >> i & 1 == 1).collect();
            let mut flip = vec![];
            for (k, &i) in vs.iter().enumerate() {
                for &j in &vs[..k] {
                    if h & a[i] & a[j] == 0 && !has(&a, h & !(a[i] | a[j]), 10) {
                        flip.push((i, j))
                    }
                }
            }
            let mut valid = 0;
            let mut ext = 0;
            for mask in 0..(1u64 << flip.len()) {
                let key: Vec<_> = flip
                    .iter()
                    .enumerate()
                    .filter(|(i, _)| mask >> i & 1 != 0)
                    .map(|(_, e)| *e)
                    .collect();
                let (ok, n) = *cache.entry(key.clone()).or_insert_with(|| {
                    let mut g = a.clone();
                    for &(i, j) in &key {
                        g[i] ^= 1 << j;
                        g[j] ^= 1 << i
                    }
                    if g.iter().any(|x| x.count_ones() > 11)
                        || vs
                            .iter()
                            .any(|&i| vs.iter().any(|&j| g[i] >> j & 1 == 1 && g[i] & g[j] != 0))
                        || has(&g, f, 12)
                    {
                        return (false, 0);
                    }
                    let low = (0..52)
                        .filter(|&i| g[i].count_ones() < 11)
                        .fold(0, |m, i| m | 1 << i);
                    let mut es = vec![];
                    sets(&g, f, 11, 0, &mut es);
                    let req: Vec<_> = es.iter().map(|t| t & low).collect();
                    let mut s = vec![];
                    supports(&g, low, 0, &req, &mut s);
                    print!("G {d} {} {}", key.len(), s.len());
                    for (i, j) in key.iter() {
                        print!(" {i}:{j}")
                    }
                    for x in &s {
                        print!(" +{x}")
                    }
                    println!();
                    (true, s.len())
                });
                if ok {
                    valid += 1;
                    ext += n
                }
            }
            println!("S {d} {} {valid} {ext}", flip.len());
        }
        eprintln!("unique mutations considered {}", cache.len())
    }
}
fn main() {
    scan::go()
}
