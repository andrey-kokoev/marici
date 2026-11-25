// Join actual blue-triple tables to realize each fixed red template. Enumerate all orientations of a seed triple. At later positions use the narrowest applicable triple fiber, or pair projection, with all other red, blue-pair and blue-triple constraints tested exactly. Repetition is not disallowed.
#[allow(dead_code)]
mod join {
    include!("ramsey312_google_three_step.rs");
    use std::collections::HashMap;
    fn pair(i: u32, j: u32) -> u64 {
        ((i.min(j) as u64) << 32) | i.max(j) as u64
    }
    struct Step {
        red: Vec<usize>,
        blue: Vec<(usize, bool)>,
        tri: Vec<(usize, usize, bool)>,
        cap: u32,
    }
    struct C {
        a: Vec<M>,
        h: M,
        s: Vec<M>,
        src: Vec<u32>,
        by: HashMap<u64, Vec<u32>>,
        blue: Vec<Vec<u32>>,
        steps: Vec<Step>,
        memo: HashMap<(M, u32), bool>,
        nodes: [u64; 9],
        found: Option<[u32; 8]>,
    }
    impl C {
        fn rec(&mut self, p: &mut [u32; 8], i: usize) {
            self.nodes[i] += 1;
            if i == 8 {
                self.found = Some(*p);
                return;
            }
            let st = &self.steps[i];
            let mut candidates = &self.src;
            for &(j, c) in &st.blue {
                if c && self.blue[p[j] as usize].len() < candidates.len() {
                    candidates = &self.blue[p[j] as usize]
                }
            }
            for &(j, k, c) in &st.tri {
                if c {
                    let Some(f) = self.by.get(&pair(p[j], p[k])) else {
                        return;
                    };
                    if f.len() < candidates.len() {
                        candidates = f
                    }
                }
            }
            let cand = candidates.clone();
            'outer: for x in cand {
                let st = &self.steps[i];
                let s = self.s[x as usize];
                if s.count_ones() > st.cap || st.red.iter().any(|&j| s & self.s[p[j] as usize] != 0)
                {
                    continue;
                }
                for &(j, c) in &st.blue {
                    if c {
                        if !self.by.contains_key(&pair(x, p[j])) {
                            continue 'outer;
                        }
                    } else {
                        let key = (self.h & !(s | self.s[p[j] as usize]), 10);
                        if *self
                            .memo
                            .entry(key)
                            .or_insert_with(|| has(&self.a, key.0, key.1))
                        {
                            continue 'outer;
                        }
                    }
                }
                for &(j, k, c) in &st.tri {
                    if c {
                        if self
                            .by
                            .get(&pair(p[j], p[k]))
                            .map_or(true, |v| v.binary_search(&x).is_err())
                        {
                            continue 'outer;
                        }
                    } else {
                        let key = (
                            self.h & !(s | self.s[p[j] as usize] | self.s[p[k] as usize]),
                            9,
                        );
                        if *self
                            .memo
                            .entry(key)
                            .or_insert_with(|| has(&self.a, key.0, key.1))
                        {
                            continue 'outer;
                        }
                    }
                }
                p[i] = x;
                self.rec(p, i + 1);
                if self.found.is_some() {
                    return;
                }
            }
        }
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
        let raw: Vec<M> = fs::read_to_string(&args[3])
            .unwrap()
            .split_whitespace()
            .map(|x| x.parse().unwrap())
            .collect();
        let s = raw[1..].to_vec();
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
        let bytes = fs::read(&args[4]).unwrap();
        let triples: Vec<[u32; 3]> = bytes
            .chunks_exact(12)
            .map(|b| {
                std::array::from_fn(|j| u32::from_le_bytes(b[4 * j..4 * j + 4].try_into().unwrap()))
            })
            .collect();
        let mut by: HashMap<u64, Vec<u32>> = HashMap::new();
        for p in &triples {
            for i in 0..3 {
                by.entry(pair(p[(i + 1) % 3], p[(i + 2) % 3]))
                    .or_default()
                    .push(p[i]);
            }
        }
        let mut blue = vec![vec![]; s.len()];
        for (&key, v) in &mut by {
            v.sort_unstable();
            v.dedup();
            let (i, j) = ((key >> 32) as u32, key as u32);
            blue[i as usize].push(j);
            if i != j {
                blue[j as usize].push(i)
            }
        }
        let src = (0..s.len() as u32)
            .filter(|&i| !blue[i as usize].is_empty())
            .collect();
        let mut ctx = C {
            h,
            a,
            s,
            src,
            blue,
            by,
            steps: vec![],
            memo: HashMap::new(),
            nodes: [0; 9],
            found: None,
        };
        for line in fs::read_to_string(&args[5]).unwrap().lines() {
            let b: Vec<usize> = line
                .split_whitespace()
                .map(|v| v.parse().unwrap())
                .collect();
            let red = |i: usize, j: usize| b[i] >> j & 1 == 1;
            let deg = |i: usize| b[i].count_ones();
            let lim = args.get(6).map_or(2, |x| x.parse::<u32>().unwrap());
            let ct = |i: usize, j: usize, k: usize| {
                (!red(i, j) && !red(i, k) && !red(j, k))
                    && [i, j, k].iter().filter(|&&v| deg(v) == 3).count() as u32 >= lim
            };
            let cp = |i: usize, j: usize| (0..8).any(|k| k != i && k != j && ct(i, j, k));
            let mut steps = vec![];
            for i in 0..8 {
                let mut st = Step {
                    red: vec![],
                    blue: vec![],
                    tri: vec![],
                    cap: 11 - deg(i),
                };
                for j in 0..i {
                    if red(i, j) {
                        st.red.push(j)
                    } else {
                        st.blue.push((j, cp(i, j)));
                        for k in 0..j {
                            if !red(i, k) && !red(j, k) {
                                st.tri.push((j, k, ct(i, j, k)))
                            }
                        }
                    }
                }
                steps.push(st)
            }
            assert!(ct(0, 1, 2));
            ctx.steps = steps;
            ctx.nodes = [0; 9];
            ctx.found = None;
            let mut p = [0; 8];
            'outer: for t in &triples {
                for ord in [
                    [0, 1, 2],
                    [0, 2, 1],
                    [1, 0, 2],
                    [1, 2, 0],
                    [2, 0, 1],
                    [2, 1, 0],
                ] {
                    for i in 0..3 {
                        p[i] = t[ord[i]]
                    }
                    if (0..3).any(|i| ctx.s[p[i] as usize].count_ones() > ctx.steps[i].cap) {
                        continue;
                    }
                    ctx.rec(&mut p, 3);
                    if ctx.found.is_some() {
                        break 'outer;
                    }
                }
            }
            println!(
                "template={b:?} nodes={:?} found={:?}",
                ctx.nodes,
                ctx.found.map(|p| p.map(|i| ctx.s[i as usize]))
            );
        }
    }
}
fn main() {
    join::run()
}
