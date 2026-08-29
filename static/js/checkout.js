

// Funcionalidad AJAX para los selects en cascada de departamento, municipio y barrio
document.addEventListener('DOMContentLoaded', function() {
    // 1. Obtenemos el formulario y los selects
    const form = document.getElementById('checkout-form');
    const departamentoSelect = document.getElementById('id_departamento');
    const municipioSelect = document.getElementById('id_municipio');
    const barrioSelect = document.getElementById('id_barrio');

    // 2. Leemos las URLs dinámicas que Django pondrá en el HTML
    const urlMunicipios = form.getAttribute('data-url-municipios');
    const urlBarrios = form.getAttribute('data-url-barrios');

    // Evento cuando cambia el Departamento
    if (departamentoSelect) {
        departamentoSelect.addEventListener('change', function() {
            const departamentoId = this.value;
            
            // Limpiar opciones
            municipioSelect.innerHTML = '<option value="">---------</option>';
            barrioSelect.innerHTML = '<option value="">---------</option>';

            if (departamentoId) {
                fetch(`${urlMunicipios}?departamento=${departamentoId}`)
                    .then(response => response.json())
                    .then(data => {
                        data.forEach(municipio => {
                            let option = new Option(municipio.nombre, municipio.id);
                            municipioSelect.add(option);
                        });
                    })
                    .catch(error => console.error('Error cargando municipios:', error));
            }
        });
    }

    // Evento cuando cambia el Municipio
    if (municipioSelect) {
        municipioSelect.addEventListener('change', function() {
            const municipioId = this.value;
            
            // Limpiar opciones de barrio
            barrioSelect.innerHTML = '<option value="">---------</option>';

            if (municipioId) {
                fetch(`${urlBarrios}?municipio=${municipioId}`)
                    .then(response => response.json())
                    .then(data => {
                        data.forEach(barrio => {
                            let option = new Option(barrio.nombre, barrio.id);
                            barrioSelect.add(option);
                        });
                    })
                    .catch(error => console.error('Error cargando barrios:', error));
            }
        });
    }
});



// Funcionalidad de tarifa
document.addEventListener("DOMContentLoaded", function() {
    
    // 1. Capturamos los elementos del DOM
    const form = document.getElementById("checkout-form");
    const selectDepartamento = document.getElementById("id_departamento"); 
    const spanCostoEnvio = document.getElementById("costo-envio");
    const spanTotalFinal = document.getElementById("total-final");
    const spanTotalProductos = document.getElementById("total-productos");

    // Validamos que estemos en la página correcta para evitar errores en otras vistas
    if (!selectDepartamento) return;

    // 2. Extraemos la URL de la vista AJAX y el total inicial de los productos
    const urlTarifa = form.getAttribute("data-url-tarifa");
    
    // Aseguramos que el total se lea como un número decimal (reemplazando comas por puntos si tu Django está en español)
    const totalString = spanTotalProductos.getAttribute("data-total").replace(',', '.');
    const totalProductos = parseFloat(totalString) || 0;

    // Herramienta para formatear los números estilo moneda (ej: 15.000,00)
    const formatoMoneda = new Intl.NumberFormat('es-CO', {
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    });

    // 3. Escuchamos el cambio en el selector de departamento
    selectDepartamento.addEventListener("change", function() {
        const departamentoId = this.value;

        // Si el usuario deselecciona el departamento, volvemos a $0.00
        if (!departamentoId) {
            spanCostoEnvio.textContent = "0.00";
            spanTotalFinal.textContent = formatoMoneda.format(totalProductos);
            return;
        }

        // 4. Hacemos la petición AJAX al backend
        fetch(`${urlTarifa}?departamento=${departamentoId}`)
            .then(response => response.json())
            .then(data => {
                const tarifa = parseFloat(data.tarifa) || 0;
                
                // Sumamos los valores
                const totalFinal = totalProductos + tarifa;

                // 5. Inyectamos los nuevos valores formateados en el HTML
                spanCostoEnvio.textContent = formatoMoneda.format(tarifa);
                spanTotalFinal.textContent = formatoMoneda.format(totalFinal);
            })
            .catch(error => {
                console.error("Error al obtener la tarifa de envío:", error);
                // Si hay error de red, por seguridad mostramos 0 temporalmente
                spanCostoEnvio.textContent = "0.00";
                spanTotalFinal.textContent = formatoMoneda.format(totalProductos);
            });
    });
});