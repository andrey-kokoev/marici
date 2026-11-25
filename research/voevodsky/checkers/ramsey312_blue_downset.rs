// Complete downward closure of valid, capped blue triples and export a deduplicated table of actual tuples. Each removal is accepted iff support legality and every blue subset are preserved.
#[allow(dead_code)]
mod scan {
    include!("ramsey312_google_three_step.rs");
    use std::collections::HashMap;
    struct C {
        h: M,
        a: Vec<M>,
        s: Vec<M>,
        ids: HashMap<M, u32>,
        seen: HashSet<[u32; 3]>,
        memo: HashMap<M, u8>,
    }
    impl C {
        fn ok(&mut self, u: M, k: u8) -> bool {
            let e = self.memo.entry(u).or_insert(0);
            let flag = 1 << (k - 9);
            if *e & flag == 0 {
                let v = has(&self.a, self.h & !u, k as u32);
                *e |= flag;
                if v {
                    *e |= flag << 2
                }
            }
            *e & (flag << 2) == 0
        }
        fn visit(&mut self, mut q: [u32; 3]) {
            q.sort_unstable();
            if !self.seen.insert(q) {
                return;
            }
            for i in 0..3 {
                let x = self.s[q[i] as usize];
                let y = self.s[q[(i + 1) % 3] as usize];
                let z = self.s[q[(i + 2) % 3] as usize];
                let mut p = x;
                while p != 0 {
                    let b = bit(p);
                    p ^= b;
                    let t = x ^ b;
                    if let Some(&j) = self.ids.get(&t) {
                        if self.ok(t | y, 10) && self.ok(t | z, 10) && self.ok(t | y | z, 9) {
                            let mut r = q;
                            r[i] = j;
                            self.visit(r)
                        }
                    }
                }
            }
        }
    }
    pub fn run() {
        let args: Vec<_> = env::args().collect();
        let b: Vec<_> = fs::read_to_string(&args[1])
            .unwrap()
            .bytes()
            .filter(|&b| b == 48 || b == 49)
            .collect();
        let mut a: Vec<M> = b
            .chunks(52)
            .map(|r| {
                r.iter()
                    .enumerate()
                    .fold(0, |m, (i, &x)| m | (((x - 48) as M) << i))
            })
            .collect();
        let raw: Vec<M> = fs::read_to_string(&args[3])
            .unwrap()
            .split_whitespace()
            .map(|t| t.parse().unwrap())
            .collect();
        let text = fs::read_to_string(&args[2]).unwrap();
        let z: Vec<_> = text
            .lines()
            .nth(raw[0] as usize)
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
        let s = raw[1..].to_vec();
        let ids = s.iter().enumerate().map(|(i, &x)| (x, i as u32)).collect();
        let mut c = C {
            a,
            h,
            s,
            ids,
            seen: HashSet::new(),
            memo: HashMap::new(),
        };
        for l in fs::read_to_string(&args[4]).unwrap().lines() {
            let q: Vec<_> = l
                .split_whitespace()
                .map(|t| c.ids[&t.parse().unwrap()])
                .collect();
            c.visit([q[0], q[1], q[2]])
        }
        eprintln!("actual {} triples", c.seen.len());
        use std::io::{BufWriter, Write};
        let mut w = BufWriter::new(fs::File::create(&args[5]).unwrap());
        for q in c.seen {
            for i in q {
                w.write_all(&i.to_le_bytes()).unwrap()
            }
        }
    }
}
fn main() {
    scan::run()
}
