# -*- coding: utf-8 -*-
import json

logo = open("logo_b64.txt").read()

profissionais = ["Marcela", "Lene (Aurilene L.)", "Aurilene Gomes", "Emylli", "Jéssica", "Iris",
                 "JOJO (João Marcos)", "Lousanne", "Luciana (Lu)", "Ludmilla", "Lindinalva",
                 "Laine (Elaine C.)", "Maria Auxiliadora", "Yaponira"]

produtos_nf = [
    "FC Fibre Clinix — Fortify Booster 100ml", "FC Fibre Clinix — Hydrate Booster 100ml",
    "FC Fibre Clinix — Vibrancy Booster 100ml", "FC Fibre Clinix — Óleo Light 100ml",
    "FC Fibre Clinix — Óleo Cream-to-Oil 100ml", "FC Fibre Clinix — Concentrado Infusão 400ml",
    "FC Fibre Clinix — Nourishing Shampoo 1L", "FC Fibre Clinix — Purifying Shampoo 1L",
    "FC Fibre Clinix — Máscara Cabelos Espessos 500ml", "FC Fibre Clinix — Máscara Cabelos Finos 500ml",
    "FC Fibre Clinix — Fortify Shampoo 1L", "FC Fibre Clinix — Fortify Condicionador 1L",
    "FC Fibre Clinix — Vibrancy Shampoo 1L", "FC Fibre Clinix — Vibrancy Condicionador 1L",
    "FC Fibre Clinix — Hydrate Shampoo 1L", "FC Fibre Clinix — Hydrate Condicionador 1L",
    "BC Moisture Kick — Máscara 500ml", "BC Moisture Kick — Spray Condicionador 400ml",
    "BC Moisture Kick — Hyalu Serum 50ml",
]
# Produtos de uso diário que apareciam como "Outro produto" nas observações (05/09/2026).
# Nomes iguais aos do cadastro do AVEC, para o Claudinho lançar 1:1 na comanda.
# REGRA: toda vez que um produto novo aparecer em "Outro produto", incluir aqui e republicar
# (python gerar_app.py && git commit && git push) — a lista do app é o cadastro oficial da pesagem.
produtos_uso = ["Lipídica", "Shampoo Day by Day 3L", "Day by Day Condicionador 3L",
                "Máscara Infusion Oil 1000ml", "Ativador de Crespos e Crespíssimos Arvensis 1L",
                "Geleia Mirra 500ml", "Ox 10V Igora",
                "PÓ DESCOLORANTE BE BLONDE WHITE ERIK KENED", "OX 30V ERIK KENED 1000ML",
                "RECONSTRUCTION RESURRECTION 3 LABRIZZA", "RECONSTRUCTION SHAMPOO RESURRECTION 2 LABRIZZA",
                "18M REPAIR OLÉO ERIK KENED 60ML",
                "SHAMPOO ICE COOL CLEANING CONTROL LABRIZZA", "MASCARA RECOVERY INTENSIVE REPAIR LABRIZZA 500G",
                "SHAMPOO RECOVERY INTENSIVE REPAIR LABRIZZA", "MASCARA COLOR SUMMER LABRIZZA",
                "Metal Metalic Cleaning Balm", "Metal Metalic Cleaning Shampoo", "Metal Metalic Cleaning Mask"]
produtos_antigos = ["Coloração Igora (escrever a cor na observação)", "Coloração Keune (escrever a cor na observação)",
                    "Pó descolorante Erik Kened Blue", "Pó descolorante Keune Cream Blonde",
                    "Ox 20v Erik Kened", "Ox 20V Igora",
                    "Ox Keune 10 vol", "Ox Keune 20 vol", "Ox Keune 30 vol", "Ox Keune 40 vol",
                    "Linha Davines (especificar na observação)", "Linha Keune (especificar na observação)",
                    "Linha La Brizza (especificar na observação)", "Linha Erik Kened (especificar na observação)",
                    "Outro produto (escrever na observação)"]

opts_prof = "".join('<option value="{0}">{0}</option>'.format(p) for p in profissionais)
opts_nf = "".join('<option value="{0}">{0}</option>'.format(p) for p in produtos_nf)
opts_old = "".join('<option value="{0}">{0}</option>'.format(p) for p in produtos_antigos)
opts_uso = "".join('<option value="{0}">{0}</option>'.format(p) for p in produtos_uso)

seta = ("data:image/svg+xml;utf8,<svg xmlns=%22http://www.w3.org/2000/svg%22 width=%2214%22 height=%228%22>"
        "<path d=%22M1 1l6 6 6-6%22 stroke=%22%235c6650%22 stroke-width=%222%22 fill=%22none%22/></svg>")

html = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Pesagem Turali</title>
<link rel="manifest" href="manifest.json">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="theme-color" content="#66705a">
<meta name="apple-mobile-web-app-capable" content="yes">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Jost:wght@300;400;500&display=swap">
<style>
  * { box-sizing: border-box; margin: 0; }
  body { background: #f7f5ec; font-family: Jost, 'Segoe UI', sans-serif; color: #33402f; min-height: 100vh; display: flex; flex-direction: column; align-items: center; padding: 22px 18px 40px; }
  .moldura { width: 100%; max-width: 430px; }
  .topo { text-align: center; margin-bottom: 18px; }
  .topo img { width: 110px; }
  h1 { font-family: 'Cormorant Garamond', Georgia, serif; font-weight: 400; font-size: 30px; margin-top: 10px; }
  .sub { font-family: 'Cormorant Garamond', Georgia, serif; font-style: italic; color: #6d7460; font-size: 17px; margin-top: 2px; }
  label { display: block; font-size: 12px; letter-spacing: 2.5px; text-transform: uppercase; color: #6d7460; margin: 18px 0 7px; }
  select, input, textarea { width: 100%; padding: 15px 14px; font-size: 17px; font-family: Jost, sans-serif; color: #33402f; background: #fffdf6; border: 1px solid #cfc9b2; border-radius: 12px; appearance: none; -webkit-appearance: none; }
  select { background-image: url('__SETA__'); background-repeat: no-repeat; background-position: right 16px center; }
  select:focus, input:focus, textarea:focus { outline: 2px solid #8a927b; }
  .botao { width: 100%; margin-top: 26px; padding: 17px; font-size: 15px; letter-spacing: 3px; text-transform: uppercase; font-weight: 500; color: #f2efe2; background: #66705a; border: none; border-radius: 14px; cursor: pointer; }
  .botao:active { background: #55604a; }
  .ok { display: none; position: fixed; inset: 0; background: #66705a; color: #f2efe2; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 30px; z-index: 10; }
  .ok h2 { font-family: 'Cormorant Garamond', Georgia, serif; font-weight: 300; font-size: 44px; }
  .ok p { font-family: 'Cormorant Garamond', Georgia, serif; font-style: italic; font-size: 20px; margin-top: 10px; color: #e3dfc9; }
  .ok .botao { background: #f2efe2; color: #33402f; max-width: 300px; }
  .linha2 { display: flex; gap: 10px; }
  .linha2 > div { flex: 1; min-width: 0; }
  input[type=date] { min-height: 54px; }
  .rodape { margin-top: 30px; font-size: 11px; letter-spacing: 2px; text-transform: uppercase; color: #a8ad93; text-align: center; }
</style>
</head>
<body>
<div class="moldura">
  <div class="topo">
    <img src="data:image/png;base64,__LOGO__" alt="Turali">
    <h1>Pesagem de Insumos</h1>
    <div class="sub">pesou, registrou &mdash; 20 segundos</div>
  </div>
  <form id="f">
    <label>Profissional</label>
    <select id="prof" required><option value="" disabled selected>Quem usou?</option>__PROF__</select>
    <label>Produto</label>
    <select id="prod" required>
      <option value="" disabled selected>Qual produto?</option>
      <optgroup label="Uso di&aacute;rio (lavat&oacute;rio / bancada)">__USO__</optgroup>
      <optgroup label="Linha nova (Schwarzkopf)">__NF__</optgroup>
      <optgroup label="Outros insumos">__OLD__</optgroup>
    </select>
    <label>Quantidade usada (g ou ml)</label>
    <input id="qtd" type="number" inputmode="decimal" step="0.1" min="0.1" placeholder="ex.: 32,5" required>
    <div class="linha2">
      <div><label>N&ordm; da comanda</label>
      <input id="comanda" type="number" inputmode="numeric" min="1" placeholder="ex.: 8" required></div>
      <div><label>Data do servi&ccedil;o</label>
      <input id="data" type="date" required></div>
    </div>
    <label>Observa&ccedil;&atilde;o (opcional)</label>
    <textarea id="obs" rows="2" placeholder="nome da cliente (confer&ecirc;ncia) ou produto 'outro'"></textarea>
    <button class="botao" type="submit">Registrar &#127807;</button>
  </form>
  <div class="rodape">Turali &middot; uso interno</div>
</div>
<div class="ok" id="ok">
  <h2>Registrado!</h2>
  <p>obrigada por cuidar do nosso estoque &#127807;</p>
  <button class="botao" onclick="fechar()">Registrar outro</button>
</div>
<iframe name="alvo" style="display:none"></iframe>
<form id="envio" action="https://docs.google.com/forms/d/e/1FAIpQLSelsvMpZCgINQ8sRgww_8hZuCUuNwXBomRWLEjCs2SfNmpXKg/formResponse" method="POST" target="alvo" style="display:none">
  <input name="entry.877485345"><input name="entry.1356314490"><input name="entry.883777642"><input name="entry.1275865626">
</form>
<script>
  var f = document.getElementById('f');
  try { var ult = localStorage.getItem('prof'); if (ult) document.getElementById('prof').value = ult; } catch (e) {}
  (function(){ var h = new Date(), p = function(n){ return (n < 10 ? '0' : '') + n; };
     document.getElementById('data').value = h.getFullYear() + '-' + p(h.getMonth() + 1) + '-' + p(h.getDate()); })();
  f.addEventListener('submit', function (ev) {
    ev.preventDefault();
    var prof = document.getElementById('prof').value;
    var prod = document.getElementById('prod').value;
    var qtd = document.getElementById('qtd').value.replace('.', ',');
    // Comanda + data do servico sempre juntas (decisao da equipe 05/09/2026): a numeracao
    // do AVEC reinicia todo dia. Vai dentro da observacao num formato fixo que a rotina le.
    var nc = document.getElementById('comanda').value;
    var d = document.getElementById('data').value.split('-');   // aaaa-mm-dd
    var dataBr = d.length === 3 ? d[2] + '/' + d[1] + '/' + d[0] : '';
    var livre = document.getElementById('obs').value.trim();
    var obs = 'Comanda ' + nc + ' · ' + dataBr + (livre ? ' · ' + livre : '');
    var e = document.getElementById('envio');
    e.elements['entry.877485345'].value = prof;
    e.elements['entry.1356314490'].value = prod;
    e.elements['entry.883777642'].value = qtd;
    e.elements['entry.1275865626'].value = obs;
    e.submit();
    try { localStorage.setItem('prof', prof); } catch (er) {}
    document.getElementById('ok').style.display = 'flex';
  });
  function fechar() {
    document.getElementById('ok').style.display = 'none';
    document.getElementById('qtd').value = '';
    document.getElementById('obs').value = '';
  }
</script>
</body>
</html>"""

html = html.replace("__LOGO__", logo).replace("__PROF__", opts_prof).replace("__NF__", opts_nf)
html = html.replace("__OLD__", opts_old).replace("__USO__", opts_uso).replace("__SETA__", seta)
open("index.html", "w", encoding="utf-8").write(html)

manifest = {
    "name": "Pesagem Turali", "short_name": "Pesagem", "start_url": ".", "display": "standalone",
    "background_color": "#f7f5ec", "theme_color": "#66705a",
    "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
              {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"}],
}
json.dump(manifest, open("manifest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("index.html + manifest.json ok")
