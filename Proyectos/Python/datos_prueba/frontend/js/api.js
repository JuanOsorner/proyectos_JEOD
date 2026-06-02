// El puerto al que nos vamos a conectar
const API_URL = "http://127.0.0.1:8000";

async function getBitcoinRegression() {

    const response = await fetch(
        `${API_URL}/regression/bitcoin`
    );

    if (!response.ok) {
        throw new Error(
            "Error obteniendo datos"
        );
    }

    return await response.json();
}