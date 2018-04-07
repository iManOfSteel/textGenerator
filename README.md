# Text generateor based on Markov chains

## There are two parts:

### train.py
Creates model from given texts set. To find out how to use it type in the command line:
```bash
python3 train.py -h
```

### generate.py
Generates text using given model. To find out how to use it type in the command line:
```bash
python3 generate.py -h
```

Generator supports usage of n-gram, but for n > 2 you have to train model with huge amount of text
to get good results.