# 🏥 Projeto de Informações de Saúde e agendamento de consultas com Dashboard

Este é um sistema web desenvolvido com **Django** e **Bootstrap** que tem como objetivo fornecer **informações acessíveis sobre saúde**, com recursos como:

- Cadastro de agendamentos
- Dashboard interativo com dados de doenças
- Informações sobre serviços de saúde e direitos dos pacientes
- Navegação inclusiva e acessível

---

## 🚀 Funcionalidades

- ✅ Cadastro e visualização de agendamentos médicos
- 📊 Dashboard com gráfico de doenças registradas nos últimos 30 dias
- 🔎 Interface intuitiva com foco em acessibilidade
- 📄 Informações sobre direitos de pacientes e serviços públicos de saúde
- 🎧 (Em desenvolvimento) Leitura em voz alta e navegação facilitada para pessoas com deficiência

---

## 🛠️ Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/)
- [Chart.js](https://www.chartjs.org/) – para geração dos gráficos
- HTML5, CSS3, JavaScript

---

## 📦 Como Executar Localmente

1. **Clone o repositório:**

```bash
git clone https://github.com/KaioHerculano/health_in_focus.git
cd seu-repositorio
```
2. **Crie e ative um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```
3.**Instale as dependências:**
```bash
pip install -r requirements.txt
```
4. **Aplique as migrações e execute o servidor:**
```bash
python manage.py migrate
python manage.py runserver
```
5.**Acesse no navegador:**
```bash
http://127.0.0.1:8000/
```
## 📊 Sobre o Dashboard
- O dashboard coleta dados dos agendamentos salvos no modelo Scheduling e exibe os nomes das doenças (especialidades) mais frequentes nos últimos 30 dias, utilizando gráficos interativos via Chart.js.

## 🤝 Contribuindo
- Contribuições são bem-vindas! Abra uma issue ou envie um pull request com sugestões de melhoria.
