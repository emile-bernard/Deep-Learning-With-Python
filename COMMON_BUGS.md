# Common bugs

## Description

Here is a list of common bugs and there solution.

## No module named tensorflow in jupyter

```
pip install tensorflow # Current release for CPU-only
```
```
conda install jupyter notebook
```
## UnicodeDecodeError: 'charmap' codec can't decode byte X in position Y: character maps to <undefined>

Specify the encoding when you open the file:
```
file = open(filename, encoding="utf8")
```

## Links

- [No module named tensorflow in jupyter](https://stackoverflow.com/questions/38221181/no-module-named-tensorflow-in-jupyter)

- [Tensorflow instal](https://www.tensorflow.org/install/#overview)

- [UnicodeDecodeError: 'charmap' codec can't decode byte X in position Y: character maps to <undefined>](https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character)
