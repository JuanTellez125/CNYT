"""
Ejemplos Practicos - Experimento de la Doble Rendija
====================================================

Autores: Camilo Aguirre, Mateo 
Fecha: 03/10/2025
"""

import sys
sys.path.append("c:\\Users\\camilo\\OneDrive\\Documentos\\Proyecto")

from doble_rendija import (
    ExperimentoDobleRendija, 
    graficar_patron, 
    comparar_experimento_teoria,
    guia_proyecto_completa,
    demo_completo_para_proyecto
)
import numpy as np
import matplotlib.pyplot as plt


# ============================================================================
# EJEMPLO 1: PREDICCIONES PARA TU EXPERIMENTO
# ============================================================================
def ejemplo_1_predicciones():
    """
    Usa esto ANTES de hacer tu experimento físico para saber qué esperar.
    """
    print("\n" + "="*70)
    print("EJEMPLO 1: PREDICCIONES PARA TU EXPERIMENTO")
    print("="*70)
    
    exp = ExperimentoDobleRendija(
        longitud_onda=632e-9,        # Láser rojo típico (632 nm)
        ancho_rendija=100e-6,        # 0.1 mm 
        separacion=400e-6,           # 0.4 mm 
        distancia_pantalla=1.5       # 1.5 metros 
    )
    
    # Imprimir predicciones
    exp.imprimir_predicciones()
    
    # Simular y visualizar
    y, intensidad = exp.simular(ancho=0.02, puntos=3000, doble=True)
    graficar_patron(y, intensidad, 
                    titulo="Predicción para Mi Experimento",
                    mostrar_predicciones=True,
                    experimento=exp,
                    guardar="prediccion_mi_experimento.png")
    
    return exp


# ============================================================================
# EJEMPLO 2: SIMULACIÓN PARA EL REPORTE
# ============================================================================
def ejemplo_2_simulacion_reporte():
    """
    Genera gráficos de calidad para incluir en tu reporte.
    """
    print("\n" + "="*70)
    print("EJEMPLO 2: SIMULACIONES PARA TU REPORTE")
    print("="*70)
    
    # Parámetros del experimento
    exp = ExperimentoDobleRendija(
        longitud_onda=632e-9,
        ancho_rendija=120e-6,
        separacion=450e-6,
        distancia_pantalla=2.0
    )
    
    # 1. Patrón de doble rendija
    print("\n📊 Generando patrón de doble rendija...")
    y, I_doble = exp.simular(doble=True)
    graficar_patron(y, I_doble, 
                    titulo="Patrón de Interferencia - Doble Rendija",
                    guardar="reporte_doble_rendija.png",
                    mostrar_predicciones=True,
                    experimento=exp)
    
    # 2. Comparación simple vs doble
    print("\n📊 Generando comparación simple vs doble...")
    y, I_simple = exp.simular(doble=False)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    ax1.plot(y*1000, I_simple, 'b-', lw=2, label='Rendija Simple')
    ax1.set_xlabel('Posición (mm)')
    ax1.set_ylabel('Intensidad Normalizada')
    ax1.set_title('Rendija Simple - Solo Difracción')
    ax1.grid(True, alpha=0.4)
    ax1.legend()
    
    ax2.plot(y*1000, I_doble, 'r-', lw=2, label='Doble Rendija')
    ax2.set_xlabel('Posición (mm)')
    ax2.set_ylabel('Intensidad Normalizada')
    ax2.set_title('Doble Rendija - Difracción + Interferencia')
    ax2.grid(True, alpha=0.4)
    ax2.legend()
    
    plt.tight_layout()
    plt.savefig('reporte_comparacion.png', dpi=300, bbox_inches='tight')
    print("✅ Guardado: reporte_comparacion.png")
    plt.show()
    
    # 3. Efecto de la longitud de onda
    print("\n📊 Generando efecto del color del láser...")
    plt.figure(figsize=(12, 6))
    
    colores = {
        'Azul (450 nm)': (450e-9, 'blue'),
        'Verde (532 nm)': (532e-9, 'green'),
        'Rojo (632 nm)': (632e-9, 'red')
    }
    
    for nombre, (longitud, color) in colores.items():
        exp_color = ExperimentoDobleRendija(
            longitud_onda=longitud,
            ancho_rendija=120e-6,
            separacion=450e-6,
            distancia_pantalla=2.0
        )
        y, I = exp_color.simular()
        plt.plot(y*1000, I, color=color, lw=2, label=nombre)
    
    plt.xlabel('Posición (mm)', fontsize=12)
    plt.ylabel('Intensidad Normalizada', fontsize=12)
    plt.title('Efecto de la Longitud de Onda en el Patrón de Interferencia', fontsize=14)
    plt.legend(fontsize=11)
    plt.grid(True, alpha=0.4)
    plt.tight_layout()
    plt.savefig('reporte_colores.png', dpi=300, bbox_inches='tight')
    print("✅ Guardado: reporte_colores.png")
    plt.show()
    
    print("\n✅ Gráficos para reporte generados exitosamente!")


# ============================================================================
# EJEMPLO 3: ANÁLISIS DE DATOS EXPERIMENTALES
# ============================================================================
def ejemplo_3_analisis_experimental():

    print("\n" + "="*70)
    print("EJEMPLO 3: ANÁLISIS DATOS EXPERIMENTALES")
    print("="*70)
    
    # ========================================
    # OPCIÓN A: Simular datos experimentales (para demostración)
    # ========================================
    print("\n⚠️ NOTA: Usando datos simulados para demostración")
    print("   Reemplaza esto con tus datos reales del experimento\n")
    
    # Parámetros del experimento
    exp = ExperimentoDobleRendija(
        longitud_onda=632e-9,
        ancho_rendija=120e-6,
        separacion=450e-6,
        distancia_pantalla=2.0
    )
    
    # Generar datos "experimentales" simulados (con ruido)
    y_teorico, I_teorico = exp.simular(ancho=0.015, puntos=200)
    
    # Agregar ruido para simular datos reales
    ruido = np.random.normal(0, 0.05, len(I_teorico))
    I_experimental = np.clip(I_teorico + ruido, 0, 1)
    
    # Realizar comparación
    print("\n📊 Comparando teoría vs experimento...")
    stats = comparar_experimento_teoria(
        y_teorico,  # Reemplaza con y_experimental
        I_experimental,
        exp,
        guardar="reporte_comparacion_experimental.png"
    )
    
    # Análisis adicional
    print("\n📈 ANÁLISIS ESTADÍSTICO:")
    print(f"   • Correlación: {stats['correlacion']:.4f}")
    print(f"   • Error cuadrático medio: {stats['mse']:.6f}")
    print(f"   • Desviación estándar de residuos: {np.std(stats['residuos']):.4f}")
    
    # Guardar resultados
    np.savetxt('resultados_analisis.txt', 
               np.column_stack([y_teorico*1000, I_experimental, I_teorico]),
               header='Posicion(mm) Experimental Teorico',
               fmt='%.6f')
    print("\n✅ Resultados guardados en: resultados_analisis.txt")


# ============================================================================
# EJEMPLO 4: MEDICIONES Y CÁLCULOS
# ============================================================================
def ejemplo_4_calcular_parametros_desde_mediciones():
    """
    Si mediste la separación entre franjas, calcula los parámetros del experimento.
    """
    print("\n" + "="*70)
    print("EJEMPLO 4: CALCULAR PARÁMETROS DESDE TUS MEDICIONES")
    print("="*70)
    
    # ========================================
    # MEDICIONES
    # ========================================
    separacion_franjas_medida = 2.5e-3  # mm convertido a metros 
    distancia_pantalla = 2.0             # metros 
    longitud_onda = 632e-9               # metros (láser rojo)
    
    print(f"\n📏 Mediciones del experimento:")
    print(f"   • Separación entre franjas: {separacion_franjas_medida*1000:.2f} mm")
    print(f"   • Distancia a la pantalla: {distancia_pantalla:.2f} m")
    print(f"   • Longitud de onda del láser: {longitud_onda*1e9:.0f} nm")
    
    # Calcular separación entre rendijas
    # Fórmula: Δy = (λ × L) / d  →  d = (λ × L) / Δy
    separacion_rendijas = (longitud_onda * distancia_pantalla) / separacion_franjas_medida
    
    print(f"\n🔍 PARÁMETROS CALCULADOS:")
    print(f"   • Separación entre rendijas: {separacion_rendijas*1e6:.1f} μm ({separacion_rendijas*1e3:.3f} mm)")
    
    # Validar si es razonable
    if 100e-6 <= separacion_rendijas <= 1000e-6:
        print("   ✅ Este valor es razonable para un experimento casero")
    else:
        print("   ⚠️ Este valor parece inusual, verifica tus mediciones")
    
    # Crear experimento con parámetros calculados
    exp = ExperimentoDobleRendija(
        longitud_onda=longitud_onda,
        ancho_rendija=100e-6,  # Estimación (difícil de medir)
        separacion=separacion_rendijas,
        distancia_pantalla=distancia_pantalla
    )
    
    # Simular con estos parámetros
    y, I = exp.simular()
    graficar_patron(y, I, 
                    titulo="Simulación con Parámetros Medidos",
                    mostrar_predicciones=True,
                    experimento=exp)


# ============================================================================
# EJEMPLO 5: EXPORTAR TODO PARA EL REPORTE
# ============================================================================
def ejemplo_5_exportar_todo():
    """
    Genera todos los archivos necesarios para tu reporte.
    """
    print("\n" + "="*70)
    print("EJEMPLO 5: EXPORTAR TODO PARA EL REPORTE")
    print("="*70)
    
    # Parámetros del experimento
    exp = ExperimentoDobleRendija(
        longitud_onda=632e-9,
        ancho_rendija=120e-6,
        separacion=450e-6,
        distancia_pantalla=2.0
    )
    
    print("\n📦 Generando todos los archivos...")
    
    # 1. Predicciones teóricas en texto
    resultados = exp.calcular_posiciones_franjas(n_max=10)
    with open('predicciones_teoricas.txt', 'w', encoding='utf-8') as f:
        f.write("PREDICCIONES TEÓRICAS DEL EXPERIMENTO\n")
        f.write("="*50 + "\n\n")
        f.write(f"Parámetros:\n")
        f.write(f"  - Longitud de onda: {resultados.parametros['longitud_onda_nm']:.1f} nm\n")
        f.write(f"  - Ancho de rendija: {resultados.parametros['ancho_rendija_um']:.1f} μm\n")
        f.write(f"  - Separación: {resultados.parametros['separacion_um']:.1f} μm\n")
        f.write(f"  - Distancia pantalla: {resultados.parametros['distancia_pantalla_m']:.2f} m\n\n")
        f.write(f"Predicciones:\n")
        f.write(f"  - Separación entre franjas: {resultados.parametros['separacion_franjas_mm']:.2f} mm\n")
        f.write(f"  - Ancho máximo central: {resultados.parametros['ancho_central_mm']:.2f} mm\n\n")
        f.write(f"Posiciones de máximos (mm):\n")
        for i, pos in enumerate(resultados.posiciones_maximos):
            orden = i - len(resultados.posiciones_maximos)//2
            f.write(f"  Orden {orden:3d}: {pos*1000:8.3f}\n")
    print("✅ Guardado: predicciones_teoricas.txt")
    
    # 2. Datos de simulación
    y, I = exp.simular(puntos=2000)
    np.savetxt('datos_simulacion.csv', 
               np.column_stack([y*1000, I]),
               header='Posicion_mm,Intensidad_normalizada',
               delimiter=',',
               comments='')
    print("✅ Guardado: datos_simulacion.csv")
    
    # 3. Gráfico principal
    graficar_patron(y, I, 
                    titulo="Simulación Teórica - Doble Rendija",
                    mostrar_predicciones=True,
                    experimento=exp,
                    guardar="grafico_principal.png")
    print("✅ Guardado: grafico_principal.png")
    
    # 4. Comparación simple vs doble
    y_s, I_s = exp.simular(doble=False)
    y_d, I_d = exp.simular(doble=True)
    
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    
    axes[0].plot(y_s*1000, I_s, 'b-', lw=2)
    axes[0].set_ylabel('Intensidad')
    axes[0].set_title('Rendija Simple (Solo Difracción)')
    axes[0].grid(True, alpha=0.4)
    
    axes[1].plot(y_d*1000, I_d, 'r-', lw=2)
    axes[1].set_xlabel('Posición (mm)')
    axes[1].set_ylabel('Intensidad')
    axes[1].set_title('Doble Rendija (Difracción + Interferencia)')
    axes[1].grid(True, alpha=0.4)
    
    plt.tight_layout()
    plt.savefig('comparacion_simple_doble.png', dpi=300, bbox_inches='tight')
    print("✅ Guardado: comparacion_simple_doble.png")
    plt.close()
    
    print("\n✅ TODOS LOS ARCHIVOS GENERADOS EXITOSAMENTE!")
    print("\nArchivos creados:")
    print("  • predicciones_teoricas.txt")
    print("  • datos_simulacion.csv")
    print("  • grafico_principal.png")
    print("  • comparacion_simple_doble.png")


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================
def menu_principal():
    """Menú interactivo para ejecutar ejemplos."""
    print("\n+--------------------------------------------------------------------------+")
    print("|              EJEMPLOS PRACTICOS - EXPERIMENTO DOBLE RENDIJA             |")
    print("+--------------------------------------------------------------------------+")
    print("\nQue quieres hacer?\n")
    print("1. Ver predicciones para mi experimento (ANTES del experimento)")
    print("2. Generar graficos para el reporte")
    print("3. Analizar datos experimentales (DESPUES del experimento)")
    print("4. Calcular parametros desde mis mediciones")
    print("5. Exportar todo para el reporte")
    print("6. Ver demostracion completa")
    print("7. Ver guia del proyecto")
    print("0. Salir")
    
    return input("\nElige una opción (0-7): ")


if __name__ == "__main__":
    while True:
        opcion = menu_principal()
        
        if opcion == '1':
            ejemplo_1_predicciones()
        elif opcion == '2':
            ejemplo_2_simulacion_reporte()
        elif opcion == '3':
            ejemplo_3_analisis_experimental()
        elif opcion == '4':
            ejemplo_4_calcular_parametros_desde_mediciones()
        elif opcion == '5':
            ejemplo_5_exportar_todo()
        elif opcion == '6':
            demo_completo_para_proyecto()
        elif opcion == '7':
            print(guia_proyecto_completa())
        elif opcion == '0':
            print("\n¡Hasta luego! Éxito con tu proyecto \n")
            break
        else:
            print("\n Opción inválida. Intenta de nuevo.")
        
        input("\n Presiona Enter para continuar...")
