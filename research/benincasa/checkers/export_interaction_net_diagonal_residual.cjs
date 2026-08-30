#!/usr/bin/env node
"use strict";
const fs=require("fs");
const lines=fs.readFileSync(process.argv[2],"utf8").split(/\r?\n/);
const labels=JSON.parse(fs.readFileSync(process.argv[3],"utf8")).labels;
const out=process.argv[4];
function isTop(label){return label[0]===3&&label.slice(1,6).every(x=>x===2);}
const kept=[];
for(let i=1;i<lines.length;i++){
 const line=lines[i];if(!line)continue;
 let top=false,lower=false;
 for(const entry of line.split(",")){
  const c=Number(entry.slice(0,entry.indexOf(":")));
  if(isTop(labels[c]))top=true;else lower=true;
 }
 if(!(top&&lower))kept.push(line);
}
const header={schema:"marici.sparse-integer-matrix.v1",rows:kept.length,columns:labels.length,source:"diagonal-only rows of filtered residual"};
fs.writeFileSync(out,JSON.stringify(header)+"\n"+kept.join("\n")+"\n");
process.stdout.write(JSON.stringify({rows:kept.length,columns:labels.length,removed_mixed_rows:lines.length-2-kept.length})+"\n");
