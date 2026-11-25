// Minimal-support red center with its three independent neighbors. Enlarge leaves subject to disjointness from the center; compute exact blue triples per center, including repetitions. Red-star existence requires center legal and all leaves jointly blue-extendible.
#[allow(dead_code)]
mod scan {
    include!("ramsey312_google_three_step.rs");
    fn tens(a: &[M], mut p: M, k: u32) -> Option<M> {
        if k == 0 {
            return Some(0);
        }
        while p.count_ones() >= k {
            let b = bit(p);
            p ^= b;
            if let Some(t) = tens(a, p & !a[b.trailing_zeros() as usize], k - 1) {
                return Some(t | b);
            }
        }
        None
    }
    pub fn go() {
        let args: Vec<_> = env::args().collect();
        let bs: Vec<_> = fs::read_to_string(&args[1])
            .unwrap()
            .bytes()
            .filter(|&b| b == 48 || b == 49)
            .collect();
        let mut a: Vec<M> = bs
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
        let text = fs::read_to_string(&args[2]).unwrap();
        let z: Vec<_> = text
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
        let s = &d[1..];
        let dom: HashSet<M> = s.iter().copied().collect();
        let mins: Vec<_> = s
            .iter()
            .copied()
            .filter(|x| !(0..52).any(|i| x >> i & 1 != 0 && dom.contains(&(x ^ (1 << i)))))
            .collect();
        for m in mins {
            let pool = h & !m;
            let v: Vec<_> = s
                .iter()
                .copied()
                .filter(|x| {
                    x & m == 0
                        && !(0..52)
                            .any(|i| (pool & !x) >> i & 1 != 0 && dom.contains(&(x | 1 << i)))
                })
                .collect();
            let mut adj = vec![vec![]; v.len()];
            for (i, &x) in v.iter().enumerate() {
                let mut ws = vec![];
                for (j, &y) in v[..=i].iter().enumerate() {
                    if ws.iter().any(|t| t & y == 0) {
                        continue;
                    }
                    if let Some(t) = tens(&a, h & !(x | y), 10) {
                        ws.push(t);
                        continue;
                    }
                    adj[i].push(j)
                }
            }
            let mut count = 0;
            for (i, edges) in adj.iter().enumerate() {
                for &j in edges {
                    for &k in &adj[j] {
                        if edges.binary_search(&k).is_ok() && !has(&a, h & !(v[i] | v[j] | v[k]), 9)
                        {
                            println!("T {m} {} {} {}", v[i], v[j], v[k]);
                            count += 1
                        }
                    }
                }
            }
            println!("S {m} {} {count}", v.len())
        }
    }
}
fn main() {
    scan::go()
}
