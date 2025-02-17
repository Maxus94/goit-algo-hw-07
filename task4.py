class Comment:
    def __init__(self, text, author):        
        self.comment = text
        self.author = author
        self.comments = []
        self.is_deleted = False
    
    def add_reply(self, comment):
        self.comments.append(comment)        

    def remove_reply(self):
        self.is_deleted = True
        self.comment = "Цей коментар було видалено."

    def display(self, level = 0):        
        if len(self.comments) == 0:
            print(level * "    " + self.author + ": " + self.comment if not self.is_deleted else level * "    " + self.comment) 
        else:        
            print(level * "    " + self.author + ": " + self.comment if not self.is_deleted else level * "    " + self.comment)
            for item in self.comments:
                item.display(level + 1)

    

root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)
reply1.remove_reply()
root_comment.display()