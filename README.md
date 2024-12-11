# GeneriZer

 A program to convert a song to Generation Z slang.
 Current version: `GZ-0.0.0`.

# Installation Guide

 ## Requirements

 The following are the requirements for using this program.
  1. A [Python 3](https://www.python.org/) installation with [Numpy](https://numpy.org/) and [spaCy](https://spacy.io/).
  2. spaCy pipelines `en_core_web_sm`, `en_core_web_md`, and `en_core_web_lg` installed.
 
 ## Installation

  Simply clone the repository with
 ```shell
 git clone https://github.com/Phoenix-the-Imperial/GeneriZer
 ```

# Usage

 The usage is simple.
 * To define the word-map, edit the file `data/wordmap.json`.
 * To edit the corpus, edit the file `data/corpus.txt`.

# Goals

 The high-level goals are as follows.
 - [ ] Lyrics
   - [ ] Use a word and phrase map.
   - [ ] Learn the word and phrase map.
 - [ ] Music
   - [ ] Filter the music from the audio.
   - [ ] Change the music to suit "generation Z".
   - [ ] Learn the music changes.
 - [ ] Voice
   - [ ] Filter the voice from the audio.
   - [ ] Change the voice to suit a given voice.
   - [ ] Learn the voice from given samples.