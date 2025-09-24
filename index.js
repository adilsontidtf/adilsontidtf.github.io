let x = prompt();
let y = prompt();
let aux = '';
let i = '';
let o = '';
let cont = 0;
let dados = [];
let jogo = [[], [], [], [], [], [], [], [], [], [],[], [], [], [], [], [], [], [], [], [],[], [], [], [], [], [], [], [], [],[],[], [], [], [], [], [], [], [], [], [],[], [], [], [], [], [], [], [], [], [],[], [], [], [], [], [], [], [], [],[],[], [], [], [], [], [], [], [], [], [],[], [], [], [], [], [], [], [], [], [],[], [], [], [], [], [], [], [], [],[],[], [], [], [], [], [], [], [], [],[],];
let jogohtml = document.getElementById("Jogo");
let bomba = document.querySelector("bomba");
let limpo = document.querySelector("limpo");

for (i = 0; i < x; i++) {
    for (o = 0; o < y; o++) {
        jogo[i][o] = getRandomInt();

        if (jogo[i][o] == 0) {
            dados[cont] = i + ',' + o;
            aux = aux + "<button class = limpo id = " + dados[cont] + " onclick = limpa(dados[" + cont +"],x,y)>?</button>";
            cont = cont + 1;
        }else{
            dados[cont] = i + ',' + o;
            aux = aux + "<button class = bomba id = " + dados[cont] + " onclick = explode()>?</button>";
            cont = cont + 1;
        }
    }
    aux = aux + "<div id=quebra></div>";
}
jogohtml.innerHTML = aux;





function explode() {
    alert("BOMMMMMMM!")
}
function limpa(xy,x,y) {
    let botaoapertado = document.getElementById(xy);
    let compx = '';
    let compy = '';
    let bombas = 0;
    let i = -1;
    let o = -1;
    let maxx = 2;
    let maxy = 2;
    let auxx = 0;
    let auxy = 0;

    let f = 0;
    let auxf = 0;
    let temp = 0;

    for(f = 0;f < 10;f++)
    {
        if(xy[f]==',')
        {
            auxf = f;
        }
    }
    for(f = 0;f < auxf;f++)
    {
        temp = xy[f];
        compx = compx + temp;
    }
    f = f+1;
    for(f;f < 10;f++)
    {
        if(xy[f]==undefined)
        {
            continue;
        }
        temp = xy[f];
        compy = compy + temp;
    }

    if (compx == 0) {
        maxx = 1;
    }
    if (compy == 0) {
        maxy = 1;
    }
    if(compx == x-1){
        auxx = 1;
    }
    if(compy == y-1){
        auxy = 1;
    }

    for (i = -1+auxx; i < maxx; i++) {
        for (o = -1+auxy; o < maxy; o++) {
            if (jogo[compx - i][compy - o] == 1) {
                bombas = bombas + 1;
            }
        }
    }

    botaoapertado.innerHTML = bombas;
}

function getRandomInt() {
    let x = Math.floor(Math.random() * (4 - 0) + 0);
    if (x == 0)
    {
        return 1;
    }
    return 0;
    
}