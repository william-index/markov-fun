# Markov Fun

This repo is for playing with markov models/chains, and most likely will evolve into some flavor of twitter bot.

### Classes

#### Trainer
Trainer is used for returning a trained set of data. Currently the list of options for a given key are not calculated as percentages, but return as a list of redundancies.

example:
```
{'multi token key': ['foo', 'bar', 'bar', 'bar']}
```

#### Stepper
Stepper Steps through a trained model to create a phrase from its tokens, starting with a random key.
