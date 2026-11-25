// A mutually blue family can be enlarged memberwise to inclusion-maximal legal supports. Count all valid such maximal-support multisets through size 8, checking every blue subtuple against its core independence bound.
#[allow(dead_code)]
mod scan {
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
    fn go(
        a: &[M],
        h: M,
        s: &[M],
        g: &[Vec<usize>],
        p: &[usize],
        chosen: &mut Vec<usize>,
        un: &[(M, u32)],
        hist: &mut [u64; 9],
        ex: &mut [Vec<M>; 9],
    ) {
        if chosen.len() == 8 {
            return;
        }
        for (j, &i) in p.iter().enumerate() {
            let x = s[i];
            let mut next = vec![];
            let mut legal = true;
            for &(m, n) in un {
                let u = m | x;
                if n >= 2 && has(a, h & !u, 11 - n) {
                    legal = false;
                    break;
                }
                next.push((u, n + 1))
            }
            if !legal {
                continue;
            }
            chosen.push(i);
            let k = chosen.len();
            hist[k] += 1;
            if k==4||k==3{print!("{}",if k==4{"Q"}else{"T"});for &j in chosen.iter(){print!(" {}",s[j]);}println!();}
            if ex[k].is_empty() {
                ex[k] = chosen.iter().map(|&z| s[z]).collect()
            }
            let rest: Vec<_> = p[j..]
                .iter()
                .copied()
                .filter(|v| g[i].binary_search(v).is_ok())
                .collect();
            if !rest.is_empty() {
                next.extend_from_slice(un);
                go(a, h, s, g, &rest, chosen, &next, hist, ex)
            }
            chosen.pop();
        }
    }
    pub fn run() {
        let args: Vec<_> = env::args().collect();
        let bs: Vec<_> = fs::read_to_string(&args[1])
            .unwrap()
            .bytes()
            .filter(|&b| b == 48 || b == 49)
            .collect();
        let a: Vec<M> = bs
            .chunks(52)
            .map(|r| {
                r.iter()
                    .enumerate()
                    .fold(0, |m, (i, &x)| m | (((x - 48) as M) << i))
            })
            .collect();
        let text = fs::read_to_string(&args[2]).unwrap();
        let cases: Vec<_> = text.lines().collect();
        for l in fs::read_to_string(&args[3]).unwrap().lines() {
            let r: Vec<M> = l.split_whitespace().map(|v| v.parse().unwrap()).collect();
            let k = r[0] as usize;
            let z: Vec<_> = cases[k].split_whitespace().collect();
            let h = ((1 << 52) - 1) ^ z[2].parse::<M>().unwrap();
            let mut a = a.clone();
            for e in &z[5..] {
                let (i, j) = e.split_once(':').unwrap();
                let (i, j): (usize, usize) = (i.parse().unwrap(), j.parse().unwrap());
                a[i] ^= 1 << j;
                a[j] ^= 1 << i
            }
            let dom: HashSet<_> = r[1..].iter().copied().collect();
            let mut s: Vec<_> = dom
                .iter()
                .copied()
                .filter(|x| !(0..52).any(|i| x >> i & 1 == 0 && dom.contains(&(x | 1 << i))))
                .collect();
            s.sort_unstable();
            let mut g = vec![vec![]; s.len()];
            for (i, &x) in s.iter().enumerate() {
                let mut w = vec![];
                for (j, &y) in s[..=i].iter().enumerate() {
                    if w.iter().any(|t| y & t == 0) {
                        continue;
                    }
                    if let Some(t) = ten(&a, h & !(x | y), 10) {
                        w.push(t);
                        continue;
                    }
                    g[i].push(j);
                    if i != j {
                        g[j].push(i)
                    }
                }
            }
            for e in &mut g {
                e.sort_unstable()
            }
            let mut hist = [0; 9];
            let mut ex = Default::default();
            go(
                &a,
                h,
                &s,
                &g,
                &(0..s.len()).collect::<Vec<_>>(),
                &mut vec![],
                &[(0, 0)],
                &mut hist,
                &mut ex,
            );
            println!("{k} {:?} {:?}", hist, ex)
        }
    }
}
fn main() {
    scan::run()
}
