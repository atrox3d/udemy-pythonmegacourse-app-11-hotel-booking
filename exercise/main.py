import pandas as pd
from fpdf import FPDF

class Article:
    def __init__(self, article_id):
        article = df[df.id == article_id]
        self.id = article.id.squeeze()
        self.name = article.name.squeeze()
        self.price = article.price.squeeze()
        self.stock = article['in stock'].squeeze()

    def available(self):
        self.stock = df.loc[df.id == self.id, 'in stock'].squeeze()
        return self.stock

    def buy(self):
        self.stock -= 1
        df.loc[df.id == self.id, 'in stock'] = self.stock
        df.to_csv('articles.csv', index=False)


class Receipt:
    count = 100

    def __init__(self, article):
        self.article = article

    def generate(self):
        self.count += 1
        content = f"""
        Receipt nr.{self.count}
        Article: {self.article.name}
        Price: {self.article.price}
        """
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font('Times', 'B', 14)
        pdf.write(h=7, txt=f'Receipt nr.{self.count}\n')
        pdf.write(h=7, txt=f'Article: {self.article.name}\n')
        pdf.write(h=7, txt=f'Price: {self.article.price}\n')
        pdf.output('receipt.pdf')

        return content


if __name__ == '__main__':
    df = pd.read_csv('articles.csv', dtype={'id': str})
    print(df.to_string(index=False))
    article_id = input('Enter an article to buy: ')
    article = Article(article_id=article_id)
    print(article.__dict__)
    if article.available():
        article.buy()
        print(article.__dict__)
        receipt = Receipt(article=article)
        print(receipt.generate())
