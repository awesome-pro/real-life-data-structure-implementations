
class Command:
    def __init__(self, action_type, position, text) -> None:
        self.action_type=action_type
        self.position=position
        self.text=text
    
    def execute(self, document):
        if self.action_type=="insert":
            document.text = document.text[:self.position] + self.text  + document.text[self.position:]
        elif self.action_type=='delete':
            document.text = document.text[:self.position] + document.text[self.position + len(self.text):]
    
    def undo(self, document):
        if self.action_type=="insert":
            document.text = document.text[:self.position:] + document.text[len(self.text) + self.position:]
        elif self.action_type=="delete":
            document.text = document.text[:self.position] + self.text + document.text[self.position:]

class Document:
    def __init__(self) -> None:
        self.text=""
    

class UndoRedoManager:
    def __init__(self) -> None:
        self.undo_stack=[]
        self.redo_stack=[]
        self.document=Document()
    
    def perform_action(self, action_type, position, text):
        command = Command(action_type=action_type, position=position, text=text)
        command.execute(self.document)
        
        self.undo_stack.append(command)
        self.redo_stack.clear()
        return self.document.text

    def undo(self):
        if not self.undo_stack:
            return self.document.text
        command=self.undo_stack.pop()
        command.undo(self.document)
        self.redo_stack.append(command)
        return self.document.text

    def redo(self):
        if not self.redo_stack:
            return self.document.text
        command = self.redo_stack.pop()
        command.execute(self.document)
        self.undo_stack.append(command)
        return self.document.text

def test_undo_redo():
    editor = UndoRedoManager()
    
    # Test 1: Insert and undo
    assert editor.perform_action("insert", 0, "hello") == "hello"
    assert editor.undo() == ""
    
    # Test 2: Insert, undo, redo
    assert editor.perform_action("insert", 0, "hello") == "hello"
    assert editor.undo() == ""
    assert editor.redo() == "hello"
    
    # Test 3: Multiple actions
    assert editor.perform_action("insert", 5, " world") == "hello world"
    assert editor.perform_action("delete", 0, "hello") == " world"
    assert editor.undo() == "hello world"
    assert editor.redo() == " world"
    
    print("All tests passed!")

test_undo_redo()