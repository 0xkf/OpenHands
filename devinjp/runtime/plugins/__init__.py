# Requirements
from devinjp.runtime.plugins.agent_skills import (
    AgentSkillsPlugin,
    AgentSkillsRequirement,
)
from devinjp.runtime.plugins.jupyter import JupyterPlugin, JupyterRequirement
from devinjp.runtime.plugins.requirement import Plugin, PluginRequirement
from devinjp.runtime.plugins.vscode import VSCodePlugin, VSCodeRequirement

__all__ = [
    'Plugin',
    'PluginRequirement',
    'AgentSkillsRequirement',
    'AgentSkillsPlugin',
    'JupyterRequirement',
    'JupyterPlugin',
    'VSCodeRequirement',
    'VSCodePlugin',
]

ALL_PLUGINS = {
    'jupyter': JupyterPlugin,
    'agent_skills': AgentSkillsPlugin,
    'vscode': VSCodePlugin,
}
