# Formal checks through the operator-directed shell/ps1 compiler route.
$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Agda = Join-Path $Tools 'agda-2.8.0/agda.exe'
$Sources = Join-Path $Root 'research/nima/agda'
$Results = Join-Path $Root 'research/nima/results'
$Receipt = Join-Path $Results 'nand-formal-audit.json'
if (Test-Path $Receipt) { Remove-Item $Receipt }
Push-Location $Root
try {
  & (Join-Path $PSScriptRoot 'check_cubical_agda.ps1') -Module NandConstructions -Fresh
  if ($LASTEXITCODE -ne 0) { throw 'Positive compilation failed' }
  $PositivePath = Join-Path $Results 'agda-NandConstructions.json'
  $Positive = Get-Content $PositivePath -Raw | ConvertFrom-Json
  if (!$Positive.passed -or !$Positive.ignore_interfaces) { throw 'Fresh receipt absent' }
  $Controls = @()
  foreach ($Name in @('NandBadTruth', 'NandBadChoiceCollapse')) {
    $File = Join-Path $Sources "negative/$Name.agda"
    $Output = & $Agda --transliterate -i $Sources -i (Join-Path $Tools 'cubical-0.9') $File 2>&1
    $Code = $LASTEXITCODE
    $Text = $Output | Out-String
    $Text | Set-Content -Encoding utf8 (Join-Path $Results "agda-$Name.log")
    Write-Output $Text
    $Expected = if ($Name -eq 'NandBadTruth') { 'false != true' } else { 'inl tt != inr tt' }
    if ($Code -eq 0 -or !$Text.Contains('[UnequalTerms]') -or !$Text.Contains($Expected) -or !$Text.Contains('refl')) {
      throw "Wrong rejection outcome: $Name"
    }
    $Controls += @{ module=$Name; exit_code=$Code; expected_diagnostic=$Expected;
      correctly_rejected=$true; source_sha256=(Get-FileHash -Algorithm SHA256 $File).Hash }
  }
  @{ status='typed-nand-and-currying-checked'; finished_at=[DateTime]::UtcNow.ToString('o');
     positive_receipt_sha256=(Get-FileHash -Algorithm SHA256 $PositivePath).Hash;
     controls=$Controls;
     scope='Empty-target Pi construction, Boolean realization equivalences, Wolfram identity on Bool, retained curry derivation. No global Booleanity or single-axiom completeness theorem.'
  } | ConvertTo-Json -Depth 6 | Set-Content -Encoding utf8 $Receipt
} finally { Pop-Location }
