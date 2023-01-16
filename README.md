[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/MatheusW166/document-similarity-measures/blob/main/LICENCE)

# Medidas de similaridade entre documentos

Implementação feita em trabalho de pesquisa na universidade, com o objetivo de testar e avaliar o desempenho da medida proposta no artigo [PDSM](https://journalofbigdata.springeropen.com/counter/pdf/10.1186/s40537-018-0163-2.pdf) frente a outras 7 medidas.

O algoritmo realiza a conversão do documento em um vetor binário de frequência de termos, que é usado como entrada para as funções que fazem o cálculo da similaridade.

## Uso
### Requisitos
- Python e pip
### Pacotes
- [NLTK (Natural Language Toolkit)](https://www.nltk.org/)
### Instalação (linux)
- Abra o terminal
- Clone o repositório com o comando `git clone https://github.com/MatheusW166/document-similarity-measures.git`
- Instale o pacote NTLK com o comando `pip install nltk`
- Teste a instalação, digite `python` e então `import nltk`

Para ver o guia completo para Windows e Linux, acesse [Installing NLTK](https://www.nltk.org/install.html)

### Execução
- Crie uma instância da classe `FrequencyList`
- Para adicionar um documento, invoque o método `addDocument` passando como parâmetro o caminho para o arquivo de texto
- Utilize o método `buildFrequenciesList` para obter uma lista dos vetores binários de cada documento adicionado
- Crie uma instância da classe `SimilarityMeasures` informando dois vetores
- Está feito, invoque o método com o nome da medida desejada para obter um valor entre 0 e 1 que indica o nível de similaridade entre os vetores (quanto mais próximo de 1, mais semelhantes são)

## Teoria aplicada
### Bag of Words (conversão de texto em vetor)
Bag of words, de forma simplificada, é uma lista que contém todas as palavras que estão nos textos de maneira não repetida.

Exemplo:
```python
texto1 = "Os cursos de NLP da Alura utilizam Bag of Words"
texto2 = "Aprendi Bag of Words perguntando no fórum da Alura"
```
| Bag of Words | Os | cursos | de | NLP | da | alura | utilizam | Bag | of | Words | Aprendi | perguntando | no | fórum |
|--------------|----|--------|----|-----|----|-------|----------|-----|----|-------|---------|-------------|----|-------|
| `texto1`       | 1  | 1      | 1  | 1   | 1  | 1     | 1        | 1   | 1  | 1     | 0       | 0           | 0  | 0     |
| `texto2`       | 0  | 0      | 0  | 0   | 1  | 1     | 0        | 1   | 1  | 1     | 1       | 1           | 1  | 1     |

## Tecnologias

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 

### Pacotes utilizados

 - [Natural Language Toolkit](https://www.nltk.org/)
 - [String](https://www.digitalocean.com/community/tutorials/python-string-module)
## Referência

 - [Implementação do Modelo Matemático Pairwise Document Similarity Meassure (PDSM)](https://pt.overleaf.com/read/txfdmrjbcnqx)
