class Comment:
    def __init__(self, text, author):        
        self.comment = text
        self.author = author
        self.comments = []        
    
    def add_reply(self, comment):
        self.comments.append(comment)        

    def display(self):        
        if len(self.comments) == 0:
            print(self.author + ": ", self.comment) 
        else:        
            print(self.author + ": ", self.comment)
            for item in self.comments:
                item.display()

    

root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)
root_comment.display()
print(root_comment.comment, root_comment.author, root_comment.comments)