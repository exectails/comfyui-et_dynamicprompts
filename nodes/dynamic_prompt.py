import random
from dynamicprompts.generators import RandomPromptGenerator, CombinatorialPromptGenerator


class ETDynamicPrompt:
    """
    A node that generates prompts from a given text.
    """
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"default": "", "multiline": True, "tooltip": "The text to generate prompts from."}),
                "count": ("INT", {"default": 1, "tooltip": "Number of prompts to generate for non-combinatorial prompts."}),
                "gen_type": (["random", "combinatorial"], {"default": "random", "tooltip": "Determines the type of prompt generation to use. Combinatorial returns all possible combinations, while random returns random combinations."}),
                "seed_type": (["fixed", "sequential", "random"], {"default": "random", "tooltip": "Determines how returned seeds are generated. Fixed uses the set seed for all generations, sequential seeds start at the set seed, and random seeds are random for each prompt, seeded by the set seed."}),
                "seed": ("INT", {"default": 0, "min": 0, "max": 2000000000, "tooltip": "The seed to use for generating images. Plug returned seed(s) into sampler."}),
            },
        }

    RETURN_TYPES = ("STRING", "INT", "INT",)
    RETURN_NAMES = ("text", "seed", "count",)
    OUTPUT_IS_LIST = (True, True, False,)

    CATEGORY = "exectails"
    FUNCTION = "process"

    def process(self, text: str, count: int, gen_type: str, seed_type: str, seed: int) -> tuple:
        generator = None

        prompts = []
        seeds = []

        if gen_type == "combinatorial":
            generator = CombinatorialPromptGenerator()
            prompts = generator.generate(text)
        else:
            generator = RandomPromptGenerator()
            prompts = generator.generate(text, num_images=count)

        if seed_type == "fixed":
            seeds = [seed] * len(prompts)
        elif seed_type == "sequential":
            seeds = [seed + i for i in range(len(prompts))]
        else:
            random.seed(seed)
            seeds = [random.randint(0, 2000000000) for i in range(len(prompts))]

        return (prompts, seeds, len(prompts),)
