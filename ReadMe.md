# NoteBook Project

## What is it ?

The aim is to post small notes mainly about programming languages.

Subjects can vary: from small hints to concept explanations and more

## How it works

Simple static web pages uploaded via GitHub Pages and a GitHub Actions pipeline.

### Inside machinery

I usually take notes in Markdown because I like its simplicity to organize almost anything.

I have tried many Markdown notepad applications (Obsidian, etc.),
but I had some trouble sharing files with other users or across different computers.
I found that a GitHub repository works just fine.

1) Once I am done taking notes, I use a basic python app that I created to turn `MD` files into
   html files, enabling css for the notes wich is a plus.
   [Md2Html project](https://github.com/TomJcb11/CrashTest/tree/master/Markdown2HTML)
2) Then I place the `HTML` file inside this project where it is supposed to be and i execute another simple python program that update the `index.html` files
3) Then every commit on `main` triggers a new build on the following URL [NoteBook](https://tomjcb11.github.io/NoteBook)

I tried to keep it as lightweight as possible (no services, no databases, etc.).
