// A group of supports all missing a core ten-set t contains at most two newcomers. Forbidding a blocker meeting every disjoint legal pair limits the group to one (any two would have to be mutually red). Enumerate minimal 0/1/2-point blockers via minimal legal supports. A complete downward family is not assumed: legal supports form an interval on each comparable pair.
#[allow(dead_code)]
mod scan {
    include!("ramsey312_google_three_step.rs");
    use std::io::{BufRead, BufReader, BufWriter, Write};
    pub fn run() {
        let args: Vec<_> = env::args().collect();
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
        let cases = fs::read_to_string(&args[2]).unwrap();
        let cases: Vec<_> = cases.lines().collect();
        let mut out = BufWriter::new(fs::File::create(&args[4]).unwrap());
        for line in BufReader::new(fs::File::open(&args[3]).unwrap()).lines() {
            let line = line.unwrap();
            let mut w = line.split_whitespace().map(|x| x.parse::<M>().unwrap());
            let k = w.next().unwrap() as usize;
            let s: Vec<_> = w.collect();
            let z: Vec<_> = cases[k].split_whitespace().collect();
            assert_eq!(z[3], "0");
            let h = ((1 << 52) - 1) ^ z[2].parse::<M>().unwrap();
            let dom: HashSet<M> = s.iter().copied().collect();
            let mins: Vec<_> = s
                .iter()
                .copied()
                .filter(|x| {
                    let mut p = *x;
                    while p != 0 {
                        let b = bit(p);
                        p ^= b;
                        if dom.contains(&(x ^ b)) {
                            return false;
                        }
                    }
                    true
                })
                .collect();
            let mut u = HashSet::new();
            for (j, &x) in mins.iter().enumerate() {
                for &y in &mins[..=j] {
                    if x & y == 0 {
                        u.insert(x | y);
                    }
                }
            }
            let u: Vec<M> = u.into_iter().collect();
            let mut tens = vec![];
            sets(&a, h, 10, 0, &mut tens);
            let mut rows = std::collections::BTreeSet::new();
            for t in tens {
                let vs: Vec<_> = u.iter().copied().filter(|v| v & t == 0).collect();
                if vs.is_empty() {
                    rows.insert((t, t));
                    continue;
                }
                let all = vs.iter().fold(h, |m, v| m & v);
                let mut p = all;
                while p != 0 {
                    let b = bit(p);
                    p ^= b;
                    rows.insert((t | b, t));
                }
                let mut p = vs[0] & !all;
                while p != 0 {
                    let b = bit(p);
                    p ^= b;
                    let mut z = h & !all;
                    for &v in &vs {
                        if v & b == 0 {
                            z &= v;
                            if z == 0 {
                                break;
                            }
                        }
                    }
                    while z != 0 {
                        let c = bit(z);
                        z ^= c;
                        rows.insert((t | b | c, t));
                    }
                }
            }
            write!(out, "{k}").unwrap();
            let mut seen = HashSet::new();
            for (w, t) in rows {
                if seen.insert(w) {
                    write!(out, " {w}:{t}").unwrap()
                }
            }
            writeln!(out).unwrap()
        }
    }
}
fn main() {
    scan::run()
}
