$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Sources = Join-Path $Root 'research/nima/agda'
$Results = Join-Path $Root 'research/nima/results'
$Receipt = Join-Path $Results 'generated-contexts-formal-audit.json'
if (Test-Path $Receipt) { Remove-Item $Receipt }
Push-Location $Root
try {
  & (Join-Path $PSScriptRoot 'check_cubical_agda.ps1') -Module GeneratedContinuationContexts -Fresh
  if ($LASTEXITCODE -ne 0) { throw 'Positive compilation failed' }
  $PositivePath = Join-Path $Results 'agda-GeneratedContinuationContexts.json'
  $Positive = Get-Content $PositivePath -Raw | ConvertFrom-Json
  if (!$Positive.passed -or !$Positive.ignore_interfaces) { throw 'Fresh receipt absent' }
  $Controls = @()
  foreach ($Name in @('GeneratedBadInverse', 'GeneratedBadProgramEquality')) {
    $File = Join-Path $Sources "negative/$Name.agda"
    $Output = & (Join-Path $Tools 'agda-2.8.0/agda.exe') --transliterate -i $Sources -i (Join-Path $Tools 'cubical-0.9') $File 2>&1
    $Code = $LASTEXITCODE
    $Text = $Output | Out-String
    $Text | Set-Content -Encoding utf8 (Join-Path $Results "agda-$Name.log")
    $Expected = if ($Name -eq 'GeneratedBadInverse') { 'a != b' } else { 'identity != identity then identity' }
    if ($Code -eq 0 -or !$Text.Contains('[UnequalTerms]') -or !$Text.Contains($Expected) -or !$Text.Contains('refl')) {
      throw "Wrong rejection outcome: $Name`n$Text"
    }
    $Controls += @{ module=$Name; exit_code=$Code; expected_diagnostic=$Expected;
      correctly_rejected=$true; source_sha256=(Get-FileHash -Algorithm SHA256 $File).Hash }
  }
  @{ status='generated-structural-contexts-with-explicit-extension-checked';
     finished_at=[DateTime]::UtcNow.ToString('o');
     positive_receipt_sha256=(Get-FileHash -Algorithm SHA256 $PositivePath).Hash;
     controls=$Controls;
     scope='Old map-root obstruction and supplied-function encoding; new nondependent typed program fragment generates swap/curry continuation tests, inverse witnesses and retained certificates without arbitrary function constructors. Original rules remain unchanged.'
  } | ConvertTo-Json -Depth 5 | Set-Content -Encoding utf8 $Receipt
} finally { Pop-Location }
