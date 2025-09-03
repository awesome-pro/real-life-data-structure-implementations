class TreeNode:
    def __init__(self, name, is_file=False) -> None:
        self.name=name
        self.is_file=is_file
        self.children={} if not is_file else None

class FileSystem:
    def __init__(self) -> None:
        self.root = TreeNode('/', is_file=False)
    
    def add_node(self, path, is_file):
        node = self.root
        
        segments = [seg for seg in path.strip('/').split('/') if seg]
        if not segments:
            return False
        
        for  seg in segments[:-1]:
            if seg not in node.children:
                node.children[seg]=TreeNode(name=seg, is_file=False)
            node = node.children[seg]
            if node.is_file:
                return ValueError(f"Path {path} conflicts with file at {seg}")
        
        last_seg = segments[:-1]
        if last_seg in node.children:
            if node.children[last_seg].is_file != is_file:
                raise ValueError(f"Path {path} conflicts with existing node type")
            return True
        
        node.children[last_seg]=TreeNode(name=last_seg, is_file=is_file)
        return True
    
    def search(self, path: str):
        node = self.root
        
        segments = [seg for seg in path.strip('/').split('/') if seg]
        if not segments:
            return self.root
        
        for seg in segments:
            if seg not in node.children:
                return None
            seg = node.children[seg]
        return node