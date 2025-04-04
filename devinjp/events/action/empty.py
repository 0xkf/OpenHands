from dataclasses import dataclass

from devinjp.core.schema import ActionType
from devinjp.events.action.action import Action


@dataclass
class NullAction(Action):
    """An action that does nothing."""

    action: str = ActionType.NULL

    @property
    def message(self) -> str:
        return 'No action'
