import os
import json
from django.core.management.base import BaseCommand
# Recuerda cambiar "checkout" por el nombre real de tu aplicación de Django
from checkout.models import Departamento, Municipio, Barrio 

class Command(BaseCommand):
    help = 'Abre un archivo JSON geográfico personalizado y puebla la base de datos'

    def handle(self, *args, **kwargs):
        # 1. Buscamos el archivo JSON en la misma carpeta donde está este script
        ruta_actual = os.path.dirname(__file__)
        ruta_json = os.path.join(ruta_actual, 'geografia.json')

        # Control de seguridad por si mueves el archivo de sitio
        if not os.path.exists(ruta_json):
            self.stdout.write(self.style.ERROR(f'Error: No se encontró el archivo JSON en {ruta_json}'))
            return

        self.stdout.write(self.style.SUCCESS('Leyendo el archivo JSON...'))

        # 2. Abrimos y procesamos el JSON usando UTF-8 para no tener problemas con las tildes
        with open(ruta_json, 'r', encoding='utf-8') as archivo:
            datos_geograficos = json.load(archivo)

        # 3. Recorremos la estructura e insertamos usando get_or_create
        for nombre_dep, municipios in datos_geograficos.items():
            # Crea el departamento si no existe; si ya existe, lo recupera sin duplicar
            departamento, creado_dep = Departamento.objects.get_or_create(nombre=nombre_dep)
            if creado_dep:
                self.stdout.write(self.style.SUCCESS(f'✔ Departamento creado: {nombre_dep}'))
            else:
                self.stdout.write(f'• Departamento ya existía: {nombre_dep}')

            for nombre_mun, barrios in municipios.items():
                municipio, creado_mun = Municipio.objects.get_or_create(
                    departamento=departamento, 
                    nombre=nombre_mun
                )
                if creado_mun:
                    self.stdout.write(self.style.SUCCESS(f'  ✔ Municipio creado: {nombre_mun}'))

                for nombre_barrio in barrios:
                    barrio, creado_barrio = Barrio.objects.get_or_create(
                        municipio=municipio,
                        nombre=nombre_barrio
                    )
                    if creado_barrio:
                        self.stdout.write(f'    ✔ Barrio creado: {nombre_barrio}')

        self.stdout.write(self.style.SUCCESS('¡Proceso de carga completado con éxito!'))