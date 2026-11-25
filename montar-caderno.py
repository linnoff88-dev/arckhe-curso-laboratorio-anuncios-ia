from pathlib import Path
from html import escape as E
import json,zipfile
R=Path(__file__).resolve().parent
cases=[]
def C(slug,title,seconds,img,fixed,rows,voice,check):
 cases.append(dict(slug=slug,title=title,duration=seconds,image=img,fixed=fixed,rows=[dict(time=t,scene=s,image_prompt=ip,motion=mo,review=rv) for t,s,ip,mo,rv in rows],voice=voice,check=check))
C('lume','Lume êÂ· anêÂºncio narrado',18,2,'Lanterna cilêÂ­ndrica magenta, alêÂ§a preta e uma lente frontal. Pedra escura e ambiente azul. NêÂ£o representa desempenho real.',[
('0ê¢â¬â2','Produto na penumbra','Lanterna inteira sobre pedra escura; contorno magenta visêÂ­vel, espaêÂ§o para texto no editor.','CêÂ¢mera fixa; nêÂ©voa leve.','O produto pode ser reconhecido pelo contorno.'),
('2ê¢â¬â4','Feixe aparece','Mesma lanterna acesa; feixe suave na nêÂ©voa azul.','A nêÂ©voa se move sem alterar a lente.','Uma lente, uma alêÂ§a, forma preservada.'),
('4ê¢â¬â6','ApresentaêÂ§êÂ£o inteira','Mesma lanterna totalmente visêÂ­vel sobre a pedra.','AproximaêÂ§êÂ£o pequena e lenta.','Nenhuma parte desaparece.'),
('6ê¢â¬â8','Textura do corpo','Detalhe do corpo magenta, mesma proporêÂ§êÂ£o e material.','Luz varia suavemente; produto parado.','Textura nêÂ£o vira letras ou marca.'),
('8ê¢â¬â10','AlêÂ§a','Detalhe da alêÂ§a preta presa ao corpo, apoio natural.','CêÂ¢mera estêÂ¡vel.','AlêÂ§a continua presa e nêÂ£o se multiplica.'),
('10ê¢â¬â12','Escala no ambiente','Produto inteiro na mesma pedra, mais espaêÂ§o azul ao redor.','NêÂ©voa passa ao fundo.','A escala nêÂ£o muda durante o clipe.'),
('12ê¢â¬â14','Luz e matêÂ©ria','Lente e corpo visêÂ­veis, brilho controlado.','Pequena mudanêÂ§a de luz.','Brilho nêÂ£o apaga a forma do produto.'),
('14ê¢â¬â16','Retorno ao conjunto','Mesma composiêÂ§êÂ£o principal com produto inteiro.','Movimento reduz atêÂ© parar.','AlêÂ§a, lente e corpo mantidos.'),
('16ê¢â¬â18','Encerramento','Produto inteiro, fundo limpo para frase adicionada no editor.','CêÂ¢mera fixa.','Nome e identificaêÂ§êÂ£o cabem sem cobrir o objeto.')],
'Quando tudo parece igual, uma pausa muda o olhar. Lume: imagine outro caminho. Grave em ritmo natural, ouêÂ§a e distribua a frase pelos 18 segundos. NêÂ£o corte palavras para caber.',
'Nove cenas, 18 segundos, produto coerente e voz compreensêÂ­vel. IdentificaêÂ§êÂ£o: conceito fictêÂ­cio com IA.')
C('vento','Vento êÂ· sequêÂªncia musical',20,5,'Pessoa adulta de roupa coral, corredor de vidro verde, mesma luz e direêÂ§êÂ£o. Quatro clipes editados; nêÂ£o êÂ© tomada real êÂºnica.',[
('0ê¢â¬â5','ComeêÂ§ar','Pessoa inteira no comeêÂ§o do corredor, braêÂ§os relaxados.','ComeêÂ§a a caminhar devagar; cêÂ¢mera acompanha.','Corpo, roupa e pilares estêÂ¡veis.'),
('5ê¢â¬â10','AvanêÂ§ar','Use o êÂºltimo quadro limpo anterior; mesma pessoa alguns passos adiante.','Continua na mesma direêÂ§êÂ£o.','PosiêÂ§êÂ£o e escala encaixam na passagem.'),
('10ê¢â¬â15','Faixa de luz','Mesma pessoa atravessa uma faixa de sol no piso.','Caminhada pequena, sem giro.','Luz pertence ao espaêÂ§o, nêÂ£o muda a roupa.'),
('15ê¢â¬â20','Parar','Mesmo corredor; pessoa encerra o passo.','Movimento desacelera atêÂ© parar.','PêÂ©s nêÂ£o deslizam e mêÂºsica termina de forma deliberada.')],
'Instrumental do kit ao longo dos 20 segundos. OuêÂ§a antes de decidir as emendas. Os intervalos sêÂ£o uma estrutura de estudo, nêÂ£o uma anêÂ¡lise de batidas da faixa.',
'Quatro trechos, trêÂªs emendas conferidas, som contêÂ­nuo e crêÂ©ditos preservados. IdentificaêÂ§êÂ£o: estudo fictêÂ­cio com IA.')
C('senda','Senda êÂ· produto com cinco planos',15,8,'ArmaêÂ§êÂ£o êÂ¢mbar translêÂºcida, duas lentes escuras, ponte e duas hastes. Papel creme. Sem alegaêÂ§êÂµes de proteêÂ§êÂ£o ou saêÂºde.',[
('0ê¢â¬â3','Inteiro','êâculos inteiros sobre papel creme, margem para as hastes.','AproximaêÂ§êÂ£o lenta.','Conjunto reconhecêÂ­vel.'),
('3ê¢â¬â6','Papel','Mesma armaêÂ§êÂ£o, dobra de papel em primeiro plano.','Dobra se move suavemente.','Papel nêÂ£o transforma o produto.'),
('6ê¢â¬â9','Material','Detalhe da armaêÂ§êÂ£o êÂ¢mbar e da dobradiêÂ§a.','CêÂ¢mera quase parada.','Material e junêÂ§êÂµes coerentes.'),
('9ê¢â¬â12','êângulo','Mesma referêÂªncia, êÂ¢ngulo levemente diferente.','Movimento mêÂ­nimo, sem giro completo.','Duas hastes sem atravessar lentes.'),
('12ê¢â¬â15','Encerramento','Produto inteiro com fundo limpo.','CêÂ¢mera fixa.','Frase Senda: observe os detalhes legêÂ­vel.')],
'MêÂºsica autorizada opcional. A peêÂ§a funciona sem voz. Se usar o trecho do kit, recorte conscientemente para 15 segundos e preserve o crêÂ©dito.',
'Cinco cenas, 15 segundos, construêÂ§êÂ£o coerente e frase legêÂ­vel. IdentificaêÂ§êÂ£o: conceito fictêÂ­cio com IA.')
C('pulso','Pulso êÂ· anêÂºncio esportivo reduzido',12,11,'TêÂªnis coral, sola creme, cadarêÂ§os corais; roupa azul marinho e pista azul. NêÂ£o promete desempenho nem saêÂºde.',[
('0ê¢â¬â4','Produto','TêÂªnis lateral apoiado na pista azul.','CêÂ¢mera fixa ou aproximaêÂ§êÂ£o pequena.','Contato com a pista e solado coerentes.'),
('4ê¢â¬â8','PreparaêÂ§êÂ£o','Pessoa adulta parada em pêÂ©, braêÂ§os soltos, roupa azul marinho, calêÂ§ando a referêÂªncia.','Pequena mudanêÂ§a de peso.','Duas pernas, dois pêÂ©s, equilêÂ­brio.'),
('8ê¢â¬â12','Um passo','Mesma pessoa e direêÂ§êÂ£o, espaêÂ§o para avanêÂ§ar um pêÂ©.','Um passo curto e apoio na pista.','PêÂ© nêÂ£o atravessa chêÂ£o; corpo nêÂ£o se multiplica.')],
'TrêÂªs batidas leves gravadas por vocêÂª podem marcar a ediêÂ§êÂ£o. SêÂ£o um recurso de ritmo, nêÂ£o um registro cardêÂ­aco. Alternativa: primeiro montar em silêÂªncio.',
'TrêÂªs cenas, 12 segundos, apoio e anatomia conferidos. IdentificaêÂ§êÂ£o: conceito fictêÂ­cio com IA.')
C('arquivo','Arquivo do Vento êÂ· primeira pessoa',16,14,'Quatro referêÂªncias: sala terracota, instrumento astronêÂ´mico de latêÂ£o, luvas cinza e luz do teto circular. NêÂ£o representa local existente.',[
('0ê¢â¬â4','Entrada','VisêÂ£o da entrada para a mesa; luz da abertura circular.','AvanêÂ§o lento.','Mesa e teto correspondem ao mapa.'),
('4ê¢â¬â8','AproximaêÂ§êÂ£o','Mesma sala, mesa mais prêÂ³xima; objeto permanece no centro da aêÂ§êÂ£o.','AvanêÂ§o pequeno, sem atravessar mesa.','AproximaêÂ§êÂ£o coerente com a escala.'),
('8ê¢â¬â12','ObservaêÂ§êÂ£o','Instrumento de latêÂ£o prêÂ³ximo; luvas na base do quadro.','MêÂ£os estêÂ¡veis; leve ajuste do olhar.','MêÂ£os e objeto sem deformaêÂ§êÂ£o.'),
('12ê¢â¬â16','Encerramento','Mesmo ponto de vista, instrumento e sala reconhecêÂ­veis.','Movimento termina com calma.','Portas, teto e mesa permanecem no lugar.')],
'Som ambiente prêÂ³prio ou autorizado, discreto. Pode comeêÂ§ar em silêÂªncio para conferir o espaêÂ§o. MêÂºsica e susto nêÂ£o sêÂ£o obrigatêÂ³rios.',
'Quatro cenas, 16 segundos, trêÂªs passagens espaciais conferidas. IdentificaêÂ§êÂ£o: universo fictêÂ­cio com IA.')
C('dobra','Dobra êÂ· demonstraêÂ§êÂ£o em sete cenas',21,17,'Jo: pele morena, cabelo preto curto, blusa creme. Bolsa retangular de lona oliva com duas alêÂ§as creme. Personagem e produto fictêÂ­cios.',[
('0ê¢â¬â3','ApresentaêÂ§êÂ£o','Jo de meio corpo segurando a bolsa inteira.','Fala curta, gestos mêÂ­nimos.','Veja o formato. Boca e voz conferidas, ou narraêÂ§êÂ£o identificada.'),
('3ê¢â¬â6','Inteiro','Bolsa inteira, mesma referêÂªncia.','CêÂ¢mera fixa.','A bolsa por inteiro. Forma retangular preservada.'),
('6ê¢â¬â9','AlêÂ§as','Detalhe das alêÂ§as creme presas ao corpo da bolsa.','MêÂ£o segura sem torcer.','Observe as alêÂ§as. MêÂ£o e tecido nêÂ£o se fundem.'),
('9ê¢â¬â12','Tecido','Detalhe da lona oliva.','AproximaêÂ§êÂ£o pequena.','Detalhe do tecido. Textura nêÂ£o muda de material.'),
('12ê¢â¬â15','Abertura','Bolsa aberta, sem alegaêÂ§êÂ£o de capacidade ou objetos surgindo.','Movimento mêÂ­nimo.','Veja a abertura. Bordas e alêÂ§as coerentes.'),
('15ê¢â¬â18','Conjunto','Jo e bolsa inteiras no enquadramento de meio corpo.','Pose simples.','Compare o conjunto. Rosto, roupa e produto preservados.'),
('18ê¢â¬â21','Encerramento','Produto visêÂ­vel e espaêÂ§o para identificaêÂ§êÂ£o.','CêÂ¢mera fixa.','ConheêÂ§a o conceito Dobra. Frase inteira e legêÂ­vel.')],
'Use as sete frases curtas indicadas, com pausas. Voz prêÂ³pria ou sintêÂ©tica permitida. NarraêÂ§êÂ£o sobre detalhes reduz a necessidade de sincronizaêÂ§êÂ£o. NêÂ£o invente experiêÂªncia de compra.',
'Sete cenas, 21 segundos, fala, personagem e bolsa coerentes. IdentificaêÂ§êÂ£o visêÂ­vel: DemonstraêÂ§êÂ£o fictêÂ­cia com IA.')
(R/'context/casos.json').write_text(json.dumps(cases,ensure_ascii=False,indent=2)+'\n')
head='''<!doctype html><html lang="pt-BR" data-theme="papel"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Caderno de produêÂ§êÂ£o êÂ· LaboratêÂ³rio de AnêÂºncios</title><link rel="stylesheet" href="assets/aula.css"><style>main{padding-top:28px;padding-bottom:50px}h1{font-family:var(--serif);font-size:clamp(36px,7vw,58px);line-height:1.1}h2{font-family:var(--serif);font-size:32px}section{padding:24px 0;scroll-margin-top:24px}article{padding:20px;border:1px solid var(--line);border-radius:12px;margin:16px 0;background:var(--panel)}article h3{font-size:22px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:inherit;background:var(--panel);padding:18px;border:1px solid var(--line)}img{max-width:100%;height:auto;border-radius:12px}audio{width:100%}.small{font-size:16px}a{overflow-wrap:anywhere}</style></head><body><main class="wrap">'''
intro='''<p><a href="curso.html#trilha">ê¢â Â voltar ao curso</a> êÂ· <a href="galeria.html">referêÂªncias didêÂ¡ticas</a></p><h1>Caderno de <em>produêÂ§êÂ£o</em></h1><p>Seis casos originais para estudar roteiro, continuidade e montagem. As imagens sêÂ£o referêÂªncias didêÂ¡ticas criadas no Codex. NêÂ£o hêÂ¡ seis campanhas renderizadas neste kit. Os exercêÂ­cios pedem que vocêÂª produza e confira seus prêÂ³prios arquivos.</p><p><a href="assets/kit-laboratorio.zip" download>Salvar roteiros, referêÂªncias e faixa de estudo</a> êÂ· <a href="assets/roteiros.txt" download>Salvar roteiros em texto</a></p><p>Formato dos seis estudos: vertical 9:16, exportaêÂ§êÂ£o MP4 em 1080 por 1920 quando seus arquivos permitirem. NêÂ£o amplie material ruim esperando recuperar detalhe. No editor, confira enquadramento e leitura. As referêÂªncias do curso sêÂ£o horizontais para leitura; gere suas prêÂ³prias referêÂªncias no formato planejado.</p><p>Acrescente identificaêÂ§êÂ£o legêÂ­vel de conceito ou demonstraêÂ§êÂ£o fictêÂ­cia com IA. Confira custos e recursos na conta antes de gerar. Para a produêÂ§êÂ£o completa, reserve 28ê¢â¬â40 horas, alêÂ©m de filas. A prêÂ¡tica de dez minutos êÂ© um recorte da etapa, frequentemente a revisêÂ£o de arquivos jêÂ¡ produzidos.</p>'''
nav='<nav aria-label="Casos">'+' êÂ· '.join(f'<a href="#{c["slug"]}">{E(c["title"].split(" êÂ· ")[0])}</a>' for c in cases)+'</nav>'
parts=[];txt=['LABORATêâRIO DE ANêÅ¡NCIOS ê¢â¬â ROTEIROS AUTORAIS','Casos fictêÂ­cios, sem campanhas reais ou resultados alegados.','Formato vertical 9:16. Identifique a ficêÂ§êÂ£o com IA na peêÂ§a.']
for c in cases:
 rows=''.join(f'<article><h3>{i}. {E(x["scene"])} êÂ· {x["time"]} s</h3><p><b>Imagem:</b> {E(x["image_prompt"])}</p><p><b>Movimento:</b> {E(x["motion"])}</p><p><b>ConferêÂªncia:</b> {E(x["review"])}</p></article>' for i,x in enumerate(c['rows'],1))
 parts.append(f'<section id="{c["slug"]}"><h2>{E(c["title"])}</h2><p><b>Ficha fixa:</b> {E(c["fixed"])}</p><img src="assets/img/aula-{c["image"]}.webp" width="1280" height="720" alt="ReferêÂªncia ilustrativa do caso {E(c["title"])}"><p class="small">Imagem didêÂ¡tica do Codex; nêÂ£o êÂ© quadro extraêÂ­do de campanha produzida.</p>{rows}<p><b>Som:</b> {E(c["voice"])}</p><p><b>Pronto:</b> {E(c["check"])}</p></section>')
 txt+=['\n'+c['title'],c['fixed']]+[f'{i}. {x["time"]}s ê¢â¬â {x["scene"]}\nImagem: {x["image_prompt"]}\nMovimento: {x["motion"]}\nConferêÂªncia: {x["review"]}' for i,x in enumerate(c['rows'],1)]+['Som: '+c['voice'],'Pronto: '+c['check']]
credit='Carefree ê¢â¬â Kevin MacLeod (incompetech.com). LicenêÂ§a CC BY 4.0: https://creativecommons.org/licenses/by/4.0/. Trecho inicial de 20 segundos, convertido para MP3. Fonte: https://incompetech.com/music/royalty-free/index.html?gt=&isrc=USUAN1400037. Obtido pelo ARCKHêVOX em 25/09/2026. Se alterar volume, duraêÂ§êÂ£o ou aplicar fades, acrescente essa informaêÂ§êÂ£o ao crêÂ©dito.'
process='''CASO:
CENA:
ARQUIVO E TENTATIVA:
REFERêÅ NCIA USADA:
PEDIDO:
SITUAêâ¡êÆO: aprovado / corrigir / pendente
TEMPO DO PROBLEMA:
O QUE OBSERVEI:
ALTERAêâ¡êÆO A TESTAR:
TRABALHO ATIVO: medido / estimado / nêÂ£o medido
ESPERA DE PROCESSAMENTO:
TENTATIVAS E CONSUMO CONHECIDO:
LIMITE E ALTERNATIVA:
'''
final='''CASO ESCOLHIDO:
PêÅ¡BLICO:
MENSAGEM:
FORMATO:
DURAêâ¡êÆO E CENAS:
ARQUIVOS ESPERADOS:
CRITêâ°RIOS: sequêÂªncia / identidade / som / leitura / identificaêÂ§êÂ£o
VERSêÆO ANTERIOR:
VERSêÆO REVISADA:
MUDANêâ¡A E EFEITO OBSERVADO:
DECISêÆO:
êÂNDICE DOS SEIS ESTUDOS:
Lume ê¢â¬â 18s ê¢â¬â arquivo e situaêÂ§êÂ£o:
Vento ê¢â¬â 20s ê¢â¬â arquivo e situaêÂ§êÂ£o:
Senda ê¢â¬â 15s ê¢â¬â arquivo e situaêÂ§êÂ£o:
Pulso ê¢â¬â 12s ê¢â¬â arquivo e situaêÂ§êÂ£o:
Arquivo do Vento ê¢â¬â 16s ê¢â¬â arquivo e situaêÂ§êÂ£o:
Dobra ê¢â¬â 21s ê¢â¬â arquivo e situaêÂ§êÂ£o:
ACABAMENTO FINAL ê¢â¬â arquivo e situaêÂ§êÂ£o:
FONTES E CRêâ°DITOS:
PENDêÅ NCIAS REAIS:
'''
end=f'''<section id="musica"><h2>Faixa de estudo êÂ· 20 segundos</h2><audio controls preload="metadata" src="assets/audio/carefree-20s.mp3"></audio><p><a href="assets/audio/carefree-20s.mp3" download>Salvar a faixa</a></p><pre>{E(credit)}</pre><p><a href="https://incompetech.com/music/royalty-free/index.html?gt=&amp;isrc=USUAN1400037">Fonte da mêÂºsica</a> êÂ· <a href="https://creativecommons.org/licenses/by/4.0/">LicenêÂ§a CC BY 4.0</a></p></section><section id="processo"><h2>Ficha de processo</h2><pre>{E(process)}</pre></section><section id="final"><h2>Ficha de acabamento e êÂ­ndice</h2><pre>{E(final)}</pre></section><p><a href="curso.html#trilha">Voltar êÂ  trilha</a></p></main></body></html>'''
(R/'caderno.html').write_text(head+intro+nav+''.join(parts)+end)
(R/'assets/roteiros.txt').write_text('\n\n'.join(txt)+'\n\n'+process+'\n'+final+'\n\nCRêâ°DITO\n'+credit+'\n')
(R/'assets/CREDITOS.txt').write_text(credit+'\n\nImagens: ilustraêÂ§êÂµes originais geradas pelo recurso nativo do Codex. NêÂ£o representam pessoas, produtos, locais ou campanhas reais. Diagramas e textos: autoria ARCKHê AI.\n')
with zipfile.ZipFile(R/'assets/kit-laboratorio.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in ['assets/roteiros.txt','assets/CREDITOS.txt','assets/audio/carefree-20s.mp3']:z.write(R/f,f.removeprefix('assets/'))
 for c in cases:z.write(R/f'assets/img/aula-{c["image"]}.webp','referencias/'+c['slug']+'.webp')
# Full named sequence is shown in the lesson's second teaching visual.
extra={}
for i,c in enumerate(cases):
 rows=''.join(f'<div class="item doc"><span class="pin">{j}</span><div><b>{E(x["scene"])} êÂ· {x["time"]} s</b><br>{E(x["review"])}</div></div>' for j,x in enumerate(c['rows'],1))
 extra[str(i*3+1)]=f'<figure class="largo"><div class="janela"><div class="tela-top">Roteiro preenchido êÂ· {E(c["title"])}</div><div class="janela-body">{rows}</div></div><figcaption>Plano autoral de {c["duration"]} segundos. O caderno detalha imagem, movimento e som de cada cena.</figcaption></figure>'
(R/'context/visuais-extras.json').write_text(json.dumps(extra,ensure_ascii=False,indent=2)+'\n')
# Gallery distinguishes didactic images from unproduced video.
gallery=head.replace('Caderno de produêÂ§êÂ£o','Galeria didêÂ¡tica')+'<p><a href="curso.html#trilha">ê¢â Â curso</a> êÂ· <a href="caderno.html">caderno</a></p><h1>ReferêÂªncias <em>didêÂ¡ticas</em></h1><p>Imagens criadas no Codex para ensinar escolhas. NêÂ£o sêÂ£o quadros extraêÂ­dos de seis anêÂºncios produzidos. As atividades de geraêÂ§êÂ£o exigem seus prêÂ³prios arquivos. Os pares 2/3, 5/6, 8/9, 14/15 e 17/18 usam referêÂªncia anterior, mas ainda exigem comparaêÂ§êÂ£o.</p>'
ls=json.loads((R/'context/aulas-editoriais.json').read_text())
for n,d in enumerate(ls,1):gallery+=f'<section id="imagem-{n}"><h2>{n}. {E(d["titulo"])}</h2><img src="assets/img/aula-{n}.webp" width="1280" height="720" loading="lazy" alt="{E(d["observacao"])}"><p>{E(d["observacao"])}</p><p><a href="assets/img/aula-{n}.webp" download>Salvar referêÂªncia didêÂ¡tica</a> êÂ· <a href="curso.html#aula-{n}">Abrir aula</a></p></section>'
(R/'galeria.html').write_text(gallery+'</main></body></html>')
