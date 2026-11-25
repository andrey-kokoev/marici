// For each D, keep selected originals' 43-core neighborhoods pinned but recolor their mutual edges; release others entirely. Enumerate resulting valid partial graphs and compatible tuples of unrestricted remaining newcomers. A nonempty tuple needs joint verification.
#[allow(dead_code)]
mod scan {
    include!("ramsey312_google_three_step.rs");
    use std::collections::HashMap;
    fn clique(a: &[M], h: M, s: &[M], p: &[usize], k: usize, q: &mut Vec<usize>) -> bool {
        if k == 0 {
            return true;
        }
        for (j, &i) in p.iter().enumerate() {
            // Start at j, not j+1: a self-compatible support can be repeated.
            q.push(i);
            let rest: Vec<_> = p[j..]
                .iter()
                .copied()
                .filter(|&j| s[i] & s[j] == 0 || !has(a, h & !(s[i] | s[j]), 10))
                .collect();
            if !rest.is_empty() || k == 1 {
                if clique(a, h, s, &rest, k - 1, q) {
                    return true;
                }
            }
            q.pop();
        }
        false
    }
    include!("ramsey312_release_clique.rs");
    include!("ramsey312_degree_budget.rs");
    pub fn run() {
        let args: Vec<_> = env::args().collect();
        let release: u32 = args[3].parse().unwrap();
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
        let f = (1 << 52) - 1;
        let mut cache = HashMap::new();
        let (mut tries, mut ok, mut pos) = (0, 0, 0);
        for line in fs::read_to_string(&args[2]).unwrap().lines() {
            let d: M = line.parse().unwrap();
            let core = f ^ d;
            let mut free = d;
            loop {
                if free.count_ones() == release {
                    let keep = d ^ free;
                    let h = f ^ free;
                    let vs: Vec<_> = (0..52).filter(|i| keep >> i & 1 == 1).collect();
                    let mut opt = vec![];
                    for (k, &i) in vs.iter().enumerate() {
                        for &j in &vs[..k] {
                            if core & a[i] & a[j] == 0 && !has(&a, core & !(a[i] | a[j]), 10) {
                                opt.push((i, j))
                            }
                        }
                    }
                    for mask in 0..(1u64 << opt.len()) {
                        tries += 1;
                        let flips: Vec<_> = opt
                            .iter()
                            .enumerate()
                            .filter_map(|(k, &v)| (mask >> k & 1 == 1).then_some(v))
                            .collect();
                        let (valid, hit) =
                            *cache.entry((free, flips.clone())).or_insert_with(|| {
                                let mut g: Vec<_> = a.iter().map(|x| x & h).collect();
                                for &(i, j) in &flips {
                                    g[i] ^= 1 << j;
                                    g[j] ^= 1 << i
                                }
                                if (0..52).any(|i| h >> i & 1 == 1 && g[i].count_ones() > 11)
                                    || vs.iter().any(|&i| {
                                        vs.iter().any(|&j| g[i] >> j & 1 == 1 && g[i] & g[j] != 0)
                                    })
                                    || has(&g, h, 12)
                                {
                                    return (false, false);
                                }
                                if release == 5 && flips.is_empty() {
                                    println!("P {d} {free}");
                                    return (true, false);
                                } // full five-deletion census of the unmodified matrix
                                let low = (0..52)
                                    .filter(|&i| h >> i & 1 == 1 && g[i].count_ones() < 11)
                                    .fold(0, |m, i| m | 1 << i);
                                let mut es = vec![];
                                sets(&g, h, 11, 0, &mut es);
                                let mut req: Vec<_> = es.iter().map(|t| t & low).collect();
                                req.sort_unstable();
                                req.dedup();
                                req.sort_unstable_by_key(|v| v.count_ones());
                                let mut mn = vec![];
                                for x in req {
                                    if !mn.iter().any(|y| x & y == *y) {
                                        mn.push(x)
                                    }
                                }
                                let mut s = vec![];
                                supports(&g, low, 0, &mn, &mut s);
                                if args.get(4).is_some_and(|x| x == "--degree") {
                                    let cert = degree_certificate(&g, h, &s, release);
                                    print!(
                                        "D {d} {free} {} {} {}",
                                        flips.len(),
                                        s.len(),
                                        cert.unwrap_or(0)
                                    );
                                    for (i, j) in &flips {
                                        print!(" {i}:{j}")
                                    }
                                    println!();
                                    return (true, cert.is_none());
                                }
                                if args.get(4).is_some_and(|x|x=="--bounded"){if s.is_empty()||degree_certificate(&g,h,&s,release).is_some(){return(true,false)}if s.len()>8000{print!("L {d} {free} {} {}",flips.len(),s.len());for(i,j)in &flips{print!(" {i}:{j}")}println!();return(true,true)}}
                                let mut q = vec![];
                                let centers: Vec<_> = (0..52)
                                    .filter(|i| free >> i & 1 != 0)
                                    .map(|i| a[i] & h)
                                    .collect();
                                let hit = if release >= 4 {
                                    fast(&g, h, &s, 1 + release as usize, &centers, &mut q)
                                } else {
                                    clique(
                                        &g,
                                        h,
                                        &s,
                                        &(0..s.len()).collect::<Vec<_>>(),
                                        1 + release as usize,
                                        &mut q,
                                    )
                                };
                                print!("G {d} {free} {} {} {}", flips.len(), s.len(), hit as u8);
                                for (i, j) in &flips {
                                    print!(" {i}:{j}")
                                }
                                for i in q {
                                    print!(" +{}", s[i])
                                }
                                println!();
                                (true, hit)
                            });
                        ok += valid as usize;
                        pos += hit as usize;
                    }
                }
                if free == 0 {
                    break;
                }
                free = (free - 1) & d;
            }
        }
        println!("S {release} {tries} {} {ok} {pos}", cache.len());
    }
}
fn main() {
    scan::run()
}
