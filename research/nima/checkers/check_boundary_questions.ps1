$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../..'))
$Tools = Join-Path $env:USERPROFILE 'tools/cubical-agda'
$Sources = Join-Path $Root 'research/nima/agda'
$Results = Join-Path $Root 'research/nima/results'
$Receipt = Join-Path $Results 'boundary-questions-formal-audit.json'
if (Test-Path $Receipt) { Remove-Item $Receipt }
Push-Location $Root
try {
  & (Join-Path $PSScriptRoot 'check_cubical_agda.ps1') -Module BoundaryGeneratedQuestions -Fresh
  if ($LASTEXITCODE -ne 0) { throw 'Positive compilation failed' }
  $PositivePath = Join-Path $Results 'agda-BoundaryGeneratedQuestions.json'
  $Positive = Get-Content $PositivePath -Raw | ConvertFrom-Json
  if (!$Positive.passed -or !$Positive.ignore_interfaces) { throw 'Fresh receipt absent' }
  $File = Join-Path $Sources 'negative/BoundaryBadWitnessCollapse.agda'
  $Output = & (Join-Path $Tools 'agda-2.8.0/agda.exe') --transliterate -i $Sources -i (Join-Path $Tools 'cubical-0.9') $File 2>&1
  $Code = $LASTEXITCODE
  $Text = $Output | Out-String
  $Text | Set-Content -Encoding utf8 (Join-Path $Results 'agda-BoundaryBadWitnessCollapse.log')
  if ($Code -eq 0 -or !$Text.Contains('[MismatchedProjectionsError]') -or !$Text.Contains('fst and snd') -or !$Text.Contains('refl')) {
    throw "Wrong rejection outcome: $Text"
  }
  @{ status='boundary-generated-questions-and-retained-fillers-checked';
     finished_at=[DateTime]::UtcNow.ToString('o');
     positive_receipt_sha256=(Get-FileHash -Algorithm SHA256 $PositivePath).Hash;
     negative_source_sha256=(Get-FileHash -Algorithm SHA256 $File).Hash;
     negative_exit_code=$Code; correctly_rejected=$true;
     scope='Comparison-rule evidence abstracted as a question; actual Resolve application; true and false questions on complete Qs; distinct witnesses; boundary-transport invariance of truth.'
  } | ConvertTo-Json -Depth 4 | Set-Content -Encoding utf8 $Receipt
} finally { Pop-Location }
