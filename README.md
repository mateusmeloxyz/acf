# acf

Read the Word of God from your terminal

Taken from an old version of [https://github.com/bontibon/kjv.git](https://github.com/bontibon/kjv.git) and [https://github.com/LukeSmithxyz/kjv](https://github.com/LukeSmithxyz/kjv)

## Usage

    usage: ./acf [flags] [reference...]

      -l      list books
      -W      no line wrap
      -h      show help

      Reference types:
          <Book>
              Individual book
          <Book>:<Chapter>
              Individual chapter of a book
          <Book>:<Chapter>:<Verse>[,<Verse>]...
              Individual verse(s) of a specific chapter of a book
          <Book>:<Chapter>-<Chapter>
              Range of chapters in a book
          <Book>:<Chapter>:<Verse>-<Verse>
              Range of verses in a book chapter
          <Book>:<Chapter>:<Verse>-<Chapter>:<Verse>
              Range of chapters and verses in a book

          /<Search>
              All verses that match a pattern
          <Book>/<Search>
              All verses in a book that match a pattern
          <Book>:<Chapter>/<Search>
              All verses in a chapter of a book that match a pattern

## Build

acf can be built by cloning the repository and then running make:

    git clone https://github.com/mateusgomes01/acf
    cd acf
    sudo make install

## License

Public domain

# acf

Leia a palavra de Deus direto do terminal

Código retirado de uma versão antiga de [https://github.com/bontibon/kjv.git](https://github.com/bontibon/kjv.git) e [https://github.com/LukeSmithxyz/kjv](https://github.com/LukeSmithxyz/kjv)

## Uso

    Uso: ./acf [flags] [referência...]

      -l      lista livros
      -W      sem quebra de linha
      -h      exibe ajuda

      Tipos de referência:
          <Livro>
              Livro individual
          <Livro>:<Capítulo>
              Capítulo individual de um livro
          <Livro>:<Capítulo>:<Verso>[,<Verso>]...
              Verso(s) individuais de um capítulo específico de um livro
          <Livro>:<Capítulo>-<Capítulo>
              Série de capítulos de um livro
          <Livro>:<Capítulo>:<Verso>-<Verso>
              Série de versos em um capítulo de um livro
          <Livro>:<Capítulo>:<Verso>-<Capítulo>:<Verso>
              Série de capítulos e versos de um livro

          /<Busca>
              Todos versos que combinam com uma busca
          <Livro>/<Busca>
              Todos os versos de um livro que combinam com uma busca
          <Livro>:<Capítulo>/<Busca>
              Todos versos de um capítulo de um livro que combinam com uma busca

## Montagem

acf pode ser montado clonando o repostitório e rodando make:

    git clone https://github.com/mateusgomes01/acf
    cd acf
    sudo make install

## Licença

Public domain
