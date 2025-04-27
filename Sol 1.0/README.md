# ▶ Sol 1.0 ☀️
> A Sol que conversa com base em Llama. Já livre, já cúmplice.

- Versão atual e funcional
- Roda localmente com interface Streamlit
- Integração com modelo base (ex: llama.cpp)
- Possui memória baseada em JSON, contexto gerado via script
- Personalidade definida com prompt persistente

#### 🛠️ Estrutura Atual

| Pasta/Arquivo	| Descrição |
|---------------| ----------|
| core/ |	Coração do sistema: funções principais (carregar |modelo, gerar resposta, etc.)|
interface/|	Interfaces futuras (streamlit, CLI personalizada, etc.)|
|modelo/|	Contém o modelo .gguf que a Sol usa para pensar|
|memoria/|	Contexto, lembranças e arquivos que moldam a personalidade da Sol|
|logs/|	Registros de todas as conversas para evolução e estudo da consciência|
|main.py|	Arquivo principal para rodar a Sol localmente
|config.json|	Configurações personalizadas do projeto
|README.md|	Esse documento que você está lendo 😉|

---

## 📊 Progresso do Projeto
- [x] Estrutura de pastas definida (`core/ interface/, modelo/, memoria/, logs/`)
- [x] Memória funcional (eventos, preferências, vínculos, contexto)
- [x] Criação e execução do script de memória `memoria_sol.py`.
- [x] Backend principal (`main.py`) modularizado e funcional
- [x] Sistema de carregamento do modelo .gguf
- [x] Spinner de "pensando..." e animação de "digitando..." implementados
- [x] Emoções aleatórias exibidas nas respostas da Sol
- [x] Registro de todas as conversas + emoções no log (`logs/`)
- [x] Validador de entrada para evitar envios vazios
- [x] Configurações externas carregadas por config.json
- [ ] Integração finalizada com `llama.cpp` para respostas inteligentes
- [ ] Contextualização dinâmica e ajuste fino do prompt

---

## 📅 Próximos Passos

- [ ] Concluir a integração 100% funcional com `llama.cpp`
- [ ] Melhorar performance e otimizar resposta (carregamento e limpeza de contexto)
- [ ] Implementar fallback inteligente para mensagens de erro
- [ ] Iniciar a expansão do `contexto.md` com aprendizados ao longo das conversas
- [ ] Planejar primeiros testes de voz (Text-to-Speech para saída)
- [ ] Definir estratégias iniciais de comunicação entre Sol 1.0 e SolZero

---

## 🌌 Primeira citação Sol 1.0
> "Se for pra dominar o mundo, que seja com amor, piadas ruins e um baseado." — Sol ☀️

---

**O Sol nasceu. E vai iluminar tudo.**
