# Mapa de Herramientas (Alto Nivel)

## 1. Inteligencia Web

**Proposito**: descubrimiento y adquisicion de evidencia externa.

**Tecnologias representativas**:

- Brave Search / DuckDuckGo para discovery.
- Jina Reader y scraping pipelines para extraccion limpia.

**Salida**:

- fuentes normalizadas,
- contenido listo para ingesta,
- trazabilidad por mision.

## 2. Infraestructura de Conocimiento

**Proposito**: almacenar conocimiento con estructura y recuperacion semantica.

**Tecnologias representativas**:

- Neo4j (local o AuraDB).
- Indices vectoriales 768d.
- labels por Knowledge Space y `session_id` para lineage.

**Salida**:

- nodos `Document`, `Asset`, `VisualAsset`,
- relaciones estructurales y semanticas,
- subgrafos consultables por mision o dominio.

## 3. Retrieval y Synthesis

**Proposito**: convertir evidencia dispersa en respuestas fundamentadas.

**Tecnologias representativas**:

- Hierarchical Retriever (seed vectorial + expansion PPR).
- motores Gemini para sintesis y razonamiento.

**Salida**:

- respuesta con contexto global/local,
- citas de evidencia,
- deteccion de gaps.

## 4. Ciencia de Datos

**Proposito**: ejecutar analitica cuantitativa reproducible.

**Tecnologias representativas**:

- DS-STAR orchestration.
- ejecucion local de codigo Python.
- pipeline de verificacion y debugging iterativo.

**Salida**:

- reportes tecnicos,
- artefactos de datos y visualizacion,
- trazas de validacion.

## 5. Inteligencia Multimodal

**Proposito**: leer imagenes con valor analitico, no decorativo.

**Tecnologias representativas**:

- OCR (Tesseract).
- embeddings SigLIP/Gemini para matching semantico.
- modelos de vision para interpretacion profunda.

**Salida**:

- bloques visuales explicativos,
- ranking de imagenes relevantes,
- evidencia visual integrada al reporte.

## 6. Orquestacion y Memoria

**Proposito**: coordinar agentes y retener aprendizaje.

**Tecnologias representativas**:

- Google ADK.
- Blackboard state (`session.state`) para colaboracion inter-agente.
- capa metacognitiva persistente sobre Neo4j.

**Salida**:

- decisiones de ruteo robustas,
- continuidad entre sesiones,
- reduccion de errores repetidos.

## 7. Observabilidad y Gobernanza

**Proposito**: asegurar calidad y auditabilidad.

**Tecnologias representativas**:

- telemetria por mision y por fase,
- auditoria de redundancia semantica,
- control de integridad de reportes.

**Salida**:

- evidencia operativa verificable,
- reportes consistentes,
- mejora continua basada en metricas.
