# Fundamentos Matematicos

Este documento resume los algoritmos nucleares usados por la arquitectura GraphRAG de K.I.M.E.R.A.

## 1. PageRank para Nucleo Semantico

Durante ingesta, PageRank ayuda a separar conceptos nucleares de perifericos.

$$
PR(v_i) = \frac{1-d}{N} + d \sum_{v_j \in M(v_i)} \frac{PR(v_j)}{L(v_j)}
$$

Donde:

- $d$: damping factor.
- $M(v_i)$: nodos que apuntan a $v_i$.
- $L(v_j)$: grado saliente de $v_j$.

## 2. Personalized PageRank para Retrieval Jerarquico

La recuperacion en grafo se modela como caminata aleatoria con reinicio sesgado a semillas semanticas.

$$
\vec{p} = (1-c)A\vec{p} + c\vec{u}
$$

Donde:

- $\vec{u}$ es el vector de preferencia (seed set).
- $A$ es la matriz de adyacencia normalizada.
- $c$ es la probabilidad de reinicio.

## 3. Similaridad Coseno para Matching Semantico

Se utiliza para ranking de chunks textuales y activos visuales.

$$
\text{Sim}(A, B) = \frac{A \cdot B}{\|A\|\|B\|}
$$

## 4. Modularidad para Deteccion de Comunidades

Leiden optimiza modularidad para identificar clusters tematicos coherentes.

$$
Q = \frac{1}{2m} \sum_{ij} \left(A_{ij} - \frac{k_i k_j}{2m}\right)\delta(c_i, c_j)
$$

Donde:

- $A_{ij}$: peso entre nodos $i, j$.
- $k_i$: grado del nodo $i$.
- $m$: numero total de aristas.
- $\delta(c_i, c_j)$: 1 si ambos nodos estan en la misma comunidad.

## 5. Filtro de Relevancia Visual

El ranking multimodal combina texto de consulta, OCR y contexto adyacente de imagen:

$$
E_{visual} = f(\text{OCR} \oplus \text{Contexto} \oplus \text{Metadata})
$$

$$
E_{query} = f(\text{Consulta})
$$

La seleccion final usa similitud coseno entre $E_{query}$ y $E_{visual}$.

## 6. Intuicion Operativa

- PageRank reduce costo de ingesta al priorizar el nucleo informativo.
- PPR corrige el sesgo "top-k local" del vector search puro.
- Leiden evita mezclar temas desconectados en sintesis global.
- Cosine similarity unifica retrieval textual y visual bajo una misma metrica.
