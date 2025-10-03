"""
Experimento de la Doble Rendija - Libreria de Simulacion
========================================================

Esta libreria simula el famoso experimento de la doble rendija, 
demostrando la naturaleza ondulatoria de la luz.

Caracteristicas:
- Simulacion de patrones de difraccion e interferencia (una y dos rendijas)
- Visualizacion del patron en 1D y 2D
- Ajuste de parametros fisicos: ancho de rendija, separacion, longitud de onda, distancia a la pantalla
- Prediccion de posiciones de maximos y minimos
- Analisis de resultados experimentales
- Comparacion teoria vs experimento
- Guia educativa completa para el montaje fisico real
- Exportacion de resultados y graficos

Autor: Equipo de Fisica Cuantica
Fecha: Octubre 2025

Modulos:
    Onda: Representa una onda monocromatica
    ExperimentoDobleRendija: Clase principal del simulador
    graficar_patron: Funcion para visualizar los resultados
    analizar_experimento: Comparar resultados teoricos con experimentales
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Optional, Dict
import warnings
from dataclasses import dataclass

# ------------------------
# Clase para resultados
# ------------------------
@dataclass
class ResultadosAnalisis:
    """Almacena los resultados del análisis del experimento."""
    posiciones_maximos: np.ndarray
    posiciones_minimos: np.ndarray
    separacion_franjas: float
    ancho_central: float
    parametros: Dict


# ------------------------
# Clase Onda
# ------------------------
class Onda:
    """
    Representa una onda monocromática utilizada en el experimento.
    
    Ejemplos:
        >>> onda_roja = Onda(632e-9)  # Láser rojo
        >>> onda_verde = Onda(532e-9)  # Láser verde
    """
    def __init__(self, longitud_onda: float, amplitud: float = 1.0):
        """
        Args:
            longitud_onda (float): Longitud de onda en metros (ej: 632e-9 para rojo)
            amplitud (float): Amplitud de la onda (por defecto = 1.0)
            
        Raises:
            ValueError: Si la longitud de onda no es positiva
        """
        if longitud_onda <= 0:
            raise ValueError(f"La longitud de onda debe ser positiva. Recibido: {longitud_onda}")
        if not (100e-9 <= longitud_onda <= 1000e-9):
            warnings.warn(f"Longitud de onda {longitud_onda*1e9:.1f} nm fuera del rango visible (400-700 nm)")
        
        self.longitud_onda = longitud_onda
        self.amplitud = amplitud
        self.k = 2 * np.pi / longitud_onda   # número de onda
        self.frecuencia = 3e8 / longitud_onda  # frecuencia en Hz
    
    def fase(self, distancia: float) -> float:
        """
        Calcula el desfase tras recorrer cierta distancia.
        
        Args:
            distancia: Distancia recorrida en metros
            
        Returns:
            Desfase en radianes
        """
        return self.k * distancia
    
    def __repr__(self):
        return f"Onda(λ={self.longitud_onda*1e9:.1f} nm, A={self.amplitud})"


# ------------------------
# Clase ExperimentoDobleRendija
# ------------------------
class ExperimentoDobleRendija:
    """
    Simula la difracción e interferencia en rendija simple y doble rendija.
    
    Ecuaciones utilizadas:
    - Difracción (rendija simple): I(θ) = I₀ * [sin(β)/β]²
      donde β = (π * a * sin(θ)) / λ
    - Interferencia (doble rendija): I(θ) = I₀ * [sin(β)/β]² * cos²(δ)
      donde δ = (π * d * sin(θ)) / λ
    
    Ejemplos:
        >>> exp = ExperimentoDobleRendija()
        >>> y, intensidad = exp.simular(doble=True)
        >>> exp.calcular_posiciones_franjas()
    """
    def __init__(self, 
                 longitud_onda: float = 632e-9,   # láser rojo (~632 nm)
                 ancho_rendija: float = 50e-6,    # ancho de cada rendija (50 μm)
                 separacion: float = 200e-6,       # separación entre rendijas (200 μm)
                 distancia_pantalla: float = 1.0   # distancia a la pantalla (1 m)
                 ):
        """
        Inicializa el experimento con los parámetros físicos.
        
        Args:
            longitud_onda: Longitud de onda en metros (default: 632 nm - láser rojo)
            ancho_rendija: Ancho de cada rendija en metros (default: 50 μm)
            separacion: Separación entre centros de rendijas en metros (default: 200 μm)
            distancia_pantalla: Distancia de las rendijas a la pantalla en metros (default: 1 m)
            
        Raises:
            ValueError: Si algún parámetro es inválido
        """
        # Validaciones
        if longitud_onda <= 0:
            raise ValueError("La longitud de onda debe ser positiva")
        if ancho_rendija <= 0:
            raise ValueError("El ancho de rendija debe ser positivo")
        if separacion <= 0:
            raise ValueError("La separación debe ser positiva")
        if distancia_pantalla <= 0:
            raise ValueError("La distancia a la pantalla debe ser positiva")
        if separacion <= ancho_rendija:
            warnings.warn("La separación es menor o igual al ancho de rendija. "
                        "Esto puede causar solapamiento.")
        
        self.onda = Onda(longitud_onda)
        self.ancho_rendija = ancho_rendija
        self.separacion = separacion
        self.distancia_pantalla = distancia_pantalla
        
        # Calcular parámetros útiles
        self._calcular_parametros_teoricos()
    
    def _calcular_parametros_teoricos(self):
        """Calcula parámetros teóricos del experimento."""
        # Separación angular entre franjas (aproximación de ángulo pequeño)
        self.separacion_angular = self.onda.longitud_onda / self.separacion
        
        # Separación lineal entre franjas en la pantalla
        self.separacion_franjas = (self.onda.longitud_onda * self.distancia_pantalla) / self.separacion
        
        # Ancho del máximo central de difracción
        self.ancho_central_difraccion = (2 * self.onda.longitud_onda * self.distancia_pantalla) / self.ancho_rendija
        
        # Número de franjas visibles dentro del máximo central
        self.num_franjas_visibles = int(self.ancho_central_difraccion / self.separacion_franjas)
    
    def rendija_simple(self, y: np.ndarray) -> np.ndarray:
        """
        Calcula la intensidad para una rendija simple (patrón de difracción).
        
        Args:
            y: Array de posiciones en la pantalla (metros)
            
        Returns:
            Array de intensidades normalizadas
        """
        theta = np.arctan(y / self.distancia_pantalla)
        beta = (np.pi * self.ancho_rendija * np.sin(theta)) / self.onda.longitud_onda
        
        # Evitar división por cero
        beta_seguro = np.where(np.abs(beta) < 1e-12, 1e-12, beta)
        return (np.sin(beta_seguro) / beta_seguro) ** 2
    
    def doble_rendija(self, y: np.ndarray) -> np.ndarray:
        """
        Calcula la intensidad para doble rendija (difracción + interferencia).
        
        Args:
            y: Array de posiciones en la pantalla (metros)
            
        Returns:
            Array de intensidades normalizadas
        """
        theta = np.arctan(y / self.distancia_pantalla)
        
        # Envolvente de difracción (una rendija)
        beta = (np.pi * self.ancho_rendija * np.sin(theta)) / self.onda.longitud_onda
        beta_seguro = np.where(np.abs(beta) < 1e-12, 1e-12, beta)
        envolvente = (np.sin(beta_seguro) / beta_seguro) ** 2
        
        # Término de interferencia (dos rendijas)
        delta = (np.pi * self.separacion * np.sin(theta)) / self.onda.longitud_onda
        interferencia = (np.cos(delta)) ** 2
        
        return envolvente * interferencia
    
    def simular(self, ancho: float = 0.01, puntos: int = 2000, doble: bool = True) -> Tuple[np.ndarray, np.ndarray]:
        """
        Ejecuta la simulación del experimento.
        
        Args:
            ancho: Ancho de la pantalla en metros (default: 1 cm)
            puntos: Resolución (cantidad de puntos) (default: 2000)
            doble: True para doble rendija, False para rendija simple
            
        Returns:
            Tupla (posiciones, intensidad) con arrays de numpy
        """
        if ancho <= 0:
            raise ValueError("El ancho de la pantalla debe ser positivo")
        if puntos < 100:
            raise ValueError("Se requieren al menos 100 puntos para una buena resolución")
        
        y = np.linspace(-ancho/2, ancho/2, puntos)
        
        if doble:
            intensidad = self.doble_rendija(y)
        else:
            intensidad = self.rendija_simple(y)
        
        # Normalización
        intensidad_normalizada = intensidad / np.max(intensidad)
        
        return y, intensidad_normalizada
    
    def calcular_posiciones_franjas(self, n_max: int = 10) -> ResultadosAnalisis:
        """
        Calcula las posiciones teóricas de máximos y mínimos de interferencia.
        
        Args:
            n_max: Número máximo de orden a calcular
            
        Returns:
            ResultadosAnalisis con las posiciones calculadas
        """
        # Máximos de interferencia: d * sin(θ) = n * λ
        # Para ángulos pequeños: sin(θ) ≈ tan(θ) = y/L
        # Entonces: y = n * λ * L / d
        
        ordenes = np.arange(-n_max, n_max + 1)
        posiciones_maximos = ordenes * self.separacion_franjas
        
        # Mínimos de interferencia: d * sin(θ) = (n + 0.5) * λ
        ordenes_minimos = np.arange(-n_max, n_max) + 0.5
        posiciones_minimos = ordenes_minimos * self.separacion_franjas
        
        parametros = {
            'longitud_onda_nm': self.onda.longitud_onda * 1e9,
            'ancho_rendija_um': self.ancho_rendija * 1e6,
            'separacion_um': self.separacion * 1e6,
            'distancia_pantalla_m': self.distancia_pantalla,
            'separacion_franjas_mm': self.separacion_franjas * 1e3,
            'ancho_central_mm': self.ancho_central_difraccion * 1e3,
            'num_franjas_visibles': self.num_franjas_visibles
        }
        
        return ResultadosAnalisis(
            posiciones_maximos=posiciones_maximos,
            posiciones_minimos=posiciones_minimos,
            separacion_franjas=self.separacion_franjas,
            ancho_central=self.ancho_central_difraccion,
            parametros=parametros
        )
    
    def imprimir_predicciones(self):
        """Imprime las predicciones teóricas del experimento."""
        resultados = self.calcular_posiciones_franjas()
        print("=" * 70)
        print("PREDICCIONES TEORICAS PARA TU EXPERIMENTO")
        print("=" * 70)
        print("\nPARAMETROS DEL EXPERIMENTO:")
        print(f"   - Longitud de onda (lambda): {resultados.parametros['longitud_onda_nm']:.1f} nm")
        print(f"   - Ancho de rendija (a): {resultados.parametros['ancho_rendija_um']:.1f} um")
        print(f"   - Separacion de rendijas (d): {resultados.parametros['separacion_um']:.1f} um")
        print(f"   - Distancia a la pantalla (L): {resultados.parametros['distancia_pantalla_m']:.2f} m")
        print("\nPREDICCIONES DE MEDICION:")
        print(f"   - Separacion entre franjas: {resultados.parametros['separacion_franjas_mm']:.2f} mm")
        print(f"   - Ancho del maximo central: {resultados.parametros['ancho_central_mm']:.2f} mm")
        print(f"   - Franjas visibles en el maximo central: ~{resultados.parametros['num_franjas_visibles']}")
        print("\nPOSICIONES DE LOS PRIMEROS 5 MAXIMOS (desde el centro):")
        for i in range(min(5, len(resultados.posiciones_maximos)//2)):
            pos = resultados.posiciones_maximos[len(resultados.posiciones_maximos)//2 + i]
            print(f"   - Maximo de orden {i}: +- {abs(pos)*1e3:.2f} mm")
        print("\n-- CONSEJOS PARA TU EXPERIMENTO:")
        print("   1. Usa una regla para medir la separacion entre franjas brillantes")
        print("   2. Toma fotos con una camara en un cuarto oscuro")
        print("   3. Mide al menos 3-5 franjas para obtener un promedio")
        print("   4. Compara tus mediciones con estas predicciones")
        print("=" * 70)
    
    def __repr__(self):
        return (f"ExperimentoDobleRendija(λ={self.onda.longitud_onda*1e9:.1f}nm, "
                f"a={self.ancho_rendija*1e6:.1f}μm, d={self.separacion*1e6:.1f}μm, "
                f"L={self.distancia_pantalla:.2f}m)")


# ------------------------
# Funciones de visualización
# ------------------------
def graficar_patron(y: np.ndarray, intensidad: np.ndarray, 
                    titulo: str = "Patrón de Interferencia", 
                    guardar: Optional[str] = None,
                    mostrar_predicciones: bool = False,
                    experimento: Optional[ExperimentoDobleRendija] = None) -> None:
    """
    Grafica en 1D y 2D el patrón de interferencia.
    
    Args:
        y: Posiciones en la pantalla (metros)
        intensidad: Intensidad normalizada
        titulo: Título del gráfico
        guardar: Ruta para guardar la imagen (opcional)
        mostrar_predicciones: Si True, marca las posiciones teóricas
        experimento: Instancia del experimento (necesaria si mostrar_predicciones=True)
    """
    plt.figure(figsize=(14, 6))
    
    # Gráfico 1D
    plt.subplot(1, 2, 1)
    plt.plot(y*1000, intensidad, 'r-', lw=2)
    
    # Agregar predicciones teóricas
    if mostrar_predicciones and experimento:
        resultados = experimento.calcular_posiciones_franjas(n_max=5)
        for pos in resultados.posiciones_maximos:
            if abs(pos) <= np.max(np.abs(y)):
                plt.axvline(pos*1000, color='green', linestyle='--', alpha=0.5, lw=1)
        plt.plot([], [], 'g--', label='Máximos teóricos', alpha=0.5)
        plt.legend()
    
    plt.title(f"{titulo} - Perfil 1D")
    plt.xlabel("Posición en la pantalla (mm)")
    plt.ylabel("Intensidad Normalizada")
    plt.grid(True, alpha=0.4)
    plt.ylim(-0.05, 1.1)
    
    # Gráfico 2D (mapa de calor)
    plt.subplot(1, 2, 2)
    patron = np.tile(intensidad, (50, 1))
    extent = [y[0]*1000, y[-1]*1000, -1, 1]
    plt.imshow(patron, extent=extent, aspect="auto", cmap="inferno")
    plt.title(f"{titulo} - Visualización 2D")
    plt.xlabel("Posición (mm)")
    plt.ylabel("Altura")
    plt.colorbar(label="Intensidad")
    
    plt.tight_layout()
    if guardar:
        plt.savefig(guardar, dpi=300, bbox_inches='tight')
        print(f"- Gráfico guardado en: {guardar}")
    plt.show()


def comparar_experimento_teoria(y_experimental: np.ndarray, 
                               intensidad_experimental: np.ndarray,
                               experimento: ExperimentoDobleRendija,
                               guardar: Optional[str] = None) -> Dict:
    """
    Compara los resultados experimentales con la teoría.
    
    Args:
        y_experimental: Posiciones medidas (metros)
        intensidad_experimental: Intensidad medida (normalizada)
        experimento: Instancia del experimento con los parámetros
        guardar: Ruta para guardar el gráfico (opcional)
        
    Returns:
        Diccionario con estadísticas de la comparación
    """
    # Simular teoría con los mismos puntos
    y_teoria, intensidad_teoria = experimento.simular(
        ancho=np.max(y_experimental) - np.min(y_experimental),
        puntos=len(y_experimental),
        doble=True
    )
    
    # Calcular error cuadrático medio
    mse = np.mean((intensidad_experimental - intensidad_teoria)**2)
    correlacion = np.corrcoef(intensidad_experimental, intensidad_teoria)[0, 1]
    
    # Graficar comparación
    plt.figure(figsize=(14, 6))
    
    # Comparación directa
    plt.subplot(1, 2, 1)
    plt.plot(y_experimental*1000, intensidad_experimental, 'bo-', 
             label='Experimental', alpha=0.6, markersize=3)
    plt.plot(y_teoria*1000, intensidad_teoria, 'r-', 
             label='Teórico', lw=2)
    plt.title("Comparación: Experimental vs Teórico")
    plt.xlabel("Posición (mm)")
    plt.ylabel("Intensidad Normalizada")
    plt.legend()
    plt.grid(True, alpha=0.4)
    
    # Residuos
    plt.subplot(1, 2, 2)
    residuos = intensidad_experimental - intensidad_teoria
    plt.plot(y_experimental*1000, residuos, 'g-', lw=1)
    plt.axhline(0, color='k', linestyle='--', lw=1)
    plt.title("Residuos (Experimental - Teórico)")
    plt.xlabel("Posición (mm)")
    plt.ylabel("Diferencia de Intensidad")
    plt.grid(True, alpha=0.4)
    
    plt.tight_layout()
    if guardar:
        plt.savefig(guardar, dpi=300, bbox_inches='tight')
        print(f" Comparación guardada en: {guardar}")
    plt.show()
    
    # Imprimir estadísticas
    print("\n" + "="*70)
    print("ANÁLISIS DE COMPARACIÓN: EXPERIMENTO vs TEORÍA")
    print("="*70)
    print(f"- Error Cuadrático Medio (MSE): {mse:.6f}")
    print(f"- Correlación: {correlacion:.4f} (1.0 = perfecto)")
    print("- Calidad del ajuste: ", end="")
    if correlacion > 0.95:
        print("EXCELENTE")
    elif correlacion > 0.85:
        print("MUY BUENO")
    elif correlacion > 0.70:
        print("BUENO")
    else:
        print("NECESITA MEJORA")
    print("="*70)
    
    return {
        'mse': mse,
        'correlacion': correlacion,
        'residuos': residuos
    }


# Guía educativa completa
def guia_proyecto_completa() -> str:
    """Devuelve la guía completa del proyecto educativo."""
    return (
          "EXPERIMENTO DE LA DOBLE RENDIJA - GUIA COMPLETA\n"
          "\nOBJETIVO DEL PROYECTO\n"
          "Reproducir el experimento de la doble rendija que demuestra la naturaleza ondulatoria de la luz y uno de los misterios mas profundos de la mecanica cuantica: la dualidad onda-particula.\n"
          "\nMATERIALES NECESARIOS\n"
          "- Puntero laser rojo (5mW, ~632 nm)\n"
          "- Papel aluminio (buena calidad, sin arrugas)\n"
          "- Cuchilla de precision o bisturi\n"
          "- Regla metalica\n"
          "- Cinta adhesiva transparente\n"
          "- Pantalla blanca (cartulina blanca o pared)\n"
          "- Camara o celular para documentar\n"
          "- Tripode o soporte para el laser\n"
          "- Cuarto oscuro\n"
          "\nPROCEDIMIENTO DE CONSTRUCCION\n"
          "PASO 1: Preparar el soporte\n  - Corta un rectangulo de carton paja de 15x15 cm\n  - Haz un marco rectangular en el centro (5x3 cm)\n"
          "PASO 2: Preparar las rendijas\n  - Corta papel aluminio de 8x8 cm (debe estar muy plano)\n  - Pegalo sobre el marco del carton con cinta adhesiva\n  - Asegurate que quede bien estirado sin arrugas\n"
          "PASO 3: Hacer las rendijas (la parte mas critica)\n  - Con la cuchilla y una regla metalica, haz dos cortes paralelos\n  - Ancho de cada rendija: ~0.1-0.2 mm (lo mas fino posible)\n  - Separacion entre rendijas: ~0.3-0.5 mm\n  - Los cortes deben ser completamente rectos y paralelos, de al menos 2 cm de largo\n  - Consejo: Practica primero en otro pedazo de aluminio\n"
          "PASO 4: Montaje del experimento\n  - Coloca el laser en un soporte estable\n  - Pon las rendijas a 10-20 cm del laser\n  - Coloca la pantalla a 1-3 metros de las rendijas\n  - Alinea todo en linea recta\n"
          "PASO 5: Observacion y ajuste\n  - Enciende el laser en un cuarto oscuro\n  - Ajusta la posicion hasta ver el patron\n  - Deberias ver multiples franjas verticales de luz\n"
          "PASO 6: Documentacion\n  - Toma fotos del montaje completo\n  - Fotografia el patron de interferencia (usa tripode)\n  - Graba un video mostrando el experimento\n  - Mide la separacion entre franjas con una regla\n"
          "\nMEDICIONES IMPORTANTES\n"
          "1. Distancia rendijas-pantalla (L): _____ metros\n"
          "2. Separacion entre franjas brillantes: _____ mm\n"
          "3. Numero de franjas visibles: _____\n"
          "4. Ancho del patron completo: _____ mm\n"
          "\nCon estas mediciones puedes calcular:\n  d = (lambda x L) / Delta_y\nDonde:\n  d = separacion entre rendijas\n  lambda = longitud de onda del laser (632 nm para rojo)\n  L = distancia a la pantalla\n  Delta_y = separacion entre franjas\n"
          "\nDOCUMENTACION REQUERIDA\n"
          "- Fotos del material antes de empezar\n"
          "- Fotos del proceso de construccion\n"
          "- Foto cercana de las rendijas\n"
          "- Foto del montaje completo\n"
          "- Foto del patron de interferencia (alta calidad)\n"
          "- Video del experimento funcionando\n"
          "- Video explicando el fenomeno observado\n"
          "\nANALISIS Y REPORTE\n"
          "1. INTRODUCCION\n  - Contexto historico del experimento\n  - Importancia en la fisica cuantica\n"
          "2. MARCO TEORICO\n  - Explicacion de difraccion e interferencia\n  - Ecuaciones relevantes\n  - Predicciones teoricas\n"
          "3. METODOLOGIA\n  - Descripcion del montaje\n  - Proceso de construccion\n  - Parametros del experimento\n"
          "4. RESULTADOS\n  - Fotos y videos del experimento\n  - Mediciones realizadas\n  - Simulaciones con esta libreria\n  - Comparacion teoria vs experimento\n"
          "5. DISCUSION\n  - Analisis de los patrones obtenidos\n  - Fuentes de error\n  - Mejoras posibles\n"
          "6. CONCLUSIONES\n  - Que demuestra el experimento\n  - Conexion con la mecanica cuantica\n"
          "\nPRECAUCIONES DE SEGURIDAD\n"
          "- NUNCA mires directamente al haz del laser\n"
          "- NUNCA apuntes el laser a personas o animales\n"
          "- Ten cuidado al usar la cuchilla\n"
          "- Manten el area de trabajo limpia y ordenada\n"
          "\nCONSEJOS PARA MEJORES RESULTADOS\n"
          "- Realiza el experimento en completa oscuridad\n"
          "- Usa un tripode para el laser (evita vibraciones)\n"
          "- Si no ves el patron, intenta con rendijas mas anchas primero\n"
          "- La humedad puede afectar el aluminio - trabaja en ambiente seco\n"
          "- Toma multiples fotos con diferentes exposiciones\n"
          "- Mide varias veces para obtener promedios\n"
          "\nCRITERIOS DE CALIDAD\n"
          "- Se ven claramente multiples franjas (minimo 5)\n"
          "- Las franjas son rectas y uniformes\n"
          "- El patron es simetrico\n"
          "- Puedes medir la separacion entre franjas\n"
          "- Tus mediciones coinciden con la teoria (10-20% error es aceptable)\n"
          "\nRECURSOS ADICIONALES\n"
          "- Instructables: https://www.instructables.com/id/How-To-Make-a-Simple-Double-Slit/\n"
          "- Video explicativo: https://www.youtube.com/watch?v=PVyJFzx7zig\n"
          "- Simulador: Esta libreria de Python\n"
          "\nBUENA SUERTE CON TU EXPERIMENTO!\n"
          "Recuerda: Este experimento demostro uno de los misterios mas profundos del universo: la luz se comporta como onda Y como particula. Estas replicando uno de los experimentos mas importantes de la historia de la fisica!\n"
     )


def guia_uso_libreria():
    """Guía de uso de la librería con ejemplos."""
    guia = """
    
             GUÍA DE USO - LIBRERÍA DE SIMULACIÓN                        


EJEMPLOS DE USO

1.SIMULACIÓN BÁSICA
```python
# Ejemplo de uso directo
# Crear experimento con parámetros por defecto (láser rojo)
exp = ExperimentoDobleRendija()

# Simular patrón de doble rendija
y, intensidad = exp.simular(doble=True)

# Graficar resultado
graficar_patron(y, intensidad, titulo="Mi Experimento")
```

2.OBTENER PREDICCIONES PARA TU EXPERIMENTO

```python
# Crear experimento con TUS parámetros medidos
exp = ExperimentoDobleRendija(
    longitud_onda=632e-9,      # Láser rojo (632 nm)
    ancho_rendija=100e-6,      # 100 micrómetros (0.1 mm)
    separacion=400e-6,         # 400 micrómetros (0.4 mm)
    distancia_pantalla=2.0     # 2 metros
)

# Ver predicciones
exp.imprimir_predicciones()

# Calcular posiciones específicas
resultados = exp.calcular_posiciones_franjas()
print(f"Separación entre franjas: {resultados.separacion_franjas*1000:.2f} mm")
```

3. COMPARAR CON TUS MEDICIONES EXPERIMENTALES
```python
import numpy as np

# Tus datos experimentales (ejemplo)
# Posiciones en metros, intensidad normalizada 0-1
y_medido = np.linspace(-0.005, 0.005, 100)
intensidad_medida = np.random.random(100)  # Reemplaza con tus datos reales

# Comparar con teoría
stats = comparar_experimento_teoria(
    y_medido, 
    intensidad_medida, 
    exp,
    guardar="comparacion.png"
)
```

4. SIMULAR DIFERENTES COLORES

```python
import matplotlib.pyplot as plt

colores = {
    'rojo': 632e-9,
    'verde': 532e-9,
    'azul': 450e-9
}

plt.figure(figsize=(12, 6))
for nombre, longitud in colores.items():
    exp = ExperimentoDobleRendija(longitud_onda=longitud)
    y, I = exp.simular()
    plt.plot(y*1000, I, label=f'Láser {nombre} ({longitud*1e9:.0f} nm)')

plt.legend()
plt.xlabel('Posición (mm)')
plt.ylabel('Intensidad')
plt.title('Efecto del Color en el Patrón de Interferencia')
plt.grid(True, alpha=0.3)
plt.show()
```

5. EXPORTAR RESULTADOS

```python
# Simular y guardar gráficos
y, I = exp.simular()
graficar_patron(y, I, 
                titulo="Experimento Grupo 3",
                guardar="patron_interferencia.png",
                mostrar_predicciones=True,
                experimento=exp)

# Guardar datos numéricos
np.savetxt('datos_simulacion.txt', 
           np.column_stack([y*1000, I]),
           header='Posicion(mm) Intensidad',
           comments='')
```

6. ANÁLISIS COMPLETO PARA EL REPORTE

```python
# 1. Crear experimento con tus parámetros
exp = ExperimentoDobleRendija(
    longitud_onda=632e-9,
    ancho_rendija=150e-6,
    separacion=500e-6,
    distancia_pantalla=1.5
)

# 2. Ver predicciones
print(guia_proyecto_completa())
exp.imprimir_predicciones()

# 3. Simular
y, I = exp.simular(ancho=0.02, puntos=3000)

# 4. Graficar con predicciones
graficar_patron(y, I, 
                titulo="Simulación - Grupo X",
                guardar="simulacion_teoria.png",
                mostrar_predicciones=True,
                experimento=exp)

# 5. Comparar con experimento (cuando tengas datos)
# y_exp, I_exp = cargar_datos_experimentales()  # Tu función
# comparar_experimento_teoria(y_exp, I_exp, exp, guardar="comparacion.png")
```

 PARÁMETROS TÍPICOS

• Longitud de onda: 632e-9 m (láser rojo común)
• Ancho de rendija: 50e-6 a 200e-6 m (0.05-0.2 mm)
• Separación: 200e-6 a 500e-6 m (0.2-0.5 mm)
• Distancia pantalla: 0.5 a 3.0 m

 CONSEJOS PARA EL ANÁLISIS

1. Primero simula con parámetros estimados
2. Realiza tu experimento físico
3. Mide los parámetros reales lo mejor posible
4. Re-simula con los parámetros reales
5. Compara teoría vs experimento
6. Discute las diferencias (siempre las hay!)


"""
    print(guia)


# ------------------------
# Funciones de demostración mejoradas
# ------------------------
def demo_simple_vs_doble():
    """Comparación entre rendija simple y doble rendija."""
    sim = ExperimentoDobleRendija()
    y, I_simple = sim.simular(doble=False)
    y, I_doble = sim.simular(doble=True)
    
    plt.figure(figsize=(14, 6))
    
    # Gráfico comparativo
    plt.subplot(1, 2, 1)
    plt.plot(y*1000, I_simple, 'b-', label="Rendija Simple (solo difracción)", lw=2)
    plt.plot(y*1000, I_doble, 'r-', label="Doble Rendija (difracción + interferencia)", lw=2)
    plt.legend(fontsize=10)
    plt.xlabel("Posición (mm)")
    plt.ylabel("Intensidad Normalizada")
    plt.title("Comparación: Rendija Simple vs Doble Rendija")
    plt.grid(True, alpha=0.4)
    
    # Patrones 2D lado a lado
    plt.subplot(1, 2, 2)
    patron_combinado = np.vstack([
        np.tile(I_simple, (25, 1)),
        np.ones((5, len(I_simple))) * 0.5,  # Separador
        np.tile(I_doble, (25, 1))
    ])
    extent = [y[0]*1000, y[-1]*1000, -2, 2]
    plt.imshow(patron_combinado, extent=extent, aspect="auto", cmap="inferno")
    plt.axhline(0, color='white', linestyle='--', lw=1, alpha=0.5)
    plt.text(0, 1.5, 'Rendija Simple', ha='center', color='white', fontsize=10)
    plt.text(0, -1.5, 'Doble Rendija', ha='center', color='white', fontsize=10)
    plt.title("Visualización 2D - Comparación")
    plt.xlabel("Posición (mm)")
    plt.colorbar(label="Intensidad")
    
    plt.tight_layout()
    plt.show()
    
    print("\n OBSERVA LA DIFERENCIA:")
    print("   • Rendija simple: Patrón de difracción suave")
    print("   • Doble rendija: Franjas de interferencia múltiples")
    print("   • La envolvente de la doble rendija sigue el patrón de rendija simple")


def demo_efecto_parametros():
    """Demuestra el efecto de variar diferentes parámetros."""
    axes = plt.subplots(2, 2, figsize=(14, 10))[1]

    # 1. Efecto de la distancia a la pantalla
    ax = axes[0, 0]
    distancias = [0.5, 1.0, 2.0]
    for d in distancias:
        exp = ExperimentoDobleRendija(distancia_pantalla=d)
        y, I = exp.simular()
        ax.plot(y*1000, I, label=f'L = {d} m')
    ax.set_xlabel('Posición (mm)')
    ax.set_ylabel('Intensidad')
    ax.set_title('Efecto de la Distancia a la Pantalla')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # 2. Efecto de la separación entre rendijas
    ax = axes[0, 1]
    separaciones = [150e-6, 250e-6, 400e-6]
    for s in separaciones:
        exp = ExperimentoDobleRendija(separacion=s)
        y, I = exp.simular()
        ax.plot(y*1000, I, label=f'd = {s*1e6:.0f} μm')
    ax.set_xlabel('Posición (mm)')
    ax.set_ylabel('Intensidad')
    ax.set_title('Efecto de la Separación entre Rendijas')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # 3. Efecto del ancho de rendija
    ax = axes[1, 0]
    anchos = [30e-6, 70e-6, 150e-6]
    for a in anchos:
        exp = ExperimentoDobleRendija(ancho_rendija=a)
        y, I = exp.simular()
        ax.plot(y*1000, I, label=f'a = {a*1e6:.0f} μm')
    ax.set_xlabel('Posición (mm)')
    ax.set_ylabel('Intensidad')
    ax.set_title('Efecto del Ancho de Rendija')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # 4. Efecto de la longitud de onda (color)
    ax = axes[1, 1]
    colores_laser = {
        'Violeta': (405e-9, 'purple'),
        'Azul': (450e-9, 'blue'),
        'Verde': (532e-9, 'green'),
        'Rojo': (632e-9, 'red')
    }
    for nombre, (longitud, color) in colores_laser.items():
        exp = ExperimentoDobleRendija(longitud_onda=longitud)
        y, I = exp.simular()
        ax.plot(y*1000, I, label=f'{nombre} ({longitud*1e9:.0f} nm)', color=color)
    ax.set_xlabel('Posición (mm)')
    ax.set_ylabel('Intensidad')
    ax.set_title('Efecto de la Longitud de Onda (Color del Láser)')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    print("\n LECCIONES IMPORTANTES:")
    print("   • Mayor distancia -> franjas más separadas")
    print("   • Mayor separación entre rendijas -> franjas más juntas")


def demo_completo_para_proyecto():
    """Demostración completa pensada para el proyecto educativo."""
    print(guia_proyecto_completa())
    print("\n" + "="*70)
    print("INICIANDO SIMULACIONES DE DEMOSTRACIÓN")
    print("="*70)
    
    # Crear experimento con parámetros realistas
    exp = ExperimentoDobleRendija(
        longitud_onda=632e-9,
        ancho_rendija=100e-6,
        separacion=400e-6,
        distancia_pantalla=1.5
    )
    
    # Mostrar predicciones
    exp.imprimir_predicciones()
    
    # Demo 1: Simple vs Doble
    print("\n\n Demo 1: Comparación Rendija Simple vs Doble Rendija")
    print("-" * 70)
    demo_simple_vs_doble()
    
    # Demo 2: Simulación con predicciones
    print("\n\n Demo 2: Simulación con Predicciones Teóricas")
    print("-" * 70)
    y, I = exp.simular(ancho=0.015, puntos=3000)
    graficar_patron(y, I, 
                    titulo="Simulación para tu Experimento",
                    mostrar_predicciones=True,
                    experimento=exp)
    
    # Demo 3: Efecto de parámetros
    print("\n\n Demo 3: Efecto de Variar Parámetros")
    print("-" * 70)
    demo_efecto_parametros()
    
    print("\n\n" + "="*70)
    print(" SIMULACIONES COMPLETADAS")
    print("="*70)
    print("\n PRÓXIMOS PASOS:")
    print("   1. Construye tu experimento físico siguiendo la guía")
    print("   2. Toma fotos y videos de calidad")
    print("   3. Mide la separación entre franjas")
    print("   4. Usa esta librería para comparar teoría vs experimento")
    print("   5. Prepara tu reporte con las simulaciones")
    print("\n¡Éxito con tu proyecto!\n")


# Ejecución directa

if __name__ == "__main__":
    print(" SIMULACIÓN DEL EXPERIMENTO DE LA DOBLE RENDIJA - VERSIÓN MEJORADA   ")
    
    print("\n")
    
    # Ejecutar demostración completa
    demo_completo_para_proyecto()
    
    # Mostrar guía de uso
    print("\n\n")
    guia_uso_libreria()
