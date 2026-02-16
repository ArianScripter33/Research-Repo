# Evaluacion y Benchmarking

## 1. Posicion de Evaluacion

Este proyecto no reporta benchmarks inventados ni metricas no auditables.

Estado:

- Benchmark comparativo formal: **pendiente**.
- Evidencia operativa real: **disponible** (tests, misiones, trazas, telemetria).

## 2. Evidencia Operativa Disponible

El sistema ya cuenta con señales empiricas de funcionamiento:

1. Misiones end-to-end de investigacion y analitica.
2. Reportes tecnicos generados con procedencia.
3. Trazas de ejecucion multi-agente.
4. Telemetria por fase (latencia, consumo, eventos).
5. Pruebas de integracion en componentes criticos.

Estas señales no sustituyen un benchmark cientifico formal, pero muestran madurez operativa.

## 3. Dimensiones de Medicion Recomendadas

Cuando se formalice benchmarking, se recomienda medir:

1. **Groundedness**: porcentaje de afirmaciones criticas con evidencia trazable.
2. **Cobertura**: amplitud de conceptos/fuentes relevantes recuperadas.
3. **No redundancia**: tasa de repeticion semantica en salida final.
4. **Consistencia inter-documento**: contradicciones entre fuentes sintetizadas.
5. **Estabilidad multi-agente**: tasa de finalizacion exitosa por mision.
6. **Costo y latencia**: por modo (`fast`, `standard`, `lite`, `pro`).

## 4. Baselines Propuestos

Comparar contra:

1. Vector RAG simple (top-k sin expansion de grafo).
2. Graph retrieval sin deduplicacion semantica.
3. Flujo single-agent sin verificacion/route/debugger.

Objetivo: cuantificar aporte incremental real de arquitectura jerarquica y ciclo multi-agente.

## 5. Protocolo de Benchmark (Futuro)

1. Definir un set fijo de tareas representativas (research, PDF complejo, data science).
2. Congelar prompts de evaluacion y criterios de scoring.
3. Controlar ventana temporal de fuentes web para comparabilidad.
4. Ejecutar al menos 3 corridas por escenario para variabilidad.
5. Publicar resultados con supuestos y limites.

## 6. Limitaciones Actuales

- Dependencia de calidad de fuentes y crawlers.
- Sensibilidad a cuotas/rate limits de LLM/API.
- Variabilidad de OCR/extraccion en documentos heterogeneos.
- Incremento de costo/latencia en investigacion profunda multimodal.
- Necesidad de revision humana en contextos de alto riesgo.

## 7. Compromiso de Transparencia

Hasta contar con benchmark formal:

1. No publicar cifras de performance no verificadas.
2. Diferenciar claramente evidencia operacional de evidencia experimental.
3. Documentar mejoras arquitectonicas junto con su plan de validacion.
