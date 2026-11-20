// Read n adjacency masks; seek two disjoint column-quadruples with equal opposite signatures.
use std::io::{self, Read};
struct Search {
    n: usize,
    s: Vec<u8>,
    cols: Vec<[usize; 3]>,
    three: bool,
}
impl Search {
    fn sig(&self, a: usize, b: usize) -> u8 {
        self.s[a * self.n + b]
    }
    fn quad(&self, t: &mut Vec<usize>, cand: &[usize], pool: &[usize]) -> bool {
        let stage = t.len() % 4;
        for (i, &x) in cand.iter().enumerate() {
            if cand.len() - i < 4 - stage {
                break;
            }
            if stage == 3 {
                let q = &t[t.len() - 3..];
                if self.sig(q[0], q[1]) != self.sig(q[2], x)
                    || self.sig(q[0], q[2]) != self.sig(q[1], x)
                    || self.sig(q[0], x) != self.sig(q[1], q[2])
                {
                    continue;
                }
            }
            t.push(x);
            if t.len() == 8 {
                return true;
            }
            if t.len() == 4 {
                let p: Vec<_> = pool
                    .iter()
                    .copied()
                    .filter(|&j| j > t[0] && t.iter().all(|&a| self.sig(a, j) != 255))
                    .collect();
                if self.three {
                    for partner in 1..4 {
                        let a = t[0];
                        let b = t[partner];
                        let other: Vec<_> =
                            t.iter().copied().filter(|&v| v != a && v != b).collect();
                        let (c, d) = (other[0], other[1]);
                        for (i, &e) in p.iter().enumerate() {
                            for &f in &p[i + 1..] {
                                if self.sig(e, f) != self.sig(a, b)
                                    || self.sig(a, e) != self.sig(b, f)
                                    || self.sig(a, f) != self.sig(b, e)
                                    || self.sig(c, e) != self.sig(d, f)
                                    || self.sig(c, f) != self.sig(d, e)
                                {
                                    continue;
                                }
                                let mut prev = vec![];
                                for g in 0..self.n {
                                    if g == e
                                        || g == f
                                        || [a, b, c, d, e, f].iter().any(|&x| self.sig(x, g) == 255)
                                    {
                                        continue;
                                    }
                                    if let Some(&h) = prev.iter().find(|&&h| self.sig(g, h) != 255)
                                    {
                                        *t = vec![a, b, c, d, e, f, g, h];
                                        return true;
                                    }
                                    prev.push(g);
                                }
                            }
                        }
                    }
                } else if self.quad(t, &p, &p) {
                    return true;
                }
            } else {
                let q: Vec<_> = cand[i + 1..]
                    .iter()
                    .copied()
                    .filter(|&j| self.sig(x, j) != 255)
                    .collect();
                if self.quad(t, &q, pool) {
                    return true;
                }
            }
            t.pop();
        }
        false
    }
}
fn main() {
    let mut buf = String::new();
    io::stdin().read_to_string(&mut buf).unwrap();
    let a: Vec<u64> = buf.split_whitespace().map(|x| x.parse().unwrap()).collect();
    let edge = |i: usize, j: usize| ((a[i] >> j) & 1) as u8;
    let v = a.len();
    for pat in std::env::args().skip(1).map(|s| s.parse::<u8>().unwrap()) {
        let mut cols = vec![];
        let mut masks = vec![];
        for x in 0..v {
            for y in 0..v {
                for z in 0..v {
                    if x != y
                        && x != z
                        && y != z
                        && (edge(x, y) | edge(x, z) << 1 | edge(y, z) << 2) == pat
                    {
                        cols.push([x, y, z]);
                        masks.push(1u64 << x | 1 << y | 1 << z)
                    }
                }
            }
        }
        let n = cols.len();
        let mut s = vec![255; n * n];
        for i in 0..n {
            for j in 0..i {
                let p = cols[i];
                let q = cols[j];
                if masks[i] & masks[j] != 0
                    || (0..3).any(|u| (0..u).any(|w| edge(p[u], q[w]) != edge(q[u], p[w])))
                {
                    continue;
                }
                let mut h = 0;
                for u in 0..3 {
                    for w in u..3 {
                        h = h * 2 + edge(p[u], q[w]);
                    }
                }
                s[i * n + j] = h;
                s[j * n + i] = h;
            }
        }
        let g = Search {
            cols,
            n,
            s,
            three: std::env::var_os("THREE_FLATS").is_some(),
        };
        let p: Vec<_> = (0..n).collect();
        let mut t = vec![];
        if g.quad(&mut t, &p, &p) {
            println!(
                "pattern {pat} layout {:?}",
                t.iter().map(|&i| g.cols[i]).collect::<Vec<_>>()
            );
            return;
        }
        println!("exhausted {pat}");
    }
}
