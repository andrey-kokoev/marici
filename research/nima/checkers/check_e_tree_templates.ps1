$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Sources = Join-Path $Root 'research/nima/agda'
$Results = Join-Path $Root 'research/nima/results'
$Receipt = Join-Path $Results 'e-tree-templates-formal-audit.json'
if (Test-Path $Receipt) { Remove-Item $Receipt }
Push-Location $Root
try {
  & (Join-Path $PSScriptRoot 'check_cubical_agda.ps1') -Module ECurriedTemplates -Fresh
  if ($LASTEXITCODE -ne 0) { throw 'Positive compilation failed' }
  $PositivePath = Join-Path $Results 'agda-ECurriedTemplates.json'
  $Positive = Get-Content $PositivePath -Raw | ConvertFrom-Json
  if (!$Positive.passed -or !$Positive.ignore_interfaces) { throw 'Fresh receipt absent' }
  $Controls = @()
  foreach ($Name in @('ETreeBadS', 'ETreeBadScope')) {
    $File = Join-Path $Sources "negative/$Name.agda"
    $Output = & (Join-Path $Tools 'agda-2.8.0/agda.exe') --transliterate -i $Sources -i (Join-Path $Tools 'cubical-0.9') $File 2>&1
    $Code = $LASTEXITCODE
    $Text = $Output | Out-String
    $Text | Set-Content -Encoding utf8 (Join-Path $Results "agda-$Name.log")
    $Expected = if ($Name -eq 'ETreeBadS') { 'g != node g x' } else { 'slot here != free false' }
    if ($Code -eq 0 -or !$Text.Contains('[UnequalTerms]') -or !$Text.Contains($Expected) -or !$Text.Contains('refl')) {
      throw "Wrong rejection outcome: $Name`n$Text"
    }
    $Controls += @{ module=$Name; exit_code=$Code; expected_diagnostic=$Expected;
      correctly_rejected=$true; source_sha256=(Get-FileHash -Algorithm SHA256 $File).Hash }
  }
  @{ status='generic-tree-substitution-and-staged-application-checked';
     finished_at=[DateTime]::UtcNow.ToString('o');
     positive_receipt_sha256=(Get-FileHash -Algorithm SHA256 $PositivePath).Hash;
     controls=$Controls;
     scope='Inductive E-tree closure, fold, substitution laws, scoped partial application and K/S template expansion. No K/S rewrite axioms. Not a full dependent P or autonomous combinator evaluator; recursion and syntax signature are supplied.'
  } | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 $Receipt
} finally { Pop-Location }
