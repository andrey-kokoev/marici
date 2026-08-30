#!/usr/bin/env node
"use strict";
const fs=require("fs");
const lines=fs.readFileSync(process.argv[2],"utf8").split(/\r?\n/);
const labels=JSON.parse(fs.readFileSync(process.argv[3],"utf8")).labels;
const prefix=process.argv[4];
function isTop(label){return label[0]===3&&label.slice(1,6).every(x=>x===2);}
const buckets={top_all:[],lower_all:[],top_diagonal:[],lower_diagonal:[]};
for(let i=1;i<lines.length;i++){
 const line=lines[i];if(!line)continue;
 const top=[],lower=[];
 for(const entry of line.split(",")){
  const column=Number(entry.slice(0,entry.indexOf(":")));
  (isTop(labels[column])?top:lower).push(entry);
 }
 if(top.length)buckets.top_all.push(top.join(","));
 if(lower.length)buckets.lower_all.push(lower.join(","));
 if(top.length&&!lower.length)buckets.top_diagonal.push(top.join(","));
 if(lower.length&&!top.length)buckets.lower_diagonal.push(lower.join(","));
}
for(const [name,rows] of Object.entries(buckets)){
 const header={schema:"marici.sparse-integer-matrix.v1",rows:rows.length,columns:labels.length,source:name+" projection of filtered residual"};
 fs.writeFileSync(prefix+"-"+name.replace("_","-")+".txt",JSON.stringify(header)+"\n"+rows.join("\n")+"\n");
}
process.stdout.write(JSON.stringify(Object.fromEntries(Object.entries(buckets).map(([k,v])=>[k,v.length])))+"\n");
