import requests
import sys
sys.path.append('.')
from config import RIOT_API_KEY, AVALIABLE_REGIONS


class Match:
    
        @staticmethod
        def get_match_data(region, match_id):
            assert RIOT_API_KEY is not None
            assert isinstance(region, str)
            region = region.lower()
            assert region in AVALIABLE_REGIONS
            url = f'https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={RIOT_API_KEY}'
            r = requests.get(url)
            return r.json()
        
        @staticmethod
        def get_timeline_data(region, match_id):
            assert RIOT_API_KEY is not None
            assert isinstance(region, str)
            region = region.lower()
            assert region in AVALIABLE_REGIONS
            url = f'https://{region}.api.riotgames.com/lol/match/v5/matches/{match_id}/timeline?api_key={RIOT_API_KEY}'
            r = requests.get(url)
            return r.json()
        
        @staticmethod
        def get_matchlist_data(region, puuid):
            assert RIOT_API_KEY is not None
            assert isinstance(region, str)
            region = region.lower()
            assert region in AVALIABLE_REGIONS
            url = f'https://{region}.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start=0&count=20&api_key={RIOT_API_KEY}'
            r = requests.get(url)
            return r.json()
        
if __name__ == '__main__':
    print(Match.get_match_data('americas', 'BR1_2877116734'))
    print(Match.get_timeline_data('americas', 'BR1_2877116734'))
    print(Match.get_matchlist_data('americas', 'wtG_GWPaFRdXdvCYmR6HKZJO70rJ4U6NW3G8M45mQr1h535ZUhdboHkWgaiDbYC_8LWmXjBtbkOuvA'))