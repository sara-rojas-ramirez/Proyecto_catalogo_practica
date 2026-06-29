


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