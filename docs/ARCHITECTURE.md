# Arquitectura del Sistema

## 1. Principio Rector

K.I.M.E.R.A. sigue una arquitectura agéntica por capas con separacion explicita entre:

1. Orquestacion conversacional.
2. Ejecucion especializada (research, data science, vision).
3. Infraestructura de conocimiento (grafo + embeddings).
4. Memoria metacognitiva.
5. Sintesis con trazabilidad.

## 2. Segmentacion de Conocimiento

El sistema separa contexto en dos ejes:

1. **Knowledge Space (label de grafo)**: dominio tematico.
2. **Session ID (propiedad)**: linea de tiempo de una mision.

Esto permite aislamiento por tema y, al mismo tiempo, trazabilidad por investigacion.

## 3. Pipeline de Ingestion

La ingesta combina procesamiento estructural y enriquecimiento semantico:

1. Descubrimiento de fuentes (locales o web).
2. Extraccion de texto y assets visuales.
3. Segmentacion en assets/chunks.
4. Embeddings y creacion de nodos/relaciones.
5. Enlaces topologicos (`NEXT_CHUNK`, `SIMILAR_TO`) para preservar flujo narrativo y afinidad semantica.

## 4. Pipeline de Retrieval (GraphRAG Jerarquico)

1. **Seed discovery**: busqueda vectorial inicial.
2. **Expansion estructural**: recorrido en subgrafo con Personalized PageRank.
3. **Fusion multimodal**: inyeccion de evidencia visual relevante.
4. **Sintesis final**: respuesta con procedencia y citas.

El resultado es una mezcla de contexto local (matching semantico) y contexto global (estructura del grafo).

## 5. Arquitectura de Agentes

### 5.1 Orquestador

Interpreta la intencion y decide la ruta:

- consulta puntual,
- investigacion profunda,
- analisis de datos,
- ruta hibrida.

### 5.2 Deep Research y Research Planner

Patron operativo: **Explore -> Plan -> Batch -> Audit -> Synthesize**.

- Explore: barrido inicial.
- Plan: generacion de sub-queries ortogonales.
- Batch: adquisicion concurrente y enriquecimiento del grafo.
- Audit: deduplicacion semantica por secciones.
- Synthesize: reporte ejecutivo y tecnico con evidencia consolidada.

### 5.3 DS-STAR (Data Scientist Agent)

Patron operativo: **Analyze -> Plan -> Code -> Verify -> Route -> Finalize**.

- Ejecuta codigo local para analisis reproducible.
- Verifica suficiencia semantica, no solo ejecucion tecnica.
- Activa depuracion cuando hay errores logicos o tecnicos.

## 6. Capa Multimodal

La capa visual opera como funnel de tres etapas:

1. Filtro OCR (reduccion de ruido).
2. Matching semantico texto-imagen.
3. Analisis de vision profunda para extraer insight.

Este diseno evita costo innecesario y mejora precision en graficas/diagramas.

## 7. Capa Metacognitiva (V5-V6)

La memoria persistente guarda trazas estructuradas de razonamiento:

- `Thought`
- `Critique`
- `Hypothesis`
- `AntiPattern`
- `FunctionCall`

Luego, un Context Hydrator recupera trazas relevantes al inicio de nuevas sesiones para evitar repetir errores y reutilizar conocimiento util.

## 8. Robustez Operativa

Mecanismos clave:

- fallback jerarquico de modelos,
- control de bloat de contexto,
- aislamiento por workspace/sesion,
- telemetria por fase para auditoria.

## 9. Resultado Esperado

K.I.M.E.R.A. produce salidas de grado profesional:

- respuestas fundamentadas,
- citas y procedencia explicita,
- consistencia entre texto, datos y visuales,
- continuidad entre sesiones de trabajo.

## 10. Estado Actual vs Arquitectura Objetivo

### 10.1 Estado Actual (Preview)

- `Research Agent` funciona de forma estable en su dominio.
- `DS-STAR` funciona de forma estable en su dominio.
- `Orchestrator` enruta, pero la colaboracion profunda entre ambos flujos aun no es completa.
- La capa metacognitiva existe a nivel arquitectonico, con implementacion parcial en el flujo productivo unificado.

### 10.2 Objetivo Inmediato

Cerrar un flujo unico de investigacion aplicada:

1. Research Agent construye evidencia y contexto.
2. DS-STAR recibe ese contexto como insumo estructurado para analisis.
3. Capa de sintesis genera un reporte final unificado (tecnico + ejecutivo + trazabilidad).

Este objetivo se documenta en `docs/INTEGRATION_BENCHMARK_PLAN.md`.
