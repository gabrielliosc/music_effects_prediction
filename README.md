<a name="readme-top">Pt-br</a>

<br />
<div align="center">
<h3 align="center">Site de predição do impacto da música utilizando IA</h3>
  <p><a href="https://github.com/gabrielliosc/comunidade-tech/issues">Report Bug</a></p>
</div>

<details>
  <summary>Súmario</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o projeto</a>
      <ul>
        <li><a href="#built-with">Construído Utilizando</a></li>
      </ul>
    </li>
    <li><a href="#instalacao">Instalação</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contato">Contato</a></li>
    <li><a href="#creditos">Créditos</a></li>
  </ol>
</details>

## Sobre O Projeto

<p>Bem vindo(a)! Esse é um pojeto fullstack desenvolvido para um MVP da Pós-graduação de engenharia de software da Puc-Rio. 
Foi treinado um modelo de machine learning utilizando o algoritmo random forest e a seguinte base de dados: https://www.kaggle.com/datasets/catherinerasgaitis/mxmh-survey-results
</p>
<p>No frontend da aplicação apresentação um formulário com perguntas sobre informações pessoais e de hábitos do usuário</p>

![image](https://github.com/user-attachments/assets/605e2abd-7496-48a7-a514-dcb44cd5196a)

<p>No backend da aplicação foi criada uma API Rest que lê os dados do questionário do frontend
e retorna a predição do impacto da música a partir do modelo treinado.

![image](https://github.com/user-attachments/assets/e9fccf67-c8dc-4988-baab-e7d1b8c75c24)

Além disso foi implementado no backend um teste automatizado para testar a acurácia do modelo</p>

![image](https://github.com/user-attachments/assets/75bcb197-4e5d-4e71-96f1-469ac2a2aac4)

<p>Demo</p>

https://github.com/user-attachments/assets/a5585337-4911-44f0-8755-6e294d140626


<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

[![Javascript][Javascript]][Javascript-url] [![CSS3][CSS3]][CSS3-url] [![HTML5][HTML5]][HTML5-url] [![Python]][Python-url] [![flask][flask]][flask-url] [![sklearn][sklearn]][sklearn-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Instalação

1. Clone o repositório
   ```sh
   git clone https://github.com/gabrielliosc/music_effects_prediction.git
   ```
2. Navegue até a pasta do backend
3. Instale as dependências
   ```sh
   conda install --file requirements.txt
   ```
4. Para rodar o teste automatizado
   ```sh
   pytest test_model.py
   ```
6. Para rodar a API inicie a aplicação flask
   ```sh
   flask run --host 0.0.0.0 --port 5000 --reload
   ```
7. Abra o arquivo index.html do frontend no navegador

## Contato

Gabrielli de Oliveira e Silva da Cruz- [Linkedin](https://www.linkedin.com/in/gabrielli-oliveira-cruz/) - gabrielli.osc@gmail.com

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Créditos

* [Font Awesome](https://fontawesome.com) 
* [Kaggle](kaggle.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[Javascript]: https://img.shields.io/badge/Javascript-efd81d?style=for-the-badge&logo=javascript&logoColor=ffffff
[Javascript-url]: https://developer.mozilla.org/pt-BR/docs/Web/JavaScript
[HTML5]: https://img.shields.io/badge/Html5-ea5d24?style=for-the-badge&logo=Html5&logoColor=ffffff
[HTML5-url]: https://developer.mozilla.org/en-US/docs/Glossary/HTML5
[CSS3]: https://img.shields.io/badge/css3-2862e9?style=for-the-badge&logo=css3&logoColor=ffffff
[CSS3-url]: https://developer.mozilla.org/pt-BR/docs/Web/CSS
[sklearn]: https://img.shields.io/badge/Sklearn-f6993a?style=for-the-badge&logo=scikit-learn&logoColor=white
[sklearn-url]: https://scikit-learn.org/stable/
[Python]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Flask]: https://img.shields.io/badge/flask-000?style=for-the-badge&logo=flask&logoColor=ffffff
[Flask-url]: https://flask.palletsprojects.com/en/3.0.x/

