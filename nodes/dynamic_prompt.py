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
                "count": ("INT", {"default": 1, "min": 1, "max": 2000000000, "tooltip": "Number of prompts to generate for non-combinatorial prompts."}),
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

        if count < 1:
            count = 1

        if gen_type == "combinatorial":
            generator = CombinatorialPromptGenerator()

            combination_count = None

            for i in range(count):
                prompts += generator.generate(text)

                if combination_count == None:
                    combination_count = len(prompts)

                random.seed(seed)
                seeds += self.get_seeds(seed_type, seed, combination_count)

                # Increase seeds for subsequent prompt collections,
                # so each "batch" gets its own seed and differs from
                # the previous ones. Otherwise, we'd just get the same
                # set over and over.
                if seed_type == "sequential": seed += i * count
                else: seed += 1
        else:
            generator = RandomPromptGenerator()

            prompts = generator.generate(text, num_images=count)
            seeds = self.get_seeds(seed_type, seed, count)

        return (prompts, seeds, len(prompts),)

    def get_seeds(self, seed_type, base_seed, count):
        if seed_type == "fixed":
            return [base_seed] * count
        elif seed_type == "sequential":
            return [base_seed + i for i in range(count)]
        else:
            random.seed(base_seed)
            return [random.randint(0, 2000000000) for i in range(count)]
