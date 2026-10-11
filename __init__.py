"""Optional ComfyUI entry point; standalone imports start no host services."""
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
try:
    import folder_paths as _folder_paths
    from server import PromptServer as _PromptServer
except ModuleNotFoundError as exc:
    if exc.name not in ("folder_paths", "server"):
        raise
else:
    from .integrations.comfyui import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

WEB_DIRECTORY = "./integrations/comfyui/web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
