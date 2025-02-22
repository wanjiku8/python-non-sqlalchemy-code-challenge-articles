def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine  # ✅ Store it as an attribute
        self.title = title

        # Ensure the magazine is linked to this article
        magazine.add_article(self)

        
class Author:
    def __init__(self, name):
        self.name = name

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass