from .nodes.dynamic_prompt import ETDynamicPrompt

et_nodes = {
    ("Dynamic Prompt", ETDynamicPrompt),
}

NODE_CLASS_MAPPINGS = {cls.__name__: cls for display_name, cls in et_nodes}
NODE_DISPLAY_NAME_MAPPINGS = {cls.__name__: display_name for display_name, cls in et_nodes}

WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
