class BrowserHistory:
    def __init__(self) -> None:
        self.back_stack=[]
        self.forward_stack=[]
        self.current_url=""
        
    def visit(self, url):
        if self.current_url:
            self.back_stack.append(self.current_url)
        self.forward_stack.clear()
        self.current_url=url
        return self.current_url
    
    def back(self):
        if not self.back_stack:
            return None
        self.forward_stack.append(self.current_url)
        self.current_url=self.back_stack.pop()
        return self.current_url
    
    def forward(self):
        if not self.forward_stack:
            return None
        self.back_stack.append(self.current_url)
        self.current_url = self.forward_stack.pop()
        
        return self.current_url