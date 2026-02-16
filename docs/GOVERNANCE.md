# Gobernanza y Calidad

## 1. Criterios de Calidad

- **Groundedness**: toda afirmacion relevante debe estar soportada por evidencia.
- **Coherencia interna**: sin contradicciones entre secciones o fuentes.
- **Relevancia**: alineacion explicita con la pregunta y objetivos de mision.
- **No redundancia**: deduplicacion semantica antes de sintesis final.

## 2. Principios de Integridad

- Separar hechos observados de inferencias.
- Declarar incertidumbre cuando la cobertura de evidencia sea baja.
- Preservar procedencia de la evidencia (fuente, sesion, contexto).

## 3. Protocolo de Evidencia

1. Identificar fragmentos fuente.
2. Enlazar cada hallazgo con evidencia verificable.
3. Marcar gaps de conocimiento en vez de rellenar con suposiciones.
4. Priorizar transparencia sobre sobreconfianza.

## 4. Politica de Reportes

Todo reporte profesional debe incluir:

1. Resumen ejecutivo.
2. Cuerpo tecnico con hallazgos.
3. Supuestos y limites del analisis.
4. Trazabilidad de fuentes y activos visuales.

## 5. Riesgos Operativos a Mitigar

- Deriva semantica en sintesis larga.
- Mezcla de contexto entre dominios no relacionados.
- Saturacion de contexto por artefactos no informativos.
- Alucinacion de datos cuando faltan pruebas.

## 6. Controles Recomendados

- Revision de consistencia cross-doc antes de publicar.
- Monitoreo de densidad de citas por seccion.
- Auditoria periodica de spaces y sesiones historicas.
- Regression tests para agentes criticos (planner, verifier, router).

## 7. Evolucion Arquitectonica

Cualquier cambio relevante en la arquitectura debe documentar:

1. Problema que resuelve.
2. Tradeoff aceptado.
3. Impacto esperado en calidad, costo y latencia.
4. Plan de verificacion posterior.
