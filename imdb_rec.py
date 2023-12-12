import requests

class IMDB_Rec:
    def __init__(self):
        pass
        
    def get_movie_recommendations(self, movieID):
        imdb_url = 'https://www.imdb.com/title/' + str(movieID)
        imdb_header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        imdb_response = requests.get(imdb_url, headers=imdb_header)
    
        list_container = str(imdb_response.text).split('<')
        toggle = False
        movies = []
        for i in list_container:
            if 'StaticFeature_MoreLikeThis' in str(i) or 'MoreLikeThis' in str(i):
                toggle = True
            if toggle == True:
                if '/title/tt' in str(i):
                    for y in str(i).split('"'):
                        if '/title/tt' in str(y):
                            for j in str(y).split('/'):
                                if 'tt' in str(j) and str(j).replace('tt','').isnumeric():
                                    if str(j) not in str(movies):
                                        movies.append(j)
            if 'StaticFeature_Storyline' in str(i) or 'Storyline' in str(i):
                toggle = False
        return movies