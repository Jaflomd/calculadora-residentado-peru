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
- El supuesto simulacro→T no está validado / the mock-to-T assumption is untested.
- Estimación poblacional: no garantiza ni niega el ingreso.

Manuscrito en preparación (Flores-Cohaila et al.). Licencia MIT.
