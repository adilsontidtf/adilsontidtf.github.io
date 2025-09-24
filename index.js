 let x = Number(prompt("Número de colunas:")); // colunas
        let y = Number(prompt("Número de linhas:"));  // linhas

        let jogo = [];
        let jogohtml = document.getElementById("Jogo");

        // Inicializa a matriz
        for (let i = 0; i < x; i++) {
            jogo[i] = [];
            for (let o = 0; o < y; o++) {
                jogo[i][o] = getRandomInt(); // 1 = bomba
            }
        }

        // Cria o HTML
        let aux = '';
        for (let i = 0; i < x; i++) {
            for (let o = 0; o < y; o++) {
                let id = `${i},${o}`;
                if (jogo[i][o] === 0) {
                    aux += `<button class="limpo" id="${id}" onclick="limpa('${id}', ${x}, ${y})">?</button>`;
                } else {
                    aux += `<button class="bomba" id="${id}" onclick="explode()">?</button>`;
                }
            }
            aux += "<div id='quebra'></div>";
        }
        jogohtml.innerHTML = aux;

        function explode() {
            alert("BOMMMMMMM!");
        }

        function limpa(xy, x, y) {
            let [compx, compy] = xy.split(',').map(Number);
            let botaoapertado = document.getElementById(xy);
            let bombas = 0;

            for (let i = -1; i <= 1; i++) {
                for (let o = -1; o <= 1; o++) {
                    let nx = compx + i;
                    let ny = compy + o;

                    if (nx >= 0 && nx < x && ny >= 0 && ny < y) {
                        if (jogo[nx][ny] === 1) {
                            bombas++;
                        }
                    }
                }
            }

            botaoapertado.innerHTML = bombas;
            botaoapertado.disabled = true; // desabilita botão após clique
        }

        function getRandomInt() {
            return Math.random() < 0.25 ? 1 : 0; // 25% de chance de bomba
        }