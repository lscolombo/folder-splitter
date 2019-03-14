# folder-splitter

## Descripción

Este proyecto es útil para organizar, en subcarpetas, archivos que se encuentran dentro de una carpeta.

### Características

- Se deberà indicar el *nùmero de archivos* que conformará un subgrupo. La cantidad de subcarpetas creadas dependerá de este nùmero. 

- Se deberá elegir entre *copiar (C)* o *mover (M)* los archivos de la carpeta hacia las nuevas subcarpetas.

- Opcionalmente, se podrá elegir por *ordenar* los archivos para su segmentación:
  - D: *Date*. Ordena los archivos por fecha de creación. *DEFAULT*
  - N: *Name*. Ordena los archivos por su nombre.


## Uso

**Clonar el repositorio**

`git clone https://github.com/lscolombo/folder-splitter.git`


**Situarse en el repositorio clonado y ejecutar el script**

`python folder_splitter.py`


## Ejemplo: Árbol de una carpeta antes y después del proceso

**Condiciones aplicadas:**
- 3 archivos por subcarpeta

- Copiar

- Ordenar por nombre de archivo


**Antes:**

![Alt text] (https://imgur.com/CHqq8uf)

**Después:**

![Alt text] (https://imgur.com/6mraDLk)
