from pathlib import Path
from html import escape as E
import json,zipfile
R=Path(__file__).resolve().parent
cases=[]
def C(slug,title,seconds,img,fixed,rows,voice,check):
 cases.append(dict(slug=slug,title=title,duration=seconds,image=img,fixed=fixed,rows=[dict(time=t,scene=s,image_prompt=ip,motion=mo,review=rv) for t,s,ip,mo,rv in rows],voice=voice,check=check))
C('lume','Lume Â· anÃºncio narrado',18,2,'Lanterna cilÃ­ndrica magenta, alÃ§a preta e uma lente frontal. Pedra escura e ambiente azul. NÃ£o representa desempenho real.',[
('0â€“2','Produto na penumbra','Lanterna inteira sobre pedra escura; contorno magenta visÃ­vel, espaÃ§o para texto no editor.','CÃ¢mera fixa; nÃ©voa leve.','O produto pode ser reconhecido pelo contorno.'),
('2â€“4','Feixe aparece','Mesma lanterna acesa; feixe suave na nÃ©voa azul.','A nÃ©voa se move sem alterar a lente.','Uma lente, uma alÃ§a, forma preservada.'),
('4â€“6','ApresentaÃ§Ã£o inteira','Mesma lanterna totalmente visÃ­vel sobre a pedra.','AproximaÃ§Ã£o pequena e lenta.','Nenhuma parte desaparece.'),
('6â€“8','Textura do corpo','Detalhe do corpo magenta, mesma proporÃ§Ã£o e material.','Luz varia suavemente; produto parado.','Textura nÃ£o vira letras ou marca.'),
('8â€“10','AlÃ§a','Detalhe da alÃ§a preta presa ao corpo, apoio natural.','CÃ¢mera estÃ¡vel.','AlÃ§a continua presa e nÃ£o se multiplica.'),
('10â€“12','Escala no ambiente','Produto inteiro na mesma pedra, mais espaÃ§o azul ao redor.','NÃ©voa passa ao fundo.','A escala nÃ£o muda durante o clipe.'),
('12â€“14','Luz e matÃ©ria','Lente e corpo visÃ­veis, brilho controlado.','Pequena mudanÃ§a de luz.','Brilho nÃ£o apaga a forma do produto.'),
('14â€“16','Retorno ao conjunto','Mesma composiÃ§Ã£o principal com produto inteiro.','Movimento reduz atÃ© parar.','AlÃ§a, lente e corpo mantidos.'),
('16â€“18','Encerramento','Produto inteiro, fundo limpo para frase adicionada no editor.','CÃ¢mera fixa.','Nome e identificaÃ§Ã£o cabem sem cobrir o objeto.')],
'Quando tudo parece igual, uma pausa muda o olhar. Lume: imagine outro caminho. Grave em ritmo natural, ouÃ§a e distribua a frase pelos 18 segundos. NÃ£o corte palavras para caber.',
'Nove cenas, 18 segundos, produto coerente e voz compreensÃ­vel. IdentificaÃ§Ã£o: conceito fictÃ­cio com IA.')
C('vento','Vento Â· sequÃªncia musical',20,5,'Pessoa adulta de roupa coral, corredor de vidro verde, mesma luz e direÃ§Ã£o. Quatro clipes editados; nÃ£o Ã© tomada real Ãºnica.',[
('0â€“5','ComeÃ§ar','Pessoa inteira no comeÃ§o do corredor, braÃ§os relaxados.','ComeÃ§a a caminhar devagar; cÃ¢mera acompanha.','Corpo, roupa e pilares estÃ¡veis.'),
('5â€“10','AvanÃ§ar','Use o Ãºltimo quadro limpo anterior; mesma pessoa alguns passos adiante.','Continua na mesma direÃ§Ã£o.','PosiÃ§Ã£o e escala encaixam na passagem.'),
('10â€“15','Faixa de luz','Mesma pessoa atravessa uma faixa de sol no piso.','Caminhada pequena, sem giro.','Luz pertence ao espaÃ§o, nÃ£o muda a roupa.'),
('15â€“20','Parar','Mesmo corredor; pessoa encerra o passo.','Movimento desacelera atÃ© parar.','PÃ©s nÃ£o deslizam e mÃºsica termina de forma deliberada.')],
'Instrumental do kit ao longo dos 20 segundos. OuÃ§a antes de decidir as emendas. Os intervalos sÃ£o uma estrutura de estudo, nÃ£o uma anÃ¡lise de batidas da faixa.',
'Quatro trechos, trÃªs emendas conferidas, som contÃ­nuo e crÃ©ditos preservados. IdentificaÃ§Ã£o: estudo fictÃ­cio com IA.')
C('senda','Senda Â· produto com cinco planos',15,8,'ArmaÃ§Ã£o Ã¢mbar translÃºcida, duas lentes escuras, ponte e duas hastes. Papel creme. Sem alegaÃ§Ãµes de proteÃ§Ã£o ou saÃºde.',[
('0â€“3','Inteiro','Ã“culos inteiros sobre papel creme, margem para as hastes.','AproximaÃ§Ã£o lenta.','Conjunto reconhecÃ­vel.'),
('3â€“6','Papel','Mesma armaÃ§Ã£o, dobra de papel em primeiro plano.','Dobra se move suavemente.','Papel nÃ£o transforma o produto.'),
('6â€“9','Material','Detalhe da armaÃ§Ã£o Ã¢mbar e da dobradiÃ§a.','CÃ¢mera quase parada.','Material e junÃ§Ãµes coerentes.'),
('9â€“12','Ã‚ngulo','Mesma referÃªncia, Ã¢ngulo levemente diferente.','Movimento mÃ­nimo, sem giro completo.','Duas hastes sem atravessar lentes.'),
('12â€“15','Encerramento','Produto inteiro com fundo limpo.','CÃ¢mera fixa.','Frase Senda: observe os detalhes legÃ­vel.')],
'MÃºsica autorizada opcional. A peÃ§a funciona sem voz. Se usar o trecho do kit, recorte conscientemente para 15 segundos e preserve o crÃ©dito.',
'Cinco cenas, 15 segundos, construÃ§Ã£o coerente e frase legÃ­vel. IdentificaÃ§Ã£o: conceito fictÃ­cio com IA.')
C('pulso','Pulso Â· anÃºncio esportivo reduzido',12,11,'TÃªnis coral, sola creme, cadarÃ§os corais; roupa azul marinho e pista azul. NÃ£o promete desempenho nem saÃºde.',[
('0â€“4','Produto','TÃªnis lateral apoiado na pista azul.','CÃ¢mera fixa ou aproximaÃ§Ã£o pequena.','Contato com a pista e solado coerentes.'),
('4â€“8','PreparaÃ§Ã£o','Pessoa adulta parada em pÃ©, braÃ§os soltos, roupa azul marinho, calÃ§ando a referÃªncia.','Pequena mudanÃ§a de peso.','Duas pernas, dois pÃ©s, equilÃ­brio.'),
('8â€“12','Um passo','Mesma pessoa e direÃ§Ã£o, espaÃ§o para avanÃ§ar um pÃ©.','Um passo curto e apoio na pista.','PÃ© nÃ£o atravessa chÃ£o; corpo nÃ£o se multiplica.')],
'TrÃªs batidas leves gravadas por vocÃª podem marcar a ediÃ§Ã£o. SÃ£o um recurso de ritmo, nÃ£o um registro cardÃ­aco. Alternativa: primeiro montar em silÃªncio.',
'TrÃªs cenas, 12 segundos, apoio e anatomia conferidos. IdentificaÃ§Ã£o: conceito fictÃ­cio com IA.')
C('arquivo','Arquivo do Vento Â· primeira pessoa',16,14,'Quatro referÃªncias: sala terracota, instrumento astronÃ´mico de latÃ£o, luvas cinza e luz do teto circular. NÃ£o representa local existente.',[
('0â€“4','Entrada','VisÃ£o da entrada para a mesa; luz da abertura circular.','AvanÃ§o lento.','Mesa e teto correspondem ao mapa.'),
('4â€“8','AproximaÃ§Ã£o','Mesma sala, mesa mais prÃ³xima; objeto permanece no centro da aÃ§Ã£o.','AvanÃ§o pequeno, sem atravessar mesa.','AproximaÃ§Ã£o coerente com a escala.'),
('8â€“12','ObservaÃ§Ã£o','Instrumento de latÃ£o prÃ³ximo; luvas na base do quadro.','MÃ£os estÃ¡veis; leve ajuste do olhar.','MÃ£os e objeto sem deformaÃ§Ã£o.'),
('12â€“16','Encerramento','Mesmo ponto de vista, instrumento e sala reconhecÃ­veis.','Movimento termina com calma.','Portas, teto e mesa permanecem no lugar.')],
'Som ambiente prÃ³prio ou autorizado, discreto. Pode comeÃ§ar em silÃªncio para conferir o espaÃ§o. MÃºsica e susto nÃ£o sÃ£o obrigatÃ³rios.',
'Quatro cenas, 16 segundos, trÃªs passagens espaciais conferidas. IdentificaÃ§Ã£o: universo fictÃ­cio com IA.')
C('dobra','Dobra Â· demonstraÃ§Ã£o em sete cenas',21,17,'Jo: pele morena, cabelo preto curto, blusa creme. Bolsa retangular de lona oliva com duas alÃ§as creme. Personagem e produto fictÃ­cios.',[
('0â€“3','ApresentaÃ§Ã£o','Jo de meio corpo segurando a bolsa inteira.','Fala curta, gestos mÃ­nimos.','Veja o formato. Boca e voz conferidas, ou narraÃ§Ã£o identificada.'),
('3â€“6','Inteiro','Bolsa inteira, mesma referÃªncia.','CÃ¢mera fixa.','A bolsa por inteiro. Forma retangular preservada.'),
('6â€“9','AlÃ§as','Detalhe das alÃ§as creme presas ao corpo da bolsa.','MÃ£o segura sem torcer.','Observe as alÃ§as. MÃ£o e tecido nÃ£o se fundem.'),
('9â€“12','Tecido','Detalhe da lona oliva.','AproximaÃ§Ã£o pequena.','Detalhe do tecido. Textura nÃ£o muda de material.'),
('12â€“15','Abertura','Bolsa aberta, sem alegaÃ§Ã£o de capacidade ou objetos surgindo.','Movimento mÃ­nimo.','Veja a abertura. Bordas e alÃ§as coerentes.'),
('15â€“18','Conjunto','Jo e bolsa inteiras no enquadramento de meio corpo.','Pose simples.','Compare o conjunto. Rosto, roupa e produto preservados.'),
('18â€“21','Encerramento','Produto visÃ­vel e espaÃ§o para identificaÃ§Ã£o.','CÃ¢mera fixa.','ConheÃ§a o conceito Dobra. Frase inteira e legÃ­vel.')],
'Use as sete frases curtas indicadas, com pausas. Voz prÃ³pria ou sintÃ©tica permitida. NarraÃ§Ã£o sobre detalhes reduz a necessidade de sincronizaÃ§Ã£o. NÃ£o invente experiÃªncia de compra.',
'Sete cenas, 21 segundos, fala, personagem e bolsa coerentes. IdentificaÃ§Ã£o visÃ­vel: DemonstraÃ§Ã£o fictÃ­cia com IA.')
(R/'context/casos.json').write_text(json.dumps(cases,ensure_ascii=False,indent=2)+'\n')
head='''<!doctype html><html lang="pt-BR" data-theme="papel"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Caderno de produÃ§Ã£o Â· LaboratÃ³rio de AnÃºncios</title><link rel="stylesheet" href="assets/aula.css"><style>main{padding-top:28px;padding-bottom:50px}h1{font-family:var(--serif);font-size:clamp(36px,7vw,58px);line-height:1.1}h2{font-family:var(--serif);font-size:32px}section{padding:24px 0;scroll-margin-top:24px}article{padding:20px;border:1px solid var(--line);border-radius:12px;margin:16px 0;background:var(--panel)}article h3{font-size:22px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:inherit;background:var(--panel);padding:18px;border:1px solid var(--line)}img{max-width:100%;height:auto;border-radius:12px}audio{width:100%}.small{font-size:16px}a{overflow-wrap:anywhere}</style></head><body><main class="wrap">'''
intro='''<p><a href="curso.html#trilha">â† voltar ao curso</a> Â· <a href="galeria.html">referÃªncias didÃ¡ticas</a></p><h1>Caderno de <em>produÃ§Ã£o</em></h1><p>Seis casos originais para estudar roteiro, continuidade e montagem. As imagens sÃ£o referÃªncias didÃ¡ticas criadas no Codex. NÃ£o hÃ¡ seis campanhas renderizadas neste kit. Os exercÃ­cios pedem que vocÃª produza e confira seus prÃ³prios arquivos.</p><p><a href="assets/kit-laboratorio.zip" download>Salvar roteiros, referÃªncias e faixa de estudo</a> Â· <a href="assets/roteiros.txt" download>Salvar roteiros em texto</a></p><p>Formato dos seis estudos: vertical 9:16, exportaÃ§Ã£o MP4 em 1080 por 1920 quando seus arquivos permitirem. NÃ£o amplie material ruim esperando recuperar detalhe. No editor, confira enquadramento e leitura. As referÃªncias do curso sÃ£o horizontais para leitura; gere suas prÃ³prias referÃªncias no formato planejado.</p><p>Acrescente identificaÃ§Ã£o legÃ­vel de conceito ou demonstraÃ§Ã£o fictÃ­cia com IA. Confira custos e recursos na conta antes de gerar. Para a produÃ§Ã£o completa, reserve 28â€“40 horas, alÃ©m de filas. A prÃ¡tica de dez minutos Ã© um recorte da etapa, frequentemente a revisÃ£o de arquivos jÃ¡ produzidos.</p>'''
nav='<nav aria-label="Casos">'+' Â· '.join(f'<a href="#{c["slug"]}">{E(c["title"].split(" Â· ")[0])}</a>' for c in cases)+'</nav>'
parts=[];txt=['LABORATÃ“RIO DE ANÃšNCIOS â€” ROTEIROS AUTORAIS','Casos fictÃ­cios, sem campanhas reais ou resultados alegados.','Formato vertical 9:16. Identifique a ficÃ§Ã£o com IA na peÃ§a.']
for c in cases:
 rows=''.join(f'<article><h3>{i}. {E(x["scene"])} Â· {x["time"]} s</h3><p><b>Imagem:</b> {E(x["image_prompt"])}</p><p><b>Movimento:</b> {E(x["motion"])}</p><p><b>ConferÃªncia:</b> {E(x["review"])}</p></article>' for i,x in enumerate(c['rows'],1))
 parts.append(f'<section id="{c["slug"]}"><h2>{E(c["title"])}</h2><p><b>Ficha fixa:</b> {E(c["fixed"])}</p><img src="assets/img/aula-{c["image"]}.webp" width="1280" height="720" alt="ReferÃªncia ilustrativa do caso {E(c["title"])}"><p class="small">Imagem didÃ¡tica do Codex; nÃ£o Ã© quadro extraÃ­do de campanha produzida.</p>{rows}<p><b>Som:</b> {E(c["voice"])}</p><p><b>Pronto:</b> {E(c["check"])}</p></section>')
 txt+=['\n'+c['title'],c['fixed']]+[f'{i}. {x["time"]}s â€” {x["scene"]}\nImagem: {x["image_prompt"]}\nMovimento: {x["motion"]}\nConferÃªncia: {x["review"]}' for i,x in enumerate(c['rows'],1)]+['Som: '+c['voice'],'Pronto: '+c['check']]
credit='Carefree â€” Kevin MacLeod (incompetech.com). LicenÃ§a CC BY 4.0: https://creativecommons.org/licenses/by/4.0/. Trecho inicial de 20 segundos, convertido para MP3. Fonte: https://incompetech.com/music/royalty-free/index.html?gt=&isrc=USUAN1400037. Obtido pelo ARCKHÉVOX em 25/09/2026. Se alterar volume, duraÃ§Ã£o ou aplicar fades, acrescente essa informaÃ§Ã£o ao crÃ©dito.'
process='''CASO:
CENA:
ARQUIVO E TENTATIVA:
REFERÃŠNCIA USADA:
PEDIDO:
SITUAÃ‡ÃƒO: aprovado / corrigir / pendente
TEMPO DO PROBLEMA:
O QUE OBSERVEI:
ALTERAÃ‡ÃƒO A TESTAR:
TRABALHO ATIVO: medido / estimado / nÃ£o medido
ESPERA DE PROCESSAMENTO:
TENTATIVAS E CONSUMO CONHECIDO:
LIMITE E ALTERNATIVA:
'''
final='''CASO ESCOLHIDO:
PÃšBLICO:
MENSAGEM:
FORMATO:
DURAÃ‡ÃƒO E CENAS:
ARQUIVOS ESPERADOS:
CRITÃ‰RIOS: sequÃªncia / identidade / som / leitura / identificaÃ§Ã£o
VERSÃƒO ANTERIOR:
VERSÃƒO REVISADA:
MUDANÃ‡A E EFEITO OBSERVADO:
DECISÃƒO:
ÃNDICE DOS SEIS ESTUDOS:
Lume â€” 18s â€” arquivo e situaÃ§Ã£o:
Vento â€” 20s â€” arquivo e situaÃ§Ã£o:
Senda â€” 15s â€” arquivo e situaÃ§Ã£o:
Pulso â€” 12s â€” arquivo e situaÃ§Ã£o:
Arquivo do Vento â€” 16s â€” arquivo e situaÃ§Ã£o:
Dobra â€” 21s â€” arquivo e situaÃ§Ã£o:
ACABAMENTO FINAL â€” arquivo e situaÃ§Ã£o:
FONTES E CRÃ‰DITOS:
PENDÃŠNCIAS REAIS:
'''
end=f'''<section id="musica"><h2>Faixa de estudo Â· 20 segundos</h2><audio controls preload="metadata" src="assets/audio/carefree-20s.mp3"></audio><p><a href="assets/audio/carefree-20s.mp3" download>Salvar a faixa</a></p><pre>{E(credit)}</pre><p><a href="https://incompetech.com/music/royalty-free/index.html?gt=&amp;isrc=USUAN1400037">Fonte da mÃºsica</a> Â· <a href="https://creativecommons.org/licenses/by/4.0/">LicenÃ§a CC BY 4.0</a></p></section><section id="processo"><h2>Ficha de processo</h2><pre>{E(process)}</pre></section><section id="final"><h2>Ficha de acabamento e Ã­ndice</h2><pre>{E(final)}</pre></section><p><a href="curso.html#trilha">Voltar Ã  trilha</a></p></main></body></html>'''
(R/'caderno.html').write_text(head+intro+nav+''.join(parts)+end)
(R/'assets/roteiros.txt').write_text('\n\n'.join(txt)+'\n\n'+process+'\n'+final+'\n\nCRÃ‰DITO\n'+credit+'\n')
(R/'assets/CREDITOS.txt').write_text(credit+'\n\nImagens: ilustraÃ§Ãµes originais geradas pelo recurso nativo do Codex. NÃ£o representam pessoas, produtos, locais ou campanhas reais. Diagramas e textos: autoria ARCKHÉ AI.\n')
with zipfile.ZipFile(R/'assets/kit-laboratorio.zip','w',zipfile.ZIP_DEFLATED) as z:
 for f in ['assets/roteiros.txt','assets/CREDITOS.txt','assets/audio/carefree-20s.mp3']:z.write(R/f,f.removeprefix('assets/'))
 for c in cases:z.write(R/f'assets/img/aula-{c["image"]}.webp','referencias/'+c['slug']+'.webp')
# Full named sequence is shown in the lesson's second teaching visual.
extra={}
for i,c in enumerate(cases):
 rows=''.join(f'<div class="item doc"><span class="pin">{j}</span><div><b>{E(x["scene"])} Â· {x["time"]} s</b><br>{E(x["review"])}</div></div>' for j,x in enumerate(c['rows'],1))
 extra[str(i*3+1)]=f'<figure class="largo"><div class="janela"><div class="tela-top">Roteiro preenchido Â· {E(c["title"])}</div><div class="janela-body">{rows}</div></div><figcaption>Plano autoral de {c["duration"]} segundos. O caderno detalha imagem, movimento e som de cada cena.</figcaption></figure>'
(R/'context/visuais-extras.json').write_text(json.dumps(extra,ensure_ascii=False,indent=2)+'\n')
# Gallery distinguishes didactic images from unproduced video.
gallery=head.replace('Caderno de produÃ§Ã£o','Galeria didÃ¡tica')+'<p><a href="curso.html#trilha">â† curso</a> Â· <a href="caderno.html">caderno</a></p><h1>ReferÃªncias <em>didÃ¡ticas</em></h1><p>Imagens criadas no Codex para ensinar escolhas. NÃ£o sÃ£o quadros extraÃ­dos de seis anÃºncios produzidos. As atividades de geraÃ§Ã£o exigem seus prÃ³prios arquivos. Os pares 2/3, 5/6, 8/9, 14/15 e 17/18 usam referÃªncia anterior, mas ainda exigem comparaÃ§Ã£o.</p>'
ls=json.loads((R/'context/aulas-editoriais.json').read_text())
for n,d in enumerate(ls,1):gallery+=f'<section id="imagem-{n}"><h2>{n}. {E(d["titulo"])}</h2><img src="assets/img/aula-{n}.webp" width="1280" height="720" loading="lazy" alt="{E(d["observacao"])}"><p>{E(d["observacao"])}</p><p><a href="assets/img/aula-{n}.webp" download>Salvar referÃªncia didÃ¡tica</a> Â· <a href="curso.html#aula-{n}">Abrir aula</a></p></section>'
(R/'galeria.html').write_text(gallery+'</main></body></html>')
