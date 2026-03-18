# 🤖 Sistema de Automação de Cadastro (RPA)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/PyAutoGUI-FFD43B?style=for-the-badge&logo=python&logoColor=3776AB" />
  <img src="https://img.shields.io/badge/RPA-Automation-007ACC?style=for-the-badge" />
</p>

> **Robotic Process Automation (RPA)** para cadastro automático de produtos, reduzindo tarefas manuais, erros humanos e tempo operacional.

---

## 🚀 Visão Geral

Este projeto automatiza o processo de **cadastro de produtos em um sistema web**, simulando interações humanas com mouse e teclado.

A automação realiza:
- Abertura do navegador  
- Login automático  
- Leitura de dados de um arquivo CSV  
- Preenchimento de formulários  
- Cadastro em massa de produtos  

Tudo de forma **data-driven**, escalável e repetível.

---

## 🧠 Fluxo da Automação

```
1. Abrir navegador
2. Acessar sistema
3. Realizar login
4. Ler base de dados (CSV)
5. Para cada produto:
   → Preencher formulário
   → Enviar cadastro
6. Repetir até finalizar lista
```

---

## ✨ Funcionalidades

- 🤖 **Automação completa de interface (UI Automation)**  
- 🔐 **Login automatizado no sistema**  
- 📊 **Leitura de dados com Pandas (CSV)**  
- 🔁 **Cadastro em massa (loop automatizado)**  
- ⚠️ **Tratamento de campos opcionais (ex: observações)**  
- ⏱️ **Controle de tempo e sincronização (delays)**  

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**

### 📦 Bibliotecas

- **PyAutoGUI** → Automação de mouse e teclado  
- **Pandas** → Manipulação de dados  
- **Time** → Controle de execução  

---

## 📂 Estrutura do Projeto

```
.
├── codigo.py          # Script principal da automação
├── auxiliar.py        # Script para captura de posição do mouse
├── produtos.csv       # Base de dados dos produtos
```

---

## ▶️ Como Executar

### 1. Pré-requisitos

- Python instalado  
- Google Chrome instalado  

Instale as dependências:

```bash
pip install pyautogui pandas openpyxl
```

---

### 2. Preparar os dados

Certifique-se de que o arquivo:

```
produtos.csv
```

está na mesma pasta do script.

---

### 3. Ajustar coordenadas

⚠️ Como o PyAutoGUI utiliza posições da tela:

- Ajuste os valores de `pyautogui.click(x, y)`
- Use o script auxiliar para descobrir posições

---

### 4. Executar

```bash
python codigo.py
```

🚨 **Importante:**  
Não utilize mouse ou teclado durante a execução da automação.

---

## 📄 Exemplo de Código (Trecho Principal)

```python
for linha in tabela.index:
    pyautogui.click(x=671, y=258)

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("enter")
```

---

## ⚠️ Pontos de Atenção

- Dependente de resolução de tela  
- Sensível a mudanças na interface do sistema  
- Requer ajustes finos de tempo (`sleep`)  

---

## 🎯 Conceitos Aplicados

- Robotic Process Automation (RPA)  
- UI Automation  
- Data-Driven Automation  
- Automação de tarefas repetitivas  
- Integração entre dados e interface  

---

## 🚀 Possíveis Melhorias

- 🔍 Detecção de elementos com visão computacional (OpenCV)  
- 🧠 Uso de Selenium para automação mais robusta  
- ⚙️ Parametrização de configurações (tempo, coordenadas)  
- 🖥️ Interface gráfica para controle da automação  

---

## 🤝 Autor

**Emanuelle Gomes**

Desenvolvedora focada em automação, backend e soluções escaláveis  
Transformando tarefas manuais em processos inteligentes 🤖✨
