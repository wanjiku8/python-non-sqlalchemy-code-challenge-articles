#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Article, Author, Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Creating Authors
    author1 = Author("Alice Walker")
    author2 = Author("James Baldwin")
    author3 = Author("Toni Morrison")

    # Creating Magazines (Ensuring name is <= 16 characters)
    mag1 = Magazine("New Yorker", "Literature")
    mag2 = Magazine("NatGeo", "Science")  # Shortened "National Geographic"
    mag3 = Magazine("Time", "News")

    # Creating Articles
    article1 = author1.add_article(mag1, "The Power of Words")
    article2 = author1.add_article(mag2, "Exploring the Wild")
    article3 = author2.add_article(mag1, "Race and Identity")
    article4 = author2.add_article(mag3, "Politics Today")
    article5 = author2.add_article(mag3, "The Future of AI")
    article6 = author2.add_article(mag3, "Climate Change Impact")
    article7 = author3.add_article(mag1, "Storytelling in America")

    # Don't remove this line, it's for debugging!
    ipdb.set_trace()
