from pydantic import Field

from devinjp.integrations.provider import PROVIDER_TOKEN_TYPE
from devinjp.integrations.service_types import Repository
from devinjp.server.settings import Settings


class ConversationInitData(Settings):
    """
    Session initialization data for the web environment - a deep copy of the global config is made and then overridden with this data.
    """

    git_provider_tokens: PROVIDER_TOKEN_TYPE | None = Field(default=None, frozen=True)
    selected_repository: Repository | None = Field(default=None)
    replay_json: str | None = Field(default=None)
    selected_branch: str | None = Field(default=None)

    model_config = {
        'arbitrary_types_allowed': True,
    }
