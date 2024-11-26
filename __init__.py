from .nodes.dynamic_prompt import ETDynamicPrompt

NODE_CLASS_MAPPINGS = {
    "ETDynamicPrompt": ETDynamicPrompt,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ETDynamicPrompt": "Dynamic Prompt",
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
