from youtube_search import YoutubeSearch
import sys

try:
    pesquisa = YoutubeSearch(sys.argv[1], max_results=1).to_dict()
    url = f"https://youtube.com{pesquisa[0]['url_suffix']}"
    print(url)

except:
    print("Não encontrei nada")
