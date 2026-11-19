# LaboratÃ³rio de AnÃºncios com IA v6.2

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="48" />
  <p><strong>Arckhé AI</strong></p>
</div>


Curso aberto INEMA.CLUB. 24 aulas em 8 mÃ³dulos, estilo OSWork v6.2. Seis casos originais e fictÃ­cios: Lume, Vento, Senda, Pulso, Arquivo do Vento e Dobra.

Estimativa completa: 28â€“40 horas de estudo e produÃ§Ã£o, alÃ©m de filas. Requer saber gerar imagens, clipes e editar, ou cursar previamente Prompting, Kling e CapCut.

IlustraÃ§Ãµes geradas pelo recurso nativo de imagens do Codex. A ferramenta nÃ£o expÃµe seletor ou confirmaÃ§Ã£o de uma versÃ£o chamada 2.5; nÃ£o foi substituÃ­da por serviÃ§o externo. O curso fornece roteiros, referÃªncias, pedidos e faixa licenciada. NÃ£o fornece seis campanhas renderizadas nem alega execuÃ§Ã£o de testes de vÃ­deo nos serviÃ§os externos. As atividades exigem arquivos produzidos pelo aluno; pendÃªncia nÃ£o equivale a conclusÃ£o.

O kit reutiliza trecho de Carefree, Kevin MacLeod, CC BY 4.0, obtido pelo INEMAVOX e creditado. NÃ£o publica material privado do acervo de anÃ¡lise.

ReconstruÃ§Ã£o: python3 montar.py. EvidÃªncias em context/.

## English / EspaÃ±ol

[English](https://inematds.github.io/curso-laboratorio-anuncios-ia/en/) Â· [EspaÃ±ol](https://inematds.github.io/curso-laboratorio-anuncios-ia/es/)

Textos traduzidos com GPT-6 Luna por subagentes nativos da assinatura Codex, sem API externa. IlustraÃ§Ãµes originais compartilhadas; progresso e anotaÃ§Ãµes separados por idioma.

ApÃ³s montar o portuguÃªs, reaplique os catÃ¡logos salvos:

```sh
python3 scripts/i18n_local.py build .
python3 scripts/verify_i18n.py .
node scripts/check_i18n_browser.cjs . /tmp/curso-i18n-checks
```

Requer Python/BeautifulSoup e os pacotes locais Babel/Playwright indicados nos scripts. A montagem nÃ£o chama modelos nem redes. MudanÃ§as na fonte PT exigem revisar os catÃ¡logos `i18n/`. O motor oficial `assets/curso.js` Ã© preservado; a proteÃ§Ã£o de importaÃ§Ã£o Ã© gerada em `assets/curso-i18n.js` e nas ediÃ§Ãµes traduzidas.

EvidÃªncias em `context/validacao-i18n.md`. RevisÃµes por agentes sÃ£o simuladas, nÃ£o testes com alunos reais.

<!-- inema-backlink:v1 -->
## Mais no INEMA.CLUB

- [Ficha completa deste curso](https://www.inema.club/cursos/298-laboratorio-de-anuncios-com-ia-6-cases-desmontados/)
- [Guia: como aprender inteligÃªncia artificial](https://www.inema.club/aprender-inteligencia-artificial/)
- [Todos os cursos](https://www.inema.club/cursos/)
<!-- /inema-backlink:v1 -->

---

<div align="center">
  <img src="capa/logo.svg" alt="Arckhé AI" height="32" />
  <p><strong>Arckhé AI</strong></p>
</div>