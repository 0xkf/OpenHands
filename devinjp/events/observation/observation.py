from dataclasses import dataclass

from devinjp.events.event import Event


@dataclass
class Observation(Event):
    content: str
