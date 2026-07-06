# Calculadora de Ingreso al Residentado Médico — Perú

Herramienta de investigación de acceso abierto que estima la probabilidad de ingreso
al residentado médico peruano, con datos públicos de CONAREME (64,477 postulantes,
concursos 2016–2025).

## Modelos
- **Con nota (escala T):** regresión logística, AUROC 0.824 en validación temporal (2024–2025).
- **Pre-examen (solo perfil):** regresión logística, AUROC 0.788 en validación temporal.
- Entrenamiento: concursos 2016–2023. Coeficientes completos embebidos en `index.html`.

## Avisos
- NO es un instrumento oficial de CONAREME.
- El uso de simulacros como sustituto de la nota real asume estandarización a T contra
  la distribución nacional; ese supuesto no está validado.
- Estimación poblacional: no garantiza ni niega el ingreso de ningún postulante.
- La competitividad por especialidad se actualiza con los concursos 2024–2025.

Manuscrito en preparación (Flores-Cohaila et al.). Licencia MIT.
