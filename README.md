ComfyUI - Dynamic Prompts
=============================================================================

Collection of custom nodes for ComfyUI implement functionality similar
to the Dynamic Prompts extension for A1111.

The nodes use the [Dynamic Prompts][2] Python module to generate prompts
the same way, and unlike the semi-official dynamic prompts nodes, the ones
in this repo are a little easier to utilize and allow the automatic
generation of all possible combinations without manual queuing.

Nodes
-----------------------------------------------------------------------------

### Dynamic Prompt

Generates prompts and seeds based on text input. The node will either
generate a given number of prompts, choosing randomly from all possible
combinations, or return prompts for all possible combinations.

#### Random Prompts

The random mode generates a number of prompts, each one using randomly
chosen variations from all potential combinations.

**Examples**
```
# One prompt with three possibilities
1x "a {red|blue|green} dog"
=> ["a red dog"]

# Two prompts with three possibilities
2x "a {red|blue|green} dog"
=> ["a green dog", "a red dog"]

# One prompt with six possibilities
1x "a {red|blue|green} dog and a {pink|yellow} cat"
=> ["a blue dog and a yellow cat"]
```

#### Combinatorial Prompts

In this mode the node generates and returns a list of prompts that make
up every single possible combination of strings based on the input text.

**Examples**
```
# Three prompts based on three possibilities
"a {red|blue|green} dog"
=> ["a red dog", "a blue dog", "a green dog"]

# Six prompts based on six possibilities
"a {red|blue|green} dog and a {pink|yellow} cat"
=> [
    "a red dog and a pink cat",
    "a red dog and a yellow cat",
    "a blue dog and a pink cat",
    "a blue dog and a yellow cat",
    "a green dog and a pink cat",
    "a green dog and a yellow cat",
]
```

For more information, see the [Dynamic Prompts][2] repository.

#### Seeds

To give a degree of control over the seeds used in the generation
to the dynamic prompt, you may plug the result into the sampler's
seeds input. The seed will then be `fixed`, `sequential`, or `random`.

Fixing the seed is useful if you want to generate an image with a
certain subject but slight variations in colors or other details.
In this mode each prompt will receive the seed set on the node.

Sequential seeds start at the given seed for the first prompt and
increase by one for every subsequent one. This can be used to get
a degree of determinism, but without giving all prompts the same
seed.

Finally, random seeds are simply entirely random integers for every
prompt.


[1]: https://github.com/adieyal/dynamicprompts
[2]: https://github.com/adieyal/dynamicprompts
