// Compile rustc -O --edition=2021; argument is the stored Google 52 adjacency matrix. CSV on stdout.
use std::{collections::HashSet, env, fs};
type M = u64;
fn bit(p: M) -> M {
    p & p.wrapping_neg()
}
fn sets(a: &[M], mut p: M, k: u32, s: M, out: &mut Vec<M>) {
    if k == 0 {
        out.push(s);
        return;
    }
    while p.count_ones() >= k {
        let b = bit(p);
        p ^= b;
        sets(a, p & !a[b.trailing_zeros() as usize], k - 1, s | b, out)
    }
}
fn has(a: &[M], mut p: M, k: u32) -> bool {
    if k == 0 {
        return true;
    }
    while p.count_ones() >= k {
        let b = bit(p);
        p ^= b;
        if has(a, p & !a[b.trailing_zeros() as usize], k - 1) {
            return true;
        }
    }
    false
}
fn supports(a: &[M], p: M, s: M, req: &[M], out: &mut Vec<M>) {
    let mut best = p;
    let mut open = false;
    for &r in req {
        if r & s == 0 {
            let z = p & r;
            if z == 0 {
                return;
            }
            if !open || z.count_ones() < best.count_ones() {
                best = z;
                open = true;
                if z.is_power_of_two() {
                    break;
                }
            }
        }
    }
    if p == 0 {
        out.push(s);
        return;
    }
    let b = bit(best);
    supports(a, p ^ b, s, req, out);
    supports(a, p & !b & !a[b.trailing_zeros() as usize], s | b, req, out)
}
include!("ramsey312_support_sides.rs");
fn main() {
    let text = fs::read_to_string(env::args().nth(1).unwrap()).unwrap();
    let data: Vec<_> = text.bytes().filter(|x| *x == 48 || *x == 49).collect();
    assert_eq!(data.len(), 52 * 52);
    let a: Vec<M> = data
        .chunks(52)
        .map(|r| {
            r.iter()
                .enumerate()
                .fold(0, |m, (i, &x)| m | (((x - 48) as M) << i))
        })
        .collect();
    let f = (1 << 52) - 1;
    let mut elev = vec![];
    sets(&a, f, 11, 0, &mut elev);
    println!(
        "u,v,oldred,supports,disjoint_pairs,blue_pairs,compatible_triples,extensions,bipartite"
    );
    for u in 0..52 {
        for v in 0..u {
            let h = f ^ (1 << u) ^ (1 << v);
            let low = (0..52)
                .filter(|&i| h >> i & 1 != 0 && (a[i] & h).count_ones() < 11)
                .fold(0, |m, i| m | 1 << i);
            let mut req: Vec<_> = elev
                .iter()
                .filter(|&&x| x & !h == 0)
                .map(|x| x & low)
                .collect::<HashSet<_>>()
                .into_iter()
                .collect();
            req.sort_unstable_by_key(|x| (x.count_ones(), *x));
            let mut minimal = vec![];
            for x in req {
                if !minimal.iter().any(|y| x & y == *y) {
                    minimal.push(x)
                }
            }
            let mut s = vec![];
            supports(&a, low, 0, &minimal, &mut s);
            assert!(s.contains(&(a[u] & h)) && s.contains(&(a[v] & h)));
            let audit = env::var_os("RAMSEY_SIDE_PROBE").is_some();
            let probes = if audit {
                Some(side_probes(&a, h, &s, u, v))
            } else {
                None
            };
            let n = s.len();
            let mut pair = vec![0u8; n * n];
            let (mut red, mut blue) = (0, 0);
            for i in 0..n {
                for j in 0..=i {
                    let r = s[i] & s[j] == 0;
                    let b = !has(&a, h & !(s[i] | s[j]), 10);
                    let m = r as u8 + 2 * b as u8;
                    pair[i * n + j] = m;
                    pair[j * n + i] = m;
                    red += r as usize;
                    blue += b as usize
                }
            }
            let (mut tri, mut ext) = (0, 0);
            for i in 0..n {
                for j in 0..=i {
                    let x = pair[i * n + j];
                    if x == 0 {
                        continue;
                    }
                    for k in 0..=j {
                        let y = pair[i * n + k];
                        let z = pair[j * n + k];
                        if y * z == 0 {
                            continue;
                        }
                        tri += 1;
                        for c in 0..8 {
                            if x & (1 << (c & 1)) == 0
                                || y & (1 << ((c >> 1) & 1)) == 0
                                || z & (1 << (c >> 2)) == 0
                                || c == 0
                            {
                                continue;
                            }
                            if c == 7 && has(&a, h & !(s[i] | s[j] | s[k]), 9) {
                                continue;
                            }
                            ext += 1;
                            eprintln!("candidate {u} {v} {} {} {} colors {c}", s[i], s[j], s[k])
                        }
                    }
                }
            }
            if let Some((old, dia, one, wd, anchors, wb)) = probes {
                let proper = |c: &[bool]| {
                    (0..n).all(|i| (0..=i).all(|j| pair[i * n + j] == 0 || c[i] != c[j]))
                };
                assert!(one.is_empty() || proper(&one));
                assert!(!wd[0] || proper(&dia));
                eprintln!("{u},{v},{n},{},{},{},{},{},{},{},{},{},{},{},{}",proper(&old)as u8,proper(&dia)as u8,wd[0]as u8,(!one.is_empty())as u8,anchors[0],anchors[1],wb.first().map_or(0,|p|p.0),wb.first().map_or(0,|p|p.1),wb.get(1).map_or(0,|p|p.0),wb.get(1).map_or(0,|p|p.1),(0..52).find(|&v|!one.is_empty()&&(0..n).all(|i|one[i]==(s[i]>>v&1!=0))).unwrap_or(52),a[u]>>v&1);
            }
            let mut col = vec![0; n];
            let mut bip = true;
            for i in 0..n {
                if col[i] != 0 {
                    continue;
                }
                col[i] = 1;
                let mut q = vec![i];
                while let Some(t) = q.pop() {
                    for j in 0..n {
                        if pair[t * n + j] == 0 {
                            continue;
                        }
                        if col[j] == 0 {
                            col[j] = 3 - col[t];
                            q.push(j)
                        } else if col[j] == col[t] {
                            bip = false
                        }
                    }
                }
            }
            println!(
                "{u},{v},{},{n},{red},{blue},{tri},{ext},{}",
                a[u] >> v & 1,
                bip as u8
            )
        }
    }
}
