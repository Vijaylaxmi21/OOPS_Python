class Book:
  def __init__(self,title,author ,reviews):
    self.title = title
    self.author = author
    self.reviews = []

  def add_review(self,review):
    self.reviews.append(review)

  def count_reviews(self):
    return len(self.reviews)

  def display_reviews(self):
    print("Book:", self.title)
    print("Author:", self.author)
    print("Reviews:")
    for review in self.reviews:
      print("-",review)

  
book = Book("Engineering Mathematics","H.K. Das ","very understable !")

book.add_review("very good book")
book.add_review("easy to understand")

book.display_reviews()
print("Total reviews:",book.count_reviews())

