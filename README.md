# Markov Fun

This repo is for playing with markov models/chains, and most likely will evolve into some flavor of twitter bot.

### Classes

#### Trainer
Trainer is used for returning a trained set of data. Currently the list of options for a given key are not calculated as percentages, but return as a list of redundancies.

example:
```
{'multi token key': ['foo', 'bar', 'bar', 'bar']}
```

#### Generating training sets
Training sets can be downloaded from google for images at 100 by 100 pixel resolution and cropped to center by running

```
python create_image_dataset.py '<string>' --count <int> --size <int> <int> --cRange <int>
```

the string is the work that google will search for images for

* **count** - number of images to retrieve (currently max 20)
* **size** - 2 ints for width and height respectively that represent the size of all images in the set
* **cRange** - range of possible/distributed RGB values to reduce image to
  * for example a cRange of 2 would enable a red value of either 0 or 255 where a cRange of 4 would allow 0,85,170,255 as possible values


#### Generating Images from Image sets
An image can be generated from any set of images within a directory

by calling
```
python generate_image.py '<string>' --size <int> <int> --norder <int>
```

* **<string>** - path to image directory
* **size** - 2 ints for width and height respectively that represent the size of all images in the set
* **norder** - what order markov chain to use


#### Stepper
Stepper Steps through a trained model to create a phrase from its tokens, starting with a random key.
