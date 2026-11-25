// On a forced anchor class test both its joint (bit,ten) certificate and, for failures, every allowed same-class pair including repeats.
use std::collections::HashMap as Memo;
struct ForcedAudit {
    adj: [u64; 52],
    memo: Memo<u64, Vec<u64>>,
    ambiguous: [u64; 6],
    no_place: [u64; 6],
    greedy_failed: u64,
    groups: u64,
    wide: u64,
    supports: u64,
    pairs: u64,
    largest: usize,
    fail: u64,
    bad_pairs: u64,
    bad_cores: u64,
    no_cert_cores: u64,
}
impl ForcedAudit {
    fn from_matrix(path: &str) -> Self {
        let data: Vec<_> = std::fs::read_to_string(path)
            .unwrap()
            .bytes()
            .filter(|&b| b == 48 || b == 49)
            .collect();
        assert_eq!(data.len(), 2704);
        let adj = std::array::from_fn(|i| {
            (0..52).fold(0, |m, j| m | (((data[52 * i + j] - 48) as u64) << j))
        });
        Self {
            adj,
            memo: Memo::new(),
            ambiguous: [0; 6],
            no_place: [0; 6],
            greedy_failed: 0,
            groups: 0,
            wide: 0,
            supports: 0,
            pairs: 0,
            largest: 0,
            fail: 0,
            bad_pairs: 0,
            bad_cores: 0,
            no_cert_cores: 0,
        }
    }
    fn ten(&mut self, un: u64, d: u64) -> bool {
        let a = &self.adj;
        let w = self.memo.entry(un).or_default();
        if w.iter().any(|t| t & d == 0) {
            return true;
        }
        fn find(a: &[u64], mut p: u64, k: u32) -> Option<u64> {
            if k == 0 {
                return Some(0);
            }
            while p.count_ones() >= k {
                let b = p & p.wrapping_neg();
                p ^= b;
                if let Some(z) = find(a, p & !a[b.trailing_zeros() as usize], k - 1) {
                    return Some(z | b);
                }
            }
            None
        }
        if let Some(t) = find(a, ((1u64 << 52) - 1) & !(un | d), 10) {
            w.push(t);
            true
        } else {
            false
        }
    }
    fn test(
        &mut self,
        d: u64,
        b: [u64; 5],
        mut classes: [Vec<u64>; 5],
        mut ambiguous: Vec<(u64, u64)>,
    ) {
        let mut sig = [(0, 0); 5];
        let oldfail = self.fail;
        let oldbad = self.bad_pairs;
        for (i, c) in classes.iter_mut().enumerate() {
            let h = (1u64 << 52) - 1 - d;
            let anchor = self.adj[b[i].trailing_zeros() as usize] & h;
            assert!(c.contains(&anchor));
            self.groups += 1;
            self.wide += (c.len() > 1) as u64;
            self.supports += c.len() as u64;
            self.largest = self.largest.max(c.len());
            self.pairs += (c.len() * (c.len() + 1) / 2) as u64;
            let common = c.iter().fold(h, |z, x| z & x);
            let union = c.iter().fold(0, |z, x| z | x);
            sig[i] = (common, union);
            if common != 0 && self.ten(union, d) {
                continue;
            }
            self.fail += 1;
            let mut first = None;
            for j in 0..c.len() {
                for k in 0..=j {
                    let (x, y) = (c[j], c[k]);
                    if x & y == 0 || !self.ten(x | y, d) {
                        self.bad_pairs += 1;
                        if first.is_none() {
                            first = Some((x, y))
                        }
                    }
                }
            }
            println!("{d},{},{},{common},{union},{:?}", b[i], c.len(), first)
        }
        let orig = sig;
        let mut failed = false;
        ambiguous.sort_unstable_by_key(|&(x, o)| (o.count_ones(), x));
        for (x, options) in ambiguous {
            let k = options.count_ones() as usize;
            self.ambiguous[k] += 1;
            let mut fits = [(100, 5usize); 5];
            for j in 0..5 {
                if options & b[j] != 0 {
                    fits[j] = (
                        (x ^ (self.adj[b[j].trailing_zeros() as usize] & !d)).count_ones(),
                        j,
                    )
                }
            }
            fits.sort_unstable();
            let mut assigned = false;
            for (_, j) in fits {
                if j < 5 && sig[j].0 & x != 0 && self.ten(sig[j].1 | x, d) {
                    sig[j].0 &= x;
                    sig[j].1 |= x;
                    assigned = true;
                    break;
                }
            }
            if !assigned {
                failed = true;
                if !(0..5).any(|j| {
                    options & b[j] != 0 && orig[j].0 & x != 0 && self.ten(orig[j].1 | x, d)
                }) {
                    self.no_place[k] += 1;
                    if self.no_place[k] == 1 {
                        eprintln!("no_place d={d} x={x} options={options}")
                    }
                }
            }
        }
        if failed && std::env::var_os("RAMSEY_PRINT_UNPLACED").is_some(){println!("projected-greedy-fail,{d}");}
        self.greedy_failed += failed as u64;
        self.no_cert_cores += (self.fail != oldfail) as u64;
        self.bad_cores += (self.bad_pairs != oldbad) as u64;
    }
    fn summary(&self) {
        eprintln!("ambiguous by available classes {:?}; individually no place {:?}; cores failing projected greedy cover {}",self.ambiguous,self.no_place,self.greedy_failed);
        eprintln!("forced_classes={} nontrivial={} forced_support_incidents={} max_class={} within_class_pairs_including_self={} no_joint_certificate={} cores_without_joint_certificate={} compatible_within_pairs={} cores_with_compatible_pair={}",self.groups,self.wide,self.supports,self.largest,self.pairs,self.fail,self.no_cert_cores,self.bad_pairs,self.bad_cores);
    }
}
