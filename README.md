# SISTEMA DE CONTROL DIFUSO PARA EL MONITOREO DE LA TEMPERATURA Y HUMEDAD EN INVERNADERO

Se propone el desarrollo de un sistema difuso para el control y monitoreo de la temperatura, la humedad, la conductividad y el pH en un invernadero

## Defincion de las Variables Linguisticas
###  Macro Tuneles
#### Variables de Entrada
- Error de Humedad: $\Delta H = H_{\text{Esperada}} - H_{\text{Real}}$
- Error de Temperatura: $\Delta T = T_{\text{Esperada}} - T_{\text{Real}}$
- Estado del Control de Humedad

<table style="text-align: center;">
  <tr >
    <th style="text-align: center;">Variable de Entrada</th>
    <th style="text-align: center;">Rango</th>
    <th style="text-align: center;">MF</th>
    <th style="text-align: center;">Abrev.</th>
    <th style="text-align: center;">Tipo de MF</th>
    <th style="text-align: center;">Parámetros</th>
  </tr>
  <tr>
    <td rowspan="3">Error de Humedad</td>
    <td rowspan="3">-70 a 30 (%)</td>
    <td>Bajo</td>
    <td>B</td>
    <td>Trapezoidal</td>
    <td>[-80 -70 -15 0]</td>
  </tr>
  <tr>
    <td>Mínimo</td>
    <td>Min</td>
    <td>Triangular</td>
    <td>[-15 0 -15]</td>
  </tr>
    <td>Alto</td>
    <td>A</td>
    <td>Trapezoidal</td>
    <td>[0 15 30 45]</td>
  </tr>
  <tr>
    <td rowspan="4">Error de Temperatura</td>
    <td rowspan="4"> -25 a 25 (C)</td>
    <td>Bajo</td>
    <td>B</td>
    <td>Trapezoidal</td>
    <td>[8 16 25 33]</td>
  </tr>
  <tr>
    <td>Mínimo</td>
    <td>Min</td>
    <td>Triangular</td>
    <td>[-8 0 8]</td>
  </tr>
  <tr>
    <td>Alto</td>
    <td>A</td>
    <td>Triangular</td>
    <td>[0 8 16]</td>
  </tr>
  <tr>
    <td>Muy Alto</td>
    <td>MA</td>
    <td>Trapezoidal</td>
    <td>[8 16 25 33]</td>
  </tr>
  <tr>
    <td rowspan="3">Estado del Control de Humedad</td>
    <td rowspan="3">-1 a 1</td>
    <td>Deshumidificación</td>
    <td>DH</td>
    <td>Triangular</td>
    <td>[-2 -1 0]</td>
  </tr>
  <tr>
    <td>OFF</td>
    <td>OFF</td>
    <td>Triangular</td>
    <td>[-0.8 0 0.8]</td>
  </tr>
  <tr>
    <td>Humidificación</td>
    <td>H</td>
    <td>Triangular</td>
    <td>[0 1 2]</td>
  </tr>
</table>

#### Variables de Salida
<table style="text-align: center;">
  <tr >
    <th style="text-align: center;">Variable de Entrada</th>
    <th style="text-align: center;">Variable de Salida</th>
    <th style="text-align: center;">Rango</th>
    <th style="text-align: center;">MF</th>
    <th style="text-align: center;">Abrev.</th>
    <th style="text-align: center;">Tipo de MF</th>
    <th style="text-align: center;">Parámetros</th>
  </tr>
  <tr>
    <td rowspan="3">Error de Humedad</td>
    <td rowspan="3">Control de Humedad</td>
    <td rowspan="3">-1 a 1</td>
    <td>Des Humidificación</td>
    <td>DH</td>
    <td>Triangular</td>
    <td>[-2 -1 0]</td>
  </tr>
  <tr>
    <td>Off</td>
    <td>Off</td>
    <td>Triangular</td>
    <td>[-0.8 0 0.8]</td>
  </tr>
  <tr>
    <td>Humidificación</td>
    <td>H</td>
    <td>Triangular</td>
    <td>[0 1 2]</td>
  </tr>
  <tr>
    <td rowspan="7">Error de Temperatura</td>
    <td rowspan="5">Ventilación</td>
    <td rowspan="5">0 a 100 (%)</td>
    <td>MuyBaja</td>
    <td>MB</td>
    <td>Triangular</td>
    <td>[-25 0 25]</td>
  </tr>
  <tr>
    <td>Baja</td>
    <td>B</td>
    <td>Triangular</td>
    <td>[0 25 50]</td>
  </tr>
  <tr>
    <td>Media</td>
    <td>M</td>
    <td>Triangular</td>
    <td>[25 50 75]</td>
  </tr>
  <tr>
    <td>Alta</td>
    <td>A</td>
    <td>Triangular</td>
    <td>[50 75 100]</td>
  </tr>
  <tr>
    <td>MuyAlta</td>
    <td>MA</td>
    <td>Triangular</td>
    <td>[75 100 125]</td>
  </tr>
  <tr>
    <td rowspan="2">Sombra</td>
    <td rowspan="2">0 a 1</td>
    <td>Quitar</td>
    <td>Q</td>
    <td>Triangular</td>
    <td>[-1 0 1]</td>
  </tr>
  <tr>
    <td>Colocar</td>
    <td>C</td>
    <td>Triangular</td>
    <td>[0 1 2]</td>
  </tr>
</table>

### Invernadero
#### Variables de Entrada
<table style="text-align: center;">
  <tr>
    <th style="text-align: center;">Variable de Entrada</th>
    <th style="text-align: center;">Rango</th>
    <th style="text-align: center;">FM</th>
    <th style="text-align: center;">Abrev.</th>
    <th style="text-align: center;">Tipo de MF</th>
    <th style="text-align: center;">Parámetros</th>
  </tr>
  <tr>
    <td rowspan="5">Error de Humedad</td>
    <td rowspan="5">-70 a 70 (%)</td>
    <td>Muy Alto</td>
    <td>MA</td>
    <td>Triangular</td>
    <td>[10 30 70]</td>
  </tr>
  <tr>
    <td>Alto</td>
    <td>A</td>
    <td>Triangular</td>
    <td>[0 10 30]</td>
  </tr>
  <tr>
    <td>Mínimo</td>
    <td>Min</td>
    <td>Triangular</td>
    <td>[-10 0 10]</td>
  </tr>
  <tr>
    <td>Bajo</td>
    <td>B</td>
    <td>Triangular</td>
    <td>[-30 -10 0]</td>
  </tr>
  <tr>
    <td>Muy Bajo</td>
    <td>MB</td>
    <td>Triangular</td>
    <td>[-70 -30 -10]</td>
  </tr>
  <tr>
    <td rowspan="5">Error de Temperatura</td>
    <td rowspan="5">-30 a 25 (°C)</td>
    <td>Muy Alto</td>
    <td>MA</td>
    <td>Triangular</td>
    <td>[14 25]</td>
  </tr>
  <tr>
    <td>Alto</td>
    <td>A</td>
    <td>Triangular</td>
    <td>[0 7 14]</td>
  </tr>
  <tr>
    <td>Mínimo</td>
    <td>Min</td>
    <td>Triangular</td>
    <td>[-5 0 5]</td>
  </tr>
  <tr>
    <td>Bajo</td>
    <td>B</td>
    <td>Triangular</td>
    <td>[-14 -7 0]</td>
  </tr>
  <tr>
    <td>Muy Bajo</td>
    <td>MB</td>
    <td>Triangular</td>
    <td>[-30 -14]</td>
  </tr>
  <tr>
    <td rowspan="5">Estado del Control de Humedad</td>
    <td rowspan="5">-100 a 100(%)</td>
    <td>Humidificación Grande</td>
    <td>HumG</td>
    <td>Triangular</td>
    <td>[50 100]</td>
  </tr>
  <tr>
    <td>Humidificación Pequeña</td>
    <td>HumP</td>
    <td>Triangular</td>
    <td>[0 50 100]</td>
  </tr>
  <tr>
    <td>Mantener</td>
    <td>M</td>
    <td>Triangular</td>
    <td>[-50 0 50]</td>
  </tr>
  <tr>
    <td>Dcs-Humidificación Pequeña</td>
    <td>DHumP</td>
    <td>Triangular</td>
    <td>[-100 -50 0]</td>
  </tr>
  <tr>
    <td>Des-Humidificación Grande</td>
    <td>DHumG</td>
    <td>Triangular</td>
    <td>[-100 -50]</td>
  </tr>
</table>

#### Variables de Salida
<table style="text-align: center;">
  <tr>
    <th style="text-align: center;">Variable de Entrada</th>
    <th style="text-align: center;">Variable de Salida</th>
    <th style="text-align: center;">Rango</th>
    <th style="text-align: center;">MF</th>
    <th style="text-align: center;">Abrev.</th>
    <th style="text-align: center;">Tipo de MF</th>
    <th style="text-align: center;">Parámetros</th>
  </tr>
  <tr>
    <td rowspan="5">Error de Humedad</td>
    <td rowspan="5">Control de Humedad</td>
    <td rowspan="5">-100 a 100 (%)</td>
    <td>Humidificación Grande</td>
    <td>HumG</td>
    <td>Triangular</td>
    <td>[50 100]</td>
  </tr>
  <tr>
    <td>Humidificación Pequeña</td>
    <td>HumP</td>
    <td>Triangular</td>
    <td>[0 50 100]</td>
  </tr>
  <tr>
    <td>Mantener</td>
    <td>M</td>
    <td>Triangular</td>
    <td>[-50 0 50]</td>
  </tr>
  <tr>
    <td>Des-Humidificación Pequeña</td>
    <td>DHumP</td>
    <td>Triangular</td>
    <td>[-100 -50 0]</td>
  </tr>
  <tr>
    <td>Des-Humidificación Grande</td>
    <td>DHumG</td>
    <td>Triangular</td>
    <td>[-100 -50]</td>
  </tr>
  <tr>
    <td rowspan="5">Error de Temperatura</td>
    <td rowspan="5">Control de Temperatura</td>
    <td rowspan="5">-100 a 100 (%)</td>
    <td>Subida Grande</td>
    <td>SG</td>
    <td>Triangular</td>
    <td>[50 100]</td>
  </tr>
  <tr>
    <td>Subida Pequeña</td>
    <td>SP</td>
    <td>Triangular</td>
    <td>[0 50 100]</td>
  </tr>
  <tr>
    <td>Mantener</td>
    <td>M</td>
    <td>Triangular</td>
    <td>[-50 0 50]</td>
  </tr>
  <tr>
    <td>Bajada Pequeña</td>
    <td>BP</td>
    <td>Triangular</td>
    <td>[-100 -50 0]</td>
  </tr>
  <tr>
    <td>Bajada Grande</td>
    <td>BG</td>
    <td>Triangular</td>
    <td>[-100 -50]</td>
  </tr>
</table>

### Agua de Riego y sustratos
#### Variables de Entrada
<table style="text-align: center;">
  <tr>
    <th style="text-align: center;">Variable de Entrada</th>
    <th style="text-align: center;">Rango</th>
    <th style="text-align: center;">FM</th>
    <th style="text-align: center;">Abrev.</th>
    <th style="text-align: center;">Tipo de MF</th>
    <th style="text-align: center;">Parámetros</th>
  </tr>
  <tr>
    <td rowspan="7">Error de pH</td>
    <td rowspan="7">7 a 7</td>
    <td>Muy Ácido</td>
    <td>M-Ac</td>
    <td>Trapezoidal</td>
    <td>[-7 -4 -2.5]</td>
  </tr>
  <tr>
    <td>Moderadamente Ácido</td>
    <td>Mod-Ac</td>
    <td>Triangular</td>
    <td>[-4 -2.5 -1]</td>
  </tr>
  <tr>
    <td>Ligeramente Ácido</td>
    <td>L-Ac</td>
    <td>Triangular</td>
    <td>[-2.5 -1 0]</td>
  </tr>
  <tr>
    <td>Mínimo</td>
    <td>Min</td>
    <td>Triangular</td>
    <td>[-0.5 0 0.5]</td>
  </tr>
  <tr>
    <td>Ligeramente Alcalino</td>
    <td>M-Al</td>
    <td>Triangular</td>
    <td>[0 1 2.5]</td>
  </tr>
  <tr>
    <td>Moderadamente Alcalino</td>
    <td>Mod-Al</td>
    <td>Triangular</td>
    <td>[1 2.5 4]</td>
  </tr>
  <tr>
    <td>Muy Alcalino</td>
    <td>M-Al</td>
    <td>Trapezoidal</td>
    <td>[2.5 4 7]</td>
  </tr>
  <tr>
    <td rowspan="6">Error de Conductividad</td>
    <td rowspan="6">0 a 10 (mS/cm)</td>
    <td>Muy Baja</td>
    <td>MB</td>
    <td>Triangular</td>
    <td>[-4.5 -3 -1.5]</td>
  </tr>
  <tr>
    <td>Baja</td>
    <td>B</td>
    <td>Triangular</td>
    <td>[-3 -1.5 0]</td>
  </tr>
  <tr>
    <td>Mínima</td>
    <td>Min</td>
    <td>Triangular</td>
    <td>[-0.75 0 0.75]</td>
  </tr>
  <tr>
    <td>Alta</td>
    <td>A</td>
    <td>Triangular</td>
    <td>[0 1.5 3]</td>
  </tr>
  <tr>
    <td>Muy Alta</td>
    <td>MA</td>
    <td>Triangular</td>
    <td>[1.5 3 4.5]</td>
  </tr>
  <tr>
    <td>Extremadamente Alta</td>
    <td>EA</td>
    <td>Triangular</td>
    <td>[3 4.5 6]</td>
  </tr>
</table>

#### Variables de Salida
<table style="text-align: center;">
  <tr>
    <th style="text-align: center;">Variable de Entrada</th>
    <th style="text-align: center;">Variable de Salida</th>
    <th style="text-align: center;">Rango</th>
    <th style="text-align: center;">MF</th>
    <th style="text-align: center;">Abrev.</th>
    <th style="text-align: center;">Tipo de MF</th>
    <th style="text-align: center;">Parámetros</th>
  </tr>
  <tr>
    <td rowspan="7">Error de pH</td>
    <td rowspan="7">Control de pH</td>
    <td rowspan="7">-100 a 100 (%)</td>
    <td>Basificación Alta</td>
    <td>Bas-A</td>
    <td>Triangular</td>
    <td>[100 60]</td>
  </tr>
  <tr>
    <td>Basificación Moderada</td>
    <td>Bas-Mod</td>
    <td>Triangular</td>
    <td>[100 60 30]</td>
  </tr>
  <tr>
    <td>Basilicación Ligera</td>
    <td>Bas-L</td>
    <td>Triangular</td>
    <td>[60 30 0]</td>
  </tr>
  <tr>
    <td>Mantener</td>
    <td>M</td>
    <td>Triangular</td>
    <td>[30 0 -30]</td>
  </tr>
  <tr>
    <td>Acidificación Ligera</td>
    <td>Ac-L</td>
    <td>Triangular</td>
    <td>[0 -30 60]</td>
  </tr>
  <tr>
    <td>Acidificación Moderada</td>
    <td>Ac-Mod</td>
    <td>Triangular</td>
    <td>[-30 0 -100]</td>
  </tr>
  <tr>
    <td>Acidificación Alta</td>
    <td>Ac-A</td>
    <td>Triangular</td>
    <td>[-60 -100]</td>
  </tr>
  <tr>
    <td rowspan="6">Error de CE</td>
    <td rowspan="6">Control de CE</td>
    <td rowspan="6">-100 a 100 (%)</td>
    <td>Bajada Crítica</td>
    <td>BC</td>
    <td>Triangular</td>
    <td>[-100 -60]</td>
  </tr>
  <tr>
    <td>Bajada Grande</td>
    <td>BG</td>
    <td>Triangular</td>
    <td>[-100 -60 -30]</td>
  </tr>
  <tr>
    <td>Bajada Pequeña</td>
    <td>BP</td>
    <td>Triangular</td>
    <td>[-60 -30 0]</td>
  </tr>
  <tr>
    <td>Mantener</td>
    <td>M</td>
    <td>Triangular</td>
    <td>[-35 0 50]</td>
  </tr>
  <tr>
    <td>Subida Pequeña</td>
    <td>SP</td>
    <td>Triangular</td>
    <td>[0 50 100]</td>
  </tr>
  <tr>
    <td>Subida Moderada</td>
    <td>SM</td>
    <td>Triangular</td>
    <td>[50 100]</td>
  </tr>
</table>

## Construccion de Base reglas
### Macro Tuneles
#### Error de Humedad
<table style="text-align: center;">
  <tr>
    <td></td>
    <td style="text-align: center;" colspan="3">Error de Humedad</td>
  </tr>
  <tr>
    <td rowspan="2">Control de Humedad</td>
    <td>Bajo</td>
    <td>Mínimo</td>
    <td>Alto</td>
  </tr>
  <tr>
    <td>H</td>
    <td>Off</td>
    <td>DH</td>
  </tr>
</table>

#### Error de Temperatura
<table style="text-align: center;">
  <tr>
    <th></th>
    <th colspan="3" style="text-align: center;">Estado del Control de Humedad</th>
  </tr>
  <tr>
    <th style="text-align: center;">Error de Temperatura</th>
    <th style="text-align: center;">DH</th>
    <th style="text-align: center;">OFF</th>
    <th style="text-align: center;">H</th>
  </tr>
  <tr>
    <td rowspan="2">Bajo</td>
    <td>MB</td>
    <td>B</td>
    <td>MB</td>
  </tr>
  <tr>
    <td>C</td>
    <td>C</td>
    <td>C</td>
  </tr>
  <tr>
    <td rowspan="2">Mínimo</td>
    <td>B</td>
    <td>M</td>
    <td>B</td>
  </tr>
  <tr>
    <td>C</td>
    <td>Q</td>
    <td>C</td>
  </tr>
  <tr>
    <td rowspan="2">Alto</td>
    <td>M</td>
    <td>A</td>
    <td>M</td>
  </tr>
  <tr>
    <td>Q</td>
    <td>C</td>
    <td>Q</td>
  </tr>
  <tr>
    <td rowspan="2">Muy Alto</td>
    <td>A</td>
    <td>MA</td>
    <td>A</td>
  </tr>
  <tr>
    <td>Q</td>
    <td>Q</td>
    <td>Q</td>
  </tr>
</table>

<table style="text-align: center;">
  <tr>
    <td rowspan="2"></td>
    <td rowspan="2"></td>
    <td rowspan="2"></td>
    <td rowspan="2"></td>
    <td rowspan="2"></td>
    <td rowspan="2"></td>
    <td rowspan="2"></td>
    <td rowspan="2"></td>
    <td rowspan="2"></td>
    <td rowspan="2"></td>
    <td rowspan="2"></td>
    <td rowspan="2"></td>
    <td>Ventilacion</td>
  </tr>
  <tr>
    <td>Sombra</td>
  </tr>
</table>

### Invernadero
#### Error de Humedad
<table style="text-align: center;">
  <tr>
    <th></th>
    <th colspan="5" style="text-align: center;">Error de Humedad</th>
  </tr>
  <tr>
    <td rowspan ="2"><b>Control de Humedad</b></td>
    <th>Muy Bajo </th>
    <th>Bajo</th>
    <th>Mínimo</th>
    <th>Alto</th>
    <th>Muy Alto</th>
  </tr>
  <tr>
    <td>HG</td>
    <td>HP</td>
    <td>M</td>
    <td>HP</td>
    <td>HG</td>
  </tr>
</table>

#### Error de Temperatura
<table style="text-align: center;">
  <tr>
    <th></th>
    <th colspan="5">Estado del Control de Humedad</th>
  </tr>
  <tr>
    <th>Error de Temperatura</th>
    <th>HG</th>
    <th>HP</th>
    <th>M</th>
    <th>DHP</th>
    <th>DHG</th>
  </tr>
  <tr>
    <td>Muy Alto</td>
    <td>BP</td>
    <td>BG</td>
    <td>BG</td>
    <td>BG</td>
    <td>BP</td>
  </tr>
  <tr>
    <td>Alto</td>
    <td>M</td>
    <td>BP</td>
    <td>BP</td>
    <td>BP</td>
    <td>M</td>
  </tr>
  <tr>
    <td>Mínimo</td>
    <td>SP</td>
    <td>M</td>
    <td>M</td>
    <td>M</td>
    <td>SP</td>
  </tr>
  <tr>
    <td>Bajo</td>
    <td>SG</td>
    <td>SP</td>
    <td>SP</td>
    <td>SP</td>
    <td>SG</td>
  </tr>
  <tr>
    <td>Muy Bajo</td>
    <td>SG</td>
    <td>SG</td>
    <td>SG</td>
    <td>SG</td>
    <td>SG</td>
  </tr>
</table>

### Agua de Riego y Sustratos
#### Error de PH
<table style="text-align: center;">
  <tr>
    <th></th>
    <th colspan="7" style="text-align: center;">Error de pH</th>
  </tr>
  <tr>
    <td rowspan="2"><b>Control de pH</b></th>
    <th>M-Ac</th>
    <th>Mod-Ac</th>
    <th>L-Ac</th>
    <th>M</th>
    <th>L-Al</th>
    <th>Mod-Al</th>
    <th>M-Al</th>
  </tr>
  <tr>
    <td>Bas-A</td>
    <td>Bas-Mod</td>
    <td>Bas-L</td>
    <td>M</td>
    <td>Ac-L</td>
    <td>Ac-Mod</td>
    <td>Ac-A</td>
  </tr>
</table>

#### Error de CE
<table>
  <tr>
    <th></th>
    <th style="text-align: center;" colspan="6">Error de CE</th>
  </tr>
  <tr>
    <td rowspan="2"><b>Control de CE</b></th>
    <th>MB</th>
    <th>B</th>
    <th>Min</th>
    <th>Alta</th>
    <th>MA</th>
    <th>EA</th>
  </tr>
  <tr>
    <td>SG</td>
    <td>SP</td>
    <td>M</td>
    <td>BP</td>
    <td>BG</td>
    <td>BC</td>
  </tr>
</table>

## Librerias Empleadas:
- scikit-fuzzy
- numpy
- matplotlib

## Referencias
- Eduardo Flores Gallegos. Sistema De Control Difuso Para El Monitoreo De La Temperatura, La Humedad, El Ph y La Conductividad Eléctrica En Invernaderos De Plantas Ornamentales, 2017. [Tesis](https://dspace.colima.tecnm.mx/bitstream/handle/123456789/721/EDUARO%20FLORES%20GALLEGOS.pdf?sequence=1&isAllowed=y)
