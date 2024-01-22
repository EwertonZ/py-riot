import requests
import sys
sys.path.append('.')
from config import RIOT_API_KEY, AVALIABLE_REGIONS


class Account:

    @staticmethod
    def get_account_data(region, name, tag):
        assert RIOT_API_KEY is not None
        assert isinstance(region, str)
        region = region.lower()
        assert region in AVALIABLE_REGIONS
        tag = tag.replace('#', '')
        url = f'https://{region}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{name}/{tag}?api_key={RIOT_API_KEY}'
        r = requests.get(url)
        return r.json()

if __name__ == '__main__':
    print(Account.get_account_data('americas', 'O Not', 'BR1'))