//! Unlabelled local colour partitions. Two restrictions agree up to renaming iff sorted restricted blocks agree. Enforce pairwise support to fixed point (not a global labelling).
use std::collections::HashMap;
pub type Cache = HashMap<(u32, u32), Vec<[u32; 3]>>;
fn models(h: &[u32], v: u32, b: u32) -> Vec<[u32; 3]> {
    let mut pool = Vec::new();
    let mut s = v;
    loop {
        if s.count_ones() <= 2 && super::ind(h, s) {
            let u = s | b;
            if super::verts(u).all(|x| {
                let y = u & !(x | super::adj(h, x));
                super::verts(y).all(|z| y & !(z | super::adj(h, z)) == 0)
            }) {
                pool.push(s)
            }
        }
        if s == 0 {
            break;
        }
        s = (s - 1) & v
    }
    let mut out = vec![];
    for &s in &pool {
        for &t in &pool {
            let u = v ^ s ^ t;
            if s <= t && s & t == 0 && t <= u && pool.contains(&u) {
                out.push([s, t, u])
            }
        }
    }
    out
}
fn sig(p: &[u32; 3], m: u32) -> [u32; 3] {
    let mut a = [p[0] & m, p[1] & m, p[2] & m];
    a.sort_unstable();
    a
}
pub fn test(h: &[u32], r: u32, f: u32, c: &mut Cache) -> (bool, bool) {
    let mut dom = vec![];
    let mut sets = vec![];
    for x in super::verts(r) {
        for y in super::verts(r & (x - 1) & !super::adj(h, x)) {
            for z in super::verts(r & (y - 1) & !(super::adj(h, x) | super::adj(h, y))) {
                let a = f & !(x | y | z | super::adj(h, x) | super::adj(h, y) | super::adj(h, z));
                let v = a & !r;
                let b = a & r;
                if v.count_ones() < 2 {
                    continue;
                }
                sets.push(v);
                dom.push(c.entry((v, b)).or_insert_with(|| models(h, v, b)).clone())
            }
        }
    }
    let mut arcs = vec![];
    for i in 0..sets.len() {
        for j in 0..i {
            let m = sets[i] & sets[j];
            if m.count_ones() < 2 {
                continue;
            }
            if !dom[i]
                .iter()
                .any(|p| dom[j].iter().any(|q| sig(p, m) == sig(q, m)))
            {
                return (false, false);
            }
            arcs.push((i, j, m));
        }
    }
    loop {
        let mut change = false;
        for &(i, j, m) in &arcs {
            for (a, b) in [(i, j), (j, i)] {
                let prev = dom[a].len();
                let support: Vec<_> = dom[b].iter().map(|p| sig(p, m)).collect();
                dom[a].retain(|p| support.contains(&sig(p, m)));
                if dom[a].is_empty() {
                    return (true, false);
                }
                change |= prev != dom[a].len();
            }
        }
        if !change {
            return (true, true);
        }
    }
}
