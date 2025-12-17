from dataclasses import dataclass

@dataclass
class TodoDTO:
    title: str
    description: str = ""
    is_completed: bool = False
