export const mirror=w=>[...w].reverse().join('')
export function patterns(width){const out=[];for(let a=0;a<width;a++)for(let b=a+2;b<width;b++)for(let c=b+2;c<width;c++)out.push(Array.from({length:width},(_,i)=>[a,b,c].includes(i)?'R':'B').join(''));return out}
export function completion(words){function take(l,h){if(l>h)return [];const w=words[l],m=mirror(w);if(m===words[h])return l===h?[w]:[w,...take(l+1,h-1),m];return [w,...take(l+1,h),m]}return take(0,words.length-1)}
export function foldPairs(words){const half=words.slice(0,Math.floor(words.length/2));return half.filter(w=>w.startsWith('RB')&&w.slice(2).includes('RBBR')&&half.includes('BR'+w.slice(2))).flatMap(w=>{const v='BR'+w.slice(2);return [[w,v],[mirror(w),mirror(v)]]})}
export function pascal(n){const rows=[[1]];while(rows.length<=n){const r=rows.at(-1);rows.push(Array.from({length:r.length+1},(_,i)=>(r[i-1]||0)+(r[i]||0)))}return rows}
