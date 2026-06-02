let sectionsAlreadyVisible = false;

const button = document.getElementById("load-data-btn");
const trendMessage = document.getElementById("trend-message");
const tableBody = document.getElementById("data-table-body");
const metricsContainer = document.getElementById("metrics-container");

button.addEventListener("click", async () => {
    try {
        button.disabled = true;
        button.textContent = "Cargando datos...";

        // 1. Esperamos la resolución de la API de Bitcoin
        const data = await getBitcoinRegression();

        // 2. Transición del Hero: Se encoge elegantemente reduciendo su min-height
        document.getElementById("hero").classList.add("hero-loaded");

        // 3. Renderizamos e inyectamos los datos inmediatamente en el DOM oculto.
        // Esto permite que el navegador calcule el tamaño real de los contenedores.
        updateTrendMessage(data);
        updateMetrics(data);
        populateTable(data);
        renderChart(data);

        // 4. Esperamos ligeramente a que la animación de encogimiento del Hero comience
        // para lanzar el reveal secuencial de las tarjetas.
        setTimeout(() => {
            revealSections();
            // Habilitamos el scroll global una vez que los elementos empiezan a desplegarse
            document.body.style.overflow = "auto";
        }, 400); 

        button.textContent = "Actualizar Datos";
        button.disabled = false;

    } catch (error) {
        console.error(error);
        trendMessage.innerHTML = "Error obteniendo datos.";
        button.disabled = false;
        button.textContent = "Cargar Datos";
    }
});

function updateTrendMessage(data) {
    const slope = data.slope;
    if (slope > 0) {
        trendMessage.innerHTML = `
            <h3>📈 Tendencia Positiva</h3>
            <p>El modelo encontró una tendencia creciente en los últimos días.</p>
            <p>Pendiente: ${slope.toFixed(2)}</p>
        `;
    } else if (slope < 0) {
        trendMessage.innerHTML = `
            <h3>📉 Tendencia Negativa</h3>
            <p>El modelo encontró una tendencia decreciente en los últimos días.</p>
            <p>Pendiente: ${slope.toFixed(2)}</p>
        `;
    } else {
        trendMessage.innerHTML = `
            <h3>➡ Tendencia Estable</h3>
            <p>No se detecta una tendencia clara.</p>
        `;
    }
}

function populateTable(data) {
    tableBody.innerHTML = "";
    for (let i = 0; i < data.x.length; i++) {
        const row = document.createElement("tr");
        row.innerHTML = `
            <td>${data.x[i]}</td>
            <td>$${Number(data.y[i]).toFixed(2)}</td>
        `;
        tableBody.appendChild(row);
    }
}

function updateMetrics(data) {
    const prices = data.y;
    const min = Math.min(...prices);
    const max = Math.max(...prices);
    const average = prices.reduce((acc, value) => acc + value, 0) / prices.length;

    metricsContainer.innerHTML = `
        <div class="metric-card">
            <h3>Muestras</h3>
            <p>${data.data_points}</p>
        </div>
        <div class="metric-card">
            <h3>Pendiente</h3>
            <p>${data.slope.toFixed(2)}</p>
        </div>
        <div class="metric-card">
            <h3>Intercepto</h3>
            <p>${data.intercept.toFixed(2)}</p>
        </div>
        <div class="metric-card">
            <h3>Precio mínimo</h3>
            <p>$${min.toFixed(2)}</p>
        </div>
        <div class="metric-card">
            <h3>Precio máximo</h3>
            <p>$${max.toFixed(2)}</p>
        </div>
        <div class="metric-card);
            <h3>Precio promedio</h3>
            <p>$${average.toFixed(2)}</p>
        </div>
    `;
}

function revealSections() {
    if (sectionsAlreadyVisible) return;
    sectionsAlreadyVisible = true;

    const sections = [
        document.getElementById("summary"),
        document.getElementById("metrics-section"),
        document.getElementById("chart-section"),
        document.getElementById("table-section")
    ];

    sections.forEach((section, index) => {
        setTimeout(() => {
            section.classList.remove("hidden-section");
            section.classList.add("visible-section");
        }, index * 150); // Reducido a 150ms para un escalonado más dinámico y profesional
    });
}