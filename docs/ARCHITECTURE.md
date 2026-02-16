# Arquitectura

## 1. Principio Arquitectónico

El sistema sigue una **arquitectura agéntica por capas** donde cada capa mantiene responsabilidades explícitas e interfaces claras.

## 2. Modelo de Capas

1. Capa de Interacción: recibe intención, alcance y restricciones.
2. Capa de Orquestación: descompone tareas y delega ejecución.
3. Capa de Agentes Especialistas: ejecuta capacidades de dominio.
4. Capa de Conocimiento: almacena y recupera evidencia.
5. Capa de Memoria y Reflexión: preserva continuidad entre sesiones.
6. Capa de Síntesis: produce salidas orientadas a decisión.

## 3. Patrón de Ejecución

El patrón dominante es:

1. Explorar.
2. Planear.
3. Ejecutar en paralelo cuando sea viable.
4. Auditar y deduplicar.
5. Sintetizar con trazabilidad de evidencia.

## 4. Tradeoffs de Diseño

- Modularidad sobre monolito para evolucionar de forma controlada.
- Evidencia trazable sobre velocidad de generación sin control.
- Refinamiento iterativo sobre resolución de una sola pasada.
- Separación de responsabilidades sobre prompts opacos de extremo a extremo.

## 5. No-Objetivos

- No es una referencia API a nivel código.
- No es una guía de despliegue de infraestructura.
- No expone implementación propietaria de bajo nivel.
