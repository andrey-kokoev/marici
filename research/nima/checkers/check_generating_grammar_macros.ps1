param([switch]$Worker)
$ErrorActionPreference = 'Stop'
if (!$Worker) {
  $PreviousPathExt = $env:PATHEXT
  $env:PATHEXT = '.COM;.EXE;.BAT;.CMD'
  try {
    $Arguments = @('-NoProfile', '-File', ('"' + $PSCommandPath + '"'), '-Worker')
    $Child = Start-Process -FilePath (Join-Path $PSHOME 'pwsh.exe') -ArgumentList $Arguments -NoNewWindow -Wait -PassThru
    exit $Child.ExitCode
  } finally { $env:PATHEXT = $PreviousPathExt }
}
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Sources = Join-Path $Root 'research/nima/agda'
$Results = Join-Path $Root 'research/nima/results'
$Receipt = Join-Path $Results 'generating-grammar-macros-formal-audit.json'
if (Test-Path $Receipt) { Remove-Item $Receipt }
& (Join-Path $PSScriptRoot 'check_cubical_agda.ps1') -Module GeneratingGrammarMacros -Fresh
if ($LASTEXITCODE -ne 0) { throw 'Grammar macros failed compilation' }
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Negative = Join-Path $Sources 'negative/GeneratingGrammarMissingOperand.agda'
$Output = & (Join-Path $Tools 'agda-2.8.0/agda.exe') --transliterate -i $Sources -i (Join-Path $Tools 'cubical-0.9') $Negative 2>&1
$Code = $LASTEXITCODE
$Text = $Output | Out-String
$Log = Join-Path $Results 'agda-GeneratingGrammarMissingOperand.log'
$Text | Set-Content -Encoding utf8 $Log
if ($Code -eq 0 -or !$Text.Contains('[UnequalTerms]') -or !$Text.Contains('Resolve')) {
  throw "Wrong missing-operand rejection: $Text"
}
$Positive = Join-Path $Results 'agda-GeneratingGrammarMacros.json'
@{status='passed'; finished_at=[DateTime]::UtcNow.ToString('o');
  positive_receipt_sha256=(Get-FileHash -Algorithm SHA256 $Positive).Hash;
  checker_sha256=(Get-FileHash -Algorithm SHA256 $PSCommandPath).Hash;
  negative_source_sha256=(Get-FileHash -Algorithm SHA256 $Negative).Hash;
  negative_log_sha256=(Get-FileHash -Algorithm SHA256 $Log).Hash;
  negative_exit_code=$Code;
  scope='Native P-kind family and ordered-pair derivations retain every supplied premise package and its actual derivation. Does not supply independent operands, labels, grouping keys or next endpoints.'
} | ConvertTo-Json -Depth 4 | Set-Content -Encoding utf8 $Receipt
exit 0
