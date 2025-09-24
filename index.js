let colunas = Number(prompt("Número de colunas:")); // x
let linhas = Number(prompt("Número de linhas:"));  // y

let jogo = []; // jogo[linha][coluna]
let jogohtml = document.getElementById("Jogo");
let primeiroClique = true;

// Inicializa matriz vazia
for (let l = 0; l < linhas; l++) {
    jogo[l] = [];
    for (let c = 0; c < colunas; c++) {
        jogo[l][c] = 0; // Preencheremos com bombas depois do 1º clique
    }
}

// Cria o HTML
let aux = '';
for (let l = 0; l < linhas; l++) {
    aux += `<div class="linha">`;
    for (let c = 0; c < colunas; c++) {
        aux += `<button class="limpo" data-l="${l}" data-c="${c}" onclick="limpa(this)" oncontextmenu="toggleBandeira(event)">?</button>`;
    }
    aux += `</div>`;
}
jogohtml.innerHTML = aux;

// Gera bombas aleatórias, exceto na posição inicial e vizinhos
function gerarBombas(evitarL, evitarC) {
    for (let l = 0; l < linhas; l++) {
        for (let c = 0; c < colunas; c++) {
            if (Math.random() < 0.25 && !estaPerto(l, c, evitarL, evitarC)) {
                jogo[l][c] = 1; // bomba
            }
        }
    }
}

function estaPerto(l1, c1, l2, c2) {
    return Math.abs(l1 - l2) <= 1 && Math.abs(c1 - c2) <= 1;
}

function limpa(botao) {
    let l = Number(botao.dataset.l);
    let c = Number(botao.dataset.c);

    // Gera bombas no primeiro clique
    if (primeiroClique) {
        gerarBombas(l, c);
        primeiroClique = false;
    }

    revelarCelula(l, c);
}

function contarBombasVizinhas(l, c) {
    let bombas = 0;
    for (let dl = -1; dl <= 1; dl++) {
        for (let dc = -1; dc <= 1; dc++) {
            let nl = l + dl;
            let nc = c + dc;
            if (
                nl >= 0 && nl < linhas &&
                nc >= 0 && nc < colunas &&
                jogo[nl][nc] === 1
            ) {
                bombas++;
            }
        }
    }
    return bombas;
}

function explode() {
    alert("BOMMMMMMM!");

    // Mostra todas as bombas
    let botoes = document.querySelectorAll("button");
    botoes.forEach(botao => {
        let l = Number(botao.dataset.l);
        let c = Number(botao.dataset.c);
        if (jogo[l][c] === 1) {
            botao.innerHTML = "💣";
            botao.classList.add("bomba");
        }
        botao.disabled = true;
    });
}

function revelarCelula(l, c) {
    // Verifica limites
    if (l < 0 || l >= linhas || c < 0 || c >= colunas) return;

    let botao = document.querySelector(`button[data-l='${l}'][data-c='${c}']`);

    if (!botao || botao.disabled) return;

    if (jogo[l][c] === 1) {
        explode();
        return;
    }

    let bombas = contarBombasVizinhas(l, c);
    botao.innerHTML = bombas === 0 ? "" : bombas;
    botao.disabled = true;
    botao.classList.add("limpo");

    // Se não há bombas ao redor, limpa vizinhos automaticamente
    if (bombas === 0) {
        for (let dl = -1; dl <= 1; dl++) {
            for (let dc = -1; dc <= 1; dc++) {
                let nl = l + dl;
                let nc = c + dc;
                if (nl === l && nc === c) continue; // pula ele mesmo
                revelarCelula(nl, nc);
            }
        }
    }
}

function toggleBandeira(event) {
    event.preventDefault(); // impede o menu padrão do clique direito

    const botao = event.target;

    // Ignora se o botão já foi revelado
    if (botao.disabled) return;

    if (botao.innerHTML === "🚩") {
        botao.innerHTML = "?";
    } else {
        botao.innerHTML = "🚩";
    }
}