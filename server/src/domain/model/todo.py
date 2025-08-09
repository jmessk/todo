class TodoItem:
    def __init__(self, id: int, title: str, description: str | None = None):
        self.id = id
        self.title = title
        self.description = description
