// Shrink maximal blue triples to degree-capped envelopes (8,8,9). For any actual bounded triple and any containing envelope, shrinking an oversized slot towards its actual support remains legal. Pick the slot with fewest permitted one-bit removals.
#[allow(dead_code)]
mod scan {
    include!("ramsey312_google_three_step.rs");
    use std::collections::HashMap;
    struct Ctx {
        a: Vec<M>,
        h: M,
        dom: HashSet<M>,
        seen: HashSet<[M; 3]>,
        memo: HashMap<(M, u32), bool>,
        leaves: HashSet<[M; 3]>,
    }
    impl Ctx {
        fn blue(&mut self, u: M, k: u32) -> bool {
            let a = &self.a;
            let p = self.h & !u;
            *self.memo.entry((p, k)).or_insert_with(|| !has(a, p, k))
        }
        fn visit(&mut self, mut q: [M; 3]) {
            if q[0] > q[1] {
                q.swap(0, 1)
            }
            if !self.seen.insert(q) {
                return;
            }
            let mut best = None;
            for i in 0..3 {
                if q[i].count_ones() <= if i == 2 { 9 } else { 8 } {
                    continue;
                }
                let mut ok = vec![];
                let mut p = q[i];
                while p != 0 {
                    let b = bit(p);
                    p ^= b;
                    let x = q[i] ^ b;
                    let y = q[(i + 1) % 3];
                    let z = q[(i + 2) % 3];
                    if self.dom.contains(&x)
                        && self.blue(x | y, 10)
                        && self.blue(x | z, 10)
                        && self.blue(x | y | z, 9)
                    {
                        ok.push(x)
                    }
                }
                if ok.is_empty() {
                    return;
                }
                if best
                    .as_ref()
                    .map_or(true, |(_, v): &(usize, Vec<M>)| ok.len() < v.len())
                {
                    best = Some((i, ok))
                }
            }
            if let Some((i, ok)) = best {
                for x in ok {
                    let mut child = q;
                    child[i] = x;
                    self.visit(child)
                }
            } else {
                self.leaves.insert(q);
            }
        }
    }
    pub fn run() {
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
        let mut c = Ctx {
            a,
            h,
            dom: d[1..].iter().copied().collect(),
            seen: HashSet::new(),
            memo: HashMap::new(),
            leaves: HashSet::new(),
        };
        for l in fs::read_to_string(&args[4])
            .unwrap()
            .lines()
            .filter(|l| l.starts_with("T "))
        {
            let q: Vec<M> = l
                .split_whitespace()
                .skip(1)
                .map(|x| x.parse().unwrap())
                .collect();
            for i in 0..3 {
                c.visit([q[(i + 1) % 3], q[(i + 2) % 3], q[i]])
            }
        }
        eprintln!(
            "states={} leaves={} unions={}",
            c.seen.len(),
            c.leaves.len(),
            c.memo.len()
        );
        let mut out: Vec<_> = c.leaves.into_iter().collect();
        out.sort_unstable();
        for q in out {
            println!("{} {} {}", q[0], q[1], q[2])
        }
    }
}
fn main() {
    scan::run()
}
