document.addEventListener('DOMContentLoaded', () => {
    const dropzone = document.getElementById('dropzone');
    const fileInput = document.getElementById('fileInput');
    const resultsPanel = document.getElementById('resultsPanel');
    
    // Elementos del Modal
    const modalOverlay = document.getElementById('modalOverlay');
    const modalContent = document.getElementById('modalContent');
    const modalLoading = document.getElementById('modalLoading');
    const modalSuccess = document.getElementById('modalSuccess');
    const btnVerResultados = document.getElementById('btnVerResultados');

    let resumenProcesamiento = null;

    dropzone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropzone.classList.add('drag-active');
    });

    dropzone.addEventListener('dragleave', () => dropzone.classList.remove('drag-active'));

    dropzone.addEventListener('drop', (e) => {
        e.preventDefault();
        dropzone.classList.remove('drag-active');
        if (e.dataTransfer.files.length > 0) procesarArchivo(e.dataTransfer.files[0]);
    });

    dropzone.addEventListener('click', () => fileInput.click());
    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) procesarArchivo(e.target.files[0]);
    });

    async function procesarArchivo(file) {
        if (!file.name.endsWith('.csv')) {
            alert('Por favor, sube un archivo con extensión .csv');
            return;
        }

        // 1. Mostrar Modal de Carga
        mostrarModalCarga();

        const formData = new FormData();
        formData.append('archivo', file);

        try {
            const response = await fetch('http://localhost:8000/api/ahe/cargar-csv', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();
            if (!response.ok) throw new Error(data.detail || 'Error en el servidor');

            resumenProcesamiento = data.resumen;
            
            // 2. Transición a estado de Éxito en el Modal (simulamos 500ms para UX)
            setTimeout(() => {
                mostrarModalExito();
            }, 500);

        } catch (error) {
            console.error(error);
            ocultarModal();
            alert(`Error: ${error.message}`);
        }
    }

    // Botón dentro del modal para cerrar y ver la tabla
    btnVerResultados.addEventListener('click', () => {
        ocultarModal();
        renderizarTablaResultados(resumenProcesamiento);
    });

    // --- Funciones de UI ---
    function mostrarModalCarga() {
        modalOverlay.classList.remove('hidden');
        modalOverlay.classList.add('modal-show');
        modalContent.classList.add('modal-content-show');
        
        modalLoading.classList.remove('hidden');
        modalSuccess.classList.add('hidden');
    }

    function mostrarModalExito() {
        modalLoading.classList.add('hidden');
        modalSuccess.classList.remove('hidden');
    }

    function ocultarModal() {
        modalOverlay.classList.add('hidden');
        modalOverlay.classList.remove('modal-show');
        modalContent.classList.remove('modal-content-show');
    }

    function renderizarTablaResultados(resumen) {
        dropzone.classList.add('hidden');
        resultsPanel.classList.remove('hidden');

        document.getElementById('countSuccess').textContent = resumen.exitosos;
        document.getElementById('countErrors').textContent = resumen.errores;

        const errorContainer = document.getElementById('errorContainer');
        const errorList = document.getElementById('errorList');
        errorList.innerHTML = ''; 

        if (resumen.errores > 0) {
            errorContainer.classList.remove('hidden');
            resumen.detalles_errores.forEach(err => {
                const li = document.createElement('li');
                li.className = 'px-4 py-3 text-red-600 bg-red-50/50';
                li.textContent = err;
                errorList.appendChild(li);
            });
        }
    }
});