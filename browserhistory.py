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
    
    
def test_browser_history():
    browser = BrowserHistory()
    
    # Test 1: Visit and check current
    assert browser.visit("page1.com") == "page1.com"
    assert browser.visit("page2.com") == "page2.com"
    
    # Test 2: Go back
    assert browser.back() == "page1.com"
    assert browser.back() == None
    
    # Test 3: Go back on empty stack
    assert browser.back() == None
    
    # Test 4: Go forward
    assert browser.forward() == "page1.com"
    assert browser.forward() == "page2.com"
    
    # Test 5: Go forward on empty stack
    assert browser.forward() == "page2.com"
    
    # Test 6: Branching
    assert browser.back() == "page1.com"
    assert browser.visit("page3.com") == "page3.com"
    assert browser.forward() == "page3.com"  # No forward history
    assert browser.back() == "page1.com"
    
    print("All tests passed!")

test_browser_history()