# Calculadora de Ingreso al Residentado Médico — Perú / Peruvian Medical Residency Admission Calculator

Herramienta de investigación de acceso abierto, **bilingüe (ES/EN)**, que estima la
probabilidad de ingreso al residentado médico peruano con datos públicos de CONAREME
(64,477 postulantes, concursos 2016–2025).

## Modelos / Models
- **Con nota (escala T) / with score:** regresión logística, AUROC 0.824 (validación temporal 2024–2025).
- **Pre-examen (solo perfil) / pre-exam:** regresión logística, AUROC 0.788.
- Entrenamiento / training: concursos 2016–2023. Coeficientes completos embebidos en `index.html`.

## Estructura
- `index.html` — página autocontenida (generada; no editar a mano).
- `template.html` + `build.py` — fuente. Recalibración anual: regenerar los CSV de
  `../outputs/` y correr `python3 build.py`.

## Avisos / Notices
- NO es un instrumento oficial de CONAREME / NOT an official CONAREME instrument.
- Un simulacro produce solo un escenario de sensibilidad, no una probabilidad calibrada / a practice score produces a sensitivity scenario, not a calibrated probability.
- El modelo pre-examen sobrepredijo 4.8 puntos porcentuales en promedio / the pre-examination model overpredicted by 4.8 percentage points on average.
- La interfaz actual admite solo modalidades activas Libre y Cautiva; Destaque se conserva únicamente como coeficiente histórico / current inputs are limited to active Open and Sponsored modalities; Destaque remains only as a historical coefficient.
- El número de intento ya incorpora la historia acumulada de postulaciones / attempt number already captures cumulative application history.
- Se requiere recalibración periódica antes de uso rutinario / periodic recalibration is required before routine use.
- Estimación poblacional: no garantiza ni niega el ingreso.

Manuscrito en preparación (Flores-Cohaila et al.). Licencia MIT.
