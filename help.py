import numpy

def category(df):
    category = df.groupby('Category').sum()[['DiscountPrice' , 'OriginalPrice', 'Ratings', 'Reviews']].sort_values('OriginalPrice', ascending=False).reset_index()
    dg = category.round()
    return dg

def Individual_category(df):
    Individual_category = df.groupby('Individual_category').sum().sort_values('OriginalPrice', ascending = False).reset_index()
    fg = Individual_category.round()
    return fg

def BrandName(df):
    BrandName = df.groupby('BrandName').sum().sort_values('OriginalPrice', ascending = False).reset_index()
    sd = BrandName.round()
    return sd

def Brand_category(df):
    Category_inv = df['Category'].unique().tolist()
    return Category_inv
def brand(Category_inv, df):
    if Category_inv == 'Bottom Wear':
        X = df[df['Category'] == 'tshirts']
        r = X['BrandName'].value_counts().head(10).index
        return r
    if Category_inv == 'Indian Wear':
        X = df[df['Category'] == 'Indian Wear']
        r = X['BrandName'].value_counts().head(10).index
        return r
    if Category_inv == 'Inner Wear & Sleep  Wear':
        X = df[df['Category'] == 'Inner Wear & Sleep  Wear']
        r = X['BrandName'].value_counts().head(10).index
        return r
    if Category_inv == ' Plus Size':
        X = df[df['Category'] == 'Plus Size']
        r = X['BrandName'].value_counts().head(10).index
        return r
    if Category_inv == 'Sports Wear':
        X = df[df['Category'] == 'Sports Wear']
        r = X['BrandName'].value_counts().head(10).index
        return r
    if Category_inv == 'Topwear':
        X = df[df['Category'] == 'TopWear']
        r = X['BrandName'].value_counts().head(10).index
        return r
    if Category_inv == 'Western':
        X = df[df['Category'] == 'Western']
        r = X['BrandName'].value_counts().head(10).index
        return r 