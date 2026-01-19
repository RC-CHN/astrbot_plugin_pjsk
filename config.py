"""Configuration for pjsk plugin."""

from typing import List

# Default configuration values
DEFAULT_CONFIG = {
    "pjsk_req_retry": 1,
    "pjsk_req_timeout": 10,
    "pjsk_use_cache": True,
    "pjsk_clear_cache": False,
}

# Asset prefixes (not configurable via WebUI for simplicity)
PJSK_ASSETS_PREFIX: List[str] = [
    "https://raw.gitmirror.com/TheOriginalAyaka/sekai-stickers/main/",
    "https://raw.githubusercontent.com/TheOriginalAyaka/sekai-stickers/main/",
]

PJSK_REPO_PREFIX: List[str] = [
    "https://raw.gitmirror.com/Agnes4m/nonebot_plugin_pjsk/main/",
    "https://raw.githubusercontent.com/Agnes4m/nonebot_plugin_pjsk/main/",
]


class PluginConfig:
    """Plugin configuration wrapper."""
    
    def __init__(self, config_dict=None):
        self._config = config_dict or DEFAULT_CONFIG
    
    @property
    def pjsk_req_retry(self) -> int:
        return self._config.get("pjsk_req_retry", DEFAULT_CONFIG["pjsk_req_retry"])
    
    @property
    def pjsk_req_timeout(self) -> int:
        return self._config.get("pjsk_req_timeout", DEFAULT_CONFIG["pjsk_req_timeout"])
    
    @property
    def pjsk_use_cache(self) -> bool:
        return self._config.get("pjsk_use_cache", DEFAULT_CONFIG["pjsk_use_cache"])
    
    @property
    def pjsk_clear_cache(self) -> bool:
        return self._config.get("pjsk_clear_cache", DEFAULT_CONFIG["pjsk_clear_cache"])
    
    @property
    def pjsk_req_proxy(self):
        return None
    
    @property
    def pjsk_assets_prefix(self) -> List[str]:
        return PJSK_ASSETS_PREFIX
    
    @property
    def pjsk_repo_prefix(self) -> List[str]:
        return PJSK_REPO_PREFIX


# Global config instance (will be updated by main.py)
config = PluginConfig()
