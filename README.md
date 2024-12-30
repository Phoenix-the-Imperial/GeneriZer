# GeneriZer

 A program to convert a song to Generation Z slang.
 Current version: `GZ-0.0.5`.

# Installation Guide

 ## Requirements

 The following are the requirements for using this program.
  1. A [Python 3](https://www.python.org/) installation with [Numpy](https://numpy.org/) and [spaCy](https://spacy.io/).
  2. spaCy pipelines `en_core_web_sm`, `en_core_web_md`, and `en_core_web_lg` installed.
 
 ## Installation

  Simply clone the repository with the following command.
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
   - [ ] Create the full phrase map.
   - [ ] Create a phrase-similarity-graph.
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
 - [ ] Documentation
   - [ ] API documentation.
   - [ ] High-level usage documentation.

# Version History

 ## Version GZ-0.0.5

  The following changes were made.
  1. Tentatively completed the phrase-map.
  2. Renamed the extension of the log file from `.txt` to `.log`.

 ## Version GZ-0.0.4

  Randomized the choices of similar and replacement phrases.

 ## Version GZ-0.0.3

  Added more Generation Z slang in the word-map.

 ## Version GZ-0.0.2

  The following additions were made.
  1. Added sentence selection and randomized phrase replacement.
  2. Added a logging system for easy debugging.

 ## Version GZ-0.0.1

  Added phrase-mapping system.

 ## Version GZ-0.0.0

  Initial commit. Has a basic text translation (to generation Z slang) system based on synonyms and a pre-defined word-map.
